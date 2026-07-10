---
name: content
description: Content hub — routes content-planning work to the right playbook. Use for content quality / E-E-A-T / readability / thin-content audits, the five-lens content audit ("/content audit", "/content-audit", "audit this content", "is this GEO-ready", "does this sound AI", "fact-check this article", "score this page" — scored SEO+GEO+AI-detection+YMYL+fact-check report for Policybazaar UAE health & travel insurance content via URL, pasted text, or .md/.docx file), pre-writing content briefs and outlines ("/content brief", "/content-brief", "content brief", "blog brief", "outline for", "help me plan this piece", "should I write this", "go/no-go on this content idea" — research-backed brief for PB/Paisabazaar UAE: SERP gap analysis, differentiation angle, verified facts with sources, section outline, completeness check), SERP-based keyword/topic clustering ("cluster keywords", "topic cluster", "hub and spoke", "pillar page"), content strategy / calendars / gap analysis / SEO roadmaps, competitor comparison & alternatives pages ("X vs Y", "alternatives page"), and programmatic SEO (template pages at scale). Invoke as "/content <sub-task> <args>" or from any matching natural-language ask.
---

# Content Hub

Router only — do NOT answer from this file. Pick the ONE row matching the
user's intent, Read that file, then follow it exactly.

| Intent / `$1` | Read this file |
|---|---|
| five-lens scored audit (SEO+GEO+AI-detection+YMYL+fact-check) of existing Policybazaar UAE health/travel content — `audit` (also `/content-audit`) | `content-audit/SKILL.md` |
| quality / E-E-A-T audit (generic, single-lens: readability, thin content) — `quality` | `~/.claude/plugins/claude-seo/skills/seo-content/SKILL.md` |
| pre-writing research brief for PB/Paisabazaar UAE content (SERP gap + angle + verified facts + outline + go/no-go) — `brief` (also `/content-brief`) | `content-brief/SKILL.md` |
| keyword/topic clustering — `cluster` | `~/.claude/plugins/claude-seo/skills/seo-cluster/SKILL.md` |
| strategy / roadmap / calendar — `plan` | `~/.claude/plugins/claude-seo/skills/seo-plan/SKILL.md` |
| vs / alternatives pages — `competitor-pages` | `~/.claude/plugins/claude-seo/skills/seo-competitor-pages/SKILL.md` |
| programmatic / pages at scale — `programmatic` | `~/.claude/plugins/claude-seo/skills/seo-programmatic/SKILL.md` |

Translation/localization routes through the `seo` hub → hreflang.
