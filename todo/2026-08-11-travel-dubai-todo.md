# TO-DO — `/travel-insurance/travel-insurance-dubai/` (Travel Insurance Dubai)

**Created:** 2026-08-11 · **Source:** five-lens content audit + GSC cannibalization audit
**Audit report:** `Travel Insurance/Result/Final Audit/policybazaar-travel-insurance-dubai-content-audit-2026-08-11.md`
**Cannibalization report:** `Cannibalization/Result/cannibalization-report-2026-08-11.xlsx`

| | |
|---|---|
| **Overall content score** | **47 / 100** 🔴 Major rework *(lowest of the three cluster pages)* |
| Lens scores | SEO 52 · GEO 53 · Human-Likeness **33** · YMYL **37** · Fact-Check 57 |
| Leads (2025-05-01 → 2026-08-11) | **686** · 84 sales · **12.2% conversion** *(worst of the three)* |
| Revenue | **AED 12,215 APE** · **AED 17.8 per lead — 37% below its two siblings** |
| AI-referred leads | 28 (4.1%) — lowest of the three |
| Word count | 3,909 |

### What this page is good at, and what it isn't

**Good:** it owns Dubai intent outright — 114 clicks / 13,902 impressions on "travel insurance dubai", where the hub records **zero impressions**. The Dubai framing is genuine differentiation, and its plan table names insurers **correctly** ("GIG Gulf (Previously AXA)", "QIC") where the hub renders one as the non-existent *"AXA QIC"*. Use this page as the reference for that data.

**Not good:** lowest content score, lowest conversion, and lowest lead value in the cluster. Those facts are connected. This page carries an unsupportable "complete protection" promise, a factual error about age limits, a claim about worldwide coverage that **PB's own sold-plan names refute**, an empty provider table, no FAQ markup, and no accountability signal.

---

## 🛣️ Lane rule — read before editing anything

The three pages stay separate (decision: *keep both, differentiate hard*, 2026-08-11). This page's lane is clean **inbound** — nothing else competes for Dubai. Its problem is **outbound bleed**: it reaches for generic and UAE terms it loses.

| Page | Lane | Owns today (12-month GSC) |
|---|---|---|
| `/travel-insurance/` | Unmodified generic | "travel insurance" 435 cl @ pos 8.2 |
| `/travel-insurance/uae/` | UAE-modified / UAE-resident | "travel insurance uae" 162 cl @ pos 11.9 |
| **`/travel-insurance-dubai/` ← this page** | **Dubai** | "travel insurance dubai" **114 cl / 13,902 impr** · "travel insurance for dubai" 6,480 impr · "dubai travel insurance" 2,639 impr · "cheap travel insurance dubai" @ pos 11.0 · "travel insurance dubai price" 5 cl @ pos 11.4 |

### Where this page is currently losing by leaving its lane

| Query it reaches for | Its position | Result |
|---|---|---|
| "travel insurance" | pos 11.4 · 2,962 impr | **3 clicks** |
| "travel insurance online" | pos 17.3 · 1,137 impr | **1 click** |
| "buy travel insurance online" | pos 34.2 · 762 impr | **2 clicks** |
| "travel insurance uae" | pos 43.9 · 2,275 impr | 13 clicks |

**~7,100 impressions converting at roughly 0.1%.** Tasks 5 and 6 below reclaim that attention for Dubai terms it already wins.

### ⛔ DO NOT

- **Do not target unmodified generic terms** ("travel insurance", "travel insurance online", "buy travel insurance online"). The hub wins all three at pos 5–8.
- **Do not target UAE-modified terms.** `/travel-insurance/uae/` owns those.
- **Do not 301 this page.** It owns its lane cleanly. All destructive verdicts in the travel cannibalization run were downgraded by the safety guards; **zero 301s are recommended.**

---

## 🔴 Critical — four factual/safety errors, all in reader-facing copy

- [ ] **1. Delete the "No Age Discrimination" claim — it's wrong and the page contradicts itself.** *(content · 30 min · YMYL/Fact-Check)*
      Current text: *"**No Age Discrimination:** Most life and health insurance plans in Dubai come with certain age limits and restrictions. However, travel insurance plans have no such limitations, and people from any age group can apply for travel insurance Dubai plans."*
      Three problems: (a) it's factually wrong — age bands are standard in travel insurance; (b) it **contradicts this page's own Insights table** three screens above, which states *"Age Range: 30 days to 60-65 years"*; (c) **PB.ae itself sells separate over-65, over-70 and over-75 travel products.**
      A 68-year-old reading this would believe no age restriction applies, apply, and risk a refused application or a declined claim.
      **Replace with:** *"Age bands apply and vary by insurer. Standard plans typically run to 65; cover for travellers over 65, 70 and 75 is written separately and priced higher, sometimes with medical screening."*
      Link `/travel-insurance/travel-insurance-for-over-65/`, `/over-70/`, `/over-75/`. Fixes the error and adds three commercial links in one edit.

- [ ] **2. Replace the "Complete Protection" claim.** *(content · 30 min · YMYL)*
      Current: *"**Complete Protection:** With a travel insurance Dubai plan, you can get complete protection against any loss or damage caused to you or your family members while travelling."*
      Absolute, unsupportable, and **directly refuted by this page's own 12-item exclusions list 60 lines further down.** This is the clearest harmful-framing failure found across all three pages.
      **Replace with:** *"Travel insurance covers the specific events named in the policy schedule — medical emergencies, cancellation, baggage, liability — each to its own limit and subject to an excess. Anything not listed is not covered."*

- [ ] **3. Replace the "Worldwide Coverage" claim — PB's own product names refute it.** *(content · 30 min · YMYL/Fact-Check)*
      Current: *"**Worldwide Coverage:** Most travel insurance Dubai plans offer worldwide coverage. So no matter what location you are travelling to across the globe, your insurance company always has your back."*
      PB's own sold-plan names in the leads data read **"Individual Standard (Worldwide excl. Schengen/US/CA)"**. Territorial validity is the most common reason a travel claim is refused, and this copy says the opposite of the truth.
      **Replace with:** *"Cover is defined by territorial validity, not 'worldwide'. Schengen, US and Canada are commonly rated or excluded separately — check that the schedule names your destination before you travel."*

- [ ] **4. Fix the pregnancy exclusion.** *(content · 20 min · YMYL/Fact-Check)*
      Exclusions list currently reads: *"Any kind of pregnancy complications"*.
      Blanket exclusion, and wrong in the direction that costs a traveller money. Travel policies commonly **do** cover unforeseen pregnancy complications; what's excluded is routine pregnancy, prenatal care and childbirth. As written, it may stop a pregnant traveller claiming on cover she holds.
      **Replace with:** *"Routine pregnancy, prenatal care and childbirth are excluded. Unforeseen pregnancy complications may be covered — check the policy wording and any pre-existing-condition terms."*
      Link `/travel-insurance/articles/does-travel-insurance-cover-pregnancy/`.
      ⚠️ **The hub makes the mirror-image error** (*"No, travel insurance does not cover pregnancy"*). Fix both in the same pass so the two pages agree.

---

## 🟠 High

- [ ] **5. Rescope the first H2 out of the UAE lane.** *(content · 20 min · **cannibalization**)*
      The page's **first H2** is *"Top Travel Insurance Plans in UAE"*, and the body under it opens *"Some of the best Travel Insurance quotes in UAE & Dubai are:"*. That sends the page's strongest structural signal to a geo a sibling page already wins.
      - Retitle to **"Top Travel Insurance Plans in Dubai"**
      - Rewrite the intro line to Dubai scope
      This is the single most direct cannibalization fix on this page.

- [ ] **6. Cut generic-intent copy from the benefits and coverage sections.** *(content · 1 day · **cannibalization** + SEO)*
      Tasks 2 and 3 already remove two of the generic benefit blocks. Continue through the rest: the *Benefits of Buying Travel Insurance Dubai* section and the *What Is Covered* section restate each other, and both are written in generic travel-insurance language that competes with the hub rather than serving a Dubai searcher.
      **Replace generic benefit prose with Dubai-specific substance:** DXB/DWC departure realities, which destinations Dubai residents most commonly need visa-mandated cover for, Dubai-side claim contacts, and — once task 7 is done — which insurers actually sell Dubai travel cover.
      **Success test:** would a reader searching "travel insurance dubai" get something here they can't get on the hub? Today: mostly no.

- [ ] **7. Populate or remove the empty provider table.** *(content/data · 2 h · SEO + GEO + YMYL)*
      The H2 *"Best Travel Insurance Dubai Providers"* is followed by a table containing **only empty cells**. A heading promises the page's single most Dubai-specific asset — which insurers actually sell Dubai travel cover — and delivers nothing. It also renders as blank rows, so it's a visible defect, not just a markup gap.
      Either populate it with insurer names and their Dubai-relevant plans, **or delete the heading** until it can be populated. Shipping a heading over an empty table on the lowest-converting page in the cluster is the worst of both options.

- [ ] **8. Add FAQPage markup (bug T8).** *(dev · 1 h · GEO)*
      The page has an on-page **`Faq's`** block with **9 question-form headings** and **no `FAQPage` node at all**. Same defect class as `/travel-insurance/france-visa/`.
      - Add `FAQPage` markup for the existing Q&A pairs
      - Promote the `Faq's` heading from **H3 to H2** while you're in there
      Cheapest GEO win available on this page — and it has the lowest AI-referral share of the three (4.1%), so it has the most headroom.

- [ ] **9. Add the author and reviewer byline.** *(dev + content · 2 h · GEO + YMYL)*
      No `author`, no `reviewedBy`, no visible byline, no visible date. The hub's 2026-08-04 edit fixed exactly this and **is the reference pattern** — copy it: `author` → Person (Mousree Das, with `/author/mousree-das/`), `reviewedBy` → Person (Richa Bansal, *Travel & Home Insurance*), visible "Written by / Reviewed by / Last updated on", Editorial Standards link.

- [ ] **10. Add policy excess and a YMYL disclaimer.** *(content · 1 h · YMYL)*
      - **"excess" ×0 · "sub-limit" ×0 · "policy wording" ×0** while *"Starting at AED 22"* headlines the page. On the page with the **lowest lead value of the three (AED 17.8/lead)**, telling buyers what they actually pay at claim time is a lead-quality fix as much as a compliance one.
      - `"disclaimer": null`, and the word appears **zero times**. Add a prominent disclaimer.
      ⚠️ Both cluster-wide — see the Cluster-wide section.

---

## 🟡 Medium

- [ ] **11. Fix the stale Covid framing.** *(content · 15 min · Fact-Check)*
      Insights table: *"Covid-19 coverage — **Mandatory** quarantine stay expenses for 7 to 14 days, including the cost for RT-PCR tests and medicines."* The benefit still exists in 2026 UAE policies, but *"Mandatory"* asserts a government quarantine mandate that no longer applies. Drop *"Mandatory"*; state it's insurer-dependent and often an add-on.
      ⚠️ Also on `/uae/` — fix both so they agree.

- [ ] **12. Fix broken keyword insertion.** *(content · part of task 6 · SEO)*
      dubai ×85 in 3,909 words, inserted as a fixed phrase to the point of breaking grammar: *"the insurance for Dubai travels"*, *"insurance for Dubai travel"*, *"your travel insurance Dubai also covers"*. Worst keyword insertion of the three pages. The page already ranks for Dubai — it does not need the phrase in every sentence.

- [ ] **13. Convert the coverage sections to a table.** *(content · 3 h · AI-detection + GEO)*
      **20+ consecutive** bolded-label-plus-colon-plus-uniform-paragraph blocks (*Complete Protection:* / *Worldwide Coverage:* / *No Age Discrimination:* / *Cancellation Refunds:* / *Covid-19 Cover:* / *Medical Cover:* / *Hospital Cash Allowance:* …). This drove Signal D to 3/3 and is the main reason Human-Likeness is 33 — the lowest of the three pages.
      **Replace with a three-column table: benefit · typical limit · excess.** Reserve prose for the two or three points that genuinely need explaining. This also delivers task 10's excess requirement.

- [ ] **14. Resolve the eligibility contradiction.** *(content · 20 min · Fact-Check)*
      Eligibility says *"You must be a UAE resident"*, but the hero carries a **"Traveling to the UAE"** toggle offering an inbound-visitor path. Split eligibility by inbound vs outbound, or scope the statement to outbound plans only.

- [ ] **15. Collapse near-duplicate "Best…" H2s.** *(content · 20 min · SEO)*
      *"Best Travel Insurance Dubai Providers"*, *"Best Travel Insurance for Dubai"* and *"How to Find the Best Travel Insurance Dubai?"* are three headings doing one job. Consolidate.

- [ ] **16. Refresh `dateModified` and add a visible date.** *(dev + content · 15 min · GEO)*
      `dateModified: 2026-03-30` — 4.5 months stale, no visible date. Update after the content work above, not before.

- [ ] **17. Fix the title and meta length.** *(content · 15 min · SEO)*
      Title is 60 chars (at the truncation limit) and stacks two openers: *"Buy Best Travel Insurance Online in Dubai Starting @ AED 22\*"*. Meta is ~163 chars (over) and repeats "Buy" three times counting the title. Tighten both, keeping Dubai targeting intact.

- [ ] **18. Add schema foundation nodes.** *(dev · part of the cluster-wide schema ticket · SEO)*
      Missing for a Destination/City page: `Service` with `areaServed` → Dubai (City) · `FAQPage` (task 8) · `InsuranceAgency` canonical node · `WebSite` node. Plus no `@id` on any node and `WebPage` missing `isPartOf` / `breadcrumb` / `primaryImageOfPage`. Bugs T2, T3, T11 present.
      `TouristDestination` / `TouristTrip` may be added as entity markup only — **never promise a rich result from either.**

---

## 🟢 Quick wins

- [ ] **19.** Delete the duplicate exclusion bullet — *"Bodily injuries or illnesses caused under the influence of alcohol"* appears **twice** in the exclusions list. *(content · 5 min)*
- [ ] **20.** Capitalise the paragraph starting *"in case of flight cancellations or missed departures…"*. *(content · 2 min)*
- [ ] **21.** Delete the article-roadmap opener: *"Keep reading to know the benefits of buying travel insurance Dubai, followed by the included and excluded covers, and steps to file a claim for the same."* Open with what a Dubai searcher wants — cost and cover. *(content · 10 min)*
- [ ] **22.** Rewrite *"Several covers are included in travel insurance Dubai that can be viewed below."* — a pointer where an answer belongs, so nothing here is extractable as a citation. Replace with the named benefits and limits. *(content · 15 min)*
- [ ] **23.** Cut or limit the hijack-cover block: *"While plane hijacking is an extremely rare event, your insurance for Dubai travel compensates for loss or damage…"* — the least useful benefit on the page, given as reassurance with no limit. Space is better spent on the excess the page never mentions. *(content · 5 min)*
- [ ] **24.** Fix image alt: 5 logos with `alt="Salama Insurance"` (cluster ticket) + 2 images with no `alt`. *(dev · 20 min)*
- [ ] **25.** Add 5 outbound links — all verified live in `assets/policybazaar-urls.txt`, none currently linked: *(content · 25 min)*
      over-65/70/75 (task 1) · `/travel-insurance/articles/does-travel-insurance-cover-pregnancy/` (task 4) · `/travel-insurance/articles/travel-insurance-claim-reimbursement/` (claims section) · `/travel-insurance/articles/baggage-travel-insurance/` (baggage section) · `/travel-insurance/uae/` (eligibility section — reinforces the intended lane split)
- [ ] **26.** Collapse the 49-link destination block behind the existing "Expand" control. *(dev · 30 min)*

---

## 🔗 Cluster-wide — fix once at template level, not three times

| # | Defect | Scope | Ticket |
|---|---|---|---|
| C1 | 5 logos `alt="Salama Insurance"` per plan-quote card | 4+ travel pages, 20+ images, zero correct | `docs/jira-alt-text-insurer-logos-travel-plan-cards.md` |
| C2 | `"disclaimer": null` | All 3 pages | — |
| C3 | Bugs T2 / T3 / T11 + no `@id` on any node | All 3 pages | — |
| C4 | `"excess"` / `"sub-limit"` / `"policy wording"` = 0 occurrences | All 3 pages | — |
| C5 | Stale Covid *"Mandatory quarantine… 7 to 14 days"* | This page + `/uae/` | — |
| C6 | No `author` / `reviewedBy` | This page + `/uae/`. **The hub is fixed — use it as the pattern.** | — |

---

## ✅ Acceptance criteria

- [ ] `grep -c "No Age Discrimination\|complete protection against any loss\|offer worldwide coverage"` returns 0.
- [ ] The exclusions list distinguishes routine pregnancy from unforeseen complications, and agrees with the hub's FAQ Q10.
- [ ] No heading on the page promises content that isn't there (provider table populated or heading removed).
- [ ] `FAQPage` markup present, covering the on-page `Faq's` pairs.
- [ ] Visible byline (author + reviewer + last-updated) present, and `author`/`reviewedBy` in the JSON-LD.
- [ ] "excess" appears at least once; a disclaimer is present near the top.
- [ ] First H2 is Dubai-scoped, and no H2 on the page contains "UAE" as its geo.
- [ ] No image lacks an `alt` attribute.
- [ ] At the next cannibalization check: impressions on "travel insurance", "travel insurance online" and "travel insurance uae" for this URL trend **down**, while Dubai-query clicks hold or rise.
- [ ] Lead conversion moves up from 12.2%, and AED/lead up from 17.8 toward the cluster's 27–28.

**Re-audit trigger:** `/content-audit https://www.policybazaar.ae/travel-insurance/travel-insurance-dubai/` after shipping, then `/uae-insurance cannibalization travel` 4–6 weeks later.

**Unresolved:** rank positions in the lane tables are 12-month GSC averages (2025-08-11 → 2026-08-08), not current live positions. Re-check before acting on anything position-sensitive.
