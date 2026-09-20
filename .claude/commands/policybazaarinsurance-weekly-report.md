# /policybazaarinsurance-weekly-report — weekly migration & leads report for policybazaarinsurance.ae

Purpose: track leads, bookings, GSC rankings, GA4 organic traffic, and crawl
stats for policybazaarinsurance.ae after the 2026-08-11 platform migration, comparing
each week against (a) the fixed pre-migration baseline and (b) the previous
week. Audience: CTO, Tech, CMO. Output is a **Markdown report** (headline
numbers first, then per-product tables — every table carries its own
baseline/this-week/since-migration date-range caption, added 2026-08-24) —
it has no "To:"/recipient line and no "Leads file: ..." line in the header,
both removed at Aakash's request on 2026-08-24; don't add them back.

**Date captions show the nominal window, not proof of full data coverage
(fixed 2026-08-24):** the "This Week"/"Since Migration" end date always
matches the leads file's latest date, but GSC (and crawl stats) commonly lag
1-3 days behind that, so the window can include a day or two with no real
GSC/crawl data yet — nothing is estimated or backfilled for those days, the
script just sums whatever real rows exist and still divides by the full
nominal day-count (so a partial window understates the rate, never
overstates it). Whenever a source's actual coverage falls short for a given
window, this is tracked as a coverage gap and surfaced to the reader —
**wording simplified to plain language on 2026-08-31**, then **consolidated
from a per-table note into ONE note at the end of the report, same date**
(Aakash: "every note is saying the same thing, make 1 note that can be added
in the end" — the old version repeated near-identical text up to 4x when
GSC/GA4/crawl stats all lagged the same day, e.g. one after Overall Metrics,
one or two after Crawl Stats, one after By-Product GSC). Current mechanism:
`check_coverage(summary)` returns `(latest_date, missing_days)` per
source/window if short, `record_coverage()` collects these into a
`coverage_issues` list as tables render, and `render_coverage_note()` groups
them by `(source, latest_date)` — so e.g. GSC lagging in both "This Week"
and "Since Migration" with the same latest date becomes one line, not two —
and renders a single italic note placed after the `## Notes` section, right
before the closing `---`. Example output: "_Data coverage note: GSC (This
Week & Since Migration) through 2026-08-29, Crawl Stats (This Week & Since
Migration) through 2026-08-29 — the most recent day(s) haven't been reported
yet. This is routine lag, not an error; per-day rates above are still
divided by the full window, so they read a little low until the rest comes
in, never high._" Don't remove this mechanism entirely (same protection as
below) — Aakash asked this exact coverage question (thinking the date might
be wrong) before it existed on 2026-08-24; the 2026-08-31 changes only
touched wording and placement, not whether the underlying gap-detection
fires.

**No "Flags" section** — removed at Aakash's request on 2026-08-24 (it had
started duplicating what the tables and the Enquiries-vs-Leads bullets
already show). Do not re-add a Flags section without him asking for it back;
see the "Per-invocation steps" note below on what replaces it.

**No conversion/booking-rate metric** — removed at Aakash's request on
2026-08-24. Leads/day and Bookings/day are shown as raw counts only; do not
re-add a conversion percentage without him asking for it back.

**Two separate lead-funnel dates — do not conflate them (added 2026-08-24):**
- `enquiry_created_at` = a visitor reached the form, whether or not they
  completed it. Always populated (546/546 rows in the file verified
  2026-08-24).
- `lead_creation_date` = an actual lead record was created. Only populated
  when the form was actually completed — 360/546 rows (66%) in that same
  file; the other 186 are visits that never became a lead.
- **"Leads/day" everywhere in this report means `lead_creation_date` counts,
  never `enquiry_created_at` counts.** Before 2026-08-24 this script counted
  every `enquiry_created_at` row as a "lead," which is wrong — verified
  against the real file, that overstated leads by ~52% in the week checked
  (reported 7.86 leads/day when the real figure was 1.62/day since
  migration). If this distinction is ever lost in a future edit, the report
  is silently wrong again in the same way — the "Enquiries vs Leads" section
  exists specifically to keep this visible (there is no separate FLAGS
  section anymore — see below).
- The report always shows both counts side by side (`## Enquiries vs Leads —
  Funnel`) with the before/after-migration change for each, plus a form
  completion rate (lead ÷ enquiry) — this section exists because Aakash asked
  2026-08-24 to be told explicitly if either count rose or dropped after
  migration, not just leads. As of that date: enquiries **rose** 4.90→5.85/day
  (+19%) since migration while leads **dropped** 3.37→1.62/day (-52%) —
  i.e. traffic reaching the form held up, but far fewer of those visits
  turned into an actual lead. That gap is itself the signal worth
  investigating (a form/submission bug on the new platform is one plausible
  cause, not confirmed) — don't let a future report bury this by only
  showing the leads number. (The italic `enquiry_created_at`/`lead_creation_date`
  definition line that used to sit under this heading was removed at Aakash's
  request on 2026-08-24 — the table + the two rose/dropped bullets carry this
  on their own now; don't re-add the definition line.)

**Verdict column — added 2026-08-31, Aakash's request.** Every comparison
table (Overall Metrics, Crawl Stats, Enquiries vs Leads Funnel, and all three
By-Product tables) carries a trailing `Verdict` column: ▲ Improved /
▼ Declined / ➖ Flat, comparing the "before" value to the "after" value —
Baseline → Since Migration everywhere except Overall Metrics, which compares
Baseline → This Week (since that table has no Since-Migration column).
Implementation: `verdict_arrow(before, after, higher_is_better=...)` in
`generate_report.py` — reuse it for any new comparison row rather than
duplicating the logic.
- **Direction-aware:** pass `higher_is_better=False` for metrics where a
  smaller number is the good outcome — currently GSC Avg Position and Crawl
  Avg Response Time. Every other metric defaults to `higher_is_better=True`.
  Get this backwards and the verdict reads exactly opposite to reality, so
  check the flag when adding a new metric row.
- **±5% counts as Flat** (`flat_pct=5.0` default) — avoids a false-precision
  Improved/Declined call on noise-level moves.
- **Zero-baseline edge case:** if the "before" value is 0, any nonzero
  "after" value is called Improved/Declined per `higher_is_better` (there's
  no percentage to compute); 0 → 0 is Flat.
- The By-Product GSC table shows two verdicts per row (`Clicks / Position`)
  since that table has three sub-metrics (clicks, impressions, position) and
  a single verdict would hide which one is actually driving it. This was my
  implementation choice, flagged to Aakash in the same response — no
  explicit sign-off yet on collapsing it to one combined verdict, so leave
  as two until he says otherwise.
- Don't silently remove or revert this column — it was an explicit ask, same
  protection as the other 2026-08-24/2026-08-31 additions in this file.

**Cadence: manually invoked by Aakash, roughly weekly.** No automated loop —
this command runs only when he types `/policybazaarinsurance-weekly-report`.

**What Aakash needs to provide each week (added 2026-08-24):** two manual
file drops, both into the same "Ranking And Leads" folder — **not** an equal
pair, they fail differently:
1. **Leads CSV** (`Leads-YYYY-MM-DD.csv`) — **required**. No file → the
   script exits with an error and the run stops; nothing is generated.
2. **Crawl Stats CSV** (`Crawl-Stats-YYYY-MM-DD.csv`) — **optional**. No file
   → the report still generates in full, it just skips the Crawl Stats
   section with a note (a WARNING is printed, not an error).

GSC and GA4 data need no manual input — pulled live via API each run.

## Data path reference

| What | Path |
|---|---|
| Leads input (Aakash drops a new file weekly) | `/Users/aakashsrivastava/Documents/PolicyBazaar Research/PolicyBazaar Insurance/Ranking And Leads/Leads-YYYY-MM-DD.csv` |
| Crawl stats input (Aakash drops a new file weekly, added 2026-08-24) | `/Users/aakashsrivastava/Documents/PolicyBazaar Research/PolicyBazaar Insurance/Ranking And Leads/Crawl-Stats-YYYY-MM-DD.csv` |
| Report output (generated each run) | `/Users/aakashsrivastava/Documents/PolicyBazaar Research/PolicyBazaar Insurance/Result/weekly-report-<latest-lead-date>.md` |
| Script | `tools/policybazaarinsurance-weekly-report/generate_report.py` |

**Crawl Stats — manual paste, no API (added 2026-08-24):** Google Search
Console's Settings > Crawl Stats report has no public API, so this is a
weekly manual drop just like the leads file: `date,total_crawl_requests,
avg_response_time_ms` (snake_case header row Aakash pastes into a CSV, one
row per day, straight from the GSC UI export). Picks the *lexicographically
latest* `Crawl-Stats-YYYY-MM-DD.csv` in the same "Ranking And Leads" folder,
same convention as leads. **If the file is missing, the report still
generates — the section is skipped with a note, it does not hard-fail** (crawl
stats are supplementary, unlike leads/GSC/GA4 which are core). Avg response
time is **request-weighted** (weighted by that day's `total_crawl_requests`,
not a plain average of daily averages) so a low-volume day with a freak
response time doesn't skew the period average.

**Leads file naming:** must match `Leads-YYYY-MM-DD.csv` exactly — the script
picks the *lexicographically latest* matching filename in the folder, so the
date in the filename must be the export date. If Aakash hasn't dropped a new
file since the last run, the script will silently reuse the old one — always
tell him which file/date range it actually used (the script prints this) so a
stale file doesn't go unnoticed.

**Leads file schema** — page-level export, verified against a real file on
2026-08-24. Required columns: `enquiry_created_at`, `lead_creation_date`,
`referer_url`, `product_name`, `ape`, `status`. `status == "Sale Complete"` is
the conversion signal (confirmed 1:1 with `booking_id` being populated on
2026-08-24) — see the enquiry/lead distinction above for what the two date
columns mean; do not treat them as interchangeable. This
is a **different, richer schema** than an earlier daily-rollup export Aakash
sent on 2026-08-19 (`product, date: Day, Distinct values of leadid...`) — if a
future file comes in that older rollup shape instead, the script will fail
loudly with a clear "missing expected columns" error naming what it found.
**Do not silently reshape a rollup-format file to fit** — stop and ask Aakash
which schema is now current, the same way this was resolved in the
2026-08-24 conversation that built this command.

## Fixed reference constants (do not re-derive each run)

- Migration go-live: **2026-08-11**
- Pre-migration baseline window: **2026-07-12 to 2026-08-10** (30 days)
- GSC property: `https://www.policybazaarinsurance.ae/`
- GA4 property: `366756478` (verified live and correctly scoped to this domain
  on 2026-08-19 — do NOT use property `309894472`, that's policybazaar.ae's
  property, or `333930486`, a decoy property under the same GA4 account with
  zero traffic despite a matching default URI)

## Product → URL mapping (for the GSC/GA4 cross-reference table)

High confidence (single, unambiguous URL prefix): Health Insurance
(`health-insurance`), Car Insurance (`car-insurance`), Travel Insurance
(`travel-insurance`), Income Protection (`income-protection-insurance`), Term
Insurance (`term-insurance`).

Lower confidence, disclosed in every report's Notes section:
- **Investment** is a 4-way grouping across `/investment-plans/`, `/lic/`,
  `/mutual-funds/`, `/bonds/` — the site splits this into four sections, the
  CRM tracks it as one product.
- The site's `/life-insurance/` section gets real traffic but **does not
  correspond to any of the 6 CRM products** — reported separately, never
  folded into Term.

## Per-invocation steps

1. Run the script:
   ```bash
   cd "tools/policybazaarinsurance-weekly-report"
   SSL_CERT_FILE=$(python3 -m certifi) python3 generate_report.py
   ```
   (The `SSL_CERT_FILE` prefix is required on this machine — see the
   `python-ssl-cert-workaround` memory.)
2. If it errors, **stop and report the exact error** — do not fabricate
   numbers to fill the gap. Common failure modes:
   - No `Leads-*.csv` in the folder → tell Aakash to drop this week's export.
   - Column-schema mismatch → surface the exact missing-columns message, ask
     which schema is current (see above), do not guess a remapping.
   - GSC/GA4 API error → report which API failed and the raw error; GSC
     data lags 2-3 days, so a request for "today" will always be partial for
     the most recent day(s) — this is expected, not a fetch error. (There is
     no FLAGS section to surface this automatically anymore — see step 4.)
   - No `Crawl-Stats-*.csv` in the folder → this is **not** a hard failure,
     the script prints a warning and the report just skips the Crawl Stats
     section with a note — still tell Aakash so he knows to drop a fresh
     export if he wants that section back.
3. On success, the script prints the Markdown report to stdout and saves it
   to the `Result/` path above. Show Aakash the full Markdown directly in
   the response — this is a scannable digest for CTO/Tech/CMO, don't wrap it
   in additional commentary that pushes the actual numbers below the fold.
4. **There is no "Flags" section in the report** (removed 2026-08-24) — the
   tables now speak for themselves with explicit date ranges (and an
   auto-generated coverage note wherever GSC/GA4/crawl data falls short of
   the window, added 2026-08-24 — see above), so scan them yourself and call
   out anything notable in your own words in the chat response (e.g. a >20%
   WoW or since-migration swing in leads, a GSC position that got
   meaningfully worse, a product with leads but zero bookings, or a notable
   crawl-requests or response-time swing since migration). Don't assume
   Aakash will independently spot these from the raw report text.
5. Remind Aakash (only if relevant that run): this produces a Markdown
   report — there is no send capability
   connected yet. If he later wants an actual Gmail draft, that requires
   authorizing the Gmail MCP connector first.

## Hard rules

- Never fabricate leads, GSC, or GA4 numbers if a data source fails — stop,
  report what failed and what's needed, exactly per this project's Tool
  Failure Policy.
- Never silently change the product→URL mapping or the migration/baseline
  dates without Aakash's explicit sign-off — these were verified against live
  data, not assumed.
- If the leads file's date range doesn't extend past the migration date yet,
  say so plainly (the Enquiries vs Leads section already handles this — see
  above) — don't imply a "since migration" comparison exists when it doesn't.
- Every table carries an explicit date-range caption (added 2026-08-24) —
  don't remove these captions, and don't reintroduce the italic funnel-
  definition line or a Flags section, without Aakash's explicit sign-off —
  the same protection given to the migration/baseline date constants
  themselves.
- Don't remove the Verdict column (added 2026-08-31) or the coverage-gap
  note (`check_coverage()` / `record_coverage()` / `render_coverage_note()`,
  added 2026-08-24, reworded and consolidated into one end-of-report note
  2026-08-31) without Aakash's explicit sign-off — same protection as above.
  Wording/placement tweaks to either are fine; dropping them outright is not.
