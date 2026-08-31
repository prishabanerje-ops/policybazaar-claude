#!/usr/bin/env python3
"""
Build the AI Overview / ChatGPT citation-position analysis from one or more
scraped datasets (one per engine). Generic for ANY topic.

Produces an .xlsx with, FOR EACH engine:
  - "<Engine> positions" sheet: rows = prompts, columns = every domain cited in
    >= --min-prompts prompts (ranked by citation frequency). Cell = the domain's
    position in that answer's cited-sources list (1 = first cited), "NA" = not cited.
    The --brand domain is always shown and highlighted, even if below the threshold.
    Two summary rows at the bottom: "cited in" and "avg position".
  - "<Engine> text" sheet: the verbatim answer text + ordered citations per prompt.

Dataset JSON schema (written by the ai-overview-scraper agent), per engine:
{
  "topic": "Health Insurance",
  "engine": "google" | "chatgpt",
  "region": {"google": "google.ae", "gl": "ae", "hl": "en"},
  "date": "2026-06-24",
  "brand": "policybazaar.ae",
  "keywords": [
    {"q": "prompt", "present": true,  "text": "verbatim...", "hosts": ["a.com","b.ae", ...]},
    {"q": "prompt", "present": false, "text": "",            "hosts": []}
  ]
}
("present" = an answer/overview with sources was captured. Back-compat: the loader
also accepts the old "hasAIO" field, or infers presence from a non-empty hosts list.)

Usage (one or more engines):
  python3 build_matrix.py \
     --data "Google AIO=/path/google.json" "ChatGPT=/path/chatgpt.json" \
     --out report.xlsx [--brand policybazaar.ae] [--min-prompts 2]

A bare path with no "Label=" prefix is labelled "AI Overview".
"""
import argparse, json, re, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

THIN = Side(style="thin", color="D8D8D8")
BORDER = Border(THIN, THIN, THIN, THIN)


def norm(host: str) -> str:
    h = (host or "").strip().lower()
    for p in ("www.", "m.", "amp."):
        if h.startswith(p):
            h = h[len(p):]
    return h


def present(k) -> bool:
    if "present" in k:
        return bool(k["present"])
    if "hasAIO" in k:
        return bool(k["hasAIO"])
    return bool(k.get("hosts"))


def position(hosts, dom):
    for i, h in enumerate(hosts):
        if norm(h) == dom:
            return i + 1
    return "NA"


def safe_sheet(name: str) -> str:
    name = re.sub(r"[:\\/?*\[\]]", "-", name)
    return name[:31] if len(name) > 31 else name


def build_engine_sheets(wb, label, data, brand, min_prompts, first):
    KW = data.get("keywords", [])
    n = len(KW)
    cov = {}
    for k in KW:
        for d in {norm(h) for h in k.get("hosts", []) if norm(h)}:
            cov[d] = cov.get(d, 0) + 1
    cols = sorted([d for d, c in cov.items() if c >= min_prompts], key=lambda d: (-cov[d], d))
    if brand not in cols:
        cols.append(brand)

    ws = wb.active if first else wb.create_sheet()
    ws.title = safe_sheet(f"{label} positions")

    reg = data.get("region", {})
    regtxt = f"{reg.get('google','')} gl={reg.get('gl','')} hl={reg.get('hl','')}".strip()
    ws["A1"] = f"{label} — citation position by prompt  |  topic: {data.get('topic','')}  |  {regtxt}  |  {data.get('date','')}"
    ws["A1"].font = Font(bold=True, size=13)
    ws["A2"] = ("Value = position in the cited-sources list (1 = first cited). NA = not cited. "
                f"Columns = domains cited in ≥{min_prompts} prompts, by frequency. Tracked brand "
                f"({brand}) highlighted and always shown.")
    ws["A2"].font = Font(italic=True, size=9, color="666666")

    HROW = 4
    hdr_fill = PatternFill("solid", fgColor="1F4E78")
    brand_hdr = PatternFill("solid", fgColor="C55A11")
    hdr_font = Font(bold=True, color="FFFFFF", size=9)
    c = ws.cell(row=HROW, column=1, value="Prompt")
    c.fill = PatternFill("solid", fgColor="404040"); c.font = Font(bold=True, color="FFFFFF"); c.border = BORDER
    for j, d in enumerate(cols, start=2):
        cell = ws.cell(row=HROW, column=j, value=d)
        cell.font = hdr_font; cell.border = BORDER
        cell.alignment = Alignment(horizontal="center", vertical="bottom", textRotation=90)
        cell.fill = brand_hdr if d == brand else hdr_fill

    brand_fill = PatternFill("solid", fgColor="FCE4D6")
    na_font = Font(color="C00000", size=9)
    cited_font = Font(color="1F7A1F", bold=True, size=9)
    counts = {d: 0 for d in cols}; possum = {d: 0 for d in cols}
    r = HROW + 1
    for k in KW:
        hosts = k.get("hosts", [])
        ws.cell(row=r, column=1, value=k.get("q", "")).border = BORDER
        for j, d in enumerate(cols, start=2):
            v = position(hosts, d)
            cell = ws.cell(row=r, column=j, value=v)
            cell.alignment = Alignment(horizontal="center"); cell.border = BORDER
            if d == brand:
                cell.fill = brand_fill
            if v == "NA":
                cell.font = na_font
            else:
                cell.font = cited_font; counts[d] += 1; possum[d] += v
        r += 1
    r += 1
    ws.cell(row=r, column=1, value=f"Cited in (of {n})").font = Font(bold=True)
    for j, d in enumerate(cols, start=2):
        ws.cell(row=r, column=j, value=f"{counts[d]} ({round(100*counts[d]/n) if n else 0}%)").font = Font(bold=True, size=9)
        ws.cell(row=r, column=j).alignment = Alignment(horizontal="center")
    r += 1
    ws.cell(row=r, column=1, value="Avg position when cited").font = Font(bold=True)
    for j, d in enumerate(cols, start=2):
        avg = round(possum[d] / counts[d], 1) if counts[d] else "NA"
        ws.cell(row=r, column=j, value=avg).font = Font(bold=True, size=9)
        ws.cell(row=r, column=j).alignment = Alignment(horizontal="center")

    ws.column_dimensions["A"].width = 52
    for j in range(2, len(cols) + 2):
        ws.column_dimensions[get_column_letter(j)].width = 6.5
    ws.row_dimensions[HROW].height = 130
    ws.freeze_panes = "B5"

    # text sheet
    ws2 = wb.create_sheet(safe_sheet(f"{label} text"))
    for j, head in enumerate(["Prompt", "Has answer?", "# citations", "Verbatim text", "Cited domains (in order)"], 1):
        cc = ws2.cell(row=1, column=j, value=head)
        cc.font = Font(bold=True, color="FFFFFF"); cc.fill = hdr_fill
    rr = 2
    for k in KW:
        ws2.cell(row=rr, column=1, value=k.get("q", ""))
        ws2.cell(row=rr, column=2, value="Yes" if present(k) else "No")
        ws2.cell(row=rr, column=3, value=len(k.get("hosts", [])))
        tcell = ws2.cell(row=rr, column=4, value=k.get("text", ""))
        tcell.alignment = Alignment(wrap_text=True, vertical="top")
        ws2.cell(row=rr, column=5, value=", ".join(norm(h) for h in k.get("hosts", [])))
        rr += 1
    ws2.column_dimensions["A"].width = 46
    ws2.column_dimensions["B"].width = 12
    ws2.column_dimensions["C"].width = 11
    ws2.column_dimensions["D"].width = 110
    ws2.column_dimensions["E"].width = 60
    ws2.freeze_panes = "A2"

    # leaderboard for stdout
    rank = sorted(cols, key=lambda d: (-counts[d], d))
    lb = [(d, counts[d], round(possum[d]/counts[d], 1) if counts[d] else "NA") for d in rank]
    answered = sum(1 for k in KW if present(k))
    return {"label": label, "n": n, "answered": answered, "leaderboard": lb,
            "brand": {"cited": counts.get(brand, 0),
                      "avg": round(possum[brand]/counts[brand], 1) if counts.get(brand) else "NA"}}


def build_fanout_sheet(wb, label, data, brand, min_prompts):
    """Fan-out visibility sheet: primary (won a specific answer sub-facet) vs
    trailing-only (supplementary source list only) citations per domain, plus a
    row-by-row list of which sub-facets the brand lost and who won them instead.
    Needs `sectionCitations`/`trailingSources` on the dataset's keywords (google
    engine only, extract_aio.js 2026-08-31+); returns None and skips silently for
    datasets without that data (older schema, or the chatgpt engine)."""
    KW = data.get("keywords", [])
    if not any(k.get("sectionCitations") or k.get("trailingSources") for k in KW):
        return None
    n = len(KW)

    primary, trailing_only = {}, {}
    mentioned_not_cited_count = 0
    gap_rows = []
    unresolved_seen = set()

    for k in KW:
        secs = k.get("sectionCitations") or []
        trail = k.get("trailingSources") or []
        prompt_primary_hosts = set()
        lost_sections = []
        for sc in secs:
            h = norm(sc.get("host") or "")
            if h:
                primary[h] = primary.get(h, 0) + 1
                prompt_primary_hosts.add(h)
            if h != brand:
                lost_sections.append((sc.get("answerSection", ""), sc.get("citedAs", ""), h))
        for tc in trail:
            h = norm(tc.get("host") or "")
            if h and h not in prompt_primary_hosts:
                trailing_only[h] = trailing_only.get(h, 0) + 1
        if k.get("mentionedNotCited"):
            mentioned_not_cited_count += 1
        for name in k.get("unresolved") or []:
            unresolved_seen.add(name)
        if lost_sections:
            gap_rows.append((k.get("q", ""), lost_sections))

    domains = sorted(
        set(list(primary.keys()) + list(trailing_only.keys())),
        key=lambda d: (-primary.get(d, 0), -trailing_only.get(d, 0), d),
    )
    if brand not in domains:
        domains.append(brand)

    ws = wb.create_sheet(safe_sheet(f"{label} fanout gap"))
    ws["A1"] = f"{label} — fan-out visibility | topic: {data.get('topic','')} | {data.get('date','')}"
    ws["A1"].font = Font(bold=True, size=13)
    ws["A2"] = (
        "Primary = cited as the source for a SPECIFIC answer bullet/section (the strong signal). "
        "Trailing-only = appears only in the supplementary source list, backing no specific bullet "
        f"(weak signal). Brand ({brand}) highlighted."
        + (f" Unresolved publisher names seen (add to KNOWN_PUBLISHERS in extract_aio.js): {', '.join(sorted(unresolved_seen))}."
           if unresolved_seen else "")
    )
    ws["A2"].font = Font(italic=True, size=9, color="666666")
    ws["A2"].alignment = Alignment(wrap_text=True)

    hdr_fill = PatternFill("solid", fgColor="1F4E78")
    hdr_font = Font(bold=True, color="FFFFFF", size=10)
    brand_fill = PatternFill("solid", fgColor="FCE4D6")

    HROW = 4
    for j, h in enumerate(["Domain", "Primary citations", "Primary %", "Trailing-only citations", "Mentioned, not cited"], start=1):
        c = ws.cell(row=HROW, column=j, value=h)
        c.font = hdr_font; c.fill = hdr_fill; c.border = BORDER
    r = HROW + 1
    for d in domains:
        p, t = primary.get(d, 0), trailing_only.get(d, 0)
        vals = [d, p, f"{round(100*p/n)}%" if n else "", t, (mentioned_not_cited_count if d == brand else "")]
        for j, v in enumerate(vals, start=1):
            cell = ws.cell(row=r, column=j, value=v)
            cell.border = BORDER
            if d == brand:
                cell.fill = brand_fill
        r += 1

    r += 2
    ws.cell(row=r, column=1, value=f"Sub-facets {brand} did NOT win").font = Font(bold=True, size=11)
    r += 1
    for j, h in enumerate(["Prompt", "Answer section lost", "Won by (publisher)", "Won by (domain)"], start=1):
        c = ws.cell(row=r, column=j, value=h)
        c.font = hdr_font; c.fill = hdr_fill; c.border = BORDER
    r += 1
    for prompt, lost in gap_rows:
        first = True
        for section, cited_as, host in lost:
            ws.cell(row=r, column=1, value=prompt if first else "").border = BORDER
            ws.cell(row=r, column=2, value=section).border = BORDER
            ws.cell(row=r, column=3, value=cited_as).border = BORDER
            ws.cell(row=r, column=4, value=host or "(unresolved)").border = BORDER
            first = False
            r += 1

    ws.column_dimensions["A"].width = 46
    ws.column_dimensions["B"].width = 46
    ws.column_dimensions["C"].width = 26
    ws.column_dimensions["D"].width = 22
    ws.freeze_panes = "A5"

    return {
        "label": label, "n": n,
        "brand_primary": primary.get(brand, 0),
        "brand_trailing_only": trailing_only.get(brand, 0),
        "brand_mentioned_not_cited": mentioned_not_cited_count,
        "top_primary": sorted(primary.items(), key=lambda kv: -kv[1])[:5],
        "unresolved": sorted(unresolved_seen),
    }


BRAND_NAME_RE = re.compile(r"\bpolicy\s*bazaar\b", re.I)


def resolve_target_url(target_urls, prompt, section):
    """Look up a verified target URL for a gap row. Section-keyword match wins
    (more specific) over the prompt-level default. Returns None (not a guess)
    when nothing matches -- the sheet must say so plainly, never invent a URL."""
    if not target_urls:
        return None
    sec_low = (section or "").lower()
    for kw, url in (target_urls.get("by_section_keyword") or {}).items():
        if kw.lower() in sec_low:
            return url
    return (target_urls.get("by_prompt") or {}).get(prompt)


def build_actions_sheet(wb, label, data, brand, min_prompts, target_urls=None):
    """Turns the fan-out gap data into a direct, prioritized action list —
    diagnosis -> prescription. Every row is derived straight from the dataset
    (competitor names, exact answer sections, exact prompts) — nothing invented.
    `target_urls` (optional): {"by_prompt": {prompt: url}, "by_section_keyword":
    {keyword: url}} -- a VERIFIED mapping (e.g. from actually navigating Google
    results, since AI Overview/SERP pages expose no real hrefs to scrape). When
    a row has no match, the Target URL cell says so explicitly rather than
    guessing a plausible-looking URL.
    Needs `sectionCitations` on the dataset; returns None and skips silently
    otherwise (mirrors build_fanout_sheet)."""
    KW = data.get("keywords", [])
    if not any(k.get("sectionCitations") or k.get("trailingSources") for k in KW):
        return None
    n = len(KW)

    losses = {}  # key (host or "name (unresolved)") -> {"name":..., "host":..., "items":[(prompt,section)]}
    offsite_wins = []  # brand's own name cited but with no resolved brand host
    mentioned_not_cited = []
    zero_presence = []

    for k in KW:
        prompt = k.get("q", "")
        hosts = {norm(h) for h in (k.get("hosts") or [])}
        brand_has_any = brand in hosts
        secs = k.get("sectionCitations") or []
        trail = k.get("trailingSources") or []

        for sc in secs:
            h = norm(sc.get("host") or "")
            cited_as = sc.get("citedAs", "")
            section = sc.get("answerSection") or "(intro / no bullet label)"
            if h == brand:
                continue
            if not h and BRAND_NAME_RE.search(cited_as):
                offsite_wins.append((prompt, section, cited_as))
                continue
            key = h or f"{cited_as.strip()} (domain unresolved)"
            entry = losses.setdefault(key, {"name": cited_as.strip(), "host": h, "items": []})
            entry["items"].append((prompt, section))

        if k.get("mentionedNotCited"):
            mentioned_not_cited.append(prompt)
        if not brand_has_any and (secs or trail):
            zero_presence.append(prompt)

    ws = wb.create_sheet(safe_sheet(f"{label} actions"))
    ws["A1"] = f"{label} — direct actions | topic: {data.get('topic','')} | {data.get('date','')}"
    ws["A1"].font = Font(bold=True, size=13)
    ws["A2"] = (f"Every row below is derived directly from this run's {n} prompt(s) — the exact answer "
                "section, the exact competitor that won it. Not generic SEO advice.")
    ws["A2"].font = Font(italic=True, size=9, color="666666")

    hdr_fill = PatternFill("solid", fgColor="1F4E78")
    hdr_font = Font(bold=True, color="FFFFFF", size=10)
    wrap = Alignment(wrap_text=True, vertical="top")
    r = 4

    def section_title(t):
        nonlocal r
        ws.cell(row=r, column=1, value=t).font = Font(bold=True, size=12, color="C55A11")
        r += 1

    def header_row(cols):
        nonlocal r
        for j, h in enumerate(cols, start=1):
            c = ws.cell(row=r, column=j, value=h)
            c.font = hdr_font; c.fill = hdr_fill; c.border = BORDER
        r += 1

    NO_URL = "Not mapped — no verified target URL supplied for this prompt/section"

    # --- Block 1: competitor content gaps, ranked by pressure ---
    section_title(f"1. Content gaps — build/strengthen a page that directly answers these (ranked by how many sub-facets each competitor owns)")
    header_row(["Competitor", "Domain", "Sub-facets they own", "Target URL (update this page)", "Recommended action"])
    ranked = sorted(losses.values(), key=lambda e: -len(e["items"]))
    for e in ranked:
        sections = sorted({s for _, s in e["items"]})
        domain = e["host"] or "unverified — add to KNOWN_PUBLISHERS to confirm"
        urls = sorted({u for u in (resolve_target_url(target_urls, p, s) for p, s in e["items"]) if u})
        url_val = "; ".join(urls) if urls else NO_URL
        action = (f"Publish or strengthen {brand} content that answers, with the same numeric/specific "
                  f"precision, each of: {'; '.join(sections)}. These currently go to {e['name']} instead of us.")
        ws.cell(row=r, column=1, value=e["name"]).border = BORDER
        ws.cell(row=r, column=2, value=domain).border = BORDER
        c = ws.cell(row=r, column=3, value="; ".join(sections)); c.border = BORDER; c.alignment = wrap
        c = ws.cell(row=r, column=4, value=url_val); c.border = BORDER; c.alignment = wrap
        c = ws.cell(row=r, column=5, value=action); c.border = BORDER; c.alignment = wrap
        r += 1
    r += 1

    # --- Block 2: brand's own off-site content winning citations the website should get ---
    if offsite_wins:
        section_title("2. Your own content is winning the citation — but not your website")
        header_row(["Prompt", "Answer section", "What's currently cited", "Target URL (add this content here)", "Recommended action"])
        for prompt, section, cited_as in offsite_wins:
            url_val = resolve_target_url(target_urls, prompt, section) or NO_URL
            action = (f"Publish the substance of \"{cited_as.strip()}\" as an indexable article/page on "
                      f"{brand} answering \"{section}\" — Google is already treating this as the right "
                      "answer, it's just citing a social post instead of the website. Redirect that citation "
                      "by giving it an equivalent web page.")
            ws.cell(row=r, column=1, value=prompt).border = BORDER
            ws.cell(row=r, column=2, value=section).border = BORDER
            ws.cell(row=r, column=3, value=cited_as.strip()).border = BORDER
            c = ws.cell(row=r, column=4, value=url_val); c.border = BORDER; c.alignment = wrap
            c = ws.cell(row=r, column=5, value=action); c.border = BORDER; c.alignment = wrap
            r += 1
        r += 1

    # --- Block 3: named but not cited ---
    if mentioned_not_cited:
        section_title("3. Brand named in the answer, but not cited as a source")
        header_row(["Prompt", "Target URL (most relevant existing page)", "Recommended action"])
        for prompt in mentioned_not_cited:
            url_val = resolve_target_url(target_urls, prompt, "") or NO_URL
            action = ("Google's AI already considers us relevant enough to name — but has no citable page to "
                      "point to for this specific question. Check whether a page exists that answers this "
                      "prompt directly; if it exists, the gap is likely formatting/extractability, not authority.")
            ws.cell(row=r, column=1, value=prompt).border = BORDER
            c = ws.cell(row=r, column=2, value=url_val); c.border = BORDER; c.alignment = wrap
            c = ws.cell(row=r, column=3, value=action); c.border = BORDER; c.alignment = wrap
            r += 1
        r += 1

    # --- Block 4: zero presence at all ---
    if zero_presence:
        section_title(f"4. Zero presence (not even trailing) — of {n} prompts")
        header_row(["Prompt", "Target URL (most relevant existing page)", "Recommended action"])
        for prompt in zero_presence:
            url_val = resolve_target_url(target_urls, prompt, "") or NO_URL
            action = "No citation anywhere in this answer. Check whether a page targeting this exact question exists at all — if not, this is a content-creation gap, not a ranking one."
            ws.cell(row=r, column=1, value=prompt).border = BORDER
            c = ws.cell(row=r, column=2, value=url_val); c.border = BORDER; c.alignment = wrap
            c = ws.cell(row=r, column=3, value=action); c.border = BORDER; c.alignment = wrap
            r += 1

    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 26
    ws.column_dimensions["C"].width = 46
    ws.column_dimensions["D"].width = 46
    ws.column_dimensions["E"].width = 60
    ws.freeze_panes = "A5"

    return {
        "label": label,
        "gap_domains": len(losses),
        "offsite_wins": len(offsite_wins),
        "mentioned_not_cited": len(mentioned_not_cited),
        "zero_presence": len(zero_presence),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True, nargs="+", help='one or more "Label=path.json" (or bare path)')
    ap.add_argument("--out", required=True)
    ap.add_argument("--brand", default="policybazaar.ae")
    ap.add_argument("--min-prompts", type=int, default=2)
    ap.add_argument("--target-urls", help='Optional JSON file: {"by_prompt": {prompt: url}, '
                     '"by_section_keyword": {keyword: url}} of VERIFIED brand URLs, for the '
                     'actions sheet\'s Target URL column. Without it, gap rows say "not mapped" '
                     'instead of guessing a plausible-looking URL.')
    args = ap.parse_args()
    brand = norm(args.brand)
    target_urls = json.load(open(args.target_urls)) if args.target_urls else None

    engines = []
    for tok in args.data:
        if "=" in tok:
            label, path = tok.split("=", 1)
        else:
            label, path = "AI Overview", tok
        engines.append((label.strip(), path.strip()))

    wb = Workbook()
    summaries = []
    fanout_summaries = []
    for i, (label, path) in enumerate(engines):
        try:
            data = json.load(open(path))
        except Exception as e:
            sys.exit(f"Could not read dataset for '{label}' at {path}: {e}")
        if not data.get("keywords"):
            sys.exit(f"Dataset for '{label}' has no keywords.")
        summaries.append(build_engine_sheets(wb, label, data, brand, args.min_prompts, first=(i == 0)))
        fo = build_fanout_sheet(wb, label, data, brand, args.min_prompts)
        if fo:
            fanout_summaries.append(fo)
        build_actions_sheet(wb, label, data, brand, args.min_prompts, target_urls)
    wb.save(args.out)

    print(f"Wrote {args.out}")
    for s in summaries:
        print(f"\n=== {s['label']} ===  prompts: {s['n']}  |  with answer+sources: {s['answered']}")
        print("Rank  Domain                              Cited        Avg pos")
        for i, (d, c, avg) in enumerate(s["leaderboard"], 1):
            tag = "  <- brand" if d == brand else ""
            print("%3d   %-34s %2d/%d (%3d%%)   %s%s" % (i, d, c, s["n"], round(100*c/s["n"]) if s["n"] else 0, avg, tag))
    # combined brand line
    print("\nBrand visibility across engines:")
    for s in summaries:
        print(f"  {s['label']:<14} {brand}: cited {s['brand']['cited']}/{s['n']}, avg pos {s['brand']['avg']}")

    if fanout_summaries:
        print("\nFan-out visibility (primary = won a specific answer sub-facet; trailing-only = supplementary list only):")
        for fo in fanout_summaries:
            print(f"  {fo['label']:<14} {brand}: primary {fo['brand_primary']}/{fo['n']}, "
                  f"trailing-only {fo['brand_trailing_only']}, mentioned-not-cited {fo['brand_mentioned_not_cited']}")
            print(f"    Top primary-citation winners: " +
                  ", ".join(f"{d} ({c})" for d, c in fo["top_primary"]))
            if fo["unresolved"]:
                print(f"    Unresolved publisher names (add to KNOWN_PUBLISHERS in extract_aio.js): {', '.join(fo['unresolved'])}")


if __name__ == "__main__":
    main()
