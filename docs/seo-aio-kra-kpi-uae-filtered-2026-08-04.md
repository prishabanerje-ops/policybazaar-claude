# SEO + AIO KRA/KPI Plan — UAE-filtered view

**Domain:** policybazaar.ae · **Month 1:** 5 August – 1 September 2026 · **Prepared:** 4 August 2026
**Search Console property:** `https://www.policybazaar.ae/` · **Country filter:** United Arab Emirates
**Companion to:** `seo-aio-kra-kpi-2026-08-04.md`, which uses the same property unfiltered

> **Do not compare click or CTR figures between this document and the unfiltered version.**
> A country filter moves Search Console onto its anonymised query-level dataset, which holds
> roughly a third of the clicks. Every number here is internally consistent and valid for
> month-on-month UAE tracking, but absolute clicks and CTR are understated against reality.
> **Positions are comparable across both documents.** See Data notes.

> Figures restated on the URL-prefix property. An earlier draft used the domain property `sc-domain:policybazaar.ae`, which has a 95-day hole in its own reporting from 5 Oct 2025 to 7 Jan 2026. That hole produced a false "October 2025 break" and a false homepage-targeting finding, both corrected here.

---

## Why this version exists, and what it shows

Site-wide UAE position was 15.5 a year ago and is 10.6 now. **The site improved.** The three segments went the other way, and they did it in two discrete steps.

| Position deterioration, bucket over bucket | A Business | B Home | C Group Health | Site-wide |
|---|---|---|---|---|
| **23 Nov – 20 Dec 2025** | **+5.8** | **+7.2** | **+8.7** | +1.9 |
| **10 May – 6 Jun 2026** | **+5.7** | **+11.4** | **+7.4** | +1.2 |

Three consequences:

1. **The decline is segment-specific, not site-wide.** Site-wide UAE position recovered after both events. The segments did not. Segment A went from 8.8 to 28.9 while the site went from 9.1 to 10.6.
2. **There are two breaks, in November 2025 and May 2026.** Each cost the segments 5 to 11 places. Neither is explained.
3. **Positions are markedly worse on UAE data than blended**, and the divergence is largest where it matters most: `/home-insurance/` ranks 68.0 in the UAE for its own head term.

---

## Data source status

| Source | Status | How it was obtained |
|---|---|---|
| Google Search Console | Live, **country = United Arab Emirates** | Property `https://www.policybazaar.ae/`, `page` regex plus `country equals are` |
| GA4 | Live, **countryId = AE** | Property `309894472`, `landingPagePlusQueryString` regex plus country filter |
| Semrush ranking export | Parsed, unchanged | UAE campaign already, so identical to the unfiltered version |
| Manual ranking tracker | Parsed, unchanged | 10 in-scope keywords, current to 4 Aug |
| Lead data (CRM) | Parsed, unchanged | UAE business by definition |
| AI Overview / GEO | Measured, unchanged | 15 queries on google.ae |
| Sitemap and redirect audit | Measured, unchanged | URL-level findings do not depend on country |

**Windows:** 360-day = 2025-08-07 → 2026-08-01 · 90-day = 2026-05-04 → 2026-08-01 · 28-day = 2026-07-05 → 2026-08-01. All 360 days carry data on this property.

---

# STEP 1 — Baseline, UAE only

## 1a. Google Search Console

| Metric | A Business | B Home | C Group Health | Site-wide |
|---|---|---|---|---|
| **360d clicks** | 1,471 | 644 | 242 | 364,535 |
| 360d impressions | 402,667 | 205,861 | 219,676 | 30,707,003 |
| 360d CTR | 0.37% | 0.31% | 0.11% | 1.19% |
| **360d avg position** | **19.4** | **19.4** | **30.0** | 10.4 |
| 360d pages earning impressions | 185 | 101 | 31 | — |
| 90d clicks | 199 | 50 | 30 | 58,485 |
| 90d impressions | 89,309 | 46,345 | 55,059 | 5,922,578 |
| 90d CTR | 0.22% | 0.11% | 0.05% | 0.99% |
| 90d avg position | 29.1 | 29.2 | 41.5 | 10.8 |
| **28d clicks** | **64** | **23** | **15** | 16,803 |
| **28d impressions** | **28,748** | **15,519** | **20,051** | 1,760,814 |
| **28d CTR** | **0.22%** | **0.15%** | **0.07%** | 0.95% |
| **28d avg position** | **28.9** | **31.0** | **41.6** | 10.6 |
| 28d pages earning impressions | 128 | 65 | 17 | — |

Rollup for the three segments, 28 days: **102 clicks, 64,318 impressions, 0.16% CTR, blended impression-weighted position 33.4.** Over 360 days: 2,357 clicks, 828,204 impressions, 0.28% CTR, blended position 22.2.

UAE share of the country-resolvable data: 81.2% of Segment A impressions, 70.0% of B, 92.8% of C.

**The gap to the trailing-year UAE run rate.** 360-day figures divided by 360 and multiplied by 28.

| Segment | Trailing-year 28d run rate | Actual last 28d | Shortfall | 360d position | Current | Gap |
|---|---|---|---|---|---|---|
| A Business | 114 clicks / 31,319 impr | 64 / 28,748 | **−44%** | 19.4 | 28.9 | −9.5 |
| B Home | 50 clicks / 16,011 impr | 23 / 15,519 | **−54%** | 19.4 | 31.0 | −11.6 |
| C Group Health | 19 clicks / 17,086 impr | 15 / 20,051 | **−21%** | 30.0 | 41.6 | −11.6 |
| **Rollup** | **183 clicks / 64,416 impr** | **102 / 64,318** | **−44%** | **22.2** | **33.4** | **−11.2** |

Two things this view shows that the unfiltered one does not. Segment C's click shortfall is only 21% because almost all its impressions were always UAE, yet its position gap of 11.6 places is joint-worst, so it is a position problem rather than a volume problem. And UAE impressions are already at the trailing-year run rate, 64,318 against 64,416, so impression growth cannot come from recovery alone.

## 1b. Twelve-month trend, 28-day buckets, UAE only

| Bucket start | A clicks / pos | B clicks / pos | C clicks / pos | Site-wide clicks / pos |
|---|---|---|---|---|
| 03 Aug 25 | 159 / 10.8 | 65 / 18.5 | 20 / 18.8 | 40,917 / 15.5 |
| 31 Aug 25 | 138 / 9.1 | 57 / 13.7 | 17 / 18.0 | 35,926 / 11.8 |
| 28 Sep 25 | 151 / **8.8** | 54 / 11.6 | 21 / **16.9** | 36,082 / 9.1 |
| 26 Oct 25 | 128 / 10.2 | 36 / **11.2** | 20 / 19.4 | 30,124 / **8.6** |
| **23 Nov 25** | **105 / 16.0** | **48 / 18.4** | **16 / 28.1** | 25,869 / 10.5 |
| 21 Dec 25 | 142 / 20.8 | 40 / 20.7 | 20 / 28.1 | 29,910 / 11.1 |
| 18 Jan 26 | 154 / 26.3 | 39 / 20.7 | 36 / 29.2 | 32,610 / 10.8 |
| 15 Feb 26 | 148 / 22.2 | **212** / 15.1 | 28 / 26.5 | 39,823 / 8.8 |
| 15 Mar 26 | 86 / 21.8 | 32 / 17.9 | 27 / 30.5 | 23,885 / **8.5** |
| 12 Apr 26 | 109 / 23.8 | 27 / 18.3 | 11 / 33.0 | 21,890 / 10.0 |
| **10 May 26** | **60 / 29.5** | **10 / 29.7** | **7 / 40.4** | 18,113 / 11.2 |
| 07 Jun 26 | 59 / 29.8 | 10 / 28.0 | 7 / 43.6 | 18,802 / 10.8 |
| 05 Jul 26 | 64 / 28.9 | 23 / 31.0 | 15 / 41.6 | 16,803 / 10.6 |
| **Trailing-year best** | **159 / 8.8** | **212 / 11.2** | **36 / 16.9** | 40,917 / 8.5 |

Two breaks, in the November 2025 and May 2026 buckets. Segment A degrades a third time between December and January, from 20.8 to 26.3, then partially recovers. Site-wide never loses more than 1.9 places in a single bucket and recovers each time.

## 1c. GA4, UAE only

| Metric | A Business | B Home | C Group Health |
|---|---|---|---|
| 360d sessions, all channels | 28,923 | 4,489 | 8,925 |
| **360d sessions, organic** | **3,585** | **1,826** | **574** |
| **Organic share of segment** | 12.4% | **40.7%** | 6.4% |
| 360d engaged sessions, organic | 2,379 | 1,169 | 450 |
| 360d key events, organic | 1,071 | 376 | 213 |
| Key events per session, organic | 29.9% | 20.6% | 37.1% |
| 90d organic sessions / key events | 584 / 207 | 146 / 41 | 66 / 25 |
| **28d organic sessions / key events** | **191 / 63** | **52 / 14** | **27 / 6** |
| 28d organic share of segment | 6.4% | **43.3%** | 5.1% |

Home Insurance is even more organic-dependent in the UAE than the blended view suggested, at **40.7% of sessions over 360 days and 43.3% over the last 28**, against 33.1% blended. It remains the clearest route from ranking recovery to leads.

## 1d. Semrush ranking export

Unchanged from the unfiltered version. The Semrush campaign already tracks UAE SERPs against UAE competitors.

| Metric | A Business | B Home | C Group Health |
|---|---|---|---|
| Tracked keywords | 52 | 40 | 33 |
| Top 3 | 11 | 4 | 3 |
| Top 10 | 22 | 14 | 8 |
| **Positions 11–20, the quick-win pool** | **14** | **21** | **22** |
| Above 50 or not ranking | 5 | 1 | 0 |
| Average position of ranked keywords | 15.0 | 12.5 | 13.4 |

Competitor top-10 count on the identical keyword set: Segment A — PB 22, giggulf 21, adnic 16, aig 10. Segment B — adnic 29, giggulf 29, PB 14. Segment C — adnic 24, giggulf 21, PB 8.

Direction of movement, excluding 26 artefact rows: Segment A 9 up against 36 down, Segment B 2 up against 10 down, Segment C 1 up against **32 down**.

**Semrush disagrees with Search Console far more sharply in this view.** Semrush places Segment C's average ranked position at 13.4 while UAE Search Console reports 41.6, a 28-place divergence on the same market. Reconciling it matters more here than in the unfiltered plan.

## 1e. Priority keywords, UAE only

| # | Keyword | 360d impr | 360d clicks | 360d pos | 28d impr | 28d clicks | 28d pos | UAE ranking URL |
|---|---|---|---|---|---|---|---|---|
| 1 | medical insurance for company | 383 | 2 | 23.0 | 24 | 0 | **12.8** | /group-health-insurance-hic/ |
| 2 | group medical insurance | 5,933 | 10 | 17.6 | 491 | 0 | 26.8 | /group-health-insurance-hic/ |
| 3 | group health insurance uae | 4,070 | 0 | 19.5 | 376 | 0 | 21.2 | /group-health-insurance-hic/ |
| 4 | group medical coverage | 612 | 1 | 13.6 | 31 | 0 | 26.5 | /group-health-insurance-hic/ |
| 5 | group health coverage | 897 | 2 | 8.6 | 64 | 0 | 23.1 | /group-health-insurance-hic/ |
| 6 | group health insurance | 4,827 | 31 | 13.0 | 441 | **3** | 20.9 | /group-health-insurance-hic/ |
| 7 | home insurance uae | 3,102 | 7 | 20.3 | 320 | 0 | 20.8 | /home-insurance/articles/best-… |
| 8 | home insurance | 7,710 | 34 | 16.6 | 541 | **1** | 25.6 | /home-insurance/articles/best-… |
| 9 | home insurance dubai | 7,121 | 30 | 17.9 | 598 | 0 | 24.5 | /home-insurance/articles/best-… |
| 10 | best home insurance in uae | 5 | 0 | **1.0** | 0 | 0 | — | /home-insurance/articles/best-… |
| | **Total** | **34,660** | **117** | | **2,886** | **4** | | |

| Priority-keyword position | Current, 28d UAE |
|---|---|
| Total clicks | **4** |
| Total impressions | 2,886 |
| Blended CTR | 0.14% |
| Keywords with at least 1 click | **2 / 10** |
| Keywords in top 10 | **0 / 10** |
| Keywords in top 20 | **1 / 10** |
| Keywords with zero impressions | **1 / 10** |
| Segment C subset, #1–6 | 3 clicks on 1,427 impressions |
| Segment B subset, #7–10 | 1 click on 1,459 impressions |

Two findings this cut surfaces:

- **All four Home priority keywords resolve to the child article, not the hub.** In the unfiltered view `home insurance` still resolves to `/home-insurance/`; in the UAE it does not. The article has taken the entire Home head-term set in this market.
- **`best home insurance in uae` does have UAE demand, and PB genuinely ranks 1.0 for it.** Five impressions across 360 days. The manual tracker's number one is real and the volume is negligible, which settles whether to keep it on the list.

All six Group Health priority keywords resolve to the `/group-health-insurance-hic/` hub, so there is no hub-versus-article conflict on that half of the list.

## 1f. Lead data (CRM)

Unchanged. Column 4 of the source file is Group Health.

| Metric | A Business Insurance | B Home Insurance | C Group Health |
|---|---|---|---|
| Jul'2026, last full month | 133 | 36 | 16 |
| 3-month monthly average | 115.0 | 37.3 | 17.7 |
| **Year on year, July** | **+33%** | **−65%** | **−63%** |
| Trailing 12 months | 1,644 | 833 | 384 |
| Trailing-12 monthly average | 137.0 | 69.4 | 32.0 |
| Trailing-12 best month | 171 (Oct'25) | 113 (Mar'26) | 45 (Sep'25) |

Rollup: 185 leads in July 2026 against a trailing-12 monthly average of 238.

## 1g. Technical, indexation and redirects

URL-level findings do not change under a country filter. Restated with UAE impression figures.

| Check | A Business | B Home | C Group Health | Total |
|---|---|---|---|---|
| URLs in sitemap | 134 | 56 | 18 | 208 |
| Distinct URLs earning impressions, unfiltered | 150 | 60 | 19 | 229 |
| **Earning impressions but missing from sitemap** | **19** | **4** | **2** | **25** |

| Finding | URLs | Action |
|---|---|---|
| Live 200, self-canonical, crawlable, simply absent | **15** | **Add to sitemap** |
| Article 301'd to a commercial hub, intent mismatch | 4 | **Review, two are questionable** |
| robots.txt-disallowed `/buy-insurance/` funnel pages | 4 | Correctly excluded, keep out |
| Cross-segment 301, Home to Business | 1 | Correct product-wise |
| 404 while still earning impressions | 1 | **Restore** |

**`/business-insurance/` is absent from all 38 child sitemaps.** In UAE data over 28 days it earns **2,068 impressions at position 21.3** with 1 click. HTTP 200, self-referential canonical, no noindex, robots.txt permits it, 1,073 rendered words. A dedicated `sitemap-business-insurance.xml` holds 5 child URLs but not the hub.

**UAE hub positions, 28 days.** Measured on the hub URL itself. These are worse than the blended figures and make the cannibalization case stronger.

| Page | UAE clicks | UAE impressions | UAE position | Unfiltered for comparison |
|---|---|---|---|---|
| /business-insurance/ | 1 | 2,068 | 21.3 | 20.6 |
| /home-insurance/ | 0 | 2,270 | **50.3** | 43.2 |
| /group-health-insurance-hic/ | 5 | 6,948 | 38.4 | 33.7 |
| /home-insurance/ for "home insurance" | 0 | 173 | **68.0** | 67.4 |

The Home hub ranks **68.0 in the UAE for its own head term** while its child article carries every Home priority keyword. That is the single largest content problem in this view.

**The dead page.** `/home-insurance/news-and-update/` returns 404 while its six child news articles are all live.

**Hub schema and depth**, unchanged: `/business-insurance/` has 1,073 rendered words with no FAQPage and no modified date. `/home-insurance/` has 3,768 and `/group-health-insurance-hic/` 3,659, both with FAQPage but no Product or Offer markup.

## 1h. Wasted impressions, UAE, 90 days

Queries with 800 or more impressions and no more than 1 click.

| Segment | Queries | Impressions | Largest |
|---|---|---|---|
| A Business | 9 | 9,552 | professional indemnity insurance, 1,456 at position 37; group life insurance uae, 1,277 at 27 |
| B Home | **9** | **13,935** | renters insurance, 3,124 at **position 8**; home insurance, 2,110 at 44 |
| C Group Health | 5 | 9,556 | group medical insurance, 2,875 at 46; group medical insurance uae, 2,198 at 48 |
| **Total** | **23** | **33,043** | |

**The brand-query distortion largely disappears in the UAE view.** `policybazaar.ae reviews` is only **1,974 impressions, 4.3% of Segment B**, against 20.3% blended. It is mostly searched from outside the UAE. UAE Segment B non-brand CTR is 0.09% on 44,371 impressions, so non-brand reporting matters far less here than in the unfiltered plan and Segment B CTR is quoted all-query.

`renters insurance` at position 8 on 3,124 UAE impressions returning one click is the standout: a page-1 UAE ranking that is not being clicked.

## 1i. AI Overview presence and citation

Unchanged, 15 queries on google.ae.

| Segment | AIO present | PB cited in AIO | PB in organic top 12 |
|---|---|---|---|
| A Business | 4/5 | **2/5** | 2/5 |
| B Home | 5/5 | **3/5** | 5/5 |
| C Group Health | 5/5 | **1/5** | **0/5** |
| **Total** | **14/15 (93%)** | **6/15 (40%)** | 7/15 (47%) |

---

## Data gaps and inconsistencies — flagged, not smoothed over

1. **This view sits on Search Console's anonymised dataset.** A country filter drops the query onto a smaller table. Verified on Segment A over 28 days: `page` and `date` breakdowns sum to the unfiltered aggregate of 249 clicks and 49,780 impressions, while `country`, `query` and `device` all sum to 71 clicks and 35,411 impressions. **Clicks and CTR here are understated by roughly two to three times.** Use them only for UAE month-on-month comparison, never against the unfiltered plan. Positions are unaffected by the volume loss and are comparable across both documents.
2. **Use the URL-prefix property, not the domain property.** `sc-domain:policybazaar.ae` is missing 95 consecutive days of its own reporting, 5 Oct 2025 to 7 Jan 2026. Every figure here comes from `https://www.policybazaar.ae/`, which is complete for all 360 days. Any dashboard still pointed at the domain property is wrong.
3. **Two undiagnosed ranking breaks, neither site-wide.** Each segment lost 5.8 to 8.7 UAE positions in the 23 Nov – 20 Dec 2025 bucket and 5.7 to 11.4 in the 10 May – 6 Jun 2026 bucket, while site-wide moved 1.9 and 1.2 and recovered both times. No known site event explains either. No cause is attributed.
4. **Semrush and UAE Search Console diverge by 28 places on Segment C**, Semrush at an average ranked position of 13.4 against 41.6. The Semrush export excludes AI Overview results, which is one candidate cause. Reconcile before acting on the page-2 pool.
5. **What fires `formSubmitSuccess` is unconfirmed,** so GA4 is baseline context only and CRM is the sole lead measure.
6. **UAE impressions are already at the trailing-year run rate**, 64,318 against 64,416. Impression growth therefore cannot come from recovery alone and must come from the indexation and targeting fixes.
7. **`best home insurance in uae` has five UAE impressions across 360 days** at position 1.0. The ranking is genuine and the demand negligible, so it should be replaced on the priority list.
8. **The Semrush export has no usable trend line.** Single-date snapshot, and 26 of 125 keywords show a change equal to `100 − position`, the signature of newly added keywords.
9. **The AI Overview baseline is a single run and was not issued from a UAE IP.** The `gl=ae` parameter influences results without replicating a Dubai search.
10. **Crawl breadth is not a problem.** Measured like-for-like against the same 28-day window last year, pages earning impressions grew in Segment A and B and held flat in C.
11. **`Total FY-26` in the lead file is not a fiscal year.** It spans April 2025 to June 2026, fifteen months, excluding July 2026.
12. **Zero-click query counts depend on the export row limit.** The figures above use a 5,000-row pull. A 500-row pull returns 16 queries instead of 23, so any comparison must use the same limit.
13. **Whether undeclared sitemaps exist is unverified.** The audit followed the 38 child sitemaps declared in `sitemap.xml`.

---

# STEP 2 — Month-1 KRAs & KPIs, UAE basis

## Cross-segment foundations

| KRA | KPI | Current Baseline | 1-Month Target | Rationale tied to baseline |
|---|---|---|---|---|
| Retire the broken property | Reporting moved off `sc-domain:policybazaar.ae` | in use | **All reporting on the URL-prefix property** | The domain property is missing 95 days of its own data. Mechanical, week 1 |
| Diagnose the November 2025 break | Root cause documented | unknown | **Written diagnosis** | Segments lost 5.8 to 8.7 UAE positions in the 23 Nov – 20 Dec bucket while the site lost 1.9 and recovered. Mechanical, week 1 |
| Diagnose the May 2026 break | Root cause documented | unknown | **Written diagnosis** | Segments lost 5.7 to 11.4 UAE positions in the 10 May – 6 Jun bucket while the site lost 1.2. Mechanical, week 1 |
| Confirm the lead event definition | What fires `formSubmitSuccess` | unknown | **Documented from analytics** | GA4 event volume runs roughly ten times CRM lead volume. Mechanical, week 1 |
| Audit the sitemap generator | Top-level hubs present across all templates | unknown | **Audit complete** | The Business hub was dropped from all 38 child sitemaps |
| Reconcile Semrush against UAE Search Console | Divergence explained | 28 places on Segment C | **Documented** | Semrush 13.4 average against Search Console 41.6. The page-2 targets depend on which source is right. Mechanical, week 1 |

## Segment A — Business / Commercial

| KRA | KPI | Current Baseline | 1-Month Target | Rationale tied to baseline |
|---|---|---|---|---|
| Fix hub indexation | `/business-insurance/` in sitemap | **absent** | **Present and indexed** | Live 200 self-canonical hub earning 2,068 UAE impressions at position 21.3, missing from all 38 child sitemaps. Highest-leverage single fix. Mechanical |
| Recover the hub | `/business-insurance/` UAE position | 21.3 | **≤18.5** | 2,068 UAE impressions and 1 click in 28 days. Stretch |
| Indexation health | Impression-earning URLs missing from sitemap | 13 | **0** | Verified set difference, each URL redirect-checked. Mechanical |
| Schema completeness | Hub schema gaps closed | FAQPage and modified date both missing | **Both live and validated** | The only one of the three hubs without either. Mechanical |
| Content depth | Hub rendered word count | **1,073** | **≥3,500** | Sibling hubs run 3,659 and 3,768 words. Stretch |
| Organic visibility | UAE average position | 28.9 | **24.0** | Trailing-year UAE average is 19.4 and the segment held 8.8 to 10.8 before the November break. Target closes 52% of the 9.5-place gap. Aggressive |
| Click growth | UAE clicks, 28d | 64 | **95, +48%** | Trailing-year UAE run rate is 114 and the segment reached 148 to 159 per 28 days pre-break. Target recovers 62% of the −44% shortfall. Aggressive |
| CTR improvement | UAE CTR, 28d | 0.22% | **0.33%** | 9 queries hold 9,552 UAE impressions at one click or fewer. Trailing-year UAE CTR is 0.37%. Stretch |
| Page-2 conversion | Semrush keywords in top 10 | 22 / 52 | **28 / 52** | 14 keywords sit at 11–20, requiring 6 conversions. Aggressive |
| Head-term expansion | Semrush keywords in top 3 | 11 / 52 | **15 / 52** | The next four must come from adnic at 8 and aig at 6. Aggressive |
| AI Overview citation | PB cited on sampled queries | 2 / 5 | **4 / 5** | AIO fires on 4 of 5 but PB ranks top-12 on only 2. Aggressive |
| Lead volume | CRM Business Insurance leads per month | 133 | **155, +16.5%** | Trailing-12 average 137, best month 171. Organic is 12.4% of UAE segment sessions, so most must come from conversion-rate work. Aggressive |

## Segment B — Home Insurance

| KRA | KPI | Current Baseline | 1-Month Target | Rationale tied to baseline |
|---|---|---|---|---|
| Resolve hub cannibalization | `/home-insurance/` UAE position for "home insurance" | **68.0** | **≤35** | The hub ranks 68.0 in the UAE for its own head term while the child article carries all four Home priority keywords. Largest content problem in this view. Aggressive |
| Recover the hub overall | `/home-insurance/` UAE position, all queries | **50.3** | **≤32** | 2,270 UAE impressions and zero clicks in 28 days. Aggressive |
| Restore the dead section index | `/home-insurance/news-and-update/` | **404** | **200 listing page** | Dead index above six live children. Mechanical |
| Indexation health | URLs missing from sitemap | 1 | **0** | `/home-insurance/articles/`. Mechanical |
| Schema completeness | Product/Offer schema on hub | missing | **Live** | Hub carries FAQPage and Rating but no product markup. Mechanical |
| Organic visibility | UAE average position | 31.0 | **24.5** | Trailing-year UAE average is 19.4 and the segment held 11.2 to 11.6 before the November break. Target closes 56% of the 11.6-place gap. Aggressive |
| Click growth | UAE clicks, 28d | 23 | **38, +65%** | Trailing-year UAE run rate is 50. The segment reached 212 in February and 54 to 65 in Aug–Sep. Target recovers 56% of the −54% shortfall. Aggressive |
| CTR improvement | UAE CTR, 28d | 0.15% | **0.24%** | 9 queries hold 13,935 UAE impressions at one click or fewer, led by `renters insurance` at position 8 on 3,124. Trailing-year UAE CTR is 0.31%. Aggressive |
| Page-2 conversion | Semrush keywords in top 10 | 14 / 40 | **22 / 40** | 21 of 40 sit at 11–20, the largest quick-win pool. Aggressive |
| Close the competitor gap | Semrush keywords in top 3 | 4 / 40 | **8 / 40** | giggulf 21 and adnic 19 against PB's 4. Aggressive |
| AI Overview citation | PB cited on sampled queries | 3 / 5 | **5 / 5** | AIO fires on all 5 and PB already ranks top-12 on all 5, so the misses are a content-format gap. Aggressive but reachable |
| Priority keyword clicks | Combined 28d UAE clicks, keywords 7 to 10 | **1** | **12** | 1,459 UAE impressions converting at 0.07%. `home insurance dubai` holds 598 at position 24.5. Aggressive |
| Priority keyword rankings | Keywords 7, 8 and 9 in UAE top 10 | 0 / 3 | **2 / 3** | All three averaged 16.6 to 20.3 over the trailing year and now sit at 20.8 to 25.6. Aggressive |
| Lead volume | CRM Home Insurance leads per month | 36 | **52, +44%** | Trailing-12 average 69, best month 113. Organic is 43.3% of UAE segment sessions, the highest of the three, so ranking recovery reaches leads fastest here. Aggressive |

## Segment C — Group Health

| KRA | KPI | Current Baseline | 1-Month Target | Rationale tied to baseline |
|---|---|---|---|---|
| Resolve the listicle redirect | Decision on `best-group-health-insurance-companies-in-uae` | 301'd to hub | **Decision made and actioned** | 4,511 impressions across 8 URL variants, redirected from comparison intent into a quote form. Stretch |
| Recover the hub | `/group-health-insurance-hic/` UAE position | **38.4** | **≤31** | 6,948 UAE impressions and 5 clicks in 28 days. All six Group Health priority keywords already resolve here, so hub position is the whole story for this segment. Aggressive |
| Indexation health | URLs missing from sitemap | 1 | **0** | `/group-health-insurance/articles/`. Mechanical |
| Schema completeness | Product/Offer schema on hub | missing | **Live** | Hub carries FAQPage but no product markup. Mechanical |
| Close a tracking gap | `medical insurance for company` in Semrush | absent | **Tracked** | 450 search volume, UAE position 12.8, not in the campaign. Mechanical |
| Organic visibility | UAE average position | 41.6 | **35.0** | Trailing-year UAE average is 30.0 and the segment held 16.9 to 19.4 before the November break. Target closes 57% of the 11.6-place gap, joint-worst of the three, and 32 of 33 Semrush keywords with genuine movement went down. Aggressive |
| Click growth | UAE clicks, 28d | 15 | **18, +20%** | Trailing-year UAE run rate is 19, so the volume shortfall is only 21%, the smallest of the three. This segment is a position problem, not a volume problem. Stretch |
| CTR improvement | UAE CTR, 28d | 0.07% | **0.09%** | 5 queries hold 9,556 UAE impressions at one click or fewer. Trailing-year UAE CTR is 0.11%. Stretch |
| Page-2 conversion | Semrush keywords in top 10 | 8 / 33 | **14 / 33** | 22 of 33 sit at 11–20 per Semrush, but UAE Search Console places the segment at 41.6. Contingent on the reconciliation above. Aggressive |
| Close the competitor gap | Semrush keywords in top 10 | PB 8 vs adnic 24 | **PB 14** | Same 33-keyword set: adnic 24, giggulf 21, PB 8. Aggressive |
| AI Overview citation | PB cited on sampled queries | 1 / 5 | **3 / 5** | AIO fires on all 5 but PB ranks top-12 on none, so citation upside is capped until rankings move. Highest-risk KPI |
| Priority keyword clicks | Combined 28d UAE clicks, keywords 1 to 6 | **3** | **18** | 1,427 UAE impressions at 0.21%. `group medical insurance` at 491 impressions and `group health insurance` at 441 carry it. Aggressive |
| Priority keyword rankings | Keywords 1 to 6 in UAE top 20 | 1 / 6 | **5 / 6** | Five of six averaged 8.6 to 19.5 over the trailing year and all now sit at 20.9 to 26.8. Aggressive |
| Lead volume | CRM Group Health leads per month | 16 | **26, +63%** | Trailing-12 average 32, best month 45. Against −63% year on year this is recovery. Aggressive |

## Month-1 rolled-up summary, UAE basis

| KRA | KPI | Current Baseline | 1-Month Target | Rationale tied to baseline |
|---|---|---|---|---|
| Organic visibility | Blended UAE position, impression-weighted | 33.4 | **27.5** | Trailing-year UAE blended average is 22.2. Target closes 53% of the 11.2-place gap. Aggressive |
| Click growth | UAE clicks, 3 segments, 28d | 102 | **151, +48%** | A 95, B 38, C 18. Trailing-year UAE run rate is 183, so this recovers 60% of the shortfall. Aggressive |
| Impression growth | UAE impressions, 28d | 64,318 | **≥68,000** | Impressions are already at the trailing-year run rate of 64,416, so this target exceeds it and must come from the hub sitemap fix and the dead-page restoration, not from recovery. Stretch |
| CTR improvement | UAE CTR, 3 segments, 28d | 0.16% | **0.23%** | 23 queries hold 33,043 UAE impressions at one click or fewer. Trailing-year UAE CTR is 0.28%. Aggressive |
| **Priority keyword clicks** | Combined 28d UAE clicks, 10 keywords | **4** | **30** | B contributes 12 and C contributes 18. Nine of ten averaged better than position 21 over the trailing year. Aggressive |
| **Priority keyword coverage** | Keywords with at least 1 click | **2 / 10** | **8 / 10** | Eight of ten currently produce nothing. Aggressive |
| **Priority keyword rankings** | Keywords in UAE top 10 | **0 / 10** | **4 / 10** | Same basis. Aggressive |
| **Priority keyword rankings** | Keywords in UAE top 20 | **1 / 10** | **7 / 10** | Same basis. Aggressive |
| Hub recovery | Three hubs at or better than target UAE position | 0 / 3 | **3 / 3** | Business 21.3, Home 50.3, Group Health 38.4. Targets ≤18.5, ≤32, ≤31. Aggressive |
| Home head-term recovery | `/home-insurance/` UAE position for "home insurance" | **68.0** | **≤35** | The article has taken all four Home priority keywords in this market. Aggressive |
| Ranking distribution | Semrush keywords in top 10, of 125 | 44 | **64** | 57 of 125 sit at 11–20. Aggressive |
| Ranking distribution | Semrush keywords in top 3, of 125 | 18 | **29** | Widest competitor gap is Segment B. Aggressive |
| Indexation and crawl health | Impression-earning URLs missing from sitemap | **15** | **0** | Includes the `/business-insurance/` hub. Mechanical |
| Indexation and crawl health | Dead URLs still earning impressions | 1 | **0** | `/home-insurance/news-and-update/`. Mechanical |
| Redirect quality | Intent-mismatch redirects resolved | 0 / 4 | **4 / 4** | 8,301 impressions sit behind these four decisions. Stretch |
| Schema completeness | Hubs with a complete schema set | 0 / 3 | **3 / 3** | Business missing FAQPage; Home and Group Health missing Product or Offer. Mechanical |
| Content freshness and E-E-A-T | Hubs with a modified date | 2 / 3 | **3 / 3** | `/business-insurance/` has none. Mechanical |
| Measurement integrity | Reporting property corrected | domain property in use | **URL-prefix only** | The domain property is missing 95 days of its own data. Mechanical |
| Measurement integrity | Ranking breaks root-caused | 0 / 2 | **2 / 2** | November 2025 and May 2026, neither site-wide, neither explained. Mechanical |
| AI Overview citation | PB cited across 15 sampled queries | 6 / 15, 40% | **12 / 15, 80%** | AIO fires on 93%. PB ranks top-12 on 7 of 15. Aggressive |
| Lead volume | CRM leads per month, 3 products | 185 | **233, +26%** | A 155, B 52, C 26. Trailing-12 average 238. Aggressive |

---

# STEP 3 — Weekly breakdown, UAE basis

Technical and diagnostic work is front-loaded into weeks 1 and 2. Ranking and lead movement is loaded into weeks 3 and 4, because search impact lags implementation. Week 1 targets a small click dip, 25 against a 25.5 per week baseline, because hub re-targeting and canonical changes cause short-term churn.

## Segment A — Business / Commercial (weekly)

| Week | Work being done | KPI checkpoint (cumulative unless noted) |
|---|---|---|
| **W1** 5–11 Aug | Move all reporting off the domain property. Add `/business-insurance/` to `sitemap-business-insurance.xml` and fix the generator that dropped it. Lead the November 2025 and May 2026 break diagnoses: change log, deploy history, log-file crawl audit for both windows. Submit the 13-URL sitemap patch. Author FAQPage and modified-date JSON-LD. Rewrite titles and metas for the 9 zero-click UAE queries holding 9,552 impressions | UAE clicks 17, dip expected. Position 28.9, unchanged. Hub 21.3, unchanged. Hub in sitemap and submitted for indexing. Reporting property corrected. Both break diagnoses documented |
| **W2** 12–18 Aug | Deploy FAQPage and modified date. Expand the hub from 1,073 to 3,500 rendered words. Ship the rewritten titles and metas. Internal links from `/commercial-motor/articles/` and `/workers-compensation/articles/` into the money pages | UAE clicks 38. CTR 0.25%. Position 27.5. Hub ≤20.5. Schema validating. Hub at 3,500 words or more |
| **W3** 19–25 Aug | Convert the 14 page-2 Semrush keywords, prioritising `public liability insurance`, `contractor all risk insurance` and `business interruption insurance`. Add answer-first blocks for the 3 uncited AI Overview queries. Re-run the AIO sample | UAE clicks 65. CTR 0.29%. Position 25.6. Hub ≤19.5. Semrush top 10 at 25/52, top 3 at 13/52. AIO 3/5 |
| **W4** 26 Aug–1 Sep | Push `workmen compensation insurance` and `professional indemnity insurance` into the top 3. Conversion-rate review of organic-landed UAE sessions | **UAE clicks 95. CTR 0.33%. Position 24.0. Hub ≤18.5. Top 10 at 28/52. Top 3 at 15/52. AIO 4/5. CRM leads 155** |

## Segment B — Home Insurance (weekly)

| Week | Work being done | KPI checkpoint (cumulative unless noted) |
|---|---|---|
| **W1** 5–11 Aug | Sign off the cannibalization decision: the hub ranks 68.0 in the UAE for "home insurance" while the child article carries all four Home priority keywords. Restore `/home-insurance/news-and-update/` from 404 to a listing page. Add `/home-insurance/articles/` to the sitemap. Author Product/Offer JSON-LD. Diagnose `renters insurance`, 3,124 UAE impressions at position 8 with one click | UAE clicks 5, dip expected. Position 31.0, unchanged. Hub 68.0 and 50.3, unchanged. News index returns 200. Cannibalization decision signed off |
| **W2** 12–18 Aug | Execute the hub fix: re-target the hub to `home insurance`, `home insurance dubai` and `home insurance uae`; re-scope the article to comparison intent; re-point internal anchors from article to hub. Deploy Product/Offer schema. Rewrite titles and metas for the 9 zero-click UAE queries holding 13,935 impressions | UAE clicks 13. CTR 0.18%. Position 29.0. Hub head-term ≤55. Hub all queries ≤44 |
| **W3** 19–25 Aug | Work the 21-keyword Semrush page-2 pool, prioritising `home contents insurance dubai`, `home insurance abu dhabi` and `house insurance`. Add answer-first blocks for `building insurance dubai` and `renters insurance dubai`, both AIO-present with PB uncited but ranking top 12. Re-run the AIO sample | UAE clicks 24. CTR 0.21%. Position 26.5. Hub head-term ≤45. Hub all queries ≤38. Top 10 at 18/40. AIO 4/5. Priority keyword clicks 6 |
| **W4** 26 Aug–1 Sep | Close the top-3 gap against giggulf and adnic on the four highest-volume terms. Confirm the hub, not the article, is the ranking URL for head terms | **UAE clicks 38. CTR 0.24%. Position 24.5. Hub head-term ≤35. Hub all queries ≤32. Top 10 at 22/40. Top 3 at 8/40. AIO 5/5. Priority keyword clicks 12. CRM leads 52** |

## Segment C — Group Health (weekly)

| Week | Work being done | KPI checkpoint (cumulative unless noted) |
|---|---|---|
| **W1** 5–11 Aug | Reconcile Semrush against UAE Search Console, a 28-place divergence. Decide whether to reverse the `best-group-health-insurance-companies-in-uae` redirect carrying 4,511 impressions. Add `/group-health-insurance/articles/` to the sitemap. Author Product/Offer JSON-LD. Add `medical insurance for company` to the Semrush campaign | UAE clicks 3. Position 41.6, unchanged. Hub 38.4, unchanged. Divergence documented. Redirect decision signed off. Semrush campaign updated |
| **W2** 12–18 Aug | If reversing, rebuild the comparison page and remove the 301. Deploy Product/Offer schema. Rewrite titles and metas for the 5 zero-click UAE queries holding 9,556 impressions, starting with `group medical insurance` at 2,875 impressions and position 46 | UAE clicks 7. CTR 0.07%. Position 39.5. Hub ≤36. Priority keywords in top 20 at 2/6 |
| **W3** 19–25 Aug | Depth work on the four highest-volume terms: `group insurance health`, `group medical insurance`, `group health insurance` and `group health coverage`. Add answer-first blocks for `corporate health insurance uae` and `employee medical insurance uae`. Re-run the AIO sample | UAE clicks 12. CTR 0.08%. Position 37.0. Hub ≤33. Semrush top 10 at 11/33. AIO 2/5. Priority keywords in top 20 at 4/6. Priority keyword clicks 9 |
| **W4** 26 Aug–1 Sep | Begin closing the adnic gap, PB 8 against adnic 24 in the top 10, on the highest-volume cluster | **UAE clicks 18. CTR 0.09%. Position 35.0. Hub ≤31. Top 10 at 14/33. AIO 3/5. Priority keywords in top 20 at 5/6. Priority keyword clicks 18. CRM leads 26** |

## Weekly rolled-up summary, UAE basis

| KPI | Baseline | W1 (5–11 Aug) | W2 (12–18 Aug) | W3 (19–25 Aug) | W4 (26 Aug–1 Sep) |
|---|---|---|---|---|---|
| UAE clicks, weekly | 25.5 per week | **25**, flat to slightly down | 33 | 43 | **50** |
| UAE clicks, cumulative | 102 in 28d | 25 | 58 | 101 | **151** |
| UAE CTR, 3 segments | 0.16% | 0.16% | 0.18% | 0.20% | **0.23%** |
| Blended UAE position | 33.4 | 33.4 | 31.7 | 29.6 | **27.5** |
| `/home-insurance/` UAE head-term position | 68.0 | 68.0 | ≤55 | ≤45 | **≤35** |
| `/home-insurance/` UAE position, all queries | 50.3 | 50.3 | ≤44 | ≤38 | **≤32** |
| `/business-insurance/` UAE position | 21.3 | 21.3 | ≤20.5 | ≤19.5 | **≤18.5** |
| `/group-health-insurance-hic/` UAE position | 38.4 | 38.4 | ≤36 | ≤33 | **≤31** |
| `/business-insurance/` in sitemap | absent | **present** | present | present | **indexed** |
| Reporting on the correct property | no | **yes** | yes | yes | yes |
| URLs missing from sitemap | 15 | **0 submitted** | 0 | 0 | **0 indexed** |
| Dead URLs earning impressions | 1 | **0** | 0 | 0 | **0** |
| Intent-mismatch redirects resolved | 0 / 4 | **4 / 4 decided** | 4 / 4 actioned | 4 / 4 | **4 / 4 verified** |
| Hubs with complete schema | 0 / 3 | 0 / 3, specs written | **3 / 3 deployed** | 3 / 3 validated | 3 / 3 |
| Business hub rendered words | 1,073 | 1,073 | **≥3,500** | ≥3,500 | ≥3,500 |
| Measurement fixes shipped | 0 / 6 | **6 / 6** | 6 / 6 | 6 / 6 | 6 / 6 |
| Priority keyword clicks, cumulative | 4 in 28d | 1 | 5 | 15 | **30** |
| Priority keywords with 1 or more clicks | 2 / 10 | 2 / 10 | 4 / 10 | 6 / 10 | **8 / 10** |
| Priority keywords in UAE top 20 | 1 / 10 | 1 / 10 | 3 / 10 | 5 / 10 | **7 / 10** |
| Priority keywords in UAE top 10 | 0 / 10 | 0 / 10 | 1 / 10 | 2 / 10 | **4 / 10** |
| Semrush top 10, of 125 | 44 | 44 | 46 | 54 | **64** |
| Semrush top 3, of 125 | 18 | 18 | 19 | 23 | **29** |
| AI Overview citation, 15 queries | 6 / 15 | 6 / 15 | 6 / 15 | 9 / 15 | **12 / 15** |
| CRM leads, cumulative | 185 per month | 49 | 104 | 166 | **233** |

**UAE click ladder by segment.**

| Segment | Baseline 28d | W1 | W2 | W3 | W4 | Month target |
|---|---|---|---|---|---|---|
| A Business | 64 | 17 | 21 | 27 | 30 | **95** |
| B Home | 23 | 5 | 8 | 11 | 14 | **38** |
| C Group Health | 15 | 3 | 4 | 5 | 6 | **18** |
| **Total** | **102** | **25** | **33** | **43** | **50** | **151** |

**Lead ladder by segment, CRM.** Unchanged from the unfiltered plan, since CRM data is UAE by definition.

| Segment | Baseline per month | W1 | W2 | W3 | W4 | Month target |
|---|---|---|---|---|---|---|
| A Business Insurance | 133 | 34 | 37 | 41 | 43 | **155** |
| B Home Insurance | 36 | 10 | 12 | 14 | 16 | **52** |
| C Group Health | 16 | 5 | 6 | 7 | 8 | **26** |
| **Total** | **185** | **49** | **55** | **62** | **67** | **233** |

---

## Key risks and assumptions

- **Clicks and CTR in this document are understated by roughly two to three times.** The country filter forces Search Console onto its anonymised dataset. Use these figures only for UAE month-on-month tracking. Never compare them against the unfiltered plan, and never present them as absolute traffic.
- **The decline is segment-specific.** Site-wide UAE position improved from 15.5 to 10.6 across the year while the three segments went from 8.8, 11.2 and 16.9 to 28.9, 31.0 and 41.6. There is no site-wide explanation available, and the targets are correspondingly harder to argue down.
- **Two undiagnosed breaks, November 2025 and May 2026.** Each cost the segments 5.7 to 11.4 places while the site lost under 2 and recovered. No cause is known. Every position target assumes whatever happened is either reversible or already spent.
- **Reporting has been on the wrong Search Console property.** The domain property is missing 95 days of its own data. Any dashboard, alert or export still pointed at it will disagree with this plan.
- **Segment C is a position problem, not a volume problem.** Its UAE click shortfall is only 21% against the trailing-year run rate, the smallest of the three, while its position gap of 11.6 places is joint-worst. Judging it on click growth would miss the point, which is why its click target is only +20% while its position and hub targets are the most demanding.
- **UAE impressions are already at the trailing-year run rate**, 64,318 against 64,416. The impression target of ≥68,000 therefore exceeds anything the segments achieved in the last year and depends entirely on the indexation fixes landing.
- **Semrush and UAE Search Console diverge by 28 places on Segment C.** The page-2 conversion target for that segment is unusable until this is reconciled in week 1.
- **CRM is the only lead measure.** GA4 organic key events are not carried as a KPI because what fires `formSubmitSuccess` is unconfirmed and the event count runs roughly ten times CRM volume.
- **Home Insurance is the clearest path from ranking to leads.** Organic is 43.3% of its UAE sessions over the last 28 days and 40.7% over 360, against 12.4% for Business and 6.4% for Group Health.
- **These are stretch targets and some will be missed.** Highest risk, in order: Segment C AI Overview citation at 3/5 when PB ranks top-12 on none of the sampled queries; the Home hub moving from 68.0 to 35 for its own head term inside a month; Segment C position 35.0 when 32 of 33 Semrush keywords with genuine movement went down; and the 12/15 rollup AIO rate.
- **Two redirect reversals carry downside.** Reversing a 301 costs re-indexing time and can lose equity already consolidated. Decide in week 1, measure in week 4, and be prepared to leave one alone.
- **The brand-query distortion is small in this view.** `policybazaar.ae reviews` is only 4.3% of Segment B UAE impressions against 20.3% blended, so Segment B CTR is quoted all-query here.
- **February may not be a fair reference peak for Segment B.** It reached 212 UAE clicks in February against 23 now, in a segment where rain-damage and fire news pages rank well. If February was event-driven, the run-rate benchmark is generous.
- **`renters insurance` is the single clearest CTR opportunity**, at 3,124 UAE impressions on position 8 returning one click over 90 days. A page-1 UAE ranking that nobody clicks usually means a title, meta or intent mismatch rather than a ranking problem.
- **Weekly figures are an allocation, not a forecast.** They were set to sum to the month target and are the most adjustable numbers here.
- **The AI Overview baseline is a single run and was not issued from a UAE IP,** so treat 93% presence and 40% citation as directional.
- **Crawl breadth is not a problem.** Like-for-like against the same 28-day window last year, pages earning impressions grew in Segment A and B and held flat in C.

**Decisions needed from the business:** what happened in November 2025 and again in May 2026; what fires `formSubmitSuccess`; whether Semrush or Search Console is right on Segment C; whether to reverse the Group Health listicle redirect; sitemap or noindex for the 12 `/articles/` pages; and whether February was an event-driven spike for Home. `best home insurance in uae` can be closed out: PB genuinely ranks 1.0 in the UAE and the term draws five impressions a year, so it should be replaced on the priority list.

---

## Data notes

- Search Console figures use `country equals are` alongside the page regex, on property `https://www.policybazaar.ae/`. GA4 uses `countryId = AE`.
- The country filter moves Search Console onto its anonymised query-level dataset. Verified on Segment A over 28 days: `page` and `date` breakdowns sum to the unfiltered aggregate of 249 clicks and 49,780 impressions, while `country`, `query` and `device` all sum to 71 clicks and 35,411 impressions. Clicks and CTR here are consequently understated. Positions are not affected by the volume loss.
- All 360 days carry data on this property. The domain property `sc-domain:policybazaar.ae` is missing 5 Oct 2025 to 7 Jan 2026 and must not be used.
- Run-rate benchmarks divide the 360-day figure by 360 and multiply by 28.
- Blended position is impression-weighted across the three segments, not a simple mean.
- Hub positions are measured on the hub URL itself, not as the site's aggregate position for a query. The two differ sharply on Home: the hub is at 68.0 for "home insurance" while the site's aggregate for that query is better, because the child article carries it.
- Semrush, CRM lead data, the AI Overview sample and the sitemap and redirect audit are identical to the unfiltered plan, since none is country-filtered at source.
- Hub word counts are rendered page text.
- Zero-click query counts use a 5,000-row export. Smaller limits undercount.
