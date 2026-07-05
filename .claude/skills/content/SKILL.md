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
