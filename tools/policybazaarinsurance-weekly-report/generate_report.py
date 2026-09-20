#!/usr/bin/env python3
"""
Weekly leads + SEO report for policybazaarinsurance.ae.

Reads the latest dated leads export (page-level: enquiry_created_at,
lead_creation_date, referer_url, product_name, ape, status, utm_source —
verified against the real export on 2026-08-24). enquiry_created_at is a form
visit (may never convert); lead_creation_date is an actual lead — "Leads/day"
in this report always means the latter, never the former. Pulls matching
GSC + GA4 windows, and renders a Markdown report (no conversion/booking-rate
metric, per Aakash's 2026-08-24 request — leads and bookings are shown as raw
counts only) comparing:
  - vs the fixed pre-migration baseline (2026-07-12 to 2026-08-10)
  - vs the previous 7 days (week-over-week)

Usage:
    python3 generate_report.py [--as-of YYYY-MM-DD]

Requires the SSL_CERT_FILE workaround on this machine for the Google API calls:
    SSL_CERT_FILE=$(python3 -m certifi) python3 generate_report.py
"""

import argparse
import csv
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

SEO_SCRIPTS = Path.home() / "Documents/PolicyBazaar Claude/.claude/plugins/claude-seo/scripts"
sys.path.insert(0, str(SEO_SCRIPTS))
from google_auth import get_oauth_credentials  # noqa: E402

LEADS_DIR = Path.home() / "Documents/PolicyBazaar Research/PolicyBazaar Insurance/Ranking And Leads"
RESULT_DIR = Path.home() / "Documents/PolicyBazaar Research/PolicyBazaar Insurance/Result"

GSC_PROPERTY = "https://www.policybazaarinsurance.ae/"
GA4_PROPERTY = "366756478"

# Fixed 2026-08-11 platform migration. Baseline window established and verified
# against live GSC/GA4 data on 2026-08-19 (see conversation history) — do not
# recompute this window each run, it is a fixed historical reference point.
MIGRATION_DATE = date(2026, 8, 11)
BASELINE_START = date(2026, 7, 12)
BASELINE_END = date(2026, 8, 10)

LEADS_FILENAME_RE = re.compile(r"^Leads-(\d{4}-\d{2}-\d{2})\.csv$")

# Crawl stats (GSC Settings > Crawl Stats) have no public API — Aakash pastes
# them from the GSC UI export, so this is a manual weekly file drop just like
# the leads CSV. Added 2026-08-24.
CRAWL_FILENAME_RE = re.compile(r"^Crawl-Stats-(\d{4}-\d{2}-\d{2})\.csv$")

# Canonical product labels — these are exactly the product_name values found in
# the real export verified 2026-08-24. Do not rename to the "International X"
# labels used in the 2026-08-19 rollup file; that was a different, coarser
# export and its naming does not appear in this schema.
CANONICAL_PRODUCTS = [
    "Health Insurance",
    "Car Insurance",
    "Travel Insurance",
    "Term Insurance",
    "Income Protection",
    "Investment",
]

DATE_FORMAT = "%B %d, %Y, %I:%M %p"


def classify_url(path: str) -> str:
    """Map a page path to a product bucket, for cross-referencing leads against
    GSC/GA4 page-level data. Verified against real site URLs on 2026-08-19."""
    if "health-insurance" in path:
        return "Health Insurance"
    if "car-insurance" in path:
        return "Car Insurance"
    if "travel-insurance" in path:
        return "Travel Insurance"
    if "income-protection-insurance" in path:
        return "Income Protection"
    if "term-insurance" in path:
        return "Term Insurance"
    if "life-insurance" in path:
        return "Life Insurance (unmapped in CRM)"
    if "investment-plans" in path or "/lic/" in path or "mutual-funds" in path or "/bonds/" in path:
        return "Investment"
    return "Other/Unclassified"


def find_latest_leads_csv():
    candidates = []
    if not LEADS_DIR.exists():
        return None
    for f in LEADS_DIR.glob("Leads-*.csv"):
        m = LEADS_FILENAME_RE.match(f.name)
        if m:
            candidates.append((m.group(1), f))
    if not candidates:
        return None
    candidates.sort()
    return candidates[-1][1]


def find_latest_crawl_csv():
    candidates = []
    if not LEADS_DIR.exists():
        return None
    for f in LEADS_DIR.glob("Crawl-Stats-*.csv"):
        m = CRAWL_FILENAME_RE.match(f.name)
        if m:
            candidates.append((m.group(1), f))
    if not candidates:
        return None
    candidates.sort()
    return candidates[-1][1]


CRAWL_HEADER_ALIASES = {
    "date": "date",
    "Date": "date",
    "total_crawl_requests": "total_crawl_requests",
    "Total crawl requests": "total_crawl_requests",
    "avg_response_time_ms": "avg_response_time_ms",
    "Average response time (ms)": "avg_response_time_ms",
}


def parse_crawl_stats(csv_path: Path):
    """Pasted from the GSC Settings > Crawl Stats UI report (no API for this
    data). Accepts either the snake_case convention
    (date,total_crawl_requests,avg_response_time_ms) or GSC's own raw export
    column labels (Date,Total crawl requests,Average response time (ms)[,
    Total download size (Bytes)]) — headers vary by how Aakash exports/pastes
    each week, both are treated as valid (added 2026-09-07)."""
    with open(csv_path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return {}
    header_map = {h: CRAWL_HEADER_ALIASES[h] for h in rows[0].keys() if h in CRAWL_HEADER_ALIASES}
    required = {"date", "total_crawl_requests", "avg_response_time_ms"}
    found = set(header_map.values())
    if required - found:
        raise ValueError(
            f"crawl stats CSV missing expected columns {required - found}. "
            f"Found columns: {sorted(rows[0].keys())}"
        )
    out = {}
    for r in rows:
        normalized = {header_map[k]: v for k, v in r.items() if k in header_map}
        d = datetime.strptime(normalized["date"], "%Y-%m-%d").date()
        reqs = int(str(normalized["total_crawl_requests"]).replace(",", ""))
        resp = int(str(normalized["avg_response_time_ms"]).replace(",", ""))
        out[d] = (reqs, resp)
    return out


def summarize_crawl(data: dict, start: date, end: date):
    n_days = (end - start).days + 1
    matched_dates = [d for d in data if start <= d <= end]
    reqs = sum(data[d][0] for d in matched_dates)
    wsum = sum(data[d][0] * data[d][1] for d in matched_dates)
    return {
        "n_days_requested": n_days,
        "n_days_with_data": len(matched_dates),
        "requests_per_day": reqs / n_days if n_days else 0,
        "avg_response_ms": (wsum / reqs) if reqs else None,
        "latest_date": max(matched_dates).isoformat() if matched_dates else None,
    }


def check_coverage(summary):
    """When a data source's real coverage in a recent window falls short of
    the window's nominal length (GSC/GA4/crawl stats all lag a few days),
    return (latest_date, missing_days) instead of letting the date caption
    imply full coverage through the window's end date. Returns None when
    coverage is complete. Paired with render_coverage_note() below, which
    collapses every gap found across the report into ONE note at the end
    (collapsed from a per-table note 2026-08-31, Aakash's request — the old
    version repeated near-identical text up to 4x when GSC/GA4/crawl stats
    all lagged the same day)."""
    if summary["n_days_with_data"] >= summary["n_days_requested"]:
        return None
    missing = summary["n_days_requested"] - summary["n_days_with_data"]
    latest = summary.get("latest_date") or "n/a"
    return latest, missing


def render_coverage_note(issues):
    """issues: list of (source_label, window_label, latest, missing) collected
    while rendering. Groups by (source, latest) so e.g. GSC lagging in both
    'This Week' and 'Since Migration' with the same latest date becomes one
    line, not two."""
    if not issues:
        return None
    grouped = {}
    for source, window, latest, _missing in issues:
        key = (source, latest)
        windows = grouped.setdefault(key, [])
        if window not in windows:
            windows.append(window)
    parts = [f"{source} ({' & '.join(windows)}) through {latest}" for (source, latest), windows in grouped.items()]
    return (f"_Data coverage note: {', '.join(parts)} — the most recent day(s) haven't been reported yet. "
            f"This is routine lag, not an error; per-day rates above are still divided by the full window, "
            f"so they read a little low until the rest comes in, never high._")


def parse_leads(csv_path: Path):
    """enquiry_created_at = a visitor reached the form, whether or not they
    completed it. lead_creation_date = an actual lead record was created —
    confirmed 2026-08-24 by Aakash and verified against the real file: all 546
    rows have enquiry_created_at, only 360 (66%) also have lead_creation_date.
    The other 186 are form visits that never became a lead. Do not treat
    enquiry_created_at rows as "leads" — that was this script's bug before
    2026-08-24."""
    with open(csv_path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError(f"leads CSV is empty: {csv_path}")
    required = {"enquiry_created_at", "lead_creation_date", "referer_url", "product_name", "ape", "status"}
    found = set(rows[0].keys())
    missing = required - found
    if missing:
        raise ValueError(
            f"leads CSV missing expected columns {missing}. "
            f"This script expects the page-level export schema (verified 2026-08-24), "
            f"not the daily-rollup schema (product, date: Day, Distinct values of leadid...). "
            f"Found columns: {sorted(found)}"
        )
    parsed = []
    unparseable_enquiry = 0
    unparseable_lead = 0
    for r in rows:
        enquiry_raw = (r["enquiry_created_at"] or "").strip()
        if not enquiry_raw:
            unparseable_enquiry += 1
            continue
        try:
            r["_enquiry_date"] = datetime.strptime(enquiry_raw, DATE_FORMAT).date()
        except ValueError:
            unparseable_enquiry += 1
            continue

        lead_raw = (r["lead_creation_date"] or "").strip()
        r["_lead_date"] = None
        if lead_raw:
            try:
                r["_lead_date"] = datetime.strptime(lead_raw, DATE_FORMAT).date()
            except ValueError:
                unparseable_lead += 1

        parsed.append(r)
    if unparseable_enquiry:
        print(f"WARNING: {unparseable_enquiry}/{len(rows)} rows had an unparseable or blank enquiry_created_at and were skipped entirely.", file=sys.stderr)
    if unparseable_lead:
        print(f"WARNING: {unparseable_lead}/{len(rows)} rows had a lead_creation_date value that failed to parse (treated as no lead).", file=sys.stderr)
    return parsed


def agg_leads(rows, window_start: date, window_end: date):
    """Counts actual leads only (rows with a lead_creation_date in the window)
    — a row with only enquiry_created_at is a form visit, not a lead, and is
    excluded here. Use agg_enquiries() for the form-visit count."""
    by_p = defaultdict(lambda: {"leads": 0, "bookings": 0, "ape": 0.0})
    for r in rows:
        if r["_lead_date"] is None or not (window_start <= r["_lead_date"] <= window_end):
            continue
        p = r["product_name"]
        by_p[p]["leads"] += 1
        if r["status"].strip() == "Sale Complete":
            by_p[p]["bookings"] += 1
            ape_raw = (r["ape"] or "").strip()
            by_p[p]["ape"] += float(ape_raw) if ape_raw else 0.0
    return by_p


def agg_enquiries(rows, window_start: date, window_end: date):
    """Counts every form visit (enquiry_created_at in the window), regardless
    of whether it became a lead."""
    by_p = defaultdict(int)
    for r in rows:
        if not (window_start <= r["_enquiry_date"] <= window_end):
            continue
        by_p[r["product_name"]] += 1
    return by_p


def gsc_daily(start: date, end: date):
    """Shell out to the existing, already-verified gsc_query.py — do not
    reimplement the Search Console API call."""
    cmd = [
        sys.executable, str(SEO_SCRIPTS / "gsc_query.py"),
        "--property", GSC_PROPERTY,
        "--start-date", start.isoformat(),
        "--end-date", end.isoformat(),
        "--dimensions", "date",
        "--json",
    ]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(out.stdout).get("rows", [])


def gsc_page_date(start: date, end: date):
    cmd = [
        sys.executable, str(SEO_SCRIPTS / "gsc_query.py"),
        "--property", GSC_PROPERTY,
        "--start-date", start.isoformat(),
        "--end-date", end.isoformat(),
        "--dimensions", "page,date",
        "--limit", "20000",
        "--json",
    ]
    out = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(out.stdout).get("rows", [])


def _ga4_post(creds, body):
    req = urllib.request.Request(
        f"https://analyticsdata.googleapis.com/v1beta/properties/{GA4_PROPERTY}:runReport",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {creds.token}", "Content-Type": "application/json"},
    )
    try:
        return json.loads(urllib.request.urlopen(req).read().decode())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"GA4 Data API error {e.code}: {e.read().decode()}") from e


def ga4_daily(creds, start: date, end: date):
    body = {
        "dateRanges": [{"startDate": start.isoformat(), "endDate": end.isoformat()}],
        "dimensions": [{"name": "date"}],
        "metrics": [{"name": "sessions"}, {"name": "engagedSessions"}, {"name": "conversions"}],
        "dimensionFilter": {"filter": {"fieldName": "sessionDefaultChannelGroup", "stringFilter": {"value": "Organic Search"}}},
        "orderBys": [{"dimension": {"dimensionName": "date"}}],
        "limit": 400,
    }
    return _ga4_post(creds, body).get("rows", [])


def ga4_page_date(creds, start: date, end: date):
    body = {
        "dateRanges": [{"startDate": start.isoformat(), "endDate": end.isoformat()}],
        "dimensions": [{"name": "landingPage"}, {"name": "date"}],
        "metrics": [{"name": "sessions"}],
        "dimensionFilter": {"filter": {"fieldName": "sessionDefaultChannelGroup", "stringFilter": {"value": "Organic Search"}}},
        "limit": 20000,
    }
    return _ga4_post(creds, body).get("rows", [])


def summarize_gsc(rows, start: date, end: date):
    rows = [r for r in rows if start.isoformat() <= r["date"] <= end.isoformat()]
    n_days = (end - start).days + 1
    clicks = sum(r["clicks"] for r in rows)
    impr = sum(r["impressions"] for r in rows)
    pos = (sum(r["position"] * r["impressions"] for r in rows) / impr) if impr else None
    return {
        "n_days_requested": n_days,
        "n_days_with_data": len(rows),
        "clicks_per_day": clicks / n_days if n_days else 0,
        "impressions_per_day": impr / n_days if n_days else 0,
        "avg_position": pos,
        "latest_date": max((r["date"] for r in rows), default=None),
    }


def summarize_ga4(rows, start: date, end: date):
    def fmt(d):
        return d.strftime("%Y%m%d")
    rows = [r for r in rows if fmt(start) <= r["dimensionValues"][0]["value"] <= fmt(end)]
    n_days = (end - start).days + 1
    sessions = sum(int(r["metricValues"][0]["value"]) for r in rows)
    engaged = sum(int(r["metricValues"][1]["value"]) for r in rows)
    conv = sum(int(r["metricValues"][2]["value"]) for r in rows)
    latest_raw = max((r["dimensionValues"][0]["value"] for r in rows), default=None)
    return {
        "n_days_requested": n_days,
        "n_days_with_data": len(rows),
        "sessions_per_day": sessions / n_days if n_days else 0,
        "engagement_rate": (engaged / sessions * 100) if sessions else None,
        "conversions_per_day": conv / n_days if n_days else 0,
        "latest_date": f"{latest_raw[:4]}-{latest_raw[4:6]}-{latest_raw[6:]}" if latest_raw else None,
    }


def by_product_gsc(page_date_rows, start: date, end: date):
    out = defaultdict(lambda: {"clicks": 0, "impr": 0, "pos_wsum": 0.0})
    for r in page_date_rows:
        page, dt = r["keys"]
        if not (start.isoformat() <= dt <= end.isoformat()):
            continue
        bucket = classify_url(page)
        out[bucket]["clicks"] += r["clicks"]
        out[bucket]["impr"] += r["impressions"]
        out[bucket]["pos_wsum"] += r["position"] * r["impressions"]
    return out


def by_product_ga4(page_date_rows, start: date, end: date):
    def fmt(d):
        return d.strftime("%Y%m%d")
    out = defaultdict(int)
    for r in page_date_rows:
        page = r["dimensionValues"][0]["value"]
        dt = r["dimensionValues"][1]["value"]
        if not (fmt(start) <= dt <= fmt(end)):
            continue
        bucket = classify_url(page)
        out[bucket] += int(r["metricValues"][0]["value"])
    return out


def pct_delta(new, old):
    if old in (0, None) or new is None:
        return None
    return (new - old) / old * 100


def fmt_delta(pct):
    if pct is None:
        return "n/a"
    arrow = "+" if pct >= 0 else ""
    return f"{arrow}{pct:.0f}%"


def verdict_arrow(before, after, higher_is_better=True, flat_pct=5.0):
    """Directional verdict comparing a 'before' value (baseline / pre-migration)
    to an 'after' value (this week / since migration). higher_is_better=False
    for metrics where a smaller number is the good outcome (position, response
    time). Within flat_pct of no change is reported as flat rather than a
    false-precision improved/declined call."""
    if before is None or after is None:
        return "n/a"
    if before == 0:
        if after == 0:
            return "➖ Flat"
        return "▲ Improved" if higher_is_better else "▼ Declined"
    pct = (after - before) / before * 100
    if abs(pct) < flat_pct:
        return "➖ Flat"
    improved = (pct > 0) == higher_is_better
    return "▲ Improved" if improved else "▼ Declined"


def fmt_range(start: date, end: date) -> str:
    """Human-readable date range for a table caption, e.g. 'Aug 11–23, 2026'
    or 'Jul 12–Aug 10, 2026' when the range crosses a month."""
    if start.year != end.year:
        return f"{start.strftime('%b %d, %Y')}–{end.strftime('%b %d, %Y')}"
    if start.month != end.month:
        return f"{start.strftime('%b %d')}–{end.strftime('%b %d, %Y')}"
    return f"{start.strftime('%b %d')}–{end.strftime('%d, %Y')}"


def render_report_markdown(as_of: date, leads_path: Path, leads_rows, gsc_daily_rows, gsc_pagedate_rows, ga4_daily_rows, ga4_pagedate_rows, crawl_data=None, crawl_path=None):
    # Anchored on enquiry_created_at (always populated) rather than
    # lead_creation_date, so the window reflects the file's true coverage —
    # not the shrunken window of rows that happened to convert to a lead.
    leads_latest_date = max(r["_enquiry_date"] for r in leads_rows)
    leads_earliest_date = min(r["_enquiry_date"] for r in leads_rows)
    wow_end = leads_latest_date
    wow_start = wow_end - timedelta(days=6)
    prev_wow_end = wow_start - timedelta(days=1)
    prev_wow_start = prev_wow_end - timedelta(days=6)

    since_migration_start = MIGRATION_DATE
    since_migration_end = leads_latest_date
    has_post_migration_leads = leads_latest_date > MIGRATION_DATE

    leads_baseline = agg_leads(leads_rows, BASELINE_START, BASELINE_END)
    leads_since_migration = agg_leads(leads_rows, since_migration_start, since_migration_end) if has_post_migration_leads else {}
    leads_wow = agg_leads(leads_rows, wow_start, wow_end)
    leads_prev_wow = agg_leads(leads_rows, prev_wow_start, prev_wow_end)

    enquiries_baseline = agg_enquiries(leads_rows, BASELINE_START, BASELINE_END)
    enquiries_since_migration = agg_enquiries(leads_rows, since_migration_start, since_migration_end) if has_post_migration_leads else {}

    n_baseline_days = (BASELINE_END - BASELINE_START).days + 1
    n_since_migration_days = max((since_migration_end - since_migration_start).days + 1, 1)
    n_wow_days = (wow_end - wow_start).days + 1
    n_prev_wow_days = (prev_wow_end - prev_wow_start).days + 1

    def total_leads_per_day(agg, n_days):
        return sum(v["leads"] for v in agg.values()) / n_days if n_days else 0

    def total_bookings(agg):
        return sum(v["bookings"] for v in agg.values())

    def total_leads(agg):
        return sum(v["leads"] for v in agg.values())

    base_lpd = total_leads_per_day(leads_baseline, n_baseline_days)
    since_lpd = total_leads_per_day(leads_since_migration, n_since_migration_days) if has_post_migration_leads else None
    wow_lpd = total_leads_per_day(leads_wow, n_wow_days)
    prevwow_lpd = total_leads_per_day(leads_prev_wow, n_prev_wow_days)

    gsc_baseline = summarize_gsc(gsc_daily_rows, BASELINE_START, BASELINE_END)
    gsc_since = summarize_gsc(gsc_daily_rows, since_migration_start, since_migration_end)
    gsc_wow = summarize_gsc(gsc_daily_rows, wow_start, wow_end)
    gsc_prevwow = summarize_gsc(gsc_daily_rows, prev_wow_start, prev_wow_end)

    ga4_baseline = summarize_ga4(ga4_daily_rows, BASELINE_START, BASELINE_END)
    ga4_since = summarize_ga4(ga4_daily_rows, since_migration_start, since_migration_end)
    ga4_wow = summarize_ga4(ga4_daily_rows, wow_start, wow_end)
    ga4_prevwow = summarize_ga4(ga4_daily_rows, prev_wow_start, prev_wow_end)

    gsc_prod_baseline = by_product_gsc(gsc_pagedate_rows, BASELINE_START, BASELINE_END)
    gsc_prod_since = by_product_gsc(gsc_pagedate_rows, since_migration_start, since_migration_end)
    ga4_prod_baseline = by_product_ga4(ga4_pagedate_rows, BASELINE_START, BASELINE_END)
    ga4_prod_since = by_product_ga4(ga4_pagedate_rows, since_migration_start, since_migration_end)
    n_ga4_baseline_days = (BASELINE_END - BASELINE_START).days + 1
    n_ga4_since_days = max((since_migration_end - since_migration_start).days + 1, 1)

    gsc_wow_ctr = (gsc_wow["clicks_per_day"] / gsc_wow["impressions_per_day"] * 100) if gsc_wow["impressions_per_day"] else None
    gsc_prevwow_ctr = (gsc_prevwow["clicks_per_day"] / gsc_prevwow["impressions_per_day"] * 100) if gsc_prevwow["impressions_per_day"] else None
    gsc_baseline_ctr = (gsc_baseline["clicks_per_day"] / gsc_baseline["impressions_per_day"] * 100) if gsc_baseline["impressions_per_day"] else None

    def md_row(label, this_w, last_w, base, fmt="{:.2f}", higher_is_better=True):
        def s(v):
            return fmt.format(v) if v is not None else "n/a"
        v = verdict_arrow(base, this_w, higher_is_better)
        return f"| {label} | {s(this_w)} | {s(last_w)} | {s(base)} | {v} |"

    coverage_issues = []

    def record_coverage(source_label, summary, window_label):
        if summary is None:
            return
        result = check_coverage(summary)
        if result is None:
            return
        latest, missing = result
        coverage_issues.append((source_label, window_label, latest, missing))

    lines = []
    lines.append(f"# PolicyBazaar Insurance — Weekly Migration & Leads Report")
    lines.append("")
    lines.append(f"**Subject:** PolicyBazaar Insurance — Weekly Migration & Leads Report — "
                  f"Week of {wow_start.strftime('%b %d')}–{wow_end.strftime('%b %d, %Y')}  ")
    lines.append("")
    lines.append(f"**Data as of:** {as_of.isoformat()}  ")
    lines.append(f"**Migration go-live:** {MIGRATION_DATE.isoformat()} &nbsp;|&nbsp; **Days since go-live:** {(leads_latest_date - MIGRATION_DATE).days}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Overall Metrics")
    lines.append("")
    lines.append(f"**This Week:** {fmt_range(wow_start, wow_end)} &nbsp;|&nbsp; "
                  f"**Last Week:** {fmt_range(prev_wow_start, prev_wow_end)} &nbsp;|&nbsp; "
                  f"**Baseline:** {fmt_range(BASELINE_START, BASELINE_END)}")
    lines.append("")
    lines.append("| Metric | This Week | Last Week | Baseline | Verdict (Baseline → This Week) |")
    lines.append("|---|---:|---:|---:|---|")
    lines.append(md_row("Leads/day", wow_lpd, prevwow_lpd, base_lpd))
    lines.append(md_row("Bookings/day", total_bookings(leads_wow)/n_wow_days, total_bookings(leads_prev_wow)/n_prev_wow_days, total_bookings(leads_baseline)/n_baseline_days))
    lines.append(md_row("GSC Clicks/day", gsc_wow["clicks_per_day"], gsc_prevwow["clicks_per_day"], gsc_baseline["clicks_per_day"]))
    lines.append(md_row("GSC Impressions/day", gsc_wow["impressions_per_day"], gsc_prevwow["impressions_per_day"], gsc_baseline["impressions_per_day"], fmt="{:.0f}"))
    lines.append(md_row("GSC Avg Position", gsc_wow["avg_position"], gsc_prevwow["avg_position"], gsc_baseline["avg_position"], fmt="{:.1f}", higher_is_better=False))
    lines.append(md_row("GSC CTR", gsc_wow_ctr, gsc_prevwow_ctr, gsc_baseline_ctr, fmt="{:.2f}%"))
    lines.append(md_row("GA4 Sessions/day", ga4_wow["sessions_per_day"], ga4_prevwow["sessions_per_day"], ga4_baseline["sessions_per_day"]))
    lines.append(md_row("GA4 Engagement %", ga4_wow["engagement_rate"], ga4_prevwow["engagement_rate"], ga4_baseline["engagement_rate"], fmt="{:.1f}%"))
    lines.append("")
    lines.append(f"**WoW change:** leads {fmt_delta(pct_delta(wow_lpd, prevwow_lpd))}, GSC clicks {fmt_delta(pct_delta(gsc_wow['clicks_per_day'], gsc_prevwow['clicks_per_day']))}, "
                  f"GA4 sessions {fmt_delta(pct_delta(ga4_wow['sessions_per_day'], ga4_prevwow['sessions_per_day']))}  ")
    lines.append(f"**vs baseline:** leads {fmt_delta(pct_delta(wow_lpd, base_lpd))}, GSC clicks {fmt_delta(pct_delta(gsc_wow['clicks_per_day'], gsc_baseline['clicks_per_day']))}, "
                  f"GA4 sessions {fmt_delta(pct_delta(ga4_wow['sessions_per_day'], ga4_baseline['sessions_per_day']))}")
    lines.append("")
    record_coverage("GSC", gsc_wow, "This Week")
    record_coverage("GA4", ga4_wow, "This Week")

    since_label = "since migration" if has_post_migration_leads else "since migration (n/a, no post-migration rows yet)"

    lines.append("## Crawl Stats (Search Console)")
    lines.append("")
    if crawl_data:
        crawl_since_end = since_migration_end
        crawl_wow = summarize_crawl(crawl_data, wow_start, wow_end)
        crawl_prevwow = summarize_crawl(crawl_data, prev_wow_start, prev_wow_end)
        crawl_baseline = summarize_crawl(crawl_data, BASELINE_START, BASELINE_END)
        crawl_since = summarize_crawl(crawl_data, since_migration_start, crawl_since_end) if has_post_migration_leads else None
        lines.append(f"**This Week:** {fmt_range(wow_start, wow_end)} &nbsp;|&nbsp; "
                      f"**Last Week:** {fmt_range(prev_wow_start, prev_wow_end)} &nbsp;|&nbsp; "
                      f"**Baseline:** {fmt_range(BASELINE_START, BASELINE_END)} &nbsp;|&nbsp; "
                      f"**Since Migration:** {fmt_range(since_migration_start, crawl_since_end)}")
        lines.append("")
        lines.append("| Metric | This Week | Last Week | Baseline | Since Migration | Verdict (Baseline → Since Migration) |")
        lines.append("|---|---:|---:|---:|---:|---|")

        def s2(v, fmt="{:.2f}"):
            return fmt.format(v) if v is not None else "n/a"

        since_reqs = crawl_since["requests_per_day"] if crawl_since else None
        since_resp = crawl_since["avg_response_ms"] if crawl_since else None
        lines.append(f"| Crawl Requests/day | {s2(crawl_wow['requests_per_day'])} | {s2(crawl_prevwow['requests_per_day'])} | "
                      f"{s2(crawl_baseline['requests_per_day'])} | {s2(since_reqs)} | "
                      f"{verdict_arrow(crawl_baseline['requests_per_day'], since_reqs, higher_is_better=True)} |")
        lines.append(f"| Avg Response Time (ms) | {s2(crawl_wow['avg_response_ms'], '{:.0f}')} | {s2(crawl_prevwow['avg_response_ms'], '{:.0f}')} | "
                      f"{s2(crawl_baseline['avg_response_ms'], '{:.0f}')} | {s2(since_resp, '{:.0f}')} | "
                      f"{verdict_arrow(crawl_baseline['avg_response_ms'], since_resp, higher_is_better=False)} |")
        lines.append("")
        record_coverage("Crawl Stats", crawl_wow, "This Week")
        record_coverage("Crawl Stats", crawl_since, "Since Migration")
    else:
        lines.append(f"_No `Crawl-Stats-YYYY-MM-DD.csv` found in {LEADS_DIR} — section skipped this week. "
                      f"Drop the latest GSC Settings > Crawl Stats export there to include it._")
        lines.append("")

    total_enq_base = sum(enquiries_baseline.values())
    total_enq_since = sum(enquiries_since_migration.values()) if has_post_migration_leads else None
    total_lead_base = total_leads(leads_baseline)
    total_lead_since = total_leads(leads_since_migration) if has_post_migration_leads else None
    enq_base_pd = total_enq_base / n_baseline_days
    enq_since_pd = (total_enq_since / n_since_migration_days) if has_post_migration_leads else None
    lead_base_pd = total_lead_base / n_baseline_days
    lead_since_pd = (total_lead_since / n_since_migration_days) if has_post_migration_leads else None

    lines.append(f"## Enquiries vs Leads — Funnel, baseline → {since_label}")
    lines.append("")
    lines.append(f"**Baseline:** {fmt_range(BASELINE_START, BASELINE_END)} &nbsp;|&nbsp; "
                  f"**Since Migration:** {fmt_range(since_migration_start, since_migration_end)}")
    lines.append("")
    lines.append("| Metric | Baseline/day | Since Migration/day | Change | Verdict |")
    lines.append("|---|---:|---:|---:|---|")
    enq_since_pd_s = f"{enq_since_pd:.2f}" if enq_since_pd is not None else "n/a"
    enq_delta_s = fmt_delta(pct_delta(enq_since_pd, enq_base_pd)) if enq_since_pd is not None else "n/a"
    lines.append(f"| Enquiries (form visits) | {enq_base_pd:.2f} | {enq_since_pd_s} | {enq_delta_s} | "
                 f"{verdict_arrow(enq_base_pd, enq_since_pd, higher_is_better=True)} |")
    lines.append(f"| Leads (actual) | {lead_base_pd:.2f} | {f'{lead_since_pd:.2f}' if lead_since_pd is not None else 'n/a'} | "
                 f"{fmt_delta(pct_delta(lead_since_pd, lead_base_pd)) if lead_since_pd is not None else 'n/a'} | "
                 f"{verdict_arrow(lead_base_pd, lead_since_pd, higher_is_better=True)} |")
    if total_enq_base and total_lead_base is not None:
        completion_base = total_lead_base / total_enq_base * 100
    else:
        completion_base = None
    if has_post_migration_leads and total_enq_since:
        completion_since = total_lead_since / total_enq_since * 100
    else:
        completion_since = None
    cb_s = f"{completion_base:.1f}%" if completion_base is not None else "n/a"
    cs_s = f"{completion_since:.1f}%" if completion_since is not None else "n/a"
    lines.append(f"| Form completion rate (lead ÷ enquiry) | {cb_s} | {cs_s} | n/a | "
                 f"{verdict_arrow(completion_base, completion_since, higher_is_better=True)} |")
    lines.append("")
    if enq_since_pd is not None:
        enq_dir = "rose" if enq_since_pd > enq_base_pd else ("dropped" if enq_since_pd < enq_base_pd else "held steady")
        lines.append(f"- Enquiries (form visits) **{enq_dir}** since migration: {enq_base_pd:.2f}/day → {enq_since_pd:.2f}/day ({fmt_delta(pct_delta(enq_since_pd, enq_base_pd))}).")
    if lead_since_pd is not None:
        lead_dir = "rose" if lead_since_pd > lead_base_pd else ("dropped" if lead_since_pd < lead_base_pd else "held steady")
        lines.append(f"- Leads (actual) **{lead_dir}** since migration: {lead_base_pd:.2f}/day → {lead_since_pd:.2f}/day ({fmt_delta(pct_delta(lead_since_pd, lead_base_pd))}).")
    if not has_post_migration_leads:
        lines.append("- No post-migration rows yet — this comparison isn't possible this week.")
    lines.append("")

    lines.append(f"## By Product — Leads (baseline → {since_label})")
    lines.append("")
    lines.append(f"**Baseline:** {fmt_range(BASELINE_START, BASELINE_END)} &nbsp;|&nbsp; "
                  f"**Since Migration:** {fmt_range(since_migration_start, since_migration_end)}")
    lines.append("")
    lines.append("| Product | Leads/day (Baseline → Since Migration) | Verdict |")
    lines.append("|---|---|---|")
    prod_gsc = {}
    prod_ga4 = {}
    for p in CANONICAL_PRODUCTS:
        b = leads_baseline.get(p, {"leads": 0, "bookings": 0})
        s = (leads_since_migration or {}).get(p, {"leads": 0, "bookings": 0})
        b_lpd = b["leads"] / n_baseline_days
        s_lpd = (s["leads"] / n_since_migration_days) if has_post_migration_leads else None
        s_lpd_s = f"{s_lpd:.2f}" if s_lpd is not None else "n/a"
        lines.append(f"| {p} | {b_lpd:.2f} → {s_lpd_s} | {verdict_arrow(b_lpd, s_lpd, higher_is_better=True)} |")

        gb = gsc_prod_baseline.get(p, {"clicks": 0, "impr": 0, "pos_wsum": 0})
        gs = gsc_prod_since.get(p, {"clicks": 0, "impr": 0, "pos_wsum": 0})
        prod_gsc[p] = (gb, gs)
        prod_ga4[p] = (ga4_prod_baseline.get(p, 0), ga4_prod_since.get(p, 0))
    lines.append("")

    lines.append(f"## By Product — GSC (baseline → {since_label})")
    lines.append("")
    lines.append(f"**Baseline:** {fmt_range(BASELINE_START, BASELINE_END)} &nbsp;|&nbsp; "
                  f"**Since Migration:** {fmt_range(since_migration_start, since_migration_end)}")
    lines.append("")
    lines.append("| Product | Clicks/day | Impressions/day | Avg Position | Verdict (Clicks / Position) |")
    lines.append("|---|---|---|---|---|")
    for p in CANONICAL_PRODUCTS:
        gb, gs = prod_gsc[p]
        gb_pos = (gb["pos_wsum"] / gb["impr"]) if gb["impr"] else None
        gs_pos = (gs["pos_wsum"] / gs["impr"]) if gs["impr"] else None
        gb_clicks_d, gs_clicks_d = gb["clicks"] / n_baseline_days, gs["clicks"] / n_since_migration_days
        gb_impr_d, gs_impr_d = gb["impr"] / n_baseline_days, gs["impr"] / n_since_migration_days
        gb_pos_s = f"{gb_pos:.0f}" if gb_pos is not None else "n/a"
        gs_pos_s = f"{gs_pos:.0f}" if gs_pos is not None else "n/a"
        clicks_v = verdict_arrow(gb_clicks_d, gs_clicks_d, higher_is_better=True)
        pos_v = verdict_arrow(gb_pos, gs_pos, higher_is_better=False)
        lines.append(f"| {p} | {gb_clicks_d:.2f} → {gs_clicks_d:.2f} | {gb_impr_d:.0f} → {gs_impr_d:.0f} | {gb_pos_s} → {gs_pos_s} | {clicks_v} / {pos_v} |")
    lines.append("")
    record_coverage("GSC", gsc_since, "Since Migration")

    lines.append(f"## By Product — GA4 Organic Sessions/day (baseline → {since_label})")
    lines.append("")
    lines.append(f"**Baseline:** {fmt_range(BASELINE_START, BASELINE_END)} &nbsp;|&nbsp; "
                  f"**Since Migration:** {fmt_range(since_migration_start, since_migration_end)}")
    lines.append("")
    lines.append("| Product | Sessions/day (Baseline → Since Migration) | Verdict |")
    lines.append("|---|---|---|")
    for p in CANONICAL_PRODUCTS:
        ga_b_total, ga_s_total = prod_ga4[p]
        ga_b = ga_b_total / n_ga4_baseline_days
        ga_s = ga_s_total / n_ga4_since_days
        lines.append(f"| {p} | {ga_b:.2f} → {ga_s:.2f} | {verdict_arrow(ga_b, ga_s, higher_is_better=True)} |")
    lines.append("")
    record_coverage("GA4", ga4_since, "Since Migration")
    lines.append("## Notes")
    lines.append("")
    lines.append("- Product buckets come directly from the leads file's `product_name` column (Health/Car/Travel/Term/Income Protection/Investment).")
    lines.append("- GSC \"Investment\" groups `/investment-plans/`, `/lic/`, `/mutual-funds/`, `/bonds/` pages (site splits this 4 ways; CRM tracks it as one product).")
    lines.append("- The site also has a `/life-insurance/` section with real traffic that does not map to any of the 6 CRM products — excluded here.")
    lines.append("- GSC position numbers with low impression counts are noisy — a single-digit-impression window is not reliable, check the raw pull if a product's position swings wildly.")
    lines.append("- Crawl Stats has no public API — it's pasted from the GSC Settings > Crawl Stats UI report into a `Crawl-Stats-YYYY-MM-DD.csv` drop, same convention as the leads file.")
    lines.append("")
    coverage_note_line = render_coverage_note(coverage_issues)
    if coverage_note_line:
        lines.append(coverage_note_line)
        lines.append("")
    lines.append("---")
    lines.append("")
    crawl_source = f" Crawl stats source: `{crawl_path}`." if crawl_path else " Crawl stats: none found this week."
    lines.append(f"*Full underlying data: GSC/GA4 pulls for {BASELINE_START} to {as_of}. Leads source: `{leads_path}`.{crawl_source}*")

    return "\n".join(l for l in lines if l is not None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--as-of", type=str, default=None, help="Override 'today' for testing (YYYY-MM-DD)")
    args = ap.parse_args()
    as_of = datetime.strptime(args.as_of, "%Y-%m-%d").date() if args.as_of else date.today()

    leads_path = find_latest_leads_csv()
    if leads_path is None:
        print(f"ERROR: no Leads-YYYY-MM-DD.csv found in {LEADS_DIR}", file=sys.stderr)
        sys.exit(1)

    leads_rows = parse_leads(leads_path)

    crawl_path = find_latest_crawl_csv()
    crawl_data = parse_crawl_stats(crawl_path) if crawl_path else None
    if crawl_path is None:
        print(f"WARNING: no Crawl-Stats-YYYY-MM-DD.csv found in {LEADS_DIR} — Crawl Stats section will be skipped.", file=sys.stderr)

    gsc_start = BASELINE_START
    gsc_end = as_of

    gsc_d_rows = gsc_daily(gsc_start, gsc_end)
    gsc_pd_rows = gsc_page_date(gsc_start, gsc_end)

    creds = get_oauth_credentials(["https://www.googleapis.com/auth/analytics.readonly"])
    ga4_d_rows = ga4_daily(creds, gsc_start, gsc_end)
    ga4_pd_rows = ga4_page_date(creds, gsc_start, gsc_end)

    report = render_report_markdown(as_of, leads_path, leads_rows, gsc_d_rows, gsc_pd_rows, ga4_d_rows, ga4_pd_rows, crawl_data, crawl_path)

    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    leads_latest_date = max(r["_enquiry_date"] for r in leads_rows)
    out_path = RESULT_DIR / f"weekly-report-{leads_latest_date.isoformat()}.md"
    out_path.write_text(report, encoding="utf-8")

    print(report)
    print(f"\n[saved to {out_path}]", file=sys.stderr)


if __name__ == "__main__":
    main()
