# Workspace Restructure — Design

**Date:** 2026-07-06
**Status:** Approved by Aakash (brainstorming session 2026-07-06)
**Scope:** `/Users/aakashsrivastava/Documents/PolicyBazaar Claude` — the whole Claude Code workspace.

## Problem

The workspace has grown organically and is hard to understand:

- `.claude/skills/` holds **50 flat entries**: 10 real skill folders + 29 symlinks into `plugins/claude-seo` + 11 symlinks into `plugins/aakash-seo`.
- The two SEO plugins overlap heavily: 10 of aakash-seo's 11 skills duplicate a claude-seo skill, including a **same-name collision** (`seo-audit` exists in both; the symlink silently picks claude-seo's).
- `post-linkedin` exists twice with diverging content: canonical in `.claude/skills/post-linkedin/` and an untracked copy in `plugins/claude-seo/skills/post-linkedin/`.
- Four `commands/scrape*.md` files are one-line wrappers around skills that already self-trigger.
- Two archive locations: `old-outputs/` (root) and `.claude/docs/archive-standalone-skills/`.
- The workspace root is **not a git repo** — CLAUDE.md, rules, settings, and all personal skills are unversioned.
- CLAUDE.md's layout section is stale (says "8 custom skills"; there are 10).

## Decisions (made by Aakash during brainstorming)

1. **Plugin dedup:** merge best-of-each-pair into `claude-seo`; delete `aakash-seo` afterwards.
2. **Skill layout:** themed **hub skills** — collapse ~44 skill entries into 6 hubs + 2 dev skills.
3. **Housekeeping:** all four items — root git repo, single archive folder, resolve the post-linkedin duplicate, delete the scrape command wrappers.

## Target structure

```
PolicyBazaar Claude/                  ← git repo (new)
├── CLAUDE.md                         ← rewritten for new layout
├── CLAUDE.local.md                   ← gitignored, unchanged
├── archive/                          ← old-outputs/ renamed; absorbs
│                                       .claude/docs/archive-standalone-skills/
└── .claude/
    ├── skills/                       ← 8 entries, zero symlinks
    │   ├── seo/                      ← HUB (plugin-backed)
    │   ├── content/                  ← HUB (plugin-backed)
    │   ├── ai-search/                ← HUB (plugin-backed + ai-overview)
    │   ├── uae-insurance/            ← HUB (plugin-backed)
    │   ├── scrape/                   ← MERGED (4 scrape skills → modes)
    │   ├── linkedin/                 ← MERGED (3 linkedin skills → modes)
    │   ├── deploy/                   ← unchanged
    │   └── security-review/          ← unchanged
    ├── commands/                     ← deploy.md, fix-issue.md, review.md only
    ├── agents/                       ← 3 existing + any ported aakash-seo agents
    ├── rules/                        ← unchanged
    ├── plugins/
    │   ├── claude-seo/               ← canonical SEO plugin
    │   └── debate/                   ← untouched
    ├── mcp/GoogleTrendsMCP/          ← untouched
    ├── docs/superpowers/             ← specs & plans (this file)
    └── plans/
```

## Hub mechanics

Claude Code skill discovery is flat (one folder + `SKILL.md` per skill; no nesting), so
grouping is done with **router hubs**:

- The hub's frontmatter `description` carries all trigger phrases for its theme, so
  natural-language auto-invocation keeps working.
- The hub body is a dispatch table: *user intent → file to read next*.
- **Plugin-backed hubs** (`seo`, `content`, `ai-search`, `uae-insurance`) point at existing
  `plugins/claude-seo/skills/<name>/SKILL.md` paths. Nothing is copied — the plugin's git
  repo stays the single source of truth. Hub files are ~60 lines.
- **Physically merged hubs** (`scrape`, `linkedin`) absorb the personal near-duplicate
  skills into one skill with modes; shared logic written once in `SKILL.md`,
  mode-specific detail in `references/`.

### Hub → sub-skill mapping

| Hub | Routes to (claude-seo skill unless noted) |
|---|---|
| `seo` | seo, seo-audit, seo-technical, seo-page, seo-schema, seo-sitemap, seo-interlinking, seo-backlinks, seo-local, seo-maps, seo-drift, seo-images, seo-image-gen, seo-google, seo-dataforseo, seo-ecommerce, seo-hreflang, seo-campaign, broken-links (ported from aakash-seo) |
| `content` | seo-content, seo-content-brief, seo-cluster, seo-plan, seo-competitor-pages, seo-programmatic; aakash-seo's content-translation gets grafted into seo-hreflang (which the `seo` hub routes to) |
| `ai-search` | seo-geo, seo-sxo, ai-visibility material (merged into seo-geo), plus the existing personal `ai-overview` skill and its scraper agent |
| `uae-insurance` | seo-flow (RACE), seo-insurance-ae, seo-leads-intel |
| `scrape` | modes: all / news / qna / reviews (merged from the 4 personal scrape skills) |
| `linkedin` | modes: write post / feed comments / reply to own-post comments (merged from the 3 personal post-linkedin skills) |

`ai-overview`'s Excel/JSON scripts move with it into `ai-search/references/` +
`ai-search/scripts/`; the `ai-overview-scraper` agent stays in `.claude/agents/` and the
hub references it.

## aakash-seo → claude-seo merge

1. For each of the 10 overlapping pairs (seo-audit, technical-seo/seo-technical,
   schema-markup/seo-schema, content-brief/seo-content-brief,
   internal-linking/seo-interlinking, keyword-clustering/seo-cluster,
   on-page-seo/seo-page, ai-visibility/seo-geo, content-strategy/seo-plan,
   content-translation/seo-hreflang): compare depth, references, scripts, UAE relevance.
   Keep claude-seo's version; graft any superior sections from aakash-seo's into it
   (committed to the claude-seo fork).
2. Port unique survivors: the `broken-links` skill; evaluate the 3 agents
   (competitor-analyzer, content-strategist, seo-auditor) and 6 commands for anything
   the claude-seo equivalents lack — port what adds value, drop the rest.
3. Archive safety net: `git bundle` (or zip) of `plugins/aakash-seo` into `archive/`
   before deletion.
4. Delete `plugins/aakash-seo/` and the `~/.claude/plugins/aakash-seo` symlink.

## Housekeeping details

1. **Root git repo:** `git init`; `.gitignore` covers `CLAUDE.local.md`,
   `.claude/settings.local.json`, `.claude/plugins/` (each is its own repo),
   `.claude/mcp/*/venv*`, `archive/`, `.DS_Store`. Initial commit captures CLAUDE.md,
   rules, skills, agents, commands, settings.json, this spec.
2. **Single archive:** rename `old-outputs/` → `archive/`; move
   `.claude/docs/archive-standalone-skills/` contents into `archive/`.
3. **post-linkedin duplicate:** diff `.claude/skills/post-linkedin/` against the
   untracked `plugins/claude-seo/skills/post-linkedin/`; the better content becomes the
   `linkedin` hub's write mode; the loser is deleted (claude-seo copy removed so the
   fork's `git status` is clean of it).
4. **Scrape wrappers:** delete the 4 `commands/scrape*.md` files and their
   `~/.claude/commands/` symlinks.

## Compatibility

- Recreate `~/.claude/skills/` symlinks to point at the 8 new skill folders; remove
  dangling ones. (`~/.claude/plugins/claude-seo` symlink stays.)
- Rewrite CLAUDE.md's "Workspace layout" section: new tree, hub cheat-sheet table,
  correct counts, note that aakash-seo is retired.
- claude-seo's pre-existing uncommitted local changes get committed to the fork first
  (own commit, before merge work starts) so merge commits are reviewable.

## Accepted trade-offs

- Flat slash commands like `/seo-audit` stop working; the forms are `/seo audit …` or
  natural language. Auto-invocation quality should improve (6 rich hub descriptions
  instead of 50 competing ones).
- Hub routing adds one indirection hop (hub SKILL.md → sub-skill file) per invocation.

## Verification

- Smoke test: one sub-skill invoked through each of the 6 hubs end-to-end.
- `find -L ~/.claude .claude -type l` → no dangling symlinks.
- `git -C .claude/plugins/claude-seo status` → clean.
- Root repo: initial commit exists; `git status` clean except intentionally ignored files.
- CLAUDE.md layout section matches `ls .claude/skills` exactly.

## Out of scope

- Recreating the debate / GoogleTrendsMCP venvs (separate task, noted in CLAUDE.local.md).
- Any changes to the `debate` plugin, `rules/`, or superpowers docs beyond this spec.
- Upstream-syncing the claude-seo fork.
