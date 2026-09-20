# Kaarwan.com SEO Audit & Recommendations

**Date:** 14 August 2026
**Auditor:** Aakash Srivastava
**Inputs:** GSC "Valid" coverage export (`kaarwan.com-Coverage-Valid-2026-07-16.xlsx`, 1,000 rows), live crawl via Chrome DevTools, `sitemap.xml` (2,246 URLs), open blog API (2,171 records), CrUX field data (25 weeks)
**SEO Health Score: 37 / 100**

| Category | Weight | Score | Note |
|---|---|---|---|
| Technical SEO | 22% | 20 | No server-rendered metadata; unbounded URL space; soft 404s; no security headers |
| Content Quality | 23% | 55 | Substantial articles, named authors; but title bloat, no hubs, Medium duplication |
| On-Page SEO | 20% | 45 | Titles/metas are decent once rendered, but exist only after JS |
| Schema | 10% | 15 | Zero structured data on 2,171 articles; wrong type + rating mismatch on courses |
| Performance (CWV) | 10% | 25 | All mobile vitals failing in field data, and degrading |
| AI Search Readiness | 10% | 30 | Good `llms.txt`, but AI crawlers receive an empty page |
| Images | 5% | 75 | Alt text complete, modern formats, some oversizing |

---

## The headline

You flagged the `?id=` parameter as a cannibalisation problem. That is real, and I confirmed it, but it is the second-biggest issue. The larger one sits underneath it:

**Every page on kaarwan.com serves an empty 6.7 KB HTML shell. No title, no canonical, no H1, no body copy. All content is fetched client-side by `?id=`.**

Those two facts compound. The `?id=` parameter is the only key that produces content, and the canonical tag that would clean up the resulting duplicates only exists after JavaScript runs. So the mechanism that creates the duplicate URLs is server-side and instant, while the mechanism that fixes them is client-side and conditional.

---

## P0 — Critical

### 1. Zero server-rendered content for any crawler

The route is a Next.js `getServerSideProps` page, but `pageProps` comes back empty:

```json
{"props":{"pageProps":{},"__N_SSP":true},"page":"/blog/[category]/[url]",
 "query":{"id":"1522","category":"architecture","url":"the-right-vastu-placement-for-lockers"}}
```

Tested against five crawler user-agents on `/blog/architecture/the-right-vastu-placement-for-lockers?id=1522`:

| User-agent | HTTP | Bytes | Visible words | `<title>` | Canonical |
|---|---|---|---|---|---|
| Googlebot | 200 | 6,763 | 0 | absent | absent |
| bingbot | 200 | 6,763 | 0 | absent | absent |
| GPTBot | 200 | 6,763 | 0 | absent | absent |
| ClaudeBot | 200 | 6,763 | 0 | absent | absent |
| PerplexityBot | 200 | 6,763 | 0 | absent | absent |

Google renders JavaScript, so it eventually sees the content, but it pays a rendering cost per URL and the render is deferred and not guaranteed. Bing renders inconsistently. GPTBot, ClaudeBot and PerplexityBot do not execute JavaScript at all, which means the entire `llms.txt` effort currently delivers nothing: `robots.txt` explicitly welcomes those five AI crawlers, and every one of them receives a blank page.

The API that holds the content is `POST https://api.kaarwan.com/api/v1/blog/details`. Content behind a POST XHR is the least crawler-friendly pattern available; Google does not cache POST responses during rendering.

**Fix:** move the article fetch into `getServerSideProps` (or `getStaticProps` with ISR) and render title, meta description, canonical, H1 and body into the initial HTML response. This is the single change that unlocks everything else in this document.

**Note on hosting:** the HTML currently returns `cache-control: private, no-cache, no-store, max-age=0, must-revalidate` and every request logs `x-cache: Miss from cloudfront`. Nothing is cached at the edge. Once pages are server-rendered, this becomes an expensive setup. Move to ISR or `s-maxage` with `stale-while-revalidate`.

### 2. The `?id=` parameter creates an unbounded duplicate URL space

Confirmed: the numeric ID selects the content and the slug in the path is decorative. Verified live:

| Requested URL | Renders | Canonical points to |
|---|---|---|
| `/blog/architecture/the-right-vastu-placement-for-lockers?id=1522` | Vastu lockers article | itself |
| `/blog/architecture/the-right-vastu-placement-for-lockers?id=407` | **Varanasi article** | `/blog/architecture/transformation-of-varanasi-urban-architecture?id=407` |
| `/blog/architecture/buy-cheap-viagra-online?id=407` | **Varanasi article, HTTP 200** | `/blog/architecture/transformation-of-varanasi-urban-architecture?id=407` |
| `/blog/totally-fake-category/top-architecture-colleges-worldwide?id=194` | HTTP 200 | — |

Two things to be precise about, because they change the remediation:

**The canonical does self-correct.** On a mismatched slug the rendered canonical points at the true URL. So this is not classic cannibalisation where Google indexes ten copies and splits equity between them. Google can consolidate, in principle.

**But it only self-corrects after JavaScript runs.** Every fabricated variant returns HTTP 200 with a valid-looking empty shell. Google must spend a render on each one before it learns the URL is a duplicate. With an unbounded number of possible slugs, that is unbounded crawl budget exposure. Any competitor or scraper can mint thousands of indexable-looking URLs on your domain.

The arbitrary-slug behaviour is also a reputation vector. `kaarwan.com/blog/architecture/buy-cheap-viagra-online?id=407` returns HTTP 200 today. That URL can be built, linked and shared by anyone.

**Fix, in order:**
1. Key the data fetch on the slug in the path, not on `?id=`. The slug is already unique in your data (only 2 duplicate slugs across 2,171 records, listed in P1 below).
2. Until then, if the requested slug does not match the record the ID resolves to, return `301` to the correct URL server-side. Not a canonical tag, a redirect.
3. Register `id` as a paginating/no-effect parameter and stop generating it in internal links (currently 79 of 108 internal links on a sample article carry `?id=`).
4. Return a real `404` for unresolvable IDs.

### 3. Clean URLs render a blank page

`/blog/architecture/transformation-of-varanasi-urban-architecture` with no `?id=` returns **HTTP 200 with an entirely white page**: empty title, no canonical, no H1, 0 words. Screenshot captured at `kaarwan-audit-evidence/blank-no-id.png`.

The same applies to the flagship commercial page. `/course/advance-revit-bim-certification-course` renders blank; only `/course/advance-revit-bim-certification-course?id=36` produces the real page with pricing, rating and `Product` schema.

This is the URL shape that any human, journalist or competitor would naturally link to, and the shape `llms.txt` itself advertises. Every one of them currently lands on nothing.

Soft-404 confirmation: `/blog/architecture/this-slug-does-not-exist-98765` returns **200**, and `/course/this-course-does-not-exist-98765` returns **200**. By contrast `/this-page-definitely-does-not-exist-98765` correctly returns 404, so the 404 handler exists; the blog and course routes simply never invoke it.

### 4. Indexed URLs serving content that contradicts their slug

This is the part of your hypothesis that is fully confirmed in the indexed set. 13 IDs in the GSC Valid export appear under more than one indexed path. The clearest case:

`https://www.kaarwan.com/blog/architecture/design-architecture-of-taj-mahal?id=62` is indexed, returns 200, and renders:

- Title: *"7 Historic Movements that Revolutionized Graphic Design"*
- H1: *"7 Historic Movements that Revolutionized Graphic Design"*
- Canonical: `/blog/ui-ux-design/historic-moment-in-graphic-design?id=62`

An indexed URL promising Taj Mahal architecture serves graphic-design history and canonicals away to a different page. The `design-architecture-of-taj-mahal` slug is effectively burned.

Full list of ID collisions across indexed paths:

| ID | Indexed paths |
|---|---|
| 152 | `/blog/architecture/exploring-the-rich-heritage-of-kashmiri-architecture`, `/case-studies/bim-certification-for-mep-engineers`, `/course/bim-certification-for-mep-engineers` |
| 135 | `/case-studies/ui-ux-design`, `/case-studies/ui-ux-design-user-interface-experience-affordable-course`, `/course/ui-ux-design-12-week-course-advance` |
| 31 | `/blog/architecture/autocad-secrets-that-you-must-know`, `/education-travel/northeast-roadtrip-2023`, `/masterclass/learn-sustainabilty-passive-design-strategies...` |
| 62 | `/blog/architecture/design-architecture-of-taj-mahal`, `/blog/ui-ux-design/historic-moment-in-graphic-design` |
| 206 | `/blog/architecture/a-comprehensive-guide-to-architecture-thesis`, `/blogs/architecture/...` |
| 80 | `/blog/architecture/vernacular-elements-intrinsic-flooring-finishes-of-india`, `/blogs/architecture/...` |
| 270 | `/blog/architecture/varanasi-architecture-temples-ghats-and-monuments`, `/blogs/architecture/...` |
| 1332 | `/blog/UI-UX Design/the-art-and-science-of-color...`, `/blog/ui-ux design/the-art-and-science-of-color...` |
| 29, 28, 84, 89, 33 | blog article paired with a `/masterclass/`, `/education-travel/` or `/case-studies/` path |

Note the `/blogs/` (plural) paths for IDs 206, 80 and 270: **both `/blog/` and `/blogs/` return 200** for the same article, and both are indexed. `/blogs/` should 301 to `/blog/`.

### 5. Half the sitemap points at non-canonical URLs

`sitemap.xml` holds 2,246 URLs. **1,105 of them (49.2%) are not the canonical URL of the page they reference.**

Root cause is the `category` field in your database, which stores nine different casings of four categories:

| Stored value | Count |
|---|---|
| `architecture` | 985 |
| `Architecture` | 729 |
| `ui-ux design` | 106 |
| `UI-UX Design` | 105 |
| `UI-UX design` | 80 |
| `engineering` | 81 |
| `interior design` | 69 |
| `Engineering` | 12 |
| `Interior Design` | 4 |

The sitemap writes the raw stored value into the URL. The application then normalises it to lowercase-hyphenated. Result:

- **741 sitemap URLs** with an uppercase category, e.g. `/blog/Architecture/top-architecture-colleges-worldwide?id=194`, which **308-redirects** to the lowercase form. A sitemap should never list a redirect.
- **364 sitemap URLs containing a literal space**, e.g. `/blog/ui-ux design/importance-of-writing-research-papers?id=30`. These return 200 and canonical to the hyphenated form, so they are duplicates advertised as originals.

Meanwhile internal links use the hyphenated form. So your sitemap and your internal linking are telling Google two different things about which URL is canonical, for 1,105 pages.

`lastmod` is also unreliable: **2,017 of 2,246 URLs claim `lastmod` = 2026-08-14**, i.e. today. Google discounts `lastmod` entirely once it looks auto-stamped. Emit the real content-modified date.

`priority` is `0.7` on 2,232 of 2,246 URLs, which carries no information. Google ignores `priority` and `changefreq`; they can be dropped.

Three robots-disallowed URLs are also listed: `/dashboard/resources` and `/dashboard/referral/how-it-works` (the latter twice).

**Missing entirely:** not a single `/course/aec/...` URL appears in the sitemap, despite those being the clean, working, no-parameter course pages.

---

## P1 — High

### 6. Commercial pages exist under five URL patterns

For one course, `advance-revit-bim-certification-course`:

| URL | Status | Canonical | Schema | In sitemap |
|---|---|---|---|---|
| `/course/advance-revit-bim-certification-course?id=36` | 200 | itself | `Product` | yes |
| `/course/aec/advance-revit-bim-certification-course` | 200 | **itself** | none | **no** |
| `/course/offer/advance-revit-bim-certification-course` | 200 | → `?id=36` version | none | yes |
| `/course/advance-revit-bim-certification-course` | 200 | none | none | no |
| `/masterclass/...` and `/case-studies/...` variants | 200 | varies | none | some |

The `/course/offer/` variant consolidates correctly. The problem is `/course/aec/...`: it **self-canonicalises**, renders 1,975 words without needing `?id=`, has a different title and H1, and is absent from the sitemap. So you have two self-canonical URLs competing for the same course, and the better-built one is hidden from Google.

This is genuine cannibalisation, and it is on revenue pages rather than blog pages.

**Fix:** pick `/course/aec/<slug>` as canonical (it is the clean, parameter-free, working pattern), 301 the others to it, port the `Product`/`Course` schema across, and add it to the sitemap.

### 7. No category hub pages exist

- `/blog/architecture` → **404**
- `/blogs/architecture` → **404**
- `/blogs` → 200, but exposes only **42 unique article links** out of 2,171

`/blogs` has no `rel=next`/`rel=prev`, no crawlable pagination links, and no category links. "Load more" is JavaScript-only. So roughly **2,129 articles have no crawlable internal path from the blog index**, and are reachable only via the sitemap and related-post modules on sibling articles.

For a site with 985 architecture articles, having no `/blog/architecture/` hub is the largest missed topical-authority opportunity here. Category hubs would give you crawl paths, internal link equity distribution, and rankable mid-funnel pages.

`/blogs` has a further problem: its title and H1 are inherited from whichever article is currently trending. Today both read *"BIM Architect Salary in India 2026 | Jobs, Skills & Career Opportunities."* The blog index has no stable identity of its own and its title changes without anyone editing it.

### 8. Zero structured data on 2,171 articles

No JSON-LD of any kind on blog article pages. Missing, in priority order:

- `Article` / `BlogPosting` with `headline`, `datePublished`, `dateModified`, `author`, `publisher`, `image`
- `BreadcrumbList` (a visual breadcrumb renders on the page but is not marked up, and no `<nav>` or `.breadcrumb` element exists)
- `FAQPage` where articles carry Q&A sections

The data is all present in the API response (`title`, `publishedAt`, `Author.name`, `Author.image`, `readTime`, `image`), so this is a template change, not a content project.

Homepage carries only `WebSite`. No `Organization` node, despite `llms.txt` holding a complete, well-written organisation profile (founders, funding, certifications, placement partners). An FAQ section renders on the homepage with no `FAQPage` markup.

### 9. Course schema: wrong type, and a rating that contradicts the page

The `Product` schema on `/course/...?id=36` declares:

```json
"aggregateRating": {"ratingValue": "4.4", "reviewCount": "127"}
```

The visible page displays **4.7**. Structured-data ratings must match visible content; a mismatch risks losing rich results and is the kind of thing that attracts a manual action. Verify which figure is true and align them.

Also:
- Type should be `Course` + `CourseInstance`, not `Product`. Kaarwan sells courses, and `Course` is the type eligible for Google's course rich results. `Product` on a training programme will not earn them.
- No `offers` node despite ₹10,000 displaying on the page, so no price in schema.
- `@context` uses `http://schema.org/`; use `https://`.
- `/course/aec/...` has no schema at all.

### 10. Malformed URLs generated by bad slugs

34 slugs in the database contain characters outside `[a-z0-9-]`, including `&`, apostrophes, commas, spaces and uppercase:

```
enhance-bim-efficiency-revit's-collaborate,-manage-&-insert-tabs
parametric-design-&-digital-fabrication
best-master's-degree-university-post-graduate-architect
legends-families-for-project-visualization-in-revit      (trailing space)
What-to-know-before-appearing-for-nata                   (trailing space + caps)
```

The `&` characters break URL parsing, which is where the garbage query strings in your GSC export come from:

```
/masterclass/best-online-interior-styling-decoration-workshop-for-architects-designers
  ?id=17&-insert-tabs=,,&ref=6EKjE0gZ&category=architecture&url=how-to-blend-nature-into-your-design...
```

The `-insert-tabs`, `-digital-fabrication`, `-BIM` and `-rendering` parameters are fragments of slugs containing `&`. The trailing `category=`/`url=` pairs indicate a client-side router bug where blog query parameters persist onto masterclass and course paths.

Trailing spaces in slugs also produced indexed URLs with a literal space, e.g. `/blog/architecture/best-hotels-in-india ?trk=...&id=90` and `/blog/architecture/the-art-deco-theatres-of-south-india `.

**Fix:** sanitise slugs to `[a-z0-9-]` at write time, 301 the old forms, and stop the router from carrying stale query parameters across route changes.

Parameter stripping is also inconsistent. `?id=407&extra=1` correctly 308s to `?id=407`, but `?preview=true&id=418` returns 200 and is indexed, as is an `fbclid` variant. The strip appears to be order-dependent. A `preview=true` URL being indexed is worth fixing on its own.

### 11. Core Web Vitals are failing on mobile and degrading

My lab test on a fast connection showed LCP 964 ms, which looks fine. CrUX field data for real users says otherwise, and field data is what Google uses.

**Mobile, origin-level, 25 weeks to 2026-08-08:**

| Metric | p75 now | Verdict | 25-week change | Mid-series peak | % of users in "poor" |
|---|---|---|---|---|---|
| LCP | 4,249 ms | **POOR** | 3,282 → 4,249 (+29.5%) | 4,570 ms | 28.1% |
| CLS | 0.38 | **POOR** | 0.26 → 0.38 (+46.2%) | 0.41 | 32.6% |
| FCP | 3,717 ms | **POOR** | 2,624 → 3,717 (+41.7%) | 4,242 ms | 35.4% |
| INP | 229 ms | Needs improvement | 197 → 229 (+16.2%) | 247 ms | 5.6% |
| TTFB | 1,068 ms | Needs improvement | 1,096 → 1,068 (stable) | 1,199 ms | 11.0% |

Percentages are computed from the raw CrUX p75 endpoints. LCP, FCP and INP each peaked mid-series and then partially recovered, which suggests part of the cause was mitigated. That partial recovery is useful for pinpointing the responsible deploy.

**Desktop:** LCP 3,401 ms (degrading +22.9%), FCP 2,174 ms (degrading +43.3%), CLS 0.105 (improving), INP 92 ms (stable).

Every mobile vital is failing and four of five are getting worse.

The week-by-week series locates the regression precisely:

```
LCP: 3282 3238 3224 3236 3289 3303 3300 3298 3328 3656 3933 4149 4425 4493 4502 4570 4528 4498 4466 4391 4311 4210 4246 4269 4249
FCP: 2624 2654 2734 2800 2857 2899 2853 2834 2866 3190 3487 3748 4039 4132 4185 4242 4215 4157 4088 4001 3885 3753 3781 3781 3717
CLS: 0.26 0.27 0.27 0.28 0.28 0.28 0.28 0.28 0.26 0.24 0.24 0.23 0.27 0.33 0.37 0.39 0.37 0.36 0.37 0.37 0.39 0.41 0.41 0.40 0.38
INP:  197  202  207  216  218  215  211  206  208  220  229  237  239  238  240  240  245  247  245  241  234  223  223  227  229
```

LCP, FCP and INP all break at the same point, the 10th value. CLS breaks three periods later.

LCP breaks from the 10th collection period, covering **2026-03-29 to 2026-04-25**. CLS breaks from the 13th, covering **2026-04-19 to 2026-05-16**. Something shipped between late March and mid-May 2026 that damaged both. Check deploys in that window before optimising anything else; this is a regression to reverse, not a baseline to improve.

Contributing factors I can measure:
- **4.7 MB of third-party JavaScript.** Google Tag Manager 2.2 MB, Facebook 1.1 MB, Google APIs 366 kB, AWS 332 kB, Crazy Egg 251 kB, ContentSquare 153 kB, LinkedIn Ads 152 kB, Clarity 103 kB. Seven separate analytics and session-recording tools: GA4, GTM, Google Ads, Facebook Pixel, Crazy Egg, ContentSquare, Microsoft Clarity, LinkedIn. Consolidate; you almost certainly do not need three session-recording products.
- On mobile emulation, **2,179 ms of a 2,432 ms LCP was render delay**, not download. That is the client-side rendering cost from P0-1. Server-rendering the content addresses LCP, FCP and CLS together.
- 500 kB of cacheable bytes served with inadequate cache lifetimes.
- 313 kB of image over-delivery.
- 384 images on the homepage.

### 12. Legacy Medium blog still live and indexed on a Kaarwan subdomain

`blog.kaarwan.com` is a Medium-hosted publication, still live, with 15 URLs in the Valid coverage export. Verified on `blog.kaarwan.com/squinches-and-pendentives-in-architecture-8359cf6b8825`:

- `meta robots: index,follow,max-image-preview:large`
- Self-canonical to the `blog.kaarwan.com` URL
- Marked **"Member-only story"**, so paywalled
- Publication bio reads: *"India's leading educational travel company, Kaarwan is on a mission to promote travel as a means to education."*

Three problems. Split authority across two Kaarwan-branded hostnames. Topic overlap with www (this post versus `/blog/architecture/pendentives-and-squinches-symbolism-in-religious-architecture?id=889`; and the Medium post `7-historical-movements-that-have-shaped-the-evolution-of-the-graphic-design-industry` versus id=62 *"7 Historic Movements that Revolutionized Graphic Design"*, which look like the same article). And a brand description that contradicts your current positioning, which matters for entity resolution in AI search: `llms.txt` says BIM edtech, Medium says travel company.

I could not systematically compare full text across all 15 posts because Medium returns 403 to non-browser requests; I verified one post in a real browser. The two overlaps above are the ones I am confident about from titles.

**Fix:** decide whether the Medium archive has value. If yes, migrate the posts to www and 301 or set cross-domain canonicals. If no, remove them. Either way, correct the publication bio, and note that Medium limits your control here, which is itself an argument for migrating.

Also `robots.txt` contains five invalid directives:

```
Disallow: https://admin.kaarwan.com/
Disallow: https://dev.kaarwan.com/
Disallow: https://dev.kaarwan.com/*
Disallow: https://api.kaarwan.com/api/
Disallow: https://devapi.kaarwan.com/api/
```

`Disallow` takes a path, not an absolute URL. Google ignores these lines entirely. Each host needs its own `robots.txt`.

---

## P2 — Medium

### 13. Title tags

From 2,171 API records: median length 64 characters, **1,272 titles (58.6%) exceed 60 characters** and will truncate in SERPs. Longest is 138 characters:

> *"Interior Architect vs Technical Architect vs Sustainability Architect vs Conservation Architect vs Industrial ..."*

Three duplicate title pairs:

| Title | IDs | Slugs |
|---|---|---|
| "Top 5 Reasons Why Every Mechanical, Electrical, and Plumbing Engineer Should Lea..." | 1993, 2014 | `5-reasons-why-mep-engineer-must-learn-bim-now`, `why-mep-engineers-must-learn-bim` |
| "Microinteractions: The Subtle Art of Elevating User Experience" | 1366, 1367 | identical slug, categories `Architecture` and `UI-UX design` |
| "Crafting Impactful Iconography: The Art of Creating Effective UI Icons" | 1365, 1359 | identical slug, categories `ui-ux design` and `UI-UX Design` |

The last two are true duplicate records: same slug, same title, two IDs, differing only by category casing. Merge and 301. IDs 1993 and 2014 are two articles on one topic and should be consolidated.

Also note the "Microinteractions" and "Iconography" articles are filed under `Architecture` in one copy, which is a miscategorisation on top of the duplication.

### 14. Heading structure

- Blog articles: single H1, 11 H2s and 24 H3s on the sample. Reasonable.
- Homepage: **four H1s**, including `"93%"` and `"9/10"` as H1 elements, and the real H1 duplicated. Stat callouts should not be H1.
- Course page: H1 duplicated twice.
- `/blogs`: H1 inherited from the trending article (see P1-7).

### 15. Indexed pages that should not be indexed

Present in the Valid coverage export:

- `/auth/login` — disallowed in robots.txt, indexed anyway, returns 200
- `/dashboard/leaderboard/1062` — `/dashboard/` disallowed, indexed, 200
- `/payments/master-interior-styling-spatial-decoration?id=715` — `/payments/` disallowed, indexed, 200
- `/resume/dimple-jethani-135-v2PRv7WjAlLDL` — a named individual's resume, publicly indexed
- `/skill-test`
- `/blog/architecture/craft-perfect-bim-resume?preview=true&id=418` — a preview URL

`robots.txt` `Disallow` prevents crawling, not indexing. A URL that is already indexed and then disallowed stays indexed indefinitely, because Google cannot re-crawl it to see a `noindex`. To remove these: allow crawling and serve `noindex`, or use the GSC Removals tool, or return 401/404. The resume URL is worth checking against whatever consent users gave when they built it.

### 16. Redirect and canonical hygiene

- Apex to www uses **302**, should be **301**: `kaarwan.com/...` → `www.kaarwan.com/...`
- Homepage canonical is `https://www.kaarwan.com` while the page is `https://www.kaarwan.com/`. Pick one.
- `llms.txt` links to apex URLs (`https://kaarwan.com/course/...`), all of which 302. Point them at the canonical www URLs.
- Category casing produces 308s, which are correct but should not be reachable from the sitemap.
- Internal links contain self-referencing `#` fragments (8 links on one sample page pointing to `...?id=1332#`).

### 17. No security headers

The homepage response carries none of:

`Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`

It does expose `x-powered-by: Next.js`. Not a direct ranking factor, but HSTS in particular matters for a site taking payments, and the Medium subdomain already sets HSTS and `X-Frame-Options` while the main domain does not.

### 18. Author and E-E-A-T signals

18 distinct author names across 2,171 articles, but **1,131 are "Team Kaarwan "** (with a trailing space) and a further 37 are `"Team Kaarwan"` (without), so the same entity is split into two values. 52% of content is attributed to a generic team byline.

Named authors carry the rest: Ar. Pragya Laungani (193), Shivani Chougula (158), Manish Kumar (133), Nishita Verma (130), Priyanka (117), Paridhi Patidar (117), Kavya Srivastava (75). `"Nishita "` (13) is likely the same person as `"Nishita Verma"`.

For an architecture-education site competing on professional credibility, and given no author markup exists at all (P1-8), this is a real gap. Recommend author bio pages, `Person` schema with credentials, and reassigning the "Team Kaarwan" bulk to real authors where records permit.

### 19. Content freshness distribution

| Year published | Articles |
|---|---|
| 2022 | 2 |
| 2023 | 93 |
| 2024 | 1,225 |
| 2025 | 596 |
| 2026 | 255 |

56% of the library was published in 2024. Once `dateModified` is in schema, an audit-and-refresh pass on the 2024 cohort will be the highest-leverage content work available, especially for anything with a year in the title or salary and jobs data.

### 20. Images

Genuinely good: **0 of 82 images missing alt text** on the sample article, 0 of 384 on the homepage. Modern formats in use (WebP, AVIF, SVG alongside JPG/PNG/GIF). 37 of 82 lazy-loaded.

Remaining: 313 kB of over-delivery from images larger than their rendered size, one image resolving with an empty file extension, and 384 images on a single homepage is worth questioning.

---

## Recommended sequence

**Phase 1, weeks 1 to 2. Stop the bleeding.**
1. Server-render title, meta description, canonical, H1 and body copy into the initial HTML (P0-1). Everything else depends on this.
2. Return `301` server-side when the requested slug does not match the ID's true slug (P0-2).
3. Return real `404`s for unresolvable slugs and IDs (P0-3).
4. Fix the sitemap generator to emit normalised lowercase-hyphenated categories, real `lastmod`, and to include `/course/aec/` URLs (P0-5).
5. `301` `/blogs/` to `/blog/` (P0-4).

**Phase 2, weeks 3 to 4. Consolidate.**
6. Pick one canonical URL pattern per course and 301 the rest (P1-6).
7. Normalise the `category` field in the database to four lowercase values (P0-5, P2-13).
8. Sanitise the 34 malformed slugs and 301 the old forms (P1-10).
9. Merge the duplicate article records and consolidate the MEP-BIM pair (P2-13).
10. Resolve the Medium subdomain (P1-12).
11. Identify and revert the March-to-May 2026 CWV regression (P1-11).

**Phase 3, weeks 5 to 8. Build.**
12. Ship category hub pages at `/blog/architecture/` and siblings, with crawlable pagination (P1-7).
13. Add `Article`, `BreadcrumbList`, `Organization`, `Course` + `CourseInstance`, `FAQPage` schema (P1-8, P1-9).
14. Fix the course `aggregateRating` mismatch (P1-9).
15. Consolidate the seven analytics tools; trim the 4.7 MB third-party payload (P1-11).
16. `noindex` the login, dashboard, payments, preview and resume URLs (P2-15).
17. Author bio pages and `Person` schema; reassign the "Team Kaarwan" bulk (P2-18).
18. Refresh the 2024 content cohort (P2-19).

Once Phase 1 ships, the `?id=` question you raised becomes tractable: the canonical will exist before Google renders, so consolidation stops depending on JavaScript execution.

---

## What I verified, and what I could not

**Verified live:** raw HTML for five crawler user-agents; ID-swap and arbitrary-slug behaviour; blank clean URLs; soft 404s; canonical tags on 8 URL patterns; HTTP status and redirect chains on 30+ URLs; `robots.txt`; `llms.txt`; all 2,246 sitemap entries; 2,171 blog records from the public API; JSON-LD on homepage, blog, and three course URL patterns; security headers; CrUX field data for 25 weeks on mobile and desktop; lab performance traces on desktop and throttled mobile; the Medium subdomain in a real browser.

**Could not verify:**
- **GSC performance data.** The export you gave me is coverage only, so I have no clicks, impressions, positions or queries. Every ranking and traffic statement above is deliberately absent. If you have GSC access to `kaarwan.com`, that would let me quantify which of these issues is actually costing traffic and rank the roadmap by revenue rather than severity.
- **Total indexed page count.** GSC caps exports at 1,000 rows and the export has exactly 1,000, so the real Valid count is 1,000 or higher, not exactly 1,000. The sitemap declares 2,246 URLs, so the gap is worth checking in the Pages report.
- **Full text comparison between the 15 Medium posts and their www counterparts.** Medium returns 403 to non-browser requests. I confirmed one post in a browser and matched two by title.
- **Whether Google is currently rendering and consolidating these duplicates.** A URL Inspection live test on `/blog/architecture/design-architecture-of-taj-mahal?id=62` would settle whether Google sees the corrected canonical. That is a one-minute check in GSC.
- **Backlink profile.** No Moz, Ahrefs or Semrush data pulled. The Semrush connector in this workspace needs authorisation.

## Deliverables

| File | Contents |
|---|---|
| `seo-audit-kaarwan.com-2026-08-14.md` | This document. All 20 findings with reproduction steps, tested URLs and observed responses. |
| `kaarwan-phase1-tickets-2026-08-14.md` | Phase 1 as five implementation-ready tickets (KAAR-101 to 105) with acceptance criteria and a runnable `Verify` block per ticket that fails today. |
| `kaarwan-seo-audit-2026-08-14.xlsx` | Seven sheets: Summary (score + key numbers + scope limits), Findings (all 20, severity-coded, with owner and estimate), Redirect Map (1,235 rows), Orphan Inventory (2,171 rows), CWV Field Data (25 periods, threshold-coded), Category Casing, Crawler Test. |
| `kaarwan-audit-evidence/blank-no-id.png` | Screenshot of the blank HTTP 200 page described in P0-3. |

## Open questions

1. Do you have GSC access to `kaarwan.com`? That unlocks query data, live URL inspection, and lets me re-rank this roadmap by traffic at risk rather than by severity.
2. Is this a client engagement, a prospect audit, or an internal project? It changes how much of the Phase 1 engineering work is realistic to recommend.
3. Do you want the ~2,129 orphaned articles mapped in full, and the 34 malformed slugs listed as a redirect map ready for engineering?
