# Month-1 KRAs & KPIs — UAE basis, split by Number driven and Task driven

**Domain:** policybazaar.ae · **Month 1:** 5 August – 1 September 2026
**Search Console property:** `https://www.policybazaar.ae/` (URL-prefix, confirmed authoritative 31 Aug 2026 — the `sc-domain:` property is missing 95 days of historical data) · **Country filter:** United Arab Emirates
**Source:** derived from `seo-aio-kra-kpi-uae-filtered-2026-08-04.md`, with Segment A targets as revised on 5 Aug

> **Number driven** covers performance outcomes: position, clicks, CTR, ranking counts, AI Overview citation, leads.
> **Task driven** covers work the team ships: sitemap and indexation fixes, hub recovery, schema, content depth, redirect and tracking decisions.

> Clicks and CTR here are UAE-filtered and therefore understated by roughly two to three times, because a country filter moves Search Console onto its anonymised dataset. Use them for UAE month-on-month tracking only, never against the unfiltered plan. Positions are unaffected and comparable.

> **This is the Month-1 close-out report.** Month-1 (5 Aug – 1 Sep 2026) has fully ended, and every Number-driven KPI except two GSC query-dimension figures now reflects genuine final or near-final data: Semrush ranking figures are from a fresh export dated **7 Sep** (period 1–7 Sep, with competitor columns); CRM lead figures are the **exact final total for the complete 28-day window** (`Leads 07-09-26.csv`, daily data through 6 Sep) — no more normalization or projection, these are the real numbers; the AI Overview re-test is from **7 Sep** (`AIO_business-insurance_2026-09-07.xlsx`, `AIO_group-health-insurance_2026-09-07.xlsx`, `AIO_home-insurance_2026-09-07.xlsx`), same 15 queries verified against the Appendix. GSC position/clicks/CTR/impression figures are a page-dimension pull, 28d to 4 Sep (from the previous cycle, not re-pulled this round). **Not refreshed this cycle:** the two query-dimension-only figures (Home's "home insurance" cannibalization position, and all Priority keyword clicks/coverage rows) still read from the 28 Aug pull.
>
> **⚠ The final Semrush read shows real give-back, not just noise.** After the unexplained 24→30 Aug jump (flagged twice, confirmed holding as of 31 Aug), the 7 Sep read shows a genuine pullback across every segment: rollup top-10 63→57, top-3 23→21; Business top-10 30→26, top-3 11→8; Group Health top-10 17→15; Home top-3 8→7. Whatever drove the original jump — still unconfirmed — does not appear to have been fully durable. Competitors receded too, not just PB: adnic dropped in Home (19→11 top-3) and Group Health (21→16 top-10); giggulf dropped in Home (22→18 top-3). This looks like broad volatility across the whole tracked set rather than something specific to PB.
>
> **⚠ CRM final totals missed target across the board, and Business fell below baseline.** Business Insurance: 115 leads for the full 28-day window, **down 13.5% versus the 133 baseline** — not just short of the +9% target, actually worse than where the segment started. Home: 40, up 11.1% vs baseline but still short of the +44% target. Group Health: 25, up 56.3% vs baseline, missing its 26-lead target by just 1 — closest of the three. Rollup: 180 vs a 185 baseline and 223 target, down 2.7%.
>
> **⚠ AI Overview citations are now at zero.** The 7 Sep re-test (same 15-query set as the Appendix, confirmed by comparing every prompt) shows PB cited on **0 of 15** queries — down from 1/15 (27 Aug) and 6/15 (baseline). AIO presence itself also slipped slightly, 13/15 vs 14/15 baseline, because `group medical insurance dubai` stopped returning an AI Overview entirely. This is a full progression across three consecutive tests (40% → 7% → 0%), not a one-off dip — see the Appendix for the complete breakdown.
>
> **⚠ Correction — the sitemap claim was wrong (carried from the 7 Sep cycle).** An earlier cycle recorded "Impression-earning URLs missing from sitemap: 0" based on Aakash's confirmation, with only the hub URL independently spot-checked. A full cross-check against all 40 sitemap files found the real count is **4, not 0** — see the Task-driven rows below.
>
> **Correction — the "broken listicle redirect" finding was wrong.** An earlier test used the wrong URL (a guessed root-level path) and reported a 404 that didn't exist. The correct documented URL, live-checked, resolves properly (301 → `/group-health-insurance-hic/`, HTTP 200). **All four intent-mismatch redirects are now identified and live-checked** (found in the original raw audit, `seo-aio-kra-kpi-2026-08-04.md`): 2 of 4 are already validated as correct by the original audit, 2 of 4 work technically but still need Aakash's decision on whether to reverse them — see the Task-driven rows below for specifics. Every KPI still marked `— (needs ...)` has not been verified in any cycle.
>
> **Lead-volume normalization:** all four lead-volume figures now lead with a value normalized to a full 28-day month (`actual ÷ days elapsed × 28`), not the raw to-date count, since that's what's directly comparable to the Target column. This is a straight-line projection assuming the run rate holds for the rest of the month — it is not the actual final count, which won't exist until after 1 Sep. Semrush ranking counts are **not** normalized this way, because they're a point-in-time snapshot (a keyword is either in the top 10 today or it isn't) rather than a cumulative daily total — there's no meaningful "days elapsed" fraction to apply to them.

---

## Segment A — Business / Commercial

### Part 1 — Number driven

| KRA | KPI | Current Baseline | 1-Month Target | Current Status (verified) | Rationale tied to baseline |
|---|---|---|---|---|---|
| Organic visibility | UAE average position | 28.9 | **15.0** | **28.5** ↓0.4 vs baseline (improved), ↓0.2 vs 28 Aug read (GSC, UAE, 28d to 4 Sep) | Benchmarked to pre-break performance, not the trailing year. The segment held 8.8 to 10.8 across Aug–Oct 2025 before the November break. Trailing-year average is 19.4, so this target goes past it. Best reading in the last nine months is 20.8, which makes this the highest-risk target in the plan |
| Click growth | UAE clicks, 28d | 64 | **100, +56%** | **126** ↑62, unchanged vs 28 Aug read, still past target (GSC, UAE, 28d to 4 Sep) | Trailing-year UAE run rate is 114 and the segment reached 148 to 159 per 28 days pre-break. Recovers 72% of the −44% shortfall |
| CTR improvement | UAE CTR, 28d | 0.22% | 0.33% | **0.38%** ↑0.16pp, still past target (GSC, UAE, 28d to 4 Sep) | 9 queries hold 9,552 UAE impressions at one click or fewer. Trailing-year UAE CTR is 0.37%. Consistent with the 100-click target only if segment impressions grow about 5% to ~30,300 |
| Page-2 conversion | Semrush keywords in top 10 | 22 / 52 | **35 / 52** | **26 / 52** ↑4 vs baseline, ↓4 vs 31 Aug's 30 (Semrush, 7 Sep, period 1–7 Sep — post-Month-1 close) | Requires converting 13 of the 14 keywords sitting at 11–20. Segment top-20 is 36 / 52, so on delivery top-10 would almost equal top-20 and further gains would have to come from outside the current top 20 |
| Head-term expansion | Semrush keywords in top 3 | 11 / 52 | 15 / 52 | **8 / 52** ↓3 vs baseline, ↓3 vs 31 Aug's 11 (Semrush, 7 Sep). adnic 8 (down from 10), giggulf 11, aig 11 (up from 9) | The next four must come from adnic at 8 and aig at 6 |
| AI Overview citation | PB cited on sampled queries | 2 / 5 | 4 / 5 | **0 / 5** ↓2 vs baseline, unchanged from 27 Aug (fresh AIO re-test, 7 Sep, `AIO_business-insurance_2026-09-07.xlsx`) — AIO now fires on only 4 of 5 (unchanged), PB still cited on none | AIO fires on 4 of 5 but PB ranks top-12 on only 2, so two wins must come from queries where PB does not yet rank |
| Lead volume | CRM Business Insurance leads per month | 133 | **145, +9.0%** | **115** — final, exact total for the complete 5 Aug–1 Sep window (all 28 days, `Leads 07-09-26.csv`), **down 13.5% vs baseline**, missed target | Trailing-12 average 137, best month 171. Organic is 12.4% of UAE segment sessions, so most must come from conversion-rate work |

### Part 2 — Task driven

| KRA | KPI | Current Baseline | 1-Month Target | Current Status (verified) | Rationale tied to baseline |
|---|---|---|---|---|---|
| Fix hub indexation | `/business-insurance/` in sitemap | absent | Present and indexed | **Present** — live-verified 31 Aug: the hub URL appears in `sitemap-static.xml` (also confirmed indexed and returning HTTP 200) | Live 200 self-canonical hub earning 2,068 UAE impressions at position 21.3, missing from all 38 child sitemaps |
| Recover the hub | `/business-insurance/` UAE position | 21.3 | ≤18.5 | **22.7** still short of target, worse than the 21.9 (28 Aug) and 20.2 (25 Aug) reads — trending the wrong way three cycles running (GSC, UAE, 28d to 4 Sep; 1,822 impr / 8 clicks) | 2,068 UAE impressions and 1 click in 28 days |
| Indexation health | Impression-earning URLs missing from sitemap | 13 | **0** | **4**, not 0 — Aakash's "present in sitemap" answer covered the hub itself (correctly), but I independently cross-referenced every UAE impression-earning page against the full 40-file sitemap set (excluding `#`-anchor fragments and `/buy-insurance/` funnel pages, which are intentionally robots.txt-disallowed) and found 4 genuine gaps: `/public-liability/articles/public-liability-insurance-for-day-in-uae/` (93 impr), `/trade-credit-insurance/articles/` (77 impr), `/fire-and-allied-perils-insurance/articles/` (57 impr), `/commercial-motor/articles/` (7 impr) | Verified set difference, each URL redirect-checked |
| Schema completeness | Hub schema gaps closed | FAQPage and modified date both missing | Both live and validated | **Both live and validated** — live-verified 31 Aug via rendered JSON-LD: FAQPage present, `dateModified` present, and Product/Offer markup also present (bonus, not required for this KPI) | The only one of the three hubs without either |
| Content depth | Hub rendered word count | 1,073 | ≥3,500 | **1,800** ↑727 vs baseline — live-verified 31 Aug (JS-rendered `innerText`, script/style/nav/header/footer stripped) — still well short of target | Sibling hubs run 3,659 and 3,768 words |

---

## Segment B — Home Insurance

### Part 1 — Number driven

| KRA | KPI | Current Baseline | 1-Month Target | Current Status (verified) | Rationale tied to baseline |
|---|---|---|---|---|---|
| Organic visibility | UAE average position | 31.0 | 24.5 | **32.4** ↑1.4 vs baseline (worse), ↑1.1 vs the 28 Aug read (GSC, UAE, 28d to 4 Sep) | Trailing-year UAE average is 19.4 and the segment held 11.2 to 11.6 before the November break. Closes 56% of the 11.6-place gap |
| Click growth | UAE clicks, 28d | 23 | 38, +65% | **42** ↑19, still past target, down 4 from the 28 Aug read (GSC, UAE, 28d to 4 Sep) | Trailing-year UAE run rate is 50. The segment reached 212 in February and 54 to 65 in Aug–Sep. Recovers 56% of the −54% shortfall |
| CTR improvement | UAE CTR, 28d | 0.15% | 0.24% | **0.27%** ↑0.12pp, still past target, down from the 28 Aug read's 0.30% (GSC, UAE, 28d to 4 Sep) | 9 queries hold 13,935 UAE impressions at one click or fewer, led by `renters insurance` at position 8 on 3,124. Trailing-year UAE CTR is 0.31% |
| Page-2 conversion | Semrush keywords in top 10 | 14 / 40 | 22 / 40 | **16 / 40** ↑2 vs baseline, flat vs 31 Aug (Semrush, 7 Sep) | 21 of 40 sit at 11–20, the largest quick-win pool |
| Close the competitor gap | Semrush keywords in top 3 | 4 / 40 | 8 / 40 | **7 / 40** ↑3 vs baseline, ↓1 vs 31 Aug's 8 — dipped just below target (Semrush, 7 Sep). giggulf 18 (down from 22), adnic 11 (down from 19) — both competitors also receded | giggulf 21 and adnic 19 against PB's 4 |
| AI Overview citation | PB cited on sampled queries | 3 / 5 | 5 / 5 | **0 / 5** ↓3 vs baseline, ↓1 vs 27 Aug's 1 (fresh AIO re-test, 7 Sep, `AIO_home-insurance_2026-09-07.xlsx`) — lost the `renters insurance dubai` citation it had gained; AIO still fires on all 5 | AIO fires on all 5 and PB already ranks top-12 on all 5, so the misses are a content-format gap |
| Priority keyword clicks | Combined 28d UAE clicks, keywords 7 to 10 | 1 | 12 | **6** ↑5 vs baseline, still short of target (GSC, UAE, 28d to 28 Aug). Keyword list from Aakash: `home insurance uae` (1 click, rank 19), `home insurance` (3 clicks, rank 16), `home insurance dubai` (2 clicks, rank 20), `best home insurance in uae` (0 clicks, rank 2) | 1,459 UAE impressions converting at 0.07%. `home insurance dubai` holds 598 at position 24.5 |
| Priority keyword rankings | Keywords 7, 8 and 9 in UAE top 10 | 0 / 3 | 2 / 3 | **0 / 3**, unchanged (Semrush position tracker, latest ~27 Aug). `home insurance uae` rank 19, `home insurance` rank 16, `home insurance dubai` rank 20 — none in top 10 | All three averaged 16.6 to 20.3 over the trailing year and now sit at 20.8 to 25.6 |
| Lead volume | CRM Home Insurance leads per month | 36 | 52, +44% | **40** — final, exact total for the complete 5 Aug–1 Sep window (all 28 days), **up 11.1% vs baseline**, still missed target | Trailing-12 average 69, best month 113. Organic is 43.3% of UAE segment sessions, the highest of the three, so ranking recovery reaches leads fastest here |

### Part 2 — Task driven

| KRA | KPI | Current Baseline | 1-Month Target | Current Status (verified) | Rationale tied to baseline |
|---|---|---|---|---|---|
| Resolve hub cannibalization | `/home-insurance/` UAE position for "home insurance" | 68.0 | ≤35 | **71.5** (28 Aug read, ↑3.5 vs baseline) — **not refreshed this cycle**, needs a query-dimension GSC pull, which wasn't run this round | The hub ranks 68.0 in the UAE for its own head term while the child article carries all four Home priority keywords. Largest content problem in this view |
| Recover the hub overall | `/home-insurance/` UAE position, all queries | 50.3 | ≤32 | **42.2** ↑8.1 vs baseline (improved), also better than the 46.2 (28 Aug) and 50.4 (25 Aug) reads — still short of target (GSC, UAE, 28d to 4 Sep; 2,744 impr / 14 clicks) | 2,270 UAE impressions and zero clicks in 28 days |
| Restore the dead section index | `/home-insurance/news-and-update/` | 404 | 200 listing page | **200** — live-verified 31 Aug (direct request, no redirect), matches Aakash's confirmation | Dead index above six live children |
| Indexation health | URLs missing from sitemap | 1 | 0 | — *(needs a live sitemap check — not covered by this cycle's checks)* | `/home-insurance/articles/` |
| Schema completeness | Product/Offer schema on hub | missing | Live | **Still missing** — live-verified 31 Aug via rendered JSON-LD: FAQPage and `dateModified` present, but no Product or Offer markup found. This contradicts Aakash's "Added" note for all three hubs; flagging rather than overwriting | Hub carries FAQPage and Rating but no product markup |

---

## Segment C — Group Health

### Part 1 — Number driven

| KRA | KPI | Current Baseline | 1-Month Target | Current Status (verified) | Rationale tied to baseline |
|---|---|---|---|---|---|
| Organic visibility | UAE average position | 41.6 | 35.0 | **40.4** ↓1.2 vs baseline (improved), roughly flat vs the 28 Aug read's 40.7 (GSC, UAE, 28d to 4 Sep) | Trailing-year UAE average is 30.0 and the segment held 16.9 to 19.4 before the November break. Closes 57% of the 11.6-place gap, joint-worst of the three, and 32 of 33 Semrush keywords with genuine movement went down |
| Click growth | UAE clicks, 28d | 15 | 18, +20% | **28** ↑13, still past target, up 2 from the 28 Aug read (GSC, UAE, 28d to 4 Sep) | Trailing-year UAE run rate is 19, so the volume shortfall is only 21%, the smallest of the three. This segment is a position problem, not a volume problem |
| CTR improvement | UAE CTR, 28d | 0.07% | 0.09% | **0.12%** ↑0.05pp, still past target (GSC, UAE, 28d to 4 Sep) | 5 queries hold 9,556 UAE impressions at one click or fewer. Trailing-year UAE CTR is 0.11% |
| Page-2 conversion | Semrush keywords in top 10 | 8 / 33 | 14 / 33 | **15 / 33** ↑7 vs baseline, ↓2 vs 31 Aug's 17 (Semrush, 7 Sep) — still past target | 22 of 33 sit at 11–20 per Semrush, but UAE Search Console places the segment at 41.6. Contingent on the reconciliation |
| Close the competitor gap | Semrush keywords in top 10 | PB 8 vs adnic 24 | PB 14 | **PB 15** — still past target. adnic 16 (down further from 21), giggulf 14 (flat) | Same 33-keyword set: adnic 24, giggulf 21, PB 8 |
| AI Overview citation | PB cited on sampled queries | 1 / 5 | 3 / 5 | **0 / 5** ↓1 vs baseline, unchanged from 27 Aug (fresh AIO re-test, 7 Sep, `AIO_group-health-insurance_2026-09-07.xlsx`) — AIO itself now only fires on 4 of 5 (`group medical insurance dubai` returned no answer at all) | AIO fires on all 5 but PB ranks top-12 on none, so citation upside is capped until rankings move. Highest-risk KPI |
| Priority keyword clicks | Combined 28d UAE clicks, keywords 1 to 6 | 3 | 18 | **8** ↑5 vs baseline, still short of target (GSC, UAE, 28d to 28 Aug). Keyword list from Aakash: `medical insurance for company` (0 clicks, rank 20), `group medical insurance` (1 click, rank 21), `group health insurance uae` (0 clicks, rank 17), `group medical coverage` (0 clicks, rank 16), `group health coverage` (3 clicks, rank 16), `group health insurance` (4 clicks, rank 13) | 1,427 UAE impressions at 0.21%. `group medical insurance` at 491 impressions and `group health insurance` at 441 carry it |
| Priority keyword rankings | Keywords 1 to 6 in UAE top 20 | 1 / 6 | 5 / 6 | **5 / 6** — **meets target** (Semrush position tracker, latest ~27 Aug). Only `group medical insurance` (rank 21) misses top 20; the other five (ranks 13–20) all qualify | Five of six averaged 8.6 to 19.5 over the trailing year and all now sit at 20.9 to 26.8 |
| Lead volume | CRM Group Health leads per month | 16 | 26, +63% | **25** — final, exact total for the complete 5 Aug–1 Sep window (all 28 days), **up 56.3% vs baseline**, missed target by just 1 | Trailing-12 average 32, best month 45. Against −63% year on year this is recovery |

### Part 2 — Task driven

| KRA | KPI | Current Baseline | 1-Month Target | Current Status (verified) | Rationale tied to baseline |
|---|---|---|---|---|---|
| Resolve the listicle redirect | Decision on `best-group-health-insurance-companies-in-uae` | 301'd to hub | Decision made and actioned | **Working correctly, not broken** (corrected 7 Sep — 31 Aug's "404" finding tested the wrong URL). Live-checked 7 Sep against the audit's actual documented source, `/group-health-insurance/articles/best-group-health-insurance-companies-in-uae/`: single 301 → `/group-health-insurance-hic/`, HTTP 200. Still needs Aakash's decision though — the original audit called this redirect "**likely wrong**" (comparison intent sent into a quote form, position 47.8 consistent with Google discounting the mismatch), so the open question isn't "is it broken" but "should it be reversed" | 4,511 impressions across 8 URL variants, redirected from comparison intent into a quote form |
| Recover the hub | `/group-health-insurance-hic/` UAE position | 38.4 | ≤31 | **38.2** roughly flat vs baseline and vs the 28 Aug read's 38.1, still short of target (GSC, UAE, 28d to 4 Sep; 5,894 impr / 18 clicks) | 6,948 UAE impressions and 5 clicks in 28 days. All six Group Health priority keywords already resolve here, so hub position is the whole story for this segment |
| Indexation health | URLs missing from sitemap | 1 | 0 | — *(needs a live sitemap check — not covered by this cycle's checks)* | `/group-health-insurance/articles/` |
| Schema completeness | Product/Offer schema on hub | missing | Live | **Still missing** — live-verified 31 Aug via rendered JSON-LD: FAQPage and `dateModified` present, but no Product or Offer markup found. Same contradiction as the Home hub — flagging rather than overwriting | Hub carries FAQPage but no product markup |
| Close a tracking gap | `medical insurance for company` in Semrush | absent | Tracked | **Deprioritized** — Aakash confirmed this is not needed, dropping this KPI rather than pursuing it | 450 search volume, UAE position 12.8, not in the campaign |

---

## Month-1 rolled-up summary, UAE basis

### Part 1 — Number driven

| KRA | KPI | Current Baseline | 1-Month Target | Current Status (verified) | Rationale tied to baseline |
|---|---|---|---|---|---|
| Organic visibility | Blended UAE position, impression-weighted | 33.4 | **23.5** | **33.1** flat vs baseline, flat vs the 28 Aug read (GSC, UAE, 28d to 4 Sep): A 28.5 + B 32.4 + C 40.4 | Impression-weighted from A 15.0, B 24.5, C 35.0. Trailing-year UAE blended average is 22.2, so this closes 88% of the 11.2-place gap. Segment A's 15.0 is what pulls it this far |
| Click growth | UAE clicks, 3 segments, 28d | 102 | **156, +53%** | **196** ↑94, still past target, down 2 from the 28 Aug read (GSC, UAE, 28d to 4 Sep): A 126 + B 42 + C 28 | A 100, B 38, C 18. Trailing-year UAE run rate is 183, so this recovers 67% of the shortfall |
| Impression growth | UAE impressions, 28d | 64,318 | ≥68,000 | **70,819** ↑6,501, past target, up slightly from the 28 Aug read's 69,762 (GSC, UAE, 28d to 4 Sep) — page-set may differ slightly from baseline's classification, see methodology note below | Impressions are already at the trailing-year run rate of 64,416, so this target exceeds it and must come from the hub sitemap fix and the dead-page restoration, not from recovery |
| CTR improvement | UAE CTR, 3 segments, 28d | 0.16% | 0.23% | **0.28%** ↑0.12pp, still past target, unchanged (GSC, UAE, 28d to 4 Sep) | 23 queries hold 33,043 UAE impressions at one click or fewer. Trailing-year UAE CTR is 0.28%. 156 clicks at 0.23% requires the impression target to land; on today's impression base the same clicks would read 0.24% |
| Priority keyword clicks | Combined 28d UAE clicks, 10 keywords | 4 | 30 | **14** ↑10 vs baseline, still short of target (GSC, UAE, 28d to 28 Aug): B 6 + C 8. Full keyword list now confirmed by Aakash — see Segment B/C rows above | B contributes 12 and C contributes 18. Nine of ten averaged better than position 21 over the trailing year |
| Priority keyword coverage | Keywords with at least 1 click | 2 / 10 | 8 / 10 | **6 / 10** ↑4 vs baseline, still short of target. Only `medical insurance for company`, `group health insurance uae`, `group medical coverage`, and `best home insurance in uae` show zero clicks | Eight of ten currently produce nothing |
| Priority keyword rankings | Keywords in UAE top 10 | 0 / 10 | 4 / 10 | **1 / 10** ↑1 vs baseline, still short of target (Semrush position tracker, latest ~27 Aug). Only `best home insurance in uae` (rank 2) is in the top 10 | Same basis |
| Priority keyword rankings | Keywords in UAE top 20 | 1 / 10 | 7 / 10 | **9 / 10** — **past target** (Semrush position tracker, latest ~27 Aug). Only `group medical insurance` (rank 21) misses top 20 | Same basis |
| Ranking distribution | Semrush keywords in top 10, of 125 | 44 | **71** | **57** ↑13 vs baseline, ↓6 vs 31 Aug's 63 (Semrush, 7 Sep, period 1–7 Sep, post-Month-1 close): A 26 + B 16 + C 15 | A 35, B 22, C 14. 57 of 125 sit at 11–20, so this converts 27 of those 57 |
| Ranking distribution | Semrush keywords in top 3, of 125 | 18 | 29 | **21** ↑3 vs baseline, ↓2 vs 31 Aug's 23 (Semrush, 7 Sep): A 8 + B 7 + C 6 | Widest competitor gap is Segment B |
| AI Overview citation | PB cited across 15 sampled queries | 6 / 15, 40% | 12 / 15, 80% | **0 / 15, 0%** ↓6 vs baseline, ↓1 vs 27 Aug's 1 (fresh AIO re-test, 7 Sep, all three `AIO_*_2026-09-07.xlsx` files): A 0 + B 0 + C 0 — PB fully wiped from citations across the whole tracked set. AIO presence itself also dipped slightly, 13/15 vs 14/15 baseline, since `group medical insurance dubai` stopped returning an AI Overview at all. See Appendix for the full breakdown | AIO fires on 93%. PB ranks top-12 on 7 of 15 |
| Lead volume | CRM leads per month, 3 products | 185 | **223, +20.5%** | **180** — final, exact total for the complete 5 Aug–1 Sep window (all 28 days, `Leads 07-09-26.csv`): A 115 + B 40 + C 25, **down 2.7% vs baseline**, missed target | A 145, B 52, C 26. Trailing-12 average 238, so the target stays inside observed capability |

### Part 2 — Task driven

| KRA | KPI | Current Baseline | 1-Month Target | Current Status (verified) | Rationale tied to baseline |
|---|---|---|---|---|---|
| Hub recovery | Three hubs at or better than target UAE position | 0 / 3 | 3 / 3 | **0 / 3**, unchanged (GSC, UAE, 28d to 4 Sep): Business 22.7 (worse, trending wrong way 3 cycles running), Home 42.2 (best reading yet, all-queries basis), Group Health 38.2 (flat) — none has crossed its target | Business 21.3, Home 50.3, Group Health 38.4. Targets ≤18.5, ≤32, ≤31 |
| Home head-term recovery | `/home-insurance/` UAE position for "home insurance" | 68.0 | ≤35 | **71.5** (28 Aug read, ↑3.5 vs baseline) — **not refreshed this cycle**, needs a query-dimension GSC pull | The article has taken all four Home priority keywords in this market |
| Indexation and crawl health | Impression-earning URLs missing from sitemap | 15 | 0 | **4**, not 0 — same finding as Segment A above (this rollup figure and the Segment A figure describe the same underlying gap; all 4 remaining genuine gaps happen to sit in the Business path prefixes). Verified by cross-referencing all UAE impression-earning pages against the full 40-file sitemap set, excluding `#`-fragments and the intentionally-disallowed `/buy-insurance/` funnel paths | Includes the `/business-insurance/` hub |
| Indexation and crawl health | Dead URLs still earning impressions | 1 | 0 | **0** — live-verified 31 Aug, `/home-insurance/news-and-update/` now returns 200 | `/home-insurance/news-and-update/` |
| Redirect quality | Intent-mismatch redirects resolved | 0 / 4 | 4 / 4 | **2 / 4 already correct, 2 / 4 need a decision** — full list recovered from the original raw audit (`seo-aio-kra-kpi-2026-08-04.md`), all four live-checked 7 Sep and none are technically broken: (1) `.../best-group-health-insurance-companies-in-uae/` → `/group-health-insurance-hic/`, 4,511 impr, pos 47.8 — audit says **likely wrong**, comparison intent into a quote form, still needs Aakash's call; (2) `/group-life-insurance/articles/group-life-insurance-policy-for-employees/` → `/group-life-insurance/`, 3,056 impr, pos 9.7 — audit says **review urgently**, redirecting away a page-1-adjacent ranker, still needs a call; (3) `/fire-and-allied-perils-insurance/articles/political-violence-insurance/` → `/business-insurance/political-violence-insurance/`, 714 impr — audit already validated this as correct; (4) `/home-insurance/articles/compare-home-insurance/` → `/home-insurance/`, 20 impr — audit already validated this as correct. Treating (3) and (4) as resolved leaves 2 of 4 genuinely open, both awaiting a keep-or-reverse decision, not a technical fix | 8,301 impressions sit behind these four decisions |
| Schema completeness | Hubs with a complete schema set | 0 / 3 | 3 / 3 | **1 / 3** ↑1 vs baseline — Business hub confirmed complete (FAQPage, modified date, Product/Offer all live); Home and Group Health still missing Product/Offer, contradicting the "Added" note — see flag at top of doc | Business missing FAQPage; Home and Group Health missing Product or Offer |
| Content freshness and E-E-A-T | Hubs with a modified date | 2 / 3 | 3 / 3 | **3 / 3** ↑1 vs baseline — `/business-insurance/` now has a modified date, live-verified 31 Aug | `/business-insurance/` has none |
| Measurement integrity | Reporting property corrected | domain property in use | URL-prefix only | **URL-prefix now in use** — all GSC pulls this cycle ran against `https://www.policybazaar.ae/`, confirmed identical to the domain property for the current window (the 95-day gap was historical, not live) | The domain property is missing 95 days of its own data |
| Measurement integrity | Ranking breaks root-caused | 0 / 2 | 2 / 2 | **0 / 2, but a lead on each:** the **May 2026 break** window (10 May–6 Jun) almost exactly matches Google's confirmed **May 2026 core update** (21 May–2 Jun) — a strong candidate cause. The **Nov 2025 break** window (23 Nov–20 Dec) only overlaps the tail of the confirmed **Dec 2025 core update** (11–29 Dec), which doesn't explain the earlier weeks — weak candidate at best. Neither is a confirmed diagnosis; both still need internal deploy/change-log review | November 2025 and May 2026, neither site-wide, neither explained |

---

## Rollup recomputation

The rolled-up figures are the sum, or impression-weighted average, of the three segments. Segment A's revised targets moved four of them.

| Rollup KPI | Previous | Revised | Derivation |
|---|---|---|---|
| Click growth | 151, +48% | **156, +53%** | A 100 + B 38 + C 18 |
| Semrush keywords in top 10, of 125 | 64 | **71** | A 35 + B 22 + C 14 |
| Lead volume | 233, +26% | **223, +20.5%** | A 145 + B 52 + C 26 |
| Blended UAE position | 27.5 | **23.5** | Impression-weighted: (15.0 × 28,748) + (24.5 × 15,519) + (35.0 × 20,051), divided by 64,318 |

Three points on the revised set:

- **The blended position target is now carried by one segment.** Segment A is 45% of the three segments' impressions, so its 15.0 pulls the rollup from 27.5 to 23.5. That closes 88% of the gap to the trailing-year blended average of 22.2, against 53% before. If Segment A misses, the rollup misses regardless of B and C.
- **Segment A clicks of 100 at a CTR of 0.33% require impressions to grow.** On today's 28,748 impressions, 100 clicks reads 0.35%. The 0.33% target holds if segment impressions reach about 30,300, roughly 5% growth, which is consistent with the rollup impression target of ≥68,000.
- **Semrush top-10 at 71 of 125 converts 27 of the 57 keywords currently at 11–20**, just under half, and Segment A carries 13 of those 27 on its own.

---

## Appendix: AI Overview sample

Fifteen queries on google.ae, `gl=ae&hl=en`, five per segment. This is the evidence base for the three AI Overview citation KPIs. Tested three times now — baseline, 27 Aug (`AIO_business_home_insurance_2026-08-27.xlsx`), and 7 Sep (`AIO_business-insurance_2026-09-07.xlsx`, `AIO_group-health-insurance_2026-09-07.xlsx`, `AIO_home-insurance_2026-09-07.xlsx`) — same 15 queries confirmed in all three runs. Single runs, not issued from a UAE IP, so treat as directional for the AE market.

| # | Segment | Query | AIO present (baseline → 27 Aug → 7 Sep) | PB cited (baseline → 27 Aug → 7 Sep) | PB organic (baseline, not re-verified) |
|---:|---|---|:---:|:---:|:---:|
| 1 | A Business | business insurance dubai | no → no → no | — | #3 |
| 2 | A Business | workmen compensation insurance uae | yes → yes → yes | no → no → no | not in top 12 |
| 3 | A Business | professional indemnity insurance dubai | yes → yes → yes | no → no → no | not in top 12 |
| 4 | A Business | public liability insurance uae | yes → yes → yes | **yes → no → no** | not in top 12 |
| 5 | A Business | contractors all risk insurance uae | yes → yes → yes | **yes → no → no** | #10 |
| 6 | B Home | home insurance dubai | yes → yes → yes | **yes → no → no** | #8 |
| 7 | B Home | home contents insurance dubai | yes → yes → yes | **yes → no → no** | #7 |
| 8 | B Home | best home insurance uae | yes → yes → yes | **yes → no → no** | #4 |
| 9 | B Home | building insurance dubai | yes → yes → yes | no → no → no | #9 |
| 10 | B Home | renters insurance dubai | yes → yes → yes | **no → yes → no** (gained, then lost again) | #3 |
| 11 | C Group Health | group health insurance dubai | yes → yes → yes | no → no → no | not in top 12 |
| 12 | C Group Health | corporate health insurance uae | yes → yes → yes | no → no → no | not in top 12 |
| 13 | C Group Health | employee medical insurance uae | yes → yes → yes | no → no → no | not in top 12 |
| 14 | C Group Health | group medical insurance dubai | yes → yes → **no** (AIO stopped firing entirely) | **yes → no → no** | not in top 12 |
| 15 | C Group Health | business health insurance uae | yes → yes → yes | no → no → no | not in top 12 |

**Baseline totals:** AIO present 14 / 15 (93%) · PB cited 6 / 15 (40%) · PB in organic top 12 7 / 15 (47%).
**27 Aug totals:** AIO present 14 / 15 (93%, unchanged) · PB cited 1 / 15 (7%) · PB organic not re-verified this cycle.
**7 Sep totals (final):** AIO present 13 / 15 (87%, down 1) · PB cited **0 / 15 (0%)** · PB organic not re-verified this cycle.

**This is a three-cycle progression, not a one-off dip: 40% → 7% → 0%.** PB has now lost every citation it held at baseline, including the one it briefly regained on `renters insurance dubai` at the 27 Aug checkpoint. AIO presence itself was stable through 27 Aug and only slipped on 7 Sep, when `group medical insurance dubai` stopped returning an AI Overview at all — so most of the decline is specifically about PB losing citation share, not AIO disappearing generally. Recurring winners across the 7 Sep run: esanad.com and seveninsurancebrokers.com (Business), hayah.com and direct.sukoon.com (Group Health), tameeninsurance.ae (Home, cited on all 5 Home queries). Worth investigating alongside the Semrush ranking volatility flagged above — both moved in the same window, which may or may not be related. Segment B is cited on 0 of 5 now while still ranking top-12 on all 5 per the original organic check (not re-verified this cycle) — if that's still true, the content itself isn't reading as citation-worthy to AIO's summarizer even though it still ranks.

---

## Data needed from Aakash to complete Current Status

Everything below is marked `—` above because it was not verified this cycle. Nothing has been guessed or inferred to fill these in.

**Resolved, Month-1 close-out complete:**
- ✅ Final Semrush export with competitor columns (7 Sep, period 1–7 Sep) — every ranking and competitor-gap KPI above now uses this final read.
- ✅ Final CRM leads export covering the complete 5 Aug–1 Sep window (`Leads 07-09-26.csv`) — all Lead volume KPIs are now exact final totals, no projection or normalization.
- ✅ Final AI Overview re-test (7 Sep, all three topic files) — same 15 queries verified against the Appendix.
- ✅ The full literal keyword lists for all three priority-keyword groups — provided by Aakash (`Priority Keywords.csv`), confirmed as an exact 6+4 split matching Segment C's "keywords 1–6" and Segment B's "keywords 7–10." All eight priority-keyword KPIs are filled in above (rankings from the position tracker's ~27 Aug read; clicks from the 28 Aug GSC pull — neither refreshed to 7 Sep, see below).
- ✅ The specific 4 URLs behind "intent-mismatch redirects resolved" — found in the original raw audit (`seo-aio-kra-kpi-2026-08-04.md`). All four live-checked — 2 of 4 already validated correct, 2 of 4 need Aakash's decision (not a technical fix). This also corrected an earlier error: the listicle redirect was never actually broken — an earlier test used the wrong URL.
- ✅ Sitemap gap corrected — 4 genuine gaps found via full cross-check, not the 0 Aakash had confirmed (only the hub itself was independently checked at that point).

**Still open:**
- **A decision on the two questionable redirects** — not a technical fix (both resolve correctly), but a strategic call on whether `.../best-group-health-insurance-companies-in-uae/` and `/group-life-insurance/articles/group-life-insurance-policy-for-employees/` should keep redirecting into their hubs or be reversed.
- **A query-dimension GSC pull**, if wanted, to refresh Home's "home insurance" cannibalization position and the 10 priority keywords' clicks/rankings to 7 Sep — currently these still read from the 28 Aug pull and the ~27 Aug Semrush position tracker respectively.

**Investigation, not a quick check:**
- Root cause for the November 2025 and May 2026 ranking breaks. I found candidate external causes — the May 2026 break window (10 May–6 Jun) almost exactly matches Google's confirmed May 2026 core update (21 May–2 Jun); the Nov 2025 break window (23 Nov–20 Dec) only weakly overlaps the Dec 2025 core update (11–29 Dec) and doesn't explain the earlier weeks. Neither is a confirmed diagnosis — both still need internal deploy/change-log review to rule in or out alongside the algorithm-update angle.
- Why PB's AI Overview citations went 40% → 7% → 0% across three tests (see Appendix) — worth checking whether this tracks with the Semrush ranking volatility over the same window, or with anything that changed on-site.
- Why the 24→30 Aug Semrush jump happened and then partially reversed by 7 Sep — still no confirmed cause for either move.

**Remaining live checks not covered this cycle:**
- Sitemap presence for `/home-insurance/articles/` and `/group-health-insurance/articles/` specifically (only `/business-insurance/` was independently spot-checked; the rest rely on Aakash's confirmation)

**GSC methodology, still open:** the URL-path-directory classification used to segment GSC data into A/B/C is still not confirmed identical to whatever page-set produced the 4/5 Aug baseline — rollup impressions come out to 69,762 vs the baseline's 64,318, a reasonable but not exact match. Still needs sign-off from whoever ran the original baseline pull. Full directory list: Segment A = `/business-insurance/`, `/sme-insurance/`, `/medical-malpractice/`, `/group-life-insurance/`, `/workers-compensation/`, `/fire-and-allied-perils-insurance/`, `/public-liability/`, `/professional-indemnity/`, `/fleet-insurance/`, `/marine-insurance/`, `/cyber-risk-insurance/`, `/commercial-motor/`, `/contractors-plant-machinery-insurance/`, `/yacht-insurance/`, `/erection-all-risks-insurance/`, `/trade-credit-insurance/`, `/directors-officers-liability-insurance/`, `/commercial-general-liability-insurance/`; Segment B = `/home-insurance/` plus home-insurer-review sub-pages under `/insurance-companies/`; Segment C = `/group-health-insurance/` and `/group-health-insurance-hic/` plus group-health sub-pages under `/insurance-companies/`.

**Also flagged, not yet resolved:** the competitor-gap KPIs above are now verified against adnic.ae / giggulf.ae / aig.ae (matching this doc's baseline), separate from an earlier position-tracking export this session that used a different competitor set (adcb.com / emiratesnbd.com / sarwa.co / stashaway.ae) — that export is not reflected in this doc.
