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
