# social-performance — Facebook + Instagram Performance Reporting — Design

**Date:** 2026-09-11
**Owner:** Aakash Srivastava (building for handoff to another PolicyBazaar UAE team member via GitHub)
**Status:** Approved (brainstorming session 2026-09-11)

## Goal

Build a Claude Code skill, `social-performance`, that generates a recurring
performance report for PolicyBazaar UAE's Facebook Page and Instagram
Business account, using the official Meta Graph API. Posting is handled by
an external agency and is explicitly out of scope — this tool is read-only:
pull metrics, compute derived/composite scores, produce a report, and
optionally email it.

This is the first of three independent sub-projects identified during
brainstorming (the other two — competitor research and trend monitoring —
are out of scope here and get their own specs later).

## Non-goals

- **No posting/publishing.** No Graph API publish calls, no content creation
  or scheduling of posts. An agency owns posting.
- **No personal-profile automation.** Business Page + Instagram Business
  account only, via the official Graph API — no browser automation.
- **No competitor tracking or trend monitoring.** Separate sub-projects.
- **No LinkedIn/YouTube/TikTok reporting in v1.** The skill name is kept
  platform-agnostic (`social-performance`, not `meta-performance`) so these
  can be added later without a rename, but v1 implements Facebook + Instagram
  only.
- **No hard dependency on other skills in this workspace.** Specifically,
  the Content Quality Score's fact-check step must not require the
  `content-audit` skill to be installed — this repo is going to be handed to
  someone else via GitHub and must work standalone.
- **No committed secrets.** No Meta tokens, account IDs used as auth, or
  recipient email addresses are committed to git. Everything credential- or
  installer-specific lives in a gitignored `.env` and a local config file.

## Context: why this is designed for portability

This skill will be pushed to its own GitHub repo (same pattern as the
existing `linkedin` skill: own git repo, cloned into `.claude/skills/`) and
handed to another PolicyBazaar UAE team member who also uses Claude Code.
She will run it against the **same** Facebook Page and Instagram Business
account this design was scoped against, but:

- She needs her **own** Meta Developer App and long-lived Page access token
  (Meta tokens are issued per-app/per-developer, not transferable as a
  shared secret checked into a repo).
- She needs to authorize her **own** Gmail connector for the email step.
- She configures her **own** recipient list and cadence.

Nothing about *her* setup should require re-reading this design doc or
asking Aakash — the skill's own README/setup doc must be self-sufficient.

## Architecture

Own git repo at `.claude/skills/social-performance/`, same structural
pattern as `.claude/skills/linkedin/`:

```
social-performance/
├── SKILL.md                  # entry point, mode routing, invocation docs
├── README.md                 # setup instructions (Meta App, tokens, Gmail connector, cron)
├── .env.example               # documents required env vars, no real values
├── .gitignore                 # excludes .env, data/snapshots/*.json (account-specific history)
├── config.example.json        # cadence + recipient list template
├── scripts/
│   ├── graph_client.py        # Meta Graph API calls (read-only)
│   ├── metrics.py             # raw -> derived/composite metric computation
│   ├── snapshot_store.py      # read/write local JSON history for deltas
│   ├── report.py              # renders dated .md + appends rolling .xlsx
│   └── quality_score.py       # Content Quality Score (fact-check gate + weighted blend)
├── references/
│   └── metric-definitions.md  # exact formula + Graph API field per metric, incl. verification status
├── data/
│   └── snapshots/              # gitignored — per-account JSON history, created at runtime
└── tests/
    ├── test_metrics.py
    ├── test_snapshot_store.py
    └── test_quality_score.py
```

`SKILL.md` documents the one invocation mode for v1: generate a report for a
given period (default: since the last snapshot). Cron-scheduled and manual
invocations both go through the same code path in `report.py`; the only
difference is who/what triggers it, per the "Scheduling & email" section
below.

## Auth (manual, one-time, per-installer)

Each installer (Aakash, and separately the team member) does this once in
their own Meta Developer account:

1. Create a Meta Developer App.
2. Request permissions: `pages_read_engagement`, `read_insights`,
   `instagram_basic`, `instagram_manage_insights`.
3. Link the PolicyBazaar UAE Facebook Page and its connected Instagram
   Business Account to the app.
4. Generate a long-lived Page access token.
5. Record the Page ID, IG Business Account ID, and token in a local `.env`
   (copied from `.env.example`, never committed).

`README.md` walks through these steps explicitly, since neither Aakash nor
this session can complete another person's Meta App creation/App Review for
her — this is out of band from the code itself.

| Variable | Purpose |
|---|---|
| `META_PAGE_ACCESS_TOKEN` | Long-lived Page access token |
| `META_PAGE_ID` | Facebook Page ID |
| `META_IG_BUSINESS_ACCOUNT_ID` | Instagram Business Account ID linked to the Page |

## Data flow

1. **Load config** — `config.json` (cadence, recipient list) + `.env`
   (credentials/IDs). Neither is committed; both are gitignored, with
   `.example` templates committed instead.
2. **Pull raw data** via `graph_client.py`:
   - List Page posts and IG media published in the report period, tagged by
     type (static image, video/reel, carousel, link).
   - Per-post/per-media insights (reach, impressions, engagement actions,
     video metrics where applicable).
   - Account-level insights (current follower count; page-level reach).
3. **Update snapshot** via `snapshot_store.py` — append this period's raw
   totals (follower count, reach, per-post engager user IDs) to
   `data/snapshots/<account>.json`. This is what makes delta metrics
   (Net New Followers MoM, Total Reach Growth Rate, repeat-engager rate)
   possible, since the Graph API only exposes current-state totals, not
   historical deltas across arbitrary windows.
4. **Compute metrics** via `metrics.py` — combines this period's raw pull
   with the snapshot history to produce every metric in the table below.
5. **Compute Content Quality Score** via `quality_score.py` (see formula
   below).
6. **Render report** via `report.py` — a dated `.md` file
   (`report-YYYY-MM-DD.md`) plus an append to a rolling, undated `.xlsx`,
   matching the convention already used by `content-audit` and the weekly
   PB Insurance report skill in this workspace.
7. **Email step** (see Scheduling & email below) — draft only; requires
   explicit human approval before anything sends.

## Metrics (Facebook + Instagram)

Both platforms unless noted. "Computed from snapshot" means the raw Graph
API value alone isn't enough — it requires the stored history from step 3.

| Metric | Source | Notes |
|---|---|---|
| Video Output per Week | Graph API media list, filtered by type | Direct count |
| Static Output per Week | Graph API media list, filtered by type | Direct count |
| Content Quality Score | `quality_score.py` | See formula below |
| Total Reach Growth Rate | Computed from snapshot | This period's reach vs. prior period, from history |
| Reach | Graph API insights | Direct |
| Impressions per Video | Graph API insights | Video-post impressions ÷ video post count |
| Hook Rate | Graph API insights | **Needs verification** — see Open Risks |
| Hold Rate | Graph API insights | **Needs verification** — see Open Risks |
| Average Watch Time | Graph API insights | **Needs verification** — see Open Risks |
| AVT (Long Videos) — FB only | Graph API insights | **Needs verification**; split by video duration |
| AVT (Short Videos) — FB only | Graph API insights | **Needs verification**; split by video duration |
| Engagement Rate (ER) | Computed | (likes + comments + shares + saves) ÷ reach |
| Total Shares — IG only | Graph API insights | Direct |
| Net New Followers MoM | Computed from snapshot | This period's follower count vs. snapshot from ~1 month prior |
| Loyalty/Retention Rate | Computed | Repeat-engager rate: accounts engaging with >1 post in period ÷ total unique engagers. Requires per-post engager lists from Graph API — **needs verification** for rate limits/availability, see Open Risks |
| Total Followers | Graph API insights | Direct |

`references/metric-definitions.md` will carry the exact Graph API endpoint
and field name for each row, with a status column (`verified` /
`needs verification` / `approximated — see note`), filled in during
implementation, not assumed now.

## Content Quality Score

Per-post score, then averaged for the period:

1. **Fact-check gate (pass/fail):** A lightweight, self-contained check
   (no dependency on the `content-audit` skill) that flags posts making
   unverifiable or contradicted factual claims (e.g. premium figures,
   regulatory citations). A failed check caps the post's score at a low
   fixed floor regardless of the other components — exact floor value
   decided during implementation, documented in
   `references/metric-definitions.md`.
2. **Normalized post performance (70% weight):** engagement/reach for this
   post relative to the account's trailing baseline (e.g. rolling average
   over the last N periods from snapshot history), not a raw number —
   so a "good" post is graded relative to that account's own recent norm.
3. **Time-sensitivity (30% weight):** whether the post's content was still
   relevant/current at publish time (e.g. not a stale seasonal reference
   posted after the relevant period). Scoring rubric finalized during
   implementation.

## Scheduling & email

- **Manual invocation:** running the skill's report mode generates the
  report, shows a summary in chat, and asks whether to send the email now.
- **Cron-triggered invocation:** a scheduled job (via this workspace's
  `schedule`/CronCreate tooling) at installer-configured cadence
  (daily/weekly/biweekly/monthly, set in `config.json`) generates the
  report and sends a notification to the installer — it does **not**
  auto-send. The email only goes out after explicit approval, identical
  behavior to the manual path.
- **Delivery mechanism:** the installer's own authorized Gmail connector.
  Each installer (Aakash, and separately the team member) must authorize
  this themselves in their own claude.ai connector settings — this cannot
  be done from within a session on their behalf.
- **Recipients:** a list in `config.json`, editable per installer. Not
  hardcoded, not committed with real values.

## Error handling

Following this workspace's code-style rule (error messages include what was
attempted and with what input): any Graph API failure surfaces the endpoint,
account/post ID, and HTTP status — never silently falls back to a
partial/fabricated report. If a metric can't be computed (e.g. missing
snapshot history for a first-ever run, so growth-rate metrics have no prior
period to compare against), the report explicitly marks that metric as
"insufficient history" rather than omitting it silently or showing a
zero/misleading value.

## Testing

Per this workspace's testing rules:

- Mock the Graph API at the HTTP boundary (`graph_client.py`'s HTTP calls),
  never call the live API in tests.
- `metrics.py` and `quality_score.py` are pure functions tested with
  specific input → output values, no snapshot tests for logic.
- Test names describe behavior (e.g. `computes zero engagement rate when
  reach is zero`, `caps quality score at floor when fact-check fails`).
- `snapshot_store.py` tested for correct read/write/append behavior against
  a temp file, including the "no prior snapshot exists yet" case.

## Open questions / risks

- **Graph API field verification (blocking, first implementation step):**
  Hook Rate, Hold Rate, Average Watch Time, and the long/short video AVT
  split are not confirmed against live Meta Graph API documentation in this
  design. The first implementation task must verify each field's existence
  and exact name against Meta's current docs (or a real API call), and
  either implement it directly or define an explicit, documented
  approximation — never silently assume a field name.
- **Repeat-engager rate feasibility:** computing this requires fetching
  per-post engager lists across every post in the period, which may hit
  rate limits at scale or have Meta-side restrictions on what commenter/
  liker data is exposed. Needs a feasibility check early in implementation;
  if infeasible, this metric is marked "insufficient data" rather than
  faked.
- **Content Quality Score weighting/floor exact values:** the 70/30 split
  and fact-check-fail floor are directional decisions from brainstorming;
  exact numeric constants are finalized during implementation and recorded
  in `references/metric-definitions.md`.
- **First-run cold start:** with no prior snapshot, MoM/growth-rate metrics
  have nothing to compare against. The report must say so explicitly for
  that first run rather than showing a misleading 0% or omitting the row.
