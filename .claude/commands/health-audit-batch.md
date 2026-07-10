# /health-audit-batch — run one batch of the health-insurance content audit

Working dir for all commands: `tools/health-audit/` in the PolicyBazaar Claude workspace.
State + outputs live in `/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result/`.

**Cadence: manually invoked by Aakash, gauged by his usage dashboard** (Settings →
Usage on claude.ai), not an automated loop. This account has two separate limits:
a fast **current-session** window (hours-scale, recovers quickly — this is what
threw "session limit" errors during testing on 2026-07-08) and a **weekly** cap
per model/plan (fixed reset, e.g. "Fable: 66% used, resets Thu 10:29 PM" — NOT
pushed later by retries, confirmed via the dashboard). The weekly cap is the real
constraint for a ~990-page project sharing a seat with Aakash's other daily work —
Claude cannot see this dashboard itself, so before invoking a batch, check it and
skip/delay if weekly usage is already high.

## Per-invocation loop

1. **Status:** `python3 state.py summary` — report counts to Aakash. If zero pending and
   zero in_progress → Task 1 is complete: stop and propose running the consistency engine
   (`python3 consistency.py`).
2. **Recover:** `python3 state.py reset-stale` — returns crashed in_progress rows to pending.
3. **Take a batch:** priority order A-core → A-articles → B. **Batch sizes are
   evidence-based, not the plan's original 12/40.** Observed on 2026-07-08:
   - 5 concurrent (mixed depth): 1.4M tokens across retries, 0/5 completed.
   - 4 concurrent, all Tier A-core (full-depth): 588K tokens, 0/4 completed.
   - 2 concurrent (1 full-depth Tier A + 1 light Tier B): **succeeded**, ~295K
     tokens, ~13.5 min, zero retries.
   - 2 concurrent, BOTH Tier A-core (full-depth): **failed**, 241K tokens (less
     than the successful mixed batch), 0/2 completed.
   The dial that matters is total concurrent **full-depth ("heavy")** load, not
   raw agent count — two heavy agents at once has failed every time, even below
   the token total of a batch that succeeded. **Safe pattern: 1 Tier-A agent per
   batch, optionally paired with 1 Tier-B (light) agent alongside it.** Don't run
   two Tier-A agents concurrently until that's specifically re-tested and proven.
   `python3 state.py take 1 A-core batch-YYYY-MM-DD-N` (falls through to
   `A-articles` then `B` when the tier is exhausted). The JSON it prints is the batch.
   Only increase batch size after a batch completes with **zero retries**, and
   increase by the smallest possible step — size/token-total alone hasn't
   predicted success reliably; each step up needs its own proof.
4. **Run the workflow:** Read `agent-prompt.md`, then invoke the Workflow tool with
   `scriptPath: tools/health-audit/workflow-batch.js` and
   `args: { batch: <the JSON from step 3>, promptTemplate: <agent-prompt.md content>,
   auditDate: "<today YYYY-MM-DD>" }`.
5. **Mark failures:** for every workflow result with status "failed":
   `python3 state.py fail "<url>" "<failure_reason>"`.
6. **Collect:** `python3 collector.py --dry-run` (sanity), then `python3 collector.py`.
7. **Refresh the tracker:** `python3 tracker.py` — regenerates
   `Result/Final Audit/policybazaar-health-audit-tracker.xlsx` from the current
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
- Before picking up a batch, `Final Audit/policybazaar-health-audit-tracker.xlsx`
  (or `python3 state.py summary`) is the source of truth for what's done — check it
  instead of guessing or re-deriving progress from memory.
