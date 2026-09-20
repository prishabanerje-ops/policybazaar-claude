# Add "Written by" and "Reviewed by" Bylines Across All Health & Travel Insurance Page Types to Improve E-E-A-T

## Description

Roll out author and reviewer bylines to every Health and Travel page carrying editorial content, to strengthen E-E-A-T signals. Health includes Critical Illness.

Same intent as PUP-6446 (Car). Difference: the byline component already exists in production and renders correctly on 23 of these pages, so this is a rollout plus a schema fix, not a new build.

## Bylines

| BU | Written By | Reviewed By |
|---|---|---|
| Health (incl. Critical Illness) | [Mousree Das](https://www.policybazaar.ae/author/mousree-das/)<br>Senior Content Writer (Expertise - Health and Travel Insurance) | [Toshita Chauhan](https://www.policybazaar.ae/reviewer/toshita-chauhan/)<br>Business Head - General Insurance |
| Travel | [Mousree Das](https://www.policybazaar.ae/author/mousree-das/)<br>Senior Content Writer (Expertise - Health and Travel Insurance) | [Richa Bansal](https://www.policybazaar.ae/reviewer/richa-bansal/)<br>Business Development Manager- Home Insurance ⚠️ see blocker 1 |

## Scope

| BU | Pages | Need bylines |
|---|---|---|
| Health (incl. Critical Illness) | 1,075 | 1,041 |
| Travel | 435 | 433 |
| **Total** | **1,510** | **1,474** |

Current state of those 1,510: 23 correct · 13 visible reviewer but no schema · 336 author only · 1,138 nothing.

Author work: 1,138 pages get an author for the first time, 372 have their existing author replaced with Mousree Das.

Verified by live crawl of the Health, Travel and Critical Illness sitemaps on 2026-07-31. All 1,510 URLs returned HTTP 200 and carry 908+ words.

## Requirements

1. Roll out the existing byline component (`author-reviewer-label` / `author-reviewer-name` / `author-reviewer-designation`) to all page types below.
2. Render a visible **Written By** and **Reviewed By** label, each with name, designation and a link to the profile page.
3. Emit matching `author` and `reviewedBy` in the `Article` / `WebPage` JSON-LD. 1,487 pages need `reviewedBy`.
4. Migrate the 13 pages on the legacy `pro--` component so they emit `reviewedBy` schema.
5. **Set Mousree Das as Written By on all 1,510 pages**, matching the PUP-6446 single-writer model. This replaces the 372 existing author attributions (Laxita Gautam 209, Nupur Jain 44, Atul Yadav 15, Ruchi Gohri 14, Chanchal Singh 11, Abhimanyu Chaturvedi 8, Shivam Sharma 7, Pratima Singh 5, Sandipan Sen 2, Aashima Mongia 1). Update both the visible byline and the JSON-LD `author`.

## Page types in scope

**Health, incl. Critical Illness — 1,075 pages**
`/health-insurance/articles/` 293 · `<insurer>-<plan>` product pages 263 · root legacy articles `-hiart` 119 · `/health-insurance/hospitals/` 104 · `/network-hospitals/` 96 · `/health-insurance/news-and-update/` 43 · `/ar-ae/` Arabic 31 · `/glossary/` 19 · `/health-guide/` 16 · podcast 16 · claim forms `-hicf` 14 · insurer plan detail `-hipvd` 12 · insurer company pages 12 · root news-and-update 11 · `/critical-illness/articles/` 5 · CI insurer pages 4 · health category `-hic` 4 · `/tpa/` 4 · network hospital `-hinh` 3 · root other 3 · `/health-insurance/` landing 1 · `/critical-illness/` landing 1 · CI plan page 1

**Travel — 435 pages**
`/travel-insurance/articles/` 256 · destination landings `travel-insurance-<country>` 76 · `/news-and-update/` 42 · visa landings `<x>-visa` 13 · other subpages 13 · insurer company pages 11 · root news-and-update 7 · podcast 6 · plan detail `-tipvd` 4 · root other 3 · `/ar-ae/` Arabic 1 · CEO blog 1 · category `-tic` 1 · `/travel-insurance/` landing 1

## Blockers

1. **Richa Bansal's designation is the wrong vertical.** Reads "Business Development Manager- Home Insurance" on Travel pages and on her own reviewer page. Fix the designation or reassign the Travel reviewer.
2. **Duplicate reviewer entity — two live profile URLs for the same person.** Both are HTTP 200, self-canonical, with different H1s and body copy:
   - [`/reviewer/toshita-chauhan/`](https://www.policybazaar.ae/reviewer/toshita-chauhan/) — H1 "Toshita Chauhan", 1,122 words, linked from 20 pages
   - [`/reviewer/toshita-chauhan-balochi/`](https://www.policybazaar.ae/reviewer/toshita-chauhan-balochi/) — H1 "Toshita Chauhan Balochi", 983 words, linked from 1 page

   Pick one as canonical, 301 the other, and use a single name string across all bylines. PUP-6446 specifies the longer form. Splitting `reviewedBy` across two URLs divides the entity signal this ticket exists to build.

## Related defects (raise separately)

- Profile pages are in **no sitemap**. Checked all 38 child sitemaps: zero `/author/` or `/reviewer/` URLs.
- `/author/*` and `/reviewer/*` return HTTP 200 for any unknown slug instead of 404 or 301.
- Reviewer pages omit `jobTitle` from JSON-LD. `/author/mousree-das/` has it; both reviewer pages do not.
- 13 of 16 author profiles serve a generic `<title>`, including Laxita Gautam who authors 209 pages.
- After requirement 5, 10 author profiles lose all attribution within Health/Travel/CI. They may still be attributed on Car or other verticals, which this crawl did not cover. Worth a follow-up call on whether those profile pages stay published, and on whether the `/author/` hub still lists them.

## Reference

Per-URL list with action per page: `docs/byline-gap-inventory-2026-07-31.csv` (filter `bu`; `CRITICAL_ILLNESS` rows roll up into Health).
Page-type rollup: `docs/byline-pagetype-rollup-2026-07-31.csv`.
