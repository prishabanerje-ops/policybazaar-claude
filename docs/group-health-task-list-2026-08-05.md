# Group Health Insurance — detailed task list

**Segment C** · URL pattern `/group-health-insurance` · **Month 1:** 5 August – 1 September 2026
**Search Console property:** `https://www.policybazaar.ae/`
**Derived from:** `seo-aio-kra-kpi-uae-filtered-2026-08-04.md` and `seo-aio-kra-kpi-2026-08-04.md`

Every task below is tied to a measured figure. Where a figure is UAE-filtered it is labelled UAE; where it is unfiltered it is labelled all-country. Page-level and query-level detail is 90-day all-country, because the UAE filter moves Search Console onto its anonymised dataset and loses roughly two-thirds of the clicks.

---

## Where the segment stands

| Metric | UAE, 28d | All-country, 28d | UAE, 360d | All-country, 360d |
|---|---|---|---|---|
| Clicks | 15 | 36 | 242 | 833 |
| Impressions | 20,051 | 25,608 | 219,676 | 351,293 |
| CTR | 0.07% | 0.14% | 0.11% | 0.24% |
| Average position | 41.6 | 36.8 | 30.0 | 26.0 |
| Pages earning impressions | 17 | 19 | 31 | 32 |

Trailing-year UAE run rate is 19 clicks and 17,086 impressions per 28 days, so the volume shortfall is only **−21%**, the smallest of the three segments. The position gap is **−11.6 places**, joint-worst. **This segment is a position and CTR problem, not a volume problem.**

Month-1 targets: UAE position 41.6 → **35.0**, UAE clicks 15 → **18**, UAE CTR 0.07% → **0.09%**, hub 38.4 → **≤31**, Semrush top 10 8 → **14**, priority keyword clicks 3 → **18**, AI Overview citation 1/5 → **3/5**, CRM leads 16 → **26**.

---

## Group 1 — Measurement and diagnosis (Week 1, blocking)

**Task 1. Move all Segment C reporting to the URL-prefix property.**
`sc-domain:policybazaar.ae` is missing 95 consecutive days, 5 Oct 2025 to 7 Jan 2026, and understates Segment C trailing-year clicks at 586 against the true 833. Any dashboard, alert or scheduled export still pointed at the domain property will disagree with this plan.

**Task 2. Diagnose the November 2025 break.**
Segment C lost **+8.1 positions all-country** and **+8.7 UAE** between the 26 Oct and 23 Nov 2025 buckets, the largest single-bucket loss of any segment. Site-wide lost 2.1 and 1.9 and recovered. Pull the change log, deploy history and log-file crawl data for 26 Oct – 20 Dec 2025.

| Bucket | C all-country position | C UAE position |
|---|---|---|
| 28 Sep 25 | 13.9 | 16.9 |
| 26 Oct 25 | 15.3 | 19.4 |
| **23 Nov 25** | **23.4** | **28.1** |

**Task 3. Diagnose the May 2026 break.**
A second, separate loss of **+6.7 all-country** and **+7.4 UAE** between the 12 Apr and 10 May 2026 buckets, from 27.2 to 33.9 and 33.0 to 40.4. Site-wide lost 1.5 and 1.2. Same evidence pull for 12 Apr – 6 Jun 2026.

**Task 4. Reconcile Semrush against Search Console.**
Semrush puts Segment C's average ranked position at **13.4**; Search Console reports **36.8 all-country and 41.6 UAE**. That is a 23 to 28 place divergence on the same market. Test four candidate causes: the `!geo&!hot&!aio` filter on the export, which excludes AI Overview SERPs; locale setting; device setting; and landing-page attribution. **Every page-2 conversion target below depends on which source is right.**

**Task 5. Add `medical insurance for company` to the Semrush campaign.**
Search volume 450, manual tracker position 24, Search Console position 12.0 all-country and 12.8 UAE. It is on the priority keyword list and absent from the tracked set.

**Task 6. Re-baseline the AI Overview sample, and set a re-measurement cadence.**
The five Segment C queries were re-captured on 11 Aug and the picture had already moved from the 4 Aug baseline. See Group 7. Fix a weekly capture on a consistent method before treating any AIO figure as a KPI.

---

## Group 2 — Indexation and crawl

**Task 7. Decide and act on `/group-health-insurance/articles/best-group-health-insurance-companies-in-uae/`.**
It carries **4,511 impressions and 2 clicks at position 50.3** across 8 URL variants, is **missing from the sitemap**, and currently **301s to `/group-health-insurance-hic/`**. See Group 3 for the decision itself. It cannot be added to the sitemap while it redirects, so Task 7 and Task 11 are the same decision.

**Task 8. Decide index or noindex on `/group-health-insurance/articles/`.**
The article index page returns 200, is missing from the sitemap, and earns **78 impressions and 0 clicks at position 66.3**. Either add it to the sitemap or apply noindex. Leaving it live and invisible is the one option that is not defensible.

**Task 9. Audit `/group-health-insurance/articles/corporate-wellness-programs-in-uae-workplace/`.**
It is the only Segment C URL in the sitemap that earns **zero impressions** in 90 days. Confirm it is indexed, has content worth serving, and targets a query that exists.

**Task 10. Deploy Product or Offer schema on `/group-health-insurance-hic/`.**
The hub carries FAQPage, BreadcrumbList, AggregateRating, author and a modified date, but has no Product or Offer markup. Segment A's and Segment B's hubs have the same gap.

**Sitemap position for the record:** 18 Segment C URLs in the sitemap, 19 distinct URLs earning impressions, 17 in both, 2 missing, 1 in the sitemap with no impressions.

---

## Group 3 — The listicle redirect decision

**Task 11. Decide whether to reverse the 301 on `best-group-health-insurance-companies-in-uae`.**

The case for reversing:

- The article holds **4,511 impressions and 2 clicks at position 50.3** while redirected.
- The query intent is comparison and listicle. The destination is a quote form.
- Position 50.3 on that impression volume is consistent with Google discounting an intent mismatch.

The case against, which is new and matters:

- **Seven anchor-fragment URLs from that same article rank at positions 9.4 to 10.6.** They are the strongest positions anywhere in Segment C.

| URL fragment | Impressions | Position |
|---|---|---|
| `#sukoon-insurance` | 62 | 9.4 |
| `#union-insurance` | 62 | 9.4 |
| `#gig-gulf-insurance` | 58 | 9.4 |
| `#rak-insurance` | 58 | 9.4 |
| `#abu-dhabi-national-insurance-company` | 16 | 10.2 |
| `#al-buhaira-national-insurance` | 12 | 10.6 |
| `#watania-takaful` | 12 | 10.6 |

Google is still surfacing the article's internal sections at page 1 for insurer-name queries even though the parent URL redirects. Reversing the redirect could consolidate that; leaving it may be losing it slowly. Decide in Week 1, measure in Week 4, and be prepared to leave it alone.

---

## Group 4 — Hub recovery

**Task 12. Recover `/group-health-insurance-hic/` from 33.7 to ≤27 all-country, and 38.4 to ≤31 UAE.**

| Measure | All-country, 28d | UAE, 28d |
|---|---|---|
| Clicks | 12 | 5 |
| Impressions | 8,741 | 6,948 |
| Position | 33.7 | 38.4 |

The hub is **37% of the segment's 90-day impressions** (27,430 of 74,268) and **30% of its clicks** (28 of 94). All six Group Health priority keywords already resolve to it, so there is no hub-versus-article conflict to fix here. Hub position is the whole story for this segment.

**Task 13. Verify the hub is the ranking URL for the head terms after any content change.**
Six of the 33 Semrush keywords currently land on the hub, including the three top-3 positions. Twenty-two land on `/articles/` pages. Confirm the split is deliberate.

---

## Group 5 — CTR and title/meta rewrites

**Task 14. Rewrite titles and metas for the 7 zero-click queries holding 11,693 impressions.**
All-country, 90 days, queries with 800 or more impressions and one click or fewer:

| Query | Impressions | Clicks | Position |
|---|---|---|---|
| group medical insurance | 2,940 | 0 | 45.5 |
| group medical insurance uae | 2,251 | 0 | 47.4 |
| group health insurance uae | 2,141 | 0 | 42.2 |
| group health insurance | 1,876 | 4 | 38.5 |
| group medical insurance dubai | 1,306 | 1 | 33.0 |
| group insurance uae | 1,136 | 0 | 19.4 |
| corporate health insurance | 1,115 | 0 | 25.9 |

**`group insurance uae` is the single clearest win: 1,136 impressions at position 19.4 with zero clicks.** It is the only high-volume Segment C query anywhere near page 1.

**Task 15. Fix the pages carrying impressions at near-zero CTR.**
All-country, 90 days:

| Page | Impressions | Clicks | Position | Note |
|---|---|---|---|---|
| `/articles/group-health-insurance-for-small-businesses/` | 10,506 | 3 | 32.6 | Second-largest impression pool in the segment, 0.03% CTR |
| `/articles/how-to-get-health-insurance-for-employees/` | 9,185 | 18 | 28.6 | Best-performing article, still 0.20% |
| `/articles/business-health-insurance/` | 4,744 | 7 | 40.8 | |
| `/articles/group-health-insurance-in-abu-dhabi/` | 2,603 | **0** | **79.9** | Worst position in the segment |
| `/articles/things-to-consider-when-buying-group-health-insurance-uae/` | 2,489 | **0** | 64.3 | |
| `/articles/employee-insurance-in-uae/` | 2,430 | 5 | 44.8 | |
| **`/articles/group-health-insurance-and-pre-existing-conditions/`** | **2,124** | **2** | **11.7** | **Page 1 and almost no clicks. Highest-value CTR fix in the segment** |
| `/articles/group-health-insurance-vs-individual-health-insurance/` | 1,655 | 1 | 60.5 | |

**Task 16. Protect the four pages that already convert.**
These have small impression pools but real CTR. Do not disturb them in any re-targeting work:

| Page | Impressions | Clicks | Position | CTR |
|---|---|---|---|---|
| `/articles/employee-fidelity-insurance/` | 408 | 5 | 12.0 | 1.23% |
| `/articles/sukoon-group-health-vs-fidelity-united-group-health-insurance/` | 461 | 5 | 9.1 | 1.08% |
| `/articles/how-to-switch-from-group-health-insurance-to-individual-cover/` | 471 | 4 | 20.0 | 0.85% |
| `/articles/labour-card-uae/` | 3,199 | 10 | 22.8 | 0.31% |

---

## Group 6 — Ranking work

**Task 17. Convert the Semrush page-2 pool: 22 of 33 keywords sit at positions 11 to 20, carrying 3,250 combined search volume.**
Target 8 → 14 in the top 10. Highest-volume first, with the two competitors that hold the positions:

| Keyword | PB | adnic | giggulf | SV | KD | Landing page |
|---|---|---|---|---|---|---|
| group medical insurance | 15 | 2 | 8 | 480 | 19 | hub |
| group health insurance | 16 | 5 | 9 | 480 | 24 | hub |
| group insurance health | 18 | 5 | 2 | 480 | 22 | hub |
| group health coverage | 19 | 8 | 10 | 480 | 0 | /articles/group-h… |
| group medical insurance for employees | 12 | 5 | 7 | 140 | 22 | /articles/how-to-… |
| group health insurance uae | 14 | 6 | 10 | 170 | 16 | /articles/group-h… |
| group medical insurance dubai | 14 | 7 | 12 | 170 | 22 | /articles/group-h… |
| best group health insurance | 14 | 8 | 13 | 170 | 18 | hub |
| medical insurance for employees in uae | 15 | 21 | 8 | 170 | 31 | /articles/how-to-… |
| group medical insurance uae | 20 | 6 | 10 | 170 | 16 | /articles/group-h… |
| group health insurance for employees | 13 | 9 | 6 | 110 | 17 | /articles/how-to-… |
| group health insurance providers | 17 | 15 | 10 | 40 | 16 | /articles/group-h… |
| employee health insurance dubai | 12 | 13 | 25 | 30 | 17 | /articles/how-to-… |
| cheap group health insurance | 13 | 8 | 6 | 30 | 0 | /articles/group-h… |
| employer group health insurance | 14 | 0 | 32 | 30 | 16 | /articles/how-to-… |
| group medical coverage | 18 | 3 | 9 | 30 | 26 | /articles/group-h… |
| group medical insurance plans | 12 | 5 | 9 | 20 | 12 | /articles/group-h… |
| group health insurance plans | 19 | 5 | 8 | 20 | 19 | /articles/group-h… |
| health insurance for company employees | 18 | 5 | 10 | 20 | 19 | /articles/how-to-… |
| group health medical insurance | 18 | 10 | 11 | 10 | 20 | /articles/group-h… |
| employee health insurance uae | 11 | 8 | 14 | 0 | 0 | /articles/how-to-… |
| group medical insurance coverage | 15 | 5 | 8 | 0 | 0 | /articles/group-h… |

**Task 18. Address the three keywords below position 20.**
`group health insurance dubai` at 22 with 140 search volume, `medical insurance groups` at 24 with 480, and `group health insurance vs individual health insurance` at 30. All three fell 20 to 24 places, the largest declines in the segment.

**Task 19. Defend the three top-3 positions.**
`best corporate health insurance` at 1, `corporate health insurance` at 3, `corporate medical insurance` at 3. All three land on the hub, so any hub change puts them at risk. Baseline them before Task 12 starts.

**Task 20. Work the Search Console page-2 pool, which is much smaller than Semrush suggests.**
Only 4 all-country queries sit at positions 11 to 20 with 100 or more impressions:

| Query | Impressions | Clicks | Position |
|---|---|---|---|
| group insurance uae | 1,136 | 0 | 19.4 |
| employee insurance | 191 | 0 | 12.2 |
| uae foreign assignment group medical insurance | 144 | 0 | 16.4 |
| corporate insurance bundle medical and life | 124 | 0 | 17.3 |

This is the gap in Task 4. Semrush says 22 keywords are within reach; Search Console says 4.

**Task 21. Recognise the scale of the deep-ranking problem.**
Of 1,774 Segment C queries over 90 days, **46 carry 300 or more impressions and hold 30,256 impressions between them, 41% of the segment**. Those 46 produce **10 clicks in total**. Their positions run from 19.4 to 57.8, with the large majority between 35 and 50. No title or meta work fixes a position-45 ranking; this pool needs ranking movement, not CTR work.

---

## Group 7 — AI Overview and GEO

**Task 22. Re-baseline before treating AIO as a KPI. The picture moved inside one week.**

| Query | 4 Aug: AIO / PB cited | 11 Aug: AIO / PB cited | PB organic top 12 |
|---|---|---|---|
| group health insurance dubai | yes / no | yes / **yes** | no |
| corporate health insurance uae | yes / no | yes / no | no |
| employee medical insurance uae | yes / no | yes / **yes** | no |
| group medical insurance dubai | yes / **yes** | **no AIO** / — | no |
| business health insurance uae | yes / no | yes / no | no |
| **Total** | **5/5 AIO, 1/5 cited** | **4/5 AIO, 2/5 cited** | **0/5** |

The Month-1 target of 3/5 was set against the 4 Aug baseline of 1/5. On the 11 Aug reading PB is already at 2/5. Either reading is defensible; what is not defensible is comparing a Week 4 capture against a baseline taken with a different method or on a different day.

**Task 23. Lead with the compliance answer.**
All three AI Overviews captured on 11 Aug open with the legal mandate:

- `group health insurance dubai`: "legally required by the Dubai Health Authority (DHA) for all private-sector employees. Employers must provide at least the Essential Benefits Plan (EBP)"
- `corporate health insurance uae`: "legally mandatory for all private-sector employers across all seven emirates in the UAE to issue or renew employee residence visas"
- `business health insurance uae`: "legally mandatory for all employers across all seven emirates. Companies must provide basic medical coverage to issue or renew employee visas. Annual costs range from…"

The hub and the two largest articles should carry an answer-first block in that exact shape: who is legally required, under which authority, what the minimum plan is, and what it costs. That is the format being cited.

**Task 24. Target the two queries where PB is not cited and an AIO fires.**
`corporate health insurance uae` and `business health insurance uae`. Note `business health insurance uae` cites **only one domain, hayah.com**, which makes it the cheapest citation to win in the segment.

**Task 25. Understand who is being cited.**
Across the four AI Overviews that fired on 11 Aug:

| Domain | Cited in |
|---|---|
| **hayah.com** | **4 of 4** |
| sukoon.com | 3 of 4 |
| dni.ae | 3 of 4 |
| metlife.ae | 3 of 4 |
| anib.ae, cigna-me.com, gargashinsurance.com, insurancehub.ae, kayrouzandassociates.com, omegainsurance.ae, **policybazaar.ae** | 2 of 4 |
| adnic.ae, aesinternational.com, allianzcare.com, amercenters.ae, colemontuae.com, damaninsurance.ae, iloe.ae, ngi.ae, pacificprime.com, pioneerinsurance.ae, seveninsurancebrokers.com, u.ae, whi.ae | 1 of 4 |

hayah.com is cited in every AI Overview that fires and ranks first organically on two of the five queries. It is the domain to study.

**Task 26. Note that government sources are being cited.**
`u.ae` and `iloe.ae` appear in the `employee medical insurance uae` overview. Citing and linking the DHA, DOH and MOHRE source pages correctly is likely part of what qualifies a page here.

**Task 27. Investigate `policybazaar.com` ranking in UAE results.**
On `group medical insurance dubai`, the organic top 12 contains **policybazaar.com at position 8** while policybazaar.ae does not appear at all. The Indian property is taking a UAE position the AE property should hold. Check hreflang, geo-targeting and whether the .com should be excluded from AE results.

---

## Group 8 — Priority keywords

**Task 28. Move the six Group Health priority keywords.**
All six resolve to `/group-health-insurance-hic/`, so this is hub work, not a targeting fix.

| # | Keyword | UAE 28d impr | UAE 28d clicks | UAE 28d pos | UAE 360d pos | All-country 28d pos |
|---|---|---|---|---|---|---|
| 1 | medical insurance for company | 24 | 0 | **12.8** | 23.0 | 12.0 |
| 2 | group medical insurance | 491 | 0 | 26.8 | 17.6 | 26.6 |
| 3 | group health insurance uae | 376 | 0 | 21.2 | 19.5 | 21.1 |
| 4 | group medical coverage | 31 | 0 | 26.5 | 13.6 | 32.4 |
| 5 | group health coverage | 64 | 0 | 23.1 | **8.6** | 25.9 |
| 6 | group health insurance | 441 | **3** | 20.9 | 13.0 | 21.0 |
| | **Total** | **1,427** | **3** | | | |

Targets: combined UAE clicks 3 → **18**, keywords in UAE top 20 1/6 → **5/6**.

Five of the six averaged 8.6 to 19.5 over the trailing year and all six now sit at 20.9 to 26.8. **Keyword 5, `group health coverage`, averaged 8.6 over the year and now sits at 23.1** — the largest single-keyword fall on the list. Keyword 1 is already at 12.8 on tiny volume, so it is the only one currently inside the top 20.

**Task 29. Raise `group medical insurance` and `group health insurance` first.**
They carry 491 and 441 UAE impressions of the 1,427 total, 65% between them, and both sit just outside the top 20 at 26.8 and 20.9.

---

## Group 9 — Lead conversion

**Task 30. Move CRM Group Health leads from 16 to 26 per month.**
Trailing-12 monthly average is 32 and the best month was 45 in September 2025, so the target sits below the average. July 2026 was down **−63% year on year** against 43 in July 2025.

**Task 31. Do not rely on organic traffic alone to deliver it.**
Organic is only **6.4% of Segment C UAE sessions** over 360 days and 5.1% over the last 28. GA4 records 574 organic sessions and 213 key events over 360 days UAE, 27 sessions and 6 key events over the last 28. Even a full ranking recovery moves a small number of sessions, so most of the lead target has to come from conversion-rate work on the sessions the segment already gets.

**Task 32. Treat the GA4 key-event figures as unconfirmed.**
What fires `formSubmitSuccess` has not been verified with analytics, and the event count runs roughly ten times CRM lead volume site-wide. CRM is the only lead measure in this plan until that is resolved.

---

# Content writer brief

Nineteen Segment C pages earn impressions. The writer's job this month is not volume; it is fixing pages that already collect impressions and convert almost none of them, and filling the one genuine topic gap. Work in the order below.

**Current page inventory, 90 days all-country, ordered by impressions.** Schema read from raw server HTML.

| Page | Impressions | Clicks | Position | FAQPage | Product |
|---|---|---|---|---|---|
| `/group-health-insurance-hic/` (hub) | 27,430 | 28 | 31.6 | yes | **no** |
| `/articles/group-health-insurance-for-small-businesses/` | 10,506 | 3 | 32.6 | yes | no |
| `/articles/how-to-get-health-insurance-for-employees/` | 9,185 | 18 | 28.6 | yes | no |
| `/articles/business-health-insurance/` | 4,744 | 7 | 40.8 | yes | no |
| `/articles/best-group-health-insurance-companies-in-uae/` | 4,231 | 2 | 50.3 | — redirected — | |
| `/articles/labour-card-uae/` | 3,199 | 10 | 22.8 | not checked | |
| `/articles/group-health-insurance-in-abu-dhabi/` | 2,603 | **0** | **79.9** | yes | no |
| `/articles/things-to-consider-when-buying-group-health-insurance-uae/` | 2,489 | **0** | 64.3 | **no** | **yes** |
| `/articles/employee-insurance-in-uae/` | 2,430 | 5 | 44.8 | not checked | |
| `/articles/group-health-insurance-and-pre-existing-conditions/` | 2,124 | 2 | **11.7** | yes | no |
| `/articles/group-health-insurance-vs-individual-health-insurance/` | 1,655 | 1 | 60.5 | not checked | |
| `/articles/group-health-insurance-vs-family-floater-insurance/` | 764 | 2 | 24.4 | not checked | |
| `/articles/what-is-enaya-program/` | 675 | 1 | 10.8 | not checked | |
| `/articles/how-to-switch-from-group-health-insurance-to-individual-cover/` | 471 | 4 | 20.0 | not checked | |
| `/articles/group-health-insurance-benefits/` | 463 | 1 | 37.8 | not checked | |
| `/articles/sukoon-group-health-vs-fidelity-united-group-health-insurance/` | 461 | 5 | 9.1 | not checked | |
| `/articles/employee-fidelity-insurance/` | 408 | 5 | 12.0 | not checked | |
| `/articles/` (index) | 78 | 0 | 66.3 | — | |
| `/articles/tips-for-buying-group-health-insurance-in-uae/` | 72 | 0 | 15.3 | not checked | |
| `/articles/corporate-wellness-programs-in-uae-workplace/` | **0** | 0 | — | not checked | |

**Query themes, 90 days all-country, query dimension.** The query dimension totals 59,824 impressions against 74,268 on the page dimension, because Search Console anonymises rare queries. Use these for proportion, not for absolute volume.

| Theme | Keywords | Impressions | Share | Clicks | Avg position | Page that owns it |
|---|---|---|---|---|---|---|
| Generic head terms | 1,017 | 42,353 | 70.8% | 25 | — | hub |
| Emirate-specific | 204 | 5,224 | 8.7% | 2 | 34.0 | Abu Dhabi article only |
| SME / small business | 162 | 4,270 | 7.1% | 1 | 34.7 | small-businesses article |
| Best / listicle | 172 | 3,203 | 5.4% | 1 | 39.1 | redirected listicle |
| Coverage / benefits | 140 | 2,398 | 4.0% | 1 | 43.0 | benefits article |
| Cost / price | 169 | 1,955 | 3.3% | 1 | **49.1** | hub section only |
| **Large / enterprise** | **17** | **1,548** | **2.6%** | **0** | **37.0** | **none** |
| Compliance / mandate | 59 | 946 | 1.6% | 1 | 46.9 | scattered |
| Renewal / switching | 14 | 93 | 0.2% | 0 | 34.5 | switching article |
| Free zone / mainland | 4 | 14 | 0.0% | 0 | 74.8 | none |

---

## Priority 1 — Fix what already has page-1 visibility

**Task 33. Rewrite the title and meta on `/articles/group-health-insurance-and-pre-existing-conditions/`.**
Position **11.7** on **2,124 impressions returning 2 clicks**, a CTR of 0.09%. This is the only Segment C page sitting on page 1 at real volume, and it is the single highest-value writing task in the segment. Current title is *"Group Health Insurance and Pre-Existing Conditions: What You Need to Know"* at 73 characters and the meta opens *"Discover essential information on…"*, which is filler. Rewrite both to lead with the answer employers are searching for: whether pre-existing conditions are covered, and from when. The page already has FAQPage schema and covers day-1 cover and medical-test requirements, so the content is there; the SERP snippet is not earning the click.

**Task 34. Do not touch the four pages that already convert.**
`/articles/sukoon-group-health-vs-fidelity-united…` at 9.1 with 1.08% CTR, `/articles/employee-fidelity-insurance/` at 12.0 with 1.23%, `/articles/how-to-switch-from-group-health-insurance-to-individual-cover/` at 20.0 with 0.85%, and `/articles/labour-card-uae/` at 22.8 with 0.31%. They carry small impression pools but the best CTR in the segment. If a re-targeting task touches them, flag it first.

---

## Priority 2 — The AI Overview format

**Task 35. Add an answer-first compliance block to the hub and the two largest articles.**
Every AI Overview captured on 11 August opens with the legal mandate, in near-identical shape:

- `group health insurance dubai`: "legally required by the Dubai Health Authority (DHA) for all private-sector employees. Employers must provide at least the Essential Benefits Plan (EBP)"
- `corporate health insurance uae`: "legally mandatory for all private-sector employers across all seven emirates in the UAE to issue or renew employee residence visas"
- `business health insurance uae`: "legally mandatory for all employers across all seven emirates. Companies must provide basic medical coverage to issue or renew employee visas. Annual costs range from…"

Write a block of 60 to 90 words, placed above the fold, answering in this order: **who is legally required, under which authority, what the minimum plan is, what it costs, and what the penalty is for not having it.** Apply to `/group-health-insurance-hic/`, `/articles/how-to-get-health-insurance-for-employees/` and `/articles/business-health-insurance/`.

The hub already mentions DHA, DOH, MOHRE, EBP, an AED figure and penalties, so the facts exist on the page. They are not assembled into a single quotable passage at the top, which is the format being cited.

**Task 36. Target `business health insurance uae` first.**
That AI Overview cites **exactly one domain, hayah.com**. It is the cheapest citation to win in the segment. The page that should win it, `/articles/business-health-insurance/`, currently mentions DHA but **not DOH, not MOHRE and not the Essential Benefits Plan**, while the overview is built entirely on the all-seven-emirates mandate. Add those three entities with correct attribution.

**Task 37. Cite the government sources by name and link them.**
`u.ae` and `iloe.ae` are both cited in the `employee medical insurance uae` overview. Where the copy states a legal requirement, name the authority and link the source page: DHA for Dubai, DOH for Abu Dhabi, MOHRE for labour-law points. This is a YMYL topic and the cited set is dominated by insurers and government.

---

## Priority 3 — Rewrite the three pages that collect impressions and rank nowhere

**Task 38. Rewrite `/articles/group-health-insurance-in-abu-dhabi/`.**
**2,603 impressions, 0 clicks, position 79.9 — the worst position in the segment.** The page is about Abu Dhabi and **does not mention DOH, the Abu Dhabi regulator**, anywhere in the HTML. It mentions DHA, which is the Dubai authority. Abu Dhabi runs under the Department of Health and the Thiqa/Basic scheme, not the DHA Essential Benefits Plan. Rewrite around the correct regulator and the correct minimum-cover rules. The emirate-specific theme is 8.7% of segment impressions and this is the only page serving it.

**Task 39. Rewrite `/articles/things-to-consider-when-buying-group-health-insurance-uae/`.**
**2,489 impressions, 0 clicks, position 64.3.** It is the **only Segment C page with no FAQPage schema**, and the only one carrying Product schema, which is the reverse of every sibling. Ten headings against 21 to 31 on the pages that perform. Expand it, add an FAQ block, and align the schema with the rest of the folder.

**Task 40. Rewrite `/articles/group-health-insurance-vs-individual-health-insurance/`.**
**1,655 impressions, 1 click, position 60.5.** The comparison theme carries 3,203 impressions at an average of 39.1, and `group insurance vs individual insurance` alone sits at 196 impressions and position 75.9. A comparison page ranking at 60 for its own comparison query needs a genuine side-by-side table with cost, cover, eligibility and portability, not prose.

---

## Priority 4 — The one real content gap

**Task 41. Write a large-company or enterprise group medical insurance page.**
**17 queries, 1,548 impressions, 0 clicks, average position 37.0, and no page targets this.** There is a small-business article and no large-business equivalent.

| Query | Impressions | Position |
|---|---|---|
| large group medical insurance | 463 | 40.8 |
| large businesses group health insurance uae | 376 | 38.2 |
| large group medical insurance uae | 339 | 41.4 |
| group medical insurance for large companies uae | 251 | 27.4 |
| large business health insurance | 45 | 44.0 |
| compare group medical insurance for large firms | 30 | 7.5 |

Brief: employee-count bands and what changes at each, experience-rated versus community-rated pricing, multi-emirate workforces under DHA and DOH together, dependants and domestic staff, and the renewal and claims-ratio conversation a large employer has. The hub and the business-health article both mention large companies in passing; neither targets these queries.

---

## Priority 5 — Strengthen the two biggest impression pools

**Task 42. Expand `/articles/group-health-insurance-for-small-businesses/`.**
**10,506 impressions, 3 clicks, position 32.6, a CTR of 0.03%** — the second-largest impression pool in the segment and the worst conversion of any page carrying real volume. The SME theme is 4,270 query impressions at an average position of 34.7, so demand is there and the page is not reaching page 1 for any of it. The page mentions DHA but **not DOH, MOHRE or the Essential Benefits Plan**, and has 21 headings. Add the compliance framing from Task 35, an employee-count section, and real AED cost bands.

**Task 43. Give the cost theme a real answer.**
**169 queries, 1,955 impressions, 1 click, average position 49.1** — the worst average position of any theme. The hub already has an H2, *"How Much Does Group Health Insurance Cost in the UAE?"*, with five sub-headings on cost factors, and it still ranks 49 on this cluster. Cost factors are not a cost answer. Add actual AED ranges by employee band and by plan tier, dated and sourced. Every AI Overview in this segment quotes a cost range; ours does not give one in a form that can be quoted.

**Task 44. Give the compliance cluster a dedicated home.**
**59 queries, 946 impressions, 1 click, average position 46.9.** The two largest are `employer group health insurance requirements` at 390 impressions and position 57.3, and `how many employees are required for group health insurance` at 252 and position 52.4. The second is already answered as FAQ Q2 on `/articles/how-to-get-health-insurance-for-employees/` and still ranks 52, which suggests an FAQ answer buried on a broad page is not enough. Either promote it to an H2 with its own section, or write a standalone employer-requirements page.

---

## Priority 6 — Titles and metas for the zero-click queries

**Task 45. Rewrite titles and metas against the 7 queries holding 11,693 impressions and 5 clicks.**

| Query | Impressions | Clicks | Position | Page to fix |
|---|---|---|---|---|
| group medical insurance | 2,940 | 0 | 45.5 | hub |
| group medical insurance uae | 2,251 | 0 | 47.4 | hub |
| group health insurance uae | 2,141 | 0 | 42.2 | hub |
| group health insurance | 1,876 | 4 | 38.5 | hub |
| group medical insurance dubai | 1,306 | 1 | 33.0 | hub |
| **group insurance uae** | **1,136** | **0** | **19.4** | hub |
| corporate health insurance | 1,115 | 0 | 25.9 | hub |

**`group insurance uae` is the clearest single win: 1,136 impressions at position 19.4 with zero clicks.** It is the only high-volume Segment C query anywhere near page 1. The hub title currently reads *"Group Health Insurance Dubai & UAE | Compare Plans from AED 2/Day*"*. Note five of these seven queries say **medical**, not **health**, and the hub title carries neither "group medical insurance" nor "group insurance UAE" as an exact string.

**Task 46. Fix the two weakest metas.**
`/articles/group-health-insurance-and-pre-existing-conditions/` opens *"Discover essential information on…"* and `/articles/things-to-consider-when-buying-group-health-insurance-uae/` opens *"Discover 6 essential tips for…"*. Both start with a filler verb rather than the answer. Every meta in the folder should lead with the fact the searcher wants.

---

## Priority 7 — Editorial standards for everything written this month

**Task 47. Apply the same standards to every page touched.**

- Named author and reviewer. The hub, `how-to-get-health-insurance-for-employees` and `business-health-insurance` already carry Chanchal Singh and Ashu Bajaj; `group-health-insurance-and-pre-existing-conditions` has no Person markup at all.
- A visible last-updated date.
- The correct regulator per emirate: DHA for Dubai, DOH for Abu Dhabi, MOHRE for labour-law points.
- Every AED figure dated and attributed.
- An FAQ block with FAQPage schema, which every page in the folder has except `things-to-consider`.
- No "not financial advice" boilerplate substituting for a source.

---

## What not to write

**Task 48. Do not commission these, the demand is not there.**

| Theme | Queries | Impressions | Verdict |
|---|---|---|---|
| Free zone / mainland | 4 | **14** | No page. The largest single query is 9 impressions |
| Renewal / switching | 14 | **93** | Covered by the existing switching article, which already converts at 0.85% |
| Claims | 11 | **17** | The hub already has a claims H2. Nothing more is justified |
| Domestic worker | 3 | 28 | Two of the three are `site:` operator searches, so this is internal testing, not demand |

**Task 49. Do not write to fix position 45.**
Of the 46 queries carrying 300 or more impressions, 41% of the segment, positions run from 19.4 to 57.8 and the large majority sit between 35 and 50. Titles and metas move CTR at a given position; they do not move a page from 45 to 10. For that pool the lever is the hub's authority and the ranking work in Group 6, not more articles.

---

## Open questions

1. What happened in late November 2025, and again in early May 2026? No known migration, replatform, redirect deploy or property change explains either.
2. Semrush or Search Console on this segment: 13.4 against 36.8. Which is right?
3. Reverse the `best-group-health-insurance-companies-in-uae` redirect, or leave it? The seven anchor URLs ranking at 9.4 to 10.6 make this less obvious than it looked.
4. Sitemap or noindex for `/group-health-insurance/articles/`?
5. Which AI Overview baseline stands, 4 Aug at 1/5 or 11 Aug at 2/5?
6. Should `policybazaar.com` be excluded from UAE results, or is its position 8 on `group medical insurance dubai` intentional?
7. What fires `formSubmitSuccess`?

---

## Data notes

- Search Console property is `https://www.policybazaar.ae/`. The domain property is missing 5 Oct 2025 to 7 Jan 2026 and must not be used.
- Page-level and query-level detail is 90-day all-country, 2026-05-04 to 2026-08-01, from a 25,000-row export. Smaller row limits undercount zero-click queries, because Search Console sorts by clicks descending and those queries sort last.
- Segment aggregates are given both UAE-filtered and all-country. A country filter moves Search Console onto its anonymised dataset, so UAE clicks and CTR are understated by roughly two to three times. Positions are unaffected.
- Semrush figures are the 4 Aug 2026 snapshot, filter `!geo&!hot&!aio`, which excludes AI Overview SERPs.
- AI Overview data was captured on google.ae with `gl=ae&hl=en`, on 4 Aug and again on 11 Aug, not from a UAE IP.
- CRM lead data carries volume only, with no quality or status split.
