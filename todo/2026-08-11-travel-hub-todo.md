# TO-DO — `/travel-insurance/` (Travel Insurance hub)

**Created:** 2026-08-11 · **Source:** five-lens content audit + GSC cannibalization audit
**Audit report:** `Travel Insurance/Result/Final Audit/policybazaar-travel-insurance-content-audit-2026-08-11.md`
**Cannibalization report:** `Cannibalization/Result/cannibalization-report-2026-08-11.xlsx`

| | |
|---|---|
| **Overall content score** | **63 / 100** 🟠 Needs work *(highest of the three cluster pages)* |
| Lens scores | SEO 69 · GEO 77 · Human-Likeness 48 · YMYL 59 · Fact-Check 56 |
| Leads (2025-05-01 → 2026-08-11) | **5,470** · 1,156 sales · **21.1% conversion** *(best of the three)* |
| Revenue | **AED 154,524 APE** · AED 28.2 per lead · **#1 travel page by APE** |
| AI-referred leads | 468 (8.6%) |
| GSC (12mo) | 1,453 clicks · 191,251 impressions · 282 queries |

---

## 🛣️ Lane rule — read before editing anything

The three pages stay separate (decision: *keep both, differentiate hard*, 2026-08-11). Each owns one intent lane. **Most of the cannibalization damage in this cluster came from pages drifting out of their lane, not from the pages existing.**

| Page | Lane | Owns today (12-month GSC) |
|---|---|---|
| **`/travel-insurance/` ← this page** | **Unmodified generic** | "travel insurance" **435 cl @ pos 8.2** · "travel insurance online" 67 cl @ 5.6 · "cheap travel insurance" 51 cl @ 5.2 · "cheapest travel insurance" 48 cl @ 6.4 · "buy travel insurance online" 22 cl @ 6.6 |
| `/travel-insurance/uae/` | UAE-modified / UAE-resident | "travel insurance uae" 162 cl @ pos 11.9 · "travel insurance uae residents" 19 cl @ 8.4 |
| `/travel-insurance/travel-insurance-dubai/` | Dubai | "travel insurance dubai" 114 cl / 13,902 impr |

### ⛔ DO NOT — lane discipline for this page

- **Do not add "UAE" to the H1, title or meta.** `/travel-insurance/uae/` owns that intent at pos 11.9; this page currently sits at **pos 50.5** for "travel insurance uae". Adding UAE would put two PB pages head-on where one is already winning. *(An earlier draft of the audit recommended exactly this. It was withdrawn on the GSC evidence.)*
- **Do not add "Dubai" targeting.** The Dubai page earns 171 clicks / 28,740 impressions across Dubai queries; this page earns 5 clicks / 683 impressions and records **zero impressions** on the four biggest Dubai terms.
- **Do not restructure the generic head-term sections.** This page converts at 21.1% and is the #1 travel page by APE. Everything below is additive or corrective — nothing asks you to rebuild what works.

---

## 🔴 Critical — factual and safety errors

- [ ] **1. Fix the visa-mandate self-contradiction.** *(content · 15 min · YMYL)*
      The H2 body says: *"Yes, travel insurance is necessary to apply for a UAE visit visa, irrespective of your nationality or the country you are travelling from."* FAQ **Q6** says: *"While it is not mandatory for all visitors to the UAE, is highly recommended."*
      GDRFA's single-entry tourist visa service lists *"medical insurance valid in UAE"* among required documents, so the H2 is correct and Q6 is wrong. Q6 is also missing a word.
      **Rewrite Q6 to:** *"Yes. Medical insurance valid in the UAE is a required document for UAE visit and tourist visa applications, per GDRFA/ICP. Separately, Schengen visas require a policy with at least €30,000 of medical cover."* Link ICP and GDRFA.

- [ ] **2. Fix the pregnancy answer.** *(content · 20 min · YMYL)*
      FAQ **Q10** says flatly: *"No, travel insurance does not cover pregnancy."* Wrong in the direction that costs a traveller money — unforeseen pregnancy complications are typically covered; what's excluded is routine pregnancy, prenatal care and childbirth.
      **Rewrite to:** *"Routine pregnancy, prenatal care and childbirth are excluded. Most policies do cover unforeseen pregnancy complications, subject to the policy wording and any pre-existing-condition terms. Airlines set their own limits — Emirates requires a medical certificate from week 29 and does not carry single pregnancies from week 37 (week 33 for multiples)."*
      Link `/travel-insurance/articles/does-travel-insurance-cover-pregnancy/` — PB already publishes this and the hub doesn't link it.
      ⚠️ The Dubai page makes the mirror-image error (*"Any kind of pregnancy complications"* as a blanket exclusion). Fix both in the same pass so they agree.

- [ ] **3. Add policy excess.** *(content · 45 min · YMYL + AI-detection)*
      The strings **"excess", "deductible" and "sub-limit" appear zero times** across 4,510 words, while *"Secure Your Travel for Just AED 22\*"* headlines the hero and the title tag.
      **Add a "What you pay at claim time" block** after the plan table: what an excess is, the typical UAE travel-policy range, and that it applies **per claim**, not per policy.
      This is also the single biggest driver of the Human-Likeness score (Signal E fired at 3/3).

- [ ] **4. Fix three provider-name errors.** *(content · 20 min · Fact-Check)*
      - [ ] *"AXA QIC Standard Traveler"* → **"QIC Standard Traveler"**. Two unrelated insurers conflated: AXA Gulf became GIG Gulf (June 2022); QIC is Qatar Insurance Company. The same plan appears correctly as "QIC" one table above.
      - [ ] FAQ Q8 *"…RAK Insurance, **Alliance**, Watania Takaful, GIG Gulf"* → **"Allianz"**. It's the insurer supplying this page's own AED 22 headline price.
      - [ ] Travel Insurers block lists **"RSA Travel Insurance"** and **"Liva Travel Insurance"** as separate entries. RSA Middle East + NLGIC rebranded to Liva GCC-wide in Sept 2023 — remove or redirect the RSA entry.
      - [ ] Same block: **"Oman Travel Insurance"** → **"Sukoon Travel Insurance"** (Oman Insurance rebranded). Note the label also collides with the Oman *destination* page linked elsewhere on this page.
      *Unfixed across 4 consecutive audits (07-28, 07-29, 08-03, 08-11).*

---

## 🟠 High

- [ ] **5. Add contextual body links to `/uae/` and `/dubai/`.** *(content · 20 min · **cannibalization**)*
      Both siblings are currently reachable from **navigation only** — there is no contextual body link from the hub to either. That's why the cluster reads as three competing pages rather than a hub with spokes; the guards returned `hub-and-spoke` on 22 of the 90 travel pairs.
      Add, in prose, in the relevant sections:
      - *"UAE residents"* → `/travel-insurance/uae/`
      - *"travelling from Dubai"* → `/travel-insurance/travel-insurance-dubai/`
      This is the cheapest cannibalization fix available and it costs nothing on this page's own rankings.

- [ ] **6. Add a page-level YMYL disclaimer.** *(dev + content · 30 min · YMYL)*
      Page config still shows `"disclaimer": null` — flagged on 2026-08-03 and unfixed. Only a mid-page visa note and a table footnote exist, and neither points to **the insurer's policy wording**.
      **Add near the top:** premiums, coverage limits and visa requirements are indicative and subject to change; verify against the insurer's policy wording and official consulate / ICP guidance before purchasing.
      ⚠️ **Cluster-wide** — `"disclaimer": null` on all three pages. Fix at template level (see Cluster-wide section).

- [ ] **7. Remove the duplicate review.** *(dev/content · 10 min · SEO)*
      The identical body *"For a quick and easy process to buy travel insurance online, always choose from Policybazaar…"* is published under **two different reviewer names** — Javed Khan (12 Feb 2026) and Ravish (5 Jun 2025) — in both the JSON-LD and the visible carousel. Identical testimony under two names is a visible trust failure.

- [ ] **8. Fix the schema foundation.** *(dev · 2–3 h · SEO)*
      - [ ] Declare the canonical `InsuranceAgency` node once at `@id: https://www.policybazaar.ae/#organization` — currently `parentOrganization` points at an `@id` **no node on the page declares** (bug T11).
      - [ ] Add a `WebSite` node at `.../#website`. **Do not add SearchAction** — blocklisted, feature removed Nov 2024.
      - [ ] Give every node an `@id`. All four are currently anonymous.
      - [ ] Remove the boilerplate `AggregateRating` 4.7 / 43,419 from the `Organization` node named *"Travel Insurance"* (bug T2) — a page topic is not an organisation, and self-serving review markup on the entity being sold is a policy risk.
      - [ ] Convert review `datePublished` from *"12 February 2026"* to ISO-8601 `2026-02-12` (bug T3).
      - [ ] Add `isPartOf`, `breadcrumb` ref and `primaryImageOfPage` to `WebPage`.
      - [ ] Add `Service` → `OfferCatalog` → `Offer` — 10 named plans with AED prices are currently entirely unmarked. Biggest GEO-value gap on the page.
      ⚠️ **Cluster-wide** — T2/T3/T11 and the missing `@id`s are on all three pages.

---

## 🟡 Medium

- [ ] **9. Merge the two "Best Plans" sections.** *(content · 30 min · SEO)*
      Two H2s — *"Best Travel Insurance Plans 2026"* and *"Best Travel Insurance Plans in UAE 2026"* — with different plan tables and contradictory entry prices (AED 22 vs AED 33). Merge into one, or retitle the second to its actual differentiator (e.g. *"Outbound Plans from the UAE — Starting Premiums"*).
      Note: the second table's title contains "UAE" — when retitling, keep it a **plan-type** distinction, not a geo one, or it drifts into `/uae/`'s lane.

- [ ] **10. Fix the Schengen AED conversion.** *(content · 10 min · Fact-Check)*
      *"at least 30,000 Euros, which is approximately AED 125,000"*. At the early-Aug-2026 rate (4.2373 AED/EUR) €30,000 ≈ **AED 127,200**. A reader buying AED 125,000 of cover is short.
      **Drop the static AED figure.** State €30,000 as the binding requirement and add "converted at the prevailing rate", or a visible as-of date. Flagged on 2026-08-03 and still drifting.
      While there: attribute the €30,000 to the **EU Visa Code (Reg. 810/2009, Art. 15)**, state it covers all **29** Schengen states, and note approval stays at consulate discretion.

- [ ] **11. Attach limits to the coverage and rider lists.** *(content · 1–2 h · GEO + AI-detection)*
      The 11-item *"What Does Travel Insurance Cover in UAE?"* list and the 6-item rider list are bare noun phrases with **no limits, sub-limits or prices**. Highest-value single content fix for both AI citation and buyer trust.
      Example: *"Emergency medical expenses and evacuation — typically $50,000–$100,000, subject to a $50–$100 excess per claim."*

- [ ] **12. Fix the Watania plan-card data contradiction.** *(dev/data · 15 min · YMYL)*
      Watania Takaful *Annual Gold* lists **"Trip Cancellation Additionally Available"** and **"Trip Cancellation NA"** on consecutive rows. Same benefit, both states. Fix the feed so each benefit renders once, and audit the other four cards.

---

## 🟢 Quick wins

- [ ] **13.** Strip the `"Q1."`–`"Q11."` prefixes from FAQ `Question.name`. The numbering **restarts three times**, so there are three distinct questions named "Q1." in one FAQPage node. Keep visual numbering in CSS. *(dev · 15 min)*
- [ ] **14.** Fix the anchor/URL mismatch in *"Know More About Travel Insurance"*: anchor *"Myths and Truths About Trip Cancellation Insurance"* points at `/articles/cancel-for-any-reason-travel-insurance/`, and **the row is listed twice**. Fix the anchor to describe CFAR cover; delete the duplicate. *(content · 10 min)*
- [ ] **15.** Add 7 outbound links — all verified live in `assets/policybazaar-urls.txt`, none currently linked: *(content · 30 min)*
      `/travel-insurance/articles/does-travel-insurance-cover-pregnancy/` · `/travel-insurance/travel-insurance-for-over-65/` (+`/over-70/`, `/over-75/`) · `/travel-insurance-calculator-uae/` · `/travel-insurance/articles/baggage-travel-insurance/` · `/travel-insurance/articles/apply-schengen-visa-in-dubai/` · `/travel-insurance/europe-visa/` · `/travel-insurance/articles/travel-insurance-claim-reimbursement/`
- [ ] **16.** Collapse the 49-link *Most Travelled Countries* block to the top 8–10 behind the existing "Expand" control. It's a mobile UX problem and the main driver of the page's 8.07% keyword density. *(dev · 30 min)*
- [ ] **17.** *Optional, low value:* drop "Dubai" from the title tag. Costs at most 683 impressions / 5 clicks. **Do not replace it with "UAE".** Do this for tidiness, not traffic. *(content · 5 min)*

---

## 🔗 Cluster-wide — fix once at template level, not three times

These are on **all three** pages. Fixing them per-page wastes effort and guarantees drift.

| # | Defect | Scope | Ticket |
|---|---|---|---|
| C1 | 5 insurer logos with `alt="Salama Insurance"` on every travel plan-quote card | 4+ travel pages, 20+ images, **zero** correct instances. Salama has no travel URL on PB.ae. | `docs/jira-alt-text-insurer-logos-travel-plan-cards.md` |
| C2 | `"disclaimer": null` | All 3 pages | — |
| C3 | Bugs T2 / T3 / T11 + no `@id` on any node | All 3 pages | — |
| C4 | `"excess"` / `"sub-limit"` / `"policy wording"` = **0 occurrences** | All 3 pages | — |
| C5 | Stale Covid *"Mandatory quarantine… 7 to 14 days"* framing | `/uae/` and `/dubai/` (not the hub) | — |
| C6 | No `author` / `reviewedBy` | `/uae/` and `/dubai/` — **the hub is already fixed and is the reference pattern** | — |

---

## ✅ Acceptance criteria

- [ ] FAQ Q6 and the visa H2 state the same thing, and both cite GDRFA/ICP.
- [ ] No page in the cluster states an unqualified position on pregnancy cover.
- [ ] "excess" appears at least once, in a block explaining what the buyer pays per claim.
- [ ] `grep -c "AXA QIC\|Alliance Travel\|RSA Travel Insurance\|Oman Travel Insurance"` returns 0.
- [ ] The hub links `/uae/` and `/dubai/` from body prose, not just navigation.
- [ ] Hub title, meta and H1 contain **no** "UAE" and (optionally) no "Dubai".
- [ ] Hub still ranks pos ≤10 for "travel insurance" and holds ≥21% lead conversion at the next check.

**Re-audit trigger:** run `/content-audit https://www.policybazaar.ae/travel-insurance/` after shipping, and `/uae-insurance cannibalization travel` 4–6 weeks later to confirm the lanes separated rather than re-collided.

**Unresolved:** rank positions in the lane table are 12-month GSC averages (2025-08-11 → 2026-08-08), not current live positions. Re-check before acting on anything position-sensitive.
