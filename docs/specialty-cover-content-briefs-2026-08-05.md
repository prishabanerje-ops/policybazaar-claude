# Specialty Cover — Content Briefs (Hub + Spokes)

**Prepared:** 5 August 2026 · **Vertical:** Health Insurance, policybazaar.ae
**Design source:** Figma `FTCKGnzdCT1AMeMxk01cju`. Spoke node `33034-15963` ("02 Orthopedic Page", 1440×7510) read via Figma MCP, so all spoke copy below is the exact text layer. Hub frame ("01 Doctor Specific Pages", 1440×5789) read from the supplied PNG.
**Read first:** `specialty-cover-seo-aio-strategy-2026-08-05.md`
**Disposition of existing pages:** `specialty-cover-content-requirements-cannibalisation-2026-08-05.md`

---

## How to use this document

Two briefs, one per template. §4 is the hub, §5 is the spoke. Both are organised block by block in Figma order, each block marked:

| Mark | Meaning |
|---|---|
| **KEEP** | Ships as designed. Copy may need sourcing, structure does not change |
| **REWRITE** | Block stays, copy or target changes. New requirement stated |
| **CUT** | Remove |
| **ADD** | Not in the Figma, needs designing |
| **FIX** | Design defect, not a content decision. Also in §3 |

§6 carries the per-spoke variables for all 21 topics (20 of which get built, see the note at §6). §7 is the sourcing checklist that gates publish. Orthopedics is the worked example throughout because it is the one fully designed.

---

## 1. Global rules, every page

**Voice.** Plain and specific. No inflated significance, no "in today's fast-paced world," no rule-of-three flourishes. The reader has a bill coming and wants a number. Register stays technical where the content is regulatory.

**The one rule that matters most.** Every page answers an insurance question, never a provider-discovery question. Details in the strategy doc §3. In practice: never promise to find, list, browse, rank or book a doctor. PB has no doctor data. Every instance of that promise in the current design is marked REWRITE below.

**Numbers.**
- No AED figure ships without a named source and a capture date (§7). All figures currently in the Figma are placeholders per decision 4.
- Ranges use an en dash and a space-free form: `AED 250–700`.
- Every table with prices or limits carries a visible "Verified [Month Year]" line.
- Never state a single price where a range is honest.

**One claim per sentence** in any cover, cost, limit or exclusion section. Compound sentences do not survive extraction into AI answers.

**Direct-answer block.** 40 to 60 words directly under the H1, answering the page's head question, with the key number in it. This is the single highest-value paragraph on the page for both featured snippets and AI answers. Write it first, not last.

**Regulators.** DHA for Dubai, DOH for Abu Dhabi, MOHAP for the northern emirates. Name them accurately and never interchangeably. For the insurance statute, the current law is **Federal Decree-Law No. (6) of 2025**; the 2007 and 2023 laws are both repealed. Verify at `rulebook.centralbank.ae`. Never cite it from memory.

**Spelling.** Pick one register and hold it. UAE market convention is British English (`orthopaedic`, `paediatric`, `gynaecologist`). PB's own GSC data shows searchers use the American form far more (`orthopedic` 78 queries / 247 impressions versus `orthopaedic` 4 / 4), though on a footprint too small to be decisive. **Recommendation: American spelling in H1, title and slug to match search demand; include the British spelling once in body copy so both are on the page.** The current design mixes them within a single page, which is the one thing that is definitely wrong. See §3 D9 and D13.

**Word counts.** Hub 1,400 to 1,800. Spoke 2,200 to 3,000. PB's existing health pages run a median of 2,763 words, so a spoke shorter than 2,200 will look thin beside its own siblings. Do not pad to hit a number.

**Internal links.** Every spoke: one up to the hub, two or three lateral to genuinely related spokes, and links down to the existing pages its disposition says to keep. Relatedness must be real. Orthopedics to physiotherapy is real because post-surgical rehab draws on the session cap. Orthopedics to dentistry is not.

---

## 2. What both templates must stop claiming

Quoted verbatim from the Figma. All four are content-only impossibilities.

| Where | Current | Replace with |
|---|---|---|
| Hub H1 | "Find a Doctor in UAE by Specialty - Costs & Insurance" | "Specialist Treatment Costs & What Health Insurance Covers in the UAE" |
| Hub sub-head | "Browse DHA & DOH-licensed specialists across Dubai, Abu Dhabi & Sharjah, see real consultation costs, and get covered from AED 4 / day" | "See what specialist care costs across the Emirates, what your health plan actually pays toward it, and which of 25+ UAE insurers cover the treatment you need." |
| Hub step 3 | "Visit a covered doctor — Book a DHA, DOH or MOHAP-licensed specialist and pay only your co-pay" | "Confirm cover before you book — Check your network, co-pay and pre-approval so the visit costs what you expect." |
| Hub FAQ 3 | "Are the doctors DHA / DOH licensed?" | "How do I check a doctor is DHA or DOH licensed?" (answer points at the regulator's own verification tool, which is genuinely useful and honest about PB's role) |

Same issue in the spoke's "How to Find an Orthopedic Doctor in the UAE." Handled at §5 block 18.

---

## 3. Figma defects (14)

Design pass, separate from content. Numbered for ticketing.

### Spoke

| # | Defect | Evidence |
|---|---|---|
| **D1** | Cost table row 1 is duplicated. "Specialist consultation (clinic) / AED 250–400 / CO-PAY ONLY" appears twice in consecutive rows | Figma text layers, cost table |
| **D2** | The KEY POINT block is duplicated. Identical text ("You don't always need a fracture or surgery…") appears after *Conditions* and again after *Training & Qualifications* | Two identical text layers |
| **D3** | Regulator row is wrong. "Department of Health / Abu Dhabi" appears **twice** and **DHA / Dubai is absent entirely**, despite the trust banner naming "DHA (Dubai), DOH (Abu Dhabi) & MOHAP (northern emirates)" | Three cards: DOH Abu Dhabi, DOH Abu Dhabi, MOHAP Northern emirates |
| **D4** | Breadcrumb contains a stray crumb: `Home > Articles > Health Guides > **Toyota** > What Is an Orthopedic Doctor in UAE?` | Text layer named "Toyota" |
| **D5** | The TOC component frame is named "Gold-valu Calculator" | Frame `33034:15964`. Template copy artifact. Confirm the component carries no calculator logic |
| **D6** | Byline gives one person two conflicting roles: "Dr. Aarti Menon — MBBS, MPH · **Medical Reviewer**" and "**Senior Health Editor** · MBBS, MPH · Policybazaar.ae" | Adjacent text layers |
| **D7** | "DHA RECOMMENDED" badge on the conservative-treatment column. DHA does not endorse treatment pathways. Unsupportable as drawn | Badge layer |
| **D8** | "DHA LICENSED" badge on the surgical-treatment column. Licensing attaches to practitioners and facilities, not procedures | Badge layer |
| **D9** | Spelling mixed within one page: "Paediatric Ortho" (British) against "Orthopedic" (American) throughout | Sub-specialty tile vs H1 |
| **D10** | Surgical column is labelled "4 procedures" but lists **5**: joint replacement, internal fixation, spinal fusion, arthroscopy, soft-tissue repair | Label vs items |

### Hub

| # | Defect | Evidence |
|---|---|---|
| **D11** | The Dubai card in "Find Doctors & Cover by Emirate" has **no body copy**. Abu Dhabi and Sharjah both have it. Dubai is the largest market and DHA the most-searched regulator | Empty card |
| **D12** | "Specialists across 12 fields" and "Choose from 12 specialties" against 28 proposed and 21 planned | Hero USP, step 1 |
| **D13** | Spelling mixed inside one grid: "Gynaecologist" (British) beside "Pediatrician" (American) | Specialty grid |
| **D14** | Breadcrumb is `Home > Health Insurance`, omitting the hub itself. Needs `Home > Health Insurance > Cover & Costs` so `BreadcrumbList` can express the hub-spoke relationship | Breadcrumb |

**Separate from the 14, and a content fix:** the hub states "health insurance is mandatory in Dubai and Abu Dhabi." Out of date since 1 January 2025. Strategy doc §9 has the correction and the sources.

---

## 4. HUB BRIEF

**URL:** `/health-insurance/cover/` (verified 404 today, so free)
**Title tag:** `Specialist Treatment Costs & Insurance Cover in the UAE | Policybazaar.ae` (≤60 chars for the distinctive part)
**Meta description:** Lead with the cost range and the co-pay promise, not with "browse specialists."
**Target intent:** what specialist care costs and what a plan pays toward it
**Head queries:** `specialist consultation cost uae`, `does health insurance cover specialist visits uae`, `specialist co-pay uae`, `do i need a gp referral to see a specialist in dubai`
**Schema:** `CollectionPage` + `BreadcrumbList` (3 levels) + `FAQPage` + `ItemList` enumerating all live spokes
**Words:** 1,400 to 1,800

| # | Figma block | Mark | Requirement |
|---|---|---|---|
| 1 | Utility bar, nav | KEEP | No change |
| 2 | **H1** "Find a Doctor in UAE by Specialty / - Costs & Insurance" | **REWRITE** | → "Specialist Treatment Costs & What Health Insurance Covers in the UAE". Keep the two-tone treatment; put "Costs & Cover" in the accent colour |
| 3 | Sub-copy + Read More | **REWRITE** | Per §2. Must not say browse or specialists-you-can-see |
| 4 | 3 hero USPs | **REWRITE** | Item 1 currently "DHA, DOH & MOHAP-licensed / Specialists across 12 fields" → "Cover checked against DHA, DOH & MOHAP rules / 21 treatment guides". Items 2 and 3 KEEP. Fixes D12 |
| 5 | Hero image | KEEP | Doctor collage is fine. Alt text describes specialist care in the UAE, not "find a doctor" |
| 6 | Quote widget | KEEP | The 5 segments (Self Only, Both Self and Family, Family without Self, Domestic Workers, Investor) and "AED 1 million Health cover starting @4/Day" are existing product copy. Verify the AED 4/day claim is current before publish |
| 7 | Trust bar | KEEP | 4.7/5, 40,413 reviews, 2M+ customers, 35+ partners, 1M+ policies. Confirm all five are current |
| 8 | Breadcrumb | **FIX (D14)** | `Home > Health Insurance > Cover & Costs` |
| 9 | **ADD** | **ADD** | **Direct-answer block**, 40 to 60 words, immediately under H1 or the trust bar. Must contain the consultation range and the co-pay reality. This is the AI-answer target for the whole cluster |
| 10 | "DOCTORS BY SPECIALTY" / "Choose a specialty to get started" | **REWRITE** | Eyebrow → "COVER BY TREATMENT". H2 → "Find what your plan covers". Sub-copy KEEP, it is already accurate: "Each specialty has a dedicated guide — conditions treated, typical costs in AED, and how UAE health insurance covers it" |
| 11 | Specialty grid, 2 featured + 10 | **REWRITE** | Card set becomes the 21 topics from strategy §6, not the current 12. Twenty cards point at new spokes; the children's-cover card points at the existing `health-insurance-for-kids-hiart/` page (see the note at §6). Featured two stay Orthopedic and Cardiology only if both are live; in wave 1 feature **Dentistry** and **Orthopedics** instead, since dental carries 270,343 impressions. Each card: benefit name, one line on the cover question, "View cover guide →". Fixes D12, D13 |
| 12 | "HOW IT WORKS" / "See a covered specialist in 3 steps" | **REWRITE** | Steps 1 and 2 KEEP. **Step 3 rewrite per §2** |
| 13 | "Consultation Costs in AED" table | **KEEP structure, RESOURCE all figures** | 6 rows today (Orthopedic 250–700, Eye 200–500, ENT 200–500, Dermatology 250–600, Dentist 150–450, Cardiologist 300–700). Extend to all live spokes. **Every figure is a placeholder** (decision 4). Add "Verified [Month Year]". Footnote KEEP, it is well written. Keep the WITH INSURANCE badge column, it is the most extractable element on the page |
| 14 | "Why Specialist Care Needs the Right Plan" | **REWRITE para 1** | Para 1 carries the mandate error. Correct per strategy §9. Para 2 KEEP. The 3 trust items KEEP. Image caption KEEP |
| 15 | "What to Check Before Booking" / "How health insurance covers doctor visits", 4 cards | **KEEP** | Network, Referral, Pre-approval, Co-pay & limits. Best section in the design: accurate, useful, and PB's actual territory. Add a link from each card to the `pre-approval` spoke. In the Co-pay card, add the physiotherapy session number once sourced |
| 16 | "Find Doctors & Cover by Emirate", 3 cards | **REWRITE + FIX (D11)** | H2 → "Cover Rules by Emirate". **Write the missing Dubai/DHA copy.** Abu Dhabi and Sharjah copy KEEP, both accurate. **ADD a 4th card** or extend Sharjah's to name all five northern emirates, and reflect the 1 Jan 2025 mandate |
| 17 | "Cover for every situation", 6 cards | KEEP | Family, Kids, Parents, Maternity, Dental, Individual. All six map to real pages. Point Maternity and Dental at the new spokes once live, not the old articles |
| 18 | FAQ, 6 items | **REWRITE Q3** | Q1 KEEP (its answer is already a model direct answer). Q2, Q4, Q5, Q6 KEEP. **Q3 rewrite per §2.** All answers 40 to 60 words, one claim per sentence. Emit `FAQPage` |
| 19 | Footer | KEEP | The "Editorial Guidelines" link is an E-E-A-T asset. Make sure it survives |
| 20 | **ADD** | **ADD** | **Insurer cover matrix** (decision 6): which of the 25+ insurers cover the highest-interest benefits, with limits. Legal sign-off gated. Build it as a switchable module so the page ships without it if legal slips |

---

## 5. SPOKE BRIEF

Master template. Orthopedics is the worked example. §6 supplies the per-page variables.

**URL:** `/health-insurance/cover/{benefit-slug}/` — e.g. `/health-insurance/cover/orthopedic/`
**Title tag pattern:** `{Benefit} Cover in the UAE: Costs, Limits & What Insurance Pays | Policybazaar.ae`
**Schema:** `MedicalWebPage` + `BreadcrumbList` (4 levels) + `FAQPage` + `author` + `reviewedBy`
→ **`Article`, not `MedicalWebPage`, until the DHA-licensed reviewer from decision 5 is engaged and has a live author profile page.** Emitting `reviewedBy` without a real reviewer is a false claim in structured data on YMYL content.
**Words:** 2,200 to 3,000

| # | Figma block | Mark | Requirement |
|---|---|---|---|
| 1 | Utility bar, nav | KEEP | |
| 2 | Breadcrumb | **FIX (D4)** | Remove "Toyota". Set `Home > Health Insurance > Cover & Costs > {Benefit}` |
| 3 | Eyebrow tags 📖 GUIDE · 🦴 ORTHOPEDIC · 🇦🇪 UAE | KEEP | Nice trust and scannability signal. Per-page emoji in §6 |
| 4 | **H1** "Orthopedic Doctor in the UAE: Conditions, Treatments, Costs & How to Find One" | **REWRITE** | → "Orthopedic Treatment in the UAE: Costs, Cover & What Your Insurance Pays". Drops the provider promise, keeps cost and cover. Per-page H1s in §6 |
| 5 | Standfirst | **REWRITE** | Current one ends "…how to find a DHA/DOH-licensed specialist in the UAE." Replace that clause with the cover question. Keep the plain, specific tone, it is good |
| 6 | Byline | **FIX (D6) + BLOCKED** | One person, one role. Ships only once the real clinician is engaged. Until then: existing insurance reviewer, `Article` schema, no MBBS string, no clinical-review claim |
| 7 | "Medically reviewed & UAE-localised" banner | **BLOCKED on decision 5** | Copy itself is good and the "Always confirm cover with your insurer before booking" clause should stay regardless. The *medical review* claim cannot ship before the reviewer exists |
| 8 | Right rail: TOC (9 items) + sticky CTA | KEEP | TOC labels are well chosen and short. Sticky CTA "Cover your ortho care" / "Make sure your health plan covers specialist visits, physiotherapy and joint surgery." / "Get a Quote ›" is the best-targeted CTA in the design. Keep the pattern, vary per benefit |
| 9 | Updated + read time | KEEP | Must match schema `dateModified` exactly. Not a static string |
| 10 | Intro, 2 paras | KEEP | Currently well written and genuinely UAE-localised ("active lifestyles, sports, and desk-based work") |
| 11 | **ADD** | **ADD** | **Direct-answer block**, 40 to 60 words, immediately after the intro. Must contain the headline cost range and the cover reality. For orthopedics: consultation range, surgery range, pre-approval requirement, physio cap |
| 12 | Hero image | KEEP | Alt text describes the care, not "find a doctor" |
| 13 | H2 "What Do Orthopedic Doctors Do?" + 3 bullets | KEEP | Establishes topical depth, which the YMYL and consensus scoring both want |
| 14 | H3 "Common sub-specialty areas include", 8 tiles | **KEEP + FIX (D9)** | Spine Surgery, Hip & Knee, Hand & Wrist, Shoulder & Elbow, Foot & Ankle, Sports Medicine, Trauma Surgery, Paediatric Ortho. Fix the spelling mix. The closing note about matching sub-specialty to concern is good, keep it |
| 15 | H2 "Conditions Orthopedic Doctors Treat", 9 cards | KEEP | Bone fractures, muscle strains, joint/back pain, arthritis, carpal tunnel, sprains & tendonitis, ACL/ligament tears, limb abnormalities, bone cancer. Descriptors are UAE-localised already ("common among desk workers in the UAE", "football and basketball players"). Keep that |
| 16 | KEY POINT callout | **FIX (D2)** | Keep the first instance. Write a different one for the second position, or cut it |
| 17 | H2 "Treatments & Procedures", 2 columns | **KEEP + FIX (D7, D8, D10)** | Content is good. Remove both DHA badges. Correct the count to 5 |
| 18 | Mid-content CTA "Find DHA-Licensed Orthopedic Doctors Near You" | **REWRITE heading** | → "Check What Your Plan Covers for Orthopedic Care". The body copy already says the right thing: "Check what your plan covers for consultations, scans and surgery — and compare 25+ UAE insurers in 2 minutes." Heading contradicts its own body |
| 19 | H2 "When Should You See an Orthopedic Doctor?", 5 items | KEEP | Clinically useful, appropriately hedged, closes with a genuine safety note. Once a clinician reviews, this is the section that earns the `MedicalWebPage` claim |
| 20 | H2 "Training & Qualifications (UAE)" + 3 regulator cards | **KEEP + FIX (D3)** | Body copy KEEP. **Card row must be DHA/Dubai, DOH/Abu Dhabi, MOHAP/northern emirates.** Currently DOH twice, DHA missing |
| 21 | H2 "How to Find an Orthopedic Doctor in the UAE", 4 steps | **REWRITE** | → "How to Confirm Your Cover Before Booking". Step 1 "Start with your GP or insurer" KEEP. Step 2 licence-and-sub-specialty KEEP, it is the honest version of the provider promise and it points at the regulator. **Step 3 "Read reviews and compare clinics" CUT** — PB has no review data and this is the weakest claim on the page. Step 4 "Confirm cover before booking" KEEP and promote to step 3, it is the conversion step |
| 22 | H2 "Orthopedic costs in the UAE (AED)" table | **KEEP structure, FIX (D1), RESOURCE all figures** | Remove the duplicate row. Current rows: consultation clinic 250–400, consultation hospital 400–700, X-ray/MRI 300–2,500, arthroscopy/day surgery 8,000–25,000, joint replacement 15,000–60,000. **All placeholders.** Badge column (CO-PAY ONLY / IF COVERED / PRE-APPROVAL) is the most extractable element on the page, keep it. Add "Verified [Month Year]". Footnote KEEP |
| 23 | H2 "Is Orthopedic Treatment Covered by Insurance?" + 5 checks | **KEEP + EXTEND** | The commercial heart of the page. Network, referral, pre-approval, co-pay/limits, physiotherapy sessions. **The "commonly 15–20" figure needs sourcing.** "Before you visit" callout KEEP |
| 24 | **ADD** | **ADD** | **Insurer cover matrix** (decision 6): which insurers cover this benefit, limit, waiting period, co-pay, with a per-row verified date. The strongest differentiator and the strongest AI-citation asset on the page. Switchable module, legal-gated |
| 25 | H2 "The Bottom Line", 2 paras | **REWRITE para 2** | Para 1 KEEP. Para 2 currently leads on finding a specialist. Re-lead on confirming cover. Its closing clause already lands the right point: "This ensures you get expert care without unexpected out-of-pocket costs" |
| 26 | FAQ, 6 items | KEEP + EXTEND | Current six are well chosen: consultation cost, referral, surgery cover, licence check, physio after treatment, free comparison. Answers 40 to 60 words, one claim per sentence, numbers where the question asks for numbers. Emit `FAQPage` |
| 27 | Footer | KEEP | |

---

## 6. Per-spoke variables (21 topics, 20 pages built)

Slug prefix throughout: `/health-insurance/cover/`. "Existing pages" column is a pointer; the binding instruction is in the disposition document.

### Wave 1

| # | Page | Slug | H1 | Primary target query | Cost-table rows needed | Existing pages |
|---|---|---|---|---|---|---|
| 1 | Orthopedics | `orthopedic` | Orthopedic Treatment in the UAE: Costs, Cover & What Your Insurance Pays | `does health insurance cover orthopedic surgery uae` | Consultation (clinic/hospital), X-ray, MRI, arthroscopy, joint replacement, physio session | `knee-replacement…-hiart`, `joint-health-insurance` |
| 2 | Dentistry | `dental` | Dental Cover in the UAE: What Insurance Pays and What It Does Not | `dental insurance uae` | Check-up, filling, root canal, extraction, crown, implant, braces | `dental-insurance-in-uae` (**270,343 impr**), `dental-implants-hiart`, 2 duplicate clinic pages |
| 3 | Maternity & OB-GYN | `maternity` | Maternity Cover in the UAE: Costs, Waiting Periods & Insurance Limits | `maternity insurance uae` | Antenatal package, normal delivery, C-section, NICU, newborn add-on | `maternity-insurance-in-uae` (**1.301% CTR, protect**) |
| 4 | Fertility / IVF | `ivf` | IVF & Fertility Cover in the UAE: What Insurance Pays per Cycle | `is ivf covered by insurance uae` | Consultation, workup, IUI, IVF cycle, ICSI, embryo freezing | `is-ivf-covered…-hiart` (0.959% CTR, pos 5.3) |
| 5 | Physiotherapy | `physiotherapy` | Physiotherapy Cover in the UAE: Session Limits, Co-pay & Costs | `does insurance cover physiotherapy uae` | Per session (clinic/hospital/home), annual cap | `health-guide/physiotherapy-treatment` |
| 6 | Dermatology | `dermatology` | Skin Treatment Cover in the UAE: Medical vs Cosmetic | `is dermatology covered by health insurance` | Consultation, acne course, patch test, mole removal, laser | `is-dermatology…-hiart` (**1.838% CTR, protect**), `skin-treatment`, `best-skin-care-clinics` |

### Wave 2

| # | Page | Slug | H1 | Primary target query |
|---|---|---|---|---|
| 7 | Optical & vision | `optical` | Eye Care Cover in the UAE: Optical Limits, Cataract & LASIK | `does health insurance cover eye treatment uae` |
| 8 | Oncology | `cancer` | Cancer Cover in the UAE: Annual Limits, Treatment Costs & Exclusions | `best health insurance for cancer uae` |
| 9 | Mental health | `mental-health` | Mental Health Cover in the UAE: Session Limits & What Insurers Pay | `is psychiatrist covered by insurance uae` |
| 10 | Cardiology | `cardiac` | Heart Treatment Cover in the UAE: Costs, Pre-approval & Limits | `health insurance for heart patients uae` |
| 11 | Chronic: diabetes & thyroid | `chronic-diabetes` | Diabetes & Thyroid Cover in the UAE: Medication, Tests & Limits | `health insurance for diabetes uae` |
| 12 | Bariatric | `bariatric` | Bariatric Surgery Cover in the UAE: When Insurance Pays | `is bariatric surgery covered by insurance uae` |
| ~~13~~ | ~~Children's cover~~ | — | **DO NOT BUILD** | see note |
| 14 | Alternative medicine | `alternative-medicine` | Alternative Medicine Cover in the UAE: What Insurers Actually Pay | `alternative medicine insurance uae` |

> **#13 is cut. Do not build a children's cover spoke.** The topic is already served by two pages converting far above benchmark: `health-insurance-for-kids-hiart/` (103,260 impressions, 2,511 clicks, **2.432% CTR**) and `can-you-buy-health-insurance-for-new-born-baby-in-uae-hiart/` (47,191 impressions, 946 clicks, **2.005% CTR**). Both are protected under Rule A and neither may be redirected. A third page would compete with PB's two best health pages. The hub links directly to both, and they get the keyword split in the cannibalisation document §4.4 instead. **Launch set is therefore 20 new pages, not 21.**

### Wave 3

| # | Page | Slug | H1 | Primary target query |
|---|---|---|---|---|
| 15 | Diagnostics | `diagnostics` | Scans & Lab Tests in the UAE: Costs, Pre-approval & Cover | `mri cost dubai with insurance` |
| 16 | Emergency & ambulance | `emergency` | Emergency & Ambulance Cover in the UAE: What Your Plan Pays | `does insurance cover ambulance uae` |
| 17 | Dialysis & kidney | `kidney` | Kidney & Dialysis Cover in the UAE: Costs and Annual Limits | `insurance for kidney patients uae` |
| 18 | Endoscopy & liver | `endoscopy-liver` | Endoscopy & Liver Treatment Cover in the UAE | `health insurance for liver uae` |
| 19 | Cosmetic vs reconstructive | `cosmetic-reconstructive` | Cosmetic vs Reconstructive Surgery: What UAE Insurance Covers | `does insurance cover plastic surgery uae` |
| 20 | Vaccinations & screening | `vaccinations` | Vaccination & Health Screening Cover in the UAE | `does health insurance cover vaccinations uae` |
| 21 | Pre-approval & network | `pre-approval` | Pre-approval, Networks & Co-pay: How UAE Health Cover Actually Works | `health insurance pre approval uae` |

**Wave 0 builds the hub and #21 first.** #21 is the mechanic every other spoke links to, so it should exist before the spokes that reference it.

---

## 7. Sourcing checklist (publish gate)

Decision 4 makes every AED figure in the design a placeholder. No page publishes with an unsourced number.

For each figure, record in the CMS or a sheet: **figure · source name · source URL or internal system · capture date · who verified.**

| Class | Acceptable source | Not acceptable |
|---|---|---|
| Consultation and procedure costs | Published provider price list (URL + capture date); or PB internal claims data with the system named and a refresh date | A competitor blog. A number from a previous PB page. Anything without a date |
| Co-pay bands, session caps, waiting periods, annual limits | Insurer policy wording or benefit table, insurer named, document version and date | "Most plans" with nothing behind it |
| Mandate and regulatory statements | The regulator's own domain (`dha.gov.ae`, `doh.gov.ae`, `mohap.gov.ae`), or `rulebook.centralbank.ae` for the statute | News summaries as the only source. Memory |
| Insurer names and benefit limits | PB's own plan data, legal-approved, per-row verified date | Anything unapproved |

**Two notes.** UAE government domains are not reachable from the automation environment, so the regulatory checks must be done by a person. And public provider price lists are stronger than internal data for AI citation, because a citable public source can be corroborated. Where both exist, cite the public one and use the internal figure to sanity-check it.

---

## 8. Definition of done

A spoke ships only when all of these are true.

**Content**
- [ ] Direct-answer block, 40 to 60 words, contains the headline number
- [ ] Word count 2,200 to 3,000, no padding
- [ ] Every AED figure carries source and capture date per §7
- [ ] "Verified [Month Year]" visible on every cost and limits table
- [ ] One claim per sentence throughout cover, cost, limit and exclusion sections
- [ ] Zero find/list/browse/rank/book-a-doctor promises (§2)
- [ ] Spelling register consistent (§1)
- [ ] Mandate wording reflects the 1 Jan 2025 position, human-verified on a `.gov.ae` domain

**E-E-A-T**
- [ ] Named author, with a live author profile page that is not a soft-404
- [ ] Named reviewer, appropriate to the content type
- [ ] Visible `dateModified` matching schema
- [ ] "Medically reviewed" banner present **only if** a DHA-licensed clinician actually reviewed it

**Technical**
- [ ] `MedicalWebPage` (or `Article` if decision 5 is not yet delivered) + `BreadcrumbList` 4 levels + `FAQPage` + `author` + `reviewedBy`
- [ ] No `Physician`, `Hospital` or `MedicalClinic` schema
- [ ] Breadcrumb renders 4 levels, matching schema
- [ ] Links: 1 up to hub, 2 to 3 lateral, plus the links its disposition specifies
- [ ] hreflang scaffolding present even though Arabic is deferred
- [ ] **Its disposition from the companion document has been applied at publish** (redirect fired, or canonical set, or the decision explicitly recorded as no-action)

**Design**
- [ ] All applicable defects from §3 fixed

**Measurement**
- [ ] Quote-form starts trackable for this URL specifically
- [ ] Included in the `/ai-search` baseline prompt set before publish
