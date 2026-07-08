# /health-audit-batch — run one batch of the health-insurance content audit

Working dir for all commands: `tools/health-audit/` in the PolicyBazaar Claude workspace.
State + outputs live in `/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result/`.

## Per-session loop

1. **Status:** `python3 state.py summary` — report counts to Aakash. If zero pending and
   zero in_progress → Task 1 is complete: stop and propose running the consistency engine
   (`python3 consistency.py`).
2. **Recover:** `python3 state.py reset-stale` — returns crashed in_progress rows to pending.
3. **Take a batch:** priority order A-core → A-articles → B. **Batch sizes are
   evidence-based, not the plan's original 12/40 — and evidence keeps revising
   them down.** Observed so far (2026-07-08):
   - 5 concurrent (mixed depth): 1.4M tokens across retries, 0/5 completed, session limit.
   - 4 concurrent, all Tier A-core (uniformly full-depth + fact-check): 588K tokens,
     0/4 completed, session limit — despite using *fewer* total tokens than the
     5-agent failure, suggesting the binding constraint is concurrent load/rate
     (simultaneous heavy streaming calls), not total token budget.
   - 2 concurrent (1 full-depth Tier A + 1 light Tier B): **succeeded**, ~295K
     tokens, ~13.5 min, zero retries. This is the only combination proven to work.
   **Current safe starting point: batch size 2, for ANY tier.** A same-tier batch
   of 2 (e.g. 2× A-core) is UNTESTED — treat it as the next experiment, not an
   assumed-safe step up from the proven 1+1 mixed case.
   `python3 state.py take 2 A-core batch-YYYY-MM-DD-N` (falls through to
   `A-articles` then `B` when the tier is exhausted). The JSON it prints is the batch.
   Only increase batch size after a batch completes with **zero retries** (check
   the workflow's per-agent `attempt` count / journal), and increase by 1 at a
   time, not by ratio — the failures above show size alone doesn't predict
   success; each step up needs its own proof. Any retry or session-limit hit means:
   drop back to the last size that worked, reset stale rows, and stop attempting
   further batches until the session limit's stated reset time has passed —
   retrying immediately just burns more quota against the same wall.
4. **Run the workflow:** Read `agent-prompt.md`, then invoke the Workflow tool with
   `scriptPath: tools/health-audit/workflow-batch.js` and
   `args: { batch: <the JSON from step 3>, promptTemplate: <agent-prompt.md content>,
   auditDate: "<today YYYY-MM-DD>" }`.
5. **Mark failures:** for every workflow result with status "failed":
   `python3 state.py fail "<url>" "<failure_reason>"`.
6. **Collect:** `python3 collector.py --dry-run` (sanity), then `python3 collector.py`.
7. **Report to Aakash:** done/failed counts this batch, cumulative summary
   (`python3 state.py summary`), score range, and any URL that failed twice
   (needs manual attention — do NOT silently retry forever).

## Hard rules

- Never fabricate audit data after a tool failure — mark failed, report, move on.
- Never touch the master xlsx except through `collector.py` (append-only).
- One collector run at a time; the workflow agents never write xlsx/state themselves.
