# Schema Expectations — policybazaar.ae Health Insurance URLs

**Scope: this file applies ONLY to policybazaar.ae health-insurance URLs.** Travel
pages have their own `schema-expectations-travel.md` (live-fetch evidence, 2026-07-10);
other verticals fall back to the generic checks in `seo-parameters.md` §10.

**Provenance:** distilled from `SCHEMA-PLAN.md` at the workspace root
(24 page types / ~1,025 health URLs; every claim there backed by live fetches on
2026-07-06 — PB.ae sample pages, Google structured-data docs, schema.org, competitor
HTML; raw JSON-LD evidence in that plan's named scratchpad dirs). If SCHEMA-PLAN.md is
revised, re-sync this file.

**How the auditor uses this file (extends §10's coverage check):**
1. Identify the page type from the URL pattern (suffixes below) or page content; state
   the assumed page type in the report.
2. Compare the implemented `@graph` against the expected stack for that type.
   Expected-but-missing types, present-but-wrong types (see bug #10), any known bug
   (§ Bugs), and **any recommendation of a blocklisted type** are findings.
3. Check the site-wide foundation nodes on every page regardless of type.

**Legend:** ✅ = active Google rich result (verified in gallery/feature docs at plan
date) · 🤖 = no rich result; value is entity understanding + AI-search (GEO) citations ·
⚠️ = policy or validity risk — read the note.

---

## Page Type × Expected Schema Stack

| # | Page Type (URL signal) | Expected stack (every node in one `@graph`) |
|---|---|---|
| 1 | BU / LOB home (`/health-insurance/`) | WebPage + speakable · BreadcrumbList ✅ · InsuranceAgency (site org, `@id`) ✅ · WebSite · Service → OfferCatalog → Offer 🤖 · FAQPage 🤖 |
| 2 | Category (`-hic`) | CollectionPage + speakable · BreadcrumbList ✅ · Service (category-scoped) 🤖 · ItemList → plans on page 🤖 · FAQPage 🤖 |
| 3 | Articles | Article ✅ · author → Person (real human, linked to author page) · BreadcrumbList ✅ · FAQPage 🤖 · VideoObject ✅ (only if video embedded) |
| 4 | Disease Insurance | Article ✅ (+ `@type: [Article, MedicalWebPage]`) · `about` → MedicalCondition 🤖 · `reviewedBy` → Person 🤖 · BreadcrumbList ✅ · FAQPage 🤖 |
| 5 | Emirates (city pages) | WebPage + speakable · BreadcrumbList ✅ · Service with `areaServed` → City/AdministrativeArea 🤖 · FAQPage 🤖 |
| 6 | Arabic (`/ar-ae/`) | Mirror the EN page type's stack · `inLanguage: "ar"` · fully-Arabic BreadcrumbList pointing at `/ar-ae/` URLs |
| 7 | Add Ons (TPA/network brands) | WebPage · BreadcrumbList ✅ · `mainEntity` → Organization (the TPA, with insurer `sameAs`) 🤖 · FAQPage 🤖 |
| 8 | Type (basic/comprehensive/…) | WebPage · BreadcrumbList ✅ · Service (`serviceType`) → OfferCatalog 🤖 · FAQPage 🤖 |
| 9 | Network Hospital (insurer × city lists) | CollectionPage · BreadcrumbList ✅ · ItemList → ListItem → Hospital (name, address, geo) 🤖 · `about` → insurer Organization 🤖 · FAQPage 🤖 |
| 10 | Provider (`-hipvd`) | WebPage · BreadcrumbList ✅ · `mainEntity` → InsuranceAgency/Organization (THE INSURER, not PB) 🤖 · AggregateRating on the insurer ✅⚠️ (only if PB genuinely collects reviews about that insurer) · ItemList → its plans 🤖 · FAQPage 🤖 |
| 11 | Provider Plan (plan-family lists) | CollectionPage · BreadcrumbList ✅ · ItemList → ListItem → Product/HealthInsurancePlan 🤖 · `about` → insurer Organization 🤖 · FAQPage 🤖 |
| 12 | Plan Detail Pages | `@type: [Product, HealthInsurancePlan]` ✅ · `brand` → insurer Organization · `offers` → Offer (price, AED, priceValidUntil) ✅ · image (16:9/4:3/1:1) · BreadcrumbList ✅ · FAQPage 🤖 |
| 13 | Hospitals (single hospital) | WebPage · BreadcrumbList ✅ · `mainEntity` → Hospital ✅ (address, geo, telephone, medicalSpecialty, availableService) · FAQPage 🤖 |
| 14 | Disease Cost | `@type: [Article, MedicalWebPage]` ✅ · `about` → MedicalProcedure/MedicalCondition 🤖 · `reviewedBy` 🤖 · costs as MonetaryAmount inside FAQ answers 🤖 · BreadcrumbList ✅ · FAQPage 🤖 |
| 15 | TPA (hub) | CollectionPage · BreadcrumbList ✅ · ItemList → ListItem → Organization (each TPA) 🤖 · FAQPage 🤖 |
| 16 | Calculator | WebPage · BreadcrumbList ✅ · WebApplication ✅⚠️ (`applicationCategory: "FinanceApplication"`, `operatingSystem: "Web"`, offers price 0 AED; safest `@type: ["WebApplication","SoftwareApplication"]`) · FAQPage 🤖 |
| 17 | Hospital (legacy `-hinh` lists) | Same as Network Hospital: CollectionPage · BreadcrumbList ✅ · ItemList → Hospital 🤖 · `about` → insurer Org 🤖 |
| 18 | Health Guide | Article ✅ (+ MedicalWebPage where clinical) · `reviewedBy` 🤖 · BreadcrumbList ✅ · FAQPage 🤖 · speakable |
| 19 | Claim Form | WebPage · BreadcrumbList ✅ · `mainEntity` → DigitalDocument (the PDF form, `about` → insurer Org) 🤖 · FAQPage 🤖 (claim steps as Q&A — HowTo is blocklisted, see below) |
| 20 | Clinic (roundup articles) | Article ✅ · ItemList → ListItem → MedicalClinic/LocalBusiness 🤖 · BreadcrumbList ✅ · FAQPage 🤖 |
| 21 | News & Update | **NewsArticle** ✅ · author Person · datePublished/dateModified · BreadcrumbList ✅ · speakable |
| 22 | Glossary | WebPage · BreadcrumbList ✅ · DefinedTerm + `inDefinedTermSet` → DefinedTermSet (one set node for the whole glossary) 🤖 · FAQPage 🤖 |
| 23 | Podcast | WebPage · BreadcrumbList ✅ · PodcastEpisode → `partOfSeries` PodcastSeries (with `webFeed`) 🤖 · VideoObject ✅ if video embedded / AudioObject 🤖 if audio-only |
| 24 | Health Benefit | Article ✅ (+ MedicalWebPage) · `reviewedBy` 🤖 · BreadcrumbList ✅ · FAQPage 🤖 |

**Site-level (not in URL list, expected as recommendations):** author bio pages →
ProfilePage ✅ with `mainEntity` → Person (jobTitle, knowsAbout, sameAs,
publishingPrinciples); Homepage/About/Contact → canonical Organization/InsuranceAgency
`@id` node ✅ + WebSite + AboutPage/ContactPage subtypes 🤖.

---

## Site-wide foundation (check on EVERY page)

1. **InsuranceAgency** — ONE canonical node, `"@id": "https://www.policybazaar.ae/#organization"`,
   *referenced* (never re-declared) from every page. Properties: name, legalName, url,
   logo (≥112×112, works on white), telephone, address + geo (≥5-decimal lat/long),
   openingHoursSpecification, foundingDate, sameAs.
2. **WebSite** — `"@id": ".../#website"`, `publisher` → `{"@id": "#organization"}`.
   **No SearchAction** (feature removed by Google, changelog Nov 29 2024; policybazaar.ae
   also has no on-site search feature, so the markup would misrepresent the site).
3. **WebPage** (or subtype) — must have `@id`, url, name, description, `inLanguage`
   ("en"/"ar"), `isPartOf` → #website, `breadcrumb` → breadcrumb `@id`,
   datePublished/dateModified, primaryImageOfPage. Keep existing `speakable`
   (beta, US/English only).
4. **BreadcrumbList** — on every page; watch the two known breadcrumb bugs below.

---

## Known bugs to grep for (all verified in PB.ae HTML at plan date)

| # | Bug | Fix |
|---|---|---|
| 1 | `mainEntityOfPage: "True"` (string literal) on Article pages | Canonical URL or `{"@type":"WebPage","@id":"<url>"}` |
| 2 | Identical 6 reviews + 4.7/41,800 AggregateRating pasted on unrelated Product nodes (TPA, calculator, hospital lists, insurers…) | Remove boilerplate; ratings only on entities genuinely reviewed |
| 3 | Review `datePublished` not ISO-8601 ("24 February 2026") | ISO-8601 (`2026-02-24`) |
| 4 | Product nodes missing image/brand/offers | Plan Detail template below; delete Product from non-product pages |
| 5 | WebPage nodes missing `name`/`url`/`@id` | Foundation item 3 |
| 6 | TPA hub breadcrumb omits its own page | Add final ListItem |
| 7 | Empty `description` (length 0) on Article pages | Populate or drop |
| 8 | Trailing spaces in names/headlines; empty `keywords: []` | Trim; drop empty arrays |
| 9 | Claim Form image filename is a base64 blob | Real image URL |
| 10 | Wrong type for intent: Plan Detail (none), News (none), Podcast (none), Glossary (none), Calculator (Product), Health Guide (Product), Hospital list (Product) | Replace per the master table |

---

## Blocklist — NEVER recommend these (recommending one is itself a finding)

| Type | Why (verified at plan date) |
|---|---|
| HowTo | Rich results removed Sep 2023; not in the current gallery |
| Sitelinks SearchBox / SearchAction | Removed — Google changelog Nov 29 2024; PB.ae also has no on-site search feature |
| SpecialAnnouncement | Deprecated Jul 2025 |
| ClaimReview, Dataset (rich result), VehicleListing, EstimatedSalary, LearningVideo | Retired 2025 |
| QAPage | User-generated single-question forums only — no PB.ae page type matches |
| Carousel/ItemList *as a rich result* | Gallery limits carousels to Recipe/Course/Restaurant/Movie — ItemList stays for entity/GEO value only |

**FAQPage caveat ⚠️:** FAQ rich results were restricted Aug 2023 and removed entirely
from Google Search as of May 2026. Keep deploying FAQPage (valid schema.org, consumed
by AI engines) — but never promise FAQ stars in a report. Strip "Q1." prefixes from
`Question.name`; answers may carry HTML links.

---

## Key templates & entity-direction rules

**Plan Detail (the biggest win — pages currently carry only WebPage + Breadcrumb):**
```json
{
  "@type": ["Product", "HealthInsurancePlan"],
  "name": "<plan name>",
  "image": ["…16x9.jpg", "…4x3.jpg", "…1x1.jpg"],
  "brand": { "@type": "Organization", "name": "<insurer>", "sameAs": "<insurer site>" },
  "offers": { "@type": "Offer", "price": "…", "priceCurrency": "AED",
              "priceValidUntil": "…", "availability": "https://schema.org/InStock",
              "seller": { "@id": "https://www.policybazaar.ae/#organization" } }
}
```
Product rich results are for single-product pages ONLY — never put Product on
list/category pages. Insurance is not in Google's prohibited-products list.

**Provider pages — entity direction:** the page is *about the insurer* →
`mainEntity` → Organization/InsuranceAgency for Orient/ADNIC/Daman etc. (their logo,
their `sameAs`). ⚠️ aggregateRating/review only "for sites capturing reviews about
other businesses" — PB rating *insurers* qualifies; PB pasting *its own* 4.7 rating on
them is a self-serving-review violation.

**Articles E-E-A-T chain:** `author` → Person with `url` → author bio page marked
ProfilePage (active gallery feature). Stop `author: Organization` on YMYL content.
`publisher` → `{"@id": "#organization"}` + `publishingPrinciples`. `image`: 16:9/4:3/1:1
array ≥50K pixels, per-article. Keep `dateModified` genuinely fresh.

**Rendering:** JSON-LD must be server-rendered in initial HTML — JS-injected structured
data faces delayed processing (Google Dec 2025 JS guidance).
