# SEO, Schema, AIO & GEO — Master Testing Checklist
### Motorcycle/Bike Forum & Marketplace — Reusable Reference

This is a standalone, reusable test-plan covering every SEO-adjacent testing surface for a
combined **discussion forum + vehicle-listing marketplace**: technical SEO, on-page SEO,
schema/structured data, GEO (Generative Engine Optimization), AIO (AI Overview / AI-citation
testing), SXO, E-E-A-T/fact-check/AI-detection/content-trust, site structure & monitoring,
Google/DataForSEO data pulls, local SEO & maps, backlinks, images, hreflang, vehicle-listing
schema, and forum/UGC-specific SEO.

Most of this document is generic SEO/GEO/schema methodology that applies to any site. **Part M
(vehicle listings) and Part N (forum SEO)** are the two sections adapted specifically for this
vertical — this workspace has no dedicated automotive-marketplace or forum-UGC skill, so those two
parts are authored/adapted rather than pulled from an existing skill file; treat their specific
numbers as reasonable starting points to validate against your own data, not verified facts.

**How to use this document:**
- Run a full audit → work top to bottom, or run `/seo audit <url>` (it already orchestrates most
  of Parts A–C, G–H, and delegates conditionally to I/J/M's generic e-commerce/product layer).
- Auditing one page → Parts A–F cover everything scoreable from a single URL or piece of content.
- Auditing a vehicle listing specifically → Part M.
- Auditing a forum thread or subforum → Part N.
- Chasing a specific problem (AI citations, local rankings, backlink health) → jump to the
  matching part.
- Every part ends with the skill/command that runs it — this document is the criteria, not the
  tool.

---

## Table of Contents

- [Priority & Severity Framework](#priority--severity-framework)
- [Part A — Technical SEO](#part-a--technical-seo)
- [Part B — On-Page SEO](#part-b--on-page-seo)
- [Part C — Schema & Structured Data](#part-c--schema--structured-data)
- [Part D — GEO (Generative Engine Optimization)](#part-d--geo-generative-engine-optimization)
- [Part E — AIO / AI-Citation Tracking & SXO](#part-e--aio--ai-citation-tracking--sxo)
- [Part F — E-E-A-T, Fact-Check, AI-Detection & Content Trust](#part-f--e-e-a-t-fact-check-ai-detection--content-trust)
- [Part G — Site Structure & Monitoring](#part-g--site-structure--monitoring)
- [Part H — Google Data & Live SERP/Keyword Data](#part-h--google-data--live-serpkeyword-data)
- [Part I — Local SEO, GBP & Maps](#part-i--local-seo-gbp--maps)
- [Part J — Backlinks](#part-j--backlinks)
- [Part K — Images](#part-k--images)
- [Part L — Hreflang / International SEO](#part-l--hreflang--international-seo)
- [Part M — Vehicle Listing & Marketplace Schema](#part-m--vehicle-listing--marketplace-schema)
- [Part N — Forum SEO & UGC Management](#part-n--forum-seo--ugc-management)
- [Part O — Full-Site Audit Methodology & Health Score](#part-o--full-site-audit-methodology--health-score)
- [Appendix — Skill/Command Quick Reference](#appendix--skillcommand-quick-reference)

---

## Priority & Severity Framework

| Priority | Definition | Fix window |
|---|---|---|
| **Critical** | Blocks indexing, causes penalties, or is SEO-breaking with likely traffic loss | Immediately |
| **High** | Significantly impacts rankings | Within 1 week |
| **Medium** | Optimization opportunity | Within 1 month |
| **Low** | Nice to have | Backlog |
| **Info** | Awareness only, may be intentional | Review at convenience |

A 3-tier variant (Critical / Warning / Info) is used for drift/regression detection specifically —
same meaning, mapped to "respond immediately / investigate within 1 week / review at convenience."

---

## Part A — Technical SEO

9-category audit. Full-site version rolls up into a full-site audit (Part O).

### A1. Crawlability
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| robots.txt validity | Exists at root, valid syntax, not blocking important resources | Present, parses correctly, no disallow on critical paths | manual fetch / crawler |
| XML sitemap | Exists, referenced in robots.txt, valid XML format | Present + referenced + well-formed | manual fetch |
| Noindex tags | Distinguish intentional vs accidental noindex | Noindex only on pages meant to be excluded | HTML source scan |
| Crawl depth | Important pages reachable from homepage | ≤3 clicks from homepage | site crawl |
| JS-dependent content | Critical content requires JS execution to appear | Critical content present in raw/initial HTML | source vs rendered diff |
| Crawl budget | For sites >10k pages, crawl efficiency | No excessive low-value URLs consuming budget (e.g. sort/filter combinations on listing pages, thin forum search-result pages) | log analysis / crawl |
| AI crawler management | robots.txt tokens for GPTBot, ChatGPT-User, ClaudeBot, PerplexityBot, Bytespider, Google-Extended, CCBot | Deliberate allow/block decision per crawler (blocking Google-Extended ≠ blocking Googlebot; blocking GPTBot ≠ blocking ChatGPT-User) | robots.txt review |

### A2. Indexability
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| Canonical tags | Self-referencing, no conflict with noindex | Present, correct, non-conflicting | HTML `<head>` scan |
| Duplicate content | Near-duplicates, parameter URLs, www vs non-www | No unresolved duplicates | crawl + diff |
| Thin content | Word count below minimum for page type | Meets per-type minimum | word count |
| Pagination | rel=next/prev or load-more implemented correctly | Correct pattern present where paginated (forum threads, listing search results) | HTML scan |
| Hreflang | Correct for multi-language/multi-region | Valid reciprocal hreflang tags | see Part L |
| Index bloat | Non-value-add pages consuming crawl budget | Low ratio of low-value indexed pages (expired listings, empty facet pages, thin profiles) | GSC index coverage |

### A3. Security
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| HTTPS | Enforced, valid SSL cert, no mixed content | HTTP→HTTPS redirect, valid cert, zero mixed-content resources | browser/cert check |
| Security headers | CSP, Strict-Transport-Security (HSTS), X-Frame-Options, X-Content-Type-Options, Referrer-Policy | All 5 present and correctly configured | HTTP response headers |
| HSTS preload | Inclusion in HSTS preload list (high-security sites) | Listed | hstspreload.org |

### A4. URL Structure
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| Clean URLs | Descriptive, hyphenated, no query params for content | No query-string content URLs | URL audit |
| Hierarchy | Logical folder structure reflecting architecture | Matches site IA (e.g. `/listings/make/model/`, `/forum/subforum/thread/`) | URL audit |
| Redirects | No chains, 301 for permanent moves | Max 1 hop, correct status code | redirect trace |
| URL length | Flag long URLs | ≤100 characters | URL audit |
| Trailing slashes | Consistent usage | One convention site-wide | URL audit |

### A5. Mobile Optimization
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| Responsive design | Viewport meta tag, responsive CSS | Present and functional | HTML scan |
| Touch targets | Minimum size and spacing | ≥48×48px with 8px spacing | visual/DOM audit |
| Font size | Minimum base font size | ≥16px base | CSS audit |
| Horizontal scroll | Overflow on mobile viewport | None present | mobile emulation |
| Mobile-first indexing | Google indexes mobile version | Mobile version complete/equivalent to desktop | mobile snapshot |

### A6. Core Web Vitals
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| LCP (Largest Contentful Paint) | Load performance | <2.5s | PageSpeed Insights / CrUX |
| INP (Interaction to Next Paint) | Responsiveness (replaced FID Mar 12 2024) | <200ms | PSI / CrUX |
| CLS (Cumulative Layout Shift) | Visual stability | <0.1 | PSI / CrUX |
| Percentile basis | Evaluation methodology | 75th percentile of real-user (field) data | CrUX |

### A7. Structured Data (format check — full validation is Part C)
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| Format detection | JSON-LD (preferred), Microdata, RDFa | JSON-LD present as primary format | source scan |
| Type validation | Against Google's supported rich-result types | Matches supported schema | see Part C |

### A8. JavaScript Rendering
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| Content visibility | Present in initial HTML vs requires JS | Critical SEO content (title, meta robots, canonical, structured data) in raw HTML | source vs rendered diff |
| Rendering type | CSR vs SSR identification | Documented; SSR preferred for critical elements | source inspection |
| SPA framework flag | React/Vue/Angular detection | Flagged if indexing risk present | tech detection |
| Canonical conflict | Raw-HTML canonical vs JS-injected canonical | Must be identical | diff check |
| noindex + JS | noindex in raw HTML removed by JS | Google may still honor raw-HTML noindex — serve correct directive server-side | diff check |
| Non-200 status pages | JS execution on error/expired-listing pages | Google does not render JS on non-200 pages — meta/content must be in the response itself | status code check |
| Time-sensitive structured data | Listing price/availability injected via JS | Should be server-rendered to avoid delayed processing (critical for "sold" status accuracy) | source scan |

### A9. IndexNow Protocol
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| IndexNow support | Protocol implementation for Bing, Yandex, Naver | Implemented — especially valuable for fast-changing listing/thread content | endpoint/key check |

**Output:** Technical Score /100 with category breakdown, priority buckets (see framework above).

**Tool/command:** `/seo technical <url>`

---

## Part B — On-Page SEO

Two complementary layers: **B1** is the content-level scoring rubric (works from pasted text or a
URL, 12 parameters, point-scored). **B2** is the live-page structural checklist (requires a
fetchable URL, covers meta/OG/Twitter/robots that content-level scoring can't see).

### B1. Content-Level SEO Scoring (12 parameters, 98 pts total)

| # | Parameter | Pts | What to check | Scoring bands |
|---|---|---|---|---|
| 1 | Title Tag | 10 | Present, 50–60 chars, primary keyword natural (not stuffed), unique, compelling for CTR | 10: all present · 7–9: minor length issue · 4–6: missing keyword/generic · 0–3: absent/duplicate/stuffed |
| 2 | Meta Description | 8 | Present, 140–160 chars, keyword, value prop/CTA, unique, natural | 8: all present · 5–7: minor issues · 3–4: too short/long/generic · 0–2: missing/duplicate |
| 3 | Heading Hierarchy H1–H6 | 10 | Exactly one H1 reflecting topic, logical H2–H6, no skipped levels, meaningful keywords, no bold-as-heading | 10: clean hierarchy · 7–9: one skipped level · 4–6: multiple H1s/flat structure · 0–3: no headings/chaos |
| 4 | Keyword Usage & Density | 10 | Primary keyword in H1 + first 100 words + naturally throughout, density 1–2%, LSI/semantic terms present, keywords in alt text | 10: full distribution + LSI · 6–9: density/LSI thin · 3–5: missing from H1/intro or over-optimized · 0–2: absent or >3% stuffed |
| 5 | Content Depth & Length | 10 | Word count vs type (listing page 300–600 · buying guide/forum digest 1,200–2,500, 1,500+ for GEO · comparison 800–1,500 · FAQ 600–1,200); comprehensive; unique insight; intent-matched. **Density over length** — a dense shorter page beats a padded longer one | 10: appropriate + comprehensive + unique + intent-matched · 6–9: correct length, thin/unoriginal · 3–5: too short or shallow · 0–2: <300 words or padded filler |
| 6 | Readability Score | 8 | Flesch-Kincaid grade 8–10 for a general enthusiast audience; sentences avg 15–20 words (none >35 unbroken); paragraphs 2–4 sentences; passive voice <15%; jargon defined on first use (e.g. "VIN," "clean title," "groupset") | 8: varied, short paragraphs, jargon explained · 5–7: 1–2 long sentences/paragraphs · 3–4: dense, frequent jargon · 0–2: unreadable walls of text |
| 7 | Internal Linking | 8 | ≥2–3 contextual internal links, descriptive anchors (not "click here"), relevant targets, no orphan risk; grep the site's own URL list for keyword fragments from the page's own subtopics to catch missed-opportunity links | 8: 3+ contextual, descriptive · 5–7: 1–2 links, mostly good · 3–4: generic anchors · 0–2: none |
| 8 | Image Alt Text | 6 | Descriptive, keyword-relevant where natural, not stuffed, decorative images use `alt=""`. No images → award full 6 pts | 6: all images good · 4–5: minor issues · 2–3: generic/missing on key images · 0–1: none |
| 9 | Duplicate/Thin Content Risk | 10 | Unique angle, no near-duplicate sections, no copy-paste/boilerplate, original examples/data. **Find-and-replace test**: could this run on a competing marketplace/forum with just the brand swapped? | 10: unique, fails the find-replace test · 6–9: 1–2 generic filler sections · 3–5: heavy boilerplate reliance · 0–2: near-duplicate/generic, passes the find-replace test |
| 10 | Structured Data Signals (URL only) | 10 | Extract actual JSON-LD `@type`s incl. inside `@graph`; parse check; parity check (markup matches visible content); coverage check (obvious missing type); cross-check against Part C's page-type table for this site | 10: 3+ valid types, matches content, no gap · 6–9: 1 parity gap or missing type · 3–5: only 1 basic type or stale markup · 0–2: none despite clear opportunity, or broken/contradicting markup |
| 11 | CTA Clarity | 5 | Clear CTA matching intent (informational → "Read the full thread"; transactional → "Contact seller"/"Message seller"), specific not generic, logically placed | 5: clear, specific, well-placed · 3–4: generic/misaligned · 0–2: buried/vague/missing |
| 12 | Mobile/UX Red Flags in Copy | 5 | No "as shown above" refs to missing visuals, no "click below" with no button, no 20+ item bullet lists, no horizontal-scroll-risk blocks, no desktop-only assumptions | 5: none · 3–4: 1 minor issue · 0–2: 2+ issues |

**Keyword-conflation note:** "motorcycle" vs "bike" vs "moto" vs a specific model name/number are
often distinct search terms — flag if a page targets several without differentiating them. Watch
for year/trim ambiguity too (e.g. "2023 Duke 390" vs bare "Duke 390" as different search intents).

**Tool/command:** content-audit-style scoring — `/content audit <url or file>` if a comparable
skill is available, or apply this rubric manually.

### B2. Live-Page Structural Checklist

**On-Page SEO**
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| Title tag | Length, keyword, uniqueness | 50–60 chars, primary keyword, unique site-wide | HTML `<title>` |
| Meta description | Length, appeal, keyword | 150–160 chars, compelling, keyword | HTML meta scan |
| H1 | Count, intent match, keyword | Exactly one, matches intent, includes keyword | HTML scan |
| H2–H6 | Hierarchy | Logical, no skipped levels, descriptive | HTML scan |
| URL | Format | Short, descriptive, hyphenated, no params | URL audit |
| Internal links | Sufficiency, anchor text, orphan check | Sufficient, relevant anchors, no orphans | link graph |
| External links | Authority, count | Authoritative sources, reasonable count | link audit |

**Technical Elements**
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| Canonical tag | Present, correct target | Self-referencing or correctly pointed | HTML head scan |
| Meta robots | Index/follow directive | `index,follow` unless intentionally blocked | HTML head scan |
| Open Graph | og:title, og:description, og:image, og:url | All 4 present and populated | HTML head scan |
| Twitter Card | twitter:card, twitter:title, twitter:description | All present | HTML head scan |
| Hreflang | If multi-language | Correct implementation | see Part L |

**Schema Markup (page-level)**
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| Type detection | All types present, JSON-LD preferred | Detected and enumerated | source scan |
| Required properties | Validate against type spec | All required properties present | see Part C |
| Missing opportunities | Content vs. applicable schema types | Opportunities identified | content-to-schema mapping |
| Deprecated/restricted guardrail | HowTo (deprecated), FAQ (restricted) | Never recommend HowTo; FAQ only per Part C rules | policy check |

**Images**
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| Alt text | Present, descriptive, keyword-natural | Present and descriptive on all images | HTML scan |
| File size | Thresholds | Warning >200KB; Critical >500KB | file size check |
| Format | Modern format usage | WebP/AVIF over JPEG/PNG | format scan |
| Dimensions | width/height set | Present, for CLS prevention | HTML scan |
| Lazy loading | Method used | Report `lazy_method`: native/perfmatters/ewww/js-generic/none — don't flag JS-driven lazy-loaders as a regression | HTML/script scan |

**Core Web Vitals (heuristic flags from static HTML only)**
| Test | What to check | Pass criteria |
|---|---|---|
| LCP risk | Huge hero/listing images, render-blocking resources | None found |
| INP risk | Heavy JS, missing async/defer | None found |
| CLS risk | Missing image dimensions, injected content | None found |

**Output:** Page Score Card — overall /100 + 5 sub-scores (On-Page, Content Quality, Technical,
Schema, Images).

**Tool/command:** `/seo page <url>`

---

## Part C — Schema & Structured Data

### C1. Detection & Validation Method

| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| JSON-LD scan | `<script type="application/ld+json">` blocks | Found and parseable | source scan |
| Microdata scan | `itemscope`/`itemprop` attributes | Found if used | HTML attribute scan |
| RDFa scan | `typeof`/`property` attributes | Found if used | HTML attribute scan |
| Format preference | Primary format | JSON-LD always recommended primary | policy check |
| Required properties | Per schema type | All required properties present | type spec diff |
| Rich-result eligibility | Against Google's supported types | Type currently eligible | Google docs cross-check |
| Missing `@context` | Structural error | Present (`https://schema.org`) | JSON-LD parse |
| Invalid `@type` | Structural error | Real, non-deprecated schema.org type | JSON-LD parse |
| Wrong data types | Field-level error | Fields match expected type (string/number/date/object) | JSON-LD parse |
| Placeholder text | Content integrity | No literal placeholders (`[Seller Name]`) in production markup | text scan |
| Relative URLs | Format error | Absolute, not relative | field scan |
| Invalid date formats | Format error | ISO 8601 | field scan |

### C2. Schema Type Lifecycle

| Status | Types | Rule |
|---|---|---|
| **ACTIVE** (recommend freely) | Organization, LocalBusiness, SoftwareApplication, WebApplication, Product, ProductGroup, Offer, Service, Article, BlogPosting, NewsArticle, Review, AggregateRating, BreadcrumbList, WebSite, WebPage, Person, ProfilePage, ContactPage, VideoObject, ImageObject, Event, JobPosting, Course, DiscussionForumPosting | Safe |
| **VIDEO & SPECIALIZED** (recommend freely) | BroadcastEvent, Clip, SeekToAction, SoftwareSourceCode | Safe |
| **RESTRICTED** | FAQPage | ONLY for government and healthcare authority sites (restricted Aug 2023; removed from Google Search entirely May 2026) — still valid schema.org, still consumed by AI engines, but never promise FAQ rich results for a forum or marketplace |
| **DEPRECATED** (never recommend) | HowTo (rich results removed Sept 2023), SpecialAnnouncement (deprecated Jul 2025), CourseInfo/EstimatedSalary/LearningVideo (retired 2025), ClaimReview (retired 2025), VehicleListing (retired from rich results 2025 — **note:** this is the schema.org type named "VehicleListing," not vehicle-listing pages in general; use `Product`/`Vehicle`-pattern markup per Part M instead), Dataset (rich result, retired 2025), Sitelinks SearchBox/SearchAction (removed Nov 29 2024), QAPage (UGC single-question forums only — see C3 for when this legitimately applies) | Fail if present/recommended |
| Historical note | Book Actions | Deprecated then reversed — still functional |

### C3. Forum & Bike-Listing Page-Type × Expected Schema Stack

| # | Page Type | Expected stack (one `@graph`) |
|---|---|---|
| 1 | Homepage | WebSite · Organization (`@id`) · WebPage · BreadcrumbList |
| 2 | Individual listing (bike for sale) | `Product` (+ Vehicle-pattern properties if motorized, see Part M) · `brand` → Organization/manufacturer · `offers` → Offer (price, currency, availability) · BreadcrumbList · ImageObject gallery |
| 3 | Listing category/search-results page (browse by make/model/year/price/location) | CollectionPage · ItemList → listings · BreadcrumbList — **never** put Product schema on the list page itself, only on individual listings |
| 4 | Seller/dealer profile page | Organization (dealer) or Person (private seller) · AggregateRating only if genuine reviews are collected · BreadcrumbList |
| 5 | Forum category/subforum page | CollectionPage · ItemList → threads · BreadcrumbList |
| 6 | Forum thread page | DiscussionForumPosting (root post) · Comment entities for replies · `interactionStatistic` for reply/view counts where available · BreadcrumbList |
| 6a | Single-question Q&A thread (narrow use) | QAPage — only for genuine single-question/single-best-answer threads, not general discussion |
| 7 | User profile page (forum member) | ProfilePage · Person — thin-value page; index only if it carries genuine public content (see Part N3) |
| 8 | Buying guide / editorial article | Article · `author` → Person · BreadcrumbList |
| 9 | Brand/model hub page (aggregates listings + forum threads for one model) | CollectionPage · ItemList · BreadcrumbList |
| 10 | Comparison page (Model A vs Model B) | Article or WebPage · comparison-table markup |
| 11 | Model review/ratings page (owner reviews of a model, not a specific listing) | Review · AggregateRating tied to the model entity |
| 12 | Event/meetup page (community rides, swap meets) | Event |
| 13 | FAQ/help page | FAQPage — valid schema.org, useful for AI engines, but not eligible for a Google rich result per the RESTRICTED rule above |

### C4. Site-Wide Foundation (every page)

1. **Organization** — ONE canonical node, `"@id":"https://www.example.com/#organization"`,
   referenced (never re-declared). Properties: name, legalName, url, logo (≥112×112, works on
   white), telephone, address, sameAs.
2. **WebSite** — `"@id":".../#website"`, `publisher`→`{"@id":"#organization"}`. Only include
   `SearchAction` if the site genuinely has an on-site search feature that supports it.
3. **WebPage** (or subtype) — `@id`, url, name, description, `inLanguage`, `isPartOf`→#website,
   `breadcrumb`→breadcrumb `@id`, datePublished/dateModified, primaryImageOfPage.
4. **BreadcrumbList** — on every page.

### C5. Common Schema Mistakes to Check For

General patterns worth grepping for on classifieds/forum sites — check whether each applies to
this site rather than assuming any of them do:

| # | Pattern | Fix |
|---|---|---|
| 1 | `mainEntityOfPage:"True"` (string literal) on Article/guide pages | Canonical URL or `{"@type":"WebPage","@id":"<url>"}` |
| 2 | Identical review count/rating pasted across unrelated listings or seller pages | Remove boilerplate; ratings only on genuinely-reviewed entities |
| 3 | Review/post `datePublished` not ISO-8601 | ISO-8601 (`2026-02-24`) |
| 4 | Listing `Product` nodes missing image/brand/offers | Use the Vehicle/Bicycle listing template (Part M) |
| 5 | WebPage nodes missing `name`/`url`/`@id` | Foundation item 3 above |
| 6 | Breadcrumb omits the current page as its own final item | Add final ListItem |
| 7 | Empty `description` (length 0) on Article/guide pages | Populate or drop |
| 8 | Trailing spaces in names/headlines; empty `keywords:[]` | Trim; drop empty arrays |
| 9 | **Sold listing still marked `InStock`** | Update to `OutOfStock`/`Discontinued`, or 410/redirect the page — see Part M8 |
| 10 | `Product` schema applied to a forum thread page, or `DiscussionForumPosting` applied to a listing page | Match page type to schema per C3 |

### C6. Blocklist — NEVER Recommend

| Type | Why |
|---|---|
| HowTo | Rich results removed Sept 2023 |
| Sitelinks SearchBox/SearchAction | Removed Nov 29 2024; only include if the site genuinely has on-site search |
| SpecialAnnouncement | Deprecated Jul 2025 |
| ClaimReview, Dataset (rich result), VehicleListing (the specific schema.org type), EstimatedSalary, LearningVideo | Retired 2025 |
| QAPage (outside the narrow single-question use in C3-6a) | UGC single-question forums only |
| Carousel/ItemList as rich result | Gallery limits to Recipe/Course/Restaurant/Movie — ItemList stays for entity/GEO value only |

**FAQPage caveat ⚠️:** restricted Aug 2023, removed from Google Search entirely May 2026. Keep
deploying it on FAQ/help pages (valid schema.org, consumed by AI engines) — never promise FAQ
stars. Strip "Q1." prefixes from `Question.name`; answers may carry HTML links.

### C7. Key Templates & Entity-Direction Rules

**Motorized vehicle listing (motorcycle/scooter) — Product + Vehicle-pattern properties:**
```json
{
  "@type": "Product",
  "name": "<year make model trim>",
  "image": ["…front.jpg", "…side.jpg", "…odometer.jpg", "…vin-plate.jpg"],
  "brand": { "@type": "Organization", "name": "<manufacturer>" },
  "vehicleIdentificationNumber": "<17-char VIN>",
  "mileageFromOdometer": { "@type": "QuantitativeValue", "value": "…", "unitCode": "SMI" },
  "productionDate": "<model year>",
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "fuelType", "value": "…" },
    { "@type": "PropertyValue", "name": "engineDisplacement", "value": "…cc" },
    { "@type": "PropertyValue", "name": "vehicleTransmission", "value": "…" }
  ],
  "offers": { "@type": "Offer", "price": "…", "priceCurrency": "…",
              "availability": "https://schema.org/InStock",
              "seller": { "@id": "https://www.example.com/#organization" } }
}
```
`vehicleIdentificationNumber`, `mileageFromOdometer` and the engine/fuel/transmission properties
aren't part of Google's core Product rich-result requirements, but they add real entity/GEO value —
AI engines and vehicle-specific search features parse them even without a dedicated rich result.

**Pedal bicycle listing — lighter Product-only pattern (no motor properties):**
```json
{
  "@type": "Product",
  "name": "<year make model, frame size>",
  "image": ["…"],
  "brand": { "@type": "Organization", "name": "<manufacturer>" },
  "additionalProperty": [
    { "@type": "PropertyValue", "name": "frameSize", "value": "…" },
    { "@type": "PropertyValue", "name": "wheelSize", "value": "…" },
    { "@type": "PropertyValue", "name": "groupset", "value": "…" }
  ],
  "offers": { "@type": "Offer", "price": "…", "priceCurrency": "…",
              "availability": "https://schema.org/InStock" }
}
```

**Seller/dealer pages — entity direction:** the page is *about the seller* → `mainEntity`→
Organization (dealer) or Person (private seller). AggregateRating only for genuinely-collected
reviews of that seller — never paste the marketplace's own aggregate rating onto an individual
seller's page.

**Forum thread — E-E-A-T chain:** `author`→Person (the original poster), linked to a ProfilePage
only if that profile carries real public content. `publisher`→`{"@id":"#organization"}` for the
site itself. Keep `dateModified` accurate to the last genuinely substantive reply, not just any
bump.

**Rendering:** JSON-LD must be server-rendered in initial HTML — JS-injected structured data faces
delayed processing (Google Dec 2025 guidance), which is especially costly for time-sensitive
listing availability.

**Output:** validation table (Schema | Type | Status ✅/⚠️/❌ | Issues) plus generated JSON-LD where
missing.

**Tool/command:** `/seo schema <url>` (generic validation/generation mechanics from C1–C2) — the
page-type stack (C3–C7) should be consulted manually alongside it for this site's page types.

---

## Part D — GEO (Generative Engine Optimization)

GEO optimizes content so AI engines (ChatGPT, Perplexity, Google AI Overviews, Gemini, Claude) cite
it. The foundational GEO study (Aggarwal et al., ACM KDD 2024, 10,000 queries) found statistics,
citations, and quotations improve AI-engine visibility by up to 40%. AI Overview keyword share grew
1.5%→~32% of searches Sep 2024–Sep 2025; AI search platform visits grew 42.8% YoY vs Google's 2.4%.
~86% of top Google results and ~82% of ChatGPT/Perplexity citations are still human-written — what
separates winners is original data, visible credentials, and a specific angle, not authorship.
Purchase decisions (a used vehicle is a real financial commitment) and safety-adjacent content
(maintenance, recalls) both draw somewhat stricter AI/quality scrutiny than pure entertainment
content — treat this vertical as "purchase-decision + community-safety" content, one notch below
classic YMYL (health/finance) but well above a hobby blog.

**D1 covers content-level scoring** (from pasted text or URL). **D2 covers technical/platform-level
GEO factors** that require live crawling/rank data.

### D1. Content-Level GEO Scoring (11 parameters, 100 pts total)

| # | Parameter | Pts | What to check | Scoring bands |
|---|---|---|---|---|
| 1 | Direct-Answer Formatting | 15 | Intro answers the core question in 2–3 sentences; H2/H3 sections lead with a direct 1–2 sentence answer before expanding; no buried-lede pattern | 15: every section leads with a direct answer · 10–14: 1–2 buried-lede violations · 5–9: inconsistent, half bury the lead · 0–4: everything context-first |
| 2 | E-E-A-T Signals | 11 | Experience (real ownership/riding-history detail), Expertise (author+credentials, mechanic quotes), Authoritativeness (manufacturer specs/service bulletins/recall databases cited), Trustworthiness (transparent, no exaggeration — freshness scored separately in #11); marketplace verification/anti-fraud signal | 11: all 4 pillars + trust signal · 7–10: 3 of 4 · 3–6: 2 of 4 · 0–2: none |
| 3 | Entity Clarity | 6 | Precise model names/trims ("KTM Duke 390," not "a naked bike"), precise specs (displacement, model year), specific geography ("Austin, TX," not "somewhere in Texas"), terms defined in context ("VIN," "clean title," "salvage title") | 6: all major entities precise · 4–5: 1–2 vague · 2–3: several vague/conflated · 0–1: generic throughout |
| 4 | Conversational Q&A Coverage | 15 | Real FAQ/forum-derived questions (not vanity), conversational/voice-search phrasing, answers ≤3 sentences, long-tail variants. When verifying a URL: cross-check questions against actual forum threads and community Q&A — plausible-but-unfindable questions are a specificity flag | 15: 5+ genuine pairs, concise · 10–14: 3–4 pairs · 5–9: 1–2 pairs or vague FAQ · 0–4: no Q&A structure |
| 5 | Statistics & Citations | 10 | Specific stats (prices, dates, counts, reliability data), sourced claims, recent (not "in 2019…"), market-specific vs generic global numbers, nothing made-up | 10: 3+ specific recent attributed stats · 6–9: 2 stats or 1 well-cited · 3–5: 1 vague/unattributed · 0–2: none or generic only |
| 6 | Schema/Structured Data Mentions | 6 | Content structure maps to schema types: FAQ structure→FAQPage-ready, numbered maintenance steps→content signal only (HowTo itself is blocklisted, see C6), author+date→Article-ready, spec tables→Product-ready, owner reviews→Review-ready | 6: maps to 3+ types · 4–5: 2 types · 2–3: 1 type · 0–1: none |
| 7 | Content Depth & Original Angle | 8 | Depth (4pt): all sub-topics covered, real examples/scenarios, terms defined, multiple intent angles, 1,500+ words as a floor not target. Original angle (4pt): a fact/data point/example not generic across competing sites — **find-and-replace test** applies here too | 7–8: 1,500+ words/dense, comprehensive, clear original angle · 5–6: strong on depth OR angle, weak on other · 2–4: 1,000–1,499 words, generic/interchangeable · 0–1: <500 words or find-replaceable |
| 8 | Semantic Heading Use | 6 | H2s contain keywords/question phrases, logical general→specific progression, headings stand alone as a summary. **Generic-heading test**: would this heading fit any other topic unchanged? Flag "Introduction/Conclusion/More Details/Why Choose Us/Benefits (bare)/Get Started" | 6: all semantic · 4–5: 1–2 generic · 2–3: half/half · 0–1: generic/vanity throughout |
| 9 | Brand/Source Credibility Signals | 3 | Site named, identified as a verified/moderated marketplace (not just an anonymous listings dump), trust signal (years active, listings volume, member count, reviews), no anonymous "the team" authorship | 3: all present · 2: 2–3 of above · 1: brand name only · 0: anonymous |
| 10 | Fan-out Rank | 12 | Does the page answer the likely fan-out sub-questions an AI research-mode assistant would ask (e.g. "buying a used motorcycle" fans into financing, inspection checklist, title transfer, insurance) — not just the primary query? FILE mode: judge topical-neighborhood coverage. URL mode: also check if part of a linked topic cluster covering sub-questions this page doesn't | 12: 4+ sub-questions answered or clearly clustered · 8–11: 2–3 sub-questions · 4–7: 1 beyond primary · 0–3: only primary query, no cluster |
| 11 | Freshness | 8 | Last-updated/as-of date present and genuinely recent; time-sensitive claims (prices, model-year-specific info) carry "as of" qualifiers; no stale year refs. FILE mode: score whether the *draft* signals its own currency, not the deploy-time publish date | 8: dated/qualified throughout, current · 5–7: 1–2 claims lack as-of framing · 2–4: no clear signal · 0–1: stale info stated as current |

**Freshness vs. Fact-Check's "Outdated Information Risk" (Part F):** Freshness checks whether a
claim *looks* current (dates/as-of framing present, structural). Outdated Information Risk (Part
F2) checks whether a claim *is* actually still true, verified live via `web_search`. A page can
score well on one and fail the other — both may legitimately fire on the same finding; that's
expected overlap, not a duplicate rule.

**Tool/command:** apply this rubric manually, or via `/content audit <url or file>` if a comparable
skill is configured for this site.

### D2. Technical/Platform GEO Factors (out of scope for D1 — requires live crawl/rank data)

**AI-Crawler Accessibility (robots.txt)**
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| Crawler enumeration | robots.txt entries for GPTBot, OAI-SearchBot, ChatGPT-User (OpenAI), ClaudeBot (Anthropic), PerplexityBot, CCBot (Common Crawl/training), anthropic-ai, Bytespider, cohere-ai | GPTBot/OAI-SearchBot/ClaudeBot/PerplexityBot **Allow**ed; CCBot/pure-training crawlers **Block**ed if desired | Manual `/robots.txt` read |
| Error case | Any AI crawler disallowed | Report exactly which crawlers blocked vs allowed + exact directive fix | error handling |

*Known gap:* Google-Extended (Gemini/Bard training crawler) and server-log-based verification of
actual crawler visits (vs. robots.txt directive alone) aren't covered by the underlying skill as
written — test manually via server logs if that matters.

**llms.txt Standard**
| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| File presence | `/llms.txt` at domain root | Exists | Manual fetch |
| Format compliance | `# Title` + `> description` + `## Main sections` (markdown links+descriptions) + optional `## Optional: Key facts` | Matches template | — |
| Missing | No file found | Generate a ready-to-use template from the site's actual structure | — |

**RSL 1.0 (Really Simple Licensing)** — machine-readable AI licensing terms. Check for
implementation and appropriate terms.

**Passage-Level Citability (25% of GEO technical score)**
| Test | What to check | Pass criteria |
|---|---|---|
| Optimal passage length | Word count of self-contained answer blocks | 134–167 words |
| Direct-answer placement | Where the answer sits | Within first 40–60 words |
| Definitional framing | Sentence pattern | "X is…" / "X refers to…" |
| Extractability | Can it stand alone | Self-contained, quotable, specific facts, unique data, attributed claims |
| Weak-signal fail conditions | Vague statements, unsupported opinion, buried conclusion, no data points | None present |

**Structural Readability & SSR Accessibility (20% + 20% of GEO technical score)**
| Test | What to check | Pass criteria |
|---|---|---|
| Heading hierarchy | H1→H2→H3, question-based headings | Clean, matches query patterns |
| Paragraph/format density | Length, tables/lists/FAQ use | Short paragraphs; tables for spec comparisons; lists for steps; clear Q&A |
| Server-side rendering | Renders without JS execution | SSR, not client-only — **AI crawlers do not execute JavaScript** |
| Ranking-position nuance | Citation source position | 92% of AI Overview citations come from top-10 pages, but 47% come from below position 5 — don't assume top-3-only sourcing |

**Multi-Modal Content Signals (15% of GEO technical score)** — text+images, embedded/linked video
(walk-around videos, ride footage), infographics/spec charts, interactive tools (payment/financing
calculators), structured data supporting media. Multi-modal content sees 156% higher selection
rates (benchmark, not a hard pass/fail).

**Off-Page Brand/Entity Presence (Authority — 20% of GEO technical score)**
| Test | What to check | Signal strength |
|---|---|---|
| Cross-platform entity presence | Wikipedia/Wikidata, Reddit, YouTube, social mentions | Brand mentions correlate more strongly with AI visibility than backlinks (per general GEO research); YouTube mentions tend strongest, followed by Reddit/forum mentions, Wikipedia, then domain rank/backlinks weakest |
| Byline/date/source signals | Author credentials, pub+update dates, primary-source citations, credentials, expert quotes | All present (weak: anonymous, no dates, no sources) |

**Platform-Specific Optimization**
| Platform | Citation source pattern | Optimization angle |
|---|---|---|
| Google AI Overviews | Top-10 ranking pages (92%) | Traditional SEO + passage optimization |
| ChatGPT | Wikipedia, Reddit-heavy | Entity presence + authoritative/community sources |
| Perplexity | Reddit-heavy, Wikipedia | Community validation, discussions — a strong fit for forum content |
| Bing Copilot | Bing index, authoritative sites | Bing SEO, IndexNow |

Only a small minority of domains are cited by both ChatGPT and Google AI Overviews for the same
query — platform-specific optimization is essential, not optional.

**Output:** Readiness Score /100, platform breakdown, crawler access status, llms.txt status,
brand mention analysis, passage-level citability, SSR check, top-5 highest-impact changes,
schema/content recommendations.

**Tool/command:** `/ai-search geo <url>` if a comparable skill is configured for this site.

---

## Part E — AIO / AI-Citation Tracking & SXO

### E1. AI-Citation Scraping Methodology

**Setup**
| Test | What to check | Pass criteria |
|---|---|---|
| Engine selection | Google AI Overview and/or ChatGPT web search | Explicit; default = Google AI Overview |
| Region/locale lock | Market targeting | Defaults to this site's target market/locale unless stated otherwise |
| Tracked-brand default | Which domain is highlighted | This site's own domain unless overridden |
| ChatGPT precondition | Session state | Logged into chatgpt.com in Chrome; flagged as slow/block-prone — many prompts legitimately return no sources |
| Prompt-set sourcing | Stored vs. supplied vs. generated | User-supplied prompts if available; else generate ~50 across intent buckets (model discovery, price/cost, buying process, specs/features, specific listing/seller, comparison/decision) |

**Measurement mechanics**
| Test | What to check | Mechanic |
|---|---|---|
| Citation "position" | How rank is computed | Order in the answer's cited-sources list — **not** classic blue-link SERP rank; must be stated as such in output |
| Verbatim capture | Answer text | Full verbatim text captured per prompt/engine, not paraphrased |
| Domain leaderboard | Matrix columns | Domains cited in ≥2 prompts, ranked by frequency, brand column highlighted |
| Coverage reporting | Engine success rate | e.g. "Google: 48/50 had an Overview, 0 blocks; ChatGPT: 31/50 answered, stopped by login wall at #32" |

**Data-integrity non-negotiables**
| Test | Requirement |
|---|---|
| No-fabrication rule | Missing sources must be stated explicitly — never present inferred content as scraped |
| Block reporting | Report exactly how far the scraper got, never silently truncated |
| Non-determinism disclosure | State this is one snapshot from one session/region, not a stable ranking |
| Engine sequencing | One browser/engine scraped at a time (sequential) |

**Tool/command:** `/ai-search <topic>` if a comparable skill is configured for this site.

### E2. SXO — Search Experience Optimization

**Fetch & parse preconditions:** SSRF-safe fetch (never raw curl on user-supplied URLs) · structured
parse (title, H1, meta desc, heading hierarchy, word count, schema, CTAs, media) · keyword
resolution (extract from title+H1 overlap if not supplied).

**SERP-backwards analysis:** per-result classification (top-10: URL, authority tier, page type,
content format, word count, schema, media) · SERP-features inventory (featured snippet, PAA, ads,
related searches, AI Overview + source types) · consensus thresholds: >60% strong consensus ·
40–60% mixed · <40% fragmented.

**Page-type mismatch severity**
| Target vs. SERP-dominant type | Severity |
|---|---|
| Forum thread vs Listing pages | CRITICAL — create a dedicated listing/hub page |
| Editorial/blog vs Comparison | HIGH — restructure with a spec-comparison matrix |
| Listing vs Informational (buying-guide intent) | HIGH — add an educational layer to the listing/category page |
| Category page vs Tool/Calculator | HIGH — build an interactive financing/comparison tool |
| Local browse page vs Local Results | MEDIUM — add location signals + local schema |
| Type match | ALIGNED — focus on depth/UX |

**User-story derivation:** PAA→knowledge gaps, ad-copy→commercial triggers, related searches→
journey stage, featured-snippet format→expected answer structure, AI Overview→"definitive answer."
3–5 stories, each traceable to a signal cluster: *"As a [persona], I want to [goal], because
[driver], but I'm blocked by [barrier]."*

**7-Dimension SXO Gap Score (0–100, lower = bigger gap):** Page Type (0–15) · Content Depth (0–15)
· UX Signals (0–15) · Schema Markup (0–15) · Media Richness (0–15) · Authority Signals (0–15) ·
Freshness (0–10). Kept explicitly separate from the SEO Health Score.

**Persona scoring (4 dimensions, 0–25 each, 4–7 personas per page):**
| Dimension | 21–25 | 16–20 | 11–15 | 6–10 | 0–5 |
|---|---|---|---|---|---|
| Relevance | Direct+specific | Covers topic, lacks depth | Tangential | Different audience | Irrelevant |
| Clarity | Above fold | Requires scroll/nav | Buried | Must piece together | Not present (bounce) |
| Trust | Multiple relevant signals | General only | Gaps | Minimal | None/undermining |
| Action | Clear low-friction CTA | Generic CTA | Present, not prominent | Mismatched CTA | Dead end |

Total/100 per persona: 80–100 Excellent · 60–79 Good · 40–59 Needs Work · 0–39 Critical Mismatch.
Weight buyer/browser personas higher if SERP shows strong commercial intent; enthusiast/research
personas higher if the SERP is dominated by informational/forum results.

**Tool/command:** `/ai-search sxo <keyword>` if a comparable skill is configured for this site.

---

## Part F — E-E-A-T, Fact-Check, AI-Detection & Content Trust

Four distinct scored lenses covering the trust/authenticity layer of content, on top of the pure
SEO (Part B1) and GEO (Part D1) scoring.

**Mode gate applying to E-E-A-T and Freshness:** FILE mode (draft/pasted text) — do NOT
score/penalize author byline, credentials, publish/update date, citation links, or brand-page
signals; these are publishing-time additions, not writer-controlled. URL mode (live page) — score
all signals in full.

### F1. E-E-A-T Framework (0–100)

| Pillar | Pts | What to check | Scoring |
|---|---|---|---|
| Experience | 0–25 | Real ownership/riding-history detail, practical realities an enthusiast would know (common failure points, aftermarket fitment issues), real comparative data from the marketplace itself ("500+ active listings"), acknowledged tradeoffs (not just marketing puffery) | 20–25: 3+ specific signals + real data · 10–19: 1–2 specific signals · 1–9: vague, could be any site · 0: none |
| Expertise | 0–25 | Author/reviewer credentials or demonstrated mechanical knowledge, correct technical terminology (torque specs, VIN decoding, title types), accurate technical claims | 20–25: named author/reviewer+credentials+accurate · 10–19: accurate, no named author · 5–9: some signals/errors · 0–4: generic, inaccurate |
| Authoritativeness | 0–25 | Citations to manufacturer specs/service bulletins/recall databases, sourced stats, named expert/mechanic quotes, verified-seller or dealer-certification program identified | 20–25: all present · 10–19: brand+1–2 signals · 5–9: brand only · 0–4: anonymous |
| Trustworthiness | 0–25 | Last-updated date visible, disclosure of affiliate/dealer relationships, balanced coverage (not just upsell), accurate listing claims (no hidden damage/mileage discrepancies), no dark-pattern urgency ("only 1 left!"), contact/support channel | 20–25: date+disclosure+balance+accuracy · 10–19: 2–3 signals · 5–9: 1 signal · 0–4: none/red flags |

**Total 80–100** Strong (citation-ready) · **60–79** Moderate · **40–59** Weak · **0–39** Critical
gaps. Feeds GEO Parameter 2 (Part D1).

**Tool/command:** apply manually, or via a content-quality skill if one is configured for this site.

### F2. Fact-Check Lens (0–100, live `web_search` verification)

**Process:** extract every checkable claim (price, mileage, engine displacement, model year,
claimed features, title status) → run a targeted `web_search` per claim against manufacturer specs
and known model data → status: ✅ Confirmed / ❌ Contradicted / ⚠️ Outdated / ⚠️ Unverifiable (flag
for human review, don't treat as false) → for any Contradicted/Outdated, supply corrected value +
source tier (Primary manufacturer data / Secondary-verify-internally / Snippet-only-must-verify).
If `web_search` unavailable, say so explicitly and score only on internal consistency.

| # | Parameter | Pts | What to check | Scoring |
|---|---|---|---|---|
| 1 | Numerical Accuracy | 25 | Price, mileage, engine displacement, model year, any number framed as "current" | 25: all confirmed current · 18–24: 1 minor outdated/unverifiable · 8–17: 2–3 contradicted/outdated · 0–7: systematically wrong |
| 2 | Specification/Claim Accuracy | 25 | Claimed trim/features actually exist for that model/year, claimed condition consistent with photos/description, title status (clean/salvage/rebuilt) framed accurately, no overstated performance claims | 25: all confirmed · 18–24: 1 minor issue · 8–17: a spec materially wrong or misleadingly framed · 0–7: multiple contradicted, or confidently wrong on title/condition |
| 3 | Model/Seller Name Accuracy | 15 | Model/trim correctly attributed (no naming/rebrand mix-up), seller/dealer actually exists and is reachable, no impossible model-year/spec combos | 15: all accurate/current · 10–14: 1 stale/rebrand-confused name · 5–9: a name mismatches search results · 0–4: multiple incorrect/fabricated-sounding |
| 4 | Statistical & Study Citation Accuracy | 15 | Cited figures (e.g. "most reliable bike in its class," "average resale value") match the named source's actual data, source is real/findable, not quietly stale | 15: all accurate to source · 10–14: 1 unverifiable-but-plausible stat · 5–9: a stat mismatches its source · 0–4: fabricated/systematically unverifiable |
| 5 | Outdated Information Risk | 10 | Are model-year-specific claims dated/qualified? Any annually-changing info (pricing, recalls, model refresh) with no "last reviewed" signal? | 10: dated/qualified, no decay risk · 6–9: minor risk, 1 claim · 3–5: several undated with real risk · 0–2: change-prone facts presented as permanent |
| 6 | General Factual Claims | 10 | Non-listing facts (model history, general mechanical background) still correct | 10: none/confirmed · 6–9: 1 minor inaccuracy · 3–5: a claim wrong, materially affects argument · 0–2: multiple general errors |

**Tool/command:** apply manually with live `web_search`, or via a fact-check skill if one is
configured for this site.

### F3. AI-Detection / Human-Likeness Signals (9 signals, 0–3 each, raw 0–27)

**Formula:** Human-Likeness Score = ((27 − raw) / 27) × 100. A phrase can fire at most 2 distinct
signals.

**Reliability caveat — report, don't omit:** commercial AI-detection tools (ZeroGPT, QuillBot,
GPTZero, Grammarly, Turnitin) have published accuracy ranges of roughly 55–97%, with false-positive
rates varying by orders of magnitude between tools, and Turnitin's own disclosed margin of error is
±15 points. **Report a score + the specific patterns that drove it — never a flat "is AI-written"
claim.** AI-sounding ≠ ranking risk — Google penalizes low-quality/thin/manipulative content
regardless of authorship; the real penalty case is scale-without-review, not AI use itself.

| Signal | What to check | 0–3 scoring basis |
|---|---|---|
| A. Perplexity (word predictability) | Generic verbs, content-free adjectives ("significant improvements"), hedged assertions, canonical AI-vocabulary list (delve, leverage, utilize, robust, comprehensive, streamline, foster, facilitate, pivotal, nuanced, notable/notably, garner, multifaceted, tapestry, testament, showcase, underscore, unlock, myriad, plethora…) plus vertical-flavored filler ("in the world of motorcycling," "whether you're a seasoned rider or a beginner," "hit the road with confidence") | Per instance, cite exact word/phrase |
| B. Burstiness Deficit | 3+ consecutive sentences within 5 words of each other; no sentence <8 words in any 150-word block; metronomic rhythm; no fragments for emphasis | Report as sentence-length sequence |
| C. Hedge Density | "often/generally/typically/in many cases" where direct assertion is warranted; "it is important to note that." **Exception:** legally required disclaimers never flagged | Quote each hedge, note if warranted |
| D. Structural Tells | Bullet list where prose serves better; topic-sentence+evidence+restatement; "In conclusion" closers; "In this guide I will…" openers; tricolon parallelism (strong); one-job-per-paragraph arc (moderate); strawman pivot "It's not about X, it's about Y" (moderate); trailing "…,making it ideal for X" (moderate); generic/templated headings (cross-ref GEO Parameter 8) | Per tell, severity as noted |
| E. Specificity Deficit | Abstract claims with no number/name/time/example; passive voice >~1/3 of sentences where active fits; universalist framing ("riders often find"); unanchored claims ("prices vary depending on factors" without naming them) | Quote each unanchored claim |
| F. Transition Word Fingerprint | Strong: "Furthermore,"/"Moreover,"/"Additionally," as openers, "It is clear that." Moderate: "However," >1/200 words, mechanical "Therefore,", fake-discovery "turns out," announcement-colon patterns | Strong vs moderate as listed |
| G. Punctuation Fingerprint | Em dashes as dramatic mid-sentence pivots; semicolons linking clauses that should split; multiple em dashes/paragraph. Em dashes alone are NOT diagnostic — only flag combined with other signals or >2 per 200 words | Combined-signal basis |
| H. Voice/Register Collapse | Press-release tone where expert advice expected; perfectly neutral tone on a topic a real enthusiast would have an opinion on; "helpful assistant" framing; no domain-specific voice | Fix template: `[Specific spec/model fact] — [specific consequence for reader] without [missing detail].` |
| I. Rhetorical Scaffolding (RLHF artifacts) | Aphoristic closers; "More like X than Y"; wisdom-dispensing narrator tone; fake humility; escalating three-beat rhythm; pseudo-paradox ("The best bike is actually…"); coached-feeling "you" address | Per instance |

**Thresholds:** raw 0–4 → 85–100 Human-consistent · 5–8 → 70–82 Mostly human-consistent · 9–13 →
52–67 Mixed signals · 14–19 → 30–48 AI-pattern-heavy · 20–27 → 0–26 Strongly AI-pattern-heavy.

**Calibration notes:** <100-word texts cap confidence at Medium; ESL writing can resemble AI
patterns — note if plausible; mixed authorship (AI draft + human edit) is common — report the
AI-edited fraction separately from the label. What actually moves the score: adding
data/names/firsthand detail and varying rhythm — not generic "humanizer" tools or synonym-swapping.

**Tool/command:** apply manually, or via an AI-detection lens if one is configured for this site.

### F4. Purchase-Decision Content Quality & Google Helpful-Content (0–100)

Google's Helpful Content system applies broadly to any UGC/marketplace site, and forums in
particular get scrutinized for thin/duplicate/AI-spam content at scale.

| # | Parameter | Pts | What to check | Scoring |
|---|---|---|---|---|
| 1 | Listing/Technical Accuracy | 20 | Claims about a bike's condition/specs/safety match reality; no unsupportable claims ("never dropped" without evidence); safety-relevant maintenance advice is technically sound | 20: all verifiable/current, no unsupported claims · 14–19: 1 minor unverified claim · 8–13: 2–3 inaccuracies · 0–7: material factual errors or misleading claims |
| 2 | No Harmful or Misleading Claims | 20 | No listing descriptions omitting known safety recalls/damage; no advice that could lead to unsafe repairs without a "consult a mechanic" disclaimer; no fear-based urgency pressure tactics | 20: none, appropriate disclaimers present · 14–19: 1 minor framing issue · 8–13: missing disclaimer or 1 meaningful omission · 0–7: harmful framing, missing disclaimer, or active misleading claims |
| 3 | Balanced & Complete Coverage | 15 | Known downsides/common issues for a model acknowledged, not just positives; buying-guide content addresses pros and cons; scope matches title's promise | 15: genuinely balanced · 10–14: 1 notable omission · 5–9: one-sided/significant gaps · 0–4: heavily one-sided/misleading scope |
| 4 | Disclaimer Present | 10 | "Consult a qualified mechanic" for technical/safety advice where warranted; affiliate/dealer relationship disclosed; used-vehicle "as-is" disclaimers where relevant; prominently placed | 10: clear, prominent · 6–9: present but buried/generic · 0–5: missing where clearly required |
| 5 | People-First Intent (Who/How/Why) | 20 | WHO: clear creator+qualification, firsthand experience. HOW: written for people not search engines, original analysis, avoids keyword-stuffed headings/padding/generic definitions. WHY: satisfying, clear purpose for existing on this site | 20: clear people-first, original, satisfying · 14–19: mostly helpful, 1–2 SEO-assembly tells · 8–13: mixed intent, some filler · 0–7: assembled for search, padded |
| 6 | Content Consensus Alignment | 15 | Technical claims align with manufacturer documentation and established enthusiast community consensus, not contradicted by known service bulletins/recalls | 15: fully aligned · 10–14: 1 minor outdated claim · 5–9: 1–2 claims deviate · 0–4: multiple violations/active misinformation |

**Tool/command:** apply manually, or via a content-quality skill if one is configured for this site.

---

## Part G — Site Structure & Monitoring

### G1. Sitemap Validation

| Test | What to check | Pass criteria | Severity |
|---|---|---|---|
| XML validity | Well-formed XML | No parse errors | — |
| URL count limit | `<url>` entries per file | <50,000 (protocol limit) | Critical if exceeded, single file |
| URL reachability | Every `<loc>` | Returns HTTP 200 | High if non-200 |
| `<lastmod>` accuracy | Dates across entries | Not all identical; a "bumped" forum thread or price-updated listing should show a genuinely fresh date | Low if identical |
| Deprecated tags | `<priority>`, `<changefreq>` | Google ignores these — flag as removable | Info |
| robots.txt reference | `Sitemap:` line | Declared | — |
| Crawl vs. sitemap coverage | Crawled pages vs. sitemap | No missing pages | — |
| Sitemap index needed | Count vs 50k | `<sitemapindex>` wrapper if exceeded | — |
| Content-type splitting | Single vs. split by type | Split by listings/threads/pages/images (quality signal) | — |
| Canonical-only inclusion | URLs vs canonical tags | No non-canonical URLs | — |
| Indexability | URLs vs `noindex` | No noindexed URLs (expired listings, thin profiles) | High if included |
| No redirects in sitemap | URLs vs 3xx targets | No redirected URLs | Medium if included |
| Protocol consistency | Scheme of every `<loc>` | HTTPS only | — |
| Location/category-page scale gate | Near-duplicate browse pages (by city, by facet combination) | ⚠️ Warning 30+ pages (must show 60%+ unique content) · 🛑 Hard stop 50+ pages (requires justification) | — |
| Sold/expired listing handling | Listings removed from active inventory | Removed from sitemap promptly; see Part M8 for page-level handling | High if stale listings remain in sitemap |

**Tool/command:** `/seo sitemap <url>`

### G2. Internal Link Audit

| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| Sitemap ingestion | Section URLs (listings, forum) | All matching URLs captured, indexes expanded recursively | crawl |
| Page-type classification | Every fetched page | Classified per page-type patterns (Part C3) | link audit |
| Link graph build | Internal structure | Full graph covering all in-scope pages | link audit |
| Forum↔listing bridge links | Model-specific threads missing a link to active listings for that model; listing pages missing a link back to relevant forum discussion/buying-guide threads | Present, severity HIGH if missing — this is the site's version of a cross-section bridge check | link audit |
| Page score | 0–100 per page | Healthy 80+ · Needs Attention 60–79 · Critical <40 | scoring model |
| Orphan detection | Incoming link count | 0 incoming = orphan | graph analysis |
| Anchor suggestion sourcing | Suggested anchor text | Extracted from real body copy — never invented | manual/tool |
| Incoming-mode output | Pages that should link to a target but don't | Top sources, each with insertion sentence + anchor + reason | manual/tool |
| Outgoing-mode output | What a source page should link to | Top targets | manual/tool |

**Tool/command:** `/seo interlinking <section>`

### G3. Broken-Link / 404 Sweep

| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| Codebase link scan | `<a href>`, framework `<Link>`, Markdown links, CSS `url()`, redirect configs | All enumerated | static scan/grep/AST |
| Route cross-reference | Internal link target vs defined routes | No undefined route targets | static mapping |
| Live crawl | Every internal link from homepage outward | Crawl completes, every link visited | site crawl |
| HTTP status per link | Code returned | 200 OK · 301/302 check chain · 404 broken · 410 intentional (e.g. removed listing) · 500 error · timeout unresponsive | HTTP status check |
| Redirect chain length | Hops to final destination | Flag 3+ hops | follow chain |
| External link resolution | Outbound links | Still resolve | HTTP check |
| Backlink 404s | External sites linking to your 404'd pages (e.g. an old listing or thread URL that moved) | Highest priority (lost link equity) — fix via 301 to the closest live equivalent | backlink cross-reference |

**Tool/command:** `/seo broken-links <url>`

### G4. SEO Drift / Baseline / Regression

**Elements snapshotted:** title, meta_description, canonical, meta_robots, h1/h2/h3, schema,
open_graph, CWV, HTTP status_code, HTML content hash, schema content hash.

| Test | What to check | Pass criteria | Tool/command |
|---|---|---|---|
| Comparison rule engine | Current vs. most recent baseline | Rule-based diff, 3 severity tiers | drift comparison tool |
| Severity classification | Each triggered rule | CRITICAL (respond immediately) · WARNING (within 1 week) · INFO (review at convenience) | — |
| URL normalization | URL used for baseline lookup | Lowercase scheme/host, strip default ports, sort query params, strip UTM, strip trailing slash | internal |
| CWV fetch failure | PageSpeed key missing/fails | Store `null`, skip CWV rules (not a hard failure) | — |
| Non-200 baseline | 4xx/5xx at baseline time | Still captured (status is a tracked field) | — |
| History retrieval | All baselines/comparisons for a URL | Newest-first, with timestamps | — |

**Cross-skill escalation:** schema removed/modified→Part C · CWV regression→Part A6 · title/meta
changed→Part B · canonical changed→Part A2 · noindex added→Part A1 · heading structure changed→
Part B · listing availability schema stale ("InStock" on a sold item)→Part M8.

**Tool/command:** `/seo drift [baseline|diff]` — run before + after every deploy.

---

## Part H — Google Data & Live SERP/Keyword Data

### H1. Credential Tiers (gate which pulls are possible)

| Tier | Requires | Unlocks |
|---|---|---|
| 0 | `api_key` | pagespeed, crux, crux-history, youtube, nlp |
| 1 | + OAuth/service account | + gsc, inspect, sitemaps, index |
| 2 | + `ga4_property_id` | + ga4, ga4-pages |
| 3 | + Ads dev token + customer ID | + keywords, volume |

### H2. PageSpeed / CrUX

| Test | Field/metric | Notes |
|---|---|---|
| Lighthouse + CrUX combined | Lab + 28-day field data | Mobile+desktop, all Lighthouse categories |
| CrUX 25-week history | LCP/INP/CLS/FCP/TTFB trend | Trend direction, % change, weekly p75 |
| CWV rating | LCP, INP, CLS | Good/Needs Improvement/Poor — see A6 for thresholds (<2.5s / <200ms / <0.1) |
| Metric encoding gotcha | CLS value type | Some APIs return CLS as a **string** — parse, don't assume numeric |
| FID deprecation | Any INP/FID reference | Replaced Mar 12 2024 — never reference FID |
| CrUX no-data case | 404 from CrUX | = insufficient Chrome traffic, not an auth error — fall back to PSI lab data |

### H3. Search Console

Search Analytics (clicks, impressions, CTR, position — default last 28 days, data lags 2–3 days) ·
quick-win detection (queries at position 4–10 with high impressions) · URL Inspection (indexation
verdict, coverage state, robots.txt status, canonical selection, mobile usability, rich results) ·
batch inspection (rate-limited 2,000/day/site) · sitemap status (errors/warnings per sitemap) ·
Indexing API (officially restricted to JobPosting/BroadcastEvent/VideoObject page types — disclose
this restriction; quota 200/day — relevant if events/meetups are posted as JobPosting-adjacent
listings, otherwise this API doesn't apply to ordinary listing/thread pages).

### H4. GA4

Organic traffic report (sessions, users, pageviews, bounce, engagement — default 28 days, Organic
Search filter) · top organic landing pages (sessions-ranked, same filter).

### H5. Rate Limits (hard ceilings during testing)

| API | Per-minute | Per-day |
|---|---|---|
| PSI v5 | 240 QPM | 25,000 QPD |
| CrUX + History (shared) | 150 QPM | Unlimited |
| GSC Search Analytics | 1,200 QPM/site | 30M QPD |
| GSC URL Inspection | 600 QPM | 2,000 QPD/site |
| Indexing API | 380 RPM | 200 publish/day |
| GA4 Data API | 10 concurrent | ~25K tokens/day |

**Tool/command:** `/seo google <query>`

### H6. DataForSEO Live Data

**Cost gate (mandatory before every call):** cost estimation → `approved`/`needs_approval` (show
estimate, get confirmation)/`blocked` (stop) → log actual cost after each call.

**SERP data:** Google/Bing/Yahoo organic, Google Images, YouTube search + video deep analysis.

**Keyword data:** ideas/suggestions/related, search volume, difficulty (0–100), search intent,
trends.

**Domain/backlink/competitor:** backlink profile, competitor domains, ranked keywords,
keyword/backlink intersection, traffic estimation, subdomains, top searches mentioning domain.

**On-page/technical/content:** on-page instant+Lighthouse, tech stack, WHOIS, content analysis
(quality/sentiment/readability), business listings.

**AI visibility/GEO:** AI-chat-scraper checks, LLM mention tracking (cross-model comparison).

**Tool/command:** `/seo dataforseo <query>`

---

## Part I — Local SEO, GBP & Maps

**Applicability:** this part matters if the site has physical dealer/shop partners, hosts a
directory of local sellers/mechanics, or supports city/region-based browsing. If it's a purely
online, nationwide marketplace with no physical presence, skip I2–I3 and I8 (GBP/review/geo-grid
specific) and keep only the location-based browse-page guidance in I4.

### I1. Business-Type Detection (gating logic)

| Test | What to check | Pass criteria |
|---|---|---|
| Business type | Physical address, Maps embed, "visit us" vs "we ship to you" language | Brick-and-mortar / online-only / hybrid correctly classified before scoring |
| Vertical-specific schema pattern | Dealer/shop pages vs pure marketplace | Routes to the matching local-schema pattern |

### I2. GBP Signals (25% weight, if applicable)

Primary/secondary category accuracy · GBP posts · photos/video · Q&A content (recreate as on-site
FAQ, since native GBP Q&A has limited longevity) · GBP link strategy (should not point to the
site's single strongest organic page, to avoid suppressing organic rankings) · business-hours
visibility.

### I3. Reviews & Reputation (20% weight, if applicable)

Review count (≥10 is a commonly-cited threshold) · star rating (≥4.5 ideal, ≥4.0 minimum) · review
recency (within last 3 months) · review velocity (no long unexplained gaps) · aggregateRating
schema completeness · owner response rate · **review gating (pre-screening before directing to a
review platform) is prohibited — flag as FAIL if detected.**

### I4. Local On-Page SEO (20% weight)

Title/H1 with city+category keyword · NAP visibility (for dealer/shop pages) · dedicated
category/location browse pages · location-page uniqueness (≥60–70% unique content vs. template) ·
**doorway-page "swap test"**: swap the city name in a location page's content — does it still make
sense generically? Fail if swappable. · embedded map (lazy-loaded) for shop pages · click-to-call
for dealer pages · internal linking depth (≤3 clicks) · URL structure
(`domain.com/listings/city-name/` pattern for location browsing) · multi-location scale gate: ⚠️
30+ location pages, 🛑 hard stop 50+.

### I5. NAP Consistency & Citations (15% weight, if applicable)

NAP cross-source match (HTML vs schema vs GBP) · directory presence (Yelp/BBB/Facebook-equivalent
for the relevant market) · Apple Business Connect / Bing Places claimed.

### I6. Local Schema Markup (10% weight, if applicable)

LocalBusiness presence with required (`name`, `address`) and recommended (`geo`,
`openingHoursSpecification`, `telephone`, `priceRange`, `aggregateRating`) properties · correct
industry subtype (e.g. `AutoDealer`, not the deprecated `VehicleListing`) · multi-location `branchOf`
linkage with unique `@id` per location.

### I7. Local Link & Authority Signals (10% weight)

Local press mentions · community involvement (sponsoring rides/meetups) · "best of" list presence ·
link velocity.

### I8. Maps Intelligence (if applicable)

Geo-grid rank tracking (grid + radius, cost-confirmed before scan) · Share of Local Voice =
`(top_3_count / total_points) × 100` · GBP profile field-by-field audit · review intelligence
(velocity, rating distribution, fake-review pattern detection: 2+ of uniform timing, low-history
reviewer accounts, geographic inconsistency, sudden 5-star-only spike, near-identical text) ·
competitor radius mapping · cross-platform NAP verification (Google/Bing/Apple/OSM) ·
**never generate self-serving review markup** — only mark up genuine third-party reviews visible
on the page.

**Tool/command:** `/seo local <business>` · `/seo maps <area>`

---

## Part J — Backlinks

### J1. Profile Overview

| Test | Good | Warning | Critical |
|---|---|---|---|
| Referring domains | >100 | 20–100 | <20 |
| Follow ratio | >60% | 40–60% | <40% |
| Domain diversity (max % from single domain) | No domain >5% | 1 domain >10% | 1 domain >25% |
| Link trend | Growing/stable | Slow decline | Rapid decline >20%/quarter |

### J2. Anchor Text Distribution

| Anchor type | Target range | Over-optimization signal |
|---|---|---|
| Branded | 30–50% | <15% (too low = red flag) |
| URL/naked link | 15–25% | — |
| Generic ("click here") | 10–20% | — |
| Exact match keyword | 3–10% | >15% (Penguin risk) |
| Partial match keyword | 5–15% | >25% |
| Long-tail/natural | 5–15% | — |

### J3–J5. Domain Quality, Toxic Links, Competitor Gap

TLD/country/domain-rank distribution of referring domains · toxic-link patterns (PBN domains,
unnatural single-domain anchor concentration, mass directory submissions, link farms, paid-link
patterns) · Spam Score >11% (Moz scale) = high risk · link magnets (highest-authority pages) ·
zero-backlink pages (internal-linking opportunity) · 404s with backlinks (redirect opportunity —
often an old listing or thread that moved) · competitor-only/shared/target-only domain gap
analysis · link velocity 30/60/90-day trend.

### J6. Backlink Health Score (weighted composite)

| Factor | Weight |
|---|---|
| Referring domain count | 20% |
| Domain quality distribution | 20% |
| Anchor text naturalness | 15% |
| Toxic link ratio | 20% |
| Link velocity trend | 10% |
| Follow/nofollow ratio | 5% |
| Geographic relevance | 10% |

**Data sufficiency gate:** 4+/7 factors scored → numeric 0–100. Fewer than 4 → must display
"INSUFFICIENT DATA (X/7 factors scored)," never a numeric score.

**Tool/command:** `/seo backlinks <domain>`

---

## Part K — Images

Especially important here: buyer trust in a listing hinges heavily on photo quality/completeness,
and forum posts often carry user-uploaded attachments.

| Test | What to check | Pass criteria |
|---|---|---|
| Alt text presence | All `<img>` except decorative | Present |
| Alt text descriptiveness | Content described, not filename/generic | Fail: "image.jpg", "photo1" |
| Alt text length | Character count | 10–125 characters |
| File size — listing photos | Target/Warning/Critical | <150KB / >300KB / >700KB |
| File size — thumbnails/avatars | Target/Warning/Critical | <50KB / >100KB / >200KB |
| Format | WebP/AVIF vs JPEG/PNG | WebP/AVIF preferred |
| Responsive `srcset`/`sizes` | Size variants + breakpoint matching | Present and accurate |
| Below-fold lazy load | `loading="lazy"` | Present on below-fold images (listing gallery thumbnails, forum attachments) |
| Above-fold/hero exemption | Primary listing photo lazy-loaded? | Must NOT be — harms LCP |
| CLS prevention | `width`/`height` attrs (or CSS `aspect-ratio`) | Present on all `<img>` |
| Filename descriptiveness | Hyphenated, lowercase vs `IMG_1234.jpg` | Descriptive |
| Minimum photo count (listings) | Number of images per listing | ≥4 recommended for buyer trust (see Part M) |
| CDN usage | Separate domain, caching headers | Present for image-heavy sites |

**Ranking-impact reference:** Alt text = CRITICAL · Filename = HIGH · Page context = HIGH ·
File size/speed = MEDIUM (indirect, via CWV) · EXIF/IPTC metadata = LOW/NONE (display only, Google
ignores IPTC keywords).

**Tool/command:** `/seo images <url>` · AI asset generation: `/seo image-gen <what>`

---

## Part L — Hreflang / International SEO

**Applicability:** relevant if the forum/marketplace operates in multiple languages or regions.
Skip entirely for a single-language, single-market site.

### L1. Core Validation Rules

Self-referencing hreflang tag on every page · return tags (bidirectional A↔B) · exactly one
x-default per set, pointing to a fallback/selector page · valid ISO 639-1 language codes and ISO
3166-1 Alpha-2 region codes · hreflang only on canonical URLs, matching exactly · protocol
consistency (all HTTPS) · cross-domain support with GSC verification on both domains if applicable.

### L2. Common Mistakes (severity)

| Issue | Severity |
|---|---|
| Missing self-referencing tag | Critical |
| Missing return tags | Critical |
| Missing x-default | High |
| Invalid language/region code | High |
| Hreflang on non-canonical URL | High |
| HTTP/HTTPS mismatch | Medium |
| Trailing slash inconsistency | Medium |
| Hreflang in both HTML and sitemap | Low |

### L3–L4. URL Structure & Implementation Method

Subdirectories (`/fr/`, `/es/`) recommended for most sites over subdomains or ccTLDs. Implementation
method: HTML link tags for <50 variants/page, HTTP headers for non-HTML assets, XML sitemap for
large/cross-domain sites (split at 50,000 URLs/file).

### L5. Cultural Adaptation & Content Parity

Locale-appropriate CTA style, trust signals, and number/date/currency formatting · content parity:
page-existence coverage, structural equivalence, localized (not copy-pasted) SEO elements,
word-count ratio by language pair, freshness tracking per translation.

**Tool/command:** `/seo hreflang <url>`

---

## Part M — Vehicle Listing & Marketplace Schema

### M1. Listing Page On-Page Checklist

| Test | Pass criteria |
|---|---|
| Title | Year + make + model + trim + price signal, under 60 characters |
| Meta description | Key specs + price + CTA, under 155 characters |
| H1 | Unique per listing, matches title |
| H2 structure | Specifications / Condition / Seller Info / Similar Listings |
| Images | ≥4 photos (front, side, rear, odometer); VIN-plate photo recommended for motorized listings as a fraud-prevention signal |
| Breadcrumb | Home > Category > Make > Model > Listing |
| Related/similar listings section | Present |
| Seller-profile link | Present |
| Description uniqueness | Not copy-pasted from a manufacturer brochure or another listing |
| Specs table | Structured (not prose-only) |
| Condition disclosure | Clear, specific (not just "good condition") |

### M2. Listing Page Scoring Weights

| Category | Weight |
|---|---|
| Schema completeness | 25% |
| Title & meta | 15% |
| Image optimization | 20% |
| Content quality | 20% |
| Internal linking | 10% |
| Technical (speed, mobile, canonical) | 10% |

### M3. Cross-Platform Listing Syndication

If listings are also fed to other marketplaces or a Shopping-style feed: pricing/positioning
consistency across platforms, duplicate-content/canonical risk from syndicated copies, and (if
using a paid data API) the same cost-approval gate as Part H6 before pulling comparison data.

### M4. Cross-Platform Price Benchmarking

Compare this site's average price, median condition/mileage, and typical time-to-sale against
comparable listings on other marketplaces for the same model — useful both for seller guidance
content and for competitive positioning.

### M5. Marketplace Keyword Gap

Pull the domain's ranked keywords → check whether comparable listings/models have organic content
coverage → bucket: Organic-Only (build a dedicated model hub page) · Content-Only-No-Listings (low
priority unless genuinely high search volume) · Both Present (optimize price/spec consistency +
schema) · Neither (low priority).

### M6. Vehicle Schema Requirements

**Required (Product pattern, universal across motorized + pedal):** `@type: Product`, `name`,
`image`, `description`, `brand` (Brand/Organization object), `offers` (Offer: `url`,
`priceCurrency`, `price`, `availability`, `seller`).

**Motorized-vehicle-specific additional properties** (layer onto the Product pattern —
schema.org's dedicated `Vehicle` type exists but Google's Product rich-result validator doesn't
recognize its properties, so express them via `additionalProperty` as shown in Part C7, or use
`Vehicle` directly if entity/GEO value matters more than rich-result eligibility for this page):
`vehicleIdentificationNumber` (VIN), `mileageFromOdometer` (with `unitCode`), `productionDate`
(model year), `fuelType`, `vehicleEngine`/engine displacement, `vehicleTransmission`, `bodyType`,
`color`, prior-owner count if known.

**Pedal-bicycle-specific (lighter Product-only pattern):** no motor properties; use
`additionalProperty` for frame size, wheel size, groupset/component tier.

| Validation rule | Pass criteria |
|---|---|
| `price` format | Number string, e.g. `"2999.00"` — NOT `"$2,999"` |
| `availability` format | Full Schema.org URL enum (`https://schema.org/InStock`, etc.) — **must reflect actual listing status** |
| `image` format | Array, ≥1 high-resolution URL — recommend ≥4 for a vehicle listing (see M1) |
| `priceCurrency` | Valid ISO 4217 code |
| `brand.name` | Not empty, not `"N/A"` |
| VIN format (motorized only) | 17-character alphanumeric, excludes I/O/Q — basic format check, not a full VIN-decode validation |
| `mileageFromOdometer` | Numeric value + `unitCode` present (e.g. `SMI` for miles, `KMT` for kilometers) |
| `aggregateRating` completeness | If present, `ratingValue` AND `reviewCount` both required |

### M7. Listing Schema Completeness Scoring

| Level | Score |
|---|---|
| Required fields only | 50/100 |
| + ≥4 images | 65/100 |
| + VIN/mileage/engine specs (motorized) or frame/wheel/groupset specs (pedal) | 75/100 |
| + verified-seller badge | 85/100 |
| + return/inspection-period policy documented | 90/100 |
| + genuine reviews of the seller (3+) | 100/100 |

### M8. Listing Lifecycle & Status Handling

| Test | What to check | Pass criteria |
|---|---|---|
| Active listing | `availability: InStock`, page indexable | Matches real inventory state |
| Sold listing | Schema availability updated to `OutOfStock`/`Discontinued`, or page returns 410, or redirects to a closely-related active listing/category | **A sold listing still marked `InStock` is a common, damaging bug** — flag as Critical |
| Expired/removed listing | Removed from sitemap promptly | No stale listing URLs lingering in the sitemap |
| Relisted/duplicate detection | Same VIN or same seller+model reposted repeatedly | Flag for review — can be legitimate (price drop repost) or a spam/scam pattern |
| JS-rendered availability | Status set via client-side JS only | Must be server-rendered — see Part A8 | 

### M9. Category & Taxonomy Pages

Browse-by-make/model/year/price-range/location pages: `CollectionPage`+`ItemList`, never `Product`
schema on the list page itself. Apply the same thin-content scale gate as Part G1/I4 to
facet-combination pages (e.g. make × year × price-band): warn at high combination counts, hard-stop
indexing near-empty facet pages. Canonicalize or noindex sort/filter parameter combinations that
don't represent meaningfully different content from the unfiltered view.

**Tool/command:** `/seo ecommerce <url>` for the generic product-schema mechanics — Vehicle-specific
properties (M6–M9) should be checked manually alongside it.

---

## Part N — Forum SEO & UGC Management

### N1. Forum Thread Schema & Structure

| Test | What to check | Pass criteria |
|---|---|---|
| Root post schema | `DiscussionForumPosting` on the thread page | Present, with `author`→Person |
| Reply schema | `Comment` entities for replies | Present where the platform supports it |
| Engagement signals | `interactionStatistic` for reply/view counts | Present where available |
| QAPage narrow use | Only for genuine single-question/single-best-answer threads | Not applied to open-ended discussion threads |
| Breadcrumb | Forum > Subforum > Thread | Present |
| Author profile link | `author`→Person, linked to a ProfilePage | Only if that profile carries genuine public content (see N3) |

### N2. Thread Content Quality & Thin/Duplicate Content

| Test | What to check | Pass criteria |
|---|---|---|
| Minimum viable thread | No replies + a low-effort single-line post | Flag as thin-content candidate for noindex until real discussion accumulates |
| Duplicate/cross-posted threads | Same question posted in multiple subforums | Canonicalize to the original, or merge |
| Locked/dead threads | Closed threads with substantive Q&A content | Keep indexed — don't blanket-noindex closed threads just because they're closed |
| Spam/moderation-flagged posts | Posts removed or flagged by moderation | Must not remain indexed |
| AI-spam UGC | Bulk-posted, low-effort, or bot-generated replies | Flag for moderation review — contributes to site-wide Helpful Content risk (Part F4) if left unchecked at scale |

### N3. Forum Technical SEO

| Test | What to check | Pass criteria |
|---|---|---|
| Pagination | Long threads split across pages | Self-referencing canonical per page (not all pages canonicalized to page 1); a "view all" page is reasonable for shorter threads only |
| Sort/filter/search parameters | `?sort=newest`, `?page=`, `?view=` combinations | Canonicalize or noindex parameter combinations that don't represent unique content |
| User profile pages | Public profile URLs | Noindex thin profiles (no posts, no bio); index only profiles with genuine public content (post history, bio, verified-seller status) |
| Reply/quote fragments | `#post-123`-style URL fragments | Must not be treated as separately indexable pages |
| Lastmod accuracy | Sitemap dates for bumped threads | A thread bumped by a genuinely new reply should show an updated `lastmod` — a thread bumped by spam should not |

### N4. Forum ↔ Listing Cross-Linking

Ties directly to Part G2's bridge-link check: model-specific threads should link to active listings
for that model, and listing pages should link back to relevant forum discussion/buying-guide
threads. Brand/model hub pages (Part C3, #9) that aggregate both are a strong internal-linking and
GEO fan-out play (Part D1, Parameter 10).

### N5. Forum Content as a GEO/AI-Citation Asset

Forum threads often directly answer long-tail conversational questions ("why does my [model] make
a knocking noise at idle") — a strong natural fit for GEO Parameter 4 (Conversational Q&A Coverage)
and passage-level citability (Part D2). Consider surfacing the single best answer from a long
thread as a distinct, highlighted, citable passage rather than relying on AI engines to parse an
entire multi-page thread.

### N6. Trust & Safety Signals (SEO-relevant)

| Test | What to check | Pass criteria |
|---|---|---|
| Verified-seller/verified-listing badges | Displayed where genuine | Never fabricate an aggregateRating to simulate this |
| Scam-listing reporting flow | Visible, functional reporting mechanism | Present — contributes to Trustworthiness (Part F1) |
| Moderation policy/community guidelines page | Publicly accessible | Present — contributes to Authoritativeness (Part F1) for the forum as a whole |

*Known gap:* this workspace's underlying skills don't include a dedicated forum/UGC-specific
subagent, so Part N is authored/adapted guidance rather than a 1:1 mapping to an existing skill —
apply it manually or use it as a spec if building a custom check.

---

## Part O — Full-Site Audit Methodology & Health Score

### O1. Crawl Configuration

| Parameter | Value |
|---|---|
| Max pages crawled | 500 |
| Respect robots.txt | Yes |
| Follow redirects | Yes, max 3 hops |
| Timeout per page | 30 seconds |
| Concurrent requests | 5 |
| Delay between requests | 1 second |

### O2. Specialist Coverage (conditionally spawned by business-type detection)

**Always relevant:** technical (Part A) · content quality (Parts B1/F) · schema (Part C) ·
sitemap (Part G1) · performance/CWV (Part A6) · visual/mobile (screenshots, above-fold) · GEO
(Part D2) · SXO (Part E2 — recommended for every full audit).

**Conditionally relevant:** local/GBP (Part I, if physical presence detected) · maps (Part I8, if
local + geo-data available) · Google data (Part H, if credentials available) · backlinks (Part J,
if backlink-data credentials available) · drift (Part G4, if a baseline exists) · vehicle-listing
schema (Part M, if listing pages detected) · forum/UGC (Part N, if forum pages detected — **no
existing skill spawns this automatically; add it as a manual step**).

### O3. Health Score Weights

| Category | Weight |
|---|---|
| Technical SEO | 22% |
| Content Quality | 23% |
| On-Page SEO | 20% |
| Schema/Structured Data | 10% |
| Performance (CWV) | 10% |
| AI Search Readiness | 10% |
| Images | 5% |

### O4. Report Structure

1. Executive Summary — Overall Score /100, business type detected, top-5 critical issues, top-5
   quick wins
2. Technical SEO — crawlability, indexability, security, CWV status
3. Content Quality — E-E-A-T, thin/duplicate content, readability
4. On-Page SEO — title/meta issues, heading structure, internal linking gaps
5. Schema & Structured Data — implementation, validation errors, missing opportunities
6. Performance — LCP/INP/CLS, resource optimization, third-party script impact
7. Images — missing alt text, oversized images, format recommendations
8. AI Search Readiness — citability score, structural improvements, authority signals
9. Vehicle Listing Health — schema completeness, sold-listing hygiene, category-page bloat
10. Forum Health — thin/duplicate threads, thread-schema coverage, forum↔listing linkage

### O5. Error Handling (condensed)

| Scenario | Action |
|---|---|
| URL unreachable/DNS failure | Report connection error + status code; never guess content |
| robots.txt not found | Note absence, recommend creating one, continue on remaining categories |
| robots.txt blocks crawling | Report blocked paths, analyze only accessible pages |
| HTTPS not configured | Flag Critical: HTTP-without-redirect, mixed content, missing/expired SSL |
| CWV data unavailable | Note CrUX unavailable (common for low-traffic sites); use Lighthouse lab data as proxy |
| Page requires auth (401/403) | Report auth-gated; ask for rendered HTML or public URL |
| JS-rendered empty body | Note possible CSR; analyze available HTML; flag possible incompleteness |
| No schema markup found | Report none detected; recommend types based on content |
| Invalid JSON-LD syntax | Parse + report specific error; provide corrected JSON-LD |
| Rate limiting/429 | Back off, reduce concurrency, report partial results |
| Timeout on 500+ page sites | Cap at timeout limit; report crawled findings; estimate total scope |

**Tool/command:** `/seo audit <url>`

---

## Appendix — Skill/Command Quick Reference

```
/seo audit <url>                    # full-site audit, up to 500 pages, health score
/seo technical <url>                # Part A — 9-category technical audit
/seo page <url>                     # Part B2 — single-page on-page/technical/schema/images
/seo schema <url>                   # Part C — detect/validate/generate JSON-LD
/seo sitemap <url>                  # Part G1
/seo interlinking <section>         # Part G2
/seo backlinks <domain>             # Part J
/seo broken-links <url>             # Part G3
/seo local <business>               # Part I2-I7
/seo maps <area>                    # Part I8
/seo drift [baseline|diff]          # Part G4 — run before + after every deploy
/seo images <url>                   # Part K
/seo image-gen <what>                # AI asset generation for SEO
/seo google <query>                 # Part H2-H5 — GSC/PSI/CrUX/GA4
/seo dataforseo <query>             # Part H6 — live SERP/keyword/backlink data
/seo ecommerce <url>                # Part M — generic product-schema mechanics
/seo hreflang <url>                 # Part L

/content audit <url or file>        # Parts B1 + D1 + F1-F4, if a comparable skill is configured
/ai-search <topic>                  # Part E1 — AI-citation scraping, if configured
/ai-search geo <url>                 # Part D2 — technical/platform GEO factors, if configured
/ai-search sxo <keyword>              # Part E2 — intent-mismatch diagnosis, if configured
```

**Parts M and N (vehicle-listing schema, forum SEO) have no dedicated end-to-end skill/command in
this workspace** — they're authored specifically for this vertical. Use `/seo schema <url>` for the
generic validation mechanics (Part C1–C2) and `/seo ecommerce <url>` for generic product-schema
plumbing, then apply Part M's vehicle-specific properties and Part N's forum-specific checks
manually against the results.

---

*Adapted from a PolicyBazaar-UAE-insurance version of this checklist, generalized and refocused for
a motorcycle/bike forum + marketplace. Parts M and N are original synthesis for this vertical, not
pulled from an existing skill file — validate their specifics against your own data before treating
them as settled thresholds.*
