# Specialist Cover Hub — Title, Description, H1 & Internal Links

**Status:** NEW page · `/health-insurance/cover/` · **verified still free (404 today)**
**Date:** 2026-08-19
**Input:** draft (`_health-insurance_cover_.md`)
**⚠️ This page already has an approved spec** — `specialty-cover-url-title-h1-spec-2026-08-05.md`, HUB row

## Verification status

| Item | Method | Result |
|---|---|---|
| Existing spec for this exact URL | Read 4 companion docs in `docs/` | Hub title, description, H1, schema and keywords already fixed on 5 Aug 2026 |
| URL availability | Fetched | **404 — still free** |
| Spoke pages | Fetched 2 samples | `cover/pre-approval/` and `cover/dental/` both **404 — not built yet** |
| Candidate link targets | 19 URLs fetched | All **200** |
| Character counts | Recomputed today | Spec values re-confirmed, see §2 |

Not run: GSC. The spec already carries measured GSC data (360 days to 1 Aug 2026, 121,927 query strings), so no new pull was needed for the keyword question.

---

## 1. Read this first: the draft's H1 is a hard publish blocker

The draft's H1 is:

> **Find a Doctor in UAE by Speciality- Cost and Insurance**

Strategy §4 lists that exact string as the first of four undeliverable promises:

| Location | Copy flagged on 5 Aug | Problem recorded |
|---|---|---|
| **Hub H1** | "Find a Doctor in UAE by Specialty - Costs & Insurance" | **PB has no doctor data** |
| Hub sub-head | "Browse DHA & DOH-licensed specialists across Dubai, Abu Dhabi & Sharjah" | Nothing to browse |
| Hub step 3 | "Book a DHA, DOH or MOHAP-licensed specialist" | No booking |
| Hub FAQ 3 | "Are the doctors DHA / DOH licensed?" | Presupposes a doctor listing |

And Decision 1 (Aakash, 5 August 2026):

> **Content-only. No doctor database, no booking.** → *"The 'Find a Doctor' framing cannot ship. Four separate promises in the Figma have to be rewritten."*

The draft has reverted to the rejected Figma copy, with only the British spelling changed ("Speciality" for "Specialty"). The spec's own H1 rule is *"no verb PB can't deliver"*.

This is not a preference. The page cannot promise doctor-finding when there is no doctor database and no booking. Two places in the draft carry the framing:

| Draft copy | Required |
|---|---|
| H1 `Find a Doctor in UAE by Speciality- Cost and Insurance` | Use the spec H1 in §4 |
| H2 `Find Doctors and Hospitals in the Emirates` | `Cover Rules by Emirate` (structure doc, block 13) |

Everything else in the draft is on-strategy. The cover-mechanics section in particular is the block the structure doc calls *"best section in the design"*.

---

## 2. Meta title

**Use the approved spec value. I re-counted it today and it still holds.**

```
Specialist Treatment Cost & Insurance Cover in the UAE | Policybazaar.ae
```
**54 characters before the brand suffix** ✅ (spec rule: ≤60 before ` | Policybazaar.ae`)

One thing to be aware of: with the suffix the string is 72 characters, so the SERP will truncate around "…in the UAE" and the brand will be the part lost. That is the intended trade under the house rule, since the brand is the expendable half. Flagging it so nobody "fixes" the length later by cutting "in the UAE" instead.

Do not use "Best", "Top" or "Near Me" — excluded by the spec's title rule. "UAE" must stay in the title.

**If you want to revisit** (all recounted today, all inside 50–60):

| # | Title (before brand) | Chars | Note |
|---|---|---|---|
| **A** | `Specialist Treatment Cost & Insurance Cover in the UAE` | **54** | **Approved spec value. Default.** |
| B | `Specialist Consultation Cost & Insurance Cover in the UAE` | 57 | Swaps "Treatment" for "Consultation" to sit closer to the primary keyword. |
| C | `Specialist Consultation Cost in UAE & What Insurance Covers` | 59 | Closest to the primary keyword, weakest on the cover half. |

Option B is defensible because the primary keyword is `specialist consultation cost uae`, not "treatment". But the spec chose "Treatment" deliberately to cover the 28 spokes that are procedures rather than consultations, so **stay with A unless you want to narrow the hub**.

---

## 3. Meta description

**Use the approved spec value.**

```
See what specialist care costs across the UAE, what your health plan actually pays, and which of 25+ insurers cover the treatment you need. Compare free.
```
**153 characters** ✅ (spec rule: 140–160)

One dependency: "which of 25+ insurers" is a countable claim. The trust bar figure recorded in the structure doc is "35+ partners". Confirm which number is right for health specifically before publish, or the description and the on-page trust bar will disagree.

---

## 4. H1

**Use the approved spec value.**

```
Specialist Treatment Costs & What Health Insurance Covers in the UAE
```
**68 characters.** Different from the title, as the spec rule requires, and it contains no verb PB cannot deliver.

**Shorter alternatives** if 68 reads long in the hero:

| H1 | Chars |
|---|---|
| `Specialist Treatment Costs & What Health Insurance Covers in the UAE` | 68 (spec) |
| `What Specialist Care Costs in the UAE, and What Your Plan Pays` | 62 |
| `Specialist Consultation Costs and Cover Across the UAE` | 54 |

### Structure gaps against the approved block list

The structure doc specifies 14 hub blocks. Measuring the draft against it:

| # | Required block | In draft? |
|---|---|---|
| 5 | Breadcrumb `Home > Health Insurance > Cover & Costs` (3 levels) | not in draft |
| **6** | **⭐ Direct answer, 40–60 words** — consultation range + the co-pay reality | **missing** |
| 8 | Cover-by-treatment grid, 30 cards grouped by benefit family | heading only, empty |
| 9 | 3 steps, with step 3 as "Confirm cover before you book" | not in draft |
| 10 | Consultation cost table, all live spokes, `Verified [Month Year]` | **3 rows only** |
| 11 | Why the right plan matters | present ✅ |
| 12 | 4 cover mechanics (Network · Referral · Pre-approval · Co-pay) | present ✅ |
| 13 | Cover rules by emirate | present but mis-titled (§1) |
| 14 | FAQ | present ✅ |

**The direct-answer block is the most important omission.** The structure doc calls it *"the AI-answer target for the whole cluster"* and instructs writing it first. It needs the consultation range and the co-pay reality in 40 to 60 words, placed directly under the H1 or trust bar.

Also unresolved: the draft contains a heading with no content —

> `## Seek Doctor Consultation via Health Insurance Policy (Need Clarification)`

That needs either content or deletion. On the framing question it raises: this is the block that should become the direct answer, reframed off "seek doctor consultation" and onto what the plan pays.

---

## 5. Internal linking

### 5a. The spokes do not exist yet, so link sideways for now

I checked: `/health-insurance/cover/pre-approval/` and `/health-insurance/cover/dental/` both 404. The 28 spokes are unbuilt, so the cover-by-treatment grid has nothing to point at and the structure doc's *"every spoke links to pre-approval"* rule cannot run in reverse yet.

That makes the existing-page links below the whole of the hub's outbound value at launch. All 19 verified 200 today.

### 5b. The two links the spec singles out

The structure doc names these explicitly, including one with measured CTR:

| Anchor (from draft copy) | Target | Why |
|---|---|---|
| `check if the chosen hospital is within your insurer's network` | `/health-insurance/network-hospitals/` | Named in the spec's linking rules |
| needs copy edit: on outpatient/consultation cover | `/health-insurance/health-guide/opd-cover/` | **1.030% CTR, directly relevant, and the spec notes it is currently unlinked from this cluster** |

The `opd-cover` link is the highest-value single addition. The spec flags it as relevant and orphaned from this cluster, and the GP row in the keyword map shows `opd` at 1,793 measured impressions.

### 5c. Regulator section — the draft names three regulators and links none

The draft's regulator block (DHA, DOH, MOHAP) is the strongest linking opportunity in the copy, and it is entirely unlinked. All four targets verified 200:

| Anchor (in draft) | Target |
|---|---|
| `DHA (Dubai Health Authority)` | `/health-insurance/articles/dubai-health-authority/` |
| `DOH (Department of Health – Abu Dhabi)` | `/health-insurance/articles/doh-abu-dhabi-haad-license/` |
| `Abu Dhabi's Thiqa programme covers the nationals` | `/health-insurance/articles/what-do-you-need-to-know-about-thiqa/` |
| needs copy edit: add a line on which regulator sets your minimum benefits | `/health-insurance/articles/dha-vs-doh-vs-moh/` |

Add `/health-insurance/articles/sharjah-health-authority/` when you extend the block to the five northern emirates, which block 13 requires.

### 5d. Plan-tier and cost-mechanic terms

The draft uses these terms and defines none of them by link:

| Anchor (in draft) | Target |
|---|---|
| `Basic plans generally require a referral` | `/health-insurance/basic/` |
| `basic and semi-comprehensive plans` (FAQ) | `/health-insurance/articles/basic-and-comprehensive-health-insurance/` |
| `co-payment and any sub-limits` | `/co-payment-in-health-insurance-hiart/` |
| `deductible of AED 50` (FAQ) | `/what-is-a-deductible-in-health-insurance-hiart/` |
| `specialist consultation fee in Abu Dhabi` | `/health-insurance-abu-dhabi/` |
| `Northern Emirates` | `/health-insurance/health-insurance-in-sharjah/` |

Prefer the `-hiart` articles over the `/glossary/` stubs where both exist — `/health-insurance/glossary/copayment/` and `/glossary/deductibles/` are both live but thinner.

The basic vs semi-comprehensive vs comprehensive distinction carries two of the draft's four FAQ answers, so linking it once is worth more than it looks.

### 5e. Two benefit links that are live now

The cost table and the eventual 30-card grid both need somewhere to send dental and maternity traffic before those spokes exist. Both are the highest-impression benefits in the keyword map (dental 2,071 + 1,701; maternity 2,306 + 2,089):

- `/health-insurance/articles/dental-insurance-in-uae/`
- `/health-insurance/articles/maternity-insurance-in-uae/`

Per the spec's disposition rules, retarget these at the new spokes once dental and obstetrics are live, not before.

### 5f. Anchor text rule

From the structure doc: *"Descriptive. Never 'click here', never bare URL."* Applies to all of the above.

---

## 6. Content flags

**F1 — the "Find a Doctor" framing. Covered in §1. Hard blocker.**

**F2 — every AED figure is unsourced, and Decision 4 makes that a hard publish blocker.**

> "All AED figures in the Figma are designer placeholders. Every number needs a named source and a capture date before publish."

The draft carries AED 150–350, AED 300–700 (twice) and an AED 50 deductible, sourced only to `healthfinder.ae/blog/doctor-consultation-fees-dubai/` — a third-party blog. The structure doc's source tier for cost data requires *"published provider price list (URL + capture date), or PB claims data with system named"*. A competitor blog does not clear that bar.

Add `Verified [Month Year]` to the table, per block 10.

**F3 — the Dermatologist figure contradicts the Figma.** The draft gives Dermatologist AED 300–700. The Figma table recorded in the briefs gives Dermatology **250–600**. One of the two is wrong; neither is sourced. Also the draft's table is 3 rows where block 10 requires extension to all live spokes, and the draft's GP row has no Figma counterpart while the Figma's Orthopedic, Eye, ENT and Dentist rows have been dropped.

**F4 — the primary keyword has drifted.** The draft's keyword line reads `specialist consultation insurance cover, specialist visit co-pay uae, do i need a referral to see a specialist in dubai, specialist consultation fee abu dhabi`. The last three match the spec's proposed secondaries exactly, so the writer had the spec. But the spec's **primary** is `specialist consultation cost uae`, not "specialist consultation insurance cover". Restore it — the spec's format note is that this is *"a price query; the table is the answer"*, which is why cost leads.

**F5 — two FAQ answers say the same thing.** "How much is the amount for specialist visit co-pay in UAE?" and "I live in Abu Dhabi. How much is the co-pay amount for medical specialist consultation?" both end on the AED 50 Abu Dhabi deductible. Merge, or make the second one genuinely Abu Dhabi-specific.

**F6 — the co-pay customisation claim needs a source.** "There is no specific co-pay percentage for specialist visits in Dubai and the Northern Emirates. In fact, they may be customisable: 0%, 10%, or even 20%." That is a plausible product statement, but it is exactly the class of claim the spec requires an insurer-wording citation for.

**F7 — no medical reviewer, so schema is capped.** Decision 5 makes the DHA-licensed reviewer a hard publish blocker for the "Medically reviewed" claim and for `MedicalWebPage`. Hub schema per the spec is **CollectionPage + BreadcrumbList + FAQPage + ItemList** — no `MedicalWebPage` until the reviewer is engaged with a live author profile. The structure doc also records that `/author/*` soft-404s, so a byline would point at a dead entity.

**F8 — the 1 Jan 2025 mandate position is absent.** The draft avoids the outdated "mandatory in Dubai and Abu Dhabi" error that block 11 was written to fix, which is good. But it also never states the current position. Since the hub explains why the right plan matters, one sentence on cover being mandatory across all emirates since 1 January 2025 belongs there. Strategy §9 has the wording and the caution that the northern-emirates mandate is framed around private-sector employees and domestic workers as a visa condition, so "mandatory everywhere" is too blunt.

**F9 — strip the working notes.** The `Keywords-` line, the `Ref. Links-` line and the `(Need Clarification)` heading are all authoring scaffold and must not ship.

**F10 — FAQ schema.** Five well-formed questions, answer-first. Emit `FAQPage` per the spec. Do not expect FAQ rich results: Google restricts those to government and health-authority sites, which does not include commercial aggregators.
