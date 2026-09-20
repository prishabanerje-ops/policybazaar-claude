# Author / Reviewer Byline Coverage — Health & Travel BU

**Date:** 2026-07-31
**Reference ticket:** PUP-6446 (Car Insurance, In Backlog)
**Method:** live crawl of `policybazaar.ae` XML sitemaps, then HTML + JSON-LD parse of every URL
**Scope rule used:** any page carrying editorial content (per Aakash). Verified: every page in scope has 908+ words, so no page was excluded on content grounds.

## Data provenance

Everything below is measured from live pages fetched on 2026-07-31. No sampling, no extrapolation.

| Item | Value |
|---|---|
| Sitemaps parsed | `sitemap-health-insurance.xml`, `sitemap-travel-insurance.xml`, `sitemap-group-health-insurance.xml`, `sitemap-critical-illness.xml` |
| URLs crawled | 1,537 |
| HTTP 200 | 1,537 (100%, zero fetch failures) |
| Word count range | min 908, median 2,763, max 8,857 |

Raw per-URL data: `byline-gap-inventory-2026-07-31.csv`
Per-page-type rollup: `byline-pagetype-rollup-2026-07-31.csv`

## Headline finding

The byline pattern PUP-6446 asks for **already exists in production on 26 pages**, including 2 Travel pages and 21 Health pages. This is not a greenfield build. It is a rollout of an existing component plus a schema fix.

That changes the ticket from "design and add bylines" to "extend component A to the remaining page types, and retire component B".

## Three different states exist today

| Component | Markup | Visible "Written By" | Visible "Reviewed By" | JSON-LD `author` | JSON-LD `reviewedBy` | Pages |
|---|---|---|---|---|---|---|
| **A** (current standard) | `author-reviewer-label` / `-name` / `-designation` | Yes | Yes | Yes | Yes | 26 |
| **B** (legacy) | `pro--text` / `pro--name` | Yes | Yes | Yes | **No** | 13 |
| **C** (author only) | `author-card` | No label | **No reviewer at all** | Yes | No | 342 |
| none | — | No | No | No | No | 1,156 |

Component A is the target state. It renders a reviewer name plus designation, for example "Reviewed By / Toshita Chauhan / Business Head - General Insurance", and emits matching `reviewedBy` in the `Article` JSON-LD.

Component C is the widest deployment. It shows an author card with name, role, description and a link to the author profile, and emits `author` in JSON-LD, but has no reviewer concept and no "Written by" label.

## Coverage by BU

| BU | Total | A (compliant) | B (no schema) | C (author only) | Nothing |
|---|---|---|---|---|---|
| Health | 1,064 | 21 | 13 | 261 | 769 |
| Travel | 435 | 2 | 0 | 75 | 358 |
| Group Health | 27 | 3 | 0 | 6 | 18 |
| Critical Illness | 11 | 0 | 0 | 0 | 11 |
| **Total** | **1,537** | **26** | **13** | **342** | **1,156** |

## Work required

| BU | Needs "Written By" | Needs "Reviewed By" | Needs schema `author` | Needs schema `reviewedBy` |
|---|---|---|---|---|
| Health | 1,030 | 1,030 | 769 | 1,043 |
| Travel | 433 | 433 | 358 | 433 |
| Group Health | 24 | 24 | 18 | 24 |
| Critical Illness | 11 | 11 | 11 | 11 |

## Reviewers already assigned in production

Read from live JSON-LD, not assumed:

| BU | Reviewer | Designation shown | Pages |
|---|---|---|---|
| Health | Toshita Chauhan | Business Head - General Insurance | 20 |
| Health | Toshita Chauhan **Balochi** | (same person, inconsistent name string) | 1 |
| Group Health | Ashu Bajaj | Business Head - Commercial and Group Health Insurance | 3 |
| Travel | Richa Bansal | Business Development Manager- **Home Insurance** | 2 |

The Travel reviewer's designation says Home Insurance. On a travel page that is a topical mismatch and works against the E-E-A-T intent. Either the designation is wrong or the reviewer assignment is.

**Writer already established for both BUs:** Mousree Das, "Senior Content Writer (Expertise - Health and Travel Insurance)". This is the author on both the Health and Travel product landings and on all 26 component A pages. It is the natural default for both tickets.

Authors in use across Health + Travel, by page count: Laxita Gautam 209, Mousree Das 65, Nupur Jain 44, Atul Yadav 15, Ruchi Gohri 14, Chanchal Singh 11, Abhimanyu Chaturvedi 8, Shivam Sharma 7, Pratima Singh 5, Sandipan Sen 2, Aashima Mongia 1.

**Component A also renders an expandable bio popup** (`author-reviewer-popup`, `role="tooltip"`) containing the avatar, name, designation and a link through to the author profile. Any rollout inherits that popup, which is why the missing profile pages below matter.

## Blockers and defects found

These need a decision or a separate ticket. Listed because they will break the E-E-A-T benefit if shipped as-is.

1. **Neither reviewer has an author profile page.** `/author/toshita-chauhan-balochi/` and `/author/richa-bansal/` both return HTTP 200 but serve the generic "Meet Our Authors" hub with no H1, byte-equivalent to deliberately fake slugs I tested as controls (787,793 and 787,889 bytes respectively). Confirmed by comparison, not inferred. Neither name appears among the 16 profiles linked from `/author/`. A `reviewedBy` plus a bio popup pointing at a non-existent profile gives Google a dead entity.

2. **`/author/*` soft-404s.** Any nonexistent author slug returns 200 with the hub page. `/author/zzz-definitely-not-a-real-author-9999/` proved this. Should 404 or 301.

3. **Author profile pages are not in any sitemap.** No `author` entry exists in `sitemap.xml` or any child sitemap. The 16 existing profiles are effectively orphaned from discovery.

4. **Author page titles are inconsistent.** Only 3 of 16 declare expertise in the title tag (Nupur Jain "Motor Insurance", Chanchal Singh "Business Insurance & Group Health Insurance", Aashima Mongia "Life, Term & I..."). The other 13, including Laxita Gautam who authors 209 pages, serve the generic "Meet Our Authors" title.

5. **Name string inconsistency.** "Toshita Chauhan" on 20 pages vs "Toshita Chauhan Balochi" on 1. PUP-6446 specifies the longer form. One must be canonical.

6. **13 pages show a reviewer visually but emit no `reviewedBy` schema** (component B, includes 3 Arabic pages). The UI claims review, the structured data does not.

7. **Arabic pages excluded from the reviewer schema entirely.** 31 `ar-ae` Health pages and 1 Travel page. 3 use component B, 28 have nothing.

## Decisions taken (Aakash, 2026-07-31)

1. **Preserve existing authors. Add the reviewer everywhere.** Where a page already has a real author, that attribution stays. Only pages with no author get Mousree Das assigned. This deliberately diverges from PUP-6446, which collapses all Car pages to a single writer. Rationale: overwriting 381 genuine attributions with one name works against the E-E-A-T goal the ticket exists to serve.
2. **Critical Illness and Group Health get their own tickets**, not folded into Health.

Author counts under this policy:

| BU | Total | Keep existing author | Assign author | Add reviewer |
|---|---|---|---|---|
| Health | 1,064 | 295 | 769 | 1,043 |
| Travel | 435 | 77 | 358 | 433 |
| Group Health | 27 | 9 | 18 | 24 |
| Critical Illness | 11 | 0 | 11 | 11 |

---

# Jira draft 1 — Health

**Title:** Add "Written by" and "Reviewed by" Bylines Across All Health Insurance Page Types to Improve E-E-A-T

**Description**

To strengthen the E-E-A-T (Experience, Expertise, Authoritativeness, and Trustworthiness) signals across the Health Insurance section, extend the existing author and reviewer byline component to all Health Insurance page types that carry editorial content.

This mirrors PUP-6446 (Car Insurance). Note that the component already exists in production: 21 Health pages render it correctly today. This ticket is a rollout, not a new build.

**Requirements**

- Roll out byline component A (`author-reviewer-label` / `author-reviewer-name` / `author-reviewer-designation`) to all Health page types listed below.
- Each page must render a visible "Written By" label with author name and designation, and a visible "Reviewed By" label with reviewer name and designation.
- Each page must emit matching `author` and `reviewedBy` in the `Article` / `WebPage` JSON-LD.
- Migrate the 13 pages using legacy component B (`pro--text` / `pro--name`) to component A so they emit `reviewedBy` schema.
- Reviewer for Health: **Toshita Chauhan**, Business Head - General Insurance. Standardise the name string (currently 20 pages say "Toshita Chauhan", 1 says "Toshita Chauhan Balochi").
- **Author policy: do not overwrite existing authors.** 295 Health pages already carry a real author in JSON-LD. Those attributions must be preserved exactly as-is. Only the 769 pages with no author get one assigned, default **Mousree Das**, "Senior Content Writer (Expertise - Health and Travel Insurance)".
- This differs from PUP-6446 by design. Do not collapse Health pages to a single writer.

**Page types in scope (1,064 pages, 1,030 need bylines)**

| Page type | Pages | Already compliant | Need byline |
|---|---|---|---|
| `/health-insurance/articles/` | 293 | 14 | 269 |
| `/health-insurance/<insurer>-<plan>` product pages | 263 | 1 | 262 |
| Root legacy articles (`-hiart`) | 119 | 3 | 116 |
| `/health-insurance/hospitals/` | 104 | 0 | 104 |
| `/network-hospitals/` directory | 96 | 0 | 96 |
| `/health-insurance/news-and-update/` | 43 | 2 | 41 |
| `/ar-ae/` Arabic Health pages | 31 | 0 | 28 |
| `/health-insurance/glossary/` | 19 | 0 | 19 |
| `/health-insurance/health-guide/` | 16 | 0 | 16 |
| Podcast pages | 16 | 0 | 16 |
| Root claim forms (`-hicf`) | 14 | 0 | 14 |
| Root insurer plan detail (`-hipvd`) | 12 | 0 | 12 |
| Insurer company pages | 12 | 0 | 12 |
| Root `news-and-update` | 11 | 0 | 11 |
| Root health category (`-hic`) | 4 | 0 | 4 |
| `/health-insurance/tpa/` | 4 | 0 | 4 |
| Root network hospital (`-hinh`) | 3 | 0 | 3 |
| Root other | 3 | 0 | 3 |
| Root product landing `/health-insurance/` | 1 | 1 | 0 |

**Dependencies**

- Author profile page for the reviewer must exist before `reviewedBy` ships. `/author/toshita-chauhan-balochi/` currently soft-404s.
- Related defects to raise separately: `/author/*` soft-404 behaviour, author pages missing from sitemap, generic title tags on 13 of 16 author profiles.

**Full URL list:** `docs/byline-gap-inventory-2026-07-31.csv`, filter `bu = HEALTH`.

---

# Jira draft 2 — Travel

**Title:** Add "Written by" and "Reviewed by" Bylines Across All Travel Insurance Page Types to Improve E-E-A-T

**Description**

To strengthen the E-E-A-T (Experience, Expertise, Authoritativeness, and Trustworthiness) signals across the Travel Insurance section, extend the existing author and reviewer byline component to all Travel Insurance page types that carry editorial content.

This mirrors PUP-6446 (Car Insurance). The component already renders correctly on 2 Travel pages (`/travel-insurance/` and `/schengen-travel-insurance-tic/`), so those two are the reference implementation.

**Requirements**

- Roll out byline component A (`author-reviewer-label` / `author-reviewer-name` / `author-reviewer-designation`) to all Travel page types listed below.
- Each page must render a visible "Written By" label with author name and designation, and a visible "Reviewed By" label with reviewer name and designation.
- Each page must emit matching `author` and `reviewedBy` in the `Article` / `WebPage` JSON-LD.
- Reviewer for Travel: **Richa Bansal**. The 2 live pages render her designation as "Business Development Manager- Home Insurance", which is the wrong vertical for a travel page. Correct the designation or reassign the reviewer before rollout.
- **Author policy: do not overwrite existing authors.** 77 Travel pages already carry a real author in JSON-LD. Those attributions must be preserved exactly as-is. Only the 358 pages with no author get one assigned, default **Mousree Das**, "Senior Content Writer (Expertise - Health and Travel Insurance)".
- This differs from PUP-6446 by design. Do not collapse Travel pages to a single writer.
- Travel has zero pages on legacy component B, so no migration work is needed here.

**Page types in scope (435 pages, 433 need bylines)**

| Page type | Pages | Already compliant | Need byline |
|---|---|---|---|
| `/travel-insurance/articles/` | 256 | 0 | 256 |
| `/travel-insurance/travel-insurance-<country>` destination landings | 76 | 0 | 76 |
| `/travel-insurance/news-and-update/` | 42 | 0 | 42 |
| `/travel-insurance/<x>-visa` visa landings | 13 | 0 | 13 |
| `/travel-insurance/` other subpages | 13 | 0 | 13 |
| Insurer company pages | 11 | 0 | 11 |
| Root `news-and-update` | 7 | 0 | 7 |
| Podcast pages | 6 | 0 | 6 |
| Root travel plan detail (`-tipvd`) | 4 | 0 | 4 |
| Root other | 3 | 0 | 3 |
| `/ar-ae/` Arabic Travel page | 1 | 0 | 1 |
| CEO blog | 1 | 0 | 1 |
| Root travel category (`-tic`) | 1 | 1 | 0 |
| Root product landing `/travel-insurance/` | 1 | 1 | 0 |

**Dependencies**

- Author profile page for Richa Bansal must exist before `reviewedBy` ships. Not present in the 16 profiles listed on `/author/`.
- Same shared defects as the Health ticket: `/author/*` soft-404, author pages missing from sitemap.

**Full URL list:** `docs/byline-gap-inventory-2026-07-31.csv`, filter `bu = TRAVEL`.

---

# Jira draft 3 — Group Health

**Title:** Add "Written by" and "Reviewed by" Bylines Across All Group Health Insurance Page Types to Improve E-E-A-T

**Description**

To strengthen the E-E-A-T (Experience, Expertise, Authoritativeness, and Trustworthiness) signals across the Group Health Insurance section, extend the existing author and reviewer byline component to all Group Health page types that carry editorial content.

Component A already renders correctly on 3 Group Health pages, so the reviewer and designation strings are established. This is the smallest of the four rollouts.

**Requirements**

- Roll out byline component A (`author-reviewer-label` / `author-reviewer-name` / `author-reviewer-designation`) to all Group Health page types below.
- Visible "Written By" and "Reviewed By" labels with name and designation, plus matching `author` and `reviewedBy` in the `Article` / `WebPage` JSON-LD.
- Reviewer: **Ashu Bajaj**, Business Head - Commercial and Group Health Insurance.
- **Author policy: do not overwrite existing authors.** 9 pages already carry a real author (Chanchal Singh on several). Preserve those. Assign an author to the remaining 18.
- No legacy component B pages in this BU, so no migration work.

**Page types in scope (27 pages, 24 need bylines)**

| Page type | Pages | Already compliant | Need byline |
|---|---|---|---|
| `/group-health-insurance/articles/` | 17 | 2 | 15 |
| Insurer company pages | 8 | 0 | 8 |
| Podcast | 1 | 0 | 1 |
| Root health category (`-hic`) | 1 | 1 | 0 |

**Dependencies**

- Confirm `/author/ashu-bajaj/` exists before shipping the bio popup. Ashu Bajaj is not among the 16 profiles linked from `/author/`.
- Shared defects: `/author/*` soft-404, author pages missing from sitemap.

**Full URL list:** `docs/byline-gap-inventory-2026-07-31.csv`, filter `bu = GROUP_HEALTH`.

---

# Jira draft 4 — Critical Illness

**Title:** Add "Written by" and "Reviewed by" Bylines Across All Critical Illness Page Types to Improve E-E-A-T

**Description**

To strengthen the E-E-A-T (Experience, Expertise, Authoritativeness, and Trustworthiness) signals across the Critical Illness section, add the author and reviewer byline component to all Critical Illness page types that carry editorial content.

Critical Illness has zero coverage today. No page in this vertical has a visible byline, a JSON-LD `author`, or a `reviewedBy`. It is the only one of the four verticals starting from nothing, and it is YMYL content, so it carries the highest E-E-A-T risk relative to its size.

**Requirements**

- Roll out byline component A (`author-reviewer-label` / `author-reviewer-name` / `author-reviewer-designation`) to all 11 pages.
- Visible "Written By" and "Reviewed By" labels with name and designation, plus matching `author` and `reviewedBy` in the `Article` / `WebPage` JSON-LD.
- **Reviewer: needs to be assigned.** No reviewer exists anywhere in this vertical. Toshita Chauhan (Business Head - General Insurance) is the closest existing fit, but this is a product decision, not a technical one.
- Author: assign to all 11 pages. No existing attributions to preserve.

**Page types in scope (11 pages, all 11 need bylines)**

| Page type | Pages | Already compliant | Need byline |
|---|---|---|---|
| `/critical-illness/articles/` | 5 | 0 | 5 |
| Insurer company pages | 4 | 0 | 4 |
| `/critical-illness/` plan/product page | 1 | 0 | 1 |
| Root product landing `/critical-illness/` | 1 | 0 | 1 |

**Dependencies**

- Reviewer assignment decision, plus a profile page for whoever is chosen.
- Shared defects: `/author/*` soft-404, author pages missing from sitemap.

**Full URL list:** `docs/byline-gap-inventory-2026-07-31.csv`, filter `bu = CRITICAL_ILLNESS`.

---

# Suggested fifth ticket — author infrastructure

The four rollout tickets all depend on this, so it should land first or in parallel. Raising as a separate item because it is platform work, not BU content work.

- Create profile pages for the reviewers: Toshita Chauhan, Richa Bansal, Ashu Bajaj. None of the three exist. All three currently soft-404.
- Fix `/author/*` to return 404 or 301 for unknown slugs instead of 200 with the hub page.
- Add author profile pages to a sitemap. Currently no `author` URL appears in `sitemap.xml` or any child sitemap.
- Fix the generic `<title>` on 13 of 16 author profiles. Only Nupur Jain, Chanchal Singh and Aashima Mongia declare expertise. Laxita Gautam authors 209 pages and serves the generic "Meet Our Authors" title.
- Correct Richa Bansal's designation, which reads "Business Development Manager- Home Insurance" on Travel pages.
- Standardise the Toshita Chauhan name string. 20 pages say "Toshita Chauhan", 1 says "Toshita Chauhan Balochi", PUP-6446 specifies the longer form.
