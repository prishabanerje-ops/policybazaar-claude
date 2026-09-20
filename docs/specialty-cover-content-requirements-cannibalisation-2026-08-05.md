# Specialty Cover — Content Requirements & Cannibalisation Handling

**Prepared:** 5 August 2026 · **Vertical:** Health Insurance, policybazaar.ae
**Read first:** `specialty-cover-seo-aio-strategy-2026-08-05.md` · **Briefs:** `specialty-cover-content-briefs-2026-08-05.md`
**Data:** `specialty-cover-disposition-2026-08-05.csv` (78 rows, machine-generated)

This is the operational document. It says, for every existing page that overlaps a planned spoke, what happens to it and why, plus the naming standard the new set has to follow.

---

## 1. Scope and what was measured

**78 existing URLs** across 21 topics overlap the planned spokes. Between them they carry **8,176 clicks and 899,342 impressions** over the trailing 360 days. That is the asset at risk, and the reason overlap gets resolved rather than ignored.

| Item | Value |
|---|---|
| Source | GSC Search Analytics, property `https://www.policybazaar.ae/` (URL-prefix, not `sc-domain:`, which has a 95-day hole from 5 Oct 2025 to 7 Jan 2026) |
| Window | 360d = 2025-08-07 → 2026-08-01 · 28d = 2026-07-05 → 2026-08-01 |
| Traffic type | Web, blended (all countries). UAE-only figures run roughly 30% lower on clicks but positions are comparable |
| URL universe | `sitemap-health-insurance.xml`, fetched 5 Aug 2026, HTTP 200, 1,064 URLs (1,033 English, 31 `ar-ae`) |
| Cannibalisation method | `query` × `page` pairs across 84 topic terms, then filtered to queries where 2+ health URLs both rank at position ≤40 with ≥50 impressions each |
| Result | **88 queries** with measured multi-URL competition |

### Exclusions applied, and why

These were removed because including them would overstate the problem:

| Excluded | Reason |
|---|---|
| URLs containing `#` | GSC reports jump-link anchors as separate rows. Same page, not cannibalisation. This alone accounted for most of the apparent duplication in the raw pull |
| URLs containing `?` | UTM and parameter variants of the same page |
| Queries beginning `site:` | Internal `site:` operator searches, not user demand |
| `/car-insurance/`, `/rta/`, `/travel-insurance/`, `/ar-ae/` paths | Matched on terms like "eye" and "doctor" but belong to other verticals |
| `get-an-indian-passport-for-newborns-in-dubai/` | Matched "newborn", but it is a passport article. Out of scope |
| `investment-plans/child-plans/` | Cannibalises `child insurance` against `health-insurance-for-kids-hiart`, but across verticals. Separate ticket |
| `/health-insurance/hospitals/*` | Handled by the hospitals-rehabilitation ticket (strategy §12) |
| `daman-care-bronze-dne-with-dental/` and `-without-dental/` | Insurer product pages, not editorial. Different page type |

**One correction worth recording.** An earlier pass reported the 96 `/network-hospitals/` URLs as having zero GSC data. That was wrong: the metrics query only covered `/health-insurance/` paths, so those URLs were never asked about. Queried directly they return **25,640 clicks and 1,130,823 impressions at 2.267% CTR**, which turned out to be the most important number in the whole analysis. Absence of data in a filtered pull is not absence of traffic.

---

## 2. Decision framework

Six actions. Each is assigned by measured metrics against the rules below, not by judgement, so the table cannot drift from the data.

| Action | Rule | Meaning |
|---|---|---|
| **KEEP + UPGRADE** | CTR ≥ 1.0% | Converts at or above the `-hiart/` benchmark (1.227%). **Never redirect.** Either it becomes the spoke, or the spoke links to it |
| **REWRITE IN PLACE** | CTR < 1.0% and impressions ≥ 20,000 | Demand is proven, the page is failing to convert it. Highest ROI in the set. Keep the URL, rebuild the content on the spoke template |
| **CONSOLIDATE** | Measured cannibalisation pair, weaker side CTR < 0.5% | 301 the weaker URL into the stronger. Pair resolutions in §4 |
| **REDIRECT** | Impressions ≥ 2,000, CTR < 0.25%, position > 40 | Earns impressions, converts nothing, buried. 301 to the spoke |
| **FOLD** | Impressions < 1,000 | Too small to justify its own page. Merge the useful content into the spoke, then 301 |
| **DIFFERENTIATE** | Distinct non-competing intent (seasonal, news, tool, employment law) | Keep and retarget. **Do not 301 into a spoke**, the intent is genuinely different |

Two rules override everything:

> **Rule A. Never redirect a page converting above 1.0%.** Six of the 78 clear 2.0%. Redirecting a proven converter into an unproven new page trades a known asset for a hypothesis.

> **Rule B. Where two pages both convert above benchmark, differentiate. Do not consolidate.** Consolidation is for splitting signal that neither page is monetising. Where both monetise, the split is working and the fix is keyword separation, not a merge. §4.4 is the case.

### Counts

| Action | URLs |
|---|---|
| REWRITE IN PLACE | 23 |
| DIFFERENTIATE | 21 |
| KEEP + UPGRADE | 15 |
| FOLD | 10 |
| CONSOLIDATE | 8 |
| REDIRECT | 1 |
| **Total** | **78** |

---

## 3. Measured cannibalisation

The clearest cases, all from GSC `query` × `page` data. Every row is a query where PB competes with itself.

### 3.1 Mental health — three-way split, zero clicks

| Query | Impressions | Clicks | Competing URLs |
|---|---|---|---|
| `is a psychiatrist covered by insurance` | 1,330 | **0** | `psychological-disorders-hiart` (pos 7.1) · `depression-hiart` (pos 37.9) |
| `psychiatric care coverage` | 1,004 | **0** | `health-insurance-for-mental-health` (pos 15.1) · `psychological-disorders-hiart` (pos 18.7) |
| `psychiatric care insurance` | 842 | **0** | `health-insurance-for-mental-health` (pos 13.7) · `psychological-disorders-hiart` (pos 23.3) |

Three queries, 3,176 impressions, **zero clicks**, two pages sitting a few positions apart on each. This is the strongest consolidation case in the set.

### 3.2 LASIK — 10x CTR gap between two pages on the same topic

| Query | Impressions | Clicks | Competing URLs |
|---|---|---|---|
| `lasik eye cost` | 1,294 | **0** | `articles/lasik-eye-surgery` (pos 37.8, 1,145 impr) · `lasik-eye-surgery-hiart` (pos 23.1, 149 impr) |

At page level the gap is decisive: the `-hiart` page converts at **0.862%**, the `articles/` page at **0.081%**.

### 3.3 Cataract — dead heat

| Query | Impressions | Clicks | Competing URLs |
|---|---|---|---|
| `cataract surgery cost` | 813 | 5 | `articles/cataract-surgery-cost-in-uae` (pos 8.6) · `cataract-surgery-in-uae-hiart` (pos 13.2) |
| `cataract surgery cost in uae` | 566 | 1 | `articles/cataract-surgery-cost-in-uae` (**pos 12.9**) · `cataract-surgery-in-uae-hiart` (**pos 13.0**) |

Two URLs one tenth of a position apart. Google cannot tell them apart either.

### 3.4 Children's cover — both pages winning

| Query | Impressions | Clicks | Competing URLs |
|---|---|---|---|
| `newborn baby insurance cost in uae` | 2,232 | 47 | `new-born-baby-hiart` (pos 3.9, 32 clk) · `for-kids-hiart` (pos 8.1, 15 clk) |
| `newborn insurance uae` | 659 | 23 | `new-born-baby-hiart` (pos 3.7, 16 clk) · `for-kids-hiart` (pos 8.9, 7 clk) |
| `newborn health insurance` | 864 | 12 | `for-kids-hiart` (pos 12.4, 2 clk) · `new-born-baby-hiart` (pos 13.4, 10 clk) |
| `medical insurance for child in uae price` | 2,931 | 101 | `for-kids-hiart` (pos 5.4, 101 clk) + 4 others |

Genuine overlap, but **both pages convert above 2.0%.** Rule B applies. See §4.4.

### 3.5 Breast cancer — three-way, zero clicks

| Query | Impressions | Clicks | Competing URLs |
|---|---|---|---|
| `breast cancer insurance` | 747 | **0** | `articles/breast-cancer` (pos 9.4) · `best-health-insurance-plans-for-cancer-patients` (pos 10.3) · `articles/breast-cancer-awareness-month` (pos 27.9) |

### 3.6 Knee replacement — the AIO signature

| Query | Impressions | Clicks | Competing URLs |
|---|---|---|---|
| `does insurance cover knee replacement in dubai` | 1,301 | **0** | `knee-replacement-surgery-hiart` (**pos 6.1**, 949 impr) · `health-guide/elective-treatment` (pos 39.7) |

Position 6.1 on 949 impressions with zero clicks is not a ranking problem. It is the signature of the answer being lifted above the results. Strategy §8.1.

### 3.7 Best dental clinic — near-duplicate, both buried

| Query | Impressions | Clicks | Competing URLs |
|---|---|---|---|
| `best dental clinic in dubai` | 1,720 | **0** | `articles/best-dental-clinics-dubai` (pos 73.6, 1,620 impr) · `articles/best-dental-clinic-in-dubai` (pos 86.2, 99 impr) |

### 3.8 Exact duplicate slugs across folders

Same slug, two folders. Confirmed from the sitemap.

| Slug | Locations |
|---|---|
| `breast-cancer-awareness-month` | `/health-insurance/articles/` **and** `/health-insurance/news-and-update/` |
| `elective-treatment` | `/health-insurance/glossary/` **and** `/health-insurance/health-guide/` |
| `premium-lock-in-health-insurance` | `/health-insurance/articles/` **and** `/health-insurance/` |

The third pair is outside this project's topics. Recorded because it is the same defect and should go in the same ticket.

### 3.9 Out of scope, found anyway

`al buhaira` and its variants (`buhaira`, `albuhaira`, `al buhaira insurance`, `al buhaira claim form`) put `/insurance-companies/al-buhaira-car-insurance/` against `/health-insurance/articles/al-buhaira-health-insurance/` across 6 queries totalling **18,403 impressions and 28 clicks**. Cross-vertical insurer-brand cannibalisation, unrelated to this project, worth its own ticket.

---

## 4. Pair resolutions

The framework in §2 flags pairs but cannot pick a winner when both sides trigger the same rule. These seven need a stated decision.

### 4.1 Dental clinic pair → neither wins

`articles/best-dental-clinics-dubai` (23,665 impr, 5 clicks, pos 58.7) and `articles/best-dental-clinic-in-dubai` (4,528 impr, 1 click, pos 23.6).

Combined: 28,193 impressions, **6 clicks**. Both are provider-discovery framing, which strategy §3 shows PB loses. Neither is worth preserving as a destination.

**Action: 301 both → `/health-insurance/cover/dental/`.** Salvage any genuinely useful clinic-selection guidance into the spoke's cover-confirmation section.

### 4.2 LASIK pair → the `-hiart` page wins

`does-health-insurance-cover-lasik-eye-surgery-hiart` (0.862% CTR, pos 12.3) beats `articles/lasik-eye-surgery` (0.081% CTR, pos 34.8) on every measure.

**Action: 301 `articles/lasik-eye-surgery` → `does-health-insurance-cover-lasik-eye-surgery-hiart`.** Keep the `-hiart` page as the canonical LASIK page and rewrite it on the spoke template. The `optical` spoke links to it and must not duplicate it.

**Keyword split, to be enforced in the brief:** the `optical` spoke owns `eye treatment cover uae`, `optical limit`, `vision cover`. The LASIK page owns `is lasik covered by insurance`, `lasik cost uae`. No overlap in H1, title or direct-answer block.

### 4.3 Cataract pair → the `articles/` page wins, on volume

`articles/cataract-surgery-cost-in-uae` (11,346 impr, 76 clicks, 0.67%, pos 11.6) against `cataract-surgery-in-uae-hiart` (3,573 impr, 36 clicks, **1.008%**, pos 16.3).

The `-hiart` page converts better but on a third of the impressions and from a worse position. The `articles/` page is the better host.

**Action: 301 `cataract-surgery-in-uae-hiart` → `articles/cataract-surgery-cost-in-uae`.** Port the `-hiart` page's title and opening framing across, since whatever it is doing earns 1.008% against 0.67%. This is the one case where the losing URL has something worth copying.

### 4.4 Children's cover → do not merge, and do not build the spoke

`health-insurance-for-kids-hiart` (103,260 impr, 2,511 clicks, **2.432%**) and `can-you-buy-health-insurance-for-new-born-baby-in-uae-hiart` (47,191 impr, 946 clicks, **2.005%**).

These are PB's two best-converting health pages. They overlap on four measured queries and both still convert at over twice the site benchmark. Rule B applies.

**Action: keep both. Differentiate by keyword.**

| Page | Owns | Must not target |
|---|---|---|
| `health-insurance-for-kids-hiart` | `health insurance for kids`, `child health insurance uae`, `medical insurance for child in uae price` | anything with "newborn" or "new baby" |
| `can-you-buy-health-insurance-for-new-born-baby-in-uae-hiart` | `newborn insurance uae`, `new baby insurance`, newborn enrolment window | anything with "kids" or "children" |

**Taxonomy amendment.** Spoke #13 (`childrens-cover`) should **not be built.** Building a third page into a topic where two existing pages already convert at 2.4% and 2.0% adds a competitor, not a capability. The hub links directly to both. This drops the launch set from 21 pages to **20**.

### 4.5 Mental health three-way → consolidate two, keep one

| Page | CTR | Action |
|---|---|---|
| `psychological-disorders-hiart` (10,165 impr, 0.403%) | below | **301 → `/health-insurance/cover/mental-health/`** |
| `articles/health-insurance-for-mental-health` (5,059 impr, 0.474%) | below | **301 → `/health-insurance/cover/mental-health/`** |
| `does-health-insurance-cover-depression-hiart` (743 impr, **1.211%**) | above | **KEEP.** Rule A. Narrow it to depression specifically; spoke links to it |

The new spoke inherits 15,224 impressions from two pages that were splitting them and converting neither.

### 4.6 Breast cancer → consolidate into the proven page

`articles/breast-cancer` (1,090 impr, 0.734%) competes with `best-health-insurance-plans-for-cancer-patients-in-uae` (10,393 impr, **1.395%**).

**Action: 301 `articles/breast-cancer` → `best-health-insurance-plans-for-cancer-patients-in-uae`,** which is protected by Rule A and becomes the `cancer` spoke's primary destination.

### 4.7 Duplicate slugs → collapse to one

| Keep | 301 away |
|---|---|
| `/health-insurance/articles/breast-cancer-awareness-month/` (2,930 impr, pos 27.6) | `/health-insurance/news-and-update/breast-cancer-awareness-month/` (1,337 impr, pos 33.8) |
| `/health-insurance/health-guide/elective-treatment/` (9,073 impr, pos 7.6) | `/health-insurance/glossary/elective-treatment/` |
| Decide on live metrics (outside this project's topics) | `premium-lock-in-health-insurance` duplicate |

---

## 5. Per-topic disposition

All 78 URLs. Machine-generated from GSC, mirrored in the CSV. Where §4 overrides a row, §4 wins.

#### orthopedic — 2 URLs, 4 clicks / 5,205 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/does-health-insurance-cover-knee-replacement-surgery-hiart/` | 4 | 3,113 | 0.128% | 39.7 | **REWRITE IN PLACE** | 3,113 impr at 0.128% CTR, pos 39.7. Below benchmark; rebuild on the spoke template. |
| `/health-insurance/joint-health-insurance/` | 0 | 2,092 | 0% | 16.1 | **REWRITE IN PLACE** | 2,092 impr at 0% CTR, pos 16.1. Below benchmark; rebuild on the spoke template. |

#### dental — 4 URLs, 881 clicks / 317,945 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance/articles/dental-insurance-in-uae/` | 852 | 270,343 | 0.315% | 6.1 | **REWRITE IN PLACE** | 270,343 impr at 0.315% CTR. Demand is proven; the page is not converting it. |
| `/health-insurance/articles/best-dental-clinics-dubai/` | 5 | 23,665 | 0.021% | 58.7 | **CONSOLIDATE** | weaker side of a measured pair vs best-dental-clinic-in-dubai; 301 into the stronger URL. |
| `/does-health-insurance-cover-dental-implants-hiart/` | 23 | 19,409 | 0.119% | 9.1 | **REWRITE IN PLACE** | 19,409 impr at 0.119% CTR, pos 9.1. Below benchmark; rebuild on the spoke template. |
| `/health-insurance/articles/best-dental-clinic-in-dubai/` | 1 | 4,528 | 0.022% | 23.6 | **CONSOLIDATE** | weaker side of a measured pair vs best-dental-clinics-dubai; 301 into the stronger URL. |

#### maternity-obgyn — 4 URLs, 1,819 clicks / 148,782 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance/articles/maternity-insurance-in-uae/` | 1,798 | 138,170 | 1.301% | 8.2 | **KEEP + UPGRADE** | converts above the -hiart benchmark (1.23%). Do not redirect. |
| `/health-insurance/articles/maternity-leave-in-uae/` | 5 | 4,703 | 0.106% | 18.0 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/health-insurance/articles/pregnancy-calculator/` | 14 | 3,531 | 0.396% | 10.6 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/things-to-know-while-buying-health-insurance-for-pregnancy-hiart/` | 2 | 2,378 | 0.084% | 36.2 | **REWRITE IN PLACE** | 2,378 impr at 0.084% CTR, pos 36.2. Below benchmark; rebuild on the spoke template. |

#### ivf-fertility — 1 URL, 196 clicks / 20,443 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/is-ivf-covered-by-health-insurance-hiart/` | 196 | 20,443 | 0.959% | 5.3 | **REWRITE IN PLACE** | 20,443 impr at 0.959% CTR. Demand is proven; the page is not converting it. |

#### physiotherapy — 1 URL, 60 clicks / 11,248 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance/health-guide/physiotherapy-treatment/` | 60 | 11,248 | 0.533% | 8.6 | **REWRITE IN PLACE** | 11,248 impr at 0.533% CTR, pos 8.6. Below benchmark; rebuild on the spoke template. |

#### dermatology — 3 URLs, 377 clicks / 30,729 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/is-dermatology-covered-by-health-insurance-hiart/` | 354 | 19,261 | 1.838% | 7.2 | **KEEP + UPGRADE** | converts above the -hiart benchmark (1.23%). Do not redirect. |
| `/health-insurance/articles/best-skin-care-clinics-in-dubai/` | 1 | 9,361 | 0.011% | 70.9 | **REDIRECT** | 9,361 impr, 0.011% CTR, pos 70.9. Buried and converting nothing. |
| `/health-insurance/articles/health-insurance-for-skin-treatment/` | 22 | 2,107 | 1.044% | 6.5 | **KEEP + UPGRADE** | converts above the -hiart benchmark (1.23%). Do not redirect. |

#### optical-vision — 5 URLs, 269 clicks / 50,176 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance/articles/health-insurance-for-vision/` | 60 | 13,894 | 0.432% | 8.0 | **REWRITE IN PLACE** | 13,894 impr at 0.432% CTR, pos 8.0. Below benchmark; rebuild on the spoke template. |
| `/health-insurance/articles/cataract-surgery-cost-in-uae/` | 76 | 11,346 | 0.67% | 11.6 | **CONSOLIDATE** | measured pair with cataract-surgery-in-uae-hiart; decide winner on position, 301 the other. |
| `/health-insurance/articles/lasik-eye-surgery/` | 9 | 11,149 | 0.081% | 34.8 | **CONSOLIDATE** | weaker side of a measured pair vs does-health-insurance-cover-lasik-eye-surgery-hiart; 301 into the stronger URL. |
| `/does-health-insurance-cover-lasik-eye-surgery-hiart/` | 88 | 10,214 | 0.862% | 12.3 | **CONSOLIDATE** | measured pair with articles/lasik-eye-surgery; decide winner on position, 301 the other. |
| `/cataract-surgery-in-uae-hiart/` | 36 | 3,573 | 1.008% | 16.3 | **KEEP + UPGRADE** | stronger side of a measured pair vs articles/cataract-surgery-cost-in-uae; absorb the weaker one. |

#### oncology — 13 URLs, 176 clicks / 19,554 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance/articles/best-health-insurance-plans-for-cancer-patients-in-uae/` | 145 | 10,393 | 1.395% | 10.8 | **KEEP + UPGRADE** | converts above the -hiart benchmark (1.23%). Do not redirect. |
| `/health-insurance/articles/breast-cancer-awareness-month/` | 15 | 2,930 | 0.512% | 27.6 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/health-insurance/articles/liver-cancer-symptoms-risk-factors-treatments-and-insurance-options/` | 2 | 1,582 | 0.126% | 12.5 | **REWRITE IN PLACE** | 1,582 impr at 0.126% CTR, pos 12.5. Below benchmark; rebuild on the spoke template. |
| `/health-insurance/news-and-update/breast-cancer-awareness-month/` | 1 | 1,337 | 0.075% | 33.8 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/health-insurance/articles/breast-cancer/` | 8 | 1,090 | 0.734% | 17.1 | **CONSOLIDATE** | measured pair with best-health-insurance-plans-for-cancer-patients-in-uae; decide winner on position, 301 the other. |
| `/health-insurance/articles/importance-of-health-insurance-on-world-cancer-day/` | 2 | 635 | 0.315% | 9.7 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/health-insurance/articles/does-stomach-cancer-cover-in-health-insurance/` | 0 | 566 | 0% | 30.6 | **FOLD** | only 566 impr. Merge into the spoke and 301. |
| `/health-insurance/articles/skin-cancer/` | 1 | 315 | 0.317% | 51.5 | **FOLD** | only 315 impr. Merge into the spoke and 301. |
| `/health-insurance/health-guide/cancer/` | 0 | 271 | 0% | 16.1 | **FOLD** | only 271 impr. Merge into the spoke and 301. |
| `/health-insurance/articles/lung-cancer-risk-factors-diagnosis-treatment-and-insurance-options/` | 2 | 192 | 1.042% | 62.1 | **KEEP + UPGRADE** | converts above the -hiart benchmark (1.23%). Do not redirect. |
| `/health-insurance/articles/kidney-cancer-symptoms-risk-factors-treatment-prevention-and-insurance-options/` | 0 | 140 | 0% | 16.0 | **FOLD** | only 140 impr. Merge into the spoke and 301. |
| `/health-insurance/articles/first-time-in-history-cancer-vanishes-from-every-patients-body-in-drug-trial/` | 0 | 74 | 0% | 42.3 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/health-insurance/news-and-update/guidelines-for-cancer-diagnosis-and-treatments-in-uae/` | 0 | 29 | 0% | 22.5 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |

#### mental-health — 8 URLs, 95 clicks / 26,805 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance/articles/mental-health-awareness-day/` | 20 | 10,479 | 0.191% | 7.6 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/does-health-insurance-cover-psychological-disorders-hiart/` | 41 | 10,165 | 0.403% | 9.3 | **CONSOLIDATE** | weaker side of a measured pair vs health-insurance-for-mental-health + depression-hiart; 301 into the stronger URL. |
| `/health-insurance/articles/health-insurance-for-mental-health/` | 24 | 5,059 | 0.474% | 11.2 | **CONSOLIDATE** | weaker side of a measured pair vs psychological-disorders-hiart; 301 into the stronger URL. |
| `/does-health-insurance-cover-depression-hiart/` | 9 | 743 | 1.211% | 15.8 | **KEEP + UPGRADE** | stronger side of a measured pair vs psychological-disorders-hiart; absorb the weaker one. |
| `/health-insurance/news-and-update/mohap-launches-mental-health-360/` | 1 | 165 | 0.606% | 10.7 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/health-insurance/articles/workplace-mental-health-uae/` | 0 | 107 | 0% | 26.9 | **FOLD** | only 107 impr. Merge into the spoke and 301. |
| `/health-insurance/news-and-update/abc-of-teenage-mental-health/` | 0 | 70 | 0% | 7.7 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/health-insurance/articles/mental-health-during-menopause/` | 0 | 17 | 0% | 7.7 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |

#### cardiology — 5 URLs, 101 clicks / 11,683 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance/articles/health-insurance-for-heart-patients/` | 95 | 8,412 | 1.129% | 12.1 | **KEEP + UPGRADE** | converts above the -hiart benchmark (1.23%). Do not redirect. |
| `/health-insurance/articles/cardiovascular-diseases-symptoms-causes-treatment-and-insurance-options/` | 2 | 2,826 | 0.071% | 10.3 | **REWRITE IN PLACE** | 2,826 impr at 0.071% CTR, pos 10.3. Below benchmark; rebuild on the spoke template. |
| `/health-insurance/health-guide/heart-valve-disease/` | 0 | 281 | 0% | 43.4 | **FOLD** | only 281 impr. Merge into the spoke and 301. |
| `/health-insurance/articles/world-heart-day/` | 4 | 157 | 2.548% | 6.0 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/health-insurance/articles/best-foods-for-heart-health/` | 0 | 7 | 0% | 31 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |

#### chronic-diabetes — 5 URLs, 166 clicks / 12,120 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance/articles/health-insurance-for-diabetes/` | 145 | 10,412 | 1.393% | 6.9 | **KEEP + UPGRADE** | converts above the -hiart benchmark (1.23%). Do not redirect. |
| `/all-about-health-insurance-for-hypertension-patients-hiart/` | 16 | 1,025 | 1.561% | 14.8 | **KEEP + UPGRADE** | converts above the -hiart benchmark (1.23%). Do not redirect. |
| `/health-insurance/articles/world-diabetes-day/` | 4 | 416 | 0.962% | 21.5 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/health-insurance/articles/fasting-with-diabetes-and-hypertension/` | 1 | 252 | 0.397% | 7.2 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/symptoms-of-diabetes-in-women-hiart/` | 0 | 15 | 0% | 3 | **FOLD** | only 15 impr. Merge into the spoke and 301. |

#### bariatric — 3 URLs, 17 clicks / 1,733 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/heres-how-obesity-affects-your-health-insurance-premiums-hiart/` | 17 | 1,672 | 1.017% | 15.6 | **KEEP + UPGRADE** | converts above the -hiart benchmark (1.23%). Do not redirect. |
| `/health-insurance/articles/obesity-and-diabetes-in-arab-population/` | 0 | 56 | 0% | 19.2 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/health-insurance/news-and-update/combating-obesity/` | 0 | 5 | 0% | 13.6 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |

#### childrens-cover — 6 URLs, 3,504 clicks / 160,907 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance-for-kids-hiart/` | 2,511 | 103,260 | 2.432% | 9.9 | **KEEP + UPGRADE** | stronger side of a measured pair vs can-you-buy-health-insurance-for-new-born-baby-in-uae-hiart; absorb the weaker one. |
| `/can-you-buy-health-insurance-for-new-born-baby-in-uae-hiart/` | 946 | 47,191 | 2.005% | 8.5 | **KEEP + UPGRADE** | stronger side of a measured pair vs health-insurance-for-kids-hiart; absorb the weaker one. |
| `/health-insurance/articles/how-to-sponsor-a-child-in-uae/` | 45 | 10,052 | 0.448% | 12.4 | **REWRITE IN PLACE** | 10,052 impr at 0.448% CTR, pos 12.4. Below benchmark; rebuild on the spoke template. |
| `/health-insurance/articles/screen-time-for-kids-how-much-is-too-much/` | 2 | 232 | 0.862% | 11.9 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/health-insurance/articles/summer-health-safety-tips-for-kids-in-uae/` | 0 | 138 | 0% | 9.1 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |
| `/health-insurance/articles/boosting-immunity-in-children-naturally/` | 0 | 34 | 0% | 27.9 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |

#### alternative-med — 1 URL, 16 clicks / 5,171 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance/articles/alternative-medicine-benefits-under-health-insurance/` | 16 | 5,171 | 0.309% | 8.2 | **REWRITE IN PLACE** | 5,171 impr at 0.309% CTR, pos 8.2. Below benchmark; rebuild on the spoke template. |

#### diagnostics — 1 URL, 32 clicks / 8,023 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance/health-guide/laboratory-tests/` | 32 | 8,023 | 0.399% | 8.2 | **REWRITE IN PLACE** | 8,023 impr at 0.399% CTR, pos 8.2. Below benchmark; rebuild on the spoke template. |

#### emergency — 1 URL, 2 clicks / 1,195 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance/glossary/ambulance-cover/` | 2 | 1,195 | 0.167% | 24.7 | **REWRITE IN PLACE** | 1,195 impr at 0.167% CTR, pos 24.7. Below benchmark; rebuild on the spoke template. |

#### dialysis-kidney — 2 URLs, 145 clicks / 7,067 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance/articles/insurance-for-kidney-patients/` | 145 | 7,003 | 2.071% | 8.4 | **KEEP + UPGRADE** | converts above the -hiart benchmark (1.23%). Do not redirect. |
| `/health-insurance/articles/best-foods-for-kidney-health/` | 0 | 64 | 0% | 18.2 | **DIFFERENTIATE** | seasonal/news/tool intent, not a cover query. Retarget or noindex; do not 301 into a spoke. |

#### endoscopy-liver — 4 URLs, 31 clicks / 4,623 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance/articles/health-insurance-for-liver/` | 16 | 2,414 | 0.663% | 25.8 | **REWRITE IN PLACE** | 2,414 impr at 0.663% CTR, pos 25.8. Below benchmark; rebuild on the spoke template. |
| `/does-health-insurance-cover-liver-cirrhosis-hiart/` | 12 | 1,010 | 1.188% | 36.9 | **KEEP + UPGRADE** | converts above the -hiart benchmark (1.23%). Do not redirect. |
| `/health-insurance/articles/gastrointestinal-diseases-symptoms-causes-treatment-and-insurance/` | 2 | 847 | 0.236% | 4.4 | **FOLD** | only 847 impr. Merge into the spoke and 301. |
| `/health-insurance/articles/health-insurance-for-liver-transplant/` | 1 | 352 | 0.284% | 11.4 | **FOLD** | only 352 impr. Merge into the spoke and 301. |

#### cosmetic-plastic — 3 URLs, 64 clicks / 13,790 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/does-health-insurance-cover-plastic-surgery-in-the-uae-hiart/` | 54 | 7,591 | 0.711% | 6.5 | **REWRITE IN PLACE** | 7,591 impr at 0.711% CTR, pos 6.5. Below benchmark; rebuild on the spoke template. |
| `/health-insurance/articles/gynecomastia-surgery-cost/` | 10 | 5,603 | 0.178% | 34.6 | **REWRITE IN PLACE** | 5,603 impr at 0.178% CTR, pos 34.6. Below benchmark; rebuild on the spoke template. |
| `/health-insurance/glossary/cosmetic-surgery/` | 0 | 596 | 0% | 42.2 | **FOLD** | only 596 impr. Merge into the spoke and 301. |

#### pre-approval — 4 URLs, 183 clicks / 29,518 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/co-payment-in-health-insurance-hiart/` | 160 | 21,404 | 0.748% | 7.7 | **REWRITE IN PLACE** | 21,404 impr at 0.748% CTR. Demand is proven; the page is not converting it. |
| `/health-insurance/articles/cashless-and-reimbursement/` | 12 | 4,896 | 0.245% | 11.7 | **REWRITE IN PLACE** | 4,896 impr at 0.245% CTR, pos 11.7. Below benchmark; rebuild on the spoke template. |
| `/health-insurance/glossary/copayment/` | 2 | 1,641 | 0.122% | 18.0 | **REWRITE IN PLACE** | 1,641 impr at 0.122% CTR, pos 18.0. Below benchmark; rebuild on the spoke template. |
| `/why-choose-a-network-hospital-over-a-non-network-hospital-hiart/` | 9 | 1,577 | 0.571% | 7.6 | **REWRITE IN PLACE** | 1,577 impr at 0.571% CTR, pos 7.6. Below benchmark; rebuild on the spoke template. |

#### general-surgery-folded — 2 URLs, 38 clicks / 12,625 impressions (360d)

| Existing URL | 360d clicks | 360d impr | CTR | Pos | Action | Why |
|---|---|---|---|---|---|---|
| `/health-insurance/health-guide/elective-treatment/` | 33 | 9,073 | 0.364% | 7.6 | **REWRITE IN PLACE** | 9,073 impr at 0.364% CTR, pos 7.6. Below benchmark; rebuild on the spoke template. |
| `/health-insurance/articles/health-insurance-for-surgery/` | 5 | 3,552 | 0.141% | 10.1 | **REWRITE IN PLACE** | 3,552 impr at 0.141% CTR, pos 10.1. Below benchmark; rebuild on the spoke template. |

---

## 6. Nomenclature standard

The current health footprint carries five URL patterns for the same kind of content (`-hiart/`, `-hipvd/`, `-hicf/`, `-hinh/`, `-hic/`, plus `/health-insurance/{folder}/`). New pages must not add a sixth.

### 6.1 URLs

| Rule | Standard |
|---|---|
| Folder | `/health-insurance/cover/` for the hub, `/health-insurance/cover/{benefit}/` for spokes. Verified free on 5 Aug 2026 |
| Slug | Benefit name, not specialty name. `dental` not `dentistry`. `maternity` not `obstetrics`. `kidney` not `nephrology` |
| Slug form | Lowercase, hyphenated, no stop words, no dates, no `-hiart`-style suffix |
| Length | Two words maximum where possible |
| Trailing slash | Always, matching site convention |
| Never | Reuse a retired slug. Never publish the same slug in two folders (§3.8) |

### 6.2 Title tags

| Page | Pattern |
|---|---|
| Hub | `Specialist Treatment Costs & Insurance Cover in the UAE \| Policybazaar.ae` |
| Spoke | `{Benefit} Cover in the UAE: Costs, Limits & What Insurance Pays \| Policybazaar.ae` |

Rules: the distinctive part stays under 60 characters. "UAE" appears in every title. Never use "Best", "Top" or "Near Me", which is the framing that put `best-dental-clinics-dubai` at position 58.7 and `best-skin-care-clinics-in-dubai` at 70.9. No year in the title unless the content is genuinely annual.

### 6.3 H1s

One H1 per page, distinct from the title tag, leading on the benefit and the cover question. Never leading on a verb PB cannot deliver (`find`, `browse`, `book`, `compare doctors`).

### 6.4 Spelling register

The design mixes British and American forms within single pages (§ briefs D9, D13). Standard: **American spelling in slug, title and H1 to match search demand; the British form appears once in body copy** so both are present. Applies to orthopedic/orthopaedic, pediatric/paediatric, gynecologist/gynaecologist, and to the -ise/-ize choice, which must be consistent site-wide.

### 6.5 Benefit naming, fixed vocabulary

Use one term per concept, everywhere, including tables and schema:

| Use | Not |
|---|---|
| co-pay | copay, co-payment, coinsurance |
| pre-approval | prior approval, pre-authorisation, PA |
| network | panel, empanelled |
| annual limit | sum insured, cap, ceiling |
| waiting period | qualifying period, moratorium |
| exclusion | not covered, uncovered |

The existing footprint uses `co-payment-in-health-insurance-hiart/` and `glossary/copayment/` for the same concept, which is how you end up with two pages competing on one query.

### 6.6 Cost tables

Consistent across all 20 spokes: three columns minimum (item, typical cash cost in AED, insurance treatment), an insurance-treatment badge from a fixed set (`CO-PAY ONLY`, `IF COVERED`, `PRE-APPROVAL`, `OFTEN PARTIAL`, `USUALLY EXCLUDED`), a visible `Verified [Month Year]` line, and the same footnote wording. The Figma footnote is already good and should be the standard: *"Guide ranges only - actual prices vary by provider. Always confirm exact costs and your co-pay with the clinic and your insurer."*

---

## 7. Redirect map

Fires **at the moment the destination publishes**, never earlier. Strategy §10.

### 7.1 301s into a new spoke

| From | To | Impr released |
|---|---|---|
| `/health-insurance/articles/best-dental-clinics-dubai/` | `/health-insurance/cover/dental/` | 23,665 |
| `/health-insurance/articles/best-dental-clinic-in-dubai/` | `/health-insurance/cover/dental/` | 4,528 |
| `/health-insurance/articles/best-skin-care-clinics-in-dubai/` | `/health-insurance/cover/dermatology/` | 9,361 |
| `/does-health-insurance-cover-psychological-disorders-hiart/` | `/health-insurance/cover/mental-health/` | 10,165 |
| `/health-insurance/articles/health-insurance-for-mental-health/` | `/health-insurance/cover/mental-health/` | 5,059 |
| `/health-insurance/articles/workplace-mental-health-uae/` | `/health-insurance/cover/mental-health/` | 107 |
| `/health-insurance/glossary/cosmetic-surgery/` | `/health-insurance/cover/cosmetic-reconstructive/` | 596 |
| `/health-insurance/health-guide/heart-valve-disease/` | `/health-insurance/cover/cardiac/` | 281 |
| `/symptoms-of-diabetes-in-women-hiart/` | `/health-insurance/cover/chronic-diabetes/` | 15 |
| `/health-insurance/articles/does-stomach-cancer-cover-in-health-insurance/` | `/health-insurance/cover/cancer/` | 566 |
| `/health-insurance/articles/skin-cancer/` | `/health-insurance/cover/cancer/` | 315 |
| `/health-insurance/health-guide/cancer/` | `/health-insurance/cover/cancer/` | 271 |
| `/health-insurance/articles/kidney-cancer-…-insurance-options/` | `/health-insurance/cover/cancer/` | 140 |
| `/health-insurance/articles/gastrointestinal-diseases-…-insurance/` | `/health-insurance/cover/endoscopy-liver/` | 847 |
| `/health-insurance/articles/health-insurance-for-liver-transplant/` | `/health-insurance/cover/endoscopy-liver/` | 352 |

### 7.2 301s between existing pages (no new page needed)

| From | To | Reason |
|---|---|---|
| `/health-insurance/articles/lasik-eye-surgery/` | `/does-health-insurance-cover-lasik-eye-surgery-hiart/` | §4.2 |
| `/cataract-surgery-in-uae-hiart/` | `/health-insurance/articles/cataract-surgery-cost-in-uae/` | §4.3 |
| `/health-insurance/articles/breast-cancer/` | `/…/best-health-insurance-plans-for-cancer-patients-in-uae/` | §4.6 |
| `/health-insurance/news-and-update/breast-cancer-awareness-month/` | `/health-insurance/articles/breast-cancer-awareness-month/` | §4.7 |
| `/health-insurance/glossary/elective-treatment/` | `/health-insurance/health-guide/elective-treatment/` | §4.7 |

### 7.3 Do not redirect, under any circumstances

Rule A. These convert above 1.0% and carry **6,076 clicks** between them.

| Page | Clicks | CTR |
|---|---|---|
| `/health-insurance-for-kids-hiart/` | 2,511 | **2.432%** |
| `/health-insurance/articles/maternity-insurance-in-uae/` | 1,798 | 1.301% |
| `/can-you-buy-health-insurance-for-new-born-baby-in-uae-hiart/` | 946 | 2.005% |
| `/is-dermatology-covered-by-health-insurance-hiart/` | 354 | 1.838% |
| `/health-insurance/articles/insurance-for-kidney-patients/` | 145 | 2.071% |
| `/health-insurance/articles/best-health-insurance-plans-for-cancer-patients-in-uae/` | 145 | 1.395% |
| `/health-insurance/articles/health-insurance-for-diabetes/` | 145 | 1.393% |
| `/health-insurance/articles/health-insurance-for-heart-patients/` | 95 | 1.129% |
| `/cataract-surgery-in-uae-hiart/`* | 36 | 1.008% |
| `/health-insurance/articles/health-insurance-for-skin-treatment/` | 22 | 1.044% |
| `/heres-how-obesity-affects-your-health-insurance-premiums-hiart/` | 17 | 1.017% |
| `/all-about-health-insurance-for-hypertension-patients-hiart/` | 16 | 1.561% |
| `/does-health-insurance-cover-liver-cirrhosis-hiart/` | 12 | 1.188% |
| `/does-health-insurance-cover-depression-hiart/` | 9 | 1.211% |
| `/health-insurance/articles/lung-cancer-…-insurance-options/` | 2 | 1.042% |

\* `cataract-surgery-in-uae-hiart` is the single documented exception, redirected under §4.3 because the receiving page holds 3x the impressions from a better position. Every other row is protected.

### 7.4 Redirect hygiene

- 301, never 302, never a JS redirect
- No chains. If A already points to B and B now points to C, repoint A to C
- Destination must be topically equivalent. A redirect to a generic hub is treated as a soft 404
- Update internal links to point at the destination. Do not rely on the redirect
- Remove the retired URL from the sitemap in the same release
- Log the pre-redirect 28d clicks and impressions per URL so recovery is measurable

---

## 8. Content requirements by disposition

### 8.1 REWRITE IN PLACE (23 URLs)

The largest group and the highest ROI. These hold proven demand and convert badly. The URL does not change, so there is no redirect risk and no lost equity.

The extreme case is `/health-insurance/articles/dental-insurance-in-uae/`: **270,343 impressions at 0.315% CTR from position 6.1.** Position 6 is not the problem. At the `-hiart/` benchmark of 1.227% the same impressions would return roughly 3,300 clicks a year instead of 852.

Requirements: keep the URL and the `dateModified` history. Rebuild against the spoke template in the briefs. Add the direct-answer block, the cost table, the insurer matrix. Rewrite the title and meta first and independently, because on a page already at position 6 the title is the likeliest single cause. Do not change the URL for tidiness.

### 8.2 KEEP + UPGRADE (15 URLs)

Do not restructure what is working. Add the direct-answer block if missing, add the reviewer byline, add the cost table, add internal links to and from the spoke. Leave the title alone unless there is a specific reason, and if the title is changed, measure it in isolation.

### 8.3 CONSOLIDATE (8 URLs) and REDIRECT (1)

Per §4 and §7. Before any 301, copy across every element the losing page had that the winner lacks. §4.3 is the case in point: the losing cataract page converts better and its title framing should move with the redirect.

### 8.4 FOLD (10 URLs)

Small pages whose content is worth keeping and whose URLs are not. Lift the substantive content into the spoke first, then 301. A fold that discards the content is just a deletion.

### 8.5 DIFFERENTIATE (21 URLs)

Mostly seasonal and awareness content (`world-heart-day`, `mental-health-awareness-day`, `breast-cancer-awareness-month`) plus tools (`pregnancy-calculator`) and employment law (`maternity-leave-in-uae`). Their intent is genuinely different and they must not be folded into cover pages.

Two need attention on their own terms. `mental-health-awareness-day` holds **10,479 impressions at 0.191%** and `articles/maternity-leave-in-uae` holds 4,703 at 0.106%. Both are large enough that if a retarget does not lift them, `noindex` is a legitimate outcome. Retiring a page that earns impressions and no clicks is not a loss.

---

## 9. Execution order

| Step | Action | Gate |
|---|---|---|
| 1 | Fix the 14 Figma defects (briefs §3) | Before build |
| 2 | Source every AED figure (briefs §7) | Before any publish |
| 3 | Engage the DHA-licensed reviewer, build the author profile page | Before any spoke publish |
| 4 | Fix `/author/*` soft-404 and add author pages to a sitemap | Before reviewer bylines carry weight |
| 5 | Legal sign-off on named insurer limits | Before the insurer matrix ships |
| 6 | `/ai-search` citation baseline on ~20 cover prompts | Before wave 1 |
| 7 | Build hub + `pre-approval` | Wave 0 |
| 8 | Build wave 1 spokes. **Apply each page's disposition at its publish** | Wave 1 |
| 9 | Resolve duplicate slugs (§4.7) | With wave 1 |
| 10 | Measure at 8 weeks against ≥1.0% CTR | Gate to wave 2 |
| 11 | Waves 2 and 3 | On passing |
| 12 | Hospitals-folder rehabilitation, `al buhaira` cross-vertical fix | Independent tickets |

---

## 10. What would make this wrong

Stated so the assumptions are checkable rather than buried.

1. **The CTR benchmark assumes CTR is the right proxy for lead intent.** It is a proxy. If spoke traffic clicks well and never reaches the quote form, the ≥1.0% gate passes while the project fails. That is why quote-form starts are tracked per URL from wave 1 and not added later.
2. **All figures are blended, not UAE-only.** UAE-only clicks run roughly 30% lower because a country filter moves GSC onto its anonymised dataset. Positions are comparable, relative comparisons hold, absolute click figures are overstated against UAE-only reality.
3. **The disposition rules are thresholds, and thresholds have edges.** A page at 0.98% CTR is classed REWRITE and one at 1.02% is protected, on a difference that is noise. Any row within 0.1 percentage points of 1.0% should be reviewed by a person, not applied mechanically. Four rows qualify: `is-ivf-covered-by-health-insurance-hiart` (0.959%), `cataract-surgery-in-uae-hiart` (1.008%), `heres-how-obesity-affects…` (1.017%), `articles/health-insurance-for-skin-treatment` (1.044%).
4. **No AI citation baseline exists.** Nothing in these documents claims measured AI Overview or ChatGPT citation data, because none was collected. Step 6 exists to fix that before launch rather than after.
5. **Keyword volume for the dropped specialties was not measured with a volume tool.** ENT, urology, pulmonology and rheumatology were dropped on PB's own footprint plus SERP reasoning. A DataForSEO pull could overturn any of those four.
