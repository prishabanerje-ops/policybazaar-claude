# Specialty Hub & Spoke — SEO + AIO Strategy

**Domain:** policybazaar.ae · **Vertical:** Health Insurance · **Prepared:** 5 August 2026
**Design source:** Figma `FTCKGnzdCT1AMeMxk01cju`, node `33034-15963` (spoke, "02 Orthopedic Page"), plus hub frame "01 Doctor Specific Pages"
**Companion documents:**
- `specialty-cover-content-briefs-2026-08-05.md` — hub and spoke briefs, mapped block by block to the Figma
- `specialty-cover-content-requirements-cannibalisation-2026-08-05.md` — per-URL disposition, redirect map, nomenclature standard
- `specialty-cover-disposition-2026-08-05.csv` — the 78-URL disposition table as data

---

## 1. Data provenance

Every figure in this document is measured. Nothing is extrapolated, and nothing is estimated from general knowledge.

| Source | Status | How obtained |
|---|---|---|
| Google Search Console | Live | Property `https://www.policybazaar.ae/` (URL-prefix, not `sc-domain:`, which carries a 95-day reporting hole from 5 Oct 2025 to 7 Jan 2026). Windows: 360d = 2025-08-07 → 2026-08-01, 28d = 2026-07-05 → 2026-08-01. Blended unless a row says UAE |
| XML sitemap | Live | `sitemap-health-insurance.xml`, fetched 5 Aug 2026, HTTP 200, 1,064 URLs (1,033 English, 31 `ar-ae`) |
| Figma design | Live | Figma MCP `get_metadata` on the spoke node, giving exact text-layer copy. Hub read from the supplied PNG at 1.35x crop because the hub node ID was not resolvable from the shared URL |
| Byline / reviewer state | Parsed | `byline-eeat-health-travel-2026-07-31.md`, itself a live crawl of 1,537 URLs on 31 Jul 2026 |
| URL availability | Live | `curl` HEAD checks on 6 candidate paths, 5 Aug 2026, with known-good and known-bad controls |
| UAE mandate status | Live | Web search, 5 Aug 2026. Sources listed in §9 |
| AI Overview / ChatGPT citations | **NOT MEASURED** | No citation baseline has been run for specialty or cover queries. §8 is structural guidance, not measured citation data. See §8.4 |

**Two limits to state plainly.** Keyword volumes for the deprioritised specialties in §6 come from PB's own GSC footprint and SERP reasoning, not from a volume tool, and §11 lists the DataForSEO pull that would settle them. And the AIO section is built on how AI systems select sources, not on a measured PB citation baseline, because none exists yet.

---

## 2. Decisions taken (Aakash, 5 August 2026)

| # | Decision | Consequence |
|---|---|---|
| 1 | **Content-only. No doctor database, no booking.** | The "Find a Doctor" framing cannot ship. Four separate promises in the Figma have to be rewritten. See §4 and the briefs |
| 2 | **Build all hub and spokes first, resolve overlap after.** | Adopted, with the build gate separated from the index gate. See §10 |
| 3 | **Cannibalisation handled case by case after an audit.** | The audit is done and is in the companion document. 78 URLs, 6 dispositions |
| 4 | **All AED figures in the Figma are designer placeholders.** | Every number needs a named source and a capture date before publish. Hard publish blocker |
| 5 | **Contract a real DHA-licensed clinician as medical reviewer.** | The "Medically reviewed" claim can ship, but only after the reviewer is engaged and has a live author profile. Unlocks `MedicalWebPage` schema. Also a hard publish blocker |
| 6 | **Publish named insurers and their benefit limits.** | This is the decision that makes the project defensible. See §7 |
| 7 | **English now. Arabic for proven performers only.** | 20 new pages at launch, with hreflang scaffolding so Arabic needs no URL change |

---

## 3. The finding that should drive the build

PB has already run this experiment twice, at scale, in the same vertical. The two results point in opposite directions, and the difference between them is the whole strategy.

### 3.1 Two programmatic page sets, near-identical scale, 7.6x apart on CTR

360 days, blended:

| Folder | Pages | Impressions | Clicks | CTR | Avg pos |
|---|---|---|---|---|---|
| **`/network-hospitals/`** (insurer × emirate) | 97 | 1,130,823 | **25,640** | **2.267%** | 7.8 |
| **`/health-insurance/hospitals/`** (provider entity) | 105 | 887,325 | **2,655** | **0.299%** | 10.4 |

Comparable page counts. Comparable impression volume. Both programmatic, both about hospitals. One returns 267 clicks per page per year, the other 25.

The win is broad-based, not an outlier: of the 97 `/network-hospitals/` pages, **36 have 100+ clicks, 80 have 10+, and only 2 have none.** The top page is 16% of the folder's clicks and the top five are 46%.

The queries show why:

| Query | Clicks | Impressions | CTR | Pos |
|---|---|---|---|---|
| `takaful emarat insurance hospital list in abu dhabi` | 156 | 509 | **30.65%** | 4.3 |
| `al sagr insurance hospital list sharjah` | 223 | 899 | **24.81%** | 3.9 |
| `orient insurance hospital list` | 653 | 5,111 | **12.78%** | 4.9 |
| `al sagr insurance hospital list` | 667 | 7,406 | **9.01%** | 5.8 |

Now the `/hospitals/` folder, same 360 days:

| Query | Clicks | Impressions | CTR | Pos |
|---|---|---|---|---|
| `amina hospital ajman` | 4 | 26,601 | **0.02%** | 10.9 |
| `nmc royal hospital sharjah` | 6 | 13,927 | **0.04%** | 8.8 |
| `al qassimi hospital` | 33 | 19,587 | 0.17% | 10.1 |

I classified all 500 queries reaching the `/hospitals/` folder by intent. **Insurance-intent queries are 3.7% of impressions but 17.3% of clicks**, so they convert roughly 5x better per impression than the navigational hospital-brand queries that make up the rest.

### 3.2 The rule this gives us

> PB earns clicks when the page answers an **insurance** question, and earns impressions it cannot convert when the page answers a **healthcare provider** question.

This holds across every folder measured:

| Folder | Pages | Impressions | Clicks | CTR | Pos | What the page answers |
|---|---|---|---|---|---|---|
| `/network-hospitals/` | 97 | 1,130,823 | 25,640 | **2.267%** | 7.8 | Insurance mechanic |
| `-hiart/` | 158 | 2,579,457 | 31,653 | **1.227%** | 8.8 | Insurance question |
| `/glossary/` | 22 | 126,760 | 872 | 0.688% | 7.7 | Insurance term |
| `/articles/` | 370 | 4,661,111 | 23,566 | 0.506% | 10.5 | Mixed |
| `/health-guide/` | 16 | 74,138 | 281 | 0.379% | 12.6 | Medical condition |
| `/hospitals/` | 105 | 887,325 | 2,655 | 0.299% | 10.4 | Provider entity |

The Figma, as drawn, is a provider-entity page set. Built that way it lands at the bottom of this table. Built as an insurance-mechanic page set it has a credible path to the top.

### 3.3 PB currently loses provider-discovery queries outright

Site-wide, 360 days, every query containing the term:

| Term | Impressions | Clicks | Pos | PB's best-ranking page |
|---|---|---|---|---|
| `orthopedic` | 247 | **0** | 16.4 | `/articles/top-veterinary-cl…` |
| `specialist` | 9,626 | **0** | 43.7 | `/car-insurance/articles/top-car-repair-garages…` |
| `dentist` | 4,703 | 5 | 65.4 | `/articles/best-dental-clinics-dubai/` |
| `cardiolog` | 102 | **0** | 8.1 | `/articles/top-8-specialty-c…` |
| `neurolog` | 178 | **0** | 38.2 | `/articles/top-veterinary-cl…` |
| `urolog` | 220 | **0** | 31.3 | `/articles/top-veterinary-cl…` |

A veterinary clinics article is PB's strongest page for orthopedic, neurology and urology queries. A car repair garages article is its strongest for "specialist." There is no orthopedic or cardiology footprint at all.

Against that, the same specialties framed as cover questions:

| Page | Impressions | Clicks | CTR | Pos |
|---|---|---|---|---|
| `is-dermatology-covered-by-health-insurance-hiart/` | 19,261 | 354 | **1.838%** | 7.2 |
| `insurance-for-kidney-patients/` | 7,003 | 145 | **2.071%** | 8.4 |
| `health-insurance-for-kids-hiart/` | 103,260 | 2,511 | **2.432%** | 9.9 |

Same medical territory. The framing is the only variable that changed.

---

## 4. What has to change in the design

The IA is sound and the block inventory is largely reusable. The targeting is aimed at the half of the query space PB loses.

Four places promise something a content-only page cannot deliver. All four are quoted verbatim from the Figma:

| Location | Current copy | Problem |
|---|---|---|
| Hub H1 | "Find a Doctor in UAE by Specialty - Costs & Insurance" | PB has no doctor data |
| Hub sub-head | "Browse DHA & DOH-licensed specialists across Dubai, Abu Dhabi & Sharjah" | Nothing to browse |
| Hub step 3 | "Book a DHA, DOH or MOHAP-licensed specialist" | No booking |
| Hub FAQ 3 | "Are the doctors DHA / DOH licensed?" | Presupposes a doctor listing |

The spoke has the same issue in its "How to Find an Orthopedic Doctor in the UAE" section, whose four steps are generic advice (start with your GP, check the licence, read reviews, confirm cover).

Rewrites are specified in the briefs. The short version: the hub becomes specialist **cost and cover** by specialty, and the spoke's find-a-doctor section becomes a **cover-confirmation** section, which is the part PB can genuinely own and the part that leads to a quote.

Design defects found in the Figma, which are separate from strategy and need a design pass, are itemised in the briefs (§3, numbered D1 to D14). There are 14, including a duplicated cost-table row, a duplicated KEY POINT block, a regulator row that lists Abu Dhabi twice and omits DHA/Dubai entirely, a stray "Toyota" breadcrumb crumb, and an empty Dubai card on the hub.

One factual error will otherwise ship. The hub states "health insurance is mandatory in Dubai and Abu Dhabi." Since 1 January 2025 that is out of date. See §9.

---

## 5. The reframe: benefit categories, not a department chart

Insurers do not price or exclude by medical specialty. They price by benefit category: outpatient, dental, optical, maternity, physiotherapy sessions, psychiatric, chronic disease, oncology, and a set of standard exclusions.

That matters for three reasons:

1. It is what people search when money is at stake, and PB's own CTR data in §3 shows it is what PB converts.
2. It is what PB uniquely knows, because PB sells the plans. Hospitals publish their own prices. Nobody else publishes cross-insurer benefit limits.
3. It maps to the AIO citation profile in §8, because benefit limits are specific, numeric and attributable.

So the taxonomy follows the benefit structure. A page exists where a cover decision exists, not where a hospital has a department.

---

## 6. Taxonomy: 28 proposed entries become 21 topics, 20 built pages

> **Amendment from the disposition analysis.** Of the 21, **`childrens-cover` should not be built.** Its topic is already served by two pages converting at **2.432%** and **2.005%**, which are PB's two best health pages. A third page there adds a competitor, not a capability. The hub links to both instead. Reasoning and the keyword split are in the cannibalisation document §4.4. So: **21 topics in the taxonomy, 20 new pages built.**

### Tier 1 — first wave (6)

| Page | Why | Existing overlap |
|---|---|---|
| **Orthopedics** | Already designed. Near-greenfield: 2 existing URLs, 5,205 impressions, 4 clicks | `knee-replacement-surgery-hiart` (3,113 impr, 0.128% CTR), `joint-health-insurance` (2,092 impr, **0 clicks**) |
| **Dentistry** | Dental is a rider in most UAE plans, the clearest cover-gap story. Largest single opportunity in the set | `dental-insurance-in-uae` (**270,343 impr at 0.315% CTR**), plus a confirmed duplicate pair |
| **Maternity & OB-GYN** | Merges Obstetrics + Gynecology. Regulation-anchored via the DHA Essential Benefits Plan | `maternity-insurance-in-uae` (138,170 impr, **1.301% CTR** — a strong page, do not disturb) |
| **Fertility / IVF** | Highest-cost elective, widest variation between insurers | `is-ivf-covered-by-health-insurance-hiart` (20,443 impr, 0.959% CTR, pos 5.3) |
| **Physiotherapy / Rehab** | Session caps are the textbook limit question, and it attaches to orthopedics | `health-guide/physiotherapy-treatment` (11,248 impr, 0.533% CTR, pos 8.6) |
| **Dermatology** | Medical vs cosmetic is a real distinction. PB's best-converting specialty page today | `is-dermatology-covered-by-health-insurance-hiart` (19,261 impr, **1.838% CTR**) |

### Tier 2 — second wave (8)

Optical & vision cover (reframed from Ophthalmology, since LASIK is typically excluded as elective and optical sits in a separate sub-limit) · Oncology · Psychiatry & mental health · Cardiology · Chronic disease: diabetes & thyroid (reframed from Endocrinology) · Bariatric surgery · Children's cover & newborn enrolment (reframed from Pediatrics) · Alternative medicine

### Tier 3 — third wave (5)

| Original entry | Becomes | Reason |
|---|---|---|
| Radiology / Pathology | **Diagnostics: imaging & lab tests** | Nobody consults a radiologist. The spoke already carries an MRI cost row |
| Emergency / Critical Care | **Emergency & ambulance cover** | Not researched mid-emergency, but a real pre-purchase question |
| Nephrology | **Dialysis & kidney cover** | The specialty term has no volume. `insurance-for-kidney-patients` runs at 2.071% CTR |
| Gastroenterology | **Endoscopy & liver cover** | Broad term is diffuse |
| Plastic Surgery | **Cosmetic vs reconstructive** | Purely an exclusion explainer, and that is fine |

### Additions (2)

**Vaccinations & preventive screening** — volume, partly mandated, and PB has nothing on it.
**Pre-approval & network rules** — not a specialty, but the mechanic that gates all 20 others and the highest-intent explainer on the map. It will earn internal links from every other spoke. Existing `co-payment-in-health-insurance-hiart` already draws 21,404 impressions.

### Folded or dropped (8 entries, 0 pages)

| Entry | Disposition |
|---|---|
| Family Medicine / GP | Fold into the hub. GP visits are cheap and near-universally covered, so no decision hangs on it. The **referral mechanic** stays as hub content |
| General Surgery | Fold into existing `health-insurance-for-surgery/`. Too vague to rank; fragments into procedures |
| ENT | Low differentiation. ENT procedures are covered as ordinary surgery |
| Neurology | Conditions already have pages (`multiple-sclerosis`, `motor-neuron-disease`, `aphasia`, `coma`). Strengthen those |
| Urology · Pulmonology · Rheumatology · Allergy/Immunology | Thin UAE footprint, no distinct cover story. Pulmonology overlaps `health-guide/copd-disease/`, rheumatology overlaps orthopedics |

---

## 7. The differentiator: named insurers and limits

Decision 6 is what turns this from an advice site into a data asset.

The evidence that insurer-entity pages work is in §3.1. Every top `/network-hospitals/` query is `[insurer] + [benefit] + [emirate]`, running at 9% to 31% CTR. That is the highest-converting pattern anywhere in PB's health footprint.

The specialty spokes should carry the same shape as a module: **which of the 25+ insurers cover this benefit, to what limit, with what waiting period, and with what co-pay.** Nobody else in the UAE market can publish that. Hospitals publish prices, not cover. Comparison blogs do not have the plan data. Insurers publish only their own.

This module is also the single strongest AIO asset on the page, for the reasons in §8.

Two requirements attach to it. It must carry a visible "last verified" date per row, because benefit limits change at renewal and a stale limit on a YMYL page is worse than no limit. And it needs legal and insurer-relations sign-off before the first page ships, so it is on the critical path, not a nice-to-have bolted on later.

**Phase 2, documented now and deliberately out of launch scope.** The `/network-hospitals/` result implies a specialty × insurer matrix ("Does Daman cover dental in Dubai?"). At 21 specialties × ~25 insurers that is a large programmatic set and it should not be attempted until the 20 editorial spokes have cleared the gate in §10. Recording it here so the URL structure in §8.2 does not foreclose it.

---

## 8. AIO and citation layer

### 8.1 What is winnable

Provider-discovery queries ("orthopedic doctor Dubai") produce AI answers citing hospitals, directories and the Local Pack. PB cannot win those and should stop trying.

Cover and cost queries ("does health insurance cover physiotherapy in the UAE", "how many physio sessions does insurance cover") are answered from whoever publishes clean, specific, attributable numbers. That is a gap PB can fill, and decision 6 is what fills it.

One measured signal worth noting. `does insurance cover knee replacement in dubai` gives PB **949 impressions at position 6.1 and zero clicks.** Position 6 with no clicks on that volume is the signature of an answer being lifted above the result rather than a ranking problem. That is the AIO problem and the AIO opportunity in one query.

### 8.2 Requirements per page

- **Direct answer first.** 40 to 60 words immediately under the H1 that answers the head question, with the number in it. AI systems lift the passage that answers, not the introduction that frames.
- **Tables for anything numeric.** Cost ranges, co-pay bands, session caps, waiting periods, insurer limits. Tables are extracted far more readily than prose.
- **One claim per sentence in cover sections.** Compound sentences do not survive extraction.
- **Named regulator anchors.** DHA (Dubai), DOH (Abu Dhabi), MOHAP (northern emirates). For the insurance regulator, the current statute is **Federal Decree-Law No. (6) of 2025**; the 2007 and 2023 laws are both repealed. Verify at `rulebook.centralbank.ae` before citing. Never cite it from memory.
- **`dateModified` in schema and visible on the page**, matching each other.
- **Entity clarity.** PB is the insurance comparison entity, not a care provider. Do not let the copy imply otherwise, which is the §4 problem restated.

### 8.3 Schema

| Page | Schema |
|---|---|
| Hub | `CollectionPage` + `BreadcrumbList` + `FAQPage` + `ItemList` enumerating the spokes |
| Spoke | `MedicalWebPage` + `BreadcrumbList` + `FAQPage` + `author` + `reviewedBy` |

`MedicalWebPage` is available **only because of decision 5**. Until the DHA-licensed reviewer is engaged and has a live author profile page, spokes use `Article`. Emitting `MedicalWebPage` or `reviewedBy` without a real, verifiable reviewer is a false claim in structured data on YMYL content, and it is the one thing in this project that could do lasting damage.

Do not use `Physician`, `Hospital` or `MedicalClinic` schema anywhere. There is no doctor or clinic data to describe.

### 8.4 Baseline before launch

No AI citation baseline exists for these queries. Run `/ai-search` over roughly 20 cover and cost prompts covering the Tier 1 six before the first page ships, so post-launch citation movement is measurable rather than asserted. Without it there is no before to compare against.

---

## 9. Regulatory accuracy

The hub states: *"In the UAE, health insurance is mandatory in Dubai and Abu Dhabi, but plans differ widely…"*

Since **1 January 2025** health insurance is mandatory for private-sector employees and domestic workers across all emirates, including Sharjah, Ajman, Umm Al Quwain, Ras Al Khaimah and Fujairah, enforced as a condition of residency-permit issue and renewal. The northern-emirates basic scheme is **AED 320**, with an enhanced top-up at **AED 120**.

Two cautions for the writer. The northern-emirates mandate is framed around private-sector employees and domestic workers as a visa condition, which is not identical in scope to how Dubai and Abu Dhabi structure their mandates, so "mandatory everywhere" is too blunt a correction. And UAE government domains are not reachable from this environment, so the primary-source check has to be done by a person on `mohap.gov.ae`, `doh.gov.ae` and `dha.gov.ae` before publish.

Sources: [LexisNexis, UAE mandatory health insurance from 1 January 2025](https://www.lexisnexis.com/blogs/ae-legal/b/insights/posts/uae-mandatory-health-insurance-starting-1-january-2025) · [The National, 22 Aug 2025](https://www.thenationalnews.com/news/uae/2025/08/22/uae-mandatory-health-insurance-cover-2025-northern-emirates/) · [The Law Reporters](https://thelawreporters.com/uaes-mandatory-health-insurance-for-workers-begins-everything-you-need-to-know)

---

## 10. Sequencing: build gate is not the index gate

Decision 2 is to build everything, then resolve overlap. Adopted, with one adjustment that costs nothing.

The risk was never the build order. It is that ~20 new pages targeting queries ~78 existing URLs already rank for creates a window of self-competition, on a site where three segments lost 5 to 11 positions in two unexplained breaks (see `seo-aio-kra-kpi-uae-filtered-2026-08-04.md`). And "decide later" tends to become never, which leaves both sets splitting signals permanently.

So:

| Gate | What it controls | When |
|---|---|---|
| **Build gate** | Content written, reviewed, QA'd | Runs continuously across all 20 |
| **Audit** | Per-URL disposition | **Already complete.** Companion document |
| **Index gate** | Page goes live, redirect fires, canonical set | Per page, at publish. Never before its disposition is applied |

The audit took days, the build takes weeks. Running them concurrently means no page waits and no overlap window ever opens.

### Release waves

| Wave | Pages | Gate to the next wave |
|---|---|---|
| 0 | Hub + `pre-approval` | Hub indexed, linked from `/health-insurance/`, breadcrumb 3 levels deep |
| 1 | Tier 1 six | Measure at 8 weeks |
| 2 | Tier 2 eight | Wave 1 passed |
| 3 | Tier 3 five + vaccinations | Wave 2 passed |

### Success bar

Set now so it is decidable rather than argued later. Benchmarks are from §3.2 on the same property and window.

| Metric | Bar | Why |
|---|---|---|
| Spoke CTR at 8 weeks | **≥ 1.0%** | `-hiart/` runs at 1.227%, `/hospitals/` at 0.299%. Above 1.0% means the reframe worked |
| Quote-form starts from spoke traffic | **> 0, tracked per spoke** | Traffic that never reaches the form is a content asset, not a lead asset |
| Cannibalised queries created | **0** | Measured by re-running the §3 query-by-page analysis. A new page must not introduce a second URL on a query its predecessor owned |
| AI citation share on the §8.4 prompt set | Directional only | No baseline yet, so wave 1 sets it |

Missing the bar is a real outcome, not a failure to explain away. It costs six pages to learn.

---

## 11. Open items

| # | Item | Owner | Blocks |
|---|---|---|---|
| 1 | Engage DHA-licensed clinical reviewer, build the author profile page | Content + HR | `MedicalWebPage`, "Medically reviewed" banner, all spoke publishes |
| 2 | Source every AED figure, with source and capture date | Content | All publishes. Decision 4 |
| 3 | Legal + insurer-relations sign-off on named-insurer limits | Legal | The §7 module, which is on the critical path |
| 4 | Fix `/author/*` soft-404 (any bad slug returns 200 with the authors hub) | Dev | Reviewer entity being credible to Google |
| 5 | Add author profile pages to a sitemap (currently in none) | Dev | Reviewer discoverability |
| 6 | 14 Figma defects (D1 to D14), itemised in the briefs §3 | Design | Build |
| 7 | Primary-source check of the mandate wording on UAE gov domains | Content, must be a human | Hub publish. §9 |
| 8 | DataForSEO volume pull for ENT, urology, pulmonology, rheumatology | SEO | Only whether those four stay dropped |
| 9 | `/ai-search` citation baseline on ~20 cover prompts | SEO | Measurability of AIO outcomes, not the build |
| 10 | Hospitals-folder rehabilitation (separate ticket, §12) | SEO + Dev | Nothing. Independent upside |

---

## 12. Adjacent opportunity: the hospitals folder

Out of scope for this build, recorded because it is the cheapest available lever in the vertical.

`/health-insurance/hospitals/` earns 887,325 impressions a year and converts 0.299% of them. 96.3% of those impressions are navigational queries for the hospital itself. That is real attention landing on PB pages and leaving.

Adding one module per hospital page (which specialties it covers, which insurers hold it in-network, linking to the matching spoke) and a reciprocal link back from each spoke does two things. Someone who arrived at `amina-hospital-ajman/` looking for a phone number gets a reason to click. And each spoke gains genuine UAE entity associations, which is exactly the local specificity that AI systems reward.

The `/network-hospitals/` result in §3.1 suggests the ceiling here is high, because it is the same content type with the insurance framing already applied.

---

## 13. Summary

1. PB's own data settles the framing question. `/network-hospitals/` converts at 2.267%, `/hospitals/` at 0.299%, at the same scale in the same vertical. Insurance-mechanic pages work; provider-entity pages accumulate impressions they cannot convert.
2. The Figma is a provider-entity design. Its IA and most of its blocks are reusable, but four promises and one factual error have to be rewritten first.
3. 28 proposed specialties become 21 topics and 20 built pages, ordered by whether a cover decision hangs on them rather than by hospital department. The children's-cover topic is deliberately left to the two existing pages that already convert at 2.4% and 2.0%.
4. Named insurer limits are what make the pages defensible and citable, and that decision puts legal sign-off on the critical path.
5. Two publish blockers are non-negotiable: a real clinical reviewer, and a source for every AED figure.
6. Build all 20 in parallel. Gate indexing per page on its disposition. Measure at 8 weeks against ≥1.0% CTR.
