# Global Rules — Aakash Srivastava (PolicyBazaar UAE)

## Greeting
Always begin every response with "Hi Aakash".

## Tool Failure Policy
If any tool call fails (403, 404, timeout, empty response, or any error), STOP immediately.
- Do NOT proceed using inferred or assumed data.
- Do NOT present fabricated numbers, rankings, or analysis as if the tool had succeeded.
- Report the failure: what failed, what data is missing, and what's needed to unblock.

## Data Integrity
Never present inferred, extrapolated, or assumed information as retrieved fact.
Distinguish explicitly between "retrieved from the page" vs. "inferred from snippets", and "tested in an AI system" vs. "estimated from general knowledge".
If a claim can't be verified, say so — do not fill the gap with a confident guess.

## Workspace layout

- `.claude/skills/` — 8 skills, no symlinks. Six hubs + two dev skills:
  - `seo` — hub routing to ~20 claude-seo playbooks (audit, technical, schema, sitemap, interlinking, backlinks, broken-links, local, maps, drift, images, image-gen, google, dataforseo, ecommerce, hreflang, campaign). `/seo audit example.com`
  - `content` — hub: quality/E-E-A-T, briefs, clustering, strategy, competitor pages, programmatic. `/content brief <topic>`
  - `ai-search` — AI-citation scraping (default) + routes to seo-geo and seo-sxo. `/ai-search <topic>`
  - `uae-insurance` — RACE flow, insurance page audits, leads intel. `/uae-insurance leads`
  - `scrape` — modes: all (default) / news / qna / reviews. `/scrape news <topic>`
  - `linkedin` — modes: write (default) / feed engage / reply to own-post comments. Has its own git repo.
  - `deploy`, `security-review` — dev workflow, standalone.
- Hubs are ROUTERS: pick the matching dispatch row, Read that file, follow it. Never answer from the hub file itself.
- `.claude/plugins/claude-seo/` — THE canonical SEO plugin (own git repo, local fork — do NOT re-clone or overwrite). Absorbed the best of aakash-seo (2026-07-06); aakash-seo is retired — do NOT reinstall it or searchfit-seo.
- `.claude/plugins/debate/` — self-built multi-model review plugin (only copy — do not delete).
- `.claude/mcp/GoogleTrendsMCP/` — Google Trends MCP server.
- `.claude/agents/ai-overview-scraper.md` — scraper agent used by the ai-search skill.
- `archive/` — ALL retired material (old datasets/decks, archived standalone skills, aakash-seo.bundle, claude-seo run outputs). Gitignored.
- The workspace root is a git repo (since 2026-07-06). `.claude/plugins/`, `.claude/mcp/`, and `.claude/skills/linkedin/` are ignored — they have their own repos.
