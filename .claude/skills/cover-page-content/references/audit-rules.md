# Cover-page audit rules

Everything here is derived from the four source-of-truth docs in `docs/`. Those docs
win any disagreement with this file — read them, don't trust a summary. This file
exists so you know *where* to look and *what* the stable rules are.

## Contents
- [Source docs](#source-docs)
- [The seven decisions and the hard blockers](#the-seven-decisions-and-the-hard-blockers)
- [Hub block list (14)](#hub-block-list-14)
- [Spoke block list (23)](#spoke-block-list-23)
- [Internal linking rules](#internal-linking-rules)
- [Cannibalisation method](#cannibalisation-method)
- [Disposition labels and what they mean for linking](#disposition-labels-and-what-they-mean-for-linking)
- [Do-not-redirect pages](#do-not-redirect-pages)
- [The 31 slugs](#the-31-slugs)
- [Recurring draft defects](#recurring-draft-defects)

---

## Source docs

All in `docs/`, all dated 2026-08-05:

| Doc | What you need from it |
|---|---|
| `specialty-cover-url-title-h1-spec-2026-08-05.md` | **Per-page row**: URL, wave, title (chars before brand), description, H1, primary keyword, demand tier, schema, existing overlap. Plus the measured/proposed keyword split. 1,015 lines — grep for the page name rather than reading it all. |
| `specialty-cover-page-content-structure-2026-08-05.md` | Hub block list (~L126), spoke block list (~L152), internal linking rules (~L219), the facts table with source tiers (~L85). |
| `specialty-cover-seo-aio-strategy-2026-08-05.md` | §2 decisions, §4 what must change in the design, §5 the reframe, §9 the mandate correction, §10 sequencing. |
| `specialty-cover-disposition-2026-08-05.csv` | One row per existing overlapping URL: `topic,url,c360,i360,ctr360,pos360,c28,i28,recommendation,rationale`. |
| `specialty-cover-cannibalisation-report-2026-08-05.md` | Per-cluster analysis, the AIO findings, the low-risk build order, and the known measurement artefacts. |

Keyword data in the spec is **PB's own GSC impressions**, not market volume. `⬤` = measured
(PB already gets impressions), `○` = proposed target. `⚪ Unmeasured` means PB has no page, so
no data — it is not evidence of no demand. DataForSEO credentials are unset on this machine,
so true volume is unavailable; don't imply otherwise.

---

## The seven decisions and the hard blockers

From strategy §2, decided by Aakash on 5 August 2026. Two of these block publication.

| # | Decision | Consequence for a draft |
|---|---|---|
| 1 | **Content-only. No doctor database, no booking.** | The "Find a Doctor" framing **cannot ship**. Scan every draft for undeliverable verbs. |
| 2 | Build hub and spokes first, resolve overlap after | Build gate ≠ index gate (§10). |
| 3 | Cannibalisation case by case after audit | The audit is done. Use the disposition CSV, but verify it (see below). |
| 4 | **All AED figures in the Figma are designer placeholders** | 🔴 **Hard blocker.** Every number needs a named source and capture date. Run the peg test. |
| 5 | **Contract a DHA-licensed clinician as medical reviewer** | 🔴 **Hard blocker** for "Medically reviewed", `MedicalWebPage`, `author`, `reviewedBy`. `/author/*` soft-404s, so a byline points at a dead entity. Ship `Article + BreadcrumbList + FAQPage` until the reviewer exists. |
| 6 | Publish named insurers and their benefit limits | This is the differentiator. It is what the insurer matrix block is for. |
| 7 | English now, Arabic for proven performers only | Don't propose Arabic links from English pages. |

**The four undeliverable promises** (strategy §4, quoted from the Figma). Any of these in a
draft is a hard blocker, not a preference:

| Location | Rejected copy | Why |
|---|---|---|
| Hub H1 | "Find a Doctor in UAE by Specialty - Costs & Insurance" | PB has no doctor data |
| Hub sub-head | "Browse DHA & DOH-licensed specialists across…" | Nothing to browse |
| Hub step 3 | "Book a DHA, DOH or MOHAP-licensed specialist" | No booking |
| Hub FAQ 3 | "Are the doctors DHA / DOH licensed?" | Presupposes a doctor listing |

Spokes carry the same defect in their "How to Find a [specialty] Doctor" section. It becomes a
**cover-confirmation** section. Grep drafts for: `find a doctor`, `find the right`, `browse`,
`book a`, `near me`, `are the doctors`, `licensed specialists across`.

Also from §4: the hub's "health insurance is mandatory in Dubai and Abu Dhabi" is **out of
date**. Since 1 Jan 2025 cover is mandatory across all emirates, but §9 cautions that the
northern-emirates mandate is framed around private-sector employees and domestic workers as a
visa condition, so "mandatory everywhere" is too blunt.

---

## Hub block list (14)

Structure doc ~L126. Two blocks are marked ⭐ ADD and are the ones drafts keep missing.

| # | Block | Note |
|---|---|---|
| 1 | Hero | H1 per spec. One CTA: Get a Quote |
| 2 | 3 USPs | Item 1 → "Cover checked against DHA, DOH & MOHAP rules / N treatment guides" |
| 3 | Quote widget | Keep. Verify the "AED 4/day" claim |
| 4 | Trust bar | 4.7/5 · 40,413 reviews · 2M+ customers · 35+ partners · 1M+ policies. Confirm all five |
| 5 | Breadcrumb | `Home > Health Insurance > Cover & Costs` (3 levels) |
| **6** | **⭐ Direct answer** | **40–60 words.** Consultation range + co-pay reality. The AI-answer target for the whole cluster |
| 7 | Format decision | Comparison table, not explainer — the primary keyword is a price query |
| 8 | Cover-by-treatment grid | 30 cards grouped by benefit family. Children's card → existing kids page |
| 9 | 3 steps | Step 3 "Book a specialist" → "Confirm cover before you book" |
| 10 | Consultation cost table | Extend to all live spokes. Keep the WITH INSURANCE badge column. Add `Verified [Month Year]` |
| 11 | Why the right plan matters | 🔴 Para 1 carries the outdated mandate claim |
| 12 | 4 cover mechanics | Network · Referral · Pre-approval · Co-pay & limits. Best section in the design. Link each to `pre-approval` |
| 13 | Cover rules by emirate | 🔴 Dubai card was empty. Add the five northern emirates |
| 14 | FAQ | Emit `FAQPage` |

---

## Spoke block list (23)

Structure doc ~L152. Blocks 9 and 21 are ⭐ ADD.

| # | Block | Note |
|---|---|---|
| 1 | Breadcrumb | 4 levels. 🔴 Remove the stray "Toyota" crumb |
| 2 | Eyebrow tags | 📖 GUIDE · BENEFIT · 🇦🇪 UAE |
| 3 | H1 | Per spec. **No find / browse / book verb** |
| 4 | Standfirst | Drop the "how to find a licensed specialist" clause |
| 5 | Byline | 🔴 One person, one role (Figma showed both Medical Reviewer and Senior Health Editor) |
| 6 | Trust banner | 🔴 "Medically reviewed" blocked until the reviewer exists |
| 7 | TOC + sticky CTA | Keep. Sticky CTA is the best-targeted element |
| 8 | Intro, 2 paras | Keep if UAE-localised |
| **9** | **⭐ Direct answer** | **40–60 words**, one claim per sentence, headline number in it. **Write this first** |
| 10 | What this covers | Topical depth for YMYL |
| 11 | Sub-areas, 8 tiles | 🔴 Fix spelling mix |
| 12 | Conditions treated | Keep UAE-localised descriptors |
| 13 | KEY POINT | 🔴 Was duplicated in the Figma |
| 14 | Treatments | 🔴 Remove "DHA RECOMMENDED"/"DHA LICENSED" badges — unsupportable |
| 15 | Mid CTA | "Find DHA-Licensed Doctors Near You" → "Check What Your Plan Covers" |
| 16 | When to see one | Earns the `MedicalWebPage` claim once the reviewer exists |
| 17 | Training & licensing | 🔴 Regulator row listed Abu Dhabi twice, omitted DHA. Purpose is helping a patient **verify** credentials, not career advice |
| 18 | **Confirm your cover** | Was "How to Find a Doctor". Keep steps 1, 2, 4. **CUT "Read reviews and compare clinics"** — PB has no review data |
| 19 | Costs table | 🔴 Row 1 was duplicated. Keep badge column. Add `Verified [Month Year]` |
| 20 | Is it covered? | The commercial heart: network · referral · pre-approval · co-pay · session limits |
| **21** | **⭐ Insurer matrix** | Insurer · limit · waiting period · co-pay · verified date. **Strongest AI-citation asset on the page** |
| 22 | Bottom line | Re-lead on confirming cover, not on finding a specialist |
| 23 | FAQ ×6 | 40–60 words each, one claim per sentence |

---

## Internal linking rules

Structure doc ~L219.

| Direction | Rule |
|---|---|
| **Up** | 1 link to hub, in breadcrumb + once in body |
| **Lateral** | 2–3 spokes, **genuine** relatedness only. Orthopedic→physiotherapy ✅ (session cap attaches to rehab). Orthopedic→dental ❌ |
| **Down** | The existing pages its disposition says to keep |
| **Every spoke** | Links to `pre-approval`. Also link `/health-insurance/network-hospitals/` and `/health-insurance/health-guide/opd-cover/` (1.030% CTR, relevant, flagged as unlinked from this cluster) |
| **Anchor text** | Descriptive. Never "click here", never a bare URL |

Two habits that matter more than the rules:

- **Extract anchors from the draft's own sentences.** Find the sentence containing the target
  concept, take the shortest 3–7 word phrase. Inventing anchor text produces copy the writer
  never agreed to and is the fastest way to get a recommendation ignored. Where no suitable
  phrase exists, say "needs copy edit" and propose the wording.
- **Most of the cluster is unbuilt.** Early in the launch the hub and sibling spokes 404, so
  Up / Lateral / pre-approval links can't resolve. Say so, and recommend CMS placeholders so
  they go live with the wave rather than being retro-fitted.

---

## Cannibalisation method

The disposition CSV is the starting point, not the answer. It assigns each existing URL to a
topic by keyword seed, and keyword seeds produce homonym false positives.

**Confirmed artefacts.** The spec already excluded `sukanya samriddhi yojana` (+7 variants),
which matched the `mri` seed inside "sa**mri**ddhi". One more slipped into the disposition:
`/health-insurance/joint-health-insurance/` is filed under `orthopedic`, but it is about
**joint policies for couples and families** — "joint" as in jointly held, not knees and hips.
Rebuilding it on an orthopedic spoke template would destroy a page about a different product.

So for every overlap row: **fetch the page and read its title, description and H1 before
accepting the topic label.** `pbcheck.py page` does this. If the topic doesn't match, flag it,
exclude it from the cluster totals, and say the disposition needs its own ticket.

**The AIO check.** When a query has substantial impressions at a good position with zero
clicks, the answer is being lifted above the results. The report's finding on
`does insurance cover knee replacement in dubai` (1,301 impr, 0 clicks, pos 6.1):

> "Position 6 with zero clicks is not a ranking problem. It's the answer being lifted above
> the results."

Where that pattern appears, blocks 9 (direct answer) and 21 (insurer matrix) stop being
nice-to-have. Ranking harder won't fix it; being the citable source will. Say that plainly.

**Coexistence split.** When the disposition keeps an overlapping page alive, the split has to be
enforced in the draft, not just described. Spoke owns **breadth** (the specialty's cover and
cost mechanics); the retained page owns **depth** on its one procedure. If the draft has two
FAQs and a table row on the retained page's exact subject, those belong to the other page.

---

## Disposition labels and what they mean for linking

Counts across the 105 audited rows:

| Label | Rows | What it means for your linking advice |
|---|---|---|
| DIFFERENTIATE | 33 | Both live. Enforce the split. Link across. |
| REWRITE IN PLACE | 27 | Page stays at its URL. **Safe to link.** |
| KEEP + UPGRADE | 18 | Converts above benchmark. **Safe to link. Do not redirect.** |
| FOLD | 15 | Content merges into the spoke. Don't link; the URL is going away. |
| CONSOLIDATE | 10 | Same. |
| REDIRECT | 2 | URL disappears. **Never link it** — you'd be linking into a redirect. |

**This is why the redirect question has to be settled before you write linking guidance.** The
same target flips from "best anchor on the page" to "do not link" depending on the label. If the
user states a redirect that contradicts the CSV, treat their decision as current but say what it
costs, using the row's own impressions, CTR and position.

---

## Do-not-redirect pages

The audit explicitly marked these KEEP + UPGRADE with "Do not redirect" because they convert
above the `-hiart` benchmark (1.227%). Redirecting one throws away a converting page:

| Page | Impr | Clicks | CTR | Pos |
|---|---|---|---|---|
| `/health-insurance/articles/maternity-insurance-in-uae/` | **138,170** | **1,798** | 1.301% | 8.2 |
| `/is-dermatology-covered-by-health-insurance-hiart/` | 19,261 | 354 | 1.838% | 7.2 |
| `/health-insurance/articles/health-insurance-for-diabetes/` | 10,412 | 145 | 1.393% | 6.9 |
| `/health-insurance/articles/best-health-insurance-plans-for-cancer-patients-in-uae/` | 10,393 | 145 | 1.395% | 10.8 |
| `/health-insurance/articles/health-insurance-for-heart-patients/` | 8,412 | 95 | 1.129% | 12.1 |
| `/health-insurance/health-guide/opd-cover/` | 7,962 | 82 | 1.030% | 8.4 |
| `/health-insurance/articles/insurance-for-kidney-patients/` | 7,003 | 145 | 2.071% | 8.4 |
| `/health-insurance/articles/health-insurance-for-skin-treatment/` | 2,107 | 22 | 1.044% | 6.5 |
| `/heres-how-obesity-affects-your-health-insurance-premiums-hiart/` | 1,672 | 17 | 1.017% | 15.6 |
| `/does-your-health-insurance-plan-cover-tonsillitis-in-uae-hiart/` | 1,368 | 18 | 1.316% | 37.2 |
| `/all-about-health-insurance-for-hypertension-patients-hiart/` | 1,025 | 16 | 1.561% | 14.8 |
| `/does-health-insurance-cover-liver-cirrhosis-hiart/` | 1,010 | 12 | 1.188% | 36.9 |
| `/health-insurance/articles/health-insurance-for-arthritis/` | 338 | 4 | 1.183% | 7.0 |

The maternity page is the launch's single biggest exposure. Flag it if maternity comes up.

---

## The 31 slugs

Confirmed to match the spec exactly (30 spokes + hub, zero mismatches).

```
/health-insurance/cover/                        (hub)
orthopedic  optical  ent  dermatology  cardiac  gp  alternative-medicine  ivf
mental-health  paediatric  neurology  gastro  diabetes-thyroid  urology  gynaecology
physiotherapy  allergy  dental  emergency  cancer  kidney  maternity  respiratory
diagnostics  rheumatology  bariatric  surgery  cosmetic-reconstructive  vaccinations
pre-approval
```

Slug rule: **benefit name, not specialty name** — `dental` not `dentistry`, `respiratory` not
`pulmonology`, `optical` not `ophthalmology`. The spec's row for a page may use the clinical
name in prose while the URL uses the benefit name; match the URL.

Wave order matters: build 🟢 Proven and 🟡 Partial first (measured demand PB already reaches and
fails to convert), sequence ⚪ Unmeasured and 🟠 Thin last. `pre-approval` is flagged as
justifying being built first on its own — `what is a deductible insurance` alone is 61,234
impressions at position 5.5 with zero clicks.

---

## Recurring draft defects

Seen in every draft audited so far. Check each one; most take a sentence to report.

| Defect | How to check |
|---|---|
| **Undeliverable verbs** | Grep for find/browse/book/near me. Hard blocker. |
| **Missing H1** | Some drafts have no `#` heading at all. |
| **Missing ⭐ blocks** | Direct answer and insurer matrix are the two most-skipped. |
| **Converted price tables** | `pbcheck.py peg`. Also look for identical bounds across different procedures — an aggregator tell. |
| **Cross-doc figure conflicts** | The same treatment priced differently in spec, Figma table, hub draft and spoke draft. Compare before accepting any number. |
| **Absolute cover claims** | "all tiers cover…", "always covered". Basic/EBP plans have real limits, and the draft usually contradicts itself a few lines later. |
| **Career-advice framing** | "Qualifications You Need to Become a…" serves aspiring clinicians, not patients. |
| **Spelling mix** | Metadata/URL/keywords use American (matching measured demand); bodies drift into British. Pick one and be consistent. |
| **Heading level jumps** | H2→H4 skipping H3; FAQ label left as plain text so questions nest under nothing. |
| **FAQ length** | 6 questions, 40–60 words each. Count them. |
| **Working notes** | `Keywords-`, `Ref. Links-`, `(Need Clarification)`, `(New Page)`, `(Re-write)` must be stripped. |
| **Third-party citations** | Competitor blogs and paid intermediaries don't clear the source tier. Government `.gov`/`.ae` regulator pages do. |
| **Base64 images** | No alt text, inline data URI. Needs descriptive alt + an optimised asset. |
| **FAQ rich results** | Emit `FAQPage` for machine readability, but Google restricts FAQ rich results to government and health-authority sites — don't promise them to a commercial aggregator. |
