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
     tokens, ~13.5 min, zero retries.
   - 2 concurrent, BOTH Tier A-core (uniformly full-depth): **failed**, 241K
     tokens (less than the successful mixed batch), 0/2 completed, session limit.
   **The dial that matters is total concurrent full-depth ("heavy") load, not
   raw agent count.** The only combination ever proven to work is exactly
   **1 heavy (Tier A) agent at a time**, optionally paired with 1 light (Tier B)
   agent alongside it. Two heavy agents at once has failed every time it's been
   tried, even when the resulting token total was lower than a batch that
   succeeded. **Current safe starting point: 1 Tier-A agent per batch** (add a
   Tier-B agent alongside it once that pattern proves stable again, don't add a
   second Tier-A agent).
   **The reset time moves later with every failed attempt** (observed: 4am → 3:10pm
   → 4:10pm across today's failures, each roughly an hour after the failing
   attempt) — this looks like a rolling usage window, not a fixed daily reset.
   Concretely: retrying too soon or too big does not just fail harmlessly, it
   pushes the recovery point further out. Treat every session-limit hit as a
   reason to WAIT LONGER before the next attempt, not just until the stated
   reset time — and drop to the smallest untested-safe size (1 Tier-A agent
   alone) rather than repeating the size that just failed.
   `python3 state.py take 1 A-core batch-YYYY-MM-DD-N` (falls through to
   `A-articles` then `B` when the tier is exhausted). The JSON it prints is the batch.
   Only increase batch size after a batch completes with **zero retries** (check
   the workflow's per-agent `attempt` count / journal), and increase by the
   smallest possible step — the failures above show size/token-total alone
   doesn't predict success; each step up needs its own proof. Any retry or
   session-limit hit means: drop back to the last size that worked, reset stale
   rows, and stop attempting further batches for a meaningfully longer window
   than the stated reset — retrying at the reset boundary has already caused a
   repeat failure once today.
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
