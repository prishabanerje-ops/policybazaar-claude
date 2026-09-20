# 2026-07-06 — Graphify Install & First Graph Build

**Status:** DONE (install + first build) — follow-ups below are OPEN.
**Source:** Installed https://github.com/Graphify-Labs/graphify (v0.9.6) and built the first knowledge graph of this workspace.

## What was done (record)

- Verified the PyPI package `graphifyy` (double-y) is legitimate — its repo link redirects to Graphify-Labs/graphify. Installed from the GitHub repo directly via `pip3 install git+https://github.com/Graphify-Labs/graphify` (permission classifier blocked the PyPI name).
- CLI at `~/Library/Python/3.14/bin/graphify`; PATH line added to `~/.zshrc` (line 3).
- `graphify claude install` → wrote `## graphify` section in CLAUDE.md + two PreToolUse hooks in `.claude/settings.json` (nudge toward `graphify query` before grep/Read; only active when `graphify-out/graph.json` exists). Hooks confirmed firing.
- `graphify install --platform claude` → `/graphify` skill at `~/.claude/skills/graphify/SKILL.md` + a small global `~/.claude/CLAUDE.md` trigger note. **Restart Claude Code sessions opened before this for /graphify to register.**
- First build (`/graphify .`): **58 nodes, 98 edges, 9 communities** over 28 files (~21k words). Outputs in `graphify-out/`: `graph.html`, `GRAPH_REPORT.md`, `graph.json`, plus extraction cache (re-runs on unchanged files are free). Token cost: ~130k (subagent extraction of 24 md docs; code was free AST).

## Open follow-ups

| # | Item | Notes | Size | Status |
|---|---|---|---|---|
| 1 | Health warning: 16 dangling-endpoint edges | Edges point to files outside the scanned corpus (claude-seo plugin scripts — plugin dir is git-ignored/own repo). Decide: rebuild with plugins included, or accept as known loose ends | S | ☐ decision |
| 2 | Trace the top bridge question | "Why does Workspace Layout (hub-based) bridge 4 communities?" — betweenness 0.229. Run `graphify query "<question>"` | XS | ☐ |
| 3 | Verify 2 INFERRED edges on AI Search Hub Skill | vs Hub Router Pattern and Data Integrity Policy — model-reasoned, unverified | XS | ☐ |
| 4 | Weakly-connected settings nodes | `$schema`, `NODE_ENV`, `allow`, `deny`, `PreToolUse`, `github@claude-plugins-official` flagged as near-orphans — settings.json noise; the whole 11-node settings cluster (cohesion 0.18) is a disconnected component with no textual link to the rest. Consider excluding `.claude/settings.json` from future builds | XS | ☐ |
| 5 | Keep graph current | After doc/code changes run `graphify update .` (AST-only, free). Optional: post-commit auto-rebuild hook (`references/hooks.md` in the skill) | XS | ☐ recurring |
| 6 | Optional: Gemini key for semantic extraction | Set `GEMINI_API_KEY` + `pip install 'graphifyy[gemini]'` to move doc extraction off Claude subagents (cheaper rebuilds) | S | ☐ decision |
| 7 | Commit the integration | CLAUDE.md graphify section + settings.json hooks are uncommitted; `graphify-out/` should probably be gitignored first | XS | ☐ |
| 8 | **Merge 3 duplicate node pairs in graph.json** | AST vs semantic extractors wrote mismatched IDs (semantic = leading `_` + `_script` suffix), so dedup missed `build_matrix.py`, `extract_aio.js`, `extract_chatgpt.js` — each exists twice. Consequences: the 7-node Python-function cluster floats disconnected, both `extract_*.js` AST twins are degree-0 isolates, and sidebar communities 7 & 8 ("AI Overview Extractor: 1", "ChatGPT Source Extractor: 1") are artifacts, not real communities. Fix: merge each pair (keep one node, rewire edges), rerun `--cluster-only`, regenerate `graph.html` + `GRAPH_REPORT.md` + labels. Caveat: shrink-guard refuses a smaller graph.json (58→55 nodes) — needs careful/forced write. A plain rebuild would reproduce the bug (extractor ID schemes), so fix via graph.json surgery. Expected after fix: components 5→2, communities 9→~7, main-component coverage 65.5%→~85% | S | ☐ |
