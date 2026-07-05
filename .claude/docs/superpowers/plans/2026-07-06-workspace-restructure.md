# Workspace Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Collapse a 50-entry flat skills folder into 6 themed hub skills + 2 dev skills, merge best-of aakash-seo into claude-seo and retire aakash-seo, and version-control the workspace root.

**Architecture:** Hub skills are thin routers — frontmatter carries all trigger phrases for a theme; the body is a dispatch table pointing (by path, never by copy) at canonical skill files inside `plugins/claude-seo`. Personal near-duplicates (4 scrape skills, 3 linkedin skills) are physically merged into single skills with mode references. Everything happens on the live workspace (no worktree — most of it isn't in git yet; Task 1 creates the safety net first).

**Tech Stack:** Plain filesystem + git + Claude Code skill conventions (SKILL.md with YAML frontmatter). No code compilation or test framework — every task's "test" is a shell verification with expected output.

**Spec:** `.claude/docs/superpowers/specs/2026-07-06-workspace-restructure-design.md`

## Global Constraints

- Workspace root: `/Users/aakashsrivastava/Documents/PolicyBazaar Claude` (note the space — always quote paths).
- All hub dispatch paths use the `~/.claude/plugins/claude-seo/...` symlink form so they work from any directory (the symlink `~/.claude/plugins/claude-seo → <root>/.claude/plugins/claude-seo` already exists and stays).
- Never copy plugin skill content into hubs — hubs point at plugin file paths.
- `plugins/claude-seo` and `plugins/debate` keep their own git repos; the root repo ignores `.claude/plugins/` entirely.
- `skills/post-linkedin` has its OWN git repo (history worth keeping) — it is renamed to `skills/linkedin` with `.git` intact, and the root repo ignores that folder.
- Do not touch: `plugins/debate/`, `.claude/mcp/GoogleTrendsMCP/`, `.claude/rules/`, `.claude/agents/code-reviewer.md`, `.claude/agents/security-auditor.md`, `commands/deploy.md`, `commands/fix-issue.md`, `commands/review.md`, `skills/deploy/`, `skills/security-review/`.
- Deletions of anything with unique content happen ONLY after an archive copy exists (Task 6 bundles aakash-seo before deleting).
- Every commit in the ROOT repo ends with `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`. Commits inside the claude-seo fork and the linkedin skill repo follow the same rule.

---

### Task 1: Root git repo — safety net BEFORE any restructuring

**Files:**
- Create: `.gitignore` (root — replaces the existing 3-line one)
- Create: git repo at workspace root
- Test: `git status` output

**Interfaces:**
- Produces: a git repo at the workspace root whose initial commit snapshots the PRE-restructure state. Every later task commits its changes here (except plugin-internal changes, which commit to the plugin's own repo).

- [ ] **Step 1: Overwrite the root `.gitignore` with the full ignore set**

```gitignore
# Personal / machine-local
CLAUDE.local.md
.claude/settings.local.json

# Own git repos — not tracked by the root repo
.claude/plugins/
.claude/mcp/
.claude/skills/linkedin/
.claude/skills/post-linkedin/

# Bulky retired data
archive/
old-outputs/

# OS noise
.DS_Store
```

(`.claude/skills/post-linkedin/` is listed as well as `linkedin/` so the repo is clean both before and after Task 9's rename.)

- [ ] **Step 2: Init the repo and make the snapshot commit**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude"
git init
git add -A
git commit -m "chore: snapshot workspace before restructure

Pre-restructure state: 50-entry flat skills folder (10 real + 40 symlinks),
aakash-seo + claude-seo plugins both exposed, two archive locations.

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

Note: git stores the 40 symlinks as symlinks (tiny path blobs) — this is expected and correct.

- [ ] **Step 3: Verify**

Run: `git -C "/Users/aakashsrivastava/Documents/PolicyBazaar Claude" status --short && git -C "/Users/aakashsrivastava/Documents/PolicyBazaar Claude" log --oneline`
Expected: empty status; exactly one commit. `git ls-files | grep -c skills/` shows the skill files tracked; `git ls-files | grep plugins/` shows NOTHING (ignored).

---

### Task 2: Single archive folder

**Files:**
- Rename: `old-outputs/` → `archive/`
- Move: `.claude/docs/archive-standalone-skills/` → `archive/archive-standalone-skills/`

**Interfaces:**
- Produces: `archive/` at the workspace root — the ONE place for retired material. Task 6 writes its aakash-seo bundle here.

- [ ] **Step 1: Rename and consolidate**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude"
mv old-outputs archive
mv .claude/docs/archive-standalone-skills archive/archive-standalone-skills
```

- [ ] **Step 2: Verify**

Run: `ls archive | head -5; ls archive/archive-standalone-skills; ls .claude/docs`
Expected: archive listing starts with the AIO xlsx files; `archive-standalone-skills` contains `seo-insurance-ae` and `seo-leads-intel`; `.claude/docs` contains only `superpowers` (and possibly `.DS_Store`).

- [ ] **Step 3: Commit (the deletion of the old docs path is the only tracked change)**

```bash
git add -A
git commit -m "chore: consolidate archives into archive/

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 3: Commit claude-seo's pre-existing local changes (clean slate for merge work)

**Files:**
- Modify: nothing new — commits the fork's existing dirty state at `.claude/plugins/claude-seo/`
- Move: stray output artifacts → `archive/claude-seo-outputs/`

**Interfaces:**
- Produces: a claude-seo fork whose `git status` shows ONLY the untracked `skills/post-linkedin/` (removed in Task 4). All later merge commits are then reviewable in isolation.

- [ ] **Step 1: Move run-output artifacts out of the plugin (they're results, not plugin code)**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/plugins/claude-seo"
mkdir -p ../../../archive/claude-seo-outputs
mv leads-intel-health-2026-06-09.html url-plan.html cluster-url-plan.csv .playwright-mcp/page-*.yml ../../../archive/claude-seo-outputs/ 2>/dev/null || true
```

- [ ] **Step 2: Commit the real local modifications to the fork**

```bash
git add -u
git add scripts/zigwheels_scraper.py skills/seo-google/scripts/
git commit -m "chore: commit accumulated local customizations

Modified: cluster-plan.json, GSC/SEMrush/leads import scripts, seo-flow
prompts, seo-leads-intel skill, tests. New: zigwheels scraper,
seo-google scripts.

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

- [ ] **Step 3: Verify**

Run: `git -C "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/plugins/claude-seo" status --short`
Expected: exactly one line — `?? skills/post-linkedin/`.

---

### Task 4: Resolve the post-linkedin duplicate

**Files:**
- Delete: `.claude/plugins/claude-seo/skills/post-linkedin/` (the stray, older copy)
- Keep: `.claude/skills/post-linkedin/` (canonical — 261-line SKILL.md, own git repo with the image-flow commits; the stray copy is 173 lines and predates them)

**Interfaces:**
- Produces: exactly one post-linkedin on disk, which Task 9 turns into the `linkedin` hub.

- [ ] **Step 1: Confirm the canonical copy is the newer one (do not skip)**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude"
diff plugins/claude-seo/skills/post-linkedin/SKILL.md skills/post-linkedin/SKILL.md | head -20
grep -c "image" skills/post-linkedin/SKILL.md
grep -c "image" plugins/claude-seo/skills/post-linkedin/SKILL.md
```

Expected: canonical (`skills/post-linkedin`) has MORE image-flow references. **Decision rule:** if instead the claude-seo copy contains any section heading absent from the canonical SKILL.md, copy that section into the canonical file first and commit it to the linkedin skill's own repo — then continue.

- [ ] **Step 2: Delete the stray copy**

```bash
rm -rf plugins/claude-seo/skills/post-linkedin
```

- [ ] **Step 3: Verify**

Run: `git -C plugins/claude-seo status --short && ls skills/post-linkedin/SKILL.md`
Expected: claude-seo status is EMPTY (clean); canonical SKILL.md still present.

---

### Task 5: Best-of merge — graft aakash-seo's superior material into claude-seo

**Files:**
- Compare (10 pairs, aakash-seo → claude-seo):
  `seo-audit → skills/seo-audit`, `technical-seo → skills/seo-technical`, `schema-markup → skills/seo-schema`, `content-brief → skills/seo-content-brief`, `internal-linking → skills/seo-interlinking`, `keyword-clustering → skills/seo-cluster`, `on-page-seo → skills/seo-page`, `ai-visibility → skills/seo-geo`, `content-strategy → skills/seo-plan`, `content-translation → skills/seo-hreflang`
- Create: `.claude/plugins/claude-seo/skills/broken-links/` (ported — aakash-seo's only unique skill)
- Modify: any claude-seo SKILL.md that receives a graft

**Interfaces:**
- Consumes: clean claude-seo repo from Tasks 3–4.
- Produces: claude-seo as the single canonical SEO skill set, including `broken-links`. Task 7's `seo` hub routes to `broken-links` at `~/.claude/plugins/claude-seo/skills/broken-links/SKILL.md`.

- [ ] **Step 1: Port broken-links verbatim**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude"
cp -R plugins/aakash-seo/skills/broken-links plugins/claude-seo/skills/broken-links
```

- [ ] **Step 2: Compare each of the 10 pairs and graft**

For EACH pair, run and read:

```bash
wc -l plugins/aakash-seo/skills/<A>/SKILL.md plugins/claude-seo/skills/<B>/SKILL.md
grep -E "^#{1,3} " plugins/aakash-seo/skills/<A>/SKILL.md
grep -E "^#{1,3} " plugins/claude-seo/skills/<B>/SKILL.md
ls plugins/aakash-seo/skills/<A>/ plugins/claude-seo/skills/<B>/
```

**Decision rule (apply mechanically):** claude-seo's version is kept as the base in all 10 cases. Graft from the aakash-seo version ONLY a section/checklist/script that satisfies BOTH: (a) its topic has no equivalent heading in the claude-seo file, and (b) it is actionable (a procedure, checklist, threshold table, or script — not generic prose like "SEO is important"). Grafted sections are appended verbatim under their original heading, prefixed with a one-line note: `<!-- grafted from aakash-seo <skill-name> 2026-07-06 -->`. If nothing qualifies (likely for most pairs — the aakash-seo files are thin de-branded generics), graft nothing. Record the verdict per pair in the commit message.

- [ ] **Step 3: Evaluate aakash-seo's 3 agents and 6 commands**

```bash
head -20 plugins/aakash-seo/agents/*/AGENT.md
cat plugins/aakash-seo/commands/*.md
```

**Decision rule:** claude-seo already ships 21 SEO agents (`plugins/claude-seo/agents/`). Port an aakash-seo agent to `.claude/agents/` ONLY if no claude-seo agent covers its role (check: competitor-analyzer vs `seo-market.md`, content-strategist vs `seo-content.md`, seo-auditor vs the seo-audit skill's own delegation). The 6 commands are thin wrappers around skills that the hubs will cover — expected verdict: port nothing; note the verdict in the commit message. If one genuinely has unique prompt material, fold that material into the matching claude-seo skill as a graft instead of porting the command.

- [ ] **Step 4: Commit to the claude-seo fork**

```bash
cd plugins/claude-seo
git add -A
git commit -m "feat: absorb aakash-seo best-of (broken-links + grafts)

broken-links: ported verbatim (unique skill).
Pair verdicts: <one line per pair, e.g. 'seo-audit: kept ours, no graft'>
Agents/commands: <verdict>

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

- [ ] **Step 5: Verify**

Run: `ls plugins/claude-seo/skills/broken-links/ && git -C plugins/claude-seo status --short`
Expected: `SKILL.md` present; status clean.

---

### Task 6: Archive and delete aakash-seo

**Files:**
- Create: `archive/aakash-seo.bundle` + `archive/aakash-seo-worktree.tar.gz`
- Delete: `.claude/plugins/aakash-seo/`, symlink `~/.claude/plugins/aakash-seo`, and the 11 aakash-seo symlinks in `.claude/skills/`

**Interfaces:**
- Consumes: Task 5 complete (everything worth keeping is already in claude-seo).
- Produces: one SEO plugin on disk. Reversal path: `git clone archive/aakash-seo.bundle` (history) + the tarball (uncommitted state).

- [ ] **Step 1: Bundle (history) + tarball (uncommitted working-tree changes)**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude"
git -C .claude/plugins/aakash-seo bundle create ../../../archive/aakash-seo.bundle --all
tar -czf archive/aakash-seo-worktree.tar.gz -C .claude/plugins aakash-seo
```

- [ ] **Step 2: Verify the archives are restorable BEFORE deleting**

Run: `git bundle verify archive/aakash-seo.bundle && tar -tzf archive/aakash-seo-worktree.tar.gz | head -3`
Expected: `archive/aakash-seo.bundle is okay` and a file listing. **If either fails, STOP — do not delete.**

- [ ] **Step 3: Delete plugin + its symlinks**

```bash
rm -rf .claude/plugins/aakash-seo
rm ~/.claude/plugins/aakash-seo
rm .claude/skills/ai-visibility .claude/skills/broken-links .claude/skills/content-brief \
   .claude/skills/content-strategy .claude/skills/content-translation .claude/skills/internal-linking \
   .claude/skills/keyword-clustering .claude/skills/on-page-seo .claude/skills/schema-markup \
   .claude/skills/technical-seo
rm .claude/skills/seo-audit 2>/dev/null || true
```

(Note: 10 of the 11 symlinks have aakash-seo names; `seo-audit` pointed at claude-seo and dies here too since Task 7's hub replaces it. If `seo-audit` is instead among Task 8's list, the `|| true` keeps this idempotent.)

- [ ] **Step 4: Verify + commit to root repo**

Run: `find -L .claude/skills -maxdepth 1 -type l` — expected: only the remaining claude-seo-target symlinks (removed in Task 8), NONE broken (`find -L` + `-type l` prints only healthy links; broken ones appear via `find .claude/skills -maxdepth 1 -type l ! -exec test -e {} \; -print` → expected empty).

```bash
git add -A
git commit -m "chore: retire aakash-seo (archived to archive/aakash-seo.bundle)

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 7: Create the four plugin-backed hubs (seo, content, ai-search, uae-insurance)

**Files:**
- Create: `.claude/skills/seo/SKILL.md`, `.claude/skills/content/SKILL.md`, `.claude/skills/uae-insurance/SKILL.md`
- Rename: `.claude/skills/ai-overview/` → `.claude/skills/ai-search/` (keeps `scripts/`), then rewrite its `SKILL.md` frontmatter/routing header
- Modify: `.claude/agents/ai-overview-scraper.md` (path references, if any)

**Interfaces:**
- Consumes: claude-seo skill files at `~/.claude/plugins/claude-seo/skills/<name>/SKILL.md` (Task 5 final state, incl. broken-links).
- Produces: hub skills `seo`, `content`, `ai-search`, `uae-insurance`. Invocation: `/seo audit example.com` etc., or natural language. Task 10's CLAUDE.md documents them.

- [ ] **Step 1: Write `.claude/skills/seo/SKILL.md`**

````markdown
---
name: seo
description: SEO hub — routes every SEO task to the right specialist playbook. Use for site/page audits ("audit SEO", "site audit", "check my site"), technical SEO (crawlability, robots.txt, Core Web Vitals, site speed, security headers), single-page analysis, schema/structured data/JSON-LD, sitemaps, internal linking/interlinking/orphan pages, backlinks/link profile/toxic links, broken links/404s, local SEO/GBP/map pack, maps/geo-grid rank tracking, SEO drift/baselines/regressions, image SEO/alt text/WebP, AI image generation for SEO assets (OG images, hero images), Google Search Console/PageSpeed/CrUX/GA4 data, DataForSEO live SERP/keyword/backlink data, e-commerce/product/marketplace SEO, hreflang/international/multi-language SEO, content translation/localization, or a full SEO campaign. Invoke as "/seo <sub-task> <args>" or from any matching natural-language ask.
---

# SEO Hub

Router only — do NOT answer from this file. Pick the ONE row that matches the
user's intent, Read that file, then follow it exactly as if it were the invoked
skill. `$1` = sub-task keyword, remaining args pass through.

| Intent / `$1` | Read this file |
|---|---|
| full site audit — `audit` | `~/.claude/plugins/claude-seo/skills/seo-audit/SKILL.md` |
| general/unclear SEO ask — `general` | `~/.claude/plugins/claude-seo/skills/seo/SKILL.md` |
| technical (crawl, CWV, speed, robots) — `technical` | `~/.claude/plugins/claude-seo/skills/seo-technical/SKILL.md` |
| one page deep-dive — `page` | `~/.claude/plugins/claude-seo/skills/seo-page/SKILL.md` |
| schema / JSON-LD — `schema` | `~/.claude/plugins/claude-seo/skills/seo-schema/SKILL.md` |
| sitemap — `sitemap` | `~/.claude/plugins/claude-seo/skills/seo-sitemap/SKILL.md` |
| internal links / orphans — `interlinking` | `~/.claude/plugins/claude-seo/skills/seo-interlinking/SKILL.md` |
| backlinks / link profile — `backlinks` | `~/.claude/plugins/claude-seo/skills/seo-backlinks/SKILL.md` |
| broken links / 404s — `broken-links` | `~/.claude/plugins/claude-seo/skills/broken-links/SKILL.md` |
| local SEO / GBP — `local` | `~/.claude/plugins/claude-seo/skills/seo-local/SKILL.md` |
| maps / geo-grid tracking — `maps` | `~/.claude/plugins/claude-seo/skills/seo-maps/SKILL.md` |
| drift / baseline / regression — `drift` | `~/.claude/plugins/claude-seo/skills/seo-drift/SKILL.md` |
| image optimization — `images` | `~/.claude/plugins/claude-seo/skills/seo-images/SKILL.md` |
| generate SEO images — `image-gen` | `~/.claude/plugins/claude-seo/skills/seo-image-gen/SKILL.md` |
| GSC / PageSpeed / CrUX / GA4 — `google` | `~/.claude/plugins/claude-seo/skills/seo-google/SKILL.md` |
| DataForSEO live data — `dataforseo` | `~/.claude/plugins/claude-seo/skills/seo-dataforseo/SKILL.md` |
| e-commerce / product — `ecommerce` | `~/.claude/plugins/claude-seo/skills/seo-ecommerce/SKILL.md` |
| hreflang / i18n / translation — `hreflang` | `~/.claude/plugins/claude-seo/skills/seo-hreflang/SKILL.md` |
| full campaign — `campaign` | `~/.claude/plugins/claude-seo/skills/seo-campaign/SKILL.md` |

UAE-insurance-specific work (RACE loop, insurance page audits, leads intel)
lives in the `uae-insurance` skill; content strategy/briefs/clusters in
`content`; AI-search visibility in `ai-search`.
````

- [ ] **Step 2: Write `.claude/skills/content/SKILL.md`**

````markdown
---
name: content
description: Content hub — routes content-planning work to the right playbook. Use for content quality / E-E-A-T / readability / thin-content audits, content briefs and outlines ("content brief", "blog brief", "outline for"), SERP-based keyword/topic clustering ("cluster keywords", "topic cluster", "hub and spoke", "pillar page"), content strategy / calendars / gap analysis / SEO roadmaps, competitor comparison & alternatives pages ("X vs Y", "alternatives page"), and programmatic SEO (template pages at scale). Invoke as "/content <sub-task> <args>" or from any matching natural-language ask.
---

# Content Hub

Router only — do NOT answer from this file. Pick the ONE row matching the
user's intent, Read that file, then follow it exactly.

| Intent / `$1` | Read this file |
|---|---|
| quality / E-E-A-T audit — `quality` | `~/.claude/plugins/claude-seo/skills/seo-content/SKILL.md` |
| brief / outline — `brief` | `~/.claude/plugins/claude-seo/skills/seo-content-brief/SKILL.md` |
| keyword/topic clustering — `cluster` | `~/.claude/plugins/claude-seo/skills/seo-cluster/SKILL.md` |
| strategy / roadmap / calendar — `plan` | `~/.claude/plugins/claude-seo/skills/seo-plan/SKILL.md` |
| vs / alternatives pages — `competitor-pages` | `~/.claude/plugins/claude-seo/skills/seo-competitor-pages/SKILL.md` |
| programmatic / pages at scale — `programmatic` | `~/.claude/plugins/claude-seo/skills/seo-programmatic/SKILL.md` |

Translation/localization routes through the `seo` hub → hreflang.
````

- [ ] **Step 3: Write `.claude/skills/uae-insurance/SKILL.md`**

````markdown
---
name: uae-insurance
description: PolicyBazaar UAE insurance hub. Use for the RACE operating loop ("RACE", "seo flow", research/authority/convert/edge stages, UAE insurance vertical prompts), senior SEO+AEO audits of UAE insurance pages vs local SERP competitors (car, health, travel, home, life, SME — "audit this insurance page"), and leads intelligence ("leads decline", "dropped pages", "traffic drop", "recovery roadmap", cross-referencing leads + SEMrush + GSC + GA4). Invoke as "/uae-insurance <sub-task> <args>" or from any matching natural-language ask.
---

# UAE Insurance Hub

Router only — do NOT answer from this file. Pick the ONE row matching the
user's intent, Read that file, then follow it exactly.

| Intent / `$1` | Read this file |
|---|---|
| RACE loop / stage prompts — `flow` | `~/.claude/plugins/claude-seo/skills/seo-flow/SKILL.md` |
| insurance page audit — `audit` | `~/.claude/plugins/claude-seo/skills/seo-insurance-ae/SKILL.md` |
| leads intel / recovery — `leads` | `~/.claude/plugins/claude-seo/skills/seo-leads-intel/SKILL.md` |
````

- [ ] **Step 4: Rename ai-overview → ai-search and rewrite its routing header**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills"
mv ai-overview ai-search
```

Then edit `ai-search/SKILL.md`: change frontmatter `name:` to `ai-search`; EXTEND (don't replace) the existing description so it still contains all its current AI-Overview/ChatGPT-citation trigger phrases and additionally covers: "GEO", "generative engine optimization", "AEO", "AI visibility", "LLM mentions", "Perplexity", "SXO", "why isn't my page ranking", "intent mismatch". Insert this routing block immediately after the frontmatter, BEFORE the existing body (the existing body remains the `scrape-citations` behavior):

```markdown
# AI Search Hub

Three sub-tasks. For `scrape-citations` (the default — "scrape AI overview",
"which sites does the AI cite", citation matrices) continue with THIS file
below. Otherwise Read the mapped file and follow it exactly:

| Intent / `$1` | Read this file |
|---|---|
| optimize for AI engines / GEO / llms.txt — `geo` | `~/.claude/plugins/claude-seo/skills/seo-geo/SKILL.md` |
| SERP intent / page-type mismatch — `sxo` | `~/.claude/plugins/claude-seo/skills/seo-sxo/SKILL.md` |
```

- [ ] **Step 5: Fix stale path references to the old name**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude"
grep -rn "skills/ai-overview" agents/ skills/ai-search/ CLAUDE.md ../CLAUDE.md 2>/dev/null
```

For every hit, replace `skills/ai-overview` → `skills/ai-search`. Expected hits: possibly `agents/ai-overview-scraper.md` and `skills/ai-search/SKILL.md` internal script paths. The agent FILE name stays `ai-overview-scraper.md` (its agent-type name is published; only paths inside it change).

- [ ] **Step 6: Verify + commit**

Run: `for f in seo content uae-insurance ai-search; do head -3 .claude/skills/$f/SKILL.md; done` — expected: four frontmatter blocks with the right `name:` lines. Then spot-check one dispatch target: `test -f ~/.claude/plugins/claude-seo/skills/seo-audit/SKILL.md && echo OK` → `OK`.

```bash
git add -A
git commit -m "feat: add seo, content, uae-insurance hubs; ai-overview -> ai-search hub

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 8: Remove the 29 claude-seo symlinks + scrape command wrappers

**Files:**
- Delete: every remaining symlink in `.claude/skills/` (all point into `plugins/claude-seo`)
- Delete: `.claude/commands/scrape.md`, `scrape-news.md`, `scrape-qna.md`, `scrape-review.md` and their `~/.claude/commands/` symlinks

**Interfaces:**
- Consumes: Task 7's hubs (the replacement routing must exist before the old routes die).
- Produces: `.claude/skills/` contains ONLY real directories. `.claude/commands/` contains only `deploy.md`, `fix-issue.md`, `review.md`.

- [ ] **Step 1: Delete all remaining skill symlinks**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills"
find . -maxdepth 1 -type l -delete
```

- [ ] **Step 2: Delete scrape command wrappers (project + home)**

```bash
rm "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/commands/"scrape*.md
rm ~/.claude/commands/scrape*.md
```

- [ ] **Step 3: Verify + commit**

Run: `ls -la .claude/skills | grep -c "^l"; ls .claude/commands; ls ~/.claude/commands`
Expected: `0` symlinks; commands = `deploy.md fix-issue.md review.md`; `~/.claude/commands` empty (or no scrape entries).

```bash
git add -A
git commit -m "chore: remove 29 plugin symlinks and 4 scrape command wrappers

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 9: Merge the personal skills — `scrape` (4→1) and `linkedin` (3→1)

**Files:**
- Create: `.claude/skills/scrape/references/` with `news.md`, `qna.md`, `reviews.md` (moved bodies of the 3 variant skills); rewrite `.claude/skills/scrape/SKILL.md` as router+shared-flow
- Delete: `.claude/skills/scrape-news/`, `scrape-qna/`, `scrape-review/`
- Rename: `.claude/skills/post-linkedin/` → `.claude/skills/linkedin/` (own `.git` moves with it)
- Create: `.claude/skills/linkedin/references/feed-comments.md`, `references/reply-comments.md` (moved from the 2 companion skills)
- Delete: `.claude/skills/post-linkedin-feed-comments/`, `post-linkedin-posts-comment/`
- Update: `~/.claude/skills/` symlinks

**Interfaces:**
- Consumes: nothing from other tasks (independent of the hub work).
- Produces: skills `scrape` and `linkedin`. `/scrape news <topic>` etc.; linkedin modes: write / feed / replies.

- [ ] **Step 1: Restructure scrape**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills"
mkdir scrape/references
mv scrape-news/SKILL.md scrape/references/news.md
mv scrape-qna/SKILL.md scrape/references/qna.md
mv scrape-review/SKILL.md scrape/references/reviews.md
rmdir scrape-news scrape-qna scrape-review
```

- [ ] **Step 2: Rewrite `scrape/SKILL.md`**

Take the CURRENT body of `scrape/SKILL.md` (everything below the frontmatter — the "three questions" flow covering all sources) and keep it as the `all` mode. New file shape — frontmatter replaced with the merged one below, then a mode table, then the existing all-sources body unchanged:

````markdown
---
name: scrape
description: Scrape hub for UAE topic research with GSC + sitemap coverage check (3-tier UPDATE/CREATE/FIX classification and two-way interlinking suggestions). Modes — all: Reddit UAE, Quora, Twitter/X, TrustPilot, Google My Business, and UAE news sites; news: UAE news sites only (Gulf News, WAM, Al Etihaad, Khaleej Times, The National); qna: Reddit/Quora/Twitter questions and discussions, best for FAQ and content-gap mining; reviews: TrustPilot + Google My Business reviews by topic and location. Use for "/scrape <topic>", "/scrape news <topic>", "/scrape qna <topic>", "/scrape reviews <topic>", or any ask to scrape these sources.
---

# Scrape Hub

Mode = first argument (default `all`). For `news`, `qna`, `reviews`: Read the
mapped reference and follow IT (each is a complete self-contained flow):

| Mode | Reference |
|---|---|
| `news` | `references/news.md` |
| `qna` | `references/qna.md` |
| `reviews` | `references/reviews.md` |

For `all` (or no mode), continue below.

[EXISTING BODY OF scrape/SKILL.md — UNCHANGED FROM HERE DOWN]
````

The reference files keep their old frontmatter — harmless, and preserves their descriptions as in-file documentation.

- [ ] **Step 3: Restructure linkedin**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills"
mv post-linkedin linkedin
mkdir -p linkedin/references
mv post-linkedin-feed-comments/SKILL.md linkedin/references/feed-comments.md
mv post-linkedin-posts-comment/SKILL.md linkedin/references/reply-comments.md
rmdir post-linkedin-feed-comments post-linkedin-posts-comment
```

- [ ] **Step 4: Edit `linkedin/SKILL.md` header**

Change frontmatter `name: post-linkedin` → `name: linkedin`. MERGE the two companion descriptions into the existing description (keep every existing trigger phrase; add: "comment on relevant posts in my feed", "scan my feed and comment", "reply to the comments on my posts", "check my LinkedIn comments", "/linkedin"). Immediately after the frontmatter insert:

```markdown
# LinkedIn Hub

Three modes. WRITE (draft/score/publish a post — the default) continues in
THIS file below. For the other two, Read the mapped reference and follow it:

| Mode | Trigger | Reference |
|---|---|---|
| feed engage | comment on others' posts in my home feed | `references/feed-comments.md` |
| reply | reply to comments on MY OWN posts | `references/reply-comments.md` |
```

Then check for cross-references between the moved files: `grep -rn "post-linkedin" linkedin/ | grep -v ".git"` — update any `post-linkedin-feed-comments`/`post-linkedin-posts-comment` skill references to the new `references/*.md` paths.

- [ ] **Step 5: Commit inside the linkedin skill's OWN repo**

```bash
cd linkedin
git add -A
git commit -m "feat: become linkedin hub — absorb feed-comments and reply-comments as modes

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
cd ..
```

- [ ] **Step 6: Refresh ~/.claude compatibility symlinks**

```bash
ROOT="/Users/aakashsrivastava/Documents/PolicyBazaar Claude"
rm ~/.claude/skills/post-linkedin ~/.claude/skills/post-linkedin-feed-comments \
   ~/.claude/skills/post-linkedin-posts-comment ~/.claude/skills/ai-overview 2>/dev/null
ln -s "$ROOT/.claude/skills/linkedin" ~/.claude/skills/linkedin
ln -s "$ROOT/.claude/skills/ai-search" ~/.claude/skills/ai-search
ln -s "$ROOT/.claude/skills/seo" ~/.claude/skills/seo
ln -s "$ROOT/.claude/skills/content" ~/.claude/skills/content
ln -s "$ROOT/.claude/skills/uae-insurance" ~/.claude/skills/uae-insurance
# ~/.claude/skills/scrape already points at .claude/skills/scrape — still valid
```

- [ ] **Step 7: Verify + commit root repo**

Run: `ls .claude/skills` — expected EXACTLY: `ai-search content deploy linkedin scrape security-review seo uae-insurance` (8 entries). Then `find ~/.claude/skills .claude/skills -maxdepth 1 -type l ! -exec test -e {} \; -print` → empty (no dangling links).

```bash
git add -A
git commit -m "feat: merge scrape 4->1 and linkedin 3->1 with mode references

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 10: Rewrite CLAUDE.md workspace-layout section

**Files:**
- Modify: `CLAUDE.md` (root)

**Interfaces:**
- Consumes: final structure from Tasks 1–9.
- Produces: CLAUDE.md that matches reality — the file every future session reads first.

- [ ] **Step 1: Replace the entire `## Workspace layout` section with:**

```markdown
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
```

- [ ] **Step 2: Verify + commit**

Run: `grep -c "aakash-seo\` — de-branded" CLAUDE.md` → `0` (old bullet gone); `ls .claude/skills | wc -l` → `8`, matching the doc.

```bash
git add CLAUDE.md
git commit -m "docs: rewrite workspace layout for hub structure

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

---

### Task 11: End-to-end verification (fresh-session smoke tests)

**Files:** none created — verification only. Requires a NEW Claude Code session (skill registry is read at session start).

**Interfaces:**
- Consumes: everything.
- Produces: pass/fail evidence per spec's Verification section.

- [ ] **Step 1: Structural checks (current session is fine)**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude"
ls .claude/skills                                        # exactly the 8 dirs
find -L ~/.claude .claude -maxdepth 3 -type l ! -exec test -e {} \; -print   # empty
git status --short                                       # empty
git -C .claude/plugins/claude-seo status --short          # empty
git -C .claude/skills/linkedin status --short             # empty
test -f archive/aakash-seo.bundle && echo bundle-ok
```

Expected: each comment's condition holds. Any failure → fix before proceeding.

- [ ] **Step 2: Hub smoke tests — in a NEW session, run one per hub and confirm the router reads the mapped file and executes the sub-flow (not the router text):**

| Test | Expect |
|---|---|
| `/seo schema https://www.policybazaar.ae` | reads seo-schema SKILL.md, produces JSON-LD flow |
| `/content brief car insurance uae` | reads seo-content-brief SKILL.md |
| `/uae-insurance flow` | reads seo-flow SKILL.md, offers RACE stages |
| `/ai-search geo` | reads seo-geo SKILL.md |
| `/scrape news travel insurance` | reads references/news.md, asks its 3 questions |
| "check the comments on my LinkedIn posts" | linkedin skill, reply mode via references/reply-comments.md |

- [ ] **Step 3: Record results**

Append a `## Verification 2026-07-06` section with the pass/fail table to the plan file, commit:

```bash
git add .claude/docs/superpowers/plans/2026-07-06-workspace-restructure.md
git commit -m "docs: record restructure verification results

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
```

## Verification 2026-07-06

Structural checks — all PASS:
- `.claude/skills` = exactly 8 dirs (ai-search, content, deploy, linkedin, scrape, security-review, seo, uae-insurance)
- No dangling symlinks in `~/.claude/skills` or `.claude/skills`
- Root repo clean; claude-seo fork clean; linkedin skill repo clean
- `archive/aakash-seo.bundle` (36K) + `aakash-seo-worktree.tar.gz` (82K) present and verified restorable
- Root-level live AIO run outputs gitignored (`aio_*.json`, `AIO_*.xlsx`) — commit 7a427d6

Hub routing smoke tests (fresh-context agent) — 6/6 PASS:

| Request | Routed to | Verdict |
|---|---|---|
| /seo schema <url> | claude-seo/skills/seo-schema | PASS |
| /content brief car insurance uae | claude-seo/skills/seo-content-brief | PASS |
| /uae-insurance flow | claude-seo/skills/seo-flow | PASS |
| /ai-search geo (+ default body intact) | claude-seo/skills/seo-geo | PASS |
| /scrape news travel insurance | scrape/references/news.md | PASS |
| "check comments on my LinkedIn posts" | linkedin/references/reply-comments.md | PASS |

Note: live slash-command invocation of the new hubs requires a fresh Claude Code
session (skill registry loads at session start); routing verified via fresh-context
agent simulation. Known cosmetic leftover: linkedin/SKILL.md retains its older
"Mode — Write or Engage" block below the new mode table (paths converge; harmless).

Correction: Task 8's commit message says "29 symlinks"; the commit actually deletes 27 (seo and seo-audit were already removed by Tasks 6-7). History not rewritten.
