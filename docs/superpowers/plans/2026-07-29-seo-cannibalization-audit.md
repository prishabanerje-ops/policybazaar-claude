# SEO Keyword Cannibalization Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `seo-cannibalization` sub-skill: detect keyword cannibalization
across PolicyBazaar UAE's Health and Travel Insurance verticals by cross-referencing
GSC, GA4, SEMrush position tracking, and leads data, and produce a prioritised Excel
report — then run it once against real production data to deliver the report Aakash
asked for.

**Architecture:** Two new Python scripts (`cannibalization_correlate.py` for
detection/scoring, `cannibalization_report.py` for the Excel writer) added to the
existing `claude-seo` plugin, following its established script conventions (argparse,
JSON I/O, pytest unit tests). A new `seo-cannibalization/SKILL.md` orchestrates them,
mirroring `seo-leads-intel`'s phase structure. Wired into the `uae-insurance` hub.

**Tech Stack:** Python 3 (stdlib + `openpyxl`, already a pinned dependency), pytest,
existing `claude-seo` scripts (`gsc_query.py`, `ga4_report.py`, `semrush_import.py`,
`leads_import.py`, `fetch_page.py`, `parse_html.py`) reused unmodified.

## Global Constraints

- Spec: `docs/superpowers/specs/2026-07-29-seo-cannibalization-audit-design.md` — every requirement in it must map to a task below.
- Scope: Health + Travel Insurance only (v1) — no other verticals.
- Time window: 12 months trailing GSC pull.
- Flagging threshold: ≥2 distinct URLs each with ≥10 impressions for the same in-scope query.
- High-severity escalation: competitor URL has ≥1 click, OR SEMrush landing URL churned ≥2 times.
- In-scope query rule: matches the vertical's `$VERTICAL_ENTITIES`/`$VERTICAL_INTENTS` taxonomy (`skills/seo-insurance-ae/SKILL.md`, Vertical 2 = Health, Vertical 3 = Travel) OR is in that vertical's SEMrush tracked list.
- Output: one combined workbook, 5 sheets, at `PolicyBazaar Research/Cannibalization/Result/cannibalization-report-{date}.xlsx`.
- All new Python files live under `.claude/plugins/claude-seo/` (scripts/, tests/, skills/) — this is a separate git repo from the main workspace; commits happen there, not in the parent `PolicyBazaar Claude` repo.
- No new dependency beyond what's already pinned (`openpyxl>=3.1.5,<4.0.0` in `requirements.txt` — already installed and used by no other script yet, so this is its first real usage).
- Follow this plugin's existing Python conventions exactly (docstring + `argparse` + `--json` flag CLI pattern, `from scripts.module import func` test import style) rather than the parent repo's generic TypeScript-oriented style rules, which don't apply to this Python codebase.

---

## Task 1: `cannibalization_correlate.py` — normalization & indexing helpers

**Files:**
- Create: `.claude/plugins/claude-seo/scripts/cannibalization_correlate.py`
- Test: `.claude/plugins/claude-seo/tests/test_cannibalization_correlate.py`

**Interfaces:**
- Consumes: nothing new — reads raw dicts matching `gsc_query.py`, `semrush_import.py`, `ga4_report.py --report top-pages`, and `leads_import.py`'s existing JSON output shapes (all already stable, unmodified).
- Produces (for Task 2 in the same file, and Task 3's report generator):
  - `normalize_path(url_or_path: str) -> str`
  - `build_gsc_query_index(gsc_data: dict) -> dict` → `{query: [{"page", "clicks", "impressions", "position"}, ...]}`
  - `build_semrush_lookup(semrush_keywords: list) -> tuple[dict, set]` → `(keyword_lower -> keyword_dict, set_of_tracked_keyword_strings)`
  - `compute_landing_churn(snapshots: dict) -> int`
  - `build_ga4_lookup(ga4_data: dict) -> dict` → `{path: {"sessions", "bounce_rate"}}`
  - `build_leads_lookup(leads_data: list) -> dict` → `{path: leads_total_int}`

- [ ] **Step 1: Write the failing tests**

Create `.claude/plugins/claude-seo/tests/test_cannibalization_correlate.py`:

```python
"""Tests for scripts/cannibalization_correlate.py"""

from scripts.cannibalization_correlate import (
    normalize_path,
    build_gsc_query_index,
    build_semrush_lookup,
    compute_landing_churn,
    build_ga4_lookup,
    build_leads_lookup,
)


# ── normalize_path ──────────────────────────────────────────────────────────

def test_normalize_path_full_url_strips_domain_adds_trailing_slash():
    assert normalize_path("https://www.policybazaar.ae/health-insurance") == "/health-insurance/"


def test_normalize_path_bare_path_without_trailing_slash():
    assert normalize_path("/car-insurance/buy-insurance") == "/car-insurance/buy-insurance/"


def test_normalize_path_already_normalized_unchanged():
    assert normalize_path("/health-insurance/") == "/health-insurance/"


def test_normalize_path_empty_string_returns_empty():
    assert normalize_path("") == ""


def test_normalize_path_root_url():
    assert normalize_path("https://www.policybazaar.ae/") == "/"


# ── build_gsc_query_index ────────────────────────────────────────────────────

def test_build_gsc_query_index_groups_rows_by_query():
    gsc_data = {
        "rows": [
            {"query": "compare health insurance uae", "page": "https://www.policybazaar.ae/health-insurance/", "clicks": 40, "impressions": 500, "position": 3.2},
            {"query": "compare health insurance uae", "page": "https://www.policybazaar.ae/", "clicks": 5, "impressions": 200, "position": 6.1},
            {"query": "best health insurance uae", "page": "https://www.policybazaar.ae/health-insurance/", "clicks": 20, "impressions": 300, "position": 2.0},
        ]
    }
    index = build_gsc_query_index(gsc_data)
    assert len(index["compare health insurance uae"]) == 2
    assert len(index["best health insurance uae"]) == 1
    assert index["compare health insurance uae"][0]["page"] == "/health-insurance/"


def test_build_gsc_query_index_skips_rows_missing_query_or_page():
    gsc_data = {"rows": [{"query": "", "page": "https://www.policybazaar.ae/", "clicks": 1, "impressions": 1, "position": 1.0}]}
    index = build_gsc_query_index(gsc_data)
    assert index == {}


# ── build_semrush_lookup ─────────────────────────────────────────────────────

def test_build_semrush_lookup_keys_by_lowercase_keyword():
    keywords = [{"keyword": "Compare Health Insurance UAE", "snapshots": {}}]
    lookup, tracked = build_semrush_lookup(keywords)
    assert "compare health insurance uae" in lookup
    assert tracked == {"compare health insurance uae"}


def test_build_semrush_lookup_empty_list():
    lookup, tracked = build_semrush_lookup([])
    assert lookup == {} and tracked == set()


# ── compute_landing_churn ────────────────────────────────────────────────────

def test_compute_landing_churn_counts_switches_chronologically():
    snapshots = {
        "2026-01-15": {"landing": "https://www.policybazaar.ae/health-insurance/"},
        "2026-01-01": {"landing": "https://www.policybazaar.ae/health-insurance/"},
        "2026-01-08": {"landing": "https://www.policybazaar.ae/"},
    }
    # chronological order: 01-01 (health-insurance), 01-08 (/), 01-15 (health-insurance) → 2 switches
    assert compute_landing_churn(snapshots) == 2


def test_compute_landing_churn_stable_history_is_zero():
    snapshots = {
        "2026-01-01": {"landing": "https://www.policybazaar.ae/health-insurance/"},
        "2026-01-08": {"landing": "https://www.policybazaar.ae/health-insurance/"},
    }
    assert compute_landing_churn(snapshots) == 0


def test_compute_landing_churn_ignores_null_landings():
    snapshots = {
        "2026-01-01": {"landing": None},
        "2026-01-08": {"landing": "https://www.policybazaar.ae/health-insurance/"},
    }
    assert compute_landing_churn(snapshots) == 0


# ── build_ga4_lookup ──────────────────────────────────────────────────────────

def test_build_ga4_lookup_normalizes_paths():
    ga4_data = {"pages": [{"landing_page": "/car-insurance/buy-insurance", "sessions": 164, "bounce_rate": 25.0}]}
    lookup = build_ga4_lookup(ga4_data)
    assert lookup["/car-insurance/buy-insurance/"] == {"sessions": 164, "bounce_rate": 25.0}


def test_build_ga4_lookup_empty_pages():
    assert build_ga4_lookup({"pages": []}) == {}


# ── build_leads_lookup ────────────────────────────────────────────────────────

def test_build_leads_lookup_sums_across_verticals():
    leads_data = [
        {"vertical": "health", "pages": [{"path": "/health-insurance/", "leads_total": 15}]},
        {"vertical": "travel", "pages": [{"path": "/travel-insurance/", "leads_total": 8}]},
    ]
    lookup = build_leads_lookup(leads_data)
    assert lookup["/health-insurance/"] == 15
    assert lookup["/travel-insurance/"] == 8


def test_build_leads_lookup_ignores_non_dict_entries():
    assert build_leads_lookup(["not a dict"]) == {}
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `cd .claude/plugins/claude-seo && python -m pytest tests/test_cannibalization_correlate.py -v`
Expected: FAIL/ERROR — `ModuleNotFoundError: No module named 'scripts.cannibalization_correlate'` (the file doesn't exist yet).

- [ ] **Step 3: Write the minimal implementation**

Create `.claude/plugins/claude-seo/scripts/cannibalization_correlate.py`:

```python
#!/usr/bin/env python3
"""
Detect keyword cannibalization by cross-referencing GSC query/page overlap with
SEMrush landing-URL churn, GA4 engagement, and leads data.

Reads JSON output from gsc_query.py (dimensions=query,page), semrush_import.py,
leads_import.py, and ga4_report.py (--report top-pages). Flags queries where 2+
distinct site URLs both receive real search impressions, scores severity, and
classifies a recommended action per pair.

Usage:
    python cannibalization_correlate.py \\
      --gsc gsc.json \\
      --semrush semrush_health.json,semrush_travel.json \\
      --leads leads_health.json,leads_travel.json \\
      --ga4 ga4.json \\
      --min-impressions 10 \\
      --json
"""

import argparse
import json
import sys
from collections import defaultdict
from urllib.parse import urlparse

# Query-scoping stems, sourced from skills/seo-insurance-ae/SKILL.md's
# $VERTICAL_INTENTS for Vertical 2 (Health) and Vertical 3 (Travel). Keep these in
# sync if that reference table changes — they define this audit's v1 scope
# (Health + Travel only; see design doc's Non-goals).
HEALTH_STEMS = [
    "health insurance", "medical insurance", "mandatory health insurance",
    "health insurance for uae visa", "best health insurance", "cheapest health insurance",
    "family health insurance", "health insurance for expats", "maternity health insurance",
    "dental health insurance", "claim health insurance", "health insurance renewal",
    "health insurance for domestic workers", "health insurance network hospitals",
]

TRAVEL_STEMS = [
    "travel insurance", "travel medical insurance", "travel insurance for schengen visa",
    "best travel insurance", "cheap travel insurance", "annual travel insurance",
    "travel insurance for us visa", "family travel insurance",
    "travel insurance adventure sports", "travel insurance for senior citizens",
    "travel insurance pre-existing conditions", "cancel for any reason travel insurance",
    "travel insurance for expats", "travel insurance medical cover",
]

MIN_IMPRESSIONS_DEFAULT = 10
HIGH_SEVERITY_CLICK_THRESHOLD = 1
HIGH_SEVERITY_CHURN_THRESHOLD = 2


def normalize_path(url_or_path: str) -> str:
    """Normalize a GSC/GA4/SEMrush/leads URL or bare path to a trailing-slash path key."""
    if not url_or_path:
        return ""
    path = urlparse(url_or_path).path if "://" in url_or_path else url_or_path
    if not path:
        path = "/"
    if not path.endswith("/"):
        path += "/"
    return path


def build_gsc_query_index(gsc_data: dict) -> dict:
    """Build {query: [{page, clicks, impressions, position}, ...]} from gsc_query.py
    JSON (expects dimensions=query,page)."""
    index: dict = defaultdict(list)
    for row in gsc_data.get("rows", []):
        query = (row.get("query") or "").strip()
        page = (row.get("page") or "").strip()
        if not query or not page:
            continue
        index[query].append({
            "page": normalize_path(page),
            "clicks": row.get("clicks", 0) or 0,
            "impressions": row.get("impressions", 0) or 0,
            "position": row.get("position", 0) or 0,
        })
    return dict(index)


def build_semrush_lookup(semrush_keywords: list) -> tuple:
    """Build ({keyword_lower: keyword_dict}, {tracked keyword strings}) from
    semrush_import.py's flat keyword list."""
    lookup = {}
    for kw in semrush_keywords:
        text = (kw.get("keyword") or "").strip().lower()
        if text:
            lookup[text] = kw
    return lookup, set(lookup.keys())


def compute_landing_churn(snapshots: dict) -> int:
    """Count landing-URL changes across the tracked history, in chronological order."""
    dated = sorted(snapshots.items())
    landings = [normalize_path(v["landing"]) for _, v in dated if v.get("landing")]
    return sum(1 for i in range(1, len(landings)) if landings[i] != landings[i - 1])


def build_ga4_lookup(ga4_data: dict) -> dict:
    """Build {path: {sessions, bounce_rate}} from ga4_report.py --report top-pages JSON."""
    lookup = {}
    for page in ga4_data.get("pages", []):
        path = normalize_path(page.get("landing_page", ""))
        if path:
            lookup[path] = {
                "sessions": page.get("sessions", 0),
                "bounce_rate": page.get("bounce_rate"),
            }
    return lookup


def build_leads_lookup(leads_data: list) -> dict:
    """Build {path: leads_total} summed across verticals, from leads_import.py's
    'verticals' list."""
    lookup: dict = {}
    for vertical_data in leads_data:
        if not isinstance(vertical_data, dict):
            continue
        for page in vertical_data.get("pages", []):
            path = normalize_path(page.get("path", ""))
            if path:
                lookup[path] = lookup.get(path, 0) + (page.get("leads_total", 0) or 0)
    return lookup


if __name__ == "__main__":
    print("This module is completed in Task 2 — run via its main() once added.", file=sys.stderr)
    sys.exit(1)
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `cd .claude/plugins/claude-seo && python -m pytest tests/test_cannibalization_correlate.py -v`
Expected: PASS — all 15 tests green.

- [ ] **Step 5: Commit**

```bash
cd .claude/plugins/claude-seo
git add scripts/cannibalization_correlate.py tests/test_cannibalization_correlate.py
git commit -m "feat: add cannibalization indexing/normalization helpers"
```

---

## Task 2: `cannibalization_correlate.py` — scoping, detection, scoring, action logic, CLI

**Files:**
- Modify: `.claude/plugins/claude-seo/scripts/cannibalization_correlate.py` (append to the file created in Task 1)
- Test: `.claude/plugins/claude-seo/tests/test_cannibalization_correlate.py` (append)

**Interfaces:**
- Consumes: all six functions produced by Task 1, with the exact signatures above.
- Produces (for Task 3's report generator):
  - `classify_query_vertical(query: str, health_tracked: set, travel_tracked: set) -> str | None`
  - `classify_action(primary: dict, competitors: list, churn_count: int) -> str` — one of `"redirect"`, `"consolidate"`, `"differentiate"`, `"reinforce-signals"`
  - `severity_score(primary: dict, competitors: list, churn_count: int, leads_lost: int) -> float`
  - `find_cannibalization_pairs(gsc_query_index, health_semrush, travel_semrush, ga4_lookup, leads_lookup, min_impressions=10) -> list[dict]`
  - `correlate(gsc_data, health_semrush, travel_semrush, ga4_data, leads_data, min_impressions=10) -> dict`
  - Each pair dict has keys: `query, vertical, urls (list of {url, clicks, impressions, position, ga4_sessions, ga4_bounce_rate, leads_count, role}), semrush_tracked, landing_churn_count, severity_score, high_severity, recommended_action, rationale`
  - `correlate()`'s return dict has keys: `date_range, pairs (list), summary (total_pairs, by_vertical, by_action, high_severity_count, total_impressions_at_risk, total_leads_at_risk)`

- [ ] **Step 1: Write the failing tests**

Append to `.claude/plugins/claude-seo/tests/test_cannibalization_correlate.py`:

```python
from scripts.cannibalization_correlate import (
    classify_query_vertical,
    classify_action,
    severity_score,
    find_cannibalization_pairs,
    correlate,
)


# ── classify_query_vertical ──────────────────────────────────────────────────

def test_classify_query_vertical_health_stem_match():
    assert classify_query_vertical("best health insurance uae", set(), set()) == "health"


def test_classify_query_vertical_travel_stem_match():
    assert classify_query_vertical("cheap travel insurance uae", set(), set()) == "travel"


def test_classify_query_vertical_tracked_keyword_without_stem_match():
    assert classify_query_vertical("sehteq", {"sehteq"}, set()) == "health"


def test_classify_query_vertical_out_of_scope_returns_none():
    assert classify_query_vertical("cheapest car insurance dubai", set(), set()) is None


# ── classify_action ───────────────────────────────────────────────────────────

def test_classify_action_redirect_when_competitor_has_zero_clicks():
    primary = {"clicks": 40, "impressions": 500}
    competitors = [{"clicks": 0, "impressions": 200}]
    assert classify_action(primary, competitors, churn_count=0) == "redirect"


def test_classify_action_consolidate_when_high_churn_and_both_have_clicks():
    primary = {"clicks": 40, "impressions": 500}
    competitors = [{"clicks": 10, "impressions": 200}]
    assert classify_action(primary, competitors, churn_count=3) == "consolidate"


def test_classify_action_differentiate_when_both_have_clicks_and_low_churn():
    primary = {"clicks": 40, "impressions": 500}
    competitors = [{"clicks": 10, "impressions": 200}]
    assert classify_action(primary, competitors, churn_count=0) == "differentiate"


def test_classify_action_reinforce_signals_when_no_clicks_at_all():
    primary = {"clicks": 0, "impressions": 500}
    competitors = [{"clicks": 0, "impressions": 200}]
    assert classify_action(primary, competitors, churn_count=0) == "reinforce-signals"


# ── severity_score ─────────────────────────────────────────────────────────────

def test_severity_score_zero_when_no_competitor_impressions_or_leads_or_churn():
    primary = {"clicks": 40, "impressions": 500}
    assert severity_score(primary, [{"clicks": 0, "impressions": 0}], churn_count=0, leads_lost=0) == 0.0


def test_severity_score_capped_at_100():
    primary = {"clicks": 0, "impressions": 1}
    competitors = [{"clicks": 0, "impressions": 1000}]
    score = severity_score(primary, competitors, churn_count=10, leads_lost=100)
    assert score <= 100.0


# ── find_cannibalization_pairs: thresholds & scoping ───────────────────────────

def _gsc_two_url_query(impressions_a=500, impressions_b=200, clicks_a=40, clicks_b=5):
    return {
        "rows": [
            {"query": "compare health insurance uae", "page": "https://www.policybazaar.ae/health-insurance/", "clicks": clicks_a, "impressions": impressions_a, "position": 3.2},
            {"query": "compare health insurance uae", "page": "https://www.policybazaar.ae/", "clicks": clicks_b, "impressions": impressions_b, "position": 6.1},
        ]
    }


def test_find_pairs_flags_query_with_two_urls_above_threshold():
    from scripts.cannibalization_correlate import build_gsc_query_index
    index = build_gsc_query_index(_gsc_two_url_query())
    pairs = find_cannibalization_pairs(index, [], [], {}, {}, min_impressions=10)
    assert len(pairs) == 1
    assert pairs[0]["query"] == "compare health insurance uae"
    assert pairs[0]["vertical"] == "health"


def test_find_pairs_no_overlap_control_case_not_flagged():
    from scripts.cannibalization_correlate import build_gsc_query_index
    gsc_data = {"rows": [{"query": "best health insurance uae", "page": "https://www.policybazaar.ae/health-insurance/", "clicks": 40, "impressions": 500, "position": 2.0}]}
    index = build_gsc_query_index(gsc_data)
    pairs = find_cannibalization_pairs(index, [], [], {}, {}, min_impressions=10)
    assert pairs == []


def test_find_pairs_below_impression_threshold_not_flagged():
    from scripts.cannibalization_correlate import build_gsc_query_index
    index = build_gsc_query_index(_gsc_two_url_query(impressions_a=9, impressions_b=9))
    pairs = find_cannibalization_pairs(index, [], [], {}, {}, min_impressions=10)
    assert pairs == []


def test_find_pairs_at_impression_threshold_is_flagged():
    from scripts.cannibalization_correlate import build_gsc_query_index
    index = build_gsc_query_index(_gsc_two_url_query(impressions_a=10, impressions_b=10))
    pairs = find_cannibalization_pairs(index, [], [], {}, {}, min_impressions=10)
    assert len(pairs) == 1


def test_find_pairs_out_of_scope_query_not_flagged():
    from scripts.cannibalization_correlate import build_gsc_query_index
    gsc_data = {
        "rows": [
            {"query": "cheapest car insurance dubai", "page": "https://www.policybazaar.ae/car-insurance/", "clicks": 40, "impressions": 500, "position": 2.0},
            {"query": "cheapest car insurance dubai", "page": "https://www.policybazaar.ae/", "clicks": 5, "impressions": 200, "position": 6.0},
        ]
    }
    index = build_gsc_query_index(gsc_data)
    pairs = find_cannibalization_pairs(index, [], [], {}, {}, min_impressions=10)
    assert pairs == []


# ── high-severity escalation ────────────────────────────────────────────────────

def test_high_severity_true_when_competitor_has_one_click():
    from scripts.cannibalization_correlate import build_gsc_query_index
    index = build_gsc_query_index(_gsc_two_url_query(clicks_b=1))
    pairs = find_cannibalization_pairs(index, [], [], {}, {}, min_impressions=10)
    assert pairs[0]["high_severity"] is True


def test_high_severity_false_when_competitor_has_zero_clicks_and_no_churn():
    from scripts.cannibalization_correlate import build_gsc_query_index
    index = build_gsc_query_index(_gsc_two_url_query(clicks_b=0))
    pairs = find_cannibalization_pairs(index, [], [], {}, {}, min_impressions=10)
    assert pairs[0]["high_severity"] is False


def test_high_severity_true_when_churn_at_threshold():
    from scripts.cannibalization_correlate import build_gsc_query_index
    semrush = [{
        "keyword": "compare health insurance uae",
        "snapshots": {
            "2026-01-01": {"landing": "https://www.policybazaar.ae/health-insurance/"},
            "2026-01-08": {"landing": "https://www.policybazaar.ae/"},
            "2026-01-15": {"landing": "https://www.policybazaar.ae/health-insurance/"},
        },
    }]
    index = build_gsc_query_index(_gsc_two_url_query(clicks_b=0))
    pairs = find_cannibalization_pairs(index, semrush, [], {}, {}, min_impressions=10)
    assert pairs[0]["landing_churn_count"] == 2
    assert pairs[0]["high_severity"] is True
    assert pairs[0]["semrush_tracked"] is True


# ── correlate() end-to-end ────────────────────────────────────────────────────

def test_correlate_summary_counts_match_pairs():
    result = correlate(_gsc_two_url_query(), [], [], {}, [], min_impressions=10)
    assert result["summary"]["total_pairs"] == len(result["pairs"]) == 1
    assert result["summary"]["by_vertical"]["health"] == 1


def test_correlate_joins_ga4_and_leads_onto_url_records():
    ga4_data = {"pages": [{"landing_page": "/health-insurance", "sessions": 300, "bounce_rate": 20.0}]}
    leads_data = [{"vertical": "health", "pages": [{"path": "/health-insurance/", "leads_total": 15}]}]
    result = correlate(_gsc_two_url_query(), [], [], ga4_data, leads_data, min_impressions=10)
    primary = next(u for u in result["pairs"][0]["urls"] if u["role"] == "primary")
    assert primary["ga4_sessions"] == 300
    assert primary["leads_count"] == 15
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `cd .claude/plugins/claude-seo && python -m pytest tests/test_cannibalization_correlate.py -v`
Expected: FAIL — `ImportError: cannot import name 'classify_query_vertical'` (and the other new names) since they don't exist yet.

- [ ] **Step 3: Write the minimal implementation**

Replace the placeholder `if __name__ == "__main__":` block at the end of
`.claude/plugins/claude-seo/scripts/cannibalization_correlate.py` with:

```python
def classify_query_vertical(query: str, health_tracked: set, travel_tracked: set) -> str:
    """Return 'health', 'travel', or None if the query is out of scope for both."""
    q = query.lower().strip()
    if q in health_tracked or any(stem in q for stem in HEALTH_STEMS):
        return "health"
    if q in travel_tracked or any(stem in q for stem in TRAVEL_STEMS):
        return "travel"
    return None


def classify_action(primary: dict, competitors: list, churn_count: int) -> str:
    """Decide redirect / consolidate / differentiate / reinforce-signals from
    GSC clicks + SEMrush churn evidence alone (no canonical/content data — that
    lightweight spot-check happens at the SKILL.md orchestration layer for the
    top-priority pairs only, per the design's Option C scoping decision)."""
    competitor_clicks = sum(c["clicks"] for c in competitors)
    primary_clicks = primary["clicks"]

    if primary_clicks == 0 and competitor_clicks == 0:
        return "reinforce-signals"
    if competitor_clicks == 0:
        return "redirect"
    if churn_count >= HIGH_SEVERITY_CHURN_THRESHOLD:
        return "consolidate"
    return "differentiate"


def severity_score(primary: dict, competitors: list, churn_count: int, leads_lost: int) -> float:
    """0-100 score. Higher = more urgent."""
    total_impressions = primary["impressions"] + sum(c["impressions"] for c in competitors)
    competitor_impressions = sum(c["impressions"] for c in competitors)
    impressions_share = (competitor_impressions / total_impressions) if total_impressions else 0.0

    leads_component = 1.0 if leads_lost > 0 else 0.0
    churn_component = min(churn_count / 3.0, 1.0)

    return round(min(100.0, impressions_share * 60 + leads_component * 25 + churn_component * 15), 1)


def _build_rationale(query: str, primary: dict, competitors: list, action: str, churn_count: int) -> str:
    comp_summary = "; ".join(f"{c['page']} ({c['clicks']} clicks, {c['impressions']} impr)" for c in competitors)
    base = f"'{query}': {primary['page']} ({primary['clicks']} clicks, {primary['impressions']} impr) vs {comp_summary}"
    if action == "redirect":
        return f"{base} -- competitor URL(s) have 0 clicks, safe to redirect into the primary."
    if action == "consolidate":
        return f"{base} -- landing URL churned {churn_count}x in SEMrush history, indicating near-duplicate pages."
    if action == "differentiate":
        return f"{base} -- both URLs earn real clicks; retarget titles/H1s to reduce head-term overlap."
    return f"{base} -- impressions-only overlap, no click evidence yet; verify canonical/technical signals."


def find_cannibalization_pairs(
    gsc_query_index: dict,
    health_semrush: list,
    travel_semrush: list,
    ga4_lookup: dict,
    leads_lookup: dict,
    min_impressions: int = MIN_IMPRESSIONS_DEFAULT,
) -> list:
    """Find and score cannibalization pairs from an indexed GSC query→page dataset."""
    health_lookup, health_tracked = build_semrush_lookup(health_semrush)
    travel_lookup, travel_tracked = build_semrush_lookup(travel_semrush)

    pairs = []
    for query, rows in gsc_query_index.items():
        vertical = classify_query_vertical(query, health_tracked, travel_tracked)
        if vertical is None:
            continue

        eligible = [r for r in rows if r["impressions"] >= min_impressions]

        # Merge rows sharing the same normalized page (GSC can return duplicate
        # query/page combos across paginated windows in rare edge cases).
        merged: dict = {}
        for r in eligible:
            m = merged.setdefault(r["page"], {"page": r["page"], "clicks": 0, "impressions": 0, "position_sum": 0.0, "position_n": 0})
            m["clicks"] += r["clicks"]
            m["impressions"] += r["impressions"]
            m["position_sum"] += r["position"]
            m["position_n"] += 1

        if len(merged) < 2:
            continue

        merged_rows = [
            {"page": m["page"], "clicks": m["clicks"], "impressions": m["impressions"],
             "position": round(m["position_sum"] / m["position_n"], 1)}
            for m in merged.values()
        ]
        merged_rows.sort(key=lambda r: (r["clicks"], r["impressions"]), reverse=True)
        primary, *competitors = merged_rows

        kw_lookup = health_lookup if vertical == "health" else travel_lookup
        tracked_kw = kw_lookup.get(query.lower().strip())
        churn_count = compute_landing_churn(tracked_kw["snapshots"]) if tracked_kw else 0

        leads_lost = sum(leads_lookup.get(c["page"], 0) for c in competitors)
        action = classify_action(primary, competitors, churn_count)
        score = severity_score(primary, competitors, churn_count, leads_lost)
        high_severity = (
            any(c["clicks"] >= HIGH_SEVERITY_CLICK_THRESHOLD for c in competitors)
            or churn_count >= HIGH_SEVERITY_CHURN_THRESHOLD
        )

        url_records = []
        for i, row in enumerate([primary] + competitors):
            ga4 = ga4_lookup.get(row["page"], {})
            url_records.append({
                "url": row["page"],
                "clicks": row["clicks"],
                "impressions": row["impressions"],
                "position": row["position"],
                "ga4_sessions": ga4.get("sessions"),
                "ga4_bounce_rate": ga4.get("bounce_rate"),
                "leads_count": leads_lookup.get(row["page"], 0),
                "role": "primary" if i == 0 else "competitor",
            })

        pairs.append({
            "query": query,
            "vertical": vertical,
            "urls": url_records,
            "semrush_tracked": tracked_kw is not None,
            "landing_churn_count": churn_count,
            "severity_score": score,
            "high_severity": high_severity,
            "recommended_action": action,
            "rationale": _build_rationale(query, primary, competitors, action, churn_count),
        })

    pairs.sort(key=lambda p: p["severity_score"], reverse=True)
    return pairs


def correlate(
    gsc_data: dict,
    health_semrush: list,
    travel_semrush: list,
    ga4_data: dict,
    leads_data: list,
    min_impressions: int = MIN_IMPRESSIONS_DEFAULT,
) -> dict:
    """Cross-join GSC + SEMrush + GA4 + Leads and return all cannibalization pairs + summary."""
    gsc_query_index = build_gsc_query_index(gsc_data)
    ga4_lookup = build_ga4_lookup(ga4_data) if ga4_data else {}
    leads_lookup = build_leads_lookup(leads_data)

    pairs = find_cannibalization_pairs(
        gsc_query_index, health_semrush, travel_semrush, ga4_lookup, leads_lookup, min_impressions,
    )

    by_vertical: dict = defaultdict(int)
    by_action: dict = defaultdict(int)
    high_severity_count = 0
    total_impressions_at_risk = 0
    total_leads_at_risk = 0

    for p in pairs:
        by_vertical[p["vertical"]] += 1
        by_action[p["recommended_action"]] += 1
        if p["high_severity"]:
            high_severity_count += 1
        competitors = [u for u in p["urls"] if u["role"] == "competitor"]
        total_impressions_at_risk += sum(u["impressions"] for u in competitors)
        total_leads_at_risk += sum(u["leads_count"] or 0 for u in competitors)

    return {
        "date_range": gsc_data.get("date_range", {}),
        "pairs": pairs,
        "summary": {
            "total_pairs": len(pairs),
            "by_vertical": dict(by_vertical),
            "by_action": dict(by_action),
            "high_severity_count": high_severity_count,
            "total_impressions_at_risk": total_impressions_at_risk,
            "total_leads_at_risk": total_leads_at_risk,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Detect keyword cannibalization from GSC + SEMrush + GA4 + Leads")
    parser.add_argument("--gsc", required=True, help="Path to GSC JSON (dimensions=query,page) from gsc_query.py")
    parser.add_argument("--semrush", required=True, help="health_semrush.json,travel_semrush.json (comma-separated, health first)")
    parser.add_argument("--leads", required=True, help="Path(s) to leads JSON from leads_import.py")
    parser.add_argument("--ga4", default=None, help="Path to GA4 top-pages JSON from ga4_report.py (optional)")
    parser.add_argument("--min-impressions", type=int, default=MIN_IMPRESSIONS_DEFAULT)
    parser.add_argument("--json", action="store_true", dest="json_out")
    args = parser.parse_args()

    def load_json(path: str):
        try:
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            sys.exit(f"Error: file not found -- {path}")
        except json.JSONDecodeError as e:
            sys.exit(f"Error: invalid JSON in {path} -- {e}")

    gsc_data = load_json(args.gsc)

    semrush_paths = [p.strip() for p in args.semrush.split(",")]
    health_semrush = load_json(semrush_paths[0]) if len(semrush_paths) > 0 else []
    travel_semrush = load_json(semrush_paths[1]) if len(semrush_paths) > 1 else []

    leads_data = []
    for p in args.leads.split(","):
        raw = load_json(p.strip())
        if isinstance(raw, dict) and "verticals" in raw:
            leads_data.extend(raw["verticals"])
        elif isinstance(raw, dict):
            leads_data.append(raw)

    ga4_data = load_json(args.ga4) if args.ga4 else {}

    result = correlate(gsc_data, health_semrush, travel_semrush, ga4_data, leads_data, args.min_impressions)

    if args.json_out:
        print(json.dumps(result, indent=2))
    else:
        s = result["summary"]
        print(f"Cannibalization pairs: {s['total_pairs']} | High severity: {s['high_severity_count']} | By action: {dict(s['by_action'])}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `cd .claude/plugins/claude-seo && python -m pytest tests/test_cannibalization_correlate.py -v`
Expected: PASS — all tests from Task 1 and Task 2 green (24 total).

- [ ] **Step 5: Commit**

```bash
cd .claude/plugins/claude-seo
git add scripts/cannibalization_correlate.py tests/test_cannibalization_correlate.py
git commit -m "feat: add cannibalization detection, scoring, and action classification"
```

---

## Task 3: `cannibalization_report.py` — Excel workbook generator

**Files:**
- Create: `.claude/plugins/claude-seo/scripts/cannibalization_report.py`
- Test: `.claude/plugins/claude-seo/tests/test_cannibalization_report.py`

**Interfaces:**
- Consumes: `correlate()`'s exact return schema from Task 2 (`date_range`, `pairs[]`, `summary{}`).
- Produces: `build_workbook(data: dict, meta: dict) -> openpyxl.Workbook` with sheets in order `["Executive Summary", "Cannibalization Pairs", "Recommended Actions", "Data Sources & Methodology", "Raw Flagged Query Data"]`; `meta` dict has keys `gsc_property, ga4_property, min_impressions`.

- [ ] **Step 1: Write the failing tests**

Create `.claude/plugins/claude-seo/tests/test_cannibalization_report.py`:

```python
"""Tests for scripts/cannibalization_report.py"""

from scripts.cannibalization_report import build_workbook

FIXTURE = {
    "date_range": {"start": "2025-07-29", "end": "2026-07-26"},
    "pairs": [
        {
            "query": "compare health insurance uae",
            "vertical": "health",
            "urls": [
                {"url": "/health-insurance/", "clicks": 40, "impressions": 500, "position": 3.2,
                 "ga4_sessions": 300, "ga4_bounce_rate": 20.0, "leads_count": 15, "role": "primary"},
                {"url": "/", "clicks": 5, "impressions": 200, "position": 6.1,
                 "ga4_sessions": 50, "ga4_bounce_rate": 40.0, "leads_count": 1, "role": "competitor"},
            ],
            "semrush_tracked": True,
            "landing_churn_count": 3,
            "severity_score": 62.5,
            "high_severity": True,
            "recommended_action": "consolidate",
            "rationale": "test rationale",
        },
    ],
    "summary": {
        "total_pairs": 1,
        "by_vertical": {"health": 1, "travel": 0},
        "by_action": {"redirect": 0, "consolidate": 1, "differentiate": 0, "reinforce-signals": 0},
        "high_severity_count": 1,
        "total_impressions_at_risk": 200,
        "total_leads_at_risk": 1,
    },
}

META = {"gsc_property": "sc-domain:policybazaar.ae", "ga4_property": "properties/309894472", "min_impressions": 10}


def test_workbook_has_five_sheets_in_order():
    wb = build_workbook(FIXTURE, META)
    assert wb.sheetnames == [
        "Executive Summary", "Cannibalization Pairs", "Recommended Actions",
        "Data Sources & Methodology", "Raw Flagged Query Data",
    ]


def test_cannibalization_pairs_sheet_has_one_row_per_url():
    wb = build_workbook(FIXTURE, META)
    ws = wb["Cannibalization Pairs"]
    # header row + 2 URL rows (primary + 1 competitor) for the single fixture pair
    assert ws.max_row == 3


def test_executive_summary_total_pairs_matches_fixture():
    wb = build_workbook(FIXTURE, META)
    ws = wb["Executive Summary"]
    rows = list(ws.iter_rows(values_only=True))
    metric_row = next(r for r in rows if r[0] == "Total cannibalization pairs found")
    assert metric_row[1] == 1


def test_recommended_actions_sheet_has_one_row_per_pair():
    wb = build_workbook(FIXTURE, META)
    ws = wb["Recommended Actions"]
    assert ws.max_row == 2  # header + 1 pair


def test_save_and_reopen_workbook(tmp_path):
    from openpyxl import load_workbook
    wb = build_workbook(FIXTURE, META)
    out = tmp_path / "test.xlsx"
    wb.save(out)
    reopened = load_workbook(out)
    assert "Cannibalization Pairs" in reopened.sheetnames


def test_workbook_with_zero_pairs_still_has_five_sheets():
    empty = {
        "date_range": {"start": "2025-07-29", "end": "2026-07-26"},
        "pairs": [],
        "summary": {"total_pairs": 0, "by_vertical": {}, "by_action": {}, "high_severity_count": 0,
                     "total_impressions_at_risk": 0, "total_leads_at_risk": 0},
    }
    wb = build_workbook(empty, META)
    assert len(wb.sheetnames) == 5
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `cd .claude/plugins/claude-seo && python -m pytest tests/test_cannibalization_report.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'scripts.cannibalization_report'`.

- [ ] **Step 3: Write the minimal implementation**

Create `.claude/plugins/claude-seo/scripts/cannibalization_report.py`:

```python
#!/usr/bin/env python3
"""
Generate the 5-sheet cannibalization audit Excel workbook from
cannibalization_correlate.py's JSON output.

Usage:
    python cannibalization_report.py --data correlation.json --output report.xlsx
"""

import argparse
import json
import sys

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter
except ImportError:
    print("Error: openpyxl required. Install with: pip install openpyxl", file=sys.stderr)
    sys.exit(1)

HEADER_FILL = PatternFill(start_color="1E3A5F", end_color="1E3A5F", fill_type="solid")
HEADER_FONT = Font(color="FFFFFF", bold=True)

ACTION_STEPS = {
    "redirect": "301 redirect the competitor URL(s) into the primary URL. Update internal links pointing to the old URL.",
    "consolidate": "Merge the strongest content from both pages into the primary URL, then 301 redirect the other(s). Landing URL has churned in SEMrush history -- Google already treats these as interchangeable.",
    "differentiate": "Rewrite title/H1/intro on the competitor URL(s) to target its own distinct sub-intent; strengthen internal links from the primary URL to reinforce which page owns the shared head-term.",
    "reinforce-signals": "No clear click evidence yet. Manually verify canonical tags and internal-link signals before deciding between redirect and differentiation.",
}


def _write_header_row(ws, headers: list) -> None:
    ws.append(headers)
    for cell in ws[ws.max_row]:
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = Alignment(horizontal="left")


def _autosize_columns(ws, widths: list) -> None:
    for i, width in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = width


def build_executive_summary(wb, data: dict) -> None:
    ws = wb.active
    ws.title = "Executive Summary"
    summary = data.get("summary", {})
    date_range = data.get("date_range", {})

    ws.append(["SEO Keyword Cannibalization Audit -- PolicyBazaar UAE"])
    ws["A1"].font = Font(bold=True, size=14)
    ws.append([f"GSC period analysed: {date_range.get('start', 'n/a')} to {date_range.get('end', 'n/a')}"])
    ws.append([])

    _write_header_row(ws, ["Metric", "Value"])

    by_vertical = summary.get("by_vertical", {})
    by_action = summary.get("by_action", {})
    rows = [
        ("Total cannibalization pairs found", summary.get("total_pairs", 0)),
        ("High severity", summary.get("high_severity_count", 0)),
        ("Health vertical pairs", by_vertical.get("health", 0)),
        ("Travel vertical pairs", by_vertical.get("travel", 0)),
        ("Recommended: redirect", by_action.get("redirect", 0)),
        ("Recommended: consolidate", by_action.get("consolidate", 0)),
        ("Recommended: differentiate", by_action.get("differentiate", 0)),
        ("Recommended: reinforce-signals", by_action.get("reinforce-signals", 0)),
        ("Total impressions at risk (competitor URLs)", summary.get("total_impressions_at_risk", 0)),
        ("Total leads at risk (competitor URLs)", summary.get("total_leads_at_risk", 0)),
    ]
    for label, value in rows:
        ws.append([label, value])

    _autosize_columns(ws, [45, 15])


def build_cannibalization_pairs(wb, data: dict) -> None:
    ws = wb.create_sheet("Cannibalization Pairs")
    headers = [
        "Query", "Vertical", "Role", "URL", "Clicks", "Impressions", "Avg Position",
        "GA4 Sessions", "GA4 Bounce Rate", "Leads", "SEMrush Tracked",
        "Landing Churn Count", "Severity Score", "High Severity",
        "Recommended Action", "Rationale",
    ]
    _write_header_row(ws, headers)

    for pair in data.get("pairs", []):
        for url_rec in pair["urls"]:
            ws.append([
                pair["query"], pair["vertical"], url_rec["role"], url_rec["url"],
                url_rec["clicks"], url_rec["impressions"], url_rec["position"],
                url_rec.get("ga4_sessions"), url_rec.get("ga4_bounce_rate"),
                url_rec.get("leads_count"), pair["semrush_tracked"],
                pair["landing_churn_count"], pair["severity_score"], pair["high_severity"],
                pair["recommended_action"], pair["rationale"],
            ])

    _autosize_columns(ws, [30, 10, 12, 45, 9, 12, 12, 12, 14, 8, 15, 12, 12, 12, 18, 70])
    ws.freeze_panes = "A2"


def build_recommended_actions(wb, data: dict) -> None:
    ws = wb.create_sheet("Recommended Actions")
    headers = ["Priority", "Vertical", "Query", "Primary URL", "Competitor URL(s)", "Action", "Steps"]
    _write_header_row(ws, headers)

    pairs_sorted = sorted(data.get("pairs", []), key=lambda p: p["severity_score"], reverse=True)
    for pair in pairs_sorted:
        primary = next(u for u in pair["urls"] if u["role"] == "primary")
        competitors = [u for u in pair["urls"] if u["role"] == "competitor"]
        priority = "P0" if pair["high_severity"] else ("P1" if pair["severity_score"] >= 30 else "P2")
        ws.append([
            priority, pair["vertical"], pair["query"], primary["url"],
            "; ".join(c["url"] for c in competitors),
            pair["recommended_action"],
            ACTION_STEPS[pair["recommended_action"]],
        ])

    _autosize_columns(ws, [10, 10, 30, 40, 40, 18, 80])
    ws.freeze_panes = "A2"


def build_methodology(wb, data: dict, meta: dict) -> None:
    ws = wb.create_sheet("Data Sources & Methodology")
    date_range = data.get("date_range", {})
    lines = [
        ("GSC property", meta.get("gsc_property", "n/a")),
        ("GSC period analysed", f"{date_range.get('start', 'n/a')} to {date_range.get('end', 'n/a')}"),
        ("GA4 property", meta.get("ga4_property") or "not configured for this run"),
        ("SEMrush source", "Local Position Tracking CSV export (not live API) -- Health + Travel"),
        ("Leads source", "Local Leads CSV export -- Health + Travel"),
        ("Minimum impressions to flag", meta.get("min_impressions", 10)),
        ("High severity rule", "Competitor URL has >=1 click, OR SEMrush landing URL churned >=2 times"),
        ("Known gap", "GA4 was only just configured for this pipeline (property "
                      f"{meta.get('ga4_property') or 'n/a'}, 2026-07-29); cross-check early "
                      "GA4 figures against the GA4 UI directly before treating them as settled."),
        ("Known gap", "SEMrush position tracking covers 200 keywords total; queries outside "
                      "this list rely on GSC evidence alone (churn column will be empty)."),
        ("Known gap", "GSC omits very low-volume query rows per Google's own anonymization "
                      "thresholds; some long-tail cannibalization is inherently invisible."),
        ("Scope", "Health + Travel Insurance verticals only (v1) -- see design doc Non-goals."),
    ]
    _write_header_row(ws, ["Item", "Value"])
    for label, value in lines:
        ws.append([label, value])
    _autosize_columns(ws, [30, 90])


def build_raw_flagged_data(wb, data: dict) -> None:
    ws = wb.create_sheet("Raw Flagged Query Data")
    headers = ["Query", "Vertical", "URL", "Role", "Clicks", "Impressions", "Position"]
    _write_header_row(ws, headers)
    for pair in data.get("pairs", []):
        for url_rec in pair["urls"]:
            ws.append([
                pair["query"], pair["vertical"], url_rec["url"], url_rec["role"],
                url_rec["clicks"], url_rec["impressions"], url_rec["position"],
            ])
    _autosize_columns(ws, [30, 10, 45, 12, 9, 12, 12])


def build_workbook(data: dict, meta: dict):
    wb = Workbook()
    build_executive_summary(wb, data)
    build_cannibalization_pairs(wb, data)
    build_recommended_actions(wb, data)
    build_methodology(wb, data, meta)
    build_raw_flagged_data(wb, data)
    return wb


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the cannibalization audit Excel report")
    parser.add_argument("--data", required=True, help="Path to cannibalization_correlate.py JSON output")
    parser.add_argument("--output", required=True, help="Output .xlsx path")
    parser.add_argument("--gsc-property", default="sc-domain:policybazaar.ae")
    parser.add_argument("--ga4-property", default="")
    parser.add_argument("--min-impressions", type=int, default=10)
    args = parser.parse_args()

    with open(args.data, encoding="utf-8") as f:
        data = json.load(f)

    meta = {
        "gsc_property": args.gsc_property,
        "ga4_property": args.ga4_property,
        "min_impressions": args.min_impressions,
    }

    wb = build_workbook(data, meta)
    wb.save(args.output)
    print(f"Report saved: {args.output}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `cd .claude/plugins/claude-seo && python -m pytest tests/test_cannibalization_report.py -v`
Expected: PASS — all 6 tests green.

- [ ] **Step 5: Commit**

```bash
cd .claude/plugins/claude-seo
git add scripts/cannibalization_report.py tests/test_cannibalization_report.py
git commit -m "feat: add cannibalization Excel report generator"
```

---

## Task 4: `seo-cannibalization/SKILL.md`

**Files:**
- Create: `.claude/plugins/claude-seo/skills/seo-cannibalization/SKILL.md`

**Interfaces:**
- Consumes: exact CLI flags of `gsc_query.py`, `ga4_report.py`, `semrush_import.py`, `leads_import.py` (all unchanged, existing), and `cannibalization_correlate.py` / `cannibalization_report.py` from Tasks 1–3 (`--gsc`, `--semrush`, `--leads`, `--ga4`, `--min-impressions`, `--json` / `--data`, `--output`, `--gsc-property`, `--ga4-property`, `--min-impressions`).
- Produces: the final `.xlsx` report path, consumed by Task 6's end-to-end run.

- [ ] **Step 1: Write the skill file**

Create `.claude/plugins/claude-seo/skills/seo-cannibalization/SKILL.md`:

```markdown
---
name: seo-cannibalization
description: >
  PolicyBazaar UAE keyword cannibalization audit: cross-references GSC query/page
  overlap, SEMrush landing-URL churn, GA4 engagement, and leads data for Health and
  Travel Insurance to identify which URLs compete against each other for the same
  search queries, and generates a prioritised Excel report with redirect/consolidate/
  differentiate recommendations. Use when asked about keyword cannibalization,
  duplicate ranking pages, URLs competing for the same query, or "which pages are
  fighting each other in search."
user-invokable: true
argument-hint: "[health|travel|both]"
metadata:
  author: Aakash Srivastava
  version: "1.0.0"
  category: seo
---

# SEO Keyword Cannibalization Audit -- PolicyBazaar UAE

You are acting as a senior SEO strategist for PolicyBazaar UAE. Cross-reference
Search Console, GA4, SEMrush position tracking, and leads data to identify keyword
cannibalization -- URLs unintentionally competing against each other for the same
search query -- and produce a prioritised Excel report with concrete fix
recommendations for each pair found.

Work through each phase in strict sequence. Collect all data before analysing.

---

## Argument Handling

If invoked with `health`, `travel`, or `both`, store as `$VERTICAL`. Default: `both`
(this audit's evidence -- leads + SEMrush position tracking -- only exists for these
two verticals; a whole-site pass isn't supported by this skill).

Set `$TODAY` = today's date in YYYY-MM-DD format:
```bash
date +%F
```

---

## Phase 1 -- Credential Check + Data Ingest

### 1.1 Check credentials

```bash
python scripts/google_auth.py --check --json
```

Note the detected tier. Tier 1 minimum for GSC; Tier 2 (+ `ga4_property_id`) for GA4.
If GA4 is unavailable, continue without it -- the report's Methodology sheet flags
GA4 columns as unavailable rather than silently omitting the gap.

### 1.2 Run all ingestion in parallel (Agent tool -- fire simultaneously)

**Agent A -- GSC, 12 months, query+page:**
```bash
python scripts/gsc_query.py --days 365 --dimensions query,page --limit 25000 --json > /tmp/cannibal_gsc.json
```

**Agent B -- GA4 top pages (skip if Tier < 2):**
```bash
python scripts/ga4_report.py --days 365 --report top-pages --json > /tmp/cannibal_ga4.json
```

**Agent C -- Health SEMrush:**
```bash
python scripts/semrush_import.py --vertical health --json > /tmp/cannibal_semrush_health.json
```

**Agent D -- Travel SEMrush:**
```bash
python scripts/semrush_import.py --vertical travel --json > /tmp/cannibal_semrush_travel.json
```

**Agent E -- Health leads:**
```bash
python scripts/leads_import.py --vertical health --json > /tmp/cannibal_leads_health.json
```

**Agent F -- Travel leads:**
```bash
python scripts/leads_import.py --vertical travel --json > /tmp/cannibal_leads_travel.json
```

Wait for all agents. If a script errors, note the missing data source and continue --
per this workspace's data-integrity requirement, never substitute inferred data for a
source that failed.

**Vertical optimization:** If `$VERTICAL` is `health`, skip Agents D and F. If
`$VERTICAL` is `travel`, skip Agents C and E. Always run Agents A and B -- GSC and
GA4 cover the whole site and the in-scope filter is applied downstream.

---

## Phase 2 -- Correlation

```bash
python scripts/cannibalization_correlate.py \
  --gsc /tmp/cannibal_gsc.json \
  --semrush /tmp/cannibal_semrush_health.json,/tmp/cannibal_semrush_travel.json \
  --leads /tmp/cannibal_leads_health.json,/tmp/cannibal_leads_travel.json \
  --ga4 /tmp/cannibal_ga4.json \
  --min-impressions 10 \
  --json > /tmp/cannibal_correlation.json
```

If `$VERTICAL` is not `both`, filter `pairs[]` in the parsed output to
`vertical == $VERTICAL` before continuing (the correlation script always covers
both verticals; single-vertical filtering happens here).

Display triage table:

```
CANNIBALIZATION TRIAGE -- [VERTICAL]

Rank | Query | Vertical | Primary URL | Competitor(s) | Severity | Action
-----|-------|----------|-------------|---------------|----------|-------
  1  | compare health insurance uae | health | /health-insurance/ | / | 62.5 | consolidate
  ...
```

---

## Phase 3 -- Spot-Check Top Findings (light corroboration, not a full crawl)

For the top 10 pairs by severity score, spawn parallel Agent tool calls (one per
pair) to check canonical/title signals -- this is the design's Option-C-derived
corroboration step, deliberately limited to these top findings only:

> Fetch $PRIMARY_URL and each competitor URL via `python scripts/fetch_page.py <url>`,
> then `python scripts/parse_html.py` on each. Report: canonical tag target for each
> URL, title tag, H1. Flag if a competitor URL's canonical already points at the
> primary URL -- if so, the action becomes "reinforce-signals" regardless of the
> correlation script's classification (Google isn't yet honoring an already-correct
> signal).

Record any override to `recommended_action` from this step before Phase 4.

---

## Phase 4 -- Excel Report

```bash
mkdir -p "/Users/aakashsrivastava/Documents/PolicyBazaar Research/Cannibalization/Result"

python scripts/cannibalization_report.py \
  --data /tmp/cannibal_correlation.json \
  --output "/Users/aakashsrivastava/Documents/PolicyBazaar Research/Cannibalization/Result/cannibalization-report-{$TODAY}.xlsx" \
  --gsc-property sc-domain:policybazaar.ae \
  --ga4-property "properties/309894472" \
  --min-impressions 10
```

After writing the file, output:
```
Report saved: /Users/aakashsrivastava/Documents/PolicyBazaar Research/Cannibalization/Result/cannibalization-report-{$TODAY}.xlsx
```

---

## Data Path Reference

| Source | Path |
|--------|------|
| Health leads CSV | `/Users/aakashsrivastava/Documents/PolicyBazaar Research/Health Insurance/Ranking And Leads/Leads.csv` |
| Travel leads CSV | `/Users/aakashsrivastava/Documents/PolicyBazaar Research/Travel Insurance/Ranking And Leads/Leads.csv` |
| Health SEMrush CSV | `/Users/aakashsrivastava/Documents/PolicyBazaar Research/Health Insurance/Ranking And Leads/Position.csv` |
| Travel SEMrush CSV | `/Users/aakashsrivastava/Documents/PolicyBazaar Research/Travel Insurance/Ranking And Leads/Position.csv` |
| Report output | `/Users/aakashsrivastava/Documents/PolicyBazaar Research/Cannibalization/Result/` |

## Error Handling

| Scenario | Action |
|----------|--------|
| GSC credential check fails | Stop. Report which tier is missing and what's needed -- do not proceed with partial/inferred data. |
| GA4 unavailable (Tier < 2) | Continue without it. Report's Methodology sheet notes GA4 columns are empty for this run. |
| SEMrush CSV not found | Continue without SEMrush corroboration for that vertical. `semrush_tracked` is `false` for all pairs in that vertical; report notes this gap. |
| Leads CSV not found | Continue without leads data. `leads_count` is `null`; severity scoring's leads component drops to 0 for all pairs. |
| Zero pairs found | Report this plainly -- it means no cannibalization above the flagging threshold was detected, not that the audit failed. |
```

- [ ] **Step 2: Verify the file is well-formed**

Run: `python3 -c "import yaml, re; content = open('.claude/plugins/claude-seo/skills/seo-cannibalization/SKILL.md').read(); fm = content.split('---')[1]; yaml.safe_load(fm); print('frontmatter OK')"`
Expected: `frontmatter OK` (confirms the YAML frontmatter parses cleanly — this repo's `hooks/hooks.json` PostToolUse schema validation runs a similar check on real skill writes, so validating it here avoids a hook failure later).

- [ ] **Step 3: Commit**

```bash
cd .claude/plugins/claude-seo
git add skills/seo-cannibalization/SKILL.md
git commit -m "feat: add seo-cannibalization skill orchestrating the audit phases"
```

---

## Task 5: Hub wiring — `uae-insurance` router + `claude-seo/CLAUDE.md` architecture doc

**Files:**
- Modify: `.claude/skills/uae-insurance/SKILL.md` (parent workspace repo)
- Modify: `.claude/plugins/claude-seo/CLAUDE.md` (claude-seo plugin repo)

**Interfaces:**
- Consumes: `seo-cannibalization/SKILL.md`'s existence and path from Task 4.
- Produces: nothing consumed by later tasks — this is documentation/routing only.

- [ ] **Step 1: Add the router row**

In `.claude/skills/uae-insurance/SKILL.md`, the router table currently reads:

```
| Intent / `$1` | Read this file |
|---|---|
| RACE loop / stage prompts — `flow` | `~/.claude/plugins/claude-seo/skills/seo-flow/SKILL.md` |
| insurance page audit — `audit` | `~/.claude/plugins/claude-seo/skills/seo-insurance-ae/SKILL.md` |
| leads intel / recovery — `leads` | `~/.claude/plugins/claude-seo/skills/seo-leads-intel/SKILL.md` |
```

Add one row after the `leads` row:

```
| keyword cannibalization / duplicate ranking — `cannibalization` | `~/.claude/plugins/claude-seo/skills/seo-cannibalization/SKILL.md` |
```

Also update the frontmatter `description:` field (first line after `name: uae-insurance`)
to mention cannibalization, so the hub actually triggers on it — append this clause
before the final sentence: `, and keyword cannibalization audits ("cannibalization",
"duplicate ranking pages", "URLs competing for the same query")`.

- [ ] **Step 2: Update `claude-seo/CLAUDE.md`'s architecture tree**

In the `skills/` tree listing, immediately after the `seo-leads-intel/` line
(`# PB UAE leads intelligence (internal — health + travel)`), add:

```
    seo-cannibalization/          # PB UAE keyword cannibalization audit (internal — health + travel)
      SKILL.md
```

In the `scripts/` tree listing, immediately after the `ga4_report.py` line, add two
lines:

```
    cannibalization_correlate.py # Cannibalization detection: GSC query/page overlap + SEMrush churn + GA4 + leads
    cannibalization_report.py    # Cannibalization audit Excel workbook generator (openpyxl)
```

In the `## Commands` table, immediately after the
`/seo-leads-intel [health|travel|both]` row, add:

```
| `/seo-cannibalization [health\|travel\|both]` | PB UAE keyword cannibalization audit: GSC + SEMrush + GA4 + leads → Excel report |
```

- [ ] **Step 3: Commit both repos**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude"
git add .claude/skills/uae-insurance/SKILL.md
git commit -m "feat(uae-insurance): route cannibalization audits to seo-cannibalization skill"

cd .claude/plugins/claude-seo
git add CLAUDE.md
git commit -m "docs: document seo-cannibalization skill and scripts in architecture tree"
```

---

## Task 6: End-to-end run against real data — deliver the report

**Files:** none created or modified — this task runs the pipeline built in Tasks 1–5
against live production data and hands back the actual deliverable.

**Interfaces:**
- Consumes: every script and the skill from Tasks 1–5, run for real (no fixtures).
- Produces: the real `.xlsx` file at
  `PolicyBazaar Research/Cannibalization/Result/cannibalization-report-{today}.xlsx`.

- [ ] **Step 1: Run the full test suite once more, from a clean state**

```bash
cd .claude/plugins/claude-seo
python -m pytest tests/test_cannibalization_correlate.py tests/test_cannibalization_report.py -v
```

Expected: all tests pass (confirms Tasks 1–3's work is intact before running against
real data).

- [ ] **Step 2: Run Phase 1 ingestion for real (both verticals)**

```bash
cd .claude/plugins/claude-seo
python scripts/gsc_query.py --days 365 --dimensions query,page --limit 25000 --json > /tmp/cannibal_gsc.json
python scripts/ga4_report.py --days 365 --report top-pages --json > /tmp/cannibal_ga4.json
python scripts/semrush_import.py --vertical health --json > /tmp/cannibal_semrush_health.json
python scripts/semrush_import.py --vertical travel --json > /tmp/cannibal_semrush_travel.json
python scripts/leads_import.py --vertical health --json > /tmp/cannibal_leads_health.json
python scripts/leads_import.py --vertical travel --json > /tmp/cannibal_leads_travel.json
```

Check each output file is non-empty and has no `"error"` field set before continuing.
If any command fails or returns an error field, stop and report exactly which source
failed and why — per this workspace's Tool Failure Policy, do not proceed with a
partial or substituted dataset.

- [ ] **Step 3: Run the correlation**

```bash
python scripts/cannibalization_correlate.py \
  --gsc /tmp/cannibal_gsc.json \
  --semrush /tmp/cannibal_semrush_health.json,/tmp/cannibal_semrush_travel.json \
  --leads /tmp/cannibal_leads_health.json,/tmp/cannibal_leads_travel.json \
  --ga4 /tmp/cannibal_ga4.json \
  --min-impressions 10 \
  --json > /tmp/cannibal_correlation.json

python -c "import json; d = json.load(open('/tmp/cannibal_correlation.json')); print(d['summary'])"
```

Review the printed summary before proceeding.

- [ ] **Step 4: Spot-check the top 3 flagged pairs against the GSC UI**

For the top 3 pairs by `severity_score` in `/tmp/cannibal_correlation.json`, manually
re-query GSC filtered to that exact query to confirm the reported impressions/clicks
per URL match:

```bash
python scripts/gsc_query.py --days 365 --dimensions page --limit 100 --json > /tmp/spot_check_query.json
```
(swap in a `filters` dimensionFilterGroup for the specific query text before running,
per `gsc_query.py --help`, or cross-reference directly against the GSC UI's
Performance → Search Results report filtered to that query.)

Confirm the numbers reconcile before treating the report as final. If they don't
reconcile, stop and debug the correlation logic rather than shipping a
mismatched report.

- [ ] **Step 5: Generate the final report**

```bash
mkdir -p "/Users/aakashsrivastava/Documents/PolicyBazaar Research/Cannibalization/Result"

python scripts/cannibalization_report.py \
  --data /tmp/cannibal_correlation.json \
  --output "/Users/aakashsrivastava/Documents/PolicyBazaar Research/Cannibalization/Result/cannibalization-report-$(date +%F).xlsx" \
  --gsc-property sc-domain:policybazaar.ae \
  --ga4-property "properties/309894472" \
  --min-impressions 10
```

- [ ] **Step 6: Report back to Aakash**

State the final file path, the top-line summary counts (total pairs, by vertical, by
severity, by action), and the top 3 highest-severity findings with their recommended
action — matching this workspace's Data Integrity rule: every number cited must come
directly from `/tmp/cannibal_correlation.json`'s `summary` and `pairs`, not
paraphrased or rounded beyond what's in the data.

No commit for this task — it produces a data deliverable in `PolicyBazaar Research/`,
not a code change.
