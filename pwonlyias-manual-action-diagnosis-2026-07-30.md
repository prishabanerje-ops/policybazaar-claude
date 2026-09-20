# pwonlyias.com — Manual Action Diagnosis

**Action:** "Thin content with little or no added value" — site-wide (`Affects all pages`)
**Notified:** 30 Jul 2026
**Audit date:** 30 Jul 2026
**Method:** public crawl only (no GSC/GA4 access) — 161 sitemaps parsed, 29,754 URLs mapped, 790 pages fetched as Googlebot, key templates render-tested in Playwright + Chrome DevTools

---

## Verdict

The action is explained by content problems that are **structural and template-level**, not article-level. Individual articles are mostly fine. Entire URL classes are not.

Three findings carry the case, in order of severity:

1. **~1,270 `/books/` URLs whose entire body content is the placeholder string `chjdsbhjdbfhrb`.** Confirmed on 199 of 200 fetched pages. All are `index, follow`, self-canonical, and submitted in the sitemap.
2. **1,116 `/upsc-notes/` URLs that are 88% identical boilerplate** — a byte-identical 9,339-word sidebar index repeats on every page. ~10.4M words of duplicated text.
3. **762 `/news-headline/` URLs that are digests of other publishers' reporting** (The Hindu, Indian Express, PIB, Live Mint, Economic Times), self-declared on the page, marked up with `NewsArticle` schema.

Together these are ~3,150 URLs, about 11% of the indexable site. That is enough surface area for a site-wide action, and #1 alone is the kind of thing a manual reviewer needs about ten seconds to find.

---

## 1. `/books/` — placeholder text at scale — **CRITICAL**

The single most damaging finding.

| Measure | Value |
|---|---|
| URLs in sitemap | 1,276 |
| Fetched and checked | 200 |
| Containing `chjdsbhjdbfhrb` | **199 (99.5%)** |
| Median unique body words | **7** |
| Max unique body words | 19 |
| HTTP status | 200 across all 200 |
| Meta robots | `follow, index` on all |
| Canonical | self-referencing on all |

The complete rendered content of a representative page:

```
URL   : https://pwonlyias.com/books/prahaar-indian-economy-2022/
Title : PRAHAAR INDIAN ECONOMY - PWOnlyIAS
H1    : PRAHAAR INDIAN ECONOMY
Body  : PRAHAAR INDIAN ECONOMY chjdsbhjdbfhrb PRAHAAR INDIAN ECONOMY
PDF   : none      Download: none      Description: none
```

`chjdsbhjdbfhrb` is keyboard-mash placeholder text. It was typed into a template field, never replaced, and shipped to ~1,270 live indexable URLs. Verified in both raw HTML and full browser render — it is not a rendering artifact.

The template also contains junk entries that were never real books:

- `/books/singing/` → H1 "Singing"
- `/books/football/` → H1 "Football"
- `/books/kerala/` → H1 "Kerala"
- `/books/csat/`, `/books/04-november/`, `/books/22-august-2025/`

Near-duplicate analysis returned **300 of 300 possible pairs** above Jaccard 0.5 within this template — because after boilerplate removal there is almost nothing left to differentiate them.

---

## 2. `/upsc-notes/` — 88% duplicate boilerplate per page — **CRITICAL**

Measured across 137 pages fetched at scale:

| Measure | Value |
|---|---|
| URLs live | 1,116 |
| Median full-body words | 11,053 |
| Median actual article words | 1,294 |
| **Median unique-content ratio** | **11.7%** |
| Repeated sidebar block | 9,339 words |
| Distinct sidebar blocks across 137 pages | **1** |

Every note page renders the same 9,339-word `betterdocs-sidebar` listing every other note on the site. The genuine article sits in `.betterdocs-entry-content` and is a fraction of the page.

The thinnest examples — each page self-declares `< 1 min read`:

| Article words | Body words | Unique | URL |
|---|---|---|---|
| 22 | 9,753 | 0.2% | `/upsc-notes/physical-geography/` |
| 23 | 9,764 | 0.2% | `/upsc-notes/environment-udaan/` |
| 26 | 9,769 | 0.3% | `/upsc-notes/budget-and-taxation/` |
| 34 | 9,768 | 0.3% | `/upsc-notes/agreements/` |
| 37 | 9,770 | 0.4% | `/upsc-notes/part-ix-non-constitutional-bodies/` |
| 40 | 9,773 | 0.4% | `/upsc-notes/post-independence-history-of-india/` |

There is also an H1 conflict: every page's first `<h1>` is the BetterDocs search widget label **"How can we help you?"**, with the actual topic demoted to a second `<h1>`. 1,116 pages share the same primary H1.

---

## 3. `/news-headline/` — third-party news aggregation — **HIGH**

762 URLs, one per day, titled `News of The Day – <date>`. All 30 sampled pages carry an explicit source line:

> "Sources: The Hindu, Indian Express, Live Mint, Business Standard, Economic Times, and PIB."

The body is a table of other publishers' headlines with brief summaries — median 463 unique words. 30/30 sampled pages match this pattern.

Two compounding problems:

- These pages carry **`NewsArticle` schema** (120 pages in the sample), presenting aggregated third-party reporting as original news.
- `robots.txt` has `Disallow: /news-headline/*`, yet **all 762 are submitted in the sitemap**. The site is simultaneously telling Google not to crawl them and asking it to index them.

---

## 4. Thin-content census across the site

Extrapolated from measured per-template rates. "Thin" = under 500 words of genuine article content, except `/books/` (placeholder rate) and `/upsc-notes/` (all pages structurally duplicative).

| Template | Live URLs | Sampled | Median article words | Unique ratio | Est. thin URLs |
|---|---|---|---|---|---|
| current-affairs | 8,523 | 55 | 556 | 55.4% | 3,874 |
| mains-answer-writing | 6,242 | 55 | 745 | 61.9% | 907 |
| (root-level) | 3,325 | 25 | 904 | 52.4% | 532 |
| editorial-analysis | 3,112 | 40 | 678 | 57.1% | 466 |
| **books** | **1,276** | **225** | **7** | **~0%** | **1,269** |
| **upsc-notes** | **1,116** | **167** | **1,294** | **11.7%** | **1,116** |
| pyq | 1,079 | 35 | 427 | 46.4% | 739 |
| daily-quiz | 911 | 30 | 1,924 | 76.9% | 0 |
| current-affair-hindi | 801 | 20 | 930 | 66.6% | 160 |
| **news-headline** | **762** | **30** | **463** | **52.6%** | **457** |
| udaan | 711 | 25 | 701 | 60.8% | 199 |
| courses | 649 | 20 | 394 | — | 454 |
| ncert-notes | 606 | 25 | 906 | 66.5% | 24 |
| editorial-hindi | 367 | 15 | 759 | 64.5% | 0 |
| **Total** | **29,480** | **430+** | — | — | **~10,200 (35%)** |

The 35% figure is a soft signal — a 400-word current-affairs summary is defensible on its own. The hard cases are the bolded rows.

---

## 5. Secondary issues

These did not cause the action but weaken any reconsideration request.

### Structural

- **92 of 430 sampled pages have no `<h1>` at all** — 55/55 `/mains-answer-writing/` and 35/35 `/pyq/`. Both entire templates ship without an H1.
- **`/pyq/` slugs are full exam question texts** — 951 slugs over 100 characters. Example: `/pyq/ashok-is-divisional-commissioner-of-one-of-the-border-districts-of-the-north-east-state-a-few-years-back-military-has-taken-over-the-neighbouring-country-after-overthrowing-the-elected-civil-governm/`
- **Broken pages indexed** — e.g. `/pyq/216968-2/`: 0 words, title `- PWOnlyIAS`. 10 of 440 sampled URLs returned HTTP 410.
- **793 `-hindi` slug variants** in `/mains-answer-writing/`; 129 confirmed EN/HI pairs where both are indexed.
- **2,390 date-stamped serial URLs**, plus ~40 root-level `/daily-current-affairs-<date>/` pages duplicating `/current-affairs/` dated pages.

### robots.txt is largely non-functional

Rules block paths that do not exist, while real paths stay open:

| Directive | URLs it actually matches | Reality |
|---|---|---|
| `Disallow: /quiz/*` | 0 | Quizzes live at `/daily-quiz/` — **912 URLs, fully crawlable** |
| `Disallow: /hi/` | 0 | Hindi lives at `/current-affair-hindi/` (802) and `/editorial-hindi/` (367) |
| `Disallow: /tag/` | 0 | no such URLs |
| `Disallow: /author/` | 0 | no such URLs |
| `Disallow: /faq/` | 0 | no such URLs |
| `Disallow: /toppers/*` | 0 | no such URLs |
| `Disallow: /news-headline/*` | 762 | blocked **and** submitted in sitemap |

Lighthouse also flags `robots.txt is not valid`. Net: 786 URLs are blocked-but-submitted, and every URL class the owner intended to hide is still open.

### Lighthouse (mobile, snapshot mode)

| Category | Score |
|---|---|
| SEO | **50** |
| Accessibility | 79 |
| Best Practices | 100 |

SEO failures: links not crawlable (mega-menu `<a>` without `href`), `robots.txt` not valid, images missing `alt`.

### Not confirmed

Stated plainly because the brief asked for no guessing:

- **Mass AI-generated content — not confirmed.** Stock LLM filler phrases appear on under 1% of sampled pages ("aspirants have to know about" 3/430, "gives an idea of all the important topics" 4/430). The crawl gives no basis to call this AI-written.
- **Scraped content beyond news aggregation — not confirmed.** `/news-headline/` self-declares its sources. `/pyq/` reproduces UPSC exam questions, which is normal for the category. No evidence of scraping other coaching sites.
- **Which URLs Google actually indexed or flagged — unknown.** No GSC access. All index counts here are sitemap-declared, not confirmed-indexed.
- `/courses/` (649 URLs) initially measured as zero-content; on browser verification these carry ~394 median words of genuine course description. Thin but legitimate — **not** part of the case against the site.

---

## Remediation plan

Ordered by what a manual reviewer will check.

### Before requesting reconsideration

**1. `/books/` — 1,276 URLs.** Do not try to fix these with light edits.
   - Write real descriptions (150+ words: contents, syllabus coverage, edition, who it is for), **or**
   - Return HTTP 410 and remove from the sitemap, **or**
   - `noindex` and consolidate into a single catalogue page.
   - Delete the junk entries outright: `singing`, `football`, `kerala`, bare-date slugs.
   - Verify no page anywhere still contains `chjdsbhjdbfhrb`.

**2. `/upsc-notes/` — 1,116 URLs.** Remove the 9,339-word sidebar from the server-rendered DOM; load it behind interaction or cut it to a contextual list of 10–15 sibling notes. Fix the H1 — "How can we help you?" must not be the primary H1. Merge or `noindex` the sub-100-word stubs (`physical-geography`, `environment-udaan`, `budget-and-taxation`, `agreements`, and similar).

**3. `/news-headline/` — 762 URLs.** Decide one way and be consistent. Either `noindex` the archive and keep only a current landing page, or add substantive original analysis per entry. Remove `NewsArticle` schema from aggregated digests either way. Remove them from the sitemap while `Disallow` stays in robots.txt.

**4. Fix robots.txt.** Correct `/quiz/*` → `/daily-quiz/*` if quizzes are meant to be blocked. Drop the dead rules. Resolve the 786 blocked-but-submitted URLs.

**5. Sitemap hygiene.** Remove 410s, zero-content pages, and blocked paths. Regenerate all 161 files.

### Then

6. Add `<h1>` to `/mains-answer-writing/` and `/pyq/` templates (90 sampled pages, both templates fully affected).
7. Consolidate the ~40 root-level `/daily-current-affairs-<date>/` duplicates into `/current-affairs/`.
8. Audit the 129 EN/HI duplicate pairs — `hreflang` or consolidate.
9. Shorten `/pyq/` slugs; the 951 slugs over 100 characters serve no one.
10. Fix mega-menu links to use real `href` attributes.

### Reconsideration request

File only after the work is deployed and verifiable — Google explicitly rejects requests on unchanged sites. State what was wrong, the URL counts, what was done to each class, and give before/after example URLs. The `chjdsbhjdbfhrb` cleanup is the single strongest thing to lead with, because it is unambiguous, self-evidently a defect, and easy for a reviewer to spot-check.

Expect several weeks for review. Do not file twice.

---

## Method and limitations

**Tools:** curl as Googlebot (raw HTML), Python + BeautifulSoup/lxml (parsing, shingling), Playwright MCP (JS render verification), Chrome DevTools MCP (Lighthouse mobile).

**Coverage:** 161 sitemaps → 29,754 unique URLs mapped. 440-URL stratified sample across 15 templates (430 × HTTP 200, 10 × 410), plus 200 `/books/` and 150 `/upsc-notes/` deep samples. Total 790 pages fetched.

**Duplication method:** 8-gram shingles; shingles present on >30% of sampled pages classed as site-wide boilerplate and subtracted before Jaccard comparison.

**Limitations:** No GSC, GA4, or server logs. Index counts are sitemap-declared, not confirmed-indexed. Per-template rates are extrapolated from samples, not full crawls — the bolded rows in the census were verified at scale (200 and 137 pages respectively); the rest were not. No backlink or off-page analysis was performed, so a link-based cause cannot be excluded, though the notice text points squarely at content.
