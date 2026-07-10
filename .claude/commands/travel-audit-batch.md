# /travel-audit-batch — run one batch of the travel-insurance content audit

Working dir for all commands: `tools/travel-audit/` in the PolicyBazaar Claude workspace.
State + outputs live in `/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Travel Insurance/Result/Final Audit/` (the pipeline's self-contained working directory since 2026-07-10 — ledger, per-URL JSON, master xlsx, tracker, and per-URL reports all live there; `Result/` root above it holds only older/unrelated files).

**Cadence: manually invoked by Aakash, gauged by his usage dashboard** (Settings →
Usage on claude.ai), not an automated loop. Same two-limit model as the health audit:
a fast **current-session** window (hours-scale, recovers quickly) and a **weekly** cap
per model/plan (fixed reset, NOT pushed later by retries). The weekly cap is the real
constraint — the travel audit (432 pages) shares the same seat as the health audit
(~990 pages) and Aakash's other daily work. Claude cannot see the dashboard itself:
before invoking a batch, check it and skip/delay if weekly usage is already high.
**Never run a health batch and a travel batch concurrently** — they share the same
session and weekly limits, and 2 concurrent heavy agents has failed every test.

## One-time setup (before the first batch)

State is seeded from Aakash's provided URL list, cross-checked against the sitemap
snapshot — NOT from the sitemap alone:
1. Aakash provides the travel URL list → save as `tools/travel-audit/travel-urls.txt`.
2. Diff it against `tools/travel-audit/sitemap-travel-2026-07-10.txt`; report any URL
   present in one but not the other to Aakash before seeding.
3. `python3 filter_urls.py` — builds `audit-state.csv` (refuses to overwrite existing state).
Tier rules (confirmed 2026-07-10): destination + visa pages A-core; news/podcast B;
`fifty-national-day-uae` + `ceo-blog` excluded.

## Per-invocation loop

1. **Status:** `python3 state.py summary` — report counts to Aakash. If zero pending and
   zero in_progress → the travel audit is complete: stop and propose running the
   consistency engine (`python3 consistency.py`).
2. **Recover:** `python3 state.py reset-stale` — returns crashed in_progress rows to pending.
3. **Take a batch:** priority order A-core → A-articles → B. Batch sizes follow the
   health audit's evidence (2026-07-08 testing): the dial is total concurrent
   **full-depth ("heavy")** load, not raw agent count — two heavy agents at once has
   failed every time. **Safe pattern: 1 Tier-A agent per batch, optionally paired with
   1 Tier-B (light) agent alongside it.** Don't run two Tier-A agents concurrently
   until that's specifically re-tested and proven.
   `python3 state.py take 1 A-core batch-YYYY-MM-DD-N` (falls through to
   `A-articles` then `B` when the tier is exhausted). The JSON it prints is the batch.
   Only increase batch size after a batch completes with **zero retries**, and
   increase by the smallest possible step.
4. **Run the workflow:** Read `agent-prompt.md`, then invoke the Workflow tool with
   `scriptPath: tools/travel-audit/workflow-batch.js` and
   `args: { batch: <the JSON from step 3>, promptTemplate: <agent-prompt.md content>,
   auditDate: "<today YYYY-MM-DD>" }`.
5. **Mark failures:** for every workflow result with status "failed":
   `python3 state.py fail "<url>" "<failure_reason>"`.
6. **Collect:** `python3 collector.py --dry-run` (sanity), then `python3 collector.py`.
7. **Refresh the tracker:** `python3 tracker.py` — regenerates
   `Result/Final Audit/policybazaar-travel-audit-tracker.xlsx` from the current
   `audit-state.csv`. This is the human-facing status file Aakash checks — always
   run it right after collector.py so it never goes stale. It's a generated view
   (fully rewritten every run); never edit the tracker xlsx by hand.
8. **Report to Aakash:** done/failed counts this batch, cumulative summary
   (`python3 state.py summary`), score range, and any URL that failed twice
   (needs manual attention — do NOT silently retry forever). If a batch hits the
   current-session limit, reset stale rows and tell Aakash to check the usage
   dashboard before the next invocation rather than immediately retrying.

## Hard rules

- Never fabricate audit data after a tool failure — mark failed, report, move on.
- Never touch the master xlsx except through `collector.py` (append-only).
- One collector run at a time; the workflow agents never write xlsx/state themselves.
- No automated polling loop for this command — it runs when Aakash invokes it.
- Before picking up a batch, `Final Audit/policybazaar-travel-audit-tracker.xlsx`
  (or `python3 state.py summary`) is the source of truth for what's done — check it
  instead of guessing or re-deriving progress from memory.
