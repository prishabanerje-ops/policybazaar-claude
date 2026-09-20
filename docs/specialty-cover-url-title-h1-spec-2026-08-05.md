# Specialty Cover — URL, Title, Description, H1 & Keyword Map

**Prepared:** 5 August 2026 · **Revised:** all 28 specialties + secondary keyword map
**Pages:** 1 hub + 28 specialty spokes + 2 additions = **31**
**Companions:** `specialty-cover-page-content-structure-2026-08-05.md` · `specialty-cover-cannibalisation-report-2026-08-05.md`

---

## ⚠️ How to read the keyword data

Secondary keywords are split two ways, and the difference matters:

| Mark | Meaning |
|---|---|
| **⬤ measured** | PB **already receives impressions** for this exact query. Pulled from GSC, 360 days to 1 Aug 2026, from a full sweep of **121,927 query strings** |
| **○ proposed** | No measured PB footprint. A deliberate target, not a validated one |

> **The impression figures are PB's own GSC impressions, not market search volume.** They tell you what PB already surfaces for. They do **not** tell you total demand — a query with 0 PB impressions may still have high market volume. `DATAFORSEO_LOGIN`/`DATAFORSEO_PASSWORD` are unset on this machine, so true volume remains unmeasured.

**Demand status** per page: 🟢 Proven (≥2,000 measured impr) · 🟡 Partial (≥300) · 🟠 Thin (>0) · ⚪ Unmeasured (0).
⚪ is not evidence of no demand. It means PB has no page, so no data.

### Three queries excluded as measurement artefacts

| Query | Why excluded |
|---|---|
| `sukanya samriddhi yojana` (+7 variants) | Matched the `mri` seed inside "sa**mri**ddhi". Indian savings scheme, not diagnostics |
| `capital health screening centre …` (~6,500 impr) | Matched `screening` but is a visa-medical centre, navigational |
| `gp parking dubai`, `gp parking zone` | Matched `gp `, unrelated |

---

## 🔥 Two findings from the keyword sweep

### 1. The largest zero-click query on the domain

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `what is a deductible insurance` | **61,234** | **0** | **5.5** |

Position 5.5, 61k impressions, not a single click. It is a cost-sharing mechanic query, so it belongs to the **`pre-approval` spoke**. On its own it justifies building that page first.

For scale: PB has **24 queries** with 5,000+ impressions and zero clicks. This is the largest, and the only health-cover one in the top five.

### 2. Physiotherapy ranks top-3 and converts nothing

12 query variants, **2,468 impressions, 1 click total**, most at **positions 2.2 to 4.7**:

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `physiotherapy is covered under insurance` | 319 | 0 | **2.2** |
| `is physiotherapy included in insurance` | 316 | 0 | **2.6** |
| `physiotherapy insurance coverage` | 307 | 1 | **2.7** |
| `physiotherapy claim insurance` | 288 | 0 | **3.7** |
| `physiotherapy coverage` | 205 | 0 | **2.5** |
| `physiotherapy covered by insurance` | 180 | 0 | **2.5** |

Ranking in the top three across a dozen variants and earning one click is a title and snippet failure, not a ranking problem. Confirms physiotherapy in wave 1.

---

## Rules applied

| Field | Rule |
|---|---|
| **Folder** | `/health-insurance/cover/` — verified free (404 on 5 Aug 2026) |
| **Slug** | Benefit name, not specialty name. `dental` not `dentistry`, `respiratory` not `pulmonology` |
| **Title** | ≤60 chars **before** the ` \| Policybazaar.ae` suffix. "UAE" in every title. Never "Best", "Top", "Near Me" |
| **Description** | 140–160 chars |
| **H1** | One per page, different from the title, no verb PB can't deliver |
| **Schema** | Spokes `MedicalWebPage` **only after** a DHA-licensed reviewer is engaged; `Article` until then. Hub `CollectionPage` |
| **Breadcrumb** | Hub 3 levels · Spoke 4 levels |

---

## 🗺️ Keyword map — all 31 pages

| # | Page | Primary keyword | Demand | Secondary keywords |
|---|---|---|---|---|
| **HUB** | Specialist cover hub | `specialist consultation cost uae` | ⚪ Unmeasured | ○ `specialist visit co-pay uae` · ○ `do i need a referral to see a specialist in dubai` · ○ `specialist consultation fee abu dhabi` |
| 1 | Orthopedics | `does health insurance cover orthopedic surgery uae` | 🟡 Partial | ⬤ `does insurance cover knee replacement in dubai` (938) · ⬤ `knee replacement surgery cost dubai` (227) · ⬤ `knee replacement cost dubai` (40) · ⬤ `is knee replacement covered by insurance` (4) · ○ `orthopedic consultation cost dubai` · ○ `arthroscopy cost uae insurance` · ○ `is physiotherapy covered after knee surgery uae` · ○ `mri knee cost dubai` |
| 2 | Ophthalmology (Eye) | `does health insurance cover eye treatment uae` | 🟢 **Proven** | ⬤ `lasik eye cost` (1,110) · ⬤ `eye vision surgery cost` (882) · ⬤ `laser correction surgery cost` (692) · ⬤ `cataract surgery cost` (546) · ⬤ `cataract surgery cost in uae` (234) · ⬤ `lasik eye surgery cost` (166) · ○ `optical sub-limit health insurance uae` · ○ `are glasses covered by health insurance uae` · ○ `is cataract surgery covered by insurance uae` |
| 3 | ENT (Ear, Nose, Throat) | `does health insurance cover ent treatment uae` | 🟠 Thin | ⬤ `tonsillectomy in dubai` (159) · ⬤ `tonsil removal insurance coverage` (8) · ⬤ `tonsillitis treatment dubai` (7) · ⬤ `tonsillectomy insurance coverage` (3) · ⬤ `is tonsillitis covered by insurance` (2) · ○ `ent specialist consultation cost uae` · ○ `is sinus surgery covered by insurance uae` · ○ `grommet surgery cost dubai` · ○ `hearing test cover uae` |
| 4 | Dermatology (Skin) | `is dermatology covered by health insurance` | 🟡 Partial | ⬤ `skin treatment in dubai` (356) · ⬤ `is dermatology covered by insurance in uae` (136) · ⬤ `is dermatology covered by insurance` (45) · ⬤ `does insurance cover dermatology` (29) · ⬤ `dermatologist covered by insurance` (11) · ○ `dermatologist consultation cost dubai` · ○ `is acne treatment covered by insurance uae` · ○ `is laser treatment covered by insurance uae` · ○ `mole removal cover uae` |
| 5 | Cardiology (Heart) | `health insurance for heart patients uae` | 🟠 Thin | ⬤ `heart valve disease treatment in dubai` (56) · ⬤ `best insurance for heart patients` (24) · ⬤ `health insurance for heart patients` (23) · ⬤ `angioplasty cost dubai` (15) · ○ `cardiologist consultation cost dubai` · ○ `bypass surgery cost dubai insurance` · ○ `is angiography covered by insurance uae` · ○ `echo test cost dubai` |
| 6 | Family Medicine / GP | `gp consultation cost dubai` | 🟢 **Proven** | ⬤ `opd` (1,793) · ⬤ `opd full form` (245) · ⬤ `what is opd cover` (127) · ⬤ `private gp consultation fee dubai aed` (106) · ⬤ `what is opd` (89) · ⬤ `what is opd cover in health insurance` (53) · ○ `gp referral requirement uae insurance` · ○ `teleconsultation cover uae` |
| 7 | Alternative Medicine | `alternative medicine insurance uae` | 🟠 Thin | ⬤ `alternative medicine covered by insurance` (40) · ⬤ `what is alternative medicine in insurance` (15) · ⬤ `alternative medicine insurance` (3) · ○ `homeopathy cover health insurance uae` · ○ `ayurveda insurance uae` · ○ `chiropractic cover dubai` · ○ `acupuncture insurance uae` |
| 8 | Fertility / IVF | `is ivf covered by insurance uae` | 🟡 Partial | ⬤ `ivf cost in dubai` (241) · ⬤ `which insurance covers ivf in dubai` (183) · ⬤ `ivf covered by insurance in uae` (153) · ⬤ `ivf cost in abu dhabi` (145) · ⬤ `free ivf treatment in dubai` (114) · ⬤ `ivf treatment cost in uae` (99) · ○ `icsi cost uae insurance` · ○ `ivf waiting period insurance uae` · ○ `how many ivf cycles covered uae` |
| 9 | Psychiatry / Psychology | `is psychiatrist covered by insurance uae` | 🟢 **Proven** | ⬤ `is a psychiatrist covered by insurance` (1,079) · ⬤ `psychiatric care coverage` (795) · ⬤ `psychiatric care insurance` (556) · ○ `psychiatrist consultation cost dubai` · ○ `therapy session cost dubai insurance` · ○ `how many therapy sessions covered uae` · ○ `does insurance cover counselling uae` |
| 10 | Pediatrics | `paediatrician consultation cost dubai` | ⚪ Unmeasured | ○ `child specialist visit cover uae` · ○ `childhood vaccination cover uae` · ○ `paediatric dental cover uae` |
| 11 | Neurology | `neurologist consultation cost dubai` | 🟡 Partial | ⬤ `multiple sclerosis treatment in dubai` (239) · ⬤ `multiple sclerosis dubai` (114) · ⬤ `which plans cover stroke, cancer, and heart attack` (20) · ○ `brain mri cost dubai insurance` · ○ `epilepsy medication cover uae` · ○ `is eeg covered by insurance uae` |
| 12 | Gastroenterology | `health insurance for liver uae` | ⚪ Unmeasured | ○ `endoscopy cost dubai insurance` · ○ `colonoscopy cost uae` · ○ `is colonoscopy covered by insurance uae` · ○ `liver function test cover uae` |
| 13 | Endocrinology (Thyroid/Diabetes) | `health insurance for diabetes uae` | 🟠 Thin | ⬤ `health insurance for type 1 diabetes` (150) · ⬤ `diabetes insurance` (11) · ⬤ `best health insurance plan for diabetes` (9) · ○ `is insulin covered by insurance uae` · ○ `hba1c test cost dubai` · ○ `thyroid test cost dubai` · ○ `chronic medication cover uae` |
| 14 | Urology | `urologist consultation cost dubai` | 🟠 Thin | ⬤ `sukoon bupa circumcision coverage` (213) · ⬤ `free circumcision in sharjah` (15) · ⬤ `circumcision charges in zulekha hospital` (5) · ○ `kidney stone treatment cost uae` · ○ `lithotripsy cover uae` · ○ `prostate surgery cover uae` · ○ `is circumcision covered by insurance uae` |
| 15 | Gynecology | `gynaecologist consultation cost dubai` | 🟠 Thin | ⬤ `women health insurance` (2) · ○ `is smear test covered by insurance uae` · ○ `ultrasound cost dubai insurance` · ○ `fibroid surgery cover uae` · ○ `pcos treatment cover uae` |
| 16 | Physiotherapy / Rehab | `does insurance cover physiotherapy uae` | 🟢 **Proven** | ⬤ `physiotherapy is covered under insurance` (319) · ⬤ `is physiotherapy included in insurance` (316) · ⬤ `physiotherapy insurance coverage` (307) · ⬤ `is physiotherapy covered by insurance` (300) · ⬤ `physiotherapy claim insurance` (288) · ⬤ `physiotherapy coverage` (205) · ○ `how many physiotherapy sessions covered insurance uae` · ○ `physiotherapy cost dubai per session` · ○ `physiotherapy co-pay uae` |
| 17 | Allergy / Immunology | `is allergy testing covered by insurance uae` | ⚪ Unmeasured | ○ `allergy test cost dubai` · ○ `skin prick test cost uae` · ○ `immunotherapy cover uae` |
| 18 | Dentistry | `dental insurance uae` | 🟢 **Proven** | ⬤ `dental insurance` (2,071) · ⬤ `dental insurance dubai` (1,701) · ⬤ `best dental clinic in dubai` (1,675) · ⬤ `dental insurance in dubai` (779) · ⬤ `top 10 dental clinics in dubai` (718) · ○ `is dental covered by basic health insurance uae` · ○ `dental implant cost dubai insurance` · ○ `root canal cost dubai` · ○ `braces cover health insurance uae` · ○ `dental annual limit uae` |
| 19 | Emergency / Critical Care | `does insurance cover ambulance uae` | 🟠 Thin | ⬤ `emergency medical insurance` (230) · ○ `emergency room cost dubai` · ○ `out of network emergency cover uae` · ○ `er visit co-pay uae` |
| 20 | Oncology | `best health insurance for cancer uae` | 🟡 Partial | ⬤ `cancer insurance` (1,031) · ⬤ `free breast cancer screening dubai 2024` (244) · ⬤ `cancer protection health insurance plans` (172) · ⬤ `cancer treatment cost in dubai` (125) · ⬤ `stomach cancer cover in health insurance` (109) · ⬤ `breast cancer insurance` (62) · ○ `is chemotherapy covered by insurance uae` · ○ `cancer annual limit health insurance uae` · ○ `radiotherapy cost dubai` |
| 21 | Nephrology | `insurance for kidney patients uae` | 🟠 Thin | ⬤ `dialysis cost in dubai` (25) · ⬤ `free dialysis in dubai` (21) · ⬤ `dialysis insurance coverage` (15) · ⬤ `health insurance for dialysis patients` (13) · ○ `is dialysis covered by insurance uae` · ○ `dialysis annual limit uae` · ○ `kidney transplant cover uae` |
| 22 | Obstetrics (Maternity) | `maternity insurance uae` | 🟢 **Proven** | ⬤ `maternity insurance` (2,306) · ⬤ `maternity insurance dubai` (2,089) · ⬤ `pregnancy insurance` (1,175) · ⬤ `maternity insurance in uae` (1,170) · ⬤ `pregnancy insurance uae` (1,122) · ⬤ `maternity health insurance` (854) · ○ `maternity insurance waiting period uae` · ○ `c-section cost dubai insurance` · ○ `antenatal cover uae` · ○ `when to add newborn to health insurance uae` |
| 23 | Pulmonology | `is asthma covered by health insurance uae` | 🟠 Thin | ⬤ `asthma` (119) · ⬤ `asthma symptoms and treatment` (56) · ○ `asthma inhaler cost dubai` · ○ `copd treatment cover uae` · ○ `spirometry cost uae` |
| 24 | Radiology / Pathology | `mri cost dubai with insurance` | 🟠 Thin | ⬤ `insurance for lab tests` (55) · ○ `ct scan cost uae` · ○ `blood test cost dubai insurance` · ○ `does mri need pre approval uae` · ○ `x-ray cost dubai` |
| 25 | Rheumatology | `health insurance for arthritis uae` | 🟠 Thin | ⬤ `arthritis cover in health insurance` (2) · ○ `rheumatologist consultation cost dubai` · ○ `are biologics covered by insurance uae` · ○ `gout treatment cover uae` |
| 26 | Bariatric Surgery | `is bariatric surgery covered by insurance uae` | 🟠 Thin | ⬤ `bariatric surgery cost in uae` (5) · ⬤ `bariatric surgery dubai cost` (4) · ⬤ `how does obesity affect health insurance` (2) · ○ `gastric sleeve cost dubai` · ○ `bmi requirement bariatric insurance uae` |
| 27 | General Surgery | `health insurance for surgery uae` | 🟡 Partial | ⬤ `elective surgery meaning` (367) · ⬤ `what is elective surgery` (193) · ○ `does insurance cover day surgery uae` · ○ `surgery pre approval uae` · ○ `hernia surgery cost dubai` · ○ `room rate limit health insurance uae` |
| 28 | Plastic Surgery | `does insurance cover plastic surgery uae` | 🟡 Partial | ⬤ `gynecomastia dubai cost` (305) · ⬤ `gynecomastia surgery cost dubai` (260) · ⬤ `cosmetic dental insurance` (134) · ⬤ `cosmetic surgery` (127) · ⬤ `rhinoplasty cost in dubai` (68) · ○ `is reconstructive surgery covered uae` · ○ `cosmetic surgery exclusion insurance uae` · ○ `is breast reconstruction covered uae` |
| 29 | Vaccinations & screening (ADDED) | `does health insurance cover vaccinations uae` | 🟠 Thin | ⬤ `flu vaccine price in dubai` (254) · ○ `annual health check up insurance uae` · ○ `childhood vaccination schedule cover uae` |
| 30 | Pre-approval & network (ADDED) | `health insurance pre approval uae` | 🟢 **Proven** | ⬤ `what is a deductible insurance` (61,234) · ⬤ `mednet reimbursement form` (12,642) · ⬤ `nextcare reimbursement` (4,681) · ⬤ `adnic reimbursement form` (4,217) · ⬤ `gig reimbursement form` (2,920) · ⬤ `metlife reimbursement form` (2,825) · ○ `what is co-pay health insurance uae` · ○ `health insurance pre approval process uae` · ○ `network vs non network hospital uae` · ○ `who arranges pre approval uae` |

⬤ = measured, with PB's own 360d impressions in brackets · ○ = proposed target

### Demand status roll-up

| Status | Pages | Which |
|---|---|---|
| 🟢 **Proven** | 7 | Ophthalmology (Eye), Family Medicine / GP, Psychiatry / Psychology, Physiotherapy / Rehab, Dentistry, Obstetrics (Maternity), Pre-approval & network (ADDED) |
| 🟡 Partial | 7 | Orthopedics, Dermatology (Skin), Fertility / IVF, Neurology, Oncology, General Surgery, Plastic Surgery |
| 🟠 Thin | 13 | ENT (Ear, Nose, Throat), Cardiology (Heart), Alternative Medicine, Endocrinology (Thyroid/Diabetes), Urology, Gynecology, Emergency / Critical Care, Nephrology, Pulmonology, Radiology / Pathology, Rheumatology, Bariatric Surgery, Vaccinations & screening (ADDED) |
| ⚪ Unmeasured | 4 | Specialist cover hub, Pediatrics, Gastroenterology, Allergy / Immunology |

**What to do with this.** The 🟢 and 🟡 pages have measured demand PB already reaches and mostly fails to convert — build those first, they are the lowest-risk. The ⚪ and 🟠 pages are genuine bets: they may be untapped or they may be low-volume, and only a volume tool will tell you which. Sequence them last, and pull DataForSEO before committing budget to the whole tail.

---

## Per-page spec

### HUB. Specialist cover hub

| | |
|---|---|
| **URL** | `/health-insurance/cover/` |
| **Type** | Commercial · Wave 0 · Your list #— |
| **Title** | `Specialist Treatment Cost & Insurance Cover in the UAE \| Policybazaar.ae` |
| | 54 chars before brand · ✅ |
| **Description** | See what specialist care costs across the UAE, what your health plan actually pays, and which of 25+ insurers cover the treatment you need. Compare free. |
| | 153 chars · ✅ |
| **H1** | Specialist Treatment Costs & What Health Insurance Covers in the UAE |
| **Primary kw** | `specialist consultation cost uae` |
| **Demand** | ⚪ Unmeasured — 0 measured impressions across 0 queries |
| **Schema** | CollectionPage + BreadcrumbList + FAQPage + ItemList |
| **Existing overlap** | — · CTR — |

**○ Proposed secondary keywords** (no measured PB footprint)

`specialist visit co-pay uae` · `do i need a referral to see a specialist in dubai` · `specialist consultation fee abu dhabi`

### 1. Orthopedics

| | |
|---|---|
| **URL** | `/health-insurance/cover/orthopedic/` |
| **Type** | Article · Wave 1 · Your list #1 |
| **Title** | `Orthopedic Treatment Cost & Insurance Cover in the UAE \| Policybazaar.ae` |
| | 54 chars before brand · ✅ |
| **Description** | What orthopedic care costs in the UAE and what insurance pays: consultation, MRI, arthroscopy and joint replacement, plus pre-approval and physio limits. |
| | 153 chars · ✅ |
| **H1** | Orthopedic Treatment in the UAE: Costs, Cover & What Your Insurance Pays |
| **Primary kw** | `does health insurance cover orthopedic surgery uae` |
| **Demand** | 🟡 Partial — 1,209 measured impressions across 4 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 2 pages, 5,205 impr · CTR 0.077% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `does insurance cover knee replacement in dubai` | 938 | 0 🔴 | 6.3 |
| `knee replacement surgery cost dubai` | 227 | 0 🔴 | 77.3 |
| `knee replacement cost dubai` | 40 | 0 | 82.0 |
| `is knee replacement covered by insurance` | 4 | 0 | 4.0 |

**○ Proposed secondary keywords** (no measured PB footprint)

`orthopedic consultation cost dubai` · `arthroscopy cost uae insurance` · `is physiotherapy covered after knee surgery uae` · `mri knee cost dubai`

### 2. Ophthalmology (Eye)

| | |
|---|---|
| **URL** | `/health-insurance/cover/optical/` |
| **Type** | Article · Wave 2 · Your list #2 |
| **Title** | `Eye Care Cover in the UAE: Optical Limits, Cataract & LASIK \| Policybazaar.ae` |
| | 59 chars before brand · ✅ |
| **Description** | Optical usually sits in its own sub-limit and LASIK is usually excluded as elective. See what UAE plans pay for eye tests, glasses, cataract surgery and lenses. |
| | 160 chars · ✅ |
| **H1** | Eye Care Cover in the UAE: Optical Limits, Cataract & LASIK |
| **Primary kw** | `does health insurance cover eye treatment uae` |
| **Demand** | 🟢 **Proven** — 3,876 measured impressions across 8 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 5 pages, 50,176 impr · CTR 0.536% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `lasik eye cost` | 1,110 | 0 🔴 | 36.2 |
| `eye vision surgery cost` | 882 | 0 🔴 | 44.3 |
| `laser correction surgery cost` | 692 | 0 🔴 | 31.1 |
| `cataract surgery cost` | 546 | 5 | 8.6 |
| `cataract surgery cost in uae` | 234 | 1 | 12.8 |
| `lasik eye surgery cost` | 166 | 0 🔴 | 17.2 |
| `corporate dental and optical insurance uae` | 126 | 0 🔴 | 7.5 |
| `optical insurance plans` | 120 | 0 🔴 | 18.7 |

**○ Proposed secondary keywords** (no measured PB footprint)

`optical sub-limit health insurance uae` · `are glasses covered by health insurance uae` · `is cataract surgery covered by insurance uae`

### 3. ENT (Ear, Nose, Throat)

| | |
|---|---|
| **URL** | `/health-insurance/cover/ent/` |
| **Type** | Article · Wave 2 · Your list #3 |
| **Title** | `ENT Cover in the UAE: Ear, Nose & Throat Treatment Costs \| Policybazaar.ae` |
| | 56 chars before brand · ✅ |
| **Description** | ENT treatment is covered as ordinary surgery on most UAE plans. See what tonsillectomy, grommets, sinus surgery and hearing tests cost, and what needs approval. |
| | 160 chars · ✅ |
| **H1** | ENT Cover in the UAE: What Insurance Pays for Ear, Nose & Throat Care |
| **Primary kw** | `does health insurance cover ent treatment uae` |
| **Demand** | 🟠 Thin — 179 measured impressions across 5 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 1 page, 1,368 impr · CTR 1.316% ⭐ |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `tonsillectomy in dubai` | 159 | 0 🔴 | 86.2 |
| `tonsil removal insurance coverage` | 8 | 0 | 3.8 |
| `tonsillitis treatment dubai` | 7 | 0 | 87.0 |
| `tonsillectomy insurance coverage` | 3 | 0 | 3.0 |
| `is tonsillitis covered by insurance` | 2 | 1 | 29.5 |

**○ Proposed secondary keywords** (no measured PB footprint)

`ent specialist consultation cost uae` · `is sinus surgery covered by insurance uae` · `grommet surgery cost dubai` · `hearing test cover uae`

### 4. Dermatology (Skin)

| | |
|---|---|
| **URL** | `/health-insurance/cover/dermatology/` |
| **Type** | Article · Wave 1 · Your list #4 |
| **Title** | `Skin Treatment Cover in the UAE: Medical vs Cosmetic \| Policybazaar.ae` |
| | 52 chars before brand · ✅ |
| **Description** | UAE insurers cover medically necessary skin treatment and exclude cosmetic work. See where the line falls, what a visit costs, and what needs prior approval. |
| | 157 chars · ✅ |
| **H1** | Skin Treatment Cover in the UAE: Medical vs Cosmetic |
| **Primary kw** | `is dermatology covered by health insurance` |
| **Demand** | 🟡 Partial — 577 measured impressions across 5 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 3 pages, 30,729 impr · CTR 1.227% ⭐ |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `skin treatment in dubai` | 356 | 0 🔴 | 95.7 |
| `is dermatology covered by insurance in uae` | 136 | 6 | 2.8 |
| `is dermatology covered by insurance` | 45 | 4 | 47.8 |
| `does insurance cover dermatology` | 29 | 3 | 41.7 |
| `dermatologist covered by insurance` | 11 | 1 | 13.5 |

**○ Proposed secondary keywords** (no measured PB footprint)

`dermatologist consultation cost dubai` · `is acne treatment covered by insurance uae` · `is laser treatment covered by insurance uae` · `mole removal cover uae`

### 5. Cardiology (Heart)

| | |
|---|---|
| **URL** | `/health-insurance/cover/cardiac/` |
| **Type** | Article · Wave 2 · Your list #5 |
| **Title** | `Heart Treatment Cover in the UAE: Costs & Pre-approval \| Policybazaar.ae` |
| | 54 chars before brand · ✅ |
| **Description** | Cardiac care in the UAE almost always needs pre-approval. See what a cardiologist visit, angiography, angioplasty and bypass cost, and what your plan pays. |
| | 155 chars · ✅ |
| **H1** | Heart Treatment Cover in the UAE: Costs, Pre-approval & Limits |
| **Primary kw** | `health insurance for heart patients uae` |
| **Demand** | 🟠 Thin — 118 measured impressions across 4 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 5 pages, 11,683 impr · CTR 0.865% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `heart valve disease treatment in dubai` | 56 | 0 | 49.8 |
| `best insurance for heart patients` | 24 | 0 | 78.9 |
| `health insurance for heart patients` | 23 | 2 | 52.0 |
| `angioplasty cost dubai` | 15 | 0 | 59.3 |

**○ Proposed secondary keywords** (no measured PB footprint)

`cardiologist consultation cost dubai` · `bypass surgery cost dubai insurance` · `is angiography covered by insurance uae` · `echo test cost dubai`

### 6. Family Medicine / GP

| | |
|---|---|
| **URL** | `/health-insurance/cover/gp/` |
| **Type** | Article · Wave 2 · Your list #6 |
| **Title** | `GP & Primary Care Cover in the UAE: Costs and Referrals \| Policybazaar.ae` |
| | 55 chars before brand · ✅ |
| **Description** | The GP visit is where most claims start. See what a consultation costs across the Emirates, when your plan needs a referral first, and how OPD cover applies. |
| | 157 chars · ✅ |
| **H1** | GP Visits in the UAE: What They Cost and When You Need a Referral |
| **Primary kw** | `gp consultation cost dubai` |
| **Demand** | 🟢 **Proven** — 2,413 measured impressions across 6 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 2 pages, 12,640 impr · CTR 0.831% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `opd` | 1,793 | 0 🔴 | 8.0 |
| `opd full form` | 245 | 0 🔴 | 1.0 |
| `what is opd cover` | 127 | 0 🔴 | 17.9 |
| `private gp consultation fee dubai aed` | 106 | 0 🔴 | 2.1 |
| `what is opd` | 89 | 0 | 7.8 |
| `what is opd cover in health insurance` | 53 | 0 | 27.8 |

**○ Proposed secondary keywords** (no measured PB footprint)

`gp referral requirement uae insurance` · `teleconsultation cover uae`

### 7. Alternative Medicine

| | |
|---|---|
| **URL** | `/health-insurance/cover/alternative-medicine/` |
| **Type** | Article · Wave 3 · Your list #7 |
| **Title** | `Alternative Medicine Cover in the UAE: What Insurers Pay \| Policybazaar.ae` |
| | 56 chars before brand · ✅ |
| **Description** | Some UAE plans cover homeopathy, ayurveda, chiropractic and acupuncture up to a sub-limit. See which do, what the limits are, and what needs a referral first. |
| | 158 chars · ✅ |
| **H1** | Alternative Medicine Cover in the UAE: What Insurers Actually Pay |
| **Primary kw** | `alternative medicine insurance uae` |
| **Demand** | 🟠 Thin — 58 measured impressions across 3 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 1 page, 5,171 impr · CTR 0.309% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `alternative medicine covered by insurance` | 40 | 1 | 5.8 |
| `what is alternative medicine in insurance` | 15 | 0 | 5.9 |
| `alternative medicine insurance` | 3 | 0 | 77.7 |

**○ Proposed secondary keywords** (no measured PB footprint)

`homeopathy cover health insurance uae` · `ayurveda insurance uae` · `chiropractic cover dubai` · `acupuncture insurance uae`

### 8. Fertility / IVF

| | |
|---|---|
| **URL** | `/health-insurance/cover/ivf/` |
| **Type** | Article · Wave 1 · Your list #8 |
| **Title** | `IVF & Fertility Insurance Cover in the UAE: What's Paid \| Policybazaar.ae` |
| | 55 chars before brand · ✅ |
| **Description** | IVF cover varies more between UAE insurers than any other benefit. See typical cycle costs, which plans contribute, the per-cycle limits and waiting periods. |
| | 157 chars · ✅ |
| **H1** | IVF & Fertility Cover in the UAE: What Insurance Pays per Cycle |
| **Primary kw** | `is ivf covered by insurance uae` |
| **Demand** | 🟡 Partial — 1,020 measured impressions across 7 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 1 page, 20,443 impr · CTR 0.959% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `ivf cost in dubai` | 241 | 0 🔴 | 1.7 |
| `which insurance covers ivf in dubai` | 183 | 5 | 3.6 |
| `ivf covered by insurance in uae` | 153 | 2 | 7.2 |
| `ivf cost in abu dhabi` | 145 | 0 🔴 | 2.7 |
| `free ivf treatment in dubai` | 114 | 1 | 1.1 |
| `ivf treatment cost in uae` | 99 | 0 | 2.9 |
| `is ivf covered by insurance in dubai` | 85 | 4 | 4.8 |

**○ Proposed secondary keywords** (no measured PB footprint)

`icsi cost uae insurance` · `ivf waiting period insurance uae` · `how many ivf cycles covered uae`

### 9. Psychiatry / Psychology

| | |
|---|---|
| **URL** | `/health-insurance/cover/mental-health/` |
| **Type** | Article · Wave 2 · Your list #9 |
| **Title** | `Mental Health Cover in the UAE: Session Limits & Costs \| Policybazaar.ae` |
| | 54 chars before brand · ✅ |
| **Description** | Psychiatry and therapy cover in the UAE is capped by session and by year. See the limits, what a consultation costs, and which plans include psychology. |
| | 152 chars · ✅ |
| **H1** | Mental Health Cover in the UAE: Session Limits & What Insurers Pay |
| **Primary kw** | `is psychiatrist covered by insurance uae` |
| **Demand** | 🟢 **Proven** — 2,430 measured impressions across 3 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 8 pages, 26,805 impr · CTR 0.354% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `is a psychiatrist covered by insurance` | 1,079 | 0 🔴 | 11.5 |
| `psychiatric care coverage` | 795 | 0 🔴 | 17.9 |
| `psychiatric care insurance` | 556 | 0 🔴 | 19.9 |

**○ Proposed secondary keywords** (no measured PB footprint)

`psychiatrist consultation cost dubai` · `therapy session cost dubai insurance` · `how many therapy sessions covered uae` · `does insurance cover counselling uae`

### 10. Pediatrics

| | |
|---|---|
| **URL** | `/health-insurance/cover/paediatric/` |
| **Type** | Article · Wave 3 · Your list #10 |
| **Title** | `Paediatric Cover in the UAE: Child Specialist Visit Costs \| Policybazaar.ae` |
| | 57 chars before brand · ✅ |
| **Description** | What a paediatrician visit costs in the UAE and what your plan pays: consultations, childhood vaccinations, common procedures and the newborn enrolment window. |
| | 159 chars · ✅ |
| **H1** | Paediatric Care Cover in the UAE: Consultation Costs & Limits |
| **Primary kw** | `paediatrician consultation cost dubai` |
| **Demand** | ⚪ Unmeasured — 0 measured impressions across 0 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | ⚠️ see note · CTR 2.432% ⭐ |

**○ Proposed secondary keywords** (no measured PB footprint)

`child specialist visit cover uae` · `childhood vaccination cover uae` · `paediatric dental cover uae`

### 11. Neurology

| | |
|---|---|
| **URL** | `/health-insurance/cover/neurology/` |
| **Type** | Article · Wave 3 · Your list #11 |
| **Title** | `Neurology Cover in the UAE: Costs, Scans & Chronic Care \| Policybazaar.ae` |
| | 55 chars before brand · ✅ |
| **Description** | Neurology care often means repeat scans and long-term medication. See what a consultation, MRI and ongoing treatment cost, and how annual limits apply. |
| | 151 chars · ✅ |
| **H1** | Neurology Cover in the UAE: Consultation, Scans & Long-term Care |
| **Primary kw** | `neurologist consultation cost dubai` |
| **Demand** | 🟡 Partial — 373 measured impressions across 3 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 8 pages, 5,301 impr · CTR 0.434% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `multiple sclerosis treatment in dubai` | 239 | 0 🔴 | 67.9 |
| `multiple sclerosis dubai` | 114 | 0 🔴 | 58.9 |
| `which plans cover stroke, cancer, and heart attack` | 20 | 0 | 3.4 |

**○ Proposed secondary keywords** (no measured PB footprint)

`brain mri cost dubai insurance` · `epilepsy medication cover uae` · `is eeg covered by insurance uae`

### 12. Gastroenterology

| | |
|---|---|
| **URL** | `/health-insurance/cover/gastro/` |
| **Type** | Article · Wave 3 · Your list #12 |
| **Title** | `Gastroenterology Cover in the UAE: Endoscopy & Liver Care \| Policybazaar.ae` |
| | 57 chars before brand · ✅ |
| **Description** | Endoscopy and colonoscopy usually need pre-approval in the UAE. See what each costs, what liver and gut treatment is covered, and when screening qualifies. |
| | 155 chars · ✅ |
| **H1** | Gastroenterology Cover in the UAE: Endoscopy, Liver & Gut Treatment |
| **Primary kw** | `health insurance for liver uae` |
| **Demand** | ⚪ Unmeasured — 0 measured impressions across 0 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 4 pages, 4,623 impr · CTR 0.671% |

**○ Proposed secondary keywords** (no measured PB footprint)

`endoscopy cost dubai insurance` · `colonoscopy cost uae` · `is colonoscopy covered by insurance uae` · `liver function test cover uae`

### 13. Endocrinology (Thyroid/Diabetes)

| | |
|---|---|
| **URL** | `/health-insurance/cover/diabetes-thyroid/` |
| **Type** | Article · Wave 2 · Your list #13 |
| **Title** | `Diabetes & Thyroid Cover in the UAE: Medication & Tests \| Policybazaar.ae` |
| | 55 chars before brand · ✅ |
| **Description** | Chronic conditions are covered differently from one-off treatment. See what UAE plans pay for diabetes and thyroid medication, monitoring and routine tests. |
| | 156 chars · ✅ |
| **H1** | Diabetes & Thyroid Cover in the UAE: Medication, Tests & Limits |
| **Primary kw** | `health insurance for diabetes uae` |
| **Demand** | 🟠 Thin — 170 measured impressions across 3 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 5 pages, 12,120 impr · CTR 1.370% ⭐ |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `health insurance for type 1 diabetes` | 150 | 0 🔴 | 28.7 |
| `diabetes insurance` | 11 | 0 | 3.4 |
| `best health insurance plan for diabetes` | 9 | 0 | 84.3 |

**○ Proposed secondary keywords** (no measured PB footprint)

`is insulin covered by insurance uae` · `hba1c test cost dubai` · `thyroid test cost dubai` · `chronic medication cover uae`

### 14. Urology

| | |
|---|---|
| **URL** | `/health-insurance/cover/urology/` |
| **Type** | Article · Wave 3 · Your list #14 |
| **Title** | `Urology Cover in the UAE: Costs, Stones & Prostate Care \| Policybazaar.ae` |
| | 55 chars before brand · ✅ |
| **Description** | Kidney stones, prostate treatment and urinary procedures in the UAE: what each costs, what your plan pays, and which procedures need approval before booking. |
| | 157 chars · ✅ |
| **H1** | Urology Cover in the UAE: What Insurance Pays for Urinary Care |
| **Primary kw** | `urologist consultation cost dubai` |
| **Demand** | 🟠 Thin — 233 measured impressions across 3 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 🟢 GREENFIELD · CTR — |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `sukoon bupa circumcision coverage` | 213 | 0 🔴 | 7.1 |
| `free circumcision in sharjah` | 15 | 0 | 1.0 |
| `circumcision charges in zulekha hospital` | 5 | 0 | 76.0 |

**○ Proposed secondary keywords** (no measured PB footprint)

`kidney stone treatment cost uae` · `lithotripsy cover uae` · `prostate surgery cover uae` · `is circumcision covered by insurance uae`

### 15. Gynecology

| | |
|---|---|
| **URL** | `/health-insurance/cover/gynaecology/` |
| **Type** | Article · Wave 2 · Your list #15 |
| **Title** | `Gynaecology Cover in the UAE: Women's Health Visit Costs \| Policybazaar.ae` |
| | 56 chars before brand · ✅ |
| **Description** | Non-maternity women's health cover in the UAE: what a gynaecologist visit, smear test, ultrasound and common surgery cost, and what your plan pays toward each. |
| | 159 chars · ✅ |
| **H1** | Gynaecology Cover in the UAE: Consultations, Scans & Surgery |
| **Primary kw** | `gynaecologist consultation cost dubai` |
| **Demand** | 🟠 Thin — 2 measured impressions across 1 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 4 pages, 8,019 impr · CTR 0.960% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `women health insurance` | 2 | 2 | 4.0 |

**○ Proposed secondary keywords** (no measured PB footprint)

`is smear test covered by insurance uae` · `ultrasound cost dubai insurance` · `fibroid surgery cover uae` · `pcos treatment cover uae`

### 16. Physiotherapy / Rehab

| | |
|---|---|
| **URL** | `/health-insurance/cover/physiotherapy/` |
| **Type** | Article · Wave 1 · Your list #16 |
| **Title** | `Physiotherapy Cover in the UAE: Session Limits & Co-pay \| Policybazaar.ae` |
| | 55 chars before brand · ✅ |
| **Description** | Most UAE plans cap physiotherapy sessions per year and need a referral. See the session limits by plan tier, the co-pay per visit and what a session costs. |
| | 155 chars · ✅ |
| **H1** | Physiotherapy Cover in the UAE: Session Limits, Co-pay & Costs |
| **Primary kw** | `does insurance cover physiotherapy uae` |
| **Demand** | 🟢 **Proven** — 2,186 measured impressions across 9 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 1 page, 11,248 impr · CTR 0.533% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `physiotherapy is covered under insurance` | 319 | 0 🔴 | 2.2 |
| `is physiotherapy included in insurance` | 316 | 0 🔴 | 2.6 |
| `physiotherapy insurance coverage` | 307 | 1 | 2.7 |
| `is physiotherapy covered by insurance` | 300 | 0 🔴 | 22.6 |
| `physiotherapy claim insurance` | 288 | 0 🔴 | 3.7 |
| `physiotherapy coverage` | 205 | 0 🔴 | 2.5 |
| `physiotherapy covered by insurance` | 180 | 0 🔴 | 2.5 |
| `insurance for physiotherapy` | 170 | 0 🔴 | 3.8 |
| `does medical insurance cover physiotherapy` | 101 | 0 🔴 | 5.2 |

**○ Proposed secondary keywords** (no measured PB footprint)

`how many physiotherapy sessions covered insurance uae` · `physiotherapy cost dubai per session` · `physiotherapy co-pay uae`

### 17. Allergy / Immunology

| | |
|---|---|
| **URL** | `/health-insurance/cover/allergy/` |
| **Type** | Article · Wave 3 · Your list #17 |
| **Title** | `Allergy & Immunology Cover in the UAE: Tests & Treatment \| Policybazaar.ae` |
| | 56 chars before brand · ✅ |
| **Description** | Allergy testing is excluded by some UAE plans and capped by others. See what patch and blood testing cost, what immunotherapy involves, and what plans pay. |
| | 155 chars · ✅ |
| **H1** | Allergy Testing & Immunology Cover in the UAE |
| **Primary kw** | `is allergy testing covered by insurance uae` |
| **Demand** | ⚪ Unmeasured — 0 measured impressions across 0 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 🟢 GREENFIELD · CTR — |

**○ Proposed secondary keywords** (no measured PB footprint)

`allergy test cost dubai` · `skin prick test cost uae` · `immunotherapy cover uae`

### 18. Dentistry

| | |
|---|---|
| **URL** | `/health-insurance/cover/dental/` |
| **Type** | Article · Wave 1 · Your list #18 |
| **Title** | `Dental Insurance in the UAE: What's Covered & What Isn't \| Policybazaar.ae` |
| | 56 chars before brand · ✅ |
| **Description** | Most UAE plans treat dental as an add-on. See what basic and enhanced plans cover, typical costs from check-up to implant, and which insurers include dental. |
| | 157 chars · ✅ |
| **H1** | Dental Cover in the UAE: What Insurance Pays and What It Does Not |
| **Primary kw** | `dental insurance uae` |
| **Demand** | 🟢 **Proven** — 6,944 measured impressions across 5 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 4 pages, 317,945 impr · CTR 0.277% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `dental insurance` | 2,071 | 55 | 4.5 |
| `dental insurance dubai` | 1,701 | 77 | 5.4 |
| `best dental clinic in dubai` | 1,675 | 0 🔴 | 74.4 |
| `dental insurance in dubai` | 779 | 4 | 8.0 |
| `top 10 dental clinics in dubai` | 718 | 1 | 48.4 |

**○ Proposed secondary keywords** (no measured PB footprint)

`is dental covered by basic health insurance uae` · `dental implant cost dubai insurance` · `root canal cost dubai` · `braces cover health insurance uae` · `dental annual limit uae`

### 19. Emergency / Critical Care

| | |
|---|---|
| **URL** | `/health-insurance/cover/emergency/` |
| **Type** | Article · Wave 3 · Your list #19 |
| **Title** | `Emergency & Ambulance Cover in the UAE: What's Paid \| Policybazaar.ae` |
| | 51 chars before brand · ✅ |
| **Description** | Emergency care works differently from planned treatment, even out of network. See what an ER visit and ambulance cost, and when cover applies without approval. |
| | 159 chars · ✅ |
| **H1** | Emergency & Ambulance Cover in the UAE: What Your Plan Pays |
| **Primary kw** | `does insurance cover ambulance uae` |
| **Demand** | 🟠 Thin — 230 measured impressions across 1 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 1 page, 1,195 impr · CTR 0.167% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `emergency medical insurance` | 230 | 0 🔴 | 40.6 |

**○ Proposed secondary keywords** (no measured PB footprint)

`emergency room cost dubai` · `out of network emergency cover uae` · `er visit co-pay uae`

### 20. Oncology

| | |
|---|---|
| **URL** | `/health-insurance/cover/cancer/` |
| **Type** | Article · Wave 2 · Your list #20 |
| **Title** | `Cancer Cover in the UAE: Annual Limits, Costs & Exclusions \| Policybazaar.ae` |
| | 58 chars before brand · ✅ |
| **Description** | Cancer treatment is where annual limits actually bite. See what chemotherapy, radiotherapy and surgery cost in the UAE, and how limits and exclusions apply. |
| | 156 chars · ✅ |
| **H1** | Cancer Cover in the UAE: Annual Limits, Treatment Costs & Exclusions |
| **Primary kw** | `best health insurance for cancer uae` |
| **Demand** | 🟡 Partial — 1,743 measured impressions across 6 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 13 pages, 19,554 impr · CTR 0.900% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `cancer insurance` | 1,031 | 0 🔴 | 9.2 |
| `free breast cancer screening dubai 2024` | 244 | 0 🔴 | 32.6 |
| `cancer protection health insurance plans` | 172 | 0 🔴 | 16.7 |
| `cancer treatment cost in dubai` | 125 | 0 🔴 | 39.7 |
| `stomach cancer cover in health insurance` | 109 | 0 🔴 | 11.1 |
| `breast cancer insurance` | 62 | 0 | 37.5 |

**○ Proposed secondary keywords** (no measured PB footprint)

`is chemotherapy covered by insurance uae` · `cancer annual limit health insurance uae` · `radiotherapy cost dubai`

### 21. Nephrology

| | |
|---|---|
| **URL** | `/health-insurance/cover/kidney/` |
| **Type** | Article · Wave 3 · Your list #21 |
| **Title** | `Kidney & Dialysis Cover in the UAE: Costs & Limits \| Policybazaar.ae` |
| | 50 chars before brand · ✅ |
| **Description** | Dialysis is one of the highest recurring costs a plan can carry. See session costs, annual limits, and what UAE insurers pay toward long-term kidney treatment. |
| | 159 chars · ✅ |
| **H1** | Kidney & Dialysis Cover in the UAE: Costs and Annual Limits |
| **Primary kw** | `insurance for kidney patients uae` |
| **Demand** | 🟠 Thin — 74 measured impressions across 4 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 2 pages, 7,067 impr · CTR 2.052% ⭐ |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `dialysis cost in dubai` | 25 | 0 | 1.1 |
| `free dialysis in dubai` | 21 | 0 | 1.0 |
| `dialysis insurance coverage` | 15 | 0 | 58.5 |
| `health insurance for dialysis patients` | 13 | 1 | 68.2 |

**○ Proposed secondary keywords** (no measured PB footprint)

`is dialysis covered by insurance uae` · `dialysis annual limit uae` · `kidney transplant cover uae`

### 22. Obstetrics (Maternity)

| | |
|---|---|
| **URL** | `/health-insurance/cover/maternity/` |
| **Type** | Article · Wave 1 · Your list #22 |
| **Title** | `Maternity Insurance UAE: Cover, Limits & Waiting Periods \| Policybazaar.ae` |
| | 56 chars before brand · ✅ |
| **Description** | Maternity cover in the UAE explained: what antenatal care, delivery and C-section cost, the waiting periods that apply, and how to add a newborn to your plan. |
| | 158 chars · ✅ |
| **H1** | Maternity Cover in the UAE: Costs, Waiting Periods & Insurance Limits |
| **Primary kw** | `maternity insurance uae` |
| **Demand** | 🟢 **Proven** — 9,560 measured impressions across 7 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 4 pages, 148,782 impr · CTR 1.223% ⭐ |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `maternity insurance` | 2,306 | 41 | 5.2 |
| `maternity insurance dubai` | 2,089 | 9 | 19.2 |
| `pregnancy insurance` | 1,175 | 18 | 12.3 |
| `maternity insurance in uae` | 1,170 | 6 | 17.9 |
| `pregnancy insurance uae` | 1,122 | 31 | 9.1 |
| `maternity health insurance` | 854 | 10 | 7.3 |
| `maternity insurance already pregnant uae price` | 844 | 24 | 6.6 |

**○ Proposed secondary keywords** (no measured PB footprint)

`maternity insurance waiting period uae` · `c-section cost dubai insurance` · `antenatal cover uae` · `when to add newborn to health insurance uae`

### 23. Pulmonology

| | |
|---|---|
| **URL** | `/health-insurance/cover/respiratory/` |
| **Type** | Article · Wave 2 · Your list #23 |
| **Title** | `Respiratory Cover in the UAE: Asthma, COPD & Lung Care \| Policybazaar.ae` |
| | 54 chars before brand · ✅ |
| **Description** | Asthma and COPD are treated as chronic conditions by UAE insurers. See what inhalers, lung function tests and specialist visits cost, and what plans cover. |
| | 155 chars · ✅ |
| **H1** | Respiratory Cover in the UAE: Asthma, COPD and Lung Treatment |
| **Primary kw** | `is asthma covered by health insurance uae` |
| **Demand** | 🟠 Thin — 175 measured impressions across 2 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 5 pages, 6,222 impr · CTR 0.096% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `asthma` | 119 | 0 🔴 | 1.0 |
| `asthma symptoms and treatment` | 56 | 0 | 1.0 |

**○ Proposed secondary keywords** (no measured PB footprint)

`asthma inhaler cost dubai` · `copd treatment cover uae` · `spirometry cost uae`

### 24. Radiology / Pathology

| | |
|---|---|
| **URL** | `/health-insurance/cover/diagnostics/` |
| **Type** | Article · Wave 3 · Your list #24 |
| **Title** | `MRI, Scan & Lab Test Costs in the UAE With Insurance \| Policybazaar.ae` |
| | 52 chars before brand · ✅ |
| **Description** | Scans and lab tests are where pre-approval most often catches people out. See what an MRI, CT, X-ray and blood panel cost, and what your plan pays toward each. |
| | 159 chars · ✅ |
| **H1** | Scans & Lab Tests in the UAE: Costs, Pre-approval & Cover |
| **Primary kw** | `mri cost dubai with insurance` |
| **Demand** | 🟠 Thin — 55 measured impressions across 1 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 1 page, 8,023 impr · CTR 0.399% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `insurance for lab tests` | 55 | 0 | 2.1 |

**○ Proposed secondary keywords** (no measured PB footprint)

`ct scan cost uae` · `blood test cost dubai insurance` · `does mri need pre approval uae` · `x-ray cost dubai`

### 25. Rheumatology

| | |
|---|---|
| **URL** | `/health-insurance/cover/rheumatology/` |
| **Type** | Article · Wave 3 · Your list #25 |
| **Title** | `Rheumatology Cover in the UAE: Arthritis & Autoimmune \| Policybazaar.ae` |
| | 53 chars before brand · ✅ |
| **Description** | Arthritis and autoimmune conditions need long-term treatment and often biologics. See what UAE plans pay, which drugs need approval, and how limits apply. |
| | 154 chars · ✅ |
| **H1** | Rheumatology Cover in the UAE: Arthritis and Autoimmune Treatment |
| **Primary kw** | `health insurance for arthritis uae` |
| **Demand** | 🟠 Thin — 2 measured impressions across 1 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 3 pages, 995 impr · CTR 0.603% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `arthritis cover in health insurance` | 2 | 0 | 1.5 |

**○ Proposed secondary keywords** (no measured PB footprint)

`rheumatologist consultation cost dubai` · `are biologics covered by insurance uae` · `gout treatment cover uae`

### 26. Bariatric Surgery

| | |
|---|---|
| **URL** | `/health-insurance/cover/bariatric/` |
| **Type** | Article · Wave 2 · Your list #26 |
| **Title** | `Bariatric Surgery Cover in the UAE: When Insurance Pays \| Policybazaar.ae` |
| | 55 chars before brand · ✅ |
| **Description** | Weight-loss surgery is excluded by most UAE plans unless strict medical criteria are met. See the criteria, the typical cost, and what approval requires. |
| | 153 chars · ✅ |
| **H1** | Bariatric Surgery Cover in the UAE: When Insurance Pays |
| **Primary kw** | `is bariatric surgery covered by insurance uae` |
| **Demand** | 🟠 Thin — 11 measured impressions across 3 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 3 pages, 1,733 impr · CTR 0.981% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `bariatric surgery cost in uae` | 5 | 0 | 47.4 |
| `bariatric surgery dubai cost` | 4 | 0 | 52.5 |
| `how does obesity affect health insurance` | 2 | 0 | 1.0 |

**○ Proposed secondary keywords** (no measured PB footprint)

`gastric sleeve cost dubai` · `bmi requirement bariatric insurance uae`

### 27. General Surgery

| | |
|---|---|
| **URL** | `/health-insurance/cover/surgery/` |
| **Type** | Article · Wave 3 · Your list #27 |
| **Title** | `Surgery Cover in the UAE: Costs, Pre-approval & Limits \| Policybazaar.ae` |
| | 54 chars before brand · ✅ |
| **Description** | Most surgery in the UAE needs pre-approval and carries a co-pay. See how day surgery and inpatient cover differ, what the limits are, and who arranges approval. |
| | 160 chars · ✅ |
| **H1** | Surgery Cover in the UAE: What Your Plan Pays and What Needs Approval |
| **Primary kw** | `health insurance for surgery uae` |
| **Demand** | 🟡 Partial — 560 measured impressions across 2 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 3 pages, 12,625 impr · CTR 0.301% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `elective surgery meaning` | 367 | 0 🔴 | 1.5 |
| `what is elective surgery` | 193 | 0 🔴 | 1.0 |

**○ Proposed secondary keywords** (no measured PB footprint)

`does insurance cover day surgery uae` · `surgery pre approval uae` · `hernia surgery cost dubai` · `room rate limit health insurance uae`

### 28. Plastic Surgery

| | |
|---|---|
| **URL** | `/health-insurance/cover/cosmetic-reconstructive/` |
| **Type** | Article · Wave 3 · Your list #28 |
| **Title** | `Cosmetic vs Reconstructive Surgery: UAE Insurance Rules \| Policybazaar.ae` |
| | 55 chars before brand · ✅ |
| **Description** | UAE insurers exclude cosmetic surgery and cover reconstructive procedures. See where the line falls, and the documentation that decides which side you land on. |
| | 159 chars · ✅ |
| **H1** | Cosmetic vs Reconstructive Surgery: What UAE Insurance Covers |
| **Primary kw** | `does insurance cover plastic surgery uae` |
| **Demand** | 🟡 Partial — 894 measured impressions across 5 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 3 pages, 13,790 impr · CTR 0.464% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `gynecomastia dubai cost` | 305 | 0 🔴 | 32.4 |
| `gynecomastia surgery cost dubai` | 260 | 0 🔴 | 34.2 |
| `cosmetic dental insurance` | 134 | 0 🔴 | 17.3 |
| `cosmetic surgery` | 127 | 0 🔴 | 70.2 |
| `rhinoplasty cost in dubai` | 68 | 0 | 52.1 |

**○ Proposed secondary keywords** (no measured PB footprint)

`is reconstructive surgery covered uae` · `cosmetic surgery exclusion insurance uae` · `is breast reconstruction covered uae`

### 29. Vaccinations & screening (ADDED)

| | |
|---|---|
| **URL** | `/health-insurance/cover/vaccinations/` |
| **Type** | Article · Wave 3 · Your list #＋ |
| **Title** | `Vaccination & Screening Cover in the UAE: What's Included \| Policybazaar.ae` |
| | 57 chars before brand · ✅ |
| **Description** | Some vaccinations and screenings are mandated, some are an add-on, some excluded. See which UAE plans pay for childhood, travel and flu vaccines and check-ups. |
| | 159 chars · ✅ |
| **H1** | Vaccination & Health Screening Cover in the UAE |
| **Primary kw** | `does health insurance cover vaccinations uae` |
| **Demand** | 🟠 Thin — 254 measured impressions across 1 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 4 pages, 15,042 impr · CTR 0.412% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `flu vaccine price in dubai` | 254 | 0 🔴 | 83.5 |

**○ Proposed secondary keywords** (no measured PB footprint)

`annual health check up insurance uae` · `childhood vaccination schedule cover uae`

### 30. Pre-approval & network (ADDED)

| | |
|---|---|
| **URL** | `/health-insurance/cover/pre-approval/` |
| **Type** | Article · Wave 0 · Your list #＋ |
| **Title** | `Pre-approval, Networks & Co-pay in UAE Health Insurance \| Policybazaar.ae` |
| | 55 chars before brand · ✅ |
| **Description** | The four things that decide what you actually pay in the UAE: network, referral, pre-approval and co-pay. What each one means, and who arranges it. |
| | 147 chars · ✅ |
| **H1** | Pre-approval, Networks & Co-pay: How UAE Health Cover Actually Works |
| **Primary kw** | `health insurance pre approval uae` |
| **Demand** | 🟢 **Proven** — 88,519 measured impressions across 6 queries |
| **Schema** | MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy |
| **Existing overlap** | 5 pages, 37,480 impr · CTR 0.707% |

**⬤ Measured secondary keywords** (PB's own 360d GSC data)

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `what is a deductible insurance` | 61,234 | 0 🔴 | 5.5 |
| `mednet reimbursement form` | 12,642 | 123 | 6.3 |
| `nextcare reimbursement` | 4,681 | 9 | 8.8 |
| `adnic reimbursement form` | 4,217 | 22 | 8.4 |
| `gig reimbursement form` | 2,920 | 18 | 8.1 |
| `metlife reimbursement form` | 2,825 | 16 | 7.6 |

**○ Proposed secondary keywords** (no measured PB footprint)

`what is co-pay health insurance uae` · `health insurance pre approval process uae` · `network vs non network hospital uae` · `who arranges pre approval uae`

---

## Validation

| Check | Result |
|---|---|
| Pages specified | ✅ 31 (1 hub + 28 specialties + 2 additions) |
| All 28 of your specialties present | ✅ 28/28 |
| Titles 35–60 chars (pre-brand) | ✅ all 31 |
| Descriptions 140–160 chars | ✅ all 31 |
| Unique slugs / H1s / primary kws | ✅ 31 / 31 / 31 |
| Measured secondary keywords | 108 across 27 pages |
| Proposed secondary keywords | 106 |
| Duplicate keyword assignments | ✅ none |

### Publish blockers

| Blocker | Effect if ignored |
|---|---|
| 🔴 **No DHA-licensed reviewer engaged** | Schema drops to `Article`; "Medically reviewed" banner cannot ship |
| 🔴 **All AED figures are designer placeholders** | Every cost table unpublishable until sourced |
| 🔴 **`/author/*` soft-404s** | `reviewedBy` points at a dead entity |
| 🟡 **Legal sign-off on named insurer limits pending** | Insurer matrix ships switched off |
| 🟡 **No DataForSEO credentials** | The 12 ⚪/🟠 pages remain unvalidated bets |
