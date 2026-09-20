# Neurology Cover — Title, Description, H1 & Internal Links

**Status:** NEW (404 — unbuilt) · **Date:** 2026-09-04 · **Input:** neurology cover-page draft (.md, with two inline base64 images) · **⚠️ Already specced** — `specialty-cover-url-title-h1-spec-2026-08-05.md`, row `cover/neurology/` (line 443)

## Verification status

| Item | Method | Result |
|---|---|---|
| Slug/hub/pre-approval live? | `pbcheck.py status` | All three 404 — cluster still unbuilt, as expected this early in the launch |
| Spec title char count | `pbcheck.py count` | 55 chars before brand — confirmed OK, re-verified not re-derived |
| Spec description char count | `pbcheck.py count` | 151 chars — confirmed OK |
| Draft's own title/H1 char count | `pbcheck.py count` | 77 chars — over the 60-char house limit, doesn't match spec anyway |
| 8 AED figures in the costs table | `pbcheck.py peg` (10 values incl. both bounds) | **10/10 resolve to a round USD figure** — converted price list, not UAE provider data |
| 8 overlapping URLs' actual topic | `pbcheck.py page` (fetched title/desc/H1 for each) | All 8 genuinely neurological — no homonym false positive here (unlike `joint-health-insurance` on the orthopedic cluster) |
| Overlap total (8 pages, 5,301 impr) | Summed the CSV's `i360` column | Matches spec exactly: 2,046+1,136+820+716+280+123+113+67 = 5,301 |
| Undeliverable verbs (find/browse/book/near me) | grep on saved draft text | **None found** — clean |
| FAQ count and word count | Parsed the FAQ block | 5 of the required 6 FAQs; only 1 of 5 lands in the 40–60 word band |
| Lateral-link candidate spokes | `pbcheck.py status` | physiotherapy, diagnostics, cardiac, mental-health all 404 |
| government regulator URLs (DHA/DOH/MOHAP) | — | Not fetched — these domains are unreachable from this environment per prior verification. The draft's DHA/Dubai, DOH/Abu Dhabi, MOHAP/Northern Emirates split is standard and consistent with the spec's own hub note, but route a hard check to a person before publishing if you want it regulator-confirmed |

## 1. What would do the most damage if this shipped: every price in the cost table is a converted USD list

Running all five rows of the "Neurology Treatment-related Costs in the UAE" table through the peg test:

```
AED 367 → $99.9 → $100        AED 1,102 → $300.1 → $300
AED 36,725 → $10,000.0        AED 183,625 → $50,000.0
AED 67,941 → $18,499.9        AED 126,701 → $34,499.9
AED 110,175 → $30,000.0       AED 238,713 → $65,000.1
AED 104,666 → $28,499.9       AED 312,163 → $85,000.1
```

**10 of 10 values resolve to a round USD figure.** This is not UAE provider pricing with AED precision — it's a USD price list (almost certainly medical-tourism/aggregator sourced) converted at a single exchange rate and dressed up with false AED precision. "AED 367" reads like a real quoted consultation fee; it's actually "$100, converted." This is Decision 4, and it's a **hard publish blocker**: every figure needs a named UAE source (insurer benefit schedule, hospital price list, or a DHA/DOH tariff reference) and a capture date before this table can ship. The in-draft disclaimer ("figures are indicative only... confirm with the hospital") doesn't cure this — it's a hedge on top of manufactured numbers, not a source citation.

Compounding this: the table has no `Verified [Month Year]` tag and no badge column, both required by the spoke spec (block 19) independent of the sourcing problem.

## 2. Meta title

**Spec value (re-verified, not re-derived):** `Neurology Cover in the UAE: Costs, Scans & Chronic Care | Policybazaar.ae` — 55 chars before brand ✅

The draft's own H1/working-title — `Health Insurance for Neurology in the UAE: Costs, Coverage & Specialist Guide` — is 77 chars and doesn't match the spec. Recommend the spec's title as-is; it's already under 60 and doesn't need trimming.

## 3. Meta description

**Spec value (re-verified):** `Neurology care often means repeat scans and long-term medication. See what a consultation, MRI and ongoing treatment cost, and how annual limits apply.` — 151 chars ✅

Note it doesn't promise a specific AED figure, which is the right call given F1 — don't let a rewritten description reintroduce an unsourced number.

## 4. H1 (+ structure gaps against the 23-block spoke spec)

**Spec H1:** `Neurology Cover in the UAE: Consultation, Scans & Long-term Care` — use this, not the draft's 77-char working title. No find/browse/book verb in either version, so no hard-blocker risk on the H1 itself.

| # | Block | Present? | Note |
|---|---|---|---|
| 1 | Breadcrumb | Not in this doc | Chrome/CMS-level — can't confirm from body copy. Verify separately, and drop the "Toyota" stray-crumb defect check when you do |
| 2 | Eyebrow tags | Not in this doc | Same — chrome, not authored here |
| 3 | H1 | ✅ present, ❌ wrong text | Swap in the spec H1 above. No banned verb |
| 4 | Standfirst | ✅ | Doesn't carry the "how to find a licensed specialist" clause — clean |
| 5 | Byline | Not in this doc | Can't confirm one-person-one-role; flag for CMS review |
| 6 | Trust banner | Not in this doc | Correctly absent of any "Medically reviewed" claim (see §7 F4) |
| 7 | TOC + sticky CTA | Not in this doc | Chrome-level |
| 8 | Intro, 2 paras | ✅ | Present, UAE-localised in tone |
| **9** | **⭐ Direct answer** | ❌ **Missing** | Intro para 1 is ~45 words — close to the 40–60 target length — but never states the consultation cost or a co-pay reality. It's framing, not the answer. Needs a rewrite: e.g. "A neurologist consultation in the UAE typically costs AED [sourced range]... under a basic plan you'll pay [co-pay]..." **Write this first**, and don't populate it until F1 is fixed |
| 10 | What this covers | Partial | Exists as "Does Health Insurance Cover Neurology Treatment?" but placed near the bottom rather than early for topical depth |
| 11 | Sub-areas, 8 tiles | ✅ | "Sub-specialities of Neurology" — exactly 8 items, matches spec count |
| 12 | Conditions treated | ✅ | 9 conditions listed, UAE-relevant |
| 13 | KEY POINT | ✅ | One instance, not duplicated (a defect seen elsewhere — clean here) |
| 14 | Treatments | ✅ | No "DHA RECOMMENDED"/"DHA LICENSED" badges in the copy — clean |
| 15 | Mid CTA | Not in this doc | Button copy isn't in a body-copy doc; verify in CMS that it reads "Check What Your Plan Covers," not the find-doctor version |
| 16 | When to see one | ✅ | "When Should You Consult a Neurologist?" — good list of red-flag symptoms |
| 17 | Training & licensing | ✅, with one flag | DHA/Dubai, DOH/Abu Dhabi, MOHAP/Northern Emirates split is correct, not duplicated. But "feedback from other patients can also help you choose" is a softer echo of the banned review-reliance promise — see §7 F7 |
| 18 | Confirm your cover | ✅ **already correct** | Renamed from "How to Find a Doctor" exactly as spec requires, and the "read reviews and compare clinics" step is **already cut** — 4 clean steps remain |
| 19 | Costs table | ⚠️ | No duplicated row (clean), but see F1 — sourcing blocker — and missing badge column / `Verified [Month Year]` |
| 20 | Is it covered? | Thin | One short paragraph; network/referral/pre-approval/co-pay/limits mostly live in block 18 instead, which is fine as a split but this section reads as an afterthought |
| **21** | **⭐ Insurer matrix** | ❌ **Missing** | No insurer names anywhere in the draft. This is the biggest structural gap — see §6 for why it matters more than usual on this cluster |
| 22 | Bottom line | ⚠️ | "Wrapping Up" re-leads correctly on reviewing cover, not finding a specialist — but see F5, a "heart conditions" reference looks like cardiac-spoke leftover text |
| 23 | FAQ ×6 | ❌ | Only 5 FAQs present, and only 1 of 5 lands in the 40–60 word band (see table below) |

## 5. Internal linking

**Up (hub):** `/health-insurance/cover/` — 404, unbuilt. Recommend a CMS placeholder now, live link when the hub ships, anchor from the breadcrumb + once in body (e.g. off "health insurance policy" in the intro).

**Lateral (2 genuine, anchor-backed):**

| Target | Status | Anchor (from the draft's own text) |
|---|---|---|
| `/health-insurance/cover/physiotherapy/` | 404, unbuilt | "Physiotherapy and cognitive therapy" (from the Non-Surgical treatments block — rehab genuinely attaches here, same logic as ortho→physio) |
| `/health-insurance/cover/diagnostics/` | 404, unbuilt | "MRI, CT, and EEG scans" (appears twice in the draft — diagnostics-heavy specialty, natural pairing) |

I didn't add a third. Cardiac is tempting because stroke sits at the intersection, but the disposition CSV already files the standalone stroke article under **neurology's own topic**, not cardiac's — so stroke breadth belongs here, not cross-linked out. Don't force a third lateral link without a genuine textual anchor.

**Down (existing pages, safe to link — REWRITE IN PLACE):**

| Target | Anchor | Why safe |
|---|---|---|
| `/health-insurance/health-guide/multiple-sclerosis/` | "Multiple sclerosis (MS)" (from the conditions-treated bullet) | REWRITE IN PLACE — page stays at this URL |
| `/health-insurance/health-guide/alzheimer-disease/` | "Alzheimer's disease" (same bullet list) | REWRITE IN PLACE — page stays |

**Do not link (FOLD/CONSOLIDATE — URLs are going away):** `motor-neuron-disease`, `coma`, `best-critical-health-insurance-plan-for-stroke`, `aphasia`. All four are merging into this spoke and 301'ing here — linking to them would point at a page about to redirect back to the page you're on.

**Every spoke (mandatory):**

| Target | Status | Anchor |
|---|---|---|
| `/health-insurance/cover/pre-approval/` | 404, unbuilt | Placeholder now — worth noting this page is flagged in the strategy doc as justifying being built *first* across the whole launch (61,234 impr at pos 5.5, zero clicks on `what is a deductible insurance`), so it may ship before neurology does |
| `/health-insurance/network-hospitals/` | ✅ 200, live | "insurer's network list" (from the "Verify the Network Hospitals" step) |
| `/health-insurance/health-guide/opd-cover/` | ✅ 200, live | **Needs copy edit** — no OPD/outpatient phrase currently exists in the draft. Propose adding one clause to "Know Your Plan Level," e.g. "...whether outpatient (OPD) consultations are covered in full or subject to a sub-limit," then anchor "outpatient (OPD) consultations" |

**One naming caution, not a live issue in this draft:** `/health-insurance/neuron/` is **Neuron the TPA** (a claims administrator), not a neurology page — the cannibalisation report explicitly warns not to conflate the two when building this spoke. The draft doesn't currently mention Neuron, so nothing to fix, just don't let a future editor add it as a "related" link by name-match.

## 6. Cannibalisation

Disposition CSV, `neurology` topic, all 8 rows fetched and topic-verified — genuinely on-topic, unlike the confirmed `joint-health-insurance` false positive on the orthopedic cluster:

| Label | Count | Pages | Draft handling |
|---|---|---|---|
| REWRITE IN PLACE | 2 | multiple-sclerosis, alzheimer-disease | Safe to link — see §5 |
| FOLD | 4 | motor-neuron-disease, coma, best-critical-...-stroke, aphasia | Merging into this spoke + 301. Stroke is already well-absorbed (listed condition, "Stroke Intervention" treatment, table row) — correct. **Motor neuron disease, coma and aphasia have zero mention anywhere in the draft.** A 301 that lands a searcher on a page with no trace of what they searched for is a weak landing; each deserves at least a condition-list mention or FAQ line before the redirects go live |
| DIFFERENTIATE | 2 | muscular-dystrophy, polio | Both stay live, CSV rationale is "seasonal/news/awareness intent, don't 301 into a spoke." Neither is mentioned in the draft, which is the correct split — the spoke doesn't need to compete on their niche/awareness angle |

**Total, re-summed:** 5,301 impressions at 0.434% CTR — matches the spec row exactly.

**Why blocks 9 and 21 matter more than usual here:** one of neurology's own measured secondary queries shows the same signature as the orthopedic AIO case the strategy doc calls out — `which plans cover stroke, cancer, and heart attack` sits at position 3.4 with 20 impressions and **0 clicks**. Smaller volume than the orthopedic knee-replacement example (1,301 impr), but the same pattern: a good position with nobody clicking through usually means an AI answer is sitting above the result, not that the page is failing to rank. Ranking this page harder won't fix that — being the page an AI answer *cites* will. That's exactly what the direct-answer block and the insurer matrix are for, and both are currently absent.

Two items outside this draft's control, worth a line since they sit inside this exact cluster: the report flags `/health-insurance/articles/top-veterinary-clinics-in-the-uae/` as PB's best-ranking page for `neurolog`-stem queries — a relevance defect with its own ticket, not something this draft fixes. And the Neuron/neurology naming collision above.

## 7. Content flags

**F1 — 🔴 Hard blocker (Decision 4).** All 5 cost-table rows / 10 bounds resolve to round USD. Converted price list, not sourced UAE data. Cannot ship until every figure has a named source and capture date. See §1.

**F2 — Both ⭐ ADD blocks missing.** No direct-answer block (40–60 words, headline consultation figure + co-pay reality, written first) and no insurer matrix (named insurers, limits, waiting periods, co-pay, verified date). Given the AIO signature in §6, these two blocks are the actual point of the page, not polish.

**F3 — FAQ count and length short of spec.** 5 of 6 required questions; word counts are 29, 35, 23, 42, 25 — only the 42-word answer clears the 40–60 band. Needs a 6th FAQ and ~4 answers lengthened, one claim per sentence per the house rule.

**F4 — Schema conflict between the spec row and Decision 5.** The spec row calls for `MedicalWebPage + BreadcrumbList + FAQPage + author + reviewedBy`. Decision 5 blocks all of `MedicalWebPage`/`author`/`reviewedBy` until a DHA-licensed clinician is contracted as reviewer, and `/author/*` currently soft-404s. Ship `Article + BreadcrumbList + FAQPage` now; upgrade once the reviewer exists. The draft's own absence of any "Medically reviewed" byline is actually the correct behavior under Decision 5 — flagging so nobody "fixes" that by adding a reviewer claim that can't be backed yet.

**F5 — Likely cross-spoke copy leftover.** "Wrapping Up" says a comprehensive policy can "cut down your financial burden of big expenses related to heart conditions and more" — heart conditions on a neurology page reads like boilerplate carried over from a cardiac draft. Recommend re-leading on neurology-specific costs (stroke, epilepsy surgery, long-term medication) instead.

**F6 — Third-party citation doesn't clear the source tier, and is tonally awkward.** The sole `Ref. Links-` entry is `us-uk.bookimed.com` — a medical-tourism booking aggregator. It doesn't meet the government/regulator source bar, and citing a booking site as a reference sits oddly next to Decision 1's ban on PB itself offering booking framing. Drop it, or replace with a DHA/DOH/MOHAP source once someone can verify those domains directly (unreachable from this environment).

**F7 — Softer echo of the review-reliance promise.** Under "What Medical Qualifications You Must Check," the line "...feedback from other patients can also help you choose the right specialist" implies PB has patient-review data on doctors, which it doesn't — the same reason "read reviews and compare clinics" was cut from block 18. The block-18 cut was done correctly; this line wasn't caught by the same pass. Recommend cutting or rewording to "their listed experience and sub-specialisation" only.

**F8 — Costs table missing required elements independent of F1.** No badge column, no `Verified [Month Year]` tag.

**F9 — Base64 inline images, no alt text.** Both images are inline data URIs with no descriptive alt attribute in the markdown (`![][image1]`, `![][image2]`). Needs descriptive alt text and an optimised (non-inline) asset before publish.

**F10 — Working notes need stripping.** `Keywords-` and `Ref. Links-` footers are present and should be removed pre-publish. Worth noting positively: the keyword footer's parenthetical impression counts (239, 114, 20) match the spec's measured secondary-keyword table exactly, which confirms the writer worked from the spec rather than guessing — a good sign for trusting the rest of the targeting.

**F11 — Spelling mix.** "hospitalisation" (British) alongside "finalizing," "sub-specialization" (American). Spec/keyword targeting uses American spelling (matches measured demand); standardise the body to American throughout.

**F12 — See §6:** three FOLD-disposition pages (motor neuron disease, coma, aphasia) have zero representation in the draft despite redirecting here.

---

**What's already right, worth keeping:** the "How to Find a Doctor" section was correctly renamed twice over — once to "What Medical Qualifications You Must Check Before Consultation?" (verification framing, not booking) and once to "Confirm Your Neurology Cover" — and the "read reviews and compare clinics" step was already cut from the latter without being told to. The sub-specialities list lands exactly on the spec's 8-tile count. No duplicated KEY POINT, no duplicated table row, no find/browse/book verb anywhere in the draft. That's a clean pass on several defects that showed up in earlier drafts in this launch.
