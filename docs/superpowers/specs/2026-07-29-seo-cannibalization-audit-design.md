# SEO Keyword Cannibalization Audit — `seo-cannibalization` Skill — Design

**Date:** 2026-07-29
**Owner:** Aakash Srivastava
**Status:** Approved (brainstorming session 2026-07-29)

## Goal

Build a data-backed keyword cannibalization audit for PolicyBazaar UAE's Health and
Travel Insurance verticals: identify which URLs are competing against each other for
the same search queries, cross-reference GSC, GA4, SEMrush position tracking, and
leads data, and produce a detailed Excel workbook with prioritized, evidence-cited
recommendations (redirect / consolidate / differentiate / reinforce-signals). Every
recommendation must cite the specific numbers behind it — no unsupported suggestions.

## Non-goals

- **Other verticals (car, life, home, SME) are out of scope for v1.** Leads and SEMrush
  position-tracking data only exist for Health and Travel Insurance in this workspace.
  A whole-site pass would fall back to GSC-only evidence for those verticals — weaker
  than the four-source cross-reference this design relies on — so it's explicitly
  deferred rather than delivered at lower rigor.
- **Not a full-site content-similarity/crawl-based duplicate detector.** This approach
  (Option C below) was considered and rejected as the primary method: crawling and
  scoring every site URL for topic similarity is expensive and prone to false positives
  (similar topic ≠ actually competing in the SERP). Limited use only: a canonical/title
  spot-check on the top-priority flagged pairs.
- **Not continuous/scheduled monitoring.** This is an on-demand audit
  (`/uae-insurance cannibalization`), not a cron job, in v1.
- **Does not execute redirects or content edits.** Output is a recommendation report;
  implementing the recommendations (redirects, content rewrites, canonical changes) is
  a separate, later action taken by Aakash.

## Context — data sources verified this session

All four sources were checked live (not assumed) before this design was written:

| Source | Status | Detail |
|---|---|---|
| **GSC** | Tier 1, live | OAuth token expired but auto-refreshes via refresh_token; property `sc-domain:policybazaar.ae` |
| **GA4** | Tier 2, live-verified | Was unconfigured at session start (no `ga4_property_id`). Configured this session: property `309894472` added to `~/.config/claude-seo/google-api.json`; missing `google-analytics-data` SDK installed; confirmed with a real 7-day `top-pages` pull (real landing-page/session data returned) |
| **SEMrush position tracking** | Local CSV, not live API | The `claude.ai Semrush` MCP connector requires OAuth unavailable in this headless session. Instead uses existing local exports: `Position.csv` per vertical — Health: 80 tracked keywords, weekly snapshots 2025-06-04 → 2026-06-09 then daily from Apr 2026; Travel: 120 tracked keywords, same structure (verified row counts, same SEMrush project/report format for both). Each week's columns give position, SERP feature type, and **landing URL** |
| **Leads** | Local CSV | `Leads.csv` per vertical with `referer_url` attribution — Health: 48,067 rows; Travel: 31,317 rows |

Paths (existing, from `seo-leads-intel`'s Data Path Reference — reused, not duplicated):

```
Health leads CSV   → PolicyBazaar Research/Health Insurance/Ranking And Leads/Leads.csv
Travel leads CSV   → PolicyBazaar Research/Travel Insurance/Ranking And Leads/Leads.csv
Health SEMrush CSV → PolicyBazaar Research/Health Insurance/Ranking And Leads/Position.csv
Travel SEMrush CSV → PolicyBazaar Research/Travel Insurance/Ranking And Leads/Position.csv
```

While inspecting `Position.csv`, one real, already-verified cannibalization example
surfaced: the tracked keyword **"compare health insurance uae"** shows its ranking
landing URL flipping between `/health-insurance/` and the homepage `/` across multiple
weeks — the classic signature of Google being unable to settle on which page to rank.
This is cited as evidence the methodology below will surface real, existing issues; it
has not yet been through the full correlation/scoring pipeline.

## 1. Detection methodology — 3 options considered

**Option A — GSC query/page overlap (recommended, primary method).** Pull Search
Console Search Analytics with `dimensions=query,page` over a trailing window,
site-wide. Group by query; any query where ≥2 distinct URLs both receive real
impressions is a live cannibalization signal observed directly from Google's own
data — not inferred from content similarity.

**Option B — SEMrush landing-URL churn only.** Watch the 200 tracked keywords across
both `Position.csv` files for cases where the ranking landing URL flips between two
site URLs across weeks. Cheap, and gives strong historical trend evidence, but only
covers keywords someone already chose to track — misses long-tail cannibalization
entirely.

**Option C — Content-similarity / crawl-based duplicate detection.** Crawl all site
URLs, compute content/topic similarity, flag near-duplicate pages regardless of current
ranking. Most thorough for catching structural duplication early, but expensive and
prone to false positives.

**Decision: A is the backbone, B is folded in as corroboration/trend evidence, C's
ideas are used only as a light spot-check** (canonical tag + title/H1, via the existing
`fetch_page.py` / `parse_html.py`) on the top-priority flagged pairs only — not a
full-site crawl.

**Scoping rule:** GSC pages are **not** filtered by URL path prefix (e.g.
`/health-insurance/*`). The homepage-vs-topic-page example above proves that filtering
by path would miss real cannibalization where one competing URL sits outside the
vertical's own path. Instead, scope is by **query relevance**: a query is in-scope if
it matches either vertical's existing entity/intent keyword taxonomy — already defined
in `seo-insurance-ae/SKILL.md` (`$VERTICAL_ENTITIES` + `$VERTICAL_INTENTS` for
Vertical 2 — Health, and Vertical 3 — Travel; reused as-is, not redefined) — or the
query appears in that vertical's SEMrush tracked list in `Position.csv`.

## 2. Time window

**12 months trailing**, matching `seo-leads-intel`'s existing convention. Long enough
to capture a full seasonal cycle for both verticals (travel insurance in particular has
strong seasonal query patterns — e.g. country-specific and Hajj-season travel queries)
without diluting results with old, potentially already-fixed issues. (16 months —
GSC's max retention — and 6 months were considered and rejected: 16 months adds little
beyond a longer tail of stale history; 6 months risks missing seasonal-only
cannibalization.)

## 3. Flagging thresholds & severity

| Rule | Threshold |
|---|---|
| Query in-scope | Matches the vertical's `$VERTICAL_ENTITIES`/`$VERTICAL_INTENTS` taxonomy (`seo-insurance-ae/SKILL.md`), OR is in that vertical's SEMrush tracked list |
| Flagged as cannibalization | ≥2 distinct URLs each receive **≥10 impressions** in the 12-month window for that query |
| Escalated to **high severity** | The non-primary (losing) URL also has **≥1 click**, OR SEMrush shows the landing URL switching **≥2 times** in its tracked history |

Thresholds are conservative on purpose — the goal is negligible false positives, per
Aakash's explicit priority on data-backed accuracy over raw finding count.

## 4. Recommended-action decision logic

| Pattern observed | Recommended action |
|---|---|
| One URL gets nearly all clicks/leads for the query; the other gets ~0 | 301 redirect the loser → winner |
| Both URLs get meaningful clicks/leads, but for genuinely different sub-intents | Differentiate content: retarget titles/H1s so they stop competing on the shared head-term |
| Two near-duplicate pages, both indexed, both getting some traffic | Consolidate: merge best content into one page, 301 the other |
| Canonical already correctly set, but Google still surfaces the "wrong" URL | Reinforce signals (internal linking, sitemap priority) — not a new redirect |

Every row in the report cites the specific GSC/GA4/SEMrush/Leads numbers that produced
its classification.

## 5. Excel report structure

One workbook, five sheets:

1. **Executive Summary** — counts by vertical/severity/action type; total impressions
   and leads affected
2. **Cannibalization Pairs** — query, vertical, URLs involved, GSC impressions/clicks/
   position per URL, GA4 sessions/bounce per URL, leads count per URL (matched via
   `referer_url`), SEMrush churn count, severity score, recommended action, rationale
3. **Recommended Actions** — one row per action item: URL(s), action type, concrete
   steps, priority (P0/P1/P2)
4. **Data Sources & Methodology** — exact date ranges, GSC/GA4 properties used,
   thresholds applied, and known gaps (below) — so nothing in sheets 1–3 is mistaken
   for more certain than it is
5. **Raw flagged query data** — the underlying pulled rows for in-scope flagged
   queries only (not the full unfiltered site-wide pull), for Aakash's own follow-up
   analysis

## 6. Architecture

New sub-skill: `claude-seo/skills/seo-cannibalization/SKILL.md`, mirroring
`seo-leads-intel`'s phase structure (credential check → parallel ingest → correlation
script → report), because it shares the same four data sources and the same vertical
scope:

- **Ingest** (reuses existing scripts unchanged): `gsc_query.py` (dimensions=query,page,
  12mo), `ga4_report.py` (top-pages), `leads_import.py` (per vertical),
  `semrush_import.py` (per vertical)
- **New script — `cannibalization_correlate.py`**: joins the four JSON outputs, applies
  the in-scope query filter, flagging thresholds, severity scoring, and action-logic
  table above. Follows the same CLI/JSON-output convention as `leads_correlation.py`
  (docstring, `argparse`, `--json` flag).
- **New script — `cannibalization_report.py`**: writes the 5-sheet Excel workbook via
  `openpyxl` (already a pinned dependency — no new install needed).
- **Hub wiring**: add one row to `uae-insurance/SKILL.md`'s router table —
  `cannibalization / duplicate ranking` → `seo-cannibalization/SKILL.md`.
- **Output location**: `PolicyBazaar Research/Cannibalization/Result/cannibalization-report-{TODAY}.xlsx`
  (new sibling folder to the existing Health/Travel Insurance folders, since this
  report spans both verticals in one combined workbook).

## 7. Known gaps / caveats (to surface in the report's Methodology sheet, not hide)

- GA4 was only just configured (property `309894472`, this session) — historical data
  itself was already being collected by the existing GA4 property, but this is the
  first time this pipeline has queried it. Any anomalies in early runs should be
  checked against the GA4 UI directly before being trusted.
- SEMrush position tracking covers only 200 keywords total across both verticals.
  Cannibalization on queries outside this tracked list relies on GSC evidence alone
  (still valid — GSC is the primary signal — but without the SEMrush churn
  corroboration column populated).
- GSC anonymizes/omits very low-volume query rows per Google's own privacy thresholds;
  a small amount of long-tail cannibalization below that threshold is inherently
  invisible to this method, from any tool.

## Testing / verification

Per this repo's testing conventions (mock at the boundary, never mock internal logic;
regression test per bug fix), and mirroring the existing
`tests/test_leads_correlation.py` / `tests/test_semrush_import.py` pattern already in
the claude-seo plugin:

- **`test_cannibalization_correlate.py`** — unit tests against fixture JSON (not live
  API calls) covering: exact query-overlap detection, a no-overlap control case (must
  NOT flag), the 10-impressions threshold boundary (9 vs. 10), the high-severity
  escalation rules (1 click boundary; churn-count boundary), and each of the four
  action-logic branches.
- **`test_cannibalization_report.py`** — verifies the generated workbook has the
  correct 5 sheets, correct headers, and that summary counts in Sheet 1 reconcile with
  the row count in Sheet 2.
- **End-to-end check against real data**: once implemented, run the full skill against
  the live Health + Travel data, then manually spot-check 2–3 flagged pairs against the
  GSC UI directly (Search Console → Performance → filter by query) to confirm the
  reported impressions/clicks match — verifying the pipeline against ground truth
  before the report is treated as final.
