# /health-audit-batch — run one batch of the health-insurance content audit

Working dir for all commands: `tools/health-audit/` in the PolicyBazaar Claude workspace.
State + outputs live in `/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result/`.

## Per-session loop

1. **Status:** `python3 state.py summary` — report counts to Aakash. If zero pending and
   zero in_progress → Task 1 is complete: stop and propose running the consistency engine
   (`python3 consistency.py`).
2. **Recover:** `python3 state.py reset-stale` — returns crashed in_progress rows to pending.
3. **Take a batch:** priority order A-core → A-articles → B. **Batch sizes are
   evidence-based, not the plan's original 12/40** — a 5-concurrent-agent batch
   burned 1.4M tokens across retries with zero completions before hitting the
   account's session limit, while a 2-concurrent batch (1 full-depth Tier A +
   1 light Tier B) completed cleanly on the first try in ~295K tokens / ~13.5 min
   (2026-07-08 pilot). Start conservative and scale only after a batch completes
   with **zero retries** (check the workflow's per-agent `attempt` count / journal —
   a batch that needed retries should not be sized up):
   - Tier A (A-core, A-articles): start at **4**, not 12.
   - Tier B: start at **12**, not 40.
   `python3 state.py take 4 A-core batch-YYYY-MM-DD-N` (falls through to
   `A-articles` then `B` when the tier is exhausted). The JSON it prints is the batch.
   If a batch completes with zero retries, the next batch may increase by roughly
   50% (e.g. 4 → 6 → 9); if a batch needs any retry or hits the session limit,
   drop back to the last size that succeeded cleanly.
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
