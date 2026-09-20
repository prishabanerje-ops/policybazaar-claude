# SEO + AIO KRA/KPI Plan — Business, Home and Group Health Insurance

**Domain:** policybazaar.ae · **Month 1:** 5 August – 1 September 2026 · **Prepared:** 4 August 2026
**Search Console property:** `https://www.policybazaar.ae/`

> Figures restated on the URL-prefix property. An earlier draft used the domain property `sc-domain:policybazaar.ae`, which has a 95-day hole in its own reporting from 5 Oct 2025 to 7 Jan 2026. The URL-prefix property is complete for all 360 days. Twenty-eight-day and ninety-day figures are unaffected; trailing-year figures and the trend are.

---

## Data source status (read this before the numbers)

| Source | Status | How it was obtained |
|---|---|---|
| Google Search Console | Live | Property `https://www.policybazaar.ae/`, `page` dimension with `includingRegex` filter per segment. **No country filter** — see gap 12 |
| GA4 | Live | Property `309894472`, `landingPagePlusQueryString` with `PARTIAL_REGEXP` per segment |
| Semrush ranking export | Parsed | Snapshot 4 Aug 2026, 125 keywords, 5 domains, filter `!geo&!hot&!aio` |
| Manual ranking tracker | Parsed | 10 in-scope keywords, current to 4 Aug. No Business segment coverage |
| Lead data (CRM) | Parsed | Monthly Dec'21–Aug'26, daily to 3 Aug'26. Volume only |
| AI Overview / GEO | Measured | 15 queries on google.ae, `gl=ae&hl=en`, 5 per segment |
| Sitemap and redirect audit | Measured | All GSC-earning URLs status-checked, every redirect chain followed |
| Semrush MCP, Supermetrics, Windsor.ai | Unauthorised | Not used, require OAuth in an interactive session |

**Windows:** 360-day = 2025-08-07 → 2026-08-01 · 90-day = 2026-05-04 → 2026-08-01 · 28-day = 2026-07-05 → 2026-08-01. The 28-day window is the operative baseline. All windows end 3 days before report date for API lag. All 360 days carry data on this property.

---

# STEP 1 — Baseline

## 1a. Google Search Console

| Metric | A Business | B Home | C Group Health | Site-wide |
|---|---|---|---|---|
| **360d clicks** | 4,786 | 2,289 | 833 | 428,555 |
| 360d impressions | 812,863 | 430,571 | 351,293 | 44,664,692 |
| 360d CTR | 0.59% | 0.53% | 0.24% | 0.96% |
| **360d avg position** | **18.9** | **16.6** | **26.0** | 11.5 |
| 360d pages earning impressions | 199 | 116 | 32 | — |
| 90d clicks | 778 | 201 | 94 | 71,125 |
| 90d impressions | 164,897 | 84,404 | 74,268 | 8,609,210 |
| 90d CTR | 0.47% | 0.24% | 0.13% | 0.83% |
| 90d avg position | 26.5 | 22.6 | 35.3 | 11.9 |
| **28d clicks** | **249** | **71** | **36** | 20,662 |
| **28d impressions** | **49,780** | **27,930** | **25,608** | 2,442,198 |
| **28d CTR** | **0.50%** | **0.25%** | **0.14%** | 0.85% |
| **28d avg position** | **26.7** | **23.3** | **36.8** | 12.4 |
| 28d pages earning impressions | 157 | 81 | 19 | — |

Rollup for the three segments, 28 days: **356 clicks, 103,318 impressions, 0.34% CTR, blended impression-weighted position 28.3.** Over 360 days: 7,908 clicks, 1,594,727 impressions, 0.50% CTR, blended position 19.8.

**The gap to the trailing-year run rate.** 360-day figures divided by 360 and multiplied by 28. This is the evidence base for every target in Step 2.

| Segment | Trailing-year 28d run rate | Actual last 28d | Shortfall | 360d position | Current | Gap |
|---|---|---|---|---|---|---|
| A Business | 372 clicks / 63,223 impr | 249 / 49,780 | **−33%** | 18.9 | 26.7 | −7.8 |
| B Home | 178 clicks / 33,489 impr | 71 / 27,930 | **−60%** | 16.6 | 23.3 | −6.7 |
| C Group Health | 65 clicks / 27,323 impr | 36 / 25,608 | **−45%** | 26.0 | 36.8 | −10.8 |
| **Rollup** | **615 clicks / 124,034 impr** | **356 / 103,318** | **−42%** | **19.8** | **28.3** | **−8.5** |

**Twelve-month trend, 28-day buckets.** All 13 buckets carry a full 28 days of data.

| Bucket start | A clicks / pos | B clicks / pos | C clicks / pos | Site-wide clicks / pos |
|---|---|---|---|---|
| 03 Aug 25 | 448 / 18.4 | 256 / 23.2 | 69 / 24.8 | 47,405 / 19.5 |
| 31 Aug 25 | 373 / 12.7 | 269 / 15.3 | 74 / 19.0 | 41,658 / 14.2 |
| 28 Sep 25 | 402 / **9.9** | 217 / 10.6 | 94 / **13.9** | 41,325 / 9.8 |
| 26 Oct 25 | 402 / 10.7 | 161 / **10.5** | 73 / 15.3 | 35,160 / **9.4** |
| **23 Nov 25** | **328 / 15.9** | **188 / 15.7** | **57 / 23.4** | 30,514 / 11.5 |
| 21 Dec 25 | 471 / 20.1 | 162 / 16.5 | 71 / 23.4 | 35,708 / 11.0 |
| 18 Jan 26 | 510 / 23.5 | 154 / 17.3 | 107 / 26.9 | 39,163 / 11.1 |
| 15 Feb 26 | **512** / 19.0 | **534** / 12.2 | 101 / 25.3 | 45,976 / **9.2** |
| 15 Mar 26 | 336 / 17.7 | 125 / 13.4 | 65 / 26.2 | 27,920 / 9.2 |
| 12 Apr 26 | 372 / 19.1 | 80 / 15.1 | 44 / 27.2 | 25,298 / 10.6 |
| **10 May 26** | **219 / 26.7** | **55 / 22.0** | **28 / 33.9** | 22,100 / 12.1 |
| 07 Jun 26 | 245 / 27.9 | 65 / 23.2 | 27 / 36.1 | 22,849 / 11.6 |
| 05 Jul 26 | 249 / 26.7 | 71 / 23.3 | 36 / 36.8 | 20,662 / 12.4 |
| **Trailing-year best** | **512 / 9.9** | **534 / 10.5** | **107 / 13.9** | 47,405 / 9.2 |

**Two breaks, not one, and neither is site-wide.** Position deterioration bucket over bucket:

| Bucket | A Business | B Home | C Group Health | Site-wide |
|---|---|---|---|---|
| **23 Nov – 20 Dec 2025** | **+5.2** | **+5.2** | **+8.1** | +2.1 |
| **10 May – 6 Jun 2026** | **+7.6** | **+6.9** | **+6.7** | +1.5 |

Each segment lost 5 to 8 positions in November and again in May, while the site lost 2.1 and 1.5 and recovered both times. Site-wide position was 9.2 in February and 12.4 now, against 18.9 → 26.7 for Segment A. The segments are not tracking the site; they are degrading independently of it, and both events are undiagnosed.

## 1b. GA4

Conversion event: **`formSubmitSuccess`**. Other configured key events (`car_insurance_Lead_GA4`, `generate_lead_health`, `talkToExpert`, `travel_Insurance_Conversion`) also fire in these sessions but are cross-product journeys and are excluded from segment lead figures.

| Metric | A Business | B Home | C Group Health |
|---|---|---|---|
| 360d sessions, all channels | 40,994 | 7,933 | 11,456 |
| **360d sessions, organic** | **5,286** | **2,626** | **988** |
| **Organic share of segment** | 12.9% | **33.1%** | 8.6% |
| 360d engagement rate, organic | 68.6% | 65.2% | 77.5% |
| 360d key events, organic | 1,535 | 573 | 325 |
| Key events per session, organic | 29.0% | 21.8% | 32.9% |
| 90d organic sessions / key events | 1,002 / 348 | 243 / 80 | 191 / 59 |
| **28d organic sessions / key events** | **334 / 98** | **84 / 23** | **70 / 13** |

360-day organic `formSubmitSuccess`: A 1,316 · B 521 · C 231.

Home Insurance is the priority for lead recovery. A third of its traffic is organic, so ranking recovery converts to leads faster there than in either other segment.

## 1c. Semrush ranking export

| Metric | A Business | B Home | C Group Health |
|---|---|---|---|
| Tracked keywords | 52 | 40 | 33 |
| Ranking, any position | 49 | 39 | 33 |
| Top 3 | 11 | 4 | 3 |
| Top 10 | 22 | 14 | 8 |
| Top 20 | 36 | 35 | 30 |
| **Positions 11–20, the quick-win pool** | **14** | **21** | **22** |
| Positions 21–50 | 11 | 4 | 3 |
| Above 50 or not ranking | 5 | 1 | 0 |
| Average position of ranked keywords | 15.0 | 12.5 | 13.4 |
| Tracked search volume | 4,700 | 5,180 | 4,340 |

**Competitor top-10 count on the identical keyword set.**

| Segment | policybazaar.ae | giggulf.ae | adnic.ae | aig.ae |
|---|---|---|---|---|
| A Business (52 kws) | **22** | 21 | 16 | 10 |
| B Home (40 kws) | **14** | 29 | 29 | 1 |
| C Group Health (33 kws) | **8** | 21 | 24 | 0 |

Top 3 within segment: A — PB 11, adnic 8, aig 6, giggulf 5. B — giggulf 21, adnic 19, PB 4. C — adnic 3, PB 3, giggulf 1. PB leads Business and is well behind in Home and Group Health.

**Direction of movement,** excluding 26 of 125 keywords whose reported change equals `100 − current position`, the signature of newly added keywords rather than real movement:

| Segment | Keywords with genuine movement | Up | Down | Flat |
|---|---|---|---|---|
| A Business | 49 | 9 | 36 | 4 |
| B Home | 13 | 2 | 10 | 1 |
| C Group Health | 33 | 1 | **32** | 0 |

## 1d. Manual tracker vs Semrush cross-check

Both dated 4 August 2026.

| Keyword | Manual | Semrush | Delta | Semrush landing page |
|---|---|---|---|---|
| medical insurance for company | 24 | absent | — | not in campaign |
| group medical insurance | 22 | 15 | −7 | /group-health-insurance-hic/ |
| group health insurance uae | 18 | 14 | −4 | /group-health-insurance/articles/… |
| group medical coverage | 15 | 18 | +3 | /group-health-insurance/articles/… |
| group health coverage | 12 | 19 | +7 | /group-health-insurance/articles/… |
| group health insurance | 12 | 16 | +4 | /group-health-insurance-hic/ |
| home insurance uae | 13 | 12 | −1 | /home-insurance/articles/best-… |
| home insurance | 14 | 14 | 0 | /home-insurance/articles/best-… |
| home insurance dubai | 14 | 10 | −4 | /home-insurance/articles/best-… |
| best home insurance in uae | 1 | absent | — | not in campaign |

Discrepancies reach ±7 on the same keyword on the same date, from three causes: different locale and device settings, the `!aio` filter on the Semrush export, and the two trackers watching different URLs. Two priority keywords are not in the Semrush campaign at all.

## 1e. Priority keywords

Search Console query-level data for the 10 priority keywords.

| # | Keyword | 360d impr | 360d clicks | 360d pos | 28d impr | 28d clicks | 28d pos | Semrush | Manual | Ranking URL |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | medical insurance for company | 165 | 2 | 32.8 | 17 | 0 | **12.0** | absent | 24 | /group-health-insurance-hic/ |
| 2 | group medical insurance | 6,032 | 10 | 18.0 | 497 | 0 | 26.6 | 15 | 22 | /group-health-insurance-hic/ |
| 3 | group health insurance uae | 4,183 | 1 | 19.2 | 383 | 0 | 21.1 | 14 | 18 | /group-health-insurance-hic/ |
| 4 | group medical coverage | 313 | 1 | 17.2 | 20 | 0 | 32.4 | 18 | 15 | /group-health-insurance-hic/ |
| 5 | group health coverage | 640 | 2 | 8.4 | 42 | 0 | 25.9 | 19 | 12 | /group-health-insurance-hic/ |
| 6 | group health insurance | 4,924 | 31 | 13.5 | 448 | **3** | 21.0 | 16 | 12 | /group-health-insurance-hic/ |
| 7 | home insurance uae | 3,454 | 11 | 19.5 | 332 | 0 | 20.5 | 12 | 13 | /home-insurance/articles/best-… |
| 8 | home insurance | 8,734 | 34 | 16.9 | 574 | **1** | 26.3 | 14 | 14 | /home-insurance/ |
| 9 | home insurance dubai | 8,853 | 45 | 17.7 | 677 | **1** | 23.0 | 10 | 14 | /home-insurance/articles/best-… |
| 10 | best home insurance in uae | **0** | 0 | — | **0** | 0 | — | absent | **1** | /home-insurance/articles/best-… |
| | **Total** | **37,298** | **137** | | **2,990** | **5** | | | | |

| Priority-keyword position | Current, 28d |
|---|---|
| Total clicks | **5** |
| Total impressions | 2,990 |
| Blended CTR | 0.17% |
| Keywords with at least 1 click | **3 / 10** |
| Keywords in GSC top 10 | **0 / 10** |
| Keywords in GSC top 20 | **1 / 10** |
| Keywords with zero impressions | **1 / 10** |
| Keywords tracked in Semrush | 8 / 10 |
| Segment C subset, #1–6 | 3 clicks on 1,407 impressions |
| Segment B subset, #7–10 | 2 clicks on 1,583 impressions |

All six Group Health priority keywords resolve to the `/group-health-insurance-hic/` hub, so there is no hub-versus-article conflict on this list. Three of the four Home keywords resolve to the child article rather than the hub. Nine of the ten averaged better than position 20 over the trailing year; all ten now sit at 21 or worse, except `medical insurance for company` at 12.0.

## 1f. Lead data (CRM)

Column 4 of the source file is Group Health. The `SME` header in the monthly block is a labelling error; the monthly and daily series are identical.

| Metric | A Business Insurance | B Home Insurance | C Group Health |
|---|---|---|---|
| Jul'2026, last full month | 133 | 36 | 16 |
| Jun'2026 | 95 | 32 | 23 |
| May'2026 | 117 | 44 | 14 |
| 3-month total | 345 | 112 | 53 |
| 3-month monthly average | 115.0 | 37.3 | 17.7 |
| Jul'2025 | 100 | 103 | 43 |
| **Year on year, July** | **+33%** | **−65%** | **−63%** |
| Trailing 12 months | 1,644 | 833 | 384 |
| Trailing-12 monthly average | 137.0 | 69.4 | 32.0 |
| Trailing-12 best month | 171 (Oct'25) | 113 (Mar'26) | 45 (Sep'25) |

Rollup: 185 leads in July 2026 against a trailing-12 monthly average of 238. No lead-quality or status split exists in the file, and no URL or page field, so segment mapping is by product column only.

## 1g. Technical, indexation and redirects

All distinct Search Console earning URLs across the three segments were status-checked and every redirect chain followed.

| Check | A Business | B Home | C Group Health | Total |
|---|---|---|---|---|
| URLs in sitemap | 134 | 56 | 18 | 208 |
| Distinct URLs earning impressions | 150 | 60 | 19 | 229 |
| In both | 131 | 56 | 17 | 204 |
| **Earning impressions but missing from sitemap** | **19** | **4** | **2** | **25** |
| In sitemap, zero impressions | 3 | 0 | 1 | 4 |

**Verdict on the 25 missing URLs.**

| Finding | URLs | Impressions | Clicks | Was the decision right? |
|---|---|---|---|---|
| Live 200, self-canonical, crawlable, simply absent | **15** | **10,376** | 17 | **No. Add to sitemap** |
| Article 301'd to a commercial hub, intent mismatch | 4 | 8,301 | 15 | **Two of four are questionable** |
| robots.txt-disallowed `/buy-insurance/` funnel pages | 4 | 92 | 0 | Yes. Keep out |
| Cross-segment 301, Home to Business, holiday home | 1 | 45 | 0 | Yes product-wise, affects attribution only |
| 404 while still earning impressions | 1 | 2 | 0 | **No. Restore** |

Total at stake: 18,816 impressions and 32 clicks. Of the 229 URLs, 223 return 200, 5 return a single-hop 301 and 1 returns 404. No chains, no loops, no homepage redirects.

**The single largest finding.** `/business-insurance/`, the Segment A commercial hub, is absent from all 38 child sitemaps. Verified against the live site: HTTP 200, self-referential canonical, no noindex, robots.txt permits it, 1,073 rendered words. A dedicated `sitemap-business-insurance.xml` holds 5 child URLs but not the hub, which points to a generator fault rather than a deliberate exclusion. The other 14 omissions are `/articles/` index pages at positions 41 to 76, carrying 1,088 impressions between them.

**Hub positions, 28 days.** Measured on the hub URL itself, not the site's aggregate for the query.

| Page | Clicks | Impressions | Position |
|---|---|---|---|
| /business-insurance/ | 2 | 2,645 | 20.6 |
| /home-insurance/ | 9 | 2,919 | **43.2** |
| /group-health-insurance-hic/ | 12 | 8,741 | 33.7 |
| /home-insurance/ for the head term "home insurance" | 0 | 176 | **67.4** |

The Home hub ranks **67.4 for its own head term**. The site's aggregate position for that query is 26.3, which is the child article carrying it. That is the clearest content problem in the account.

**The four intent-mismatch redirects.**

| From | To | Impr | Clicks | Pos | Assessment |
|---|---|---|---|---|---|
| /group-health-insurance/articles/best-group-health-insurance-companies-in-uae/ (8 URL variants) | /group-health-insurance-hic/ | **4,511** | 2 | 47.8 | **Likely wrong.** Comparison intent redirected into a quote form. Position 47.8 is consistent with Google discounting the mismatch |
| /group-life-insurance/articles/group-life-insurance-policy-for-employees/ | /group-life-insurance/ | **3,056** | 5 | **9.7** | **Review urgently.** Still averages position 9.7. Redirecting a page-1 ranker into a hub risks that position |
| /fire-and-allied-perils-insurance/articles/political-violence-insurance/ | /business-insurance/political-violence-insurance/ | 714 | 8 | 46.7 | Correct. Same topic, article to matching product page |
| /home-insurance/articles/compare-home-insurance/ | /home-insurance/ | 20 | 0 | 13.8 | Correct. Transactional intent, hub is the right destination |

**The dead page.** `/home-insurance/news-and-update/` returns 404 while its six child news articles are all live, two of them at positions 9.4 and 9.9 with 2,552 and 150 impressions.

**Hub pages, schema and E-E-A-T.** Word counts are rendered page text.

| Page | HTTP | Rendered words | FAQPage | Product/Offer | Breadcrumb | Rating | Author | Last-updated |
|---|---|---|---|---|---|---|---|---|
| /business-insurance/ | 200 | **1,073** | **missing** | InsuranceAgency only | yes | yes | yes | **missing** |
| /home-insurance/ | 200 | 3,768 | yes | **missing** | yes | yes | yes | yes |
| /group-health-insurance-hic/ | 200 | 3,659 | yes | **missing** | yes | yes | yes | yes |

All three canonicals are self-referential. The Business hub is 3.4 times thinner than both siblings while carrying the segment's highest commercial intent, and is the only one without FAQPage or a modified date.

**Wasted impressions, 90 days.** Queries with 800 or more impressions and no more than 1 click.

| Segment | Queries | Impressions | Largest |
|---|---|---|---|
| A Business | **14** | **15,059** | professional indemnity insurance, 1,465 at position 37; business insurance uae, 1,398 at 28; sme insurance uae, 1,231 at **13.9** |
| B Home | 10 | 15,028 | renters insurance, 3,134 at **position 8**; home insurance, 2,155 at 43 |
| C Group Health | 7 | 11,693 | group medical insurance, 2,940 at 46; group medical insurance uae, 2,251 at 47 |
| **Total** | **31** | **41,780** | |

Segment B carries a brand-query distortion: `policybazaar.ae reviews` accounts for 17,159 of 84,404 segment impressions, 20.3%, at position 8.7. Excluding it, real non-brand CTR is 187 clicks on 67,245 impressions, **0.28%**, against a headline 0.24%. All Segment B CTR targets use the non-brand figure.

Two standouts sit on page 1 already and return almost nothing: `renters insurance` at position 8 on 3,134 impressions, and `sme insurance uae` at position 13.9 on 1,231. Those are title, meta or intent problems rather than ranking problems.

## 1h. AI Overview presence and citation

15 queries on google.ae, 5 per segment.

| Segment | AIO present | PB cited in AIO | PB in organic top 12 |
|---|---|---|---|
| A Business | 4/5 | **2/5** | 2/5 |
| B Home | 5/5 | **3/5** | 5/5 |
| C Group Health | 5/5 | **1/5** | **0/5** |
| **Total** | **14/15 (93%)** | **6/15 (40%)** | 7/15 (47%) |

Domains the AI Overview cites most across the sample: sukoon.com 9× · dni.ae 8× · adnic.ae 7× · livainsurance.ae 6× · omegainsurance.ae 6× · **policybazaar.ae 6×** · giggulf.ae 6× · seveninsurancebrokers.com 5× · unioninsurance.ae 5× · hayah.com 5× · reddit.com 4×.

AI Overviews fire on 93% of these commercial queries. Segment B already ranks in the organic top 12 on all five sampled queries but is cited in only three, so that is a content-format gap rather than a ranking gap. Segment C is cited on one query while ranking in the top 12 on none, so its citation ceiling is set by ranking.

---

## Data gaps and inconsistencies — flagged, not smoothed over

1. **Use the URL-prefix property, not the domain property.** `sc-domain:policybazaar.ae` is missing 95 consecutive days of its own reporting, 5 Oct 2025 to 7 Jan 2026, and understates trailing-year clicks by about 40%. `https://www.policybazaar.ae/` is complete. Every figure in this plan comes from the URL-prefix property. Any dashboard or export still pointed at the domain property is wrong.
2. **Two undiagnosed ranking breaks, neither site-wide.** Each segment lost 5 to 8 positions in the 23 Nov – 20 Dec 2025 bucket and again in the 10 May – 6 Jun 2026 bucket, while site-wide position moved 2.1 and 1.5 and recovered both times. No known migration, replatform, redirect deploy or property change explains either. No cause is attributed in this plan.
3. **What fires `formSubmitSuccess` is unconfirmed.** GA4 records 3,293 events for Segment A over 90 days against 345 CRM leads, roughly ten times. Until analytics confirms the definition, CRM is the sole lead measure and GA4 is baseline context only.
4. **Segment B impressions are 20.3% brand query.** `policybazaar.ae reviews` alone is 17,159 of 84,404 impressions at position 8.7, so headline CTR understates real performance. Non-brand is used throughout.
5. **Semrush and Search Console contradict each other on Segment C.** Semrush places 22 of 33 keywords at 11–20 and the average ranked position at 13.4; Search Console reports 36.8 for the segment and 21 to 32 for the same head terms. The `!aio` filter on the Semrush export, which excludes AI Overview results, is one candidate cause. Reconcile before acting on that pool.
6. **The Semrush export has no usable trend line.** Single-date snapshot, and 26 of 125 keywords show a change equal to `100 − position`, the signature of newly added keywords. Ranking movement is measured as snapshot-to-snapshot top-3 and top-10 counts instead.
7. **GA4 organic sessions exceed Search Console clicks** by 1.29× in A, 1.21× in B and 2.03× in C. GA4 organic includes non-Google engines, and Segment C is further inflated by funnel URLs counted as landing pages.
8. **The manual tracker has no Segment A coverage,** so there is no independent ranking cross-check for the largest segment. Two priority keywords are absent from the Semrush campaign.
9. **`best home insurance in uae` ranks 1 in the manual tracker with zero Search Console impressions in 360 days.** A genuine number one producing no impressions means that exact string carries no measurable demand, so it should be replaced on the priority list.
10. **Distinguish a hub's position from the site's position for a query.** `/home-insurance/` ranks 67.4 for "home insurance"; the site's aggregate for that query is 26.3, carried by the child article. Reporting the aggregate hides the hub problem.
11. **`Total FY-26` in the lead file is not a fiscal year.** It spans April 2025 to June 2026, fifteen months, and excludes July 2026. `Total FY-25` reconciles exactly to April 2024 to March 2025, so the two are not comparable.
12. **No country filter is applied, and applying one is not free.** Filtering or grouping by `country` moves the query onto Google's anonymised query-level dataset, which holds roughly a third of the clicks. The unfiltered figures are retained because they are the only complete dataset. Within the country-resolvable data UAE is 70% to 93% of impressions and 85% to 100% of clicks. A parallel UAE-filtered plan is maintained separately for position reporting.
13. **The AI Overview baseline is a single run and was not issued from a UAE IP.** The `gl=ae` parameter influences results without replicating a Dubai search. Treat 93% presence and 40% citation as directional.
14. **Crawl breadth is not a problem.** Measured like-for-like against the same 28-day window last year, pages earning impressions grew in A and B and held flat in C. Month-1 effort belongs on position and CTR for pages already earning impressions.
15. **Zero-click query counts depend on the export row limit.** The figures above use a 25,000-row pull. A 500-row pull returns 15 queries instead of 31, so any comparison must use the same limit.
16. **Whether undeclared sitemaps exist is unverified.** The audit followed the 38 child sitemaps declared in `sitemap.xml`.

---

# STEP 2 — Month-1 KRAs & KPIs

## Cross-segment foundations

| KRA | KPI | Current Baseline | 1-Month Target | Rationale tied to baseline |
|---|---|---|---|---|
| Retire the broken property | Reporting moved off `sc-domain:policybazaar.ae` | in use | **All reporting on the URL-prefix property** | The domain property is missing 95 days of its own data and understates trailing-year clicks by 40%. Mechanical, week 1 |
| Diagnose the November 2025 break | Root cause documented | unknown | **Written diagnosis** | Each segment lost 5.2 to 8.1 positions in the 23 Nov – 20 Dec bucket while the site lost 2.1 and recovered. Mechanical, week 1 |
| Diagnose the May 2026 break | Root cause documented | unknown | **Written diagnosis** | Each segment lost 6.7 to 7.6 positions in the 10 May – 6 Jun bucket while the site lost 1.5. Mechanical, week 1 |
| Confirm the lead event definition | What fires `formSubmitSuccess` | unknown | **Documented from analytics** | GA4 event volume runs roughly ten times CRM lead volume. Needed before GA4 can serve as a lead measure. Mechanical, week 1 |
| Audit the sitemap generator | Top-level hubs present across all templates | unknown | **Audit complete** | The Business hub was dropped from all 38 child sitemaps. Others outside these segments may be too |
| Reconcile Semrush against Search Console | Divergence explained | 23 places on Segment C | **Documented** | Semrush 13.4 average ranked position against Search Console 36.8. The page-2 targets depend on which source is right. Mechanical, week 1 |

## Segment A — Business / Commercial

| KRA | KPI | Current Baseline | 1-Month Target | Rationale tied to baseline |
|---|---|---|---|---|
| Fix hub indexation | `/business-insurance/` in sitemap | **absent** | **Present and indexed** | Live 200 self-canonical hub earning 2,645 impressions at position 20.6, missing from all 38 child sitemaps. Highest-leverage single fix. Mechanical |
| Recover the hub | `/business-insurance/` position | 20.6 | **≤18** | 2,645 impressions and 2 clicks in 28 days. Stretch |
| Indexation health | Impression-earning URLs missing from sitemap | 13 | **0** | Verified set difference, each URL redirect-checked. Mechanical |
| Schema completeness | Hub schema gaps closed | FAQPage and modified date both missing | **Both live and validated** | The only one of the three hubs without either. Mechanical |
| Content depth | Hub rendered word count | **1,073** | **≥3,500** | Sibling hubs run 3,659 and 3,768 words. This hub is 3.4 times thinner while carrying the highest commercial intent. Stretch |
| Protect redirected equity | Hub position for `group life insurance policy for employees` | old URL at 9.7 | **Hub holds ≤12** | 3,056 impressions at position 9.7 were 301'd into the hub. Confirm it inherited them. Stretch |
| Organic visibility | GSC average position | 26.7 | **22.5** | Trailing-year average is 18.9 and the segment held 9.9 to 10.7 before the November break. Target closes 54% of the 7.8-place gap. Aggressive |
| Click growth | GSC clicks, 28d | 249 | **330, +32.5%** | Trailing-year run rate is 372 and the segment reached 510 to 512 in Jan–Feb. Target recovers 66% of the −33% shortfall. Aggressive |
| CTR improvement | GSC CTR, 28d | 0.50% | **0.66%** | 14 queries hold 15,059 impressions at one click or fewer, including `sme insurance uae` at position 13.9. Trailing-year CTR is 0.59%. Stretch |
| Page-2 conversion | Semrush keywords in top 10 | 22 / 52 | **28 / 52** | 14 keywords sit at 11–20, requiring 6 conversions. Aggressive |
| Head-term expansion | Semrush keywords in top 3 | 11 / 52 | **15 / 52** | The next four must come from adnic at 8 and aig at 6. Aggressive |
| AI Overview citation | PB cited on sampled queries | 2 / 5 | **4 / 5** | AIO fires on 4 of 5 but PB ranks top-12 on only 2, so two wins must come from queries where PB does not yet rank. Aggressive |
| Lead volume | CRM Business Insurance leads per month | 133 | **155, +16.5%** | Trailing-12 average 137, best month 171, so the target sits inside observed capability. Organic is 12.9% of segment sessions, so most must come from conversion-rate work on organic-landed sessions. Aggressive |

## Segment B — Home Insurance

| KRA | KPI | Current Baseline | 1-Month Target | Rationale tied to baseline |
|---|---|---|---|---|
| Resolve hub cannibalization | `/home-insurance/` position for "home insurance" | **67.4** | **≤35** | The hub ranks 67.4 for its own head term while the child article carries the query at 26.3 and takes three of the four Home priority keywords. Largest content problem in the account. Aggressive |
| Recover the hub overall | `/home-insurance/` position, all queries | **43.2** | **≤30** | 2,919 impressions and 9 clicks in 28 days. Aggressive |
| Restore the dead section index | `/home-insurance/news-and-update/` | **404** | **200 listing page** | Dead index above six live children, two ranking at 9.4 and 9.9. Mechanical |
| Indexation health | URLs missing from sitemap | 1 | **0** | `/home-insurance/articles/`. Mechanical |
| Schema completeness | Product/Offer schema on hub | missing | **Live** | Hub carries FAQPage and Rating but no product markup. Mechanical |
| Reporting hygiene | Non-brand CTR view in place | absent | **Live** | One brand query is 20.3% of segment impressions and distorts every CTR reading. Mechanical |
| Organic visibility | GSC average position | 23.3 | **19.5** | Trailing-year average is 16.6 and the segment held 10.5 to 10.6 before the November break. Target closes 57% of the 6.7-place gap. Aggressive |
| Click growth | GSC clicks, 28d | 71 | **125, +76%** | Trailing-year run rate is 178, the largest shortfall of the three at −60%. The segment reached 534 in February and 256 to 269 in Aug–Sep. Target recovers 50% of the shortfall. Aggressive |
| CTR improvement | GSC non-brand CTR, 28d | 0.28% | **0.45%** | 10 queries hold 15,028 impressions at one click or fewer, led by `renters insurance` at position 8 on 3,134 impressions. Trailing-year CTR is 0.53%. Aggressive |
| Page-2 conversion | Semrush keywords in top 10 | 14 / 40 | **22 / 40** | 21 of 40 keywords sit at 11–20, the largest quick-win pool in the account. Requires converting 8 of 21. Aggressive |
| Close the competitor gap | Semrush keywords in top 3 | 4 / 40 | **8 / 40** | giggulf holds 21 and adnic 19 against PB's 4 on an identical keyword set. Aggressive |
| AI Overview citation | PB cited on sampled queries | 3 / 5 | **5 / 5** | AIO fires on all 5 and PB already ranks top-12 on all 5, so the two misses are a content-format gap rather than a ranking gap. Aggressive but genuinely reachable |
| Priority keyword clicks | Combined 28d clicks, keywords 7 to 10 | **2** | **18** | 1,583 impressions converting at 0.13%. `home insurance dubai` alone holds 677 impressions at position 23. Aggressive |
| Priority keyword rankings | Keywords 7, 8 and 9 in GSC top 10 | 0 / 3 | **2 / 3** | All three averaged 16.9 to 19.5 over the trailing year and now sit at 20.5 to 26.3. Aggressive |
| Lead volume | CRM Home Insurance leads per month | 36 | **52, +44%** | Trailing-12 average 69, best month 113, so the target remains 25% below the average. Against −65% year on year this is recovery, not growth. Aggressive |

## Segment C — Group Health

| KRA | KPI | Current Baseline | 1-Month Target | Rationale tied to baseline |
|---|---|---|---|---|
| Resolve the listicle redirect | Decision on `best-group-health-insurance-companies-in-uae` | 301'd to hub, old URL at 47.8 | **Decision made and actioned** | 4,511 impressions across 8 URL variants, redirected from comparison intent into a quote form. Largest redirect decision in the audit. Stretch |
| Recover the hub | `/group-health-insurance-hic/` position, all queries | **33.7** | **≤27** | 8,741 impressions and 12 clicks in 28 days. All six Group Health priority keywords already resolve here, so hub position is the whole story for this segment. Aggressive |
| Indexation health | URLs missing from sitemap | 1 | **0** | `/group-health-insurance/articles/`. Mechanical |
| Schema completeness | Product/Offer schema on hub | missing | **Live** | Hub carries FAQPage but no product markup. Mechanical |
| Close a tracking gap | `medical insurance for company` in Semrush | absent | **Tracked** | 450 search volume, Search Console position 12.0, not in the campaign. Mechanical |
| Organic visibility | GSC average position | 36.8 | **31.0** | Trailing-year average is 26.0 and the segment held 13.9 to 15.3 before the November break. Target closes 54% of the 10.8-place gap, the largest gap of the three, and 32 of 33 Semrush keywords with genuine movement went down. Aggressive |
| Click growth | GSC clicks, 28d | 36 | **58, +61%** | Trailing-year run rate is 65 and the segment reached 107 in January. Target recovers 76% of the −45% shortfall. Note the percentage sits on a small base, +22 clicks. Aggressive |
| CTR improvement | GSC CTR, 28d | 0.14% | **0.23%** | 7 queries hold 11,693 impressions at one click or fewer. Trailing-year CTR is 0.24%, so this target is just under it. Stretch |
| Page-2 conversion | Semrush keywords in top 10 | 8 / 33 | **14 / 33** | 22 of 33 keywords sit at 11–20 per Semrush, but Search Console places the segment at 36.8. Contingent on the reconciliation in the foundations table. Aggressive |
| Close the competitor gap | Semrush keywords in top 10 | PB 8 vs adnic 24 | **PB 14** | Same 33-keyword set: adnic 24, giggulf 21, PB 8. Aggressive |
| AI Overview citation | PB cited on sampled queries | 1 / 5 | **3 / 5** | AIO fires on all 5 but PB ranks top-12 on none, so citation upside is capped until rankings move. Highest-risk KPI in the plan |
| Priority keyword clicks | Combined 28d clicks, keywords 1 to 6 | **3** | **22** | 1,407 impressions at 0.21%. `group medical insurance` at 497 impressions and `group health insurance` at 448 carry it. Aggressive |
| Priority keyword rankings | Keywords 1 to 6 in GSC top 20 | 1 / 6 | **5 / 6** | Five of six averaged 8.4 to 19.2 over the trailing year and all now sit at 21.0 to 32.4. Aggressive |
| Lead volume | CRM Group Health leads per month | 16 | **26, +63%** | Trailing-12 average 32, best month 45, so the target remains below the average. Against −63% year on year this is recovery. Aggressive |

## Month-1 rolled-up summary

| KRA | KPI | Current Baseline | 1-Month Target | Rationale tied to baseline |
|---|---|---|---|---|
| Organic visibility | Blended average position, impression-weighted | 28.3 | **23.8** | Trailing-year blended average is 19.8. Target closes 53% of the 8.5-place gap. Aggressive |
| Click growth | GSC clicks, 3 segments, 28d | 356 | **513, +44%** | A 330, B 125, C 58. Trailing-year run rate is 615, so this recovers 61% of the aggregate shortfall. Aggressive |
| Impression growth | GSC impressions, 28d | 103,318 | **≥112,000** | Trailing-year run rate is 124,034. Target recovers 42% of that gap, driven by the hub sitemap fix and the dead-page restoration rather than new content. Stretch |
| CTR improvement | GSC CTR, 3 segments, 28d | 0.34% | **0.50%** | 31 queries across the three segments hold 41,780 impressions at one click or fewer. Trailing-year CTR is 0.50%, so this is a return to it. Aggressive |
| **Priority keyword clicks** | Combined 28d clicks, 10 keywords | **5** | **40** | B contributes 18 and C contributes 22. Nine of ten averaged better than position 20 over the trailing year. Aggressive |
| **Priority keyword coverage** | Keywords with at least 1 click | **3 / 10** | **8 / 10** | Seven of ten currently produce nothing at all. Aggressive |
| **Priority keyword rankings** | Keywords in GSC top 10 | **0 / 10** | **4 / 10** | Same basis. Aggressive |
| **Priority keyword rankings** | Keywords in GSC top 20 | **1 / 10** | **7 / 10** | Same basis. Aggressive |
| Hub recovery | Three hubs at or better than target position | 0 / 3 | **3 / 3** | Business 20.6, Home 43.2, Group Health 33.7. Targets ≤18, ≤30, ≤27. Aggressive |
| Ranking distribution | Semrush keywords in top 10, of 125 | 44 | **64** | 57 of 125 tracked keywords sit at 11–20. Aggressive |
| Ranking distribution | Semrush keywords in top 3, of 125 | 18 | **29** | Widest competitor gap is Segment B, where PB holds 4 against giggulf's 21. Aggressive |
| Indexation and crawl health | Impression-earning URLs missing from sitemap | **15** | **0** | Includes the `/business-insurance/` hub. Mechanical |
| Indexation and crawl health | Dead URLs still earning impressions | 1 | **0** | `/home-insurance/news-and-update/`. Mechanical |
| Redirect quality | Intent-mismatch redirects resolved | 0 / 4 | **4 / 4** | 8,301 impressions and 15 clicks sit behind these four decisions. Stretch |
| Schema completeness | Hubs with a complete schema set | 0 / 3 | **3 / 3** | Business missing FAQPage; Home and Group Health missing Product or Offer. Mechanical |
| Content freshness and E-E-A-T | Hubs with a modified date | 2 / 3 | **3 / 3** | `/business-insurance/` has none. Mechanical |
| Measurement integrity | Reporting property corrected | domain property in use | **URL-prefix only** | The domain property is missing 95 days of its own data. Mechanical |
| Measurement integrity | Ranking breaks root-caused | 0 / 2 | **2 / 2** | November 2025 and May 2026, neither site-wide, neither explained. Mechanical |
| AI Overview citation | PB cited across 15 sampled queries | 6 / 15, 40% | **12 / 15, 80%** | AIO fires on 93% of these queries. PB ranks top-12 on 7 of 15, so five of the six gains must come from queries where PB does not yet rank. Aggressive |
| Lead volume | CRM leads per month, 3 products | 185 | **233, +26%** | A 155, B 52, C 26. Trailing-12 average is 238, so the target stays inside observed capability. Aggressive |

---

# STEP 3 — Weekly breakdown

Technical and diagnostic work is front-loaded into weeks 1 and 2. Ranking and lead movement is loaded into weeks 3 and 4, because search impact lags implementation. Week 1 targets a small click dip, 84 against an 89 per week baseline, because hub re-targeting and canonical changes cause short-term churn. A flat or slightly down week 1 is the plan working.

## Segment A — Business / Commercial (weekly)

| Week | Work being done | KPI checkpoint (cumulative unless noted) |
|---|---|---|
| **W1** 5–11 Aug | Move all reporting off the domain property. Add `/business-insurance/` to `sitemap-business-insurance.xml` and fix the generator that dropped it. Lead the November 2025 and May 2026 break diagnoses: change log, deploy history, log-file crawl audit for both windows. Submit the 13-URL sitemap patch. Author FAQPage and modified-date JSON-LD. Rewrite titles and metas for the 14 zero-click queries holding 15,059 impressions, starting with `sme insurance uae` at position 13.9 | Clicks 58, dip expected. Position 26.7, unchanged. Hub in sitemap and submitted for indexing. Reporting property corrected. Both break diagnoses documented |
| **W2** 12–18 Aug | Deploy FAQPage and modified date. Expand the hub from 1,073 to 3,500 rendered words. Ship the rewritten titles and metas. Internal links from `/commercial-motor/articles/` and `/workers-compensation/articles/` into the money pages. Verify the hub inherited position 9.7 from the redirected group-life article | Clicks 130. CTR 0.55%. Position 25.8. Schema validating in Rich Results Test. Hub at 3,500 words or more. Hub position ≤19.5 |
| **W3** 19–25 Aug | Convert the 14 page-2 Semrush keywords, prioritising `public liability insurance` at 13, `contractor all risk insurance` at 11, `business interruption insurance` at 17 and `commercial vehicle insurance` at 14. Add answer-first blocks for the 3 uncited AI Overview queries. Re-run the AIO sample | Clicks 222. CTR 0.61%. Position 24.0. Semrush top 10 at 25/52, top 3 at 13/52. AIO 3/5. Hub ≤18.5 |
| **W4** 26 Aug–1 Sep | Push `workmen compensation insurance` at 10 and `professional indemnity insurance` at 21 into the top 3. Conversion-rate review of organic-landed sessions | **Clicks 330. CTR 0.66%. Position 22.5. Top 10 at 28/52. Top 3 at 15/52. AIO 4/5. Hub ≤18. CRM leads 155** |

## Segment B — Home Insurance (weekly)

| Week | Work being done | KPI checkpoint (cumulative unless noted) |
|---|---|---|
| **W1** 5–11 Aug | Sign off the cannibalization decision: the hub ranks 67.4 for "home insurance" while the child article carries the query at 26.3 and takes three of the four Home priority keywords. Restore `/home-insurance/news-and-update/` from 404 to a listing page above its six live children. Add `/home-insurance/articles/` to the sitemap. Author Product/Offer JSON-LD. Stand up non-brand CTR reporting. Diagnose `renters insurance`, 3,134 impressions at position 8 returning one click | Clicks 17, dip expected. Position 23.3, unchanged. Hub 67.4 and 43.2, unchanged. News index returns 200. Non-brand CTR baseline locked at 0.28% |
| **W2** 12–18 Aug | Execute the hub fix: re-target the hub to `home insurance`, `home insurance dubai` and `home insurance uae`; re-scope the article to comparison intent; re-point internal anchors from article to hub. Deploy Product/Offer schema. Rewrite titles and metas for the 10 zero-click queries holding 15,028 impressions | Clicks 43. Non-brand CTR 0.33%. Position 22.4. Hub head-term ≤55. Hub all queries ≤38. Priority keywords 7 to 9 in top 20 at 1/3 |
| **W3** 19–25 Aug | Work the 21-keyword Semrush page-2 pool, prioritising `home contents insurance dubai` at 13 with 1,600 search volume, `home insurance abu dhabi` at 11 and `house insurance` at 16. Add answer-first blocks for `building insurance dubai` and `renters insurance dubai`, both AIO-present with PB uncited but already ranking top 12. Re-run the AIO sample | Clicks 80. Non-brand CTR 0.39%. Position 20.8. Hub head-term ≤45. Hub all queries ≤34. Top 10 at 18/40, top 3 at 6/40. AIO 4/5. Priority keyword clicks 9 |
| **W4** 26 Aug–1 Sep | Close the top-3 gap against giggulf and adnic on the four highest-volume terms. Confirm the hub, not the article, is the ranking URL for head terms | **Clicks 125. Non-brand CTR 0.45%. Position 19.5. Hub head-term ≤35. Hub all queries ≤30. Top 10 at 22/40. Top 3 at 8/40. AIO 5/5. Priority keyword clicks 18. CRM leads 52** |

## Segment C — Group Health (weekly)

| Week | Work being done | KPI checkpoint (cumulative unless noted) |
|---|---|---|
| **W1** 5–11 Aug | Reconcile Semrush against Search Console, a 23-place divergence on this segment. Decide whether to reverse the `best-group-health-insurance-companies-in-uae` redirect carrying 4,511 impressions. Add `/group-health-insurance/articles/` to the sitemap. Author Product/Offer JSON-LD. Add `medical insurance for company` to the Semrush campaign | Clicks 9. Position 36.8, unchanged. Hub 33.7, unchanged. Divergence documented. Redirect decision signed off. Semrush campaign updated |
| **W2** 12–18 Aug | If reversing, rebuild the comparison page and remove the 301. Deploy Product/Offer schema. Rewrite titles and metas for the 7 zero-click queries holding 11,693 impressions, starting with `group medical insurance` at 2,940 impressions and position 46 | Clicks 21. CTR 0.16%. Position 35.5. Hub ≤31. Priority keywords 1 to 6 in top 20 at 2/6 |
| **W3** 19–25 Aug | Depth work on the four highest-volume terms: `group insurance health` at 18, `group medical insurance` at 15, `group health insurance` at 16 and `group health coverage` at 19. Add answer-first blocks for `corporate health insurance uae` and `employee medical insurance uae`. Re-run the AIO sample | Clicks 38. CTR 0.20%. Position 33.0. Hub ≤29. Semrush top 10 at 11/33. AIO 2/5. Priority keywords 1 to 6 in top 20 at 4/6. Priority keyword clicks 11 |
| **W4** 26 Aug–1 Sep | Begin closing the adnic gap, PB 8 against adnic 24 in the top 10, on the highest-volume cluster | **Clicks 58. CTR 0.23%. Position 31.0. Hub ≤27. Top 10 at 14/33. AIO 3/5. Priority keywords 1 to 6 in top 20 at 5/6. Priority keyword clicks 22. CRM leads 26** |

## Weekly rolled-up summary

| KPI | Baseline | W1 (5–11 Aug) | W2 (12–18 Aug) | W3 (19–25 Aug) | W4 (26 Aug–1 Sep) |
|---|---|---|---|---|---|
| Clicks, weekly | 89 per week | **84**, −6% dip | 110 | 146 | **173** |
| Clicks, cumulative | 356 in 28d | 84 | 194 | 340 | **513** |
| CTR, 3 segments | 0.34% | 0.34% | 0.39% | 0.45% | **0.50%** |
| Blended average position | 28.3 | 28.3 | 27.2 | 25.5 | **23.8** |
| `/home-insurance/` head-term position | 67.4 | 67.4 | ≤55 | ≤45 | **≤35** |
| `/home-insurance/` position, all queries | 43.2 | 43.2 | ≤38 | ≤34 | **≤30** |
| `/business-insurance/` position | 20.6 | 20.6 | ≤19.5 | ≤18.5 | **≤18** |
| `/group-health-insurance-hic/` position | 33.7 | 33.7 | ≤31 | ≤29 | **≤27** |
| `/business-insurance/` in sitemap | absent | **present** | present | present | **indexed** |
| Reporting on the correct property | no | **yes** | yes | yes | yes |
| URLs missing from sitemap | 15 | **0 submitted** | 0 | 0 | **0 indexed** |
| Dead URLs earning impressions | 1 | **0** | 0 | 0 | **0** |
| Intent-mismatch redirects resolved | 0 / 4 | **4 / 4 decided** | 4 / 4 actioned | 4 / 4 | **4 / 4 verified** |
| Hubs with complete schema | 0 / 3 | 0 / 3, specs written | **3 / 3 deployed** | 3 / 3 validated | 3 / 3 |
| Business hub rendered words | 1,073 | 1,073 | **≥3,500** | ≥3,500 | ≥3,500 |
| Measurement fixes shipped | 0 / 6 | **6 / 6** | 6 / 6 | 6 / 6 | 6 / 6 |
| Priority keyword clicks, cumulative | 5 in 28d | 1 | 7 | 20 | **40** |
| Priority keywords with 1 or more clicks | 3 / 10 | 3 / 10 | 5 / 10 | 6 / 10 | **8 / 10** |
| Priority keywords in GSC top 20 | 1 / 10 | 1 / 10 | 3 / 10 | 5 / 10 | **7 / 10** |
| Priority keywords in GSC top 10 | 0 / 10 | 0 / 10 | 1 / 10 | 2 / 10 | **4 / 10** |
| Semrush top 10, of 125 | 44 | 44 | 46 | 54 | **64** |
| Semrush top 3, of 125 | 18 | 18 | 19 | 23 | **29** |
| AI Overview citation, 15 queries | 6 / 15 | 6 / 15 | 6 / 15 | 9 / 15 | **12 / 15** |
| CRM leads, cumulative | 185 per month | 49 | 104 | 166 | **233** |

**Click ladder by segment.**

| Segment | Baseline 28d | W1 | W2 | W3 | W4 | Month target |
|---|---|---|---|---|---|---|
| A Business | 249 | 58 | 72 | 92 | 108 | **330** |
| B Home | 71 | 17 | 26 | 37 | 45 | **125** |
| C Group Health | 36 | 9 | 12 | 17 | 20 | **58** |
| **Total** | **356** | **84** | **110** | **146** | **173** | **513** |

**Lead ladder by segment, CRM.**

| Segment | Baseline per month | W1 | W2 | W3 | W4 | Month target |
|---|---|---|---|---|---|---|
| A Business Insurance | 133 | 34 | 37 | 41 | 43 | **155** |
| B Home Insurance | 36 | 10 | 12 | 14 | 16 | **52** |
| C Group Health | 16 | 5 | 6 | 7 | 8 | **26** |
| **Total** | **185** | **49** | **55** | **62** | **67** | **233** |

---

## Key risks and assumptions

- **The decline is segment-specific, not site-wide.** Each segment lost 5 to 8 positions in November 2025 and again in May 2026, while site-wide position moved 2.1 and 1.5 and recovered both times. There is no site-wide explanation available, so the targets cannot be argued down on that basis.
- **Both breaks are undiagnosed.** No known migration, replatform, redirect deploy or property change explains either. Every position target assumes whatever happened is either reversible or already spent. Week 1's diagnosis may force a revision.
- **Reporting has been on the wrong Search Console property.** The domain property is missing 95 days of its own data and understates trailing-year clicks by roughly 40%. Any dashboard, alert or export still pointed at it will disagree with this plan. Fixing that is a week 1 deliverable.
- **CRM is the only lead measure.** GA4 organic key events are not carried as a KPI because what fires `formSubmitSuccess` is unconfirmed and the event count runs roughly ten times CRM volume. GA4 remains in the baseline for organic share and engagement context. If the definition is confirmed in week 1, an organic-attributed conversion KPI can be added mid-month.
- **These are stretch targets and some will be missed.** Highest risk, in order: Segment C AI Overview citation at 3/5 when PB ranks top-12 on none of the sampled queries; the Home hub moving from 67.4 to 35 for its own head term inside a month; Segment C position 31.0 when 32 of 33 Semrush keywords with genuine movement went down; and the 12/15 rollup AIO rate. Those four are where to negotiate if a landable plan is preferred to a stretch one.
- **Two redirect reversals carry downside.** `group-life-insurance-policy-for-employees` still averages position 9.7 on 3,056 impressions, and the Group Health listicle holds 4,511 impressions across 8 URL variants. Reversing a 301 costs re-indexing time and can lose equity already consolidated. Decide in week 1, measure in week 4, and be prepared to leave one alone.
- **Lead targets require conversion-rate work, not only SEO.** Organic is 12.9% of Segment A sessions, 33.1% of B and 8.6% of C. A 26% rollup lead increase cannot come from ranking gains alone in 28 days. Segment B is the only one where organic share is high enough to carry it on traffic alone.
- **Segment C percentage targets sit on small absolute numbers.** A 61% click increase is 22 clicks. Judge that segment on position, hub recovery and priority-keyword rankings rather than click percentage.
- **Segment B CTR must be reported non-brand.** One brand query is 20.3% of segment impressions at position 8.7, so including it makes both the baseline and any improvement misleading.
- **Two page-1 rankings return almost nothing.** `renters insurance` at position 8 on 3,134 impressions and `sme insurance uae` at position 13.9 on 1,231. Those are title, meta or intent mismatches, and they are the cheapest CTR wins in the plan.
- **February may not be a fair reference peak for Segment B.** It reached 534 clicks in February against 71 now, in a segment where rain-damage and fire news pages rank well. If February was event-driven, the run-rate benchmark and the 125-click target are both generous.
- **Semrush and Search Console are not directly comparable.** The Semrush export excludes AI Overview results while Search Console includes them, and the two disagree by 23 places on Segment C. Reconcile before acting on that keyword pool.
- **The missing hub may be a symptom rather than the whole fault.** A sitemap generator that drops a top-level hub may be dropping others outside these three segments, hence the generator audit.
- **The 12 `/articles/` listing pages need a decision, not a default.** They sit at positions 41 to 76. Adding them to the sitemap and applying noindex are both defensible; leaving them live but invisible is not.
- **The AI Overview baseline is a single run and was not issued from a UAE IP.** Consider re-capturing from a UAE IP before it becomes a reported KPI.
- **Weekly figures are an allocation, not a forecast.** The splits reflect the expected shape of a lagging metric and were set to sum to the month target. They are the most adjustable numbers in the plan.
- **Crawl breadth is not a problem.** Like-for-like against the same 28-day window last year, pages earning impressions grew in A and B and held flat in C. Month-1 effort belongs on position and CTR for pages already earning impressions.
- **`best home insurance in uae` should be replaced on the priority list.** It ranks 1 in the manual tracker with zero Search Console impressions in 360 days, so that exact string carries no measurable demand.

**Decisions needed from the business:** what happened in November 2025 and again in May 2026; what fires `formSubmitSuccess`; whether Semrush or Search Console is right on Segment C; whether to reverse the Group Health listicle redirect; sitemap or noindex for the 12 `/articles/` pages; whether to replace `best home insurance in uae`; whether February was an event-driven spike for Home; and whether to re-capture the AI Overview baseline from a UAE IP.

---

*A parallel UAE-filtered version of this plan is maintained as `seo-aio-kra-kpi-uae-filtered-2026-08-04.md`. Positions are comparable between the two documents; clicks and CTR are not, because a country filter moves Search Console onto its anonymised dataset.*
