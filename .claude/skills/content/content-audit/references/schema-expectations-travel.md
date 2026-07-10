# Schema Expectations — policybazaar.ae Travel Insurance URLs

**Scope: this file applies ONLY to policybazaar.ae travel-insurance URLs.** Health
pages use `schema-expectations-health.md`; other verticals fall back to the generic
checks in `seo-parameters.md` §10.

**Provenance:** built from live fetches on **2026-07-10** — 12 representative PB.ae
travel pages (one per page type below), JSON-LD extracted and inspected directly, plus
the site-wide conventions already verified in `schema-expectations-health.md` (whose
foundation rules, blocklist, and Google-feature status checks apply site-wide and are
restated here so this file stands alone). Re-verify against live pages if PB.ae
retemplates.

**How the auditor uses this file (extends §10's coverage check):**
1. Identify the page type from the URL pattern or page content; state the assumed page
   type in the report.
2. Compare the implemented `@graph` against the expected stack for that type.
   Expected-but-missing types, present-but-wrong types, any known bug (§ Bugs), and
   **any recommendation of a blocklisted type** are findings.
3. Check the site-wide foundation nodes on every page regardless of type.

**Legend:** ✅ = active Google rich result · 🤖 = no rich result; value is entity
understanding + AI-search (GEO) citations · ⚠️ = policy or validity risk — read the note.

---

## What travel pages implement TODAY (baseline, verified 2026-07-10)

Almost every travel page carries the same thin four-node graph:
`WebPage (name, url, description, inLanguage, speakable — no @id, no isPartOf, no
breadcrumb ref, usually no dates) · BreadcrumbList · FAQPage (on some types) ·
"Organization" pseudo-node named after the PAGE (e.g. "Travel Insurance") carrying the
boilerplate 4.7/41,800 AggregateRating + 6 reviews with non-ISO dates and a
parentOrganization pointing at an #organization @id that is never declared anywhere
on the page.`

Per-type observations:

| Page type (sample fetched) | Implemented today | Gap severity |
|---|---|---|
| Hub `/travel-insurance/` | WebPage (+dates, author→Person) · Breadcrumb · FAQPage(26) · Org pseudo-node | FAQ "questions" are benefit headings, not questions |
| Product-type (`single-trip-…`) | WebPage · Breadcrumb · FAQPage(12) · Org pseudo-node | No Service/OfferCatalog |
| Destination (`travel-insurance-uk`) | WebPage · Breadcrumb · FAQPage(4) · Org pseudo-node | No Service/areaServed |
| Visa (`france-visa`) | WebPage · Breadcrumb · Org pseudo-node — **NO FAQPage despite ~100 FAQ mentions on-page** | Missing FAQPage where content exists |
| Category (`schengen-…-tic`) | WebPage · Breadcrumb · FAQPage(11) · Org pseudo-node | Not CollectionPage, no ItemList |
| Provider (root `-tipvd` and `insurance-companies/`) | WebPage · Breadcrumb · FAQPage · Org pseudo-node | No insurer mainEntity — the page's actual subject is absent |
| Article (`articles/spain-schengen-visa`) | Article+WebPage (ISO dates ✓) · Breadcrumb | `mainEntityOfPage: "True"` bug; author → org @id (dangling); single 175×132 image |
| News (`news-and-update/umrah-insurance`) | WebPage · Breadcrumb · NewsArticle+WebPage (author → Person ✓) | **NO datePublished/dateModified at all** |
| Podcast | WebPage · Breadcrumb · BlogPosting+WebPage | Wrong type for intent (expect PodcastEpisode) |
| Calculator (`travel-insurance-calculator-uae`) | WebPage · Breadcrumb · Org pseudo-node | No WebApplication |
| Destination hub (`travel-insurance-by-destination`) | WebPage · Breadcrumb(2) · Org pseudo-node | Not CollectionPage, no ItemList of destinations |

---

## Page Type × Expected Schema Stack

| # | Page Type (URL signal) | Expected stack (every node in one `@graph`) |
|---|---|---|
| 1 | Hub (`/travel-insurance/`) | WebPage + speakable · BreadcrumbList ✅ · InsuranceAgency (site org, `@id`) ✅ · WebSite · Service → OfferCatalog → Offer 🤖 · FAQPage 🤖 (real questions) |
| 2 | Product-type (`single-trip-…`, `family-…`, `…-for-over-65` etc.) | WebPage · BreadcrumbList ✅ · Service (`serviceType`) → OfferCatalog 🤖 · FAQPage 🤖 |
| 3 | Destination (`travel-insurance-<place>`) | WebPage · BreadcrumbList ✅ · Service with `areaServed` → Country/City 🤖 · FAQPage 🤖 |
| 4 | Visa (`<place>-visa` under `/travel-insurance/`) | WebPage · BreadcrumbList ✅ · FAQPage 🤖 (the on-page FAQs — currently unmarked) · Service (Schengen/visa-compliant travel insurance) with `areaServed` → destination Country 🤖 |
| 5 | Category (root `-tic`) | CollectionPage · BreadcrumbList ✅ · Service (category-scoped) 🤖 · ItemList → plans on page 🤖 · FAQPage 🤖 |
| 6 | Provider (root `-tipvd` and `/insurance-companies/*-travel-insurance/`) | WebPage · BreadcrumbList ✅ · `mainEntity` → InsuranceAgency/Organization (THE INSURER, current post-rebrand name — Liva not RSA, GIG Gulf not AXA) 🤖 · AggregateRating on the insurer ✅⚠️ (only if PB genuinely collects reviews about that insurer) · ItemList → its travel plans 🤖 · FAQPage 🤖 |
| 7 | Articles (`/travel-insurance/articles/`) | Article ✅ · author → Person (real human, linked to author page — NOT the org node) · BreadcrumbList ✅ · FAQPage 🤖 · image array 16:9/4:3/1:1 ≥50K px · VideoObject ✅ (only if video embedded) |
| 8 | News (`news-and-update/`) | **NewsArticle** ✅ · author Person · **datePublished/dateModified (currently absent — always a finding)** · BreadcrumbList ✅ · speakable |
| 9 | Podcast (`/podcast/`) | WebPage · BreadcrumbList ✅ · PodcastEpisode → `partOfSeries` PodcastSeries (with `webFeed`) 🤖 · VideoObject ✅ if video / AudioObject 🤖 if audio-only — NOT BlogPosting |
| 10 | Calculator (`travel-insurance-calculator-uae`) | WebPage · BreadcrumbList ✅ · WebApplication ✅⚠️ (`applicationCategory: "FinanceApplication"`, `operatingSystem: "Web"`, offers price 0 AED; safest `@type: ["WebApplication","SoftwareApplication"]`) · FAQPage 🤖 |
| 11 | Destination hub (`travel-insurance-by-destination`) | CollectionPage · BreadcrumbList ✅ · ItemList → ListItem per destination page 🤖 · FAQPage 🤖 |

**Plan-detail template:** if travel plan pages emerge, follow the health file's
Plan Detail template with `@type: ["Product"]` + `brand` → insurer + `offers` (AED).
(`HealthInsurancePlan` is health-specific — don't copy it onto travel products.)

---

## Site-wide foundation (check on EVERY page — identical to health)

1. **InsuranceAgency** — ONE canonical node, `"@id": "https://www.policybazaar.ae/#organization"`,
   *referenced* (never re-declared) from every page. Travel pages currently reference
   this `@id` via `parentOrganization` without any page declaring it — a dangling
   reference; flag it.
2. **WebSite** — `"@id": ".../#website"`, `publisher` → `{"@id": "#organization"}`.
   **No SearchAction** (feature removed by Google Nov 2024; PB.ae has no on-site search).
3. **WebPage** (or subtype) — must have `@id`, url, name, description, `inLanguage`,
   `isPartOf` → #website, `breadcrumb` → breadcrumb `@id`, datePublished/dateModified,
   primaryImageOfPage. Travel WebPage nodes currently carry only
   name/url/description/inLanguage/speakable.
4. **BreadcrumbList** — on every page.

---

## Known bugs to grep for (verified in travel HTML, 2026-07-10)

**How to read this table:** the *Defect* column is what is wrong in the live pages'
JSON-LD **today**; *Evidence* is the exact markup found on the named sample page at
fetch date; *Fix (for dev team)* is the recommendation — it describes the target state,
NOT something already implemented.

| # | Defect (live today) | Evidence (sample page, 2026-07-10) | Fix (for dev team) |
|---|---|---|---|
| T1 | `mainEntityOfPage` is the string `"True"` instead of a URL/reference | `"mainEntityOfPage": "True"` on `articles/spain-schengen-visa/` | Set canonical URL or `{"@type":"WebPage","@id":"<url>"}` |
| T2 | The identical 4.7★/41,800 AggregateRating + same 6 reviews stamped on an "Organization" node that is **named after the page topic** — a page topic is not an Organization | Org node with `"name": "Travel Insurance"`, `ratingValue 4.7`, `reviewCount 41800` on the hub; same block on nearly all non-article pages | Remove the boilerplate block; ratings only on entities genuinely reviewed |
| T3 | Review dates are plain English, not machine-readable | `"datePublished": "12 February 2026"` in the review blocks | ISO-8601 (`2026-02-12`) |
| T4 | NewsArticle carries **no publish/modified date at all** — the properties are absent, so news pages have no freshness signal and can't qualify for News rich results | NewsArticle node on `news-and-update/umrah-insurance/` has ONLY: @type, author, description, headline, publisher, speakable, url | Add `datePublished` + `dateModified`, ISO-8601 format |
| T5 | Articles are authored by the organization, not a person — an E-E-A-T failure on YMYL content | `"author": {"@id": ".../#organization"}` + `"creator": "Policybazaar UAE"` on `articles/spain-schengen-visa/` | `author` → Person with `url` → author bio page (ProfilePage) |
| T6 | FAQPage "questions" are benefit headings, not questions — invalid Q&A markup | `Question.name` values on the hub: "Wide-Ranging Protection", "Emergency Medical Support", "Protection for Cancellations" | Only mark up genuine Q&A pairs; move benefit blurbs out of FAQPage |
| T7 | Podcast pages typed as blog posts | `BlogPosting+WebPage` on `/podcast/travel-insurance-a-true-need-or-a-hoax/` | PodcastEpisode → `partOfSeries` PodcastSeries |
| T8 | Wrong/missing type for the page's intent | Calculator page = WebPage only (no WebApplication); `france-visa` has ~100 FAQ mentions on-page but NO FAQPage node; category/destination-hub lack CollectionPage/ItemList; provider pages lack an insurer `mainEntity` | Replace/add per the Page Type × Expected Stack table above |
| T9 | Article image too small and single-aspect | One ImageObject 175×132 (~23K px; guidance is ≥50K px) on `articles/spain-schengen-visa/` | 16:9 / 4:3 / 1:1 array, ≥50K px each |
| T10 | Provider pages describe insurers by pre-rebrand names that no longer exist | `/axa-travel-insurance-tipvd/` (AXA Gulf → GIG Gulf, Jun 2022), `/rsa-travel-insurance-tipvd/` (RSA ME → Liva, Sep 2023) | `mainEntity` uses the current legal/brand name; old name at most in `alternateName` |
| T11 | Pages reference an `#organization` `@id` that no page ever declares — a dangling reference | `"parentOrganization": {"@id": ".../#organization"}` on every Org pseudo-node; no InsuranceAgency node found on any fetched page | Declare the canonical node once (site-wide foundation item 1) |

---

## Blocklist — NEVER recommend these (identical to health; recommending one is itself a finding)

| Type | Why |
|---|---|
| HowTo | Rich results removed Sep 2023 |
| Sitelinks SearchBox / SearchAction | Removed Nov 2024; PB.ae has no on-site search |
| SpecialAnnouncement | Deprecated Jul 2025 |
| ClaimReview, Dataset (rich result), VehicleListing, EstimatedSalary, LearningVideo | Retired 2025 |
| QAPage | User-generated single-question forums only |
| Carousel/ItemList *as a rich result* | Gallery limits carousels to Recipe/Course/Restaurant/Movie — ItemList stays for entity/GEO value only |
| TouristDestination / TouristTrip ⚠️ | No Google rich result; fine as 🤖 entity markup on destination pages but never promise a rich result from it |

**FAQPage caveat ⚠️:** FAQ rich results removed from Google Search as of May 2026. Keep
deploying FAQPage (valid schema.org, consumed by AI engines) — but never promise FAQ
stars, and only for genuine Q&A (see bug T6).

**Rendering:** JSON-LD must be server-rendered in initial HTML — JS-injected structured
data faces delayed processing.
