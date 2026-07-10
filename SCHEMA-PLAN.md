# PolicyBazaar UAE — Schema Plan by Page Type

**Date:** 2026-07-06 · **Scope:** 24 page types / ~1,025 health-insurance URLs from `Page Type - URL.rtf`
**Method:** every claim below is backed by a live fetch made today — PB.ae sample page per type (24/24 fetched OK), Google's structured-data docs + search gallery, schema.org type pages, and competitor HTML (PB India, insurancemarket.ae, yallacompare, shory, wellx→wellxai.com, Sukoon, ADNIC, Daman, Orient/insuranceuae.com, Takaful Emarat, NerdWallet, Forbes Advisor).
**Fetch failures (no data — not guessed):** comparethemarket.com and moneysupermarket.com (Cloudflare 403, all routes), orientinsurance.ae and tameen.ae (connection timeout), wellx.ae (NXDOMAIN — live brand domain is wellxai.com, which has zero schema).

**Legend:**
- ✅ = active Google rich result (verified in the gallery / feature doc today)
- 🤖 = no Google rich result; value is entity understanding + AI search (GEO) citations
- ⚠️ = policy or validity risk — read the note

---

## 1. Master Table — Page Type × Schema

**Site-wide YMYL layer — applies to EVERY row below (decision: Aakash, 2026-07-06):**
- **`author` → Person + `reviewedBy` → Person on every page's WebPage/Article node** — PB.ae is YMYL, so every page carries a named human author (with `url` → author ProfilePage) and a named reviewer with `jobTitle` (e.g. "Business Head - General Insurance").
- **Org node is `@type: ["InsuranceAgency","FinancialService"]`** with `makesOffer` → Offer → Service (one per LOB: Car, Health, Term Life, Business, Investment, Insurance Comparison) — rides on every page via the shared `#organization` `@id`.
- **`aggregateRating` (+ sample reviews) on the `#organization` node** — present on every page via the same shared node. ⚠️ Documented risk accepted: Google's local-business doc limits rating markup to reviews about *other* businesses, so PB's own rating on PB's own entity won't earn stars and carries self-serving-review policy risk; value is AI-search/GEO visibility. Keep it ONLY on `#organization` — never re-paste it on Product/TPA/hospital/calculator nodes (§4 bug 2 still applies to those).

| # | Page Type | URLs | Schema stack (every node in one `@graph`) |
|---|-----------|------|-------------------------------------------|
| 1 | BU (LOB home) | 2 | WebPage + speakable · BreadcrumbList ✅ · InsuranceAgency (site org, `@id`) ✅ · WebSite · Service → OfferCatalog → Offer 🤖 · FAQPage 🤖 |
| 2 | Category (`-hic`) | 10 | CollectionPage + speakable · BreadcrumbList ✅ · Service (category-scoped) 🤖 · ItemList → plans on page 🤖 · FAQPage 🤖 |
| 3 | Articles | 377 | Article ✅ · author → Person (real human, linked to author page) · BreadcrumbList ✅ · FAQPage 🤖 · VideoObject ✅ (only if video embedded) |
| 4 | Disease Insurance | 22 | Article ✅ (+ `@type: [Article, MedicalWebPage]`) · `about` → MedicalCondition 🤖 · `reviewedBy` → Person 🤖 · BreadcrumbList ✅ · FAQPage 🤖 |
| 5 | Emirates (city pages) | 6 | WebPage + speakable · BreadcrumbList ✅ · Service with `areaServed` → City/AdministrativeArea 🤖 · FAQPage 🤖 |
| 6 | Arabic (`/ar-ae/`) | 5 | Mirror the EN page type's stack · `inLanguage: "ar"` on WebPage/Article · fully-Arabic BreadcrumbList pointing at `/ar-ae/` URLs |
| 7 | Add Ons (TPA/network brands) | 7 | WebPage · BreadcrumbList ✅ · `mainEntity` → Organization (the TPA — Nextcare/NAS/MedNet, with insurer `sameAs`) 🤖 · FAQPage 🤖 |
| 8 | Type (basic/comprehensive/…) | 5 | WebPage · BreadcrumbList ✅ · Service (`serviceType`) → OfferCatalog 🤖 · FAQPage 🤖 |
| 9 | Network Hospital (insurer × city lists) | 100 | CollectionPage · BreadcrumbList ✅ · ItemList → ListItem → Hospital (name, address, geo) 🤖 · `about` → insurer Organization 🤖 · FAQPage 🤖 |
| 10 | Provider (`-hipvd`) | 51 | WebPage · BreadcrumbList ✅ · `mainEntity` → InsuranceAgency/Organization (THE INSURER, not PB — brand, logo, sameAs → insurer site) 🤖 · AggregateRating on the insurer ✅⚠️ (only if PB genuinely collects reviews *about that insurer*) · ItemList → its plans 🤖 · FAQPage 🤖 |
| 11 | Provider Plan (plan-family lists) | 47 | CollectionPage · BreadcrumbList ✅ · ItemList → ListItem → Product/HealthInsurancePlan 🤖 · `about` → insurer Organization 🤖 · FAQPage 🤖 |
| 12 | Plan Detail Pages | 184 | `@type: [Product, HealthInsurancePlan]` ✅ · `brand` → insurer Organization · `offers` → Offer (price, AED, priceValidUntil) ✅ · image (16:9/4:3/1:1) · BreadcrumbList ✅ · FAQPage 🤖 |
| 13 | Hospitals (single hospital) | 91 | WebPage · BreadcrumbList ✅ · `mainEntity` → Hospital ✅ (address, geo, telephone, medicalSpecialty, availableService) · FAQPage 🤖 |
| 14 | Disease Cost | 4 | `@type: [Article, MedicalWebPage]` ✅ · `about` → MedicalProcedure/MedicalCondition 🤖 · `reviewedBy` 🤖 · cost ranges as MonetaryAmount inside FAQ answers 🤖 · BreadcrumbList ✅ · FAQPage 🤖 |
| 15 | TPA (hub) | 14 | CollectionPage · BreadcrumbList ✅ · ItemList → ListItem → Organization (each TPA) 🤖 · FAQPage 🤖 |
| 16 | Calculator | 3 | WebPage · BreadcrumbList ✅ · WebApplication ✅⚠️ (`applicationCategory: "FinanceApplication"`, `operatingSystem: "Web"`, offers price 0 AED) · FAQPage 🤖 |
| 17 | Hospital (legacy `-hinh` lists) | 9 | Same as Network Hospital: CollectionPage · BreadcrumbList ✅ · ItemList → Hospital 🤖 · `about` → insurer Org 🤖 |
| 18 | Health Guide | 22 | Article ✅ (+ MedicalWebPage where clinical) · `reviewedBy` 🤖 · BreadcrumbList ✅ · FAQPage 🤖 · speakable |
| 19 | Claim Form | 14 | WebPage · BreadcrumbList ✅ · `mainEntity` → DigitalDocument (the PDF form, `about` → insurer Org) 🤖 · FAQPage 🤖 (claim steps as Q&A — HowTo is dead, see §5) |
| 20 | Clinic (roundup articles) | 6 | Article ✅ · ItemList → ListItem → MedicalClinic/LocalBusiness (each listed clinic) 🤖 · BreadcrumbList ✅ · FAQPage 🤖 |
| 21 | News & Update | 24 | **NewsArticle** ✅ · author Person · datePublished/dateModified · BreadcrumbList ✅ · speakable (news is its designed use case) |
| 22 | Glossary | 16 | WebPage · BreadcrumbList ✅ · DefinedTerm + `inDefinedTermSet` → DefinedTermSet (one set node for the whole glossary) 🤖 · FAQPage 🤖 (the term Q&A itself) |
| 23 | Podcast | 4 | WebPage · BreadcrumbList ✅ · PodcastEpisode → `partOfSeries` PodcastSeries (with `webFeed`) 🤖 · VideoObject ✅ if video version embedded / AudioObject 🤖 if audio-only |
| 24 | Health Benefit | 2 | Article ✅ (+ MedicalWebPage) · `reviewedBy` 🤖 · BreadcrumbList ✅ · FAQPage 🤖 |

**Plus two site-level additions not in the URL list (recommended):**

| Page | Schema |
|------|--------|
| Author bio pages (create if missing) | ProfilePage ✅ · `mainEntity` → Person with `jobTitle`, `knowsAbout`, `award`, `memberOf`, `alumniOf`, `sameAs` (LinkedIn + mailto:), `publishingPrinciples` → editorial-guidelines URL — the NerdWallet E-E-A-T pattern, observed live today |
| Homepage / About / Contact | Organization/InsuranceAgency (single canonical `@id` node) ✅ · WebSite · AboutPage / ContactPage subtypes 🤖 |

---

## 2. Site-wide foundation (every page's `@graph`)

PB.ae already emits one `@graph` per page — keep that architecture, standardize the nodes:

1. **InsuranceAgency** — ONE canonical node, `"@type": ["InsuranceAgency","FinancialService"]`, `"@id": "https://www.policybazaar.ae/#organization"`, referenced (never re-declared) from every page. Google's local-business doc verified today says to use the most specific LocalBusiness subtype — InsuranceAgency is exactly that; FinancialService as second type widens entity understanding. Properties: name, legalName, url, logo (≥112×112, works on white), telephone, address + geo (≥5-decimal lat/long), openingHoursSpecification, foundingDate, sameAs (socials + Wikipedia/Wikidata if pages exist; NerdWallet also lists Glassdoor), `makesOffer` → Offer → Service per LOB, and `aggregateRating` + reviews (⚠️ accepted-risk decision — see the YMYL layer note in §1; ISO-8601 review dates only).
2. **WebSite** — `"@id": ".../#website"`, `publisher` → `{"@id": "#organization"}`. **Do not add SearchAction** — sitelinks search box was removed by Google (changelog Nov 29, 2024, verified today), and policybazaar.ae has no on-site search feature, so the markup would misrepresent the site.
3. **WebPage** (or subtype CollectionPage/AboutPage/ContactPage/MedicalWebPage) — currently missing `name`, `url`, `@id` on every PB.ae page. Add: `@id`, url, name, description, `inLanguage` ("en" / "ar"), `isPartOf` → #website, `breadcrumb` → breadcrumb node `@id`, datePublished/dateModified, primaryImageOfPage, **`author` → Person (name, jobTitle, `url` → author ProfilePage) and `reviewedBy` → Person (name, jobTitle)** — mandatory on all page types per the YMYL layer (§1), not just articles. Keep the existing `speakable` (selectors verified present in the HTML) — note it's still beta, US/English only.
4. **BreadcrumbList** — already everywhere; fix the TPA page (self item missing) and Arabic pages (EN URLs inside AR breadcrumbs).

---

## 3. Per-type property notes (the non-obvious ones)

### Plan Detail Pages — the biggest win (184 URLs, currently ZERO product schema)
Verified today: these pages carry only WebPage + Breadcrumb. Daman is the only regional player using `HealthInsurancePlan` (multi-typed with Product, verified on damaninsurance.ae today) — adopt and out-execute it:

```json
{
  "@type": ["Product", "HealthInsurancePlan"],
  "name": "Takaful Emarat eCare Blue",
  "image": ["…16x9.jpg", "…4x3.jpg", "…1x1.jpg"],
  "description": "…",
  "brand": { "@type": "Organization", "name": "Takaful Emarat", "sameAs": "https://takafulemarat.com/" },
  "healthPlanNetworkId": "…", "benefitsSummaryUrl": "…",
  "offers": {
    "@type": "Offer",
    "price": "…", "priceCurrency": "AED", "priceValidUntil": "…",
    "availability": "https://schema.org/InStock",
    "seller": { "@id": "https://www.policybazaar.ae/#organization" }
  }
}
```
Google's Product doc (fetched today): product snippets need `name` + one of offers/review/aggregateRating; `Offer.price` required, `priceCurrency` ISO-4217. Insurance is NOT in Google's prohibited-products list (weapons/drugs/tobacco/gambling — verbatim from the doc). Product rich results are for single-product pages only — which is exactly what Plan Detail pages are; do NOT put Product on list/category pages.

### Provider pages — fix the entity direction
Today these are `Product` nodes carrying PB's own 4.7/41,800 rating regardless of insurer. Invert it: the page is *about the insurer*, so `mainEntity` → Organization/InsuranceAgency describing Orient/ADNIC/Daman (their logo, their `sameAs`). ⚠️ Google's local-business doc (fetched today): aggregateRating/review only "for sites capturing reviews about other businesses" — PB rating *insurers* qualifies; PB pasting *its own* rating on them does not (self-serving-review violation).

### Articles (377 URLs) — E-E-A-T chain
- `author` → Person with `url` → an author bio page marked ProfilePage (Profile page is an active gallery feature, verified today). Stop using `author: Organization` on YMYL money content.
- `publisher` → `{"@id": "#organization"}` + `publishingPrinciples` → editorial guidelines page (pattern live on both PB India and NerdWallet today).
- `image`: array of 16:9, 4:3, 1:1 ≥50K pixels (Google article doc, fetched today). Per-article images, not the one stock image currently reused.
- Keep `dateModified` genuinely fresh — Forbes Advisor's winning roundup showed dateModified 4 days old at fetch time.

### Hospital / Network Hospital (200 URLs combined) — nobody in the region does this
Zero competitors mark up hospital entities (verified across all scans today). `Hospital` is a LocalBusiness subtype → eligible for the Local business rich result when properties are complete: name, address (PostalAddress), geo, telephone, url, `medicalSpecialty`, `availableService`. On list pages wrap them in ItemList; on single-hospital pages use `mainEntity`. This is an uncontested structured-data moat for 191 URLs.

### Glossary (16 URLs) — DefinedTerm
No Google rich result (the Google doc URL 404s — verified), but DefinedTerm/DefinedTermSet is precisely what AI engines need to cite definitional content. One `DefinedTermSet` node (`name: "Health Insurance Glossary"`, `url: /health-insurance/glossary/`), each term page: `DefinedTerm` with `name`, `description`, `inDefinedTermSet`.

### Calculator (3 URLs) — WebApplication
`applicationCategory: "FinanceApplication"`, `operatingSystem: "Web"` (or `browserRequirements`), `offers: {price: "0", priceCurrency: "AED"}`, aggregateRating if real tool ratings exist. ⚠️ The Software-app gallery feature is verified active, but whether it accepts `WebApplication` vs only `SoftwareApplication` was not confirmed from today's fetches — safest is `@type: ["WebApplication", "SoftwareApplication"]`.

### News & Update (24 URLs) — NewsArticle
Currently no article schema at all on news pages (verified). NewsArticle is explicitly supported by the Article rich result (Google article doc, fetched today). Required nothing / recommended: headline, image array, datePublished, dateModified, author.name + author.url. Speakable's designed use case is exactly this content.

### Podcast (4 URLs)
Google retired podcast rich results (doc 404s — verified today), so this is pure entity/GEO markup: `PodcastEpisode` (name, datePublished, duration, `associatedMedia` → AudioObject with contentUrl) + `partOfSeries` → `PodcastSeries` (name, `webFeed` → RSS). If episodes are video embeds, VideoObject instead — that HAS an active rich result (required: name, thumbnailUrl, uploadDate ISO-8601).

### FAQPage — everywhere it exists on-page, but eyes open ⚠️
Verified today from Google's own doc: FAQ rich results were restricted to gov/health sites in Aug 2023 and **removed entirely from Google Search as of May 2026**. Keep deploying FAQPage anyway — the markup is valid schema.org, PB.ae already generates it well, and Q&A-structured data is heavily consumed by AI search engines (your chosen "include, flagged" position). Just never promise stakeholders FAQ stars.
Formatting fixes: strip "Q1." prefixes from `Question.name`; answers may carry HTML links (Forbes uses FAQ answers as an internal-linking surface — observed live today).

### Arabic pages (5 URLs + the whole /ar-ae/ tree)
Mirror the EN stack per page type with `inLanguage: "ar"` and fully-localized breadcrumbs (today's audit found EN URLs inside AR breadcrumb trails). Schema keys stay in English; values in Arabic.

---

## 4. Bugs in current markup to fix during rollout (all verified in today's HTML)

| # | Bug | Where | Fix |
|---|-----|-------|-----|
| 1 | `mainEntityOfPage: "True"` (string literal) | all 8 sampled Article pages | Set to the canonical URL or `{"@type":"WebPage","@id":"<url>"}` |
| 2 | Identical 6 reviews + 4.7/41,800 AggregateRating pasted on 10 unrelated Product nodes (TPA, calculator, hospital list, insurers…) | site-wide Product template | Remove from Product/entity nodes. PB's rating lives in exactly ONE place — the `#organization` node (accepted-risk decision, §1 YMYL layer) — plus genuinely-reviewed entities per §3 Provider note |
| 3 | Review `datePublished` not ISO-8601 ("24 February 2026") | Product review blocks | ISO-8601 (`2026-02-24`) — the InsuranceAgency blocks already do this correctly |
| 4 | Product nodes missing image/brand/offers | everywhere Product is used | Follow §3 Plan Detail template; delete Product from non-product pages |
| 5 | WebPage nodes missing `name`/`url`/`@id` | all 24 page types | §2 item 3 |
| 6 | TPA hub breadcrumb omits its own page | /health-insurance/tpa/ | Add final ListItem |
| 7 | Empty `description` (length 0) | 4+ Article pages | Populate or drop the property |
| 8 | Trailing spaces in names/headlines; empty `keywords: []` | multiple | Trim; drop empty arrays |
| 9 | Claim Form image filename is a base64 blob | claim-form pages | Real image URL |
| 10 | Wrong type for intent: Plan Detail (none), News (none), Podcast (none), Glossary (none), Calculator (Product), Health Guide (Product), Hospital list (Product) | see master table | Replace per §1 |

---

## 5. Deliberately excluded (don't let anyone re-add these)

| Type | Why (verified today) |
|------|----------------------|
| HowTo | Rich results removed Sep 2023; not in the current gallery |
| Sitelinks SearchBox / SearchAction | Feature removed — Google changelog Nov 29, 2024, doc now redirects to "bye-sitelinkbox"; PB.ae also has no on-site search feature |
| SpecialAnnouncement | Deprecated Jul 2025 |
| ClaimReview, Dataset(rich result), VehicleListing, EstimatedSalary, LearningVideo | Retired 2025 (plugin reference, Feb 2026) |
| QAPage | For user-generated single-question forums only — no PB.ae page type matches |
| Carousel/ItemList *as a rich result* | Gallery limits carousels to Recipe/Course/Restaurant/Movie — ItemList stays in the plan for entity/GEO value only |

---

## 6. Competitive position (what today's scans actually showed)

- **Nobody in UAE insurance is executing schema well.** yallacompare: zero JSON-LD. shory: zero JSON-LD (despite an llms.txt and AI-crawler-friendly robots.txt). wellx (wellxai.com): zero. insurancemarket.ae: decent blog graph (BlogPosting + real author Person + FAQPage + WebSite) but an invalid `@type: "author"` node, nothing on its homepage, and bare breadcrumbs on insurer pages. Sukoon's inner-page schema is trapped in client-side JS (invisible to non-JS crawlers). ADNIC's FAQPage JSON is syntactically invalid on every page carrying it. Daman is the only sophisticated one (HealthInsurancePlan, rich Organization) — and it undermines itself with a self-authored 5/5 CEO review and keyword-stuffed properties.
- **PolicyBazaar India is weaker than PB.ae** on structured data: plan pages and network-hospital pages ship zero JSON-LD; breadcrumbs only on the BU page. Its one pattern worth keeping: Article nested in WebPage via `mainEntity`, with `publishingPrinciples`.
- **The plays no competitor is making** (open field for PB.ae): Product+HealthInsurancePlan with real offers on 184 plan pages · Hospital entity markup on 191 hospital URLs · DefinedTerm glossary · ProfilePage author dossiers · NewsArticle on news · correct insurer-entity markup on 51 provider pages.
- Server-render every JSON-LD block in initial HTML (Google's Dec 2025 JS guidance: JS-injected structured data faces delayed processing — Sukoon is the cautionary tale).

## 7. Suggested rollout order (impact × effort)

1. **Plan Detail** (184 URLs, zero→Product/HealthInsurancePlan+Offer, active rich result)
2. **Site-wide fixes** (§4 — template-level, fixes hundreds of pages at once)
3. **Hospitals + Network Hospital** (191 URLs, uncontested Hospital/ItemList markup)
4. **Provider + Provider Plan** (98 URLs, correct insurer entities)
5. **News, Podcast, Glossary, Calculator** (47 URLs, wrong/no types today)
6. **Author ProfilePages + Article author chain** (E-E-A-T backbone for 377 articles)
7. **Arabic mirror** of all of the above

*Raw evidence: agent working files under the session scratchpad (`pbae-audit/`, `pb-india/`, `uae-aggregators/`, `uae-insurers/`, `global-comparison/`) — every JSON-LD block referenced above is saved there.*
