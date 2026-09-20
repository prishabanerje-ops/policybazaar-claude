# TO-DO — `/travel-insurance/uae/` (Travel Insurance UAE)

**Created:** 2026-08-11 · **Source:** five-lens content audit + GSC cannibalization audit
**Audit report:** `Travel Insurance/Result/Final Audit/policybazaar-travel-insurance-uae-content-audit-2026-08-11.md`
**Cannibalization report:** `Cannibalization/Result/cannibalization-report-2026-08-11.xlsx`

| | |
|---|---|
| **Overall content score** | **49 / 100** 🔴 Major rework |
| Lens scores | SEO 52 · GEO 53 · Human-Likeness 41 · YMYL 45 · Fact-Check 52 |
| Leads (2025-05-01 → 2026-08-11) | **1,574** · 240 sales · **15.2% conversion** |
| Revenue | **AED 43,942 APE** · AED 27.9 per lead |
| AI-referred leads | **207 (13.2%) — highest AI share of the three cluster pages** |
| Word count | 6,513 — largest of the three |

### The one number that frames this whole file

This page attracts leads worth essentially the same as the hub's (**AED 27.9 vs 28.2 per lead**) and converts them **6 percentage points worse** (15.2% vs 21.1%). Same traffic value, worse outcome. That is a page-quality problem, not a traffic problem — and the audit found why: no byline, no disclaimer, no excess, three coverage figures with no currency unit, a likely-wrong portability claim, and stale Covid content.

**And it has the cluster's highest AI-referral share (13.2%).** AI engines weight E-E-A-T hardest on YMYL content. This is the page where the E-E-A-T fixes below have the most leverage anywhere in the travel vertical.

---

## 🛣️ Lane rule — read before editing anything

The three pages stay separate (decision: *keep both, differentiate hard*, 2026-08-11). This page's problem is that **it is currently a longer duplicate of the hub with "UAE" appended to every heading.**

| Page | Lane | Owns today (12-month GSC) |
|---|---|---|
| `/travel-insurance/` | Unmodified generic | "travel insurance" 435 cl @ pos 8.2 |
| **`/travel-insurance/uae/` ← this page** | **UAE-modified / UAE-resident** | "travel insurance uae" **162 cl @ pos 11.9** · "travel insurance uae residents" 19 cl @ 8.4 · "uae travel insurance" 16 cl @ 23.7 · "best travel insurance in uae" 6 cl @ 8.2 · "cheap travel insurance uae" 9 cl @ 8.0 |
| `/travel-insurance/travel-insurance-dubai/` | Dubai | "travel insurance dubai" 114 cl / 13,902 impr |

**Proof this page is a duplicate, not a distinct intent:** `inbound` ×0 · `outbound` ×0 · `abroad` ×11 · `schengen` ×12. It is outbound-focused, same as the hub. Section-for-section:

| Hub | This page |
|---|---|
| What is Travel Insurance? | What is Travel Insurance **UAE**? |
| What Does Travel Insurance Cover in UAE? | Inclusions of Travel Insurance **UAE** Plans |
| Does Travel Insurance in UAE Offer Riders? | Travel Insurance Add ons **in UAE** |
| How to Make a Travel Insurance Claim? | Travel Insurance **UAE** Claim Processes |

### ⛔ DO NOT

- **Do not target the unmodified head term.** This page holds **8,021 impressions at pos 8.2 for "travel insurance" and converts 2 clicks**, while the hub holds 22,532 impressions at the same position and converts 435. That is the largest dead-impression block in the travel cluster. Task 5 below is about *removing* that overlap, not deepening it.
- **Do not add "Dubai".** That lane belongs to `/travel-insurance/travel-insurance-dubai/`.
- **Do not consolidate or 301 this page.** Considered and rejected — it earns 162 clicks at pos 11.9 where the hub sits at 50.5, and all 18 `consolidate` / 7 `redirect` verdicts in the travel cannibalization run were downgraded by the safety guards (G3_CROSS_SECTION, G5, G4). **Zero 301s are recommended.**

---

## 🔴 Critical

- [ ] **1. Add the author and reviewer byline — highest-leverage fix on this page.** *(dev + content · 2 h · GEO + YMYL)*
      The WebPage node has **no `author`, no `reviewedBy`**, and the page carries **no visible byline, no reviewer, and no last-updated date** anywhere in 6,513 words. The only "Last Updated" strings on the page come from the shared article carousel.
      The hub's 2026-08-04 edit already fixed exactly this and **is the reference pattern** — copy it:
      - `author` → Person, **Mousree Das**, `jobTitle` + `url` → `/author/mousree-das/`
      - `reviewedBy` → Person, **Richa Bansal**, *"Business Development Manager – Travel & Home Insurance"*
      - Visible "Written by / Reviewed by / Last updated on" block below the H1
      - Editorial Standards link
      **Why this one first:** YMYL page, AED 43,942 APE, 13.2% of leads arriving from ChatGPT/Perplexity, and currently 1 of 4 E-E-A-T pillars.

- [ ] **2. Remove or correct the portability claim.** *(content + product sign-off · 30 min · YMYL/Fact-Check)*
      Current text: *"To provide you with ease and convenience, travel insurance UAE can be ported from one insurer to another. However, take note that you can port annual plans only during the renewal period."*
      Portability is a **health**-insurance mechanism in the UAE (≥12 months continuity, 45-day notice, renewal-only). **No source was found supporting inter-insurer portability of travel policies.** It reads as copy-paste from health content. A reader could delay buying, believing cover transfers later.
      **Replace with:** *"Annual multi-trip policies can be renewed with the same insurer, or you can buy a new policy from a different insurer at expiry. Cover does not transfer mid-term."*
      ⚠️ **Confirm with the product team before publishing** — this is the one item in this file where I could not reach a verified answer either way.

- [ ] **3. Fix the stale Covid framing.** *(content · 20 min · YMYL/Fact-Check)*
      Two places:
      - Insights table: *"Covid-19 coverage — **Mandatory** quarantine stay expenses for 7 to 14 days, including the cost for RT-PCR tests and medicines."*
      - *"Covid 19 Coverage"* section: *"…you start receiving the insurance benefits **as soon as you are tested Covid-19 positive**."*
      The **benefit still exists** in 2026 UAE travel policies — but *"Mandatory"* asserts a government quarantine mandate that no longer applies, and the benefit is usually conditional and often an add-on.
      **Reframe:** *"Optional or built-in depending on insurer — typically covers quarantine accommodation and treatment costs if you test positive abroad. Check whether your plan includes it or needs the add-on."* Drop *"Mandatory"*.
      ⚠️ Also on `/dubai/` — fix both so they agree.

- [ ] **4. Add currency units to three coverage figures.** *(content/data · 15 min · Fact-Check)*
      In the *Top Travel Insurance UAE Plans* table:
      - *"Trip cancellation cover of up to **5,000**"*
      - *"Personal Liability Cover of **1,000,000**"*
      - *"Accidental Death cover of **150,000**"*
      Sibling rows in the same table use USD, but these three state no unit — on a page that quotes both USD and AED. **AED vs USD is a ~3.67× difference on a financial product.** Add the unit to every figure and audit the whole table for consistency.

---

## 🟠 High

- [ ] **5. Differentiate the content — the cannibalization root cause.** *(content · 2–3 days · **cannibalization** + SEO + GEO)*
      This is the big one, and it fixes three separate findings at once: the duplicate-content risk (SEO 3/10), the missing original angle (GEO 3/8), and the 8,021 dead head-term impressions.
      **Cut** every section that only restates the hub with "UAE" appended.
      **Build** around UAE-resident specifics the hub does *not* cover:
      - Visa-linked cover for UAE residents — which destinations mandate it, and the minimums (Schengen appears 12× on this page already and is under-exploited)
      - Emirates ID / residency requirements when buying and when claiming
      - The UAE-departure claim process: who to call from abroad, what UAE-side documentation insurers ask for
      - Named UAE insurers' **territorial tiers** — PB's own sold-plan names include *"Individual Standard (Worldwide excl. Schengen/US/CA)"*, which is genuinely useful and appears nowhere on the page
      - Inbound vs outbound: the page is 100% outbound today despite the hero carrying a "Traveling to the UAE" toggle
      **Success test:** could this page's body be published on the hub with a find-and-replace of "UAE"? Today: yes. After: no.

- [ ] **6. Add policy excess and a YMYL disclaimer.** *(content · 1 h · YMYL)*
      - **"excess" ×0 · "sub-limit" ×0 · "policy wording" ×0** across 6,513 words — alongside six plan rows quoting limits up to USD 1,000,000. Add a "what you pay at claim time" block after the plans table.
      - `"disclaimer": null` and the word "disclaimer" appears **zero times**. Add a prominent disclaimer: premiums and coverage indicative and subject to change; verify against the insurer's policy wording and official consulate/ICP guidance.
      ⚠️ Both cluster-wide — see the Cluster-wide section.

- [ ] **7. Fix two stale insurer names.** *(content · 10 min · Fact-Check)*
      In the *Top Travel Insurance UAE Plans* table:
      - [ ] *"AXA Travel Insurance"* → **"GIG Gulf"**. AXA Gulf became GIG Gulf in June 2022. The hub already renders this correctly as *"GIG Gulf (Previously AXA)"* — the correct string exists on the same site.
      - [ ] *"Alliance Travel Insurance"* → **"Allianz"**. It's the insurer supplying this page's own AED 22 headline price.

- [ ] **8. Fix image alt text.** *(dev · 45 min · SEO + accessibility)*
      - [ ] **11 `view-quotes.png` CTA images with no `alt` attribute at all.** The page's primary conversion control is invisible to screen readers, 11 times over. Set `alt="View travel insurance quotes"`, or `alt=""` if the button already carries a visible text label.
      - [ ] 5 insurer logos with `alt="Salama Insurance"` — cluster-wide bug, has its own ticket (`docs/jira-alt-text-insurer-logos-travel-plan-cards.md`).

- [ ] **9. Fix the "60-65 years" age ceiling.** *(content · 20 min · Fact-Check/YMYL)*
      Insights table: *"Age Range Covered — 30 days to 60-65 years"*. A range expressed as a range, and it isn't the ceiling — **PB.ae itself sells over-65, over-70 and over-75 travel cover**. State the actual per-insurer bands and link all three pages. Fixes an error and adds three commercial links in one edit.

---

## 🟡 Medium

- [ ] **10. Collapse four near-identical H2s.** *(content · 30 min · SEO + GEO)*
      The page has a bare **"Travel Insurance UAE"** H2 that repeats the H1 verbatim, **"Top Travel Insurance UAE Plans" twice**, and **"Best Travel Insurance UAE"**. Four headings competing to be the primary section. Collapse to one plans H2 and one overview H2; delete the bare duplicate.

- [ ] **11. Refresh `dateModified` and add a visible date.** *(dev + content · 15 min · GEO)*
      `dateModified: 2026-03-30` — **4.5 months stale**, and no visible date anywhere. Update after shipping the content work above (not before).

- [ ] **12. Rewrite the meta description.** *(content · 15 min · SEO)*
      Current: *"Best Travel Insurance UAE : Buy Travel Insurance UAE from Policybazaar, which Includes Medical Related Coverage, Emergency Medical Expenses, Medical E…"* — a truncated feature list, stray space before the colon, "Travel Insurance UAE" twice, no CTA, cuts off mid-word.
      Write a value proposition with a CTA, in the **UAE-resident** lane — not generic, not Dubai.

- [ ] **13. Reduce exact-match keyword insertion.** *(content · part of task 5 · SEO)*
      uae ×135 in 6,513 words, with "travel insurance UAE" jammed into nearly every heading and paragraph — *"travel insurance UAE Cost"*, *"a travelling insurance plan in the UAE"*. Fold this into the task-5 rewrite rather than doing a separate pass.

- [ ] **14. Add schema foundation nodes.** *(dev · part of the cluster-wide schema ticket · SEO)*
      Missing: `InsuranceAgency` canonical node · `WebSite` node · `Service` → `OfferCatalog` → `Offer` (six priced plans entirely unmarked). Plus no `@id` on any node, and `WebPage` missing `isPartOf` / `breadcrumb` / `primaryImageOfPage`. Bugs T2, T3, T11 all present.

---

## 🟢 Quick wins

- [ ] **15.** Proofread the Insights table and FAQ: **"Claim Settlement Preiod"** → "Period" · **"upto"** ×2 → "up to" · FAQ Q10 *"Can I opt for are specific Travel Insurance in UAE?"* → fix the grammar. *(content · 15 min)*
- [ ] **16.** Delete the *"In that light, let's go through the article below to find the best travel insurance UAE…"* opener. Replace with the answer: *"UAE residents need travel insurance for Schengen and several other visas, and cover starts at AED 22 for a single trip."* *(content · 10 min)*
- [ ] **17.** Strip the `"Qn."` prefixes from FAQ `Question.name` (11 questions). *(dev · 10 min)*
- [ ] **18.** Add 5 outbound links — all verified live in `assets/policybazaar-urls.txt`, none currently linked: *(content · 25 min)*
      `/travel-insurance-calculator-uae/` (the page has a *"How to Calculate Travel Insurance Premium Online in UAE"* section and doesn't link the calculator) · `/travel-insurance/travel-insurance-for-over-65/` +`/over-70/` +`/over-75/` · `/travel-insurance/articles/does-travel-insurance-cover-pregnancy/` · `/travel-insurance/articles/baggage-travel-insurance/` · `/schengen-travel-insurance-tic/` (schengen ×12 on this page; that category page earns AED 82,285 APE)
- [ ] **19.** Collapse the 49-link destination block behind the existing "Expand" control. *(dev · 30 min)*

---

## 🔗 Cluster-wide — fix once at template level, not three times

| # | Defect | Scope | Ticket |
|---|---|---|---|
| C1 | 5 logos `alt="Salama Insurance"` per plan-quote card | 4+ travel pages, 20+ images, zero correct | `docs/jira-alt-text-insurer-logos-travel-plan-cards.md` |
| C2 | `"disclaimer": null` | All 3 pages | — |
| C3 | Bugs T2 / T3 / T11 + no `@id` on any node | All 3 pages | — |
| C4 | `"excess"` / `"sub-limit"` / `"policy wording"` = 0 occurrences | All 3 pages | — |
| C5 | Stale Covid *"Mandatory quarantine… 7 to 14 days"* | This page + `/dubai/` | — |
| C6 | No `author` / `reviewedBy` | This page + `/dubai/`. **The hub is fixed — use it as the pattern.** | — |

---

## ✅ Acceptance criteria

- [ ] Visible byline (author + reviewer + last-updated) present, and `author`/`reviewedBy` in the JSON-LD.
- [ ] The portability claim is either removed or replaced with a product-team-confirmed statement.
- [ ] `grep -c "Mandatory quarantine"` returns 0.
- [ ] Every coverage figure in the plans table carries a currency unit.
- [ ] `grep -c "AXA Travel Insurance\|Alliance Travel"` returns 0.
- [ ] No image on the page lacks an `alt` attribute.
- [ ] "excess" appears at least once; a disclaimer is present near the top.
- [ ] **Find-and-replace test:** the body can no longer be published on the hub by swapping "UAE" out.
- [ ] Impressions for the unmodified term "travel insurance" on this URL trend **down** at the next cannibalization check, while "travel insurance uae" clicks hold or rise.
- [ ] Lead conversion moves toward the hub's 21.1% from today's 15.2%.

**Re-audit trigger:** `/content-audit https://www.policybazaar.ae/travel-insurance/uae/` after shipping, then `/uae-insurance cannibalization travel` 4–6 weeks later.

**Unresolved:** the portability claim (task 2) needs product-team confirmation — I could not verify it either way. Rank positions in the lane table are 12-month GSC averages, not live positions.
