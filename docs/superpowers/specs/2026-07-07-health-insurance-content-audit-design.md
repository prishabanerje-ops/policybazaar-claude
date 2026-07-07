# Health Insurance Content Audit at Scale — Design

**Date:** 2026-07-07
**Owner:** Aakash Srivastava
**Status:** Approved (brainstorming session 2026-07-07)

## Goal

Run the five-lens `/content-audit` (SEO + GEO + AI-detection + YMYL + fact-check) across
every English health-insurance page on policybazaar.ae (~990 URLs), producing:

- **Task 1:** one dated `.md` report per URL + rows appended to the rolling master
  workbook `policybazaar-insurance-content-audit.xlsx`.
- **Task 2:** after Task 1 completes, a cross-site consistency check — every factual
  claim checked against verified truth AND against every other page stating the same
  fact — delivered as a consistency report `.md` plus a **Consistency** sheet in the
  master workbook.

## Non-goals

- Arabic (`/ar-ae/`) pages — excluded from this run.
- Fixing the content. This run audits and reports; rewrites are follow-up work.
- Non-health verticals (car, travel, life, etc.).

## 1. URL set & tiering

**Source of truth:** `.claude/skills/content/content-audit/assets/policybazaar-urls.txt`
(July 2026 live snapshot).

**Filter (anchored):** a URL is in scope if it matches any of:

- suffix `-hipvd/$`, `-hiart/$`, `-hic/$`, `-hinh/$`, or `-hicf/$`
- path contains `/health-insurance/` or `/network-hospitals/`

…AND does not contain `/ar-ae/`. Deduplicate the result.

The raw regex Aakash supplied (`health-insurance/|hipvd|hiart|hic|hinh|hicf|/network-hospitals/`)
over-matches: bare `hic` hits "w**hic**h" and "ve**hic**les" (car/term pages), and Arabic
duplicates slip in. Anchoring yields **~990 URLs** vs 1,122 raw.

**Tiers:**

| Tier | Pages | Count | Depth |
|---|---|---|---|
| A — core | `/health-insurance/` plan, city, category, comparison pages (~264); `-hipvd/` provider pages (12); `-hic/` category pages (5); `/health-insurance/tpa/` (4); `/health-insurance/health-guide/` (16) | ~300 | Full five-lens incl. per-claim web fact-check |
| A — articles | `/health-insurance/articles/` (293) + legacy `-hiart/` (119) | ~412 | Full five-lens, batched |
| B — light | Hospital listings (`/health-insurance/hospitals/` 104, `/network-hospitals/` 97, `-hinh/` 3); claim forms `-hicf/` (14); glossary (19); news-and-update (41) | ~278 | Template-family audit + per-page essentials |

**Tier B "light" definition:** one full five-lens audit per page *family* (e.g. one
representative hospital-listing page, one claim-form page) to score the shared template;
then every other page in the family gets a reduced per-page pass: title/meta/H1,
page-specific facts (hospital name/location, insurer name, form links resolve),
duplicate/thin-content risk, and any fact-checkable claim unique to that page. Each Tier B
page still gets its own `.md` (shorter) and its own workbook rows, with template-level
findings referenced once, not repeated 200 times.

## 2. State file — the run's backbone

`audit-state.csv` in
`/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result/`
(the doubled `Documents/Documents` is correct).

One row per URL:

```
url, slug, page_type, tier, status, seo, geo, human_likeness, ymyl, fact_check,
overall, md_file, json_file, audit_date, batch_id, failure_reason
```

`status` ∈ `pending | in_progress | done | failed`.

- Created once from the filtered URL list before the first batch.
- Every session reads it, takes the next N `pending` URLs, marks them `in_progress`,
  and updates rows as agents finish. Fully resumable across sessions/days.
- **Failure policy (per global rules):** a fetch/tool failure marks the row `failed`
  with `failure_reason`; nothing is inferred or fabricated. Failed rows are retried in
  a later batch; persistent failures are reported to Aakash, not papered over.

## 3. Per-URL agent output (parallel workers)

Execution uses multi-agent workflow orchestration (explicitly approved 2026-07-07):
each batch fans out parallel subagents, one URL each. Each agent runs the existing
`/content-audit` skill (URL MODE, all five lenses at its tier's depth) and writes:

1. **`policybazaar-<page-slug>-content-audit-YYYY-MM-DD.md`** — the full report per the
   existing convention, in the Result folder. Date = actual run date. Slug = last URL
   path segment; on slug collision across sections, prefix the section
   (e.g. `articles-<slug>`).
2. **`audit-data/<slug>.json`** (subfolder of Result) — structured mirror of the report:

```json
{
  "url": "...", "slug": "...", "page_type": "...", "tier": "A-core",
  "audit_date": "YYYY-MM-DD", "mode": "URL",
  "scores": {"seo": 0, "geo": 0, "human_likeness": 0, "ymyl": 0, "fact_check": 0, "overall": 0},
  "parameters": [{"lens": "seo", "name": "...", "score": 0, "max": 0, "status": "ok|warn|fail", "finding": "..."}],
  "findings": [{"lens": "...", "severity": "...", "found": "...", "why": "...", "fix": "..."}],
  "fact_checks": [{"claim": "...", "verification": "...", "correct_value": "...",
                   "source": "...", "source_tier": "Primary|Secondary|Snippet-only",
                   "status": "Confirmed|Contradicted|Outdated|Unverifiable"}],
  "ledger_entries": [{"fact_key": "dha-ebp-annual-premium", "page_value": "AED 320",
                      "verified_value": "AED 320", "source": "...", "source_tier": "...",
                      "status": "..."}],
  "schema_audit": [...],
  "priority_recs": [{"priority": "...", "issue": "...", "action": "..."}]
}
```

`ledger_entries.fact_key` is a normalized kebab-case key for the underlying fact — the
join key Task 2 groups on. Agents pick keys from a shared, growing key registry
(`audit-data/fact-keys.md`) and add new keys when a fact isn't listed yet; the collector
flags near-duplicate keys for merge.

Agents do NOT touch the xlsx or the state CSV scores — that's the collector's job.

## 4. Serial collector (after each batch)

A single-threaded step (openpyxl script) that, per batch:

1. Loads `policybazaar-insurance-content-audit.xlsx` (creates with the standard 7 sheets
   if missing) and **appends** rows from each new JSON — Summary, Lens Scores, Findings,
   Fact-Check, Schema, Priority Recs, Verification Ledger. Never overwrites; re-audits
   append new rows (before/after history preserved).
2. Updates `audit-state.csv` rows to `done`/`failed` with scores and filenames.
3. Reports batch results on-screen: done/failed counts, score distribution, notable
   findings.

**Batch cadence:** ~10–15 Tier A audits or ~30–50 Tier B audits per session. Aakash
re-invokes (or `/loop`s) sessions until the state file shows zero `pending`.

**Pilot batch first:** batch 1 is 5 URLs spanning page types (1 core plan page,
1 provider `-hipvd/`, 1 article, 1 hospital listing, 1 claim form) to validate the JSON
schema, collector, and workbook layout before scaling. Aakash reviews pilot output
before batch 2.

## 5. Task 2 — consistency engine

Runs once Task 1 is complete (state file: no `pending`/`in_progress`; `failed` rows
acknowledged by Aakash).

1. Read all `audit-data/*.json`; group `ledger_entries` by `fact_key` (after the
   key-merge pass).
2. For each fact, flag:
   - **Truth violations** — a page's value contradicts the verified external value
     (Contradicted/Outdated in Task 1).
   - **Internal disagreements** — pages give different values for the same fact where
     no external source arbitrates (platform figures like "plans from AED X"), including
     facts individually marked Unverifiable.
3. Deliverables:
   - **`policybazaar-health-consistency-report-YYYY-MM-DD.md`** — per fact: canonical
     value + source, every page stating it, who disagrees, and a page-by-page fix list
     ordered by traffic/importance (core pages first).
   - **Consistency sheet** appended to the master workbook:
     `Fact Key · Canonical Value · Source · Source Tier · URL · Page Value · Verdict
     (consistent / truth-violation / internal-disagreement) · Fix`.

## Error handling

- Any tool failure (403/404/timeout/empty) → row marked `failed` + reason; no inferred
  data ever enters a report, the workbook, or the ledger (global tool-failure policy).
- Agent crash mid-batch → row stays `in_progress`; next session resets stale
  `in_progress` rows (no JSON present) to `pending`.
- Collector validates each JSON against the schema before appending; malformed JSON →
  row `failed`, agent re-run in a later batch.
- xlsx corruption guard: collector writes to a temp copy and replaces the master only
  on successful save.

## Testing / validation

- **Pilot batch (5 URLs)** validates end-to-end: agent output format, JSON schema,
  collector append, workbook layout, state transitions.
- Collector script gets a dry-run mode (parse JSONs, print rows, don't write).
- Spot check: after batch 2, Aakash reviews 2–3 `.md` reports against the live pages.

## Open items for the implementation plan

- Exact worker-count per workflow run (bounded by rate limits observed in the pilot).
- Seed list for `fact-keys.md` (start from the verified figures already in memory,
  e.g. AED 320 EBP scheme figures).
