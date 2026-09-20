# Kaarwan.com — Phase 1 Engineering Tickets

**Sprint goal:** make article and course pages indexable without JavaScript, and close the unbounded duplicate URL space.
**Duration:** 2 weeks
**Blocking relationship:** KAAR-101 blocks 102, 103 and 105. 104 can run in parallel.
**Stack context:** Next.js (pages router, `getServerSideProps`), API at `api.kaarwan.com`, CloudFront in front.

Every ticket below is reproducible against production as of 14 Aug 2026. Each "Verify" block is a command or check that fails today and must pass on completion.

---

## KAAR-101 — Server-render article and course metadata and body copy

**Type:** Bug · **Priority:** P0 · **Est:** 5 days · **Owner:** Frontend

### Problem

`/blog/[category]/[url]` and `/course/[slug]` are declared as `getServerSideProps` routes but return empty props, so the server response contains no title, meta description, canonical, H1 or body copy. All content is fetched client-side via `POST https://api.kaarwan.com/api/v1/blog/details`.

Current server response for any article:

```json
{"props":{"pageProps":{},"__N_SSP":true},
 "page":"/blog/[category]/[url]",
 "query":{"id":"1522","category":"architecture","url":"the-right-vastu-placement-for-lockers"}}
```

### Impact

- Googlebot and bingbot must render JavaScript to see any content, on a deferred and non-guaranteed schedule.
- GPTBot, ClaudeBot and PerplexityBot do not execute JavaScript, so they receive nothing. `robots.txt` explicitly allows all three.
- 2,179 ms of a 2,432 ms throttled-mobile LCP is render delay, not download. This is the largest single contributor to the failing mobile LCP.

### Scope

1. Move the article fetch into `getServerSideProps` for `/blog/[category]/[url]`.
2. Do the same for the course routes.
3. Render into the initial HTML: `<title>`, `<meta name="description">`, `<link rel="canonical">`, `<meta property="og:*">`, the `<h1>`, and the full article body.
4. Prefer `getStaticProps` with `revalidate` (ISR) over SSR where the content is not personalised. Article bodies are not personalised.
5. Replace the `POST /blog/details` call with a `GET` so the response is cacheable. If the API cannot change, proxy it server-side.

### Acceptance criteria

- [ ] `curl` with no JavaScript returns a document containing the correct `<title>`, `<link rel="canonical">` and `<h1>` for the requested article.
- [ ] Visible word count in the raw HTML is within 5% of the client-rendered word count.
- [ ] Response is `Cache-Control: public, s-maxage=3600, stale-while-revalidate=86400` or equivalent; `x-cache: Hit from cloudfront` on a repeat request.
- [ ] No regression in the rendered page for logged-in users.

### Verify

```bash
U="https://www.kaarwan.com/blog/architecture/the-right-vastu-placement-for-lockers?id=1522"

# must print the real title, currently prints nothing
curl -s "$U" | grep -o '<title>[^<]*</title>'

# must print the canonical, currently prints nothing
curl -s "$U" | grep -o 'rel="canonical"[^>]*'

# must be > 1000, currently 0
curl -s "$U" | sed -e 's/<script[^>]*>.*<\/script>//g' -e 's/<[^>]*>/ /g' | wc -w

# must return the article for a non-JS AI crawler, currently returns an empty shell
curl -s -A "GPTBot/1.0 (+https://openai.com/gptbot)" "$U" | grep -c "Vastu"
```

---

## KAAR-102 — Resolve article content by slug, not by `?id=`

**Type:** Bug · **Priority:** P0 · **Est:** 3 days · **Owner:** Frontend + Backend
**Depends on:** KAAR-101

### Problem

The numeric `?id=` parameter selects the content; the slug in the path is ignored. Any slug paired with a valid ID returns HTTP 200 with that ID's content.

Reproduced on production:

| URL | Renders |
|---|---|
| `/blog/architecture/the-right-vastu-placement-for-lockers?id=1522` | Vastu lockers article (correct) |
| `/blog/architecture/the-right-vastu-placement-for-lockers?id=407` | Varanasi article |
| `/blog/architecture/buy-cheap-viagra-online?id=407` | Varanasi article, HTTP 200 |
| `/blog/totally-fake-category/top-architecture-colleges-worldwide?id=194` | HTTP 200 |

The rendered canonical does self-correct, but it is written by JavaScript, so it appears only after render. The duplicate URL is created server-side and instantly. The result is an unbounded space of crawlable 200-status URLs, plus a reputation vector: the third URL above resolves on the production domain today.

### Scope

1. Change the data fetch to key on the path slug. Slugs are unique across all 2,171 records with two exceptions, listed below, which KAAR-2xx resolves separately.
2. Keep `?id=` accepted for backward compatibility for one release, then remove it.
3. Where a request arrives with both a slug and an `?id=` that disagree, **301** to the canonical URL for that ID. Server-side, before render.
4. Stop emitting `?id=` in internal links. A sample article currently carries the parameter on 79 of 108 internal links.

### Known slug collisions to handle first

| Slug | IDs | Note |
|---|---|---|
| `microinteractions-the-subtle-art-of-elevating-user-experience` | 1366, 1367 | Same title. 1366 miscategorised as `Architecture`. |
| `crafting-impactful-iconography-the-art-of-creating-effective-ui-icons` | 1365, 1359 | Same title, differ only by category casing. |

### Acceptance criteria

- [ ] `/blog/architecture/<any-slug>?id=407` where `<any-slug>` is not ID 407's slug returns **301** to `/blog/architecture/transformation-of-varanasi-urban-architecture`.
- [ ] `/blog/architecture/transformation-of-varanasi-urban-architecture` with no parameter renders the article (see KAAR-103).
- [ ] A fabricated slug with a valid ID no longer returns 200.
- [ ] Zero internal links in rendered HTML contain `?id=`.
- [ ] Redirects are single-hop; no chains.

### Verify

```bash
# must be 301, currently 200
curl -sI "https://www.kaarwan.com/blog/architecture/buy-cheap-viagra-online?id=407" | head -1

# must be 301 to the canonical slug, currently 200
curl -sI "https://www.kaarwan.com/blog/architecture/the-right-vastu-placement-for-lockers?id=407" \
  | grep -Ei '^(HTTP|location)'

# must be 0, currently 79
curl -s "https://www.kaarwan.com/blog/architecture/the-right-vastu-placement-for-lockers?id=1522" \
  | grep -o 'href="[^"]*id=[0-9]*"' | wc -l
```

---

## KAAR-103 — Parameter-less URLs must render; unresolvable URLs must 404

**Type:** Bug · **Priority:** P0 · **Est:** 2 days · **Owner:** Frontend
**Depends on:** KAAR-101

### Problem

Two separate failures on the same routes.

**Blank 200 pages.** Without `?id=`, the article route returns HTTP 200 with an entirely white page: empty `<title>`, no canonical, no `<h1>`, 0 words. Confirmed visually. The same applies to the flagship course page.

| URL | Status | Renders |
|---|---|---|
| `/blog/architecture/transformation-of-varanasi-urban-architecture` | 200 | blank |
| `/course/advance-revit-bim-certification-course` | 200 | blank |

These are the URL shapes external sites link to, and the shapes `llms.txt` advertises.

**Soft 404s.** Unresolvable slugs return 200 rather than 404:

| URL | Status | Expected |
|---|---|---|
| `/blog/architecture/this-slug-does-not-exist-98765` | 200 | 404 |
| `/course/this-course-does-not-exist-98765` | 200 | 404 |
| `/this-page-definitely-does-not-exist-98765` | 404 | 404 (already correct) |

The 404 handler exists and works at the root level; the blog and course routes never invoke it.

### Scope

1. Once KAAR-102 lands, parameter-less URLs resolve naturally. Confirm and add tests.
2. Return `notFound: true` from `getServerSideProps`/`getStaticProps` when the slug does not resolve, so Next.js serves a real 404.
3. Apply to `/blog/[category]/[url]`, `/course/[slug]`, `/course/aec/[slug]`, `/masterclass/[slug]` and `/case-studies/[slug]`.

### Acceptance criteria

- [ ] `/blog/architecture/transformation-of-varanasi-urban-architecture` returns 200 with the full article and a self-referencing canonical.
- [ ] `/blog/architecture/<nonexistent-slug>` returns HTTP 404 with the branded 404 page.
- [ ] `/course/<nonexistent-slug>` returns HTTP 404.
- [ ] No route in the list above can return a 200 with an empty `<body>`.

### Verify

```bash
# must be 200 with content, currently 200 blank
curl -s "https://www.kaarwan.com/blog/architecture/transformation-of-varanasi-urban-architecture" \
  | grep -o '<title>[^<]*</title>'

# must be 404, currently 200
curl -so /dev/null -w '%{http_code}\n' \
  "https://www.kaarwan.com/blog/architecture/this-slug-does-not-exist-98765"
curl -so /dev/null -w '%{http_code}\n' \
  "https://www.kaarwan.com/course/this-course-does-not-exist-98765"
```

---

## KAAR-104 — Regenerate sitemap.xml from canonical URLs

**Type:** Bug · **Priority:** P0 · **Est:** 2 days · **Owner:** Backend
**Runs in parallel with:** KAAR-101

### Problem

**1,105 of 2,246 sitemap URLs (49.2%) are not the canonical URL of the page they reference.**

The `category` field stores nine casings of four categories. The sitemap writes the raw stored value; the application normalises to lowercase-hyphenated. Internal links use the normalised form, so the sitemap and internal linking disagree for 1,105 pages.

| Stored value | Records | URL behaviour |
|---|---|---|
| `architecture` | 985 | canonical |
| `Architecture` | 729 | 308 redirect |
| `ui-ux design` | 106 | 200, live duplicate (canonicals to hyphen form) |
| `UI-UX Design` | 105 | 308 to space form, which is itself non-canonical |
| `UI-UX design` | 80 | 308 to space form |
| `engineering` | 81 | canonical |
| `interior design` | 69 | 200, live duplicate |
| `Engineering` | 12 | 308 redirect |
| `Interior Design` | 4 | 308 to space form |

Additional defects in the same file:

- **2,017 of 2,246 URLs claim `lastmod` = the generation date.** Google discounts `lastmod` entirely once it looks auto-stamped.
- `priority` is `0.7` on 2,232 of 2,246 URLs. Google ignores `priority` and `changefreq`; both can be dropped.
- Three robots-disallowed URLs are listed: `/dashboard/resources` and `/dashboard/referral/how-it-works`, the latter twice.
- **No `/course/aec/` URL appears at all**, despite those being the clean, working, parameter-free course pages.
- 382 `<loc>` values contain a literal unencoded space.

### Scope

1. Normalise `category` in the database to four values: `architecture`, `engineering`, `interior-design`, `ui-ux-design`. Migration, not a display-time transform.
2. Regenerate the sitemap from canonical URLs only. Assert `loc == canonical` for every entry.
3. Emit real content-modified timestamps as `lastmod`. Omit the field where no reliable value exists.
4. Drop `priority` and `changefreq`.
5. Exclude anything disallowed in `robots.txt`.
6. Include `/course/aec/` URLs.
7. Add a build-time guard that fails CI if any `loc` returns a non-200, or differs from that page's canonical.

### Acceptance criteria

- [ ] Zero `<loc>` values contain an uppercase character in the path or a literal space.
- [ ] Every `<loc>` returns HTTP 200 with no redirect.
- [ ] Every `<loc>` equals the canonical emitted by that page.
- [ ] `lastmod` values reflect real modification dates; fewer than 10% share any single date.
- [ ] No robots-disallowed path is present.
- [ ] `/course/aec/` URLs are present.
- [ ] Sitemap contains no duplicate `<loc>`.

### Verify

```bash
curl -s https://www.kaarwan.com/sitemap.xml > s.xml

# all four must be 0
grep -o '<loc>[^<]*</loc>' s.xml | grep -c '/blog/[A-Z]'
grep -o '<loc>[^<]*</loc>' s.xml | grep -c ' '
grep -o '<loc>[^<]*</loc>' s.xml | grep -cE '/(dashboard|auth|payments|admin)/'
grep -o '<loc>[^<]*</loc>' s.xml | sort | uniq -d | wc -l

# must be > 0
grep -c '/course/aec/' s.xml

# lastmod must not be dominated by one date
grep -o '<lastmod>[^<]*</lastmod>' s.xml | sort | uniq -c | sort -rn | head -3
```

---

## KAAR-105 — 301 the `/blogs/` path and consolidate course URL patterns

**Type:** Bug · **Priority:** P0 · **Est:** 2 days · **Owner:** Backend
**Depends on:** KAAR-101

### Problem

**Plural blog path.** Both `/blog/` and `/blogs/` return 200 for the same article, and both are indexed. Confirmed for IDs 206, 80 and 270.

**Five competing course URL patterns.** For `advance-revit-bim-certification-course`:

| URL | Status | Canonical | Schema | In sitemap |
|---|---|---|---|---|
| `/course/<slug>?id=36` | 200 | itself | `Product` | yes |
| `/course/aec/<slug>` | 200 | **itself** | none | **no** |
| `/course/offer/<slug>` | 200 | → `/course/<slug>?id=36` | none | yes |
| `/course/<slug>` | 200 | none | none | no |
| `/masterclass/<slug>`, `/case-studies/<slug>` | 200 | varies | none | some |

`/course/offer/` consolidates correctly. The problem is `/course/aec/`: it self-canonicalises, renders 1,975 words with no parameter needed, has a different title and H1, and is absent from the sitemap. Two self-canonical URLs compete for the same course, and the better-built one is invisible to Google.

### Decision required from the client before implementation

Confirm `/course/aec/<slug>` as the canonical pattern. It is the recommendation: it works without `?id=`, has cleaner copy, and needs no parameter handling. The tradeoff is that the `Product` schema and any existing backlink equity currently sit on `/course/<slug>?id=N`, so the redirects must be correct.

### Scope

1. 301 `/blogs/*` to `/blog/*`.
2. 301 `/course/<slug>`, `/course/offer/<slug>`, `/case-studies/<slug>` and `/masterclass/<slug>` to `/course/aec/<slug>` where they describe the same course.
3. Port structured data to `/course/aec/`, converting `Product` to `Course` + `CourseInstance` (see KAAR-2xx, Phase 2).
4. Change the apex-to-www redirect from **302** to **301**.
5. Fix parameter stripping, which is currently order-dependent: `?id=407&extra=1` correctly 308s, but `?preview=true&id=418` returns 200 and is indexed, as does an `fbclid` variant.
6. Update the URLs in `llms.txt`, which currently point at apex (`https://kaarwan.com/...`) and therefore all redirect.

The full from/to list is in the **Redirect Map** sheet of `kaarwan-seo-audit-2026-08-14.xlsx`, 1,235 rows with priority, owning team and current status per row. Note that it distinguishes rows that already redirect and only need removing from the sitemap (741) from rows that return 200 and need a new 301 (364).

### Acceptance criteria

- [ ] `/blogs/architecture/a-comprehensive-guide-to-architecture-thesis?id=206` returns 301 to the `/blog/` equivalent.
- [ ] All course URL variants return single-hop 301 to `/course/aec/<slug>`.
- [ ] `https://kaarwan.com/...` returns 301, not 302.
- [ ] `?preview=true`, `?fbclid=`, `?trk=` and `?ref=` are stripped regardless of parameter order.
- [ ] No redirect chain exceeds one hop.
- [ ] `llms.txt` URLs all return 200 with no redirect.

### Verify

```bash
# must be 301, currently 200
curl -sI "https://www.kaarwan.com/blogs/architecture/a-comprehensive-guide-to-architecture-thesis?id=206" | head -1

# must be 301 to /course/aec/..., currently 200 self-canonical
curl -sI "https://www.kaarwan.com/course/advance-revit-bim-certification-course?id=36" \
  | grep -Ei '^(HTTP|location)'

# must be 301, currently 302
curl -sI "https://kaarwan.com/" | head -1

# must be 301, currently 200 and indexed
curl -sI "https://www.kaarwan.com/blog/architecture/craft-perfect-bim-resume?preview=true&id=418" | head -1

# every llms.txt URL must be 200 with 0 redirects
curl -s https://www.kaarwan.com/llms.txt | grep -o 'https://[^)]*kaarwan.com[^) ]*' | sort -u \
  | while read u; do printf '%s %s %s\n' \
      "$(curl -so /dev/null -w '%{http_code}' "$u")" \
      "$(curl -so /dev/null -w '%{num_redirects}' "$u")" "$u"; done
```

---

## Sprint exit criteria

The sprint is done when all of the following hold on production:

1. `curl` with no JavaScript returns full title, canonical, H1 and body for any article or course URL.
2. A fabricated slug with a valid `?id=` returns 301, not 200.
3. A parameter-less article URL renders the article.
4. A nonexistent slug returns 404.
5. `sitemap.xml` contains only canonical, 200-status URLs with real `lastmod` values.
6. `/blogs/` and all redundant course patterns return single-hop 301s.
7. GPTBot, ClaudeBot and PerplexityBot receive full article text.

### Post-deploy monitoring

- Submit the regenerated sitemap in GSC and watch the Pages report for two weeks. Expect "Discovered, not indexed" and "Duplicate without user-selected canonical" counts to fall.
- Run URL Inspection live tests on: one article, `/blog/architecture/design-architecture-of-taj-mahal?id=62`, and one course URL.
- Watch CrUX mobile LCP. If KAAR-101 lands cleanly, expect movement on LCP and FCP within 28 days, since render delay currently accounts for roughly 90% of mobile LCP.
- Separately, identify the deploy between **29 Mar and 16 May 2026** that broke LCP, FCP, INP and CLS. That regression is independent of this sprint's work and needs its own investigation (Phase 2).

### Out of scope for Phase 1

Category hub pages, the randomised related-posts query, structured data, the `aggregateRating` mismatch, the Medium subdomain, slug sanitisation, and the analytics consolidation. All are scheduled in Phases 2 and 3 in the main audit document.
