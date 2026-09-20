# Pickyourtrail Bali — Technical & On-Page SEO Recovery Plan

**Pages in scope**
1. `https://pickyourtrail.com/packages/bali` — targets *Bali Package*, *Bali Tour Packages*
2. `https://pickyourtrail.com/packages/bali/honeymoon-tour-packages` — targets *Bali Honeymoon Package*, *Bali Honeymoon Tour Packages*, *Bali packages for couples*

**Audit date:** 30 July 2026
**Method:** live crawl of both pages (raw HTML + rendered DOM), Lighthouse mobile navigation audit, Chrome performance trace with CrUX field data, robots.txt and XML sitemap inspection, JSON-LD parsing, and head-element comparison against 12 named competitor URLs.

---

## 0. What is verified and what is not

Everything in this document was pulled from the live pages on 30 July 2026. Nothing is estimated. Where a source could not be reached, it is marked as such and no substitute figure has been invented.

| Source | Status |
|---|---|
| Both Pickyourtrail pages (HTML, DOM, schema, CWV) | Retrieved and measured |
| EaseMyTrip, Thomas Cook, SOTC, DPauls (Bali packages) | Retrieved |
| GT Holidays, DPauls, SOTC, Flamingo (Bali honeymoon) | Retrieved |
| **MakeMyTrip** (both URLs) | **Not retrieved.** Bot protection returned no response on curl and timed out twice on fetch. No MMT data appears below. |
| **Yatra** (both URLs) | **Not retrieved.** Same reason. |

MakeMyTrip and Yatra are the two largest competitors in this set. Their pages need to be reviewed manually in a browser before this plan is presented as complete. Every other competitive claim below is backed by a retrieved page.

One Lighthouse warning has been deliberately excluded: the "mixed content" errors resolve to `auth.iws-hybrid.trendmicro.com`, which is a network security proxy on the audit machine intercepting third-party pixels. That is a local artefact, not a site defect. It should not be reported to the client.

---

## 1. Reading the GSC data

### Bali main page

| Month | Clicks | Impressions | CTR | Avg. position |
|---|---|---|---|---|
| January | 994 | 198,000 | 0.50% | 5.4 |
| February | 691 | 147,000 | 0.50% | 5.1 |
| March | 640 | 171,000 | 0.40% | **4.5 (peak)** |
| April | 638 | 148,000 | 0.40% | 6.2 |
| May | 753 | 126,000 | 0.60% | 9.1 |
| June | 450 | 68,800 | 0.70% | 11.0 |
| July | 390 | 49,500 | 0.80% | 12.7 |

### Bali honeymoon page

| Month | Clicks | Impressions | CTR | Avg. position |
|---|---|---|---|---|
| January | 181 | 43,700 | 0.40% | 7.7 |
| February | 146 | 33,600 | 0.40% | 4.5 |
| March | 114 | 33,800 | 0.30% | **3.9 (peak)** |
| April | 95 | 19,200 | 0.50% | 6.7 |
| May | 125 | 13,300 | 0.90% | 14.0 |
| June | 75 | 8,530 | 0.90% | 15.7 |
| July | 42 | 7,030 | 0.60% | 20.9 |

### Three things this data says

**Both pages peaked in March and have fallen every month since.** Main page 4.5 to 12.7 over four months. Honeymoon page 3.9 to 20.9 over the same four months. Two different pages breaking in the same month, then declining monotonically together, is not a content-decay pattern. Content decays unevenly. A synchronised break across a URL cluster points to a site-level cause: an algorithmic update, a template or platform change shipped around late March or April, or coordinated competitor displacement. Identifying which of these it was is the highest-value first task, and it is answered by data, not by opinion (see Phase 0 below).

**The CTR is anomalously low and that matters more than the decline.** At an average position of 4.5 in March, the main page recorded 0.40% CTR. A position-4 to position-5 result on a commercial query would ordinarily be expected in the mid single digits. Recording roughly ten times below that means the reported average position is not describing the queries that generate the impressions. In practice this almost always means the impression base is dominated by broad or peripheral queries where the page surfaces deep, while a small number of low-volume queries rank well and pull the average up. Do not plan against the blended average position. It is describing a different query set than the one being optimised for.

**Rising CTR during a ranking collapse confirms the above.** CTR climbed from 0.40% to 0.80% on the main page while position fell from 4.5 to 12.7. Rankings and CTR moving in opposite directions means the page shed a large volume of low-relevance impressions faster than it shed clicks. The remaining traffic is more qualified. The commercial core is intact; the broad visibility footprint is what collapsed.

### The missing number

There is no year-over-year comparison in this dataset. Indian outbound demand for Bali is seasonal, and a January to July decline partly reflects that. Without July 2025 against July 2026, the seasonal component cannot be separated from the genuine ranking loss. **Pull 13 months of GSC data before any target is committed to.** A PIP target built on a January baseline that includes peak season is a target set up to fail.

What is not seasonal, and cannot be explained away: average position 4.5 to 12.7. Seasonality moves volume. It does not move a page eight positions down the SERP.

---

## 2. Technical findings

### 2.1 Core Web Vitals are failing on real users (Priority: Critical)

CrUX field data, p75, for `/packages/bali`:

| Metric | Field value | Threshold | Status |
|---|---|---|---|
| LCP | 1,990 ms | < 2,500 ms | Pass |
| INP | 174 ms | < 200 ms | Pass, marginal |
| **CLS** | **0.34** | **< 0.10** | **Fail, 3.4x over** |
| TTFB | 1,092 ms | < 800 ms | Fail |

Lab CLS on a clean load measured 0.00. Field CLS is 0.34. That gap is the finding. A defect that does not reproduce in a clean lab load but hits real users at p75 is caused by something that only appears in real sessions: late-loading personalisation, A/B test variants, consent widgets, or images that arrive without reserved space over a real network.

The cause is measurable and specific:

| Page | Total `<img>` | Images with no `width`/`height` |
|---|---|---|
| `/packages/bali` | 213 | **124** |
| `/packages/bali/honeymoon-tour-packages` | 231 | **145** |

An image without intrinsic dimensions reserves no layout space. When it loads, everything below it moves. With 124 such images on a 17,291px page, CLS of 0.34 is the expected outcome.

**Fix:** set explicit `width` and `height` (or a CSS `aspect-ratio`) on every image in the package card component and the content blocks. This is a component-level change, not 124 individual edits. It is the single highest-leverage technical fix available and it addresses a confirmed failing Core Web Vital.

The honeymoon page has **no URL-level CrUX data at all**, which means it does not meet the traffic threshold to qualify. It carries the same defect at higher density.

### 2.2 React hydration failures (Priority: Critical)

The browser console logs, on every load:

```
Minified React error #418  (hydration mismatch: server HTML does not match client render)
Minified React error #423  (error while hydrating, switched to client rendering)
```

Error #423 means React abandoned the server-rendered HTML for at least one boundary and re-rendered it on the client. Google renders pages with its own headless Chrome, so whatever content sits inside a failed boundary is at risk of being indexed in its client-rendered state rather than the server-rendered state, or of not being indexed at all if rendering is deferred or budgeted.

Two pages losing rank simultaneously from March onward, on a React application throwing hydration errors, is a correlation worth taking seriously. This is the first thing to hand to engineering.

**Fix:** identify which components throw #418 and #423 using a development build, then correct the server and client render mismatch. Common causes are date or currency formatting that differs between server and browser locale, `Math.random()` or `Date.now()` in render, and browser-only checks such as `window` guards.

**Verification:** Search Console URL Inspection, "View crawled page" and "Screenshot", on both URLs. Compare Google's rendered output against the server HTML. If package cards, pricing, or body copy are missing from Google's render, this moves from critical to emergency.

### 2.3 Page weight and DOM size (Priority: High)

| Measure | `/packages/bali` | `/honeymoon-tour-packages` |
|---|---|---|
| Raw HTML, uncompressed | 1.48 MB | 2.09 MB |
| Raw HTML, gzipped | 143 KB | not measured |
| DOM elements | 6,749 | 6,477 |
| Rendered page height | 17,291 px | 16,914 px |
| `<img>` tags | 213 | 231 |
| Images loading eagerly | **119** | **141** |

Google's guidance for DOM size is under roughly 1,500 elements. Both pages are more than four times that. Lighthouse recorded style recalculation events affecting 3,735 elements and taking 105 ms.

Third-party transfer on the main page, measured in the trace:

| Third party | Transfer |
|---|---|
| **gumlet.io (image CDN)** | **5.4 MB** |
| tempera.ai | 523 KB |
| Google/Doubleclick, Quora, Clarity, PostHog, GA, Heap | under 15 KB each |

5.4 MB of images on a single page view is the dominant cost. 119 of 213 images load eagerly rather than lazily, so a large share of that downloads before the user has scrolled anywhere near it.

**Fixes, in order of return:**
1. Set `loading="lazy"` on every image below the first viewport. Only the LCP hero should be eager.
2. Serve AVIF or WebP through Gumlet with responsive `srcset` and correct `sizes`. Gumlet supports this through URL parameters, so it is a template change.
3. Paginate or lazily mount the package listing. 28 cards fully rendered at page load is the main driver of both DOM size and image count.

### 2.4 HTML is served with no-store (Priority: High)

```
cache-control: private, no-cache, no-store, max-age=0, must-revalidate
```

This is on a public, anonymous, indexable landing page. It forbids all caching, including at the CDN edge. TTFB of 1,092 ms in field data is consistent with that. The Chrome trace flagged 418 KB of wasted bytes attributable to cache policy.

**Fix:** serve public landing pages with a short shared cache and stale-while-revalidate, for example `public, max-age=0, s-maxage=300, stale-while-revalidate=86400`. Keep `private, no-store` for authenticated routes only. This is likely a single misapplied global header rule, and it is a small change with a direct TTFB benefit.

### 2.5 Brotli is not enabled (Priority: Medium)

Requesting the page with `Accept-Encoding: br` alone returns 1,481,607 bytes uncompressed. Only gzip is served. On documents this size, Brotli typically saves 15 to 25% over gzip. Enable `br` at the CloudFront and nginx layer.

### 2.6 Uncrawlable links (Priority: Medium)

This is the only failure in the Lighthouse SEO category, which otherwise scores 92.

| Page | `<a>` elements with no `href` |
|---|---|
| `/packages/bali` | 32 |
| `/honeymoon-tour-packages` | 30 |

Anchors without `href` are not followed and pass no link equity. On pages carrying 352 and 363 internal links respectively, 30-plus dead anchors is meaningful leakage inside the Bali cluster.

**Fix:** every navigational element must be a real `<a href="...">`. Reserve `<button>` for actions that are genuinely not navigation.

### 2.7 Sitemap lastmod is bulk-stamped (Priority: Medium)

All 38 Bali URLs in `sitemap/packages.xml` carry `lastmod` values within seconds of one another:

```
/packages/bali/tour-packages-from-ahmedabad    2026-07-28T02:01:53+05:30
/packages/bali/tour-packages-from-bengaluru    2026-07-28T02:01:53+05:30
/packages/bali/tour-packages-from-chennai      2026-07-28T02:01:53+05:30
/packages/bali/tour-packages-from-delhi        2026-07-28T02:01:53+05:30
... 34 more, all 2026-07-28T02:01:5x
```

Every page in the cluster did not change at 02:01 on the same night. This is an automated rebuild timestamp. Google detects and discounts bulk-stamped lastmod, which means genuine updates get no crawl priority.

**Fix:** stamp `lastmod` from actual content modification time. If that is not available, remove the field. An absent lastmod is treated better than a lastmod that is provably unreliable.

### 2.8 The `/guides/` block (Priority: Investigate)

`robots.txt` contains:

```
Disallow: /guides/
Disallow: /guides/*
```

`https://pickyourtrail.com/guides` returns HTTP 200 and `/guides/bali` returns a 301. An entire content directory is blocked from crawling. If destination guide content lives there, it can pass no internal link equity or topical support to the Bali package pages, and it cannot rank.

This needs a decision, not an assumption. Establish what is in `/guides/`, whether it is indexed, and whether the block is deliberate. If the content is worth having, unblock it and link it to the package pages. If it is not, that is fine, but it should be a decision rather than an inherited rule.

### 2.9 Accessibility and markup issues (Priority: Low, do alongside other work)

Lighthouse mobile: Accessibility 84, Best Practices 50, SEO 92.

- No `<main>` landmark on either page.
- All 5 `<table>` elements on each page lack `<th>` headers. These are the "best time to visit" and comparison tables, which are exactly the content most likely to be pulled into a rich result or an AI answer. Proper `<th>` markup materially improves machine parsing.
- Buttons without accessible names, colour contrast failures in breadcrumbs and card labels.
- One image with a missing `alt` on the main page. Image alt coverage is otherwise good.

---

## 3. On-page findings

### 3.1 The title tags do not contain the target keywords (Priority: Critical)

This is the clearest single finding in the audit.

| Page | Title | Contains exact target phrase? |
|---|---|---|
| **PYT Bali** | `28 Bali Tour Package From India Starts @ ₹16,761` | **No** ("Package" singular) |
| EaseMyTrip | `Bali Tour Packages – Book Bali Holidays at Best Price` | Yes |
| Thomas Cook | `Bali Tour Packages – Book Bali Trip Starting at Just ₹21,100` | Yes |
| SOTC | `Bali Tour Packages – Buy 1 Get 1 Free \| Book Now – SOTC` | Yes |
| DPauls | `Bali Tour Packages- Book Bali Holiday Packages Online \|DPauls Holidays` | Yes |

| Page | Title | Contains exact target phrase? |
|---|---|---|
| **PYT Honeymoon** | `26 Bali honeymoon package From ₹24,364  for Couples` | **No** (singular, lowercase, double space) |
| GT Holidays | `Book Bali Honeymoon Packages Starting @INR 10,000 \| GT Holidays` | Yes |
| SOTC | `Bali Honeymoon Packages – Bestseller for Couples` | Yes |
| Flamingo | `Bali Honeymoon Packages 2026 - Best Bali Honeymoon Deals` | Yes |
| DPauls | `Bali Honeymoon Packages- Book Bali Honeymoon Tour Packages` | Yes |

Pickyourtrail is the only page in either set whose title does not carry the exact target phrase. Eight out of eight reachable competitors do. Both PYT titles also lead with a dynamic package count, spending the most valuable characters in the title on a number rather than on the keyword, and neither carries the brand name.

The honeymoon title additionally contains a double space before "for Couples", which is a template bug.

**Rewrites (character counts measured):**

| Page | Proposed title | Chars |
|---|---|---|
| Bali main | `Bali Tour Packages from India @ ₹16,761 \| Pickyourtrail` | 55 |
| Honeymoon | `Bali Honeymoon Packages from ₹24,364 \| Pickyourtrail` | 52 |

If the count genuinely converts, keep it but move it out of the opening position:
`Bali Tour Packages: 28 Trips from ₹16,761 | Pickyourtrail` (57 chars).

**Meta descriptions** (current ones are serviceable; these are tighter and lead with the keyword):

- Main, 148 chars: `Compare 28 customisable Bali tour packages from India starting ₹16,761. Flights, handpicked hotels, private transfers, 24x7 support and no-cost EMI.`
- Honeymoon, 152 chars: `Compare 26 Bali honeymoon packages for couples from ₹24,364. Private pool villas, candlelight dinners, flights and 24x7 on-trip support. Customise free.`

### 3.2 The H1s miss the keyword too (Priority: Critical)

| Page | Current H1 | Problem |
|---|---|---|
| Bali main | `Bali Package From India` | Omits "Tour". Does not contain *Bali Tour Packages* |
| Honeymoon | `Bali Honeymoon Package` | Singular. Does not contain *Bali Honeymoon Packages* or *packages for couples* |

Every reachable competitor uses the plural exact-match H1: EaseMyTrip `Bali Tour Packages`, GT Holidays `Bali Honeymoon Packages`, SOTC `Bali Honeymoon Packages`, Flamingo `Bali Honeymoon Tour Packages`.

**Rewrites:**
- Main: `Bali Tour Packages from India`
- Honeymoon: `Bali Honeymoon Packages for Couples`

Combined with the title fix, this is the lowest-effort and highest-probability ranking intervention on the list. Both pages currently rank for terms their two most important on-page elements do not contain.

### 3.3 Above the fold is spent on decoration (Priority: High)

See `screenshots/02-honeymoon-mobile-fold.png` against `screenshots/04-sotc-honeymoon-mobile-fold.png`.

On the Pickyourtrail honeymoon page at 412x915 mobile:
- A hero image consumes the top third of the viewport. On the main page it is an autoplaying video carousel.
- The H1 sits inside a small grey box, set at roughly body-copy weight.
- The intro paragraph is clamped to a single truncated line behind "Read more".

On SOTC, at the same viewport, `Bali Honeymoon Packages` renders as a large red H1 with the full intro paragraph visible beneath it.

To be precise about the SEO impact of the "Read more" clamp: the text is present in the DOM and is fully crawlable. Measured `clientHeight` and `scrollHeight` are both 104px, meaning this is a CSS line clamp, not a JavaScript content injection. **This is not an indexation problem and should not be reported as one.** It is an engagement problem. Users landing from a commercial search see one truncated line of value proposition.

**Fix:** show the first 40 to 60 words uncollapsed, keep "Read more" for the remainder, and increase H1 visual weight.

### 3.4 The honeymoon page merchandises against its own keyword (Priority: High)

Default sort on the honeymoon page is "Lowest to highest". The first card returned is:

> *An incredible 8 day Bali + Thailand itinerary for an unforgettable Honeymoon vacation* — ₹24,364

The lead product on a page targeting *Bali honeymoon packages* is a Bali plus Thailand multi-country package. Its listing image is a street-level photograph of the Matahari House frontage showing shopfronts, parked motorbikes and overhead cabling. That is the first impression a honeymoon searcher receives. It is visible in `screenshots/02-honeymoon-mobile-fold.png`.

The page contains 18 separate mentions of Bali combined with Thailand, Malaysia or Singapore. On a page whose job is to be the most relevant result for "Bali honeymoon packages", multi-country inventory dilutes the topical signal and the commercial impression at the same time.

**Fixes:**
1. Change the default sort to a relevance or bestseller order that puts Bali-only honeymoon packages first. Keep price sort as a user-selectable option.
2. Filter multi-country combos out of the primary listing, or move them to a clearly separated section below the Bali-only packages.
3. Replace lead-card imagery with romantic Bali visuals. A street frontage photo on a honeymoon package is a merchandising error independent of SEO.

### 3.5 Structured data is broken where it counts (Priority: High)

Both pages carry three JSON-LD blocks: `WebPage`, `FAQPage`, and `Product` with `AggregateOffer`, `AggregateRating`, `Brand` and `Organization`. `BreadcrumbList` and `TouristTrip` are also present. Coverage is good. Two things inside it are wrong.

**The AggregateOffer misreports inventory.**

```json
"offers": {
  "@type": "AggregateOffer",
  "lowPrice": "16760.5",
  "highPrice": "16760.5",
  "offerCount": "1"
}
```

The page displays 28 packages ranging from ₹16,761 to ₹111,693. The schema declares one offer with identical low and high prices. The honeymoon page does the same, declaring `lowPrice` and `highPrice` both at `24364.156` against 26 displayed packages. Prices are also emitted with three decimal places on a rupee value.

This throws away the price-range rich result and creates a visible mismatch between structured data and page content.

**Fix:** emit true `lowPrice` and `highPrice` from the rendered listing, set `offerCount` to the real count, and round to whole rupees.

**The AggregateRating is site-wide, not page-specific.**

Both pages declare `ratingValue: 4.6, reviewCount: 8250` on a `Product`. The identical figure on both pages confirms it is the sitewide Google review count. Google's structured data policy requires review markup to describe the specific item being reviewed. Sitewide ratings applied to individual product entities are a documented cause of rich result suppression and manual action.

Given both pages lost rankings from March onward, this carries real risk and should be corrected regardless.

**Fix:** either attach ratings genuinely specific to the Bali package set, or remove `aggregateRating` from the `Product` and keep the sitewide rating on the `Organization` entity where it belongs.

### 3.6 Content depth is not the problem

Worth stating plainly, because it is where effort usually gets wasted.

| Page | Word count | H2s | H3s | FAQs | Internal links |
|---|---|---|---|---|---|
| Bali main | approx. 8,500 | 14 | 29 | 12 | 352 |
| Honeymoon | 6,413 (measured) | 13 | 17 | 15 | 363 |

Both pages already cover visa and entry requirements, best time to visit, area selection, sample itineraries, cost breakdowns, and inclusions. Both carry FAQ schema. The honeymoon page has a seven-day sample itinerary and a season-by-season table. This is equal to or deeper than every competitor reviewed.

**Do not write more content on these pages.** The gap is not informational coverage. Adding words to a page whose title and H1 miss the target keyword changes nothing.

### 3.7 The city cluster is well built (do not consolidate it)

The Bali cluster runs to 38 URLs, including 27 "from city" variants. These were checked for templated duplication and they are genuinely differentiated:

| URL | Title | H2s |
|---|---|---|
| `/tour-packages-from-delhi` | Bali Tour Packages from Delhi Starting at ₹21,190 | 19, including Delhi to Bali flight routes and airlines |
| `/tour-packages-from-chennai` | Bali Tour Packages from Chennai starts at ₹21,190 | 20, including Chennai airport and arrival guide |
| `/tour-packages-from-mumbai` | Bali Tour Packages from Mumbai \| No Cost EMI | 9, Mumbai-specific |
| `/honeymoon-tour-packages-from-delhi` | Bali Honeymoon Packages from Delhi - From ₹28,206 | 11, Delhi-specific honeymoon costs |

Each has a self-referencing canonical and city-specific content covering flight routes, duration and cost from that origin. This is a properly executed programmatic cluster, not a doorway farm. It should be left alone.

There is one thing to check rather than assume. The city pages carry `Bali Tour Packages` as an exact match in their titles while the main hub page does not. It is plausible that Google is favouring a city page over the hub for the head term. This cannot be confirmed without query-level data and is listed as a Phase 0 diagnostic, not a finding.

---

## 4. Ninety-day roadmap for the top 5 keywords

Target keywords:

| # | Keyword | Page | Position (Jul) | Peak (Mar) |
|---|---|---|---|---|
| 1 | Bali Tour Packages | `/packages/bali` | blended 12.7 | 4.5 |
| 2 | Bali Package | `/packages/bali` | blended 12.7 | 4.5 |
| 3 | Bali Honeymoon Packages | `/packages/bali/honeymoon-tour-packages` | blended 20.9 | 3.9 |
| 4 | Bali Honeymoon Tour Packages | same | blended 20.9 | 3.9 |
| 5 | Bali packages for couples | same | blended 20.9 | 3.9 |

Positions shown are blended page averages. Section 1 explains why these should not be treated as per-keyword positions. Phase 0 replaces them with real ones.

### Phase 0 — Days 1 to 5: establish the baseline

Nothing here is optional. A PIP plan built on the blended figures above is built on sand.

| Task | Output |
|---|---|
| Export GSC query-level data for both URLs, last 16 months | True position, clicks, impressions per target keyword |
| Pull the same period year over year (Jul 2025 vs Jul 2026) | Separates seasonality from genuine ranking loss |
| Run "Pages" report filtered to each target query | Confirms or rules out hub vs city-page cannibalisation |
| Cross-check the March to April break against the Google update timeline | Confirms or rules out an algorithmic cause |
| URL Inspection, "View crawled page", both URLs | Confirms whether hydration failures affect Google's render |
| Ask engineering what shipped to the packages template in March and April | Confirms or rules out a self-inflicted regression |

**Deliverable:** a one-page baseline with real per-keyword positions and a stated cause hypothesis. Take this to the PIP review. It reframes the conversation from "rankings dropped" to "here is what happened and here is the plan".

### Phase 1 — Days 6 to 20: on-page corrections

Highest confidence, lowest effort, fastest feedback. All of it is content or template, none of it needs an engineering sprint.

| # | Task | Page | Owner |
|---|---|---|---|
| 1 | Rewrite title to `Bali Tour Packages from India @ ₹16,761 \| Pickyourtrail` | Main | SEO |
| 2 | Rewrite title to `Bali Honeymoon Packages from ₹24,364 \| Pickyourtrail` | Honeymoon | SEO |
| 3 | Fix the double space in the honeymoon title template | Honeymoon | Dev |
| 4 | Change H1 to `Bali Tour Packages from India` | Main | SEO |
| 5 | Change H1 to `Bali Honeymoon Packages for Couples` | Honeymoon | SEO |
| 6 | Rewrite both meta descriptions to lead with the keyword | Both | SEO |
| 7 | Fix `AggregateOffer` to emit real low, high and count | Both | Dev |
| 8 | Remove sitewide `aggregateRating` from `Product`, move to `Organization` | Both | Dev |
| 9 | Change honeymoon default sort away from cheapest-first | Honeymoon | Product |
| 10 | Move multi-country combos below Bali-only inventory | Honeymoon | Product |
| 11 | Replace lead-card imagery with romantic Bali visuals | Honeymoon | Content |
| 12 | Uncollapse the first 40 to 60 words of intro copy | Both | Dev |

Request indexing through URL Inspection on completion. Expect first movement in 10 to 21 days.

### Phase 2 — Days 15 to 45: technical remediation

Runs in parallel with Phase 1. Needs engineering time, so book it now.

| # | Task | Metric it moves | Priority |
|---|---|---|---|
| 1 | Add `width`/`height` or `aspect-ratio` to all card and content images | CLS 0.34 to under 0.10 | Critical |
| 2 | Diagnose and fix React #418 and #423 hydration errors | Render and index reliability | Critical |
| 3 | Replace `no-store` with `s-maxage` plus `stale-while-revalidate` | TTFB 1,092 ms | High |
| 4 | Set `loading="lazy"` on all below-fold images (119 and 141 currently eager) | Payload, LCP | High |
| 5 | Serve AVIF/WebP with `srcset` via Gumlet | 5.4 MB image transfer | High |
| 6 | Enable Brotli at CDN and origin | 15 to 25% transfer saving | Medium |
| 7 | Add `href` to the 32 and 30 dead anchors | Internal link equity | Medium |
| 8 | Fix sitemap `lastmod` to real modification time | Crawl prioritisation | Medium |
| 9 | Paginate or lazily mount the package listing | DOM 6,749 elements | Medium |
| 10 | Resolve the `/guides/` robots block | Topical support | Investigate |
| 11 | Add `<main>` landmark, `<th>` to all 5 tables, fix button names and contrast | Accessibility, machine parsing | Low |

**Gate:** confirm CLS below 0.10 in CrUX before declaring this phase done. CrUX is a 28-day rolling window, so the field metric will lag the fix by roughly four weeks. Plan for that in the PIP timeline and say so up front.

### Phase 3 — Days 30 to 60: competitive and authority work

| Task | Notes |
|---|---|
| Manually review MakeMyTrip and Yatra pages in a browser | Both blocked automated access. This gap must be closed before the competitive analysis is presented as complete. |
| Build the SERP feature inventory for all 5 keywords | Which competitors hold AI Overview citations, People Also Ask, image packs and video. Determines whether the ceiling is organic position at all. |
| Audit internal links into both hub pages | 352 and 363 outbound links each, but inbound link count from the wider site is unmeasured. Hub pages need inbound equity, not just outbound. |
| Compare referring domain profiles against SOTC, Thomas Cook and EaseMyTrip | Establishes whether the gap is on-page or off-page. Not measured in this audit. |
| Add `<th>` markup and concise answer formatting to comparison tables | Improves eligibility for AI Overview and featured snippet extraction |

### Phase 4 — Days 60 to 90: measure, iterate, report

| Task | Cadence |
|---|---|
| Weekly rank tracking for all 5 keywords, mobile, India, city-segmented | Weekly |
| CrUX CLS, LCP, INP check on both URLs | Fortnightly |
| GSC impressions, clicks, CTR, position per target keyword against Phase 0 baseline | Fortnightly |
| Re-run Lighthouse and confirm SEO category returns 100 | Day 60 and Day 90 |
| Written progress report against the Phase 0 baseline | Day 45 and Day 90 |

### Realistic expectations

Worth being straight about this, because a PIP is a bad place to over-promise.

| Phase | What should move | When |
|---|---|---|
| Phase 1 | CTR on both pages. Title and H1 keyword matching is the fastest lever available. | 2 to 4 weeks |
| Phase 2 | CLS into the pass band, TTFB down. Ranking benefit is indirect and slower. | 4 to 8 weeks, CrUX lags 28 days |
| Phase 1 + 2 combined | Position recovery toward the March baseline, if the cause was on-page or technical | 6 to 12 weeks |
| Any phase | Nothing, if the March break was a core update or off-page displacement | Phase 0 tells you this in week 1 |

That last row is why Phase 0 comes first. If the decline turns out to be algorithmic or link-driven, the on-page and technical work is still correct and still worth doing, but the recovery curve is different and the target needs renegotiating. Better to establish that in week one than in week ten.

---

## 5. Priority summary

| # | Finding | Type | Priority | Effort |
|---|---|---|---|---|
| 1 | Titles miss exact target keyword on both pages, only site in the set that does | On-page | Critical | Low |
| 2 | H1s miss exact target keyword on both pages | On-page | Critical | Low |
| 3 | CLS 0.34 in field data, 124 and 145 images without dimensions | Technical | Critical | Medium |
| 4 | React hydration failures #418 and #423 on every load | Technical | Critical | Medium |
| 5 | Sitewide 8,250 review count on page-level `Product` schema | Schema | High | Low |
| 6 | `AggregateOffer` declares 1 offer against 28 and 26 real packages | Schema | High | Low |
| 7 | Honeymoon page leads with a Bali+Thailand combo and a street-frontage photo | On-page | High | Low |
| 8 | HTML served `no-store`, TTFB 1,092 ms | Technical | High | Low |
| 9 | 5.4 MB images, 119 and 141 eager loads | Technical | High | Medium |
| 10 | H1 and value proposition below the fold, intro clamped to one line | On-page | High | Low |
| 11 | 32 and 30 anchors without `href` | Technical | Medium | Low |
| 12 | Sitemap `lastmod` bulk-stamped across all 38 URLs | Technical | Medium | Low |
| 13 | Brotli not enabled | Technical | Medium | Low |
| 14 | DOM 6,749 and 6,477 elements | Technical | Medium | High |
| 15 | `/guides/` blocked in robots.txt | Technical | Investigate | Low |
| 16 | No `<main>`, 5 tables without `<th>`, contrast and button-name failures | Accessibility | Low | Low |

---

## 6. Evidence

| File | Shows |
|---|---|
| `screenshots/01-honeymoon-above-fold.png` | Desktop honeymoon page. Full viewport is hero image, H1 and packages below fold. |
| `screenshots/02-honeymoon-mobile-fold.png` | Mobile honeymoon page. Clamped intro, Bali+Thailand lead card, Matahari street-frontage image. |
| `screenshots/03-bali-main-mobile-fold.png` | Mobile main page. Autoplaying video hero, H1 "Bali Package From India", clamped intro. |
| `screenshots/04-sotc-honeymoon-mobile-fold.png` | SOTC at the same viewport. Large exact-match H1, full intro paragraph visible. |

Measurements are reproducible with Lighthouse mobile navigation audit and a Chrome performance trace against the live URLs.

---

## 7. Open items

1. MakeMyTrip and Yatra pages, four URLs total, need manual browser review. They blocked automated access.
2. Backlink and referring domain comparison was not run. It is needed to rule out an off-page cause.
3. Query-level GSC data is not available in this audit. Every per-keyword position in Section 4 is a blended page average until Phase 0 replaces it.
4. Whether the March to April break aligns with a Google update is unconfirmed. No update was assumed or named.
