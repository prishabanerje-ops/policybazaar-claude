# Invocation Guide — PolicyBazaar UAE Claude Workspace

Every skill and command you can invoke, what it does, and when to use it.
Two ways to invoke anything: the slash form (`/seo audit example.com`) or plain
natural language ("audit policybazaar.ae") — the hub descriptions catch both.

> New skills register when a session starts — if a slash form doesn't fire, open a fresh session.

---

## 1. `/seo` — SEO Hub (19 playbooks)

| Skill | Detailed use | Application |
|---|---|---|
| `/seo audit <url>` | Full-site SEO audit: crawls up to 500 pages, detects business type, delegates to up to 15 specialist subagents, produces a health score | Quarterly site health check of policybazaar.ae; before/after a big release |
| `/seo general <ask>` | General SEO orchestrator for asks that don't fit one specialist — routes internally | "Something is off with our SEO" when you can't name the area yet |
| `/seo technical <url>` | 9-category technical audit: crawlability, indexability, security headers, URL structure, mobile, Core Web Vitals, structured data, JS rendering, IndexNow | Diagnosing indexing drops, slow pages, robots.txt/sitemap conflicts |
| `/seo page <url>` | Deep single-page analysis: on-page elements, content quality, meta tags, schema, images, performance | Optimizing one money page (e.g. /health-insurance/) before a campaign |
| `/seo schema <url>` | Detect, validate, and generate Schema.org JSON-LD | Adding InsuranceAgency/FAQ/Product markup; fixing rich-result errors |
| `/seo sitemap <url>` | Analyze existing XML sitemaps or generate new ones; validates format, URLs, structure | Sitemap bloat, missing pages, or building a sitemap for a new section |
| `/seo interlinking <section>` | Internal-link audit + suggestion engine: scores every page 0–100, finds orphans/dead-ends, suggests contextual links with real anchor text from body copy | Strengthening the health/travel cluster pages; fixing orphaned blog posts |
| `/seo backlinks <domain>` | Backlink profile analysis: referring domains, anchor distribution, toxic links, competitor gap | Comparing link profile vs yallacompare/InsuranceMarket; disavow prep |
| `/seo broken-links <url>` | Find and fix broken links / 404s on a site or in a codebase | Post-migration link rot sweep; fixing dead outbound links in blog archive |
| `/seo local <business>` | Local SEO: Google Business Profile, NAP consistency, citations, reviews, local schema, multi-location | PolicyBazaar UAE office GBP optimization; map-pack visibility |
| `/seo maps <area>` | Maps intelligence: geo-grid rank tracking, GBP API audits, review velocity, competitor radius, Share of Local Voice | Tracking "insurance broker near me" rankings across Dubai/Abu Dhabi grids |
| `/seo drift [baseline\|diff]` | Git-for-SEO: capture baselines of SEO-critical elements, detect regressions between snapshots | Run before + after every deploy — catches "who changed the title tags?" |
| `/seo images <url>` | Image SEO: alt text, file sizes, WebP/AVIF conversion, lazy loading, CLS prevention, image-SERP rankings | Compressing hero images that hurt LCP; alt-text sweep for accessibility |
| `/seo image-gen <what>` | AI image generation for SEO assets: OG/social previews, blog heroes, infographics (needs banana extension) | Generating OG images for new vertical pages or blog posts |
| `/seo google <query>` | Real Google data: Search Console analytics, URL Inspection, PageSpeed Insights, CrUX field data (25-week history), GA4 organic | Pulling clicks/impressions/position for any page; real CWV field data |
| `/seo dataforseo <query>` | Live SERP/keyword/backlink/competitor data via DataForSEO (needs the extension) | Real search volumes and SERP snapshots for UAE keywords |
| `/seo ecommerce <url>` | Product SEO: Google Shopping visibility, product schema, marketplace keyword gaps | Less used here — relevant if PB ever lists products/plans as shopping feed |
| `/seo hreflang <url>` | International SEO: hreflang audit/validation/generation + content translation & localization strategy (incl. URL-structure decision table) | Arabic/English versions of policybazaar.ae; GCC market expansion |
| `/seo campaign <url>` | Full three-phase campaign pipeline: parallel data collection (GSC, SEMrush, market) → 11 analysis subagents → prioritised roadmap (optional PDF) | Building the next quarter's complete SEO campaign in one run |

## 2. `/content` — Content Hub (7 playbooks)

| Skill | Detailed use | Application |
|---|---|---|
| `/content audit <url or file>` | Five-lens scored audit of existing content: SEO (12 params), GEO citation readiness (9 params), AI-detection/human-likeness (9 signals), YMYL/Helpful Content, and live fact-check via web search; detects brand (Policybazaar vs Paisabazaar UAE) and FILE vs URL mode; also answers to `/content-audit` | Pre-publish gate for insurance guides or loan pages — one report with per-lens scores, line-level evidence, and fix list |
| `/content quality <url>` | Content quality + E-E-A-T analysis with AI-citation readiness scoring, readability, thin-content detection | Auditing YMYL trust signals on insurance guides (critical for finance niche) |
| `/content brief <topic>` | Pre-writing research brief for PB/Paisabazaar UAE content: reads top SERP competitors and states the gap, one-sentence differentiation angle, web-verified facts/figures with sources, Commercial vs Article outline (FAQ questions sourced from PAA/Reddit/Quora), cannibalization check against the live URL list, go/no-go completeness verdict; also answers to `/content-brief` | Briefing writers for "best health insurance UAE 2026" before they draft; go/no-go on a content idea |
| `/content cluster <keywords>` | SERP-based semantic clustering — groups keywords by actual Google SERP overlap, designs hub-and-spoke architecture with internal-link matrices | Planning the car-insurance content cluster; deciding pillar vs spoke pages |
| `/content plan <site>` | Content strategy: industry templates, competitive analysis, editorial calendar, implementation roadmap (includes prioritization matrix: quick wins / big bets / fill-ins / avoid) | Annual content roadmap; deciding what to write next quarter |
| `/content competitor-pages <X vs Y>` | Generate SEO-optimized "X vs Y" comparison and "alternatives to X" pages with feature matrices and schema | "PolicyBazaar vs yallacompare" pages; "Salama alternatives" landing pages |
| `/content programmatic <plan>` | Programmatic SEO: template engines, URL patterns, thin-content safeguards, index-bloat prevention for pages generated at scale | Per-emirate or per-insurer template pages (e.g. 50 network-hospital pages) |

## 3. `/uae-insurance` — PolicyBazaar UAE Hub (3 playbooks)

| Skill | Detailed use | Application |
|---|---|---|
| `/uae-insurance flow` | The RACE operating loop — Research, Authority, Convert, Edge. Stage-specific prompt packs with vertical packs for health, travel, car, home, life | Your core weekly SEO operating rhythm; e.g. "run the Research stage for travel" |
| `/uae-insurance audit <url>` | Senior SEO+AEO audit of a UAE insurance page vs live local SERP competitors — detects vertical automatically, checks YMYL/regulatory compliance (incl. CBUAE license verification), outputs self-contained HTML report | Auditing /car-insurance/ against the real Dubai SERP before a relaunch |
| `/uae-insurance leads` | Leads intelligence: cross-references health/travel leads CSVs + SEMrush position tracking + GSC + GA4 to find dropped pages, diagnose root causes, output prioritised HTML recovery roadmap | Monthly "why did health leads drop?" investigation with a fix list |

## 4. `/ai-search` — AI Search Hub (default + 2 routes)

| Skill | Detailed use | Application |
|---|---|---|
| `/ai-search <topic>` *(default: citation scraping)* | Scrapes Google AI Overviews AND ChatGPT web-search citations for a prompt set; produces Excel citation-position matrix, raw JSON, verbatim answers, on-screen leaderboard | Monthly "are we cited in AI answers for health insurance UAE?" tracking (your June datasets in archive/ came from this) |
| `/ai-search geo <url>` | Generative Engine Optimization: brand-mention signals, AI-crawler accessibility, llms.txt, passage-level citability scoring, platform-specific optimization | Making PB pages more quotable by ChatGPT/Perplexity/AI Overviews |
| `/ai-search sxo <keyword>` | Search Experience Optimization: reads SERPs backwards to find page-type mismatches, derives user stories from intent signals, persona scoring | "Why isn't this well-optimized page ranking?" — intent mismatch diagnosis |

## 5. `/scrape` — Scrape Hub (4 modes)

All modes end with a live GSC + sitemap coverage check, 3-tier classification (🔄 UPDATE / 🆕 CREATE / 🔧 FIX), and two-way interlinking suggestions.

| Skill | Detailed use | Application |
|---|---|---|
| `/scrape <topic>` *(default: all sources)* | Scrapes Reddit UAE subreddits, Quora, Twitter/X, TrustPilot, Google My Business, and UAE news sites for a topic | Full landscape scan when entering a new topic (e.g. "golden visa insurance") |
| `/scrape news <topic>` | UAE news sites only: Gulf News, WAM, Al Etihaad, Khaleej Times, The National | Newsjacking — reacting to a new insurance regulation with timely content |
| `/scrape qna <topic>` | Reddit/Quora/Twitter questions and discussions only | Mining FAQs and content gaps — what real people actually ask |
| `/scrape reviews <topic> <location>` | TrustPilot + Google My Business reviews | Competitor pain-point mining; reputation monitoring for PB and rivals |

## 6. `/linkedin` — LinkedIn Hub (3 modes)

| Skill | Detailed use | Application |
|---|---|---|
| `/linkedin` write *(default)* — "write me a LinkedIn post about X" | Drafts a research-backed post on one of three pillars (SEO+AI `seo-ai`, AI in daily life `ai-life`, vibe coding `vibe-coding`) by scraping 3–5 live sources, scores engagement potential; text-only or with an auto-generated image | Your personal brand posting; e.g. "write a post about AI Overviews killing CTR, with an image" |
| "comment on relevant posts in my feed" *(feed engage)* | Drives your logged-in browser, scans your home feed, shortlists on-topic recent posts, drafts comments in your voice, posts each only after your approval | Daily 10-minute engagement routine without doomscrolling |
| "reply to the comments on my posts" *(reply)* | Opens your recent posts, pulls every comment thread, flags unanswered ones, drafts replies in your voice, posts after per-item approval | Clearing your notifications after a post takes off |

## 7. Dev & workflow skills

| Skill | Detailed use | Application |
|---|---|---|
| `/deploy <env>` | Pre-deploy checks then deploys this project to the given environment | Shipping to staging/production safely |
| `/security-review` | Security review of code changes: auth, secrets, injection, payments, user data | Before merging anything touching auth or user data |
| `/review` (command) | Reviews current changes for bugs, style, and test coverage | Quick PR self-check |
| `/fix-issue <number>` (command) | Fetches a GitHub issue and implements a fix | One-shot issue resolution |
| `/graphify <input>` | Turns any input (code, docs, papers) into a persistent knowledge graph with query/path/explain tools; `graphify query "<question>"` answers codebase questions from the graph | Understanding a new codebase or keeping the workspace graph current |
| `/debate <topic>` (plugin) | Multi-model debate/review — several models argue a question and converge | Second opinion on a big decision (venv needs recreating first — see CLAUDE.local.md) |

## 8. Supporting agents (invoked automatically, not by you)

| Agent | Used by | What it does |
|---|---|---|
| `ai-overview-scraper` | `/ai-search` (default mode) | Drives the browser to collect AI Overview / ChatGPT citations per prompt |
| `code-reviewer` | after significant code changes | Expert review pass |
| `security-auditor` | changes touching auth/payments/data | Security-focused review pass |

---

## Cheat sheet — most-used one-liners

```
/uae-insurance flow                          # start the weekly RACE loop
/uae-insurance leads                         # investigate a leads drop
/ai-search health insurance uae              # AI-citation tracking run
/seo google /health-insurance/               # GSC data for a page
/seo drift baseline                          # snapshot SEO state before a deploy
/content brief best travel insurance uae     # writer brief
/scrape qna car insurance                    # FAQ mining
/linkedin write about AI Overviews, with image
```
