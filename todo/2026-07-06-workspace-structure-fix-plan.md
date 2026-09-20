# 2026-07-06 — Workspace Structure Fix Plan

**Status:** OPEN — audited 2026-07-06, none of the fixes applied yet.
**Source:** Full folder-structure audit (drift, dead files, hub → playbook routing).
**Audit verdict:** All 33 hub → playbook routes resolve. Both venvs healthy (Python 3.14.6, deps verified). All three repos (root, claude-seo, linkedin) clean. Findings below are hygiene + reachability, nothing blocks daily work.

Sizes: XS = under 5 min · S = 5–15 min · M = 15–45 min. Total if all approved: ~45 min.

## At a glance

| # | Finding | Current state | Usability today | Size | Status |
|---|---|---|---|---|---|
| 1 | `/seo-interlinking` call in scrape skill | Broken reference — targets an unregistered skill | Scrape works to step 4, step 5 improvised | XS | ☐ |
| 2 | `debate` plugin unreachable | Code + venv healthy; no route, not registered | 0% — nothing triggers it | S–M | ☐ decision |
| 3 | GoogleTrendsMCP not wired | Server + venv healthy; `mcpServers` empty everywhere | 0% — server never starts | S | ☐ decision |
| 4 | `deploy` skill vs command collision | Two divergent copies both registered as "deploy" | Works; which copy wins is luck | S | ☐ |
| 5 | `security-review` vs security-guidance plugin | Project skill + plugin skill share the name | Works; same ambiguity | S | ☐ |
| 6 | `post-linkedin.skill` zip | Dead 6.4 KB artifact, tracked in linkedin repo | No impact, clutter | XS | ☐ |
| 7 | Run outputs committed in claude-seo repo | 3 tracked files its own ignore policy excludes | Repo hygiene only | XS | ☐ |
| 8 | Run-output clutter in claude-seo root | ~7 ignored items on disk inside plugin dir | Violates archive/ rule | XS | ☐ |
| 9 | CLAUDE.local.md stale | Venv + `~/.claude/commands` claims now false | Misleads future sessions | XS | ☐ |
| 10 | Dead root `.gitignore` entry | Ignores nonexistent `.claude/skills/post-linkedin/` | None | XS | ☐ |
| 11 | Uncommitted `.claude/settings.json` | Legit github-plugin enable, in working tree | Risk of being lost | XS | ☐ |

## Batch A — mechanical, no decisions (#1, 6–11)

1. **Fix scrape route** — `.claude/skills/scrape/SKILL.md` line 82 (step 5): replace "invoke `/seo-interlinking` with the topic" with "Read `~/.claude/plugins/claude-seo/skills/seo-interlinking/SKILL.md` and follow it with the topic". Commit to root repo.
6. **Linkedin repo** — `git rm post-linkedin.skill`, commit "chore: remove stale packaged export of pre-rename skill".
7. **claude-seo repo** — append `cluster-plan.json`, `cluster-plan.md`, `.playwright-mcp/` to plugin `.gitignore`; `git rm --cached cluster-plan.json cluster-plan.md ".playwright-mcp/page-2026-05-14T12-51-38-950Z.yml"`; commit. Files stay on disk (moved in #8).
8. **Sweep plugin-root clutter → `archive/claude-seo-run-outputs/`**: `FULL-AUDIT-REPORT.md`, `ACTION-PLAN.md`, `Google-SEO-Report-policybazaar.ae-cwv-audit.html`, `charts/`, `cluster-map.html`, `cluster-plan.*`, `.playwright-mcp/` logs. Delete `.pytest_cache/` and `skills/seo-google/scripts/__pycache__/` outright (regenerable). All gitignored — no commit needed.
9. **CLAUDE.local.md** — replace venv bullet with: venvs recreated on this machine (Python 3.14.6, deps verified 2026-07-06); correct symlink bullet: symlinks exist in `~/.claude/skills` and `~/.claude/plugins` only, `~/.claude/commands` is empty.
10. **Root `.gitignore`** — remove `.claude/skills/post-linkedin/` line.
11. **Commit `.claude/settings.json`** — "chore: enable github plugin at project scope". Can share a commit with #1 and #10.

Commit plan: three commits total — root repo (#1, #10, #11, #9 is gitignored so no commit), linkedin repo (#6), claude-seo repo (#7).

## Batch B — needs Aakash's call (#2–5)

2. **debate plugin** —
   - **Option A (recommended, S):** thin router skill at `.claude/skills/debate/SKILL.md` → "Read `~/.claude/plugins/debate/skills/debate/SKILL.md` and follow it exactly", with proper trigger description. Update CLAUDE.md skill count 8 → 9.
   - Option B (M): register as local plugin — needs a `marketplace.json` added + `/plugin` install in an interactive session. Little payoff over A.
3. **GoogleTrendsMCP** — decide: still used?
   - Yes → create root `.mcp.json`:
     ```json
     {
       "mcpServers": {
         "google-trends": {
           "command": "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/GoogleTrendsMCP/venv/bin/python3",
           "args": ["/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/GoogleTrendsMCP/server.py"]
         }
       }
     }
     ```
     Requires one-time approval in an interactive session.
   - No → move `.claude/mcp/GoogleTrendsMCP/` to `archive/`.
4. **deploy merge** — keep the skill (`.claude/skills/deploy/SKILL.md`, documented in CLAUDE.md); fold in the command's `allowed-tools` and `<staging|production>` argument hint; delete `.claude/commands/deploy.md`. Rollback section survives. `fix-issue` and `review` commands untouched.
5. **security-review collision** — add `"security-guidance@claude-plugins-official": false` under `enabledPlugins` in project `.claude/settings.json` so the tailored project skill wins here, plugin stays available elsewhere. Verify the per-project disable takes effect in an interactive session; fallback = rename project skill (e.g. `pb-security-review`).

## Suggested order

Batch A in one pass → #4, #5 → #2 Option A → #3 after the keep/archive decision on Trends.
