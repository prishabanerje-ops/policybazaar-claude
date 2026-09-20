# 🔻 Cannibalisation Report — Health Insurance Cover Cluster

**Prepared:** 5 August 2026 · **Revised:** scope expanded to all 28 specialties
**Domain:** policybazaar.ae · **Full row data:** `specialty-cover-disposition-2026-08-05.csv` (105 rows)
**Companions:** `specialty-cover-url-title-h1-spec-2026-08-05.md` · `specialty-cover-page-content-structure-2026-08-05.md`

---

## ⚡ Verdict

> **105 existing URLs overlap the 30 planned pages. They carry 8,487 clicks and 954,905 impressions.**
>
> **88 queries** have measured self-competition. **4 near-duplicate pairs** and **3 exact duplicate slugs.**
>
> The worst cases share one trait: **PB ranks on page one and gets zero clicks.**
>
> **15 pages are confidently protected** and must never be redirected. They carry **6,342 clicks**.

| Do this | Don't do this |
|---|---|
| ✅ Rewrite the 27 pages holding demand and converting badly | ❌ Redirect anything converting above 1.0% on real volume |
| ✅ Consolidate the 10 measured duplicate cases | ❌ Merge two pages that both convert — differentiate instead |
| ✅ Fire each redirect **at the moment its destination publishes** | ❌ Fire redirects early, or "decide later" |

---

## 📊 Scale

| Metric | Value |
|---|---|
| URLs in scope | **105** (78 first pass + 27 found on the wider sweep) |
| 360d clicks at stake | **8,487** |
| 360d impressions at stake | **954,905** |
| Queries with measured self-competition | **88** |
| Near-duplicate pairs | **4** (dental clinics · LASIK · cataract · **asthma**) |
| Exact duplicate slugs | **3** |
| Confidently protected | **15** pages, 6,342 clicks |
| Topics with **no** existing page | **2** — Urology, Allergy/Immunology |

**Window** 2025-08-07 → 2026-08-01 · **Property** `https://www.policybazaar.ae/` (URL-prefix; the `sc-domain:` property has a 95-day hole from 5 Oct 2025) · **Traffic** web, blended

### Why the scope grew from 78 to 105

The first pass only covered the topics in the reduced 20-page plan. Restoring all 28 specialties brought 8 more topics into scope, and grepping the full 3,751-URL asset (rather than only the health sitemap) surfaced overlaps the first sweep missed — including the asthma duplicate pair and three separate arthritis pages.

**The restored specialties are not low-value.** Five have existing pages performing at or above the `-hiart/` benchmark:

| Restored specialty | Existing page | Impr | CTR | Pos |
|---|---|---|---|---|
| **ENT** | `cover-tonsillitis-hiart` | 1,368 | **1.316%** | 37.2 |
| **Rheumatology** | `health-insurance-for-arthritis` | 338 | **1.183%** | 7.0 |
| **Family Medicine / GP** | `opd-cover` | 7,962 | **1.030%** | 8.4 |
| **Gynaecology** | `best-health-insurance-for-women-hiart` | 7,276 | 0.976% | 9.3 |
| **Pulmonology** | `everything-you-need-to-know-about-asthma` | 5,483 | **0.018%** | **3.0** |

---

## 🎯 Action summary

| Action | URLs | Rule |
|---|---|---|
| **DIFFERENTIATE** | 33 | Seasonal / news / awareness / tool intent. Keep and retarget, **never 301 into a spoke** |
| **REWRITE IN PLACE** | 27 | CTR <1.0%. Demand proven, page failing. **Highest ROI** |
| **KEEP + UPGRADE** | 18 | CTR ≥1.0%. Don't redirect |
| **FOLD** | 15 | <1,000 impressions. Lift content into spoke, then 301 |
| **CONSOLIDATE** | 10 | Measured duplicate. 301 weaker → stronger |
| **REDIRECT** | 2 | Buried, converting nothing |

### Three rules that override the thresholds

| Rule | Statement |
|---|---|
| **A** | **Never redirect a page converting above 1.0% on ≥1,000 impressions.** Trading a known asset for an unproven page is the one mistake that can't be undone |
| **B** | **If two pages both convert above benchmark, differentiate — don't consolidate.** Consolidation fixes split signal nobody is monetising. When both monetise, the split is working |
| **C** | **Below 1,000 impressions, CTR is noise.** 6 pages clear 1.0% on tiny samples. They need a human call, not automatic protection. Listed in §Protected |

Benchmark = the `-hiart/` folder at **1.227% CTR**.

---

## 🔥 The confirmed cases

### 1. Mental health — 3 pages, 3,176 impressions, **0 clicks**

| Query | Impr | Clicks | Competing |
|---|---|---|---|
| `is a psychiatrist covered by insurance` | 1,330 | **0** | psychological-disorders (pos 7.1) · depression (pos 37.9) |
| `psychiatric care coverage` | 1,004 | **0** | mental-health (pos 15.1) · psychological-disorders (pos 18.7) |
| `psychiatric care insurance` | 842 | **0** | mental-health (pos 13.7) · psychological-disorders (pos 23.3) |

**→ Strongest consolidation case.** 301 the two under-benchmark pages into the `mental-health` spoke. Keep `depression-hiart` narrowed to depression only (1.211%, but small sample — Rule C).

### 2. 🆕 Asthma — position 3, **1 click from 5,483 impressions**

| Page | Impr | Clicks | CTR | Pos |
|---|---|---|---|---|
| `articles/everything-you-need-to-know-about-asthma` | 5,483 | **1** | **0.018%** | **3.0** |
| `heres-everything-you-need-to-know-about-asthma-in-the-uae-hiart` | 546 | 5 | 0.916% | 28.5 |

Near-identical titles. One sits at **position 3** and converts essentially nothing.

**→ The largest single recoverable loss found in this pass.** Position 3 with 0.018% CTR is a title and snippet failure, not a ranking problem. 301 the `-hiart` twin into the `articles/` page, then rewrite the title independently and measure it alone. Feeds the `respiratory` spoke.

### 3. LASIK — 10x CTR gap, same topic

| Page | Impr | CTR | Pos |
|---|---|---|---|
| `does-health-insurance-cover-lasik-eye-surgery-hiart` | 10,214 | **0.862%** | 12.3 |
| `articles/lasik-eye-surgery` | 11,149 | **0.081%** | 34.8 |

**→ The `-hiart` page wins outright.** 301 `articles/lasik-eye-surgery` into it. Keep it as the canonical LASIK page; the `optical` spoke links to it and must not duplicate it.

**Keyword split:** `optical` spoke owns *eye treatment cover / optical limit / vision cover*. LASIK page owns *is lasik covered / lasik cost*.

### 4. Cataract — dead heat, one tenth of a position apart

| Query | Impr | Clicks | Competing |
|---|---|---|---|
| `cataract surgery cost in uae` | 566 | 1 | articles (**pos 12.9**) · hiart (**pos 13.0**) |
| `cataract surgery cost` | 813 | 5 | articles (pos 8.6) · hiart (pos 13.2) |

**→ `articles/cataract-surgery-cost-in-uae` wins on volume** (11,346 vs 3,573 impr). 301 the `-hiart` page into it — **and port its title framing across**, because it converts at 1.008% vs 0.67%. The only case where the losing URL has something worth copying.

### 5. Children's cover — ⚠️ both pages winning, **do not merge**

| Page | Impr | Clicks | CTR |
|---|---|---|---|
| `health-insurance-for-kids-hiart` | 103,260 | 2,511 | **2.432%** |
| `can-you-buy-health-insurance-for-new-born-baby-in-uae-hiart` | 47,191 | 946 | **2.005%** |

Overlap on 4 measured queries, both converting at over twice benchmark. **Rule B.**

**→ Keep both. Split by keyword:**

| Page | Owns | Must not target |
|---|---|---|
| kids | `health insurance for kids`, `child health insurance uae` | anything with *newborn* / *new baby* |
| newborn | `newborn insurance uae`, enrolment window | anything with *kids* / *children* |

**→ And the new `paediatric` spoke must target care-cost intent only** — paediatrician visit cost, child specialist cover, vaccination cover. Never `health insurance for kids`, which is plan-purchase intent these two own. Enforce in H1, title and direct-answer block.

### 6. Knee replacement — the AI-answer signature

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `does insurance cover knee replacement in dubai` | 1,301 | **0** | **6.1** |

**→ Position 6 with zero clicks is not a ranking problem.** It's the answer being lifted above the results. The AIO case in one query, and the orthopedic spoke's primary target.

### 7. Best dental clinic — near-duplicate, both buried, **neither wins**

| Page | Impr | Clicks | Pos |
|---|---|---|---|
| `articles/best-dental-clinics-dubai` | 23,665 | 5 | 58.7 |
| `articles/best-dental-clinic-in-dubai` | 4,528 | 1 | 23.6 |

Combined: **28,193 impressions, 6 clicks.** Both provider-discovery framing.

**→ 301 both into the `dental` spoke.** Neither is worth preserving as a destination.

### 8. 🆕 Arthritis — three pages, one topic

| Page | Impr | Clicks | CTR | Pos |
|---|---|---|---|---|
| `articles/health-insurance-for-arthritis` | 338 | 4 | **1.183%** | 7.0 |
| `articles/world-arthritis-day` | 509 | 1 | 0.196% | 7.7 |
| `articles/health-guide-for-arthritis-awareness` | 148 | 1 | 0.676% | 10.8 |

Three pages inside three positions of each other on the same topic.

**→ `health-insurance-for-arthritis` becomes the `rheumatology` spoke's anchor** (small sample, Rule C — confirm before protecting). The two awareness pages stay DIFFERENTIATE and get retargeted to seasonal intent, not folded.

### 9. Breast cancer — 3 pages, 747 impressions, **0 clicks**

`articles/breast-cancer` (pos 9.4) · `best-health-insurance-plans-for-cancer-patients` (pos 10.3) · `articles/breast-cancer-awareness-month` (pos 27.9)

**→ 301 `articles/breast-cancer` into the cancer-plans page** (1.395%, protected).

### 10. Exact duplicate slugs — same slug, two folders

| Slug | Keep | 301 away |
|---|---|---|
| `breast-cancer-awareness-month` | `/articles/` (2,930 impr, pos 27.6) | `/news-and-update/` (1,337 impr, pos 33.8) |
| `elective-treatment` | `/health-guide/` (9,073 impr, pos 7.6) | `/glossary/` |
| `premium-lock-in-health-insurance` | decide on live metrics | `/health-insurance/` duplicate |

The third is outside this cluster's topics. Same defect, same ticket.

---

## 🛡️ Protected

### Confidently protected — 15 pages, 6,342 clicks. **Never redirect.**

CTR ≥1.0% **and** ≥1,000 impressions, so the CTR is stable.

| Page | Clicks | Impr | CTR |
|---|---|---|---|
| `health-insurance-for-kids-hiart` | 2,511 | 103,260 | **2.432%** |
| `articles/maternity-insurance-in-uae` | 1,798 | 138,170 | 1.301% |
| `can-you-buy-health-insurance-for-new-born-baby-in-uae-hiart` | 946 | 47,191 | **2.005%** |
| `is-dermatology-covered-by-health-insurance-hiart` | 354 | 19,261 | **1.838%** |
| `articles/health-insurance-for-diabetes` | 145 | 10,412 | 1.393% |
| `articles/insurance-for-kidney-patients` | 145 | 7,003 | **2.071%** |
| `articles/best-health-insurance-plans-for-cancer-patients-in-uae` | 145 | 10,393 | 1.395% |
| `articles/health-insurance-for-heart-patients` | 95 | 8,412 | 1.129% |
| `health-guide/opd-cover` 🆕 | 82 | 7,962 | 1.030% |
| `cataract-surgery-in-uae-hiart` * | 36 | 3,573 | 1.008% |
| `articles/health-insurance-for-skin-treatment` | 22 | 2,107 | 1.044% |
| `cover-tonsillitis-in-uae-hiart` 🆕 | 18 | 1,368 | **1.316%** |
| `heres-how-obesity-affects-your-health-insurance-premiums-hiart` | 17 | 1,672 | 1.017% |
| `all-about-health-insurance-for-hypertension-patients-hiart` | 16 | 1,025 | **1.561%** |
| `does-health-insurance-cover-liver-cirrhosis-hiart` | 12 | 1,010 | 1.188% |

\* **The one documented exception**, redirected under case 4 because the receiving page holds 3x the impressions from a better position. Every other row is absolute.

### 🟡 Small sample — CTR ≥1.0% but under 1,000 impressions. Human call, not automatic protection.

| Page | Clicks | Impr | CTR | Current class |
|---|---|---|---|---|
| `does-health-insurance-cover-depression-hiart` | 9 | 743 | 1.211% | KEEP |
| `articles/international-womens-day` | 6 | 550 | 1.091% | DIFFERENTIATE |
| `articles/health-insurance-for-arthritis` | 4 | 338 | 1.183% | KEEP |
| `articles/world-heart-day` | 4 | 157 | 2.548% | DIFFERENTIATE |
| `articles/lung-cancer-…-insurance-options` | 2 | 192 | 1.042% | KEEP |
| `health-guide/polio` | 1 | 67 | 1.493% | DIFFERENTIATE |

**Rule C.** A page with 1 click from 67 impressions is not "converting at 1.493%" — that's one click. Don't build a decision on it.

---

## 💰 Biggest opportunities

| # | Page | Impr | Clicks | CTR | Pos | Why |
|---|---|---|---|---|---|---|
| 1 | `articles/dental-insurance-in-uae` | **270,343** | 852 | **0.315%** | **6.1** | At benchmark this returns ~3,300 clicks/yr instead of 852 |
| 2 | 🆕 `articles/everything-you-need-to-know-about-asthma` | 5,483 | **1** | **0.018%** | **3.0** | Position 3 converting nothing. Pure title failure |
| 3 | `articles/best-dental-clinics-dubai` | 23,665 | 5 | 0.021% | 58.7 | 28,193 impr across the pair for 6 clicks |
| 4 | `does-health-insurance-cover-dental-implants-hiart` | 19,409 | 23 | 0.119% | 9.1 | Page one, converting nothing |
| 5 | `co-payment-in-health-insurance-hiart` | 21,404 | 160 | 0.748% | 7.7 | Anchors the `pre-approval` spoke |

**→ All five are REWRITE IN PLACE.** Keep the URL and its history. Rewrite title and meta **first and in isolation** — on pages already ranking at positions 3 to 9, the title is the likeliest single cause.

---

## ↪️ Redirect map

### Into a new spoke

| From | To | Impr released |
|---|---|---|
| `articles/best-dental-clinics-dubai` | `cover/dental/` | 23,665 |
| `does-health-insurance-cover-psychological-disorders-hiart` | `cover/mental-health/` | 10,165 |
| `articles/best-skin-care-clinics-in-dubai` | `cover/dermatology/` | 9,361 |
| `articles/top-8-specialty-clinics-in-dubai` ⚠️ | `cover/` (hub) | 5,993 |
| `articles/health-insurance-for-mental-health` | `cover/mental-health/` | 5,059 |
| `articles/best-dental-clinic-in-dubai` | `cover/dental/` | 4,528 |
| `health-guide/multiple-sclerosis` | `cover/neurology/` | 2,046 |
| `health-guide/alzheimer-disease` | `cover/neurology/` | 1,136 |
| `articles/gastrointestinal-diseases-…` | `cover/gastro/` | 847 |
| `health-guide/motor-neuron-disease` | `cover/neurology/` | 820 |
| `health-guide/coma` | `cover/neurology/` | 716 |
| `glossary/cosmetic-surgery` | `cover/cosmetic-reconstructive/` | 596 |
| `articles/does-stomach-cancer-cover-in-health-insurance` | `cover/cancer/` | 566 |
| `articles/health-insurance-for-liver-transplant` | `cover/gastro/` | 352 |
| `articles/skin-cancer` | `cover/cancer/` | 315 |
| `health-guide/heart-valve-disease` | `cover/cardiac/` | 281 |
| `articles/best-critical-health-insurance-plan-for-stroke` | `cover/neurology/` | 280 |
| `health-guide/cancer` | `cover/cancer/` | 271 |
| `articles/kidney-cancer-…` | `cover/cancer/` | 140 |
| `health-guide/aphasia` | `cover/neurology/` | 113 |
| `articles/workplace-mental-health-uae` | `cover/mental-health/` | 107 |
| `health-guide/copd-disease` | `cover/respiratory/` | 89 |
| `symptoms-of-diabetes-in-women-hiart` | `cover/diabetes-thyroid/` | 15 |

⚠️ **`top-8-specialty-clinics-in-dubai` is a documented override.** The REDIRECT rule requires position >40; this sits at 20.3, so by threshold it would be REWRITE. Redirected anyway because it is provider-discovery framing at **0.234% CTR** — the exact content type this project moves away from. Flagged rather than bent silently.

### Between existing pages (no new page needed)

| From | To | Case |
|---|---|---|
| 🆕 `heres-everything-…-asthma-in-the-uae-hiart` | `articles/everything-you-need-to-know-about-asthma` | 2 |
| `articles/lasik-eye-surgery` | `does-health-insurance-cover-lasik-eye-surgery-hiart` | 3 |
| `cataract-surgery-in-uae-hiart` | `articles/cataract-surgery-cost-in-uae` | 4 |
| `articles/breast-cancer` | `articles/best-health-insurance-plans-for-cancer-patients-in-uae` | 9 |
| `news-and-update/breast-cancer-awareness-month` | `articles/breast-cancer-awareness-month` | 10 |
| `glossary/elective-treatment` | `health-guide/elective-treatment` | 10 |

### Hygiene

- ✅ 301 only. Never 302, never JS
- ✅ No chains. If A→B and B→C, repoint A→C
- ✅ Destination must be topically equivalent. A redirect to a generic hub reads as a soft 404
- ✅ Update internal links to the destination. Don't rely on the redirect
- ✅ Remove the retired URL from the sitemap in the same release
- ✅ Log pre-redirect 28d clicks and impressions per URL so recovery is measurable

---

## 📋 Per-topic rollup

All 105 rows in the CSV. ⭐ = topic already converts above benchmark, protect it.

| Topic | URLs | 360d clicks | 360d impr | Blended CTR | Actions |
|---|---|---|---|---|---|
| **dental** | 4 | 881 | 317,945 | 0.277% | 2×Rewrite · 2×Consolidate |
| **childrens-cover** | 6 | 3,504 | 160,907 | 2.178% ⭐ | 3×Differentiate · 2×Keep · 1×Rewrite |
| **maternity-obgyn** | 4 | 1,819 | 148,782 | 1.223% ⭐ | 2×Differentiate · 1×Keep · 1×Rewrite |
| **optical-vision** | 5 | 269 | 50,176 | 0.536% | 3×Consolidate · 1×Keep · 1×Rewrite |
| **dermatology** | 3 | 377 | 30,729 | 1.227% ⭐ | 2×Keep · 1×Redirect |
| **pre-approval** | 4 | 183 | 29,518 | 0.620% | 4×Rewrite |
| **mental-health** | 8 | 95 | 26,805 | 0.354% | 4×Differentiate · 2×Consolidate · 1×Keep · 1×Fold |
| **ivf-fertility** | 1 | 196 | 20,443 | 0.959% | 1×Rewrite |
| **oncology** | 13 | 176 | 19,554 | 0.900% | 5×Differentiate · 4×Fold · 2×Keep · 1×Consolidate · 1×Rewrite |
| **vaccinations** 🆕 | 4 | 62 | 15,042 | 0.412% | 4×Differentiate |
| **cosmetic-plastic** | 3 | 64 | 13,790 | 0.464% | 2×Rewrite · 1×Fold |
| **family-medicine-gp** 🆕 | 2 | 105 | 12,640 | 0.831% | 1×Keep · 1×Rewrite |
| **general-surgery** | 2 | 38 | 12,625 | 0.301% | 2×Rewrite |
| **chronic-diabetes** | 5 | 166 | 12,120 | 1.370% ⭐ | 2×Keep · 2×Differentiate · 1×Fold |
| **cardiology** | 5 | 101 | 11,683 | 0.865% | 2×Differentiate · 1×Rewrite · 1×Keep · 1×Fold |
| **physiotherapy** | 1 | 60 | 11,248 | 0.533% | 1×Rewrite |
| **diagnostics** | 1 | 32 | 8,023 | 0.399% | 1×Rewrite |
| **gynaecology** 🆕 | 3 | 77 | 8,002 | 0.962% | 2×Differentiate · 1×Rewrite |
| **dialysis-kidney** | 2 | 145 | 7,067 | 2.052% ⭐ | 1×Differentiate · 1×Keep |
| **pulmonology** 🆕 | 5 | 6 | 6,222 | **0.096%** | 2×Consolidate · 2×Differentiate · 1×Fold |
| **hub-adjacent** 🆕 | 1 | 14 | 5,993 | 0.234% | 1×Redirect |
| **neurology** 🆕 | 8 | 23 | 5,301 | 0.434% | 4×Fold · 2×Rewrite · 2×Differentiate |
| **orthopedic** | 2 | 4 | 5,205 | **0.077%** | 2×Rewrite |
| **alternative-med** | 1 | 16 | 5,171 | 0.309% | 1×Rewrite |
| **endoscopy-liver** | 4 | 31 | 4,623 | 0.671% | 2×Fold · 1×Keep · 1×Rewrite |
| **bariatric** | 3 | 17 | 1,733 | 0.981% | 2×Differentiate · 1×Keep |
| **ent** 🆕 | 1 | 18 | 1,368 | 1.316% ⭐ | 1×Keep |
| **emergency** | 1 | 2 | 1,195 | 0.167% | 1×Rewrite |
| **rheumatology** 🆕 | 3 | 6 | 995 | 0.603% | 2×Differentiate · 1×Keep |
| **urology** | 🟢 0 | — | — | — | Greenfield |
| **allergy-immunology** | 🟢 0 | — | — | — | Greenfield |

**Read it this way.** Topics at the top of the CTR column are working and mostly need protecting. **Three topics are effectively greenfield or near it:**

| Topic | Status | Why it's the safest launch |
|---|---|---|
| **Urology** | 🟢 No existing page | Zero cannibalisation risk |
| **Allergy / Immunology** | 🟢 No existing page | Zero cannibalisation risk |
| **Orthopedic** | 0.077% CTR, 4 clicks | Almost nothing to lose, and already designed in Figma |
| **Pulmonology** | 0.096% CTR, 6 clicks | Plus a position-3 page to recover |

---

## ⏱️ Sequencing — the one thing that matters

> **The build gate is not the index gate.**

| Gate | Controls | When |
|---|---|---|
| **Build** | Content written, reviewed, QA'd | Continuously, all 30 |
| **Audit** | Per-URL disposition | ✅ **Complete.** This document |
| **Index** | Page live, redirect fires, canonical set | **Per page, at its own publish.** Never before |

The audit took days, the build takes weeks. Running them concurrently means **no page waits and no self-competition window ever opens.**

---

## 🚧 Out of scope, found anyway

| Finding | Detail |
|---|---|
| **`al buhaira` cross-vertical** | `/insurance-companies/al-buhaira-car-insurance/` vs `/health-insurance/articles/al-buhaira-health-insurance/` across 6 queries: **18,403 impressions, 28 clicks.** Own ticket |
| **`investment-plans/child-plans/`** | Competes with the kids page on `child insurance` (1,350 impr). Cross-vertical. Own ticket |
| **`/hospitals/` folder** | 887,325 impressions at **0.299%**. 96.3% navigational hospital-brand queries. Separate rehabilitation ticket |
| **A veterinary article ranks for medical queries** | `/health-insurance/articles/top-veterinary-clinics-in-the-uae/` is PB's best-ranking page for `orthopedic`, `neurolog` and `urolog` queries. Relevance defect, own ticket |
| **`/health-insurance/neuron/`** | This is **Neuron the TPA**, not neurology. Do not conflate when building the `neurology` spoke |

---

## ⚠️ Caveats

| # | Caveat |
|---|---|
| 1 | **CTR is a proxy for lead intent, not a measure of it.** If spoke traffic clicks well and never reaches the quote form, the ≥1.0% gate passes while the project fails. Track quote-form starts per URL from wave 1 |
| 2 | **Figures are blended, not UAE-only.** UAE clicks run ~30% lower (country filter moves GSC to its anonymised dataset). Positions comparable, relative comparisons hold, absolute clicks overstated |
| 3 | **Thresholds have edges, and small samples are noise.** Rule C exists because 6 pages clear 1.0% on under 1,000 impressions. Four more sit within 0.1pp of the 1.0% line and need a human call: `is-ivf-covered-…-hiart` (0.959%), `cataract-surgery-in-uae-hiart` (1.008%), `heres-how-obesity-affects…` (1.017%), `articles/health-insurance-for-skin-treatment` (1.044%) |
| 4 | **No keyword volume data exists for any of the 28.** `DATAFORSEO_LOGIN` / `DATAFORSEO_PASSWORD` are not configured on this machine. Every topic-priority judgement here rests on PB's own GSC footprint, which is circular for topics with no page. Setting those credentials would close it |
| 5 | **Measurement artefacts were excluded.** URLs with `#` or `?`, `site:` operator queries, and car/travel/RTA paths. Including them would overstate the problem several times over |
| 6 | **Two errors from earlier passes, both corrected here.** (a) The 96 `/network-hospitals/` URLs were reported as zero-traffic; the query had only covered `/health-insurance/` paths. Asked directly they return **25,640 clicks at 2.267% CTR**, which became the most important number in the project. (b) A grep using `\|` under `grep -E` returned no matches for the restored specialties and briefly looked like "no existing overlaps". Both cases: absence of data in a broken or filtered query is not absence of data |
