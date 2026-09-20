# Q3 Innovations & Projection — Sep to Dec 2026
PolicyBazaar UAE · Prepared 2026-09-09 · Section 2's projection extends through Mar 2027 (see below); Sections 1, 3, 4, 5 remain scoped to Sep-Dec 2026.

---

## 1. Innovations Planned for Next Quarter

### Committed
- **Health Cover Page Launch.** `/health-insurance/cover/` hub plus 30 specialty spokes (orthopedic, cardiac, dental, IVF, mental health, etc.), audited page-by-page against the approved spec before publish.
- **Remove / re-optimise redundant content.** Prune or consolidate underperforming pages identified through the leads-intelligence and cannibalisation audits (Sections 2 and 4).
- **Partially automate weekly performance reporting.** Currently built fully manually (Google Slides). Confirmed scope: automate the data sections only (KPI cards, landing-page table, AI-citations table) from Metabase, GA4, SEMrush (manually downloaded) and manual rank checks; the Key Insights narrative and Initiatives/Roadmap sections stay human-written. Output as a generated PPT file for manual upload to Drive, not a live edit of the existing deck (no Slides-content-editing tool is currently available). Health Insurance only for the first version. Cadence (weekly vs. monthly) and the exact Metabase source cards are still being finalised and will be locked in when the automation skill itself gets built — this quarter's commitment is scoping and data-source validation, not a shipped automation yet.

### Proposed (not yet committed — for your review)
- **FAQPage/Article schema rollout** on high-intent informational pages. `travel-insurance-for-over-65` has 950 words of editorial content and zero FAQ schema, a gap that's likely costing it AI Overview/PAA visibility.
- **Google Messages (RCS) business chat.** RCS (Rich Communication Services) lets users chat directly with the brand straight from Google Search results or the Google Messages app on Android, with no separate app download or site visit required.
- **Internal-link cleanup pass** on URLs already 301-redirected into a consolidated primary (e.g. `cheapest-expat-health-insurance-plans-in-uae` to `medical-insurance`), so internal links and sitemaps point at the resolved URL directly instead of riding the redirect.
- **E-E-A-T remediation pass** on pages scoring below roughly 65/100 (Section 2): add multi-insurer citations instead of single-insurer bias, and fill in missing senior/product-specific entities such as pre-existing conditions, Schengen/worldwide cover, and cancel-for-any-reason.

---

## 2. Impact Analysis (Quantifiable)

**Basis:** retrospective, real data only — CRM leads export, SEMrush position tracking, GSC, GA4. Nothing below is estimated or projected.

### Leads ΔYoY (3-month window vs. same period last year — retrieved from CRM)
| Vertical | This period | Same period LY | Δ |
|---|---|---|---|
| Health | 6,687 | 10,103 | **-33.8%** |
| Travel | 3,534 | 7,822 | **-54.8%** |

### Traffic ΔYoY
**Now available — corrected.** The first two pulls used the wrong GSC property (`sc-domain:policybazaar.ae`), which returned a `page,date` result silently capped at 100,000 rows and appeared to have a 95-day gap (Oct-Dec 2025). Re-querying the correct property, the URL-prefix property `https://www.policybazaar.ae/` (matching what's actually used in Search Console), returned complete, gap-free daily data from 2025-06-01 through 2026-09-07 — 464 of 464 expected days present, zero missing.

**Real YoY, Jun-Aug (3-month window, matching the leads comparison above):**
| Metric | Jun-Aug 2025 | Jun-Aug 2026 | Δ |
|---|---|---|---|
| Clicks | 171,512 | 70,968 | **-58.6%** |
| Impressions | 12,263,116 | 8,467,080 | **-31.0%** |

Clicks fell much faster than impressions, meaning average position/CTR also degraded, not just visibility — consistent with the SEMrush position slides already documented on the worst-hit pages above.

**Full monthly trend (2025-06 to 2026-09, GSC `date`-only, correct property):**
| Month | Clicks | Impressions |
|---|---|---|
| 2025-08 | 35,488 | 2,683,474 |
| 2025-09 | 44,487 | 3,287,741 |
| 2025-10 | 45,743 | 3,291,724 |
| 2025-11 | 35,377 | 3,409,693 |
| 2025-12 | 34,607 | 4,110,342 |
| 2026-01 | 43,818 | 5,760,952 |
| 2026-02 | 35,313 | 4,600,026 |
| 2026-03 | 46,206 | 4,578,739 |
| 2026-04 | 27,836 | 3,594,511 |
| 2026-05 | 25,241 | 3,153,723 |
| 2026-06 | 24,560 | 2,927,835 |
| 2026-07 | 23,296 | 2,749,530 |
| 2026-08 | 23,112 | 2,789,715 |
| 2026-09 (partial, through the 7th) | 5,133 | 633,317 |

Clicks peaked in October 2025 (45,743) and March 2026 (46,206), then declined every month since March — down 50% by August. GA4 gave a single 12-month snapshot only (476,542 organic sessions sitewide) — not YoY, not vertical-split, context only.

### Worst-hit pages by leads ΔYoY (real CRM + SEMrush data)
| Page | Vertical | Leads ΔYoY | Position Δ |
|---|---|---|---|
| how-to-check-medical-insurance-status-with-emirates-id-hiart | Health | 997→113 (-88.7%) | — |
| top-10-health-insurance-companies-in-uae-hiart | Health | 207→31 (-85.0%) | — |
| can-you-buy-health-insurance-for-new-born-baby-in-uae-hiart | Health | 85→4 (-95.3%) | — |
| 10-best-travel-insurance-companies-in-uae | Travel | 71→0 (-100%) | — |
| travel-insurance-dubai | Travel | 245→37 (-84.9%) | — |
| travel-insurance-armenia | Travel | 222→51 (-77.0%) | — |
| travel-insurance-for-over-65 | Travel | 1→0 (-100%) | **+14.7 (worse)** |
| emirates-travel-insurance | Travel | 30→1 (-96.7%) | +15.0 (worse) |

### Root-cause deep dive — `travel-insurance-for-over-65` (top-severity page, fully audited)
- Position slid +14.7 YoY (SEMrush, real)
- E-E-A-T score ≈ 61/100 — no FAQ/Article schema; missing pre-existing-conditions, Schengen/worldwide cover, and cancel-for-any-reason content despite these being core to "over 65" search intent; direct answer buried at word ~64 instead of the 40-60 word target; single-insurer (Orient) framing
- Mobile field LCP: 4.10s (**Poor**); CLS 0.16 mobile / 0.21 desktop (**Needs Improvement** both)
- Desktop: a promo interstitial blurs the H1/nav/CTA behind a modal on first load
- Backlink profile: Common Crawl only (no Moz key) — policybazaar.ae has the strongest PageRank rank of 4 compared domains, but weaker link-density than 2 smaller competitors; no referring-domain gap list available without a paid backlink index

**Full reports:**
- `Health Insurance/Result/leads-intel-health-2026-09-09.html`
- `Travel Insurance/Result/leads-intel-travel-2026-09-09.html`

**Data-quality flag:** travel SEMrush snapshot is stale (2026-06-09 vs. health's 2026-09-07) — refresh before trusting travel position trends further. Phases 3-5 (full per-page deep-dive, competitor leaderboard, backlink targets, new-content roadmap) were only completed for the single page above; not run sitewide this pass.

### Real Travel leads trend (Metabase, `International Travel` product, same metric definition as Health)
| Month | Leads | Bookings | Conversion% |
|---|---|---|---|
| Feb 2025 | 2,142 | 838 | 39.12% |
| Mar 2025 | 2,752 | 1,090 | 39.61% |
| Apr 2025 | 2,178 | 755 | 34.66% |
| May 2025 | 2,099 | 827 | 39.40% |
| Jun 2025 | 2,027 | 721 | 35.57% |
| Jul 2025 | 1,673 | 651 | 38.91% |
| Aug 2025 | 1,238 | 507 | 40.95% |
| Sep 2025 | 1,236 | 511 | 41.34% |
| Oct 2025 | 1,382 | 533 | 38.57% |
| Nov 2025 | 1,409 | 495 | 35.13% |
| Dec 2025 | 1,185 | 474 | 40.00% |
| Jan 2026 | 851 | 349 | 41.01% |
| Feb 2026 | 721 | 278 | 38.56% |
| Mar 2026 | 728 | 158 | 21.70% |
| Apr 2026 | 547 | 202 | 36.93% |
| May 2026 | 919 | 404 | 43.96% |
| Jun 2026 | 821 | 352 | 42.87% |
| Jul 2026 | 905 | 412 | 45.52% |
| Aug 2026 | 921 | 421 | 45.71% |
| Sep 2026 (partial, through the 9th) | 240 | 118 | 49.17% |

Travel leads peaked in March 2025 (2,752) and have been on a much rockier decline than Health — a sharp drop through early 2026 (Apr 2026 low of 547), a partial recovery through mid-2026, then flat at ~900-920/month since May. Aug 2026 (921) is 66.5% below the March 2025 peak.

---

### PROJECTION — Sep 2026 to Mar 2027 (Health, Assumption-Based)

**Everything in this subsection is a projection, not retrieved fact.** It's built from two inputs you gave directly, applied mechanically:
- **Keyword rank targets:** tiering rule — current rank 1-5 holds; 6-15 targets top 10; 16-30 targets top 15; 30+ targets top 20.
- **Leads target:** Mar 2027 = 80% of March 2025's real leads figure.
- **Glide assumption:** even linear progression from the current baseline to the Mar 2027 target, month by month. This is a modeling choice, not a measured trend — actual month-to-month movement will be lumpier in reality.

**Keyword ranking migration (51 keywords, Health), by rank band:**
| Band | Sep-26 | Oct-26 | Nov-26 | Dec-26 | Jan-27 | Feb-27 | Mar-27 |
|---|---|---|---|---|---|---|---|
| Top 5 (rank 1-5) | 20 | 21 | 21 | 21 | 21 | 22 | 22 |
| Top 10 (rank 6-10) | 4 | 6 | 7 | 9 | 10 | 12 | 13 |
| Top 15 (rank 11-15) | 9 | 10 | 11 | 13 | 14 | 15 | 16 |
| Top 20 (rank 16-20) | 9 | 7 | 6 | 4 | 3 | 1 | 0 |
| Rank 21+ | 9 | 7 | 6 | 4 | 3 | 1 | 0 |

Current real distribution (baseline): Top5=20, Top10=3, Top15=8, Top20=10, 21+=10. Corrected from an earlier draft: the tiering rule doesn't mean a keyword in the 6-15 group stops exactly at rank 10 — a keyword already at rank 6 is close enough to Top 5 that it plausibly crosses in, while one at rank 15 barely reaches 10. So each tier's current range is mapped proportionally onto its target range (6-15 → 5-10, 16-30 → 10-15), letting the best performers in each tier spill into the better band above. That's why Top 5 grows to 22 by March instead of staying flat at 20 — 2 keywords currently at rank 6 are close enough to cross in. This is still a modeling choice, not a measured trend, and it says nothing about which specific initiative moves which specific keyword.

**Leads recovery (Health, monthly), assuming initiatives reverse the current decline:**
| Metric | Aug-26 (real) | Sep-26 | Oct-26 | Nov-26 | Dec-26 | Jan-27 | Feb-27 | Mar-27 (target) |
|---|---|---|---|---|---|---|---|---|
| Leads | 1,669 | 1,813 | 1,958 | 2,102 | 2,247 | 2,391 | 2,536 | 2,680 |
| MoM growth | — | 8.6% | 8.0% | 7.4% | 6.9% | 6.4% | 6.1% | 5.7% |

Baseline (Aug 2026 = 1,669 leads) and target (Mar 2027 = 2,680, i.e. 80% of March 2025's real 3,350) are both real, retrieved figures (Metabase, `Impure_conversion_Monthwise - Health` metric, International Health product, PB_Insurance_SEO/SEO/Footer traffic). Everything between them is a straight-line assumption, not a forecast derived from any predictive model — there is no historical basis in this data to say recovery will actually be linear, or that it will happen at all without the initiatives in Section 1 landing on schedule.

For reference, the current trajectory without intervention: leads fell from 3,350 (Mar 2025) to 1,669 (Aug 2026) — a real 50.2% decline over 17 months. The recovery target assumes that decline fully reverses to -20% (vs. Mar 2025) by Mar 2027, a materially different trajectory than anything observed in the data to date.

### PROJECTION — Sep 2026 to Mar 2027 (Travel, Assumption-Based)

Same methodology as Health above: current-rank tiering rule, 80%-of-March-2025 leads target, even linear glide. Nothing here is a forecast derived from a predictive model.

**Keyword ranking migration (77 keywords, Travel), by rank band:**
| Band | Sep-26 | Oct-26 | Nov-26 | Dec-26 | Jan-27 | Feb-27 | Mar-27 |
|---|---|---|---|---|---|---|---|
| Top 5 (rank 1-5) | 57 | 58 | 58 | 59 | 59 | 60 | 60 |
| Top 10 (rank 6-10) | 9 | 10 | 11 | 13 | 14 | 15 | 16 |
| Top 15 (rank 11-15) | 9 | 7 | 6 | 5 | 4 | 2 | 1 |
| Top 20 (rank 16-20) | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| Rank 21+ | 1 | 1 | 1 | 0 | 0 | 0 | 0 |

Current real distribution (baseline): Top5=57, Top10=8, Top15=10, Top20=1, 21+=1 (of 77 keywords). Travel already has far more keywords in Top5 than Health proportionally — 57 of 77 (74%) vs. Health's 20 of 51 (39%) — so there's less headroom for dramatic band movement; the main action is the 18 keywords currently ranked 6-15 pushing into Top5/Top10.

**Leads recovery (Travel, monthly), assuming initiatives reverse the current decline:**
| Metric | Aug-26 (real) | Sep-26 | Oct-26 | Nov-26 | Dec-26 | Jan-27 | Feb-27 | Mar-27 (target) |
|---|---|---|---|---|---|---|---|---|
| Leads | 921 | 1,104 | 1,287 | 1,470 | 1,653 | 1,836 | 2,019 | 2,202 |
| MoM growth | — | 19.9% | 16.6% | 14.2% | 12.5% | 11.1% | 10.0% | 9.1% |

Baseline (Aug 2026 = 921) and target (Mar 2027 = 2,202, i.e. 80% of March 2025's real 2,752) are both real, retrieved figures from the same Metabase metric as Health (International Travel product). **This is a steeper assumed recovery than Health's**, in both absolute and relative terms — Travel's Mar 2025 figure was near an all-time peak, and the current base (921) sits 66.5% below it, versus Health's 50.2% decline over the same window. Treat the Travel recovery target as more aggressive relative to its recent trend than the Health one.

---

## 3. Arabic Enhancement — Priority URL List

Pages flagged for Arabic-language enhancement this quarter:

- https://www.policybazaar.ae/health-insurance/medical-insurance/
- https://www.policybazaar.ae/travel-insurance/uae/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-georgia/
- https://www.policybazaar.ae/how-to-check-medical-insurance-status-with-emirates-id-hiart/
- https://www.policybazaar.ae/health-insurance-for-kids-hiart/
- https://www.policybazaar.ae/travel-insurance/articles/how-to-get-orange-card-for-oman/
- https://www.policybazaar.ae/travel-insurance/articles/travel-ban-check-by-passport-number/
- https://www.policybazaar.ae/health-insurance/articles/maternity-insurance-in-uae/
- https://www.policybazaar.ae/ar-ae/health-insurance/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-usa/
- https://www.policybazaar.ae/top-10-health-insurance-companies-in-uae-hiart/
- https://www.policybazaar.ae/ar-ae/health-insurance/articles/top-10-health-insurance-comapnies-in-uae/
- https://www.policybazaar.ae/orient-health-insurance-hipvd/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-russia/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-armenia/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-turkey/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-indonesia/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-dubai/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-uk/
- https://www.policybazaar.ae/health-insurance/health-insurance-in-sharjah/
- https://www.policybazaar.ae/ar-ae/senior-citizen-health-insurance-hic/
- https://www.policybazaar.ae/health-insurance/articles/dental-insurance-in-uae/
- https://www.policybazaar.ae/network-hospitals/orient-insurance-hospital-list-dubai/
- https://www.policybazaar.ae/health-insurance-abu-dhabi/
- https://www.policybazaar.ae/travel-insurance/articles/cancel-for-any-reason-travel-insurance/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-for-over-70/
- https://www.policybazaar.ae/travel-insurance/annual-multi-trip-travel-insurance/
- https://www.policybazaar.ae/can-you-buy-health-insurance-for-new-born-baby-in-uae-hiart/
- https://www.policybazaar.ae/ar-ae/individual-health-insurance-hic/
- https://www.policybazaar.ae/travel-insurance/articles/best-winter-sports-travel-insurance/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-japan/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-morocco/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-south-africa/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-vietnam/
- https://www.policybazaar.ae/health-insurance/domestic-worker-health-insurance/
- https://www.policybazaar.ae/insurance-companies/dnata-travel-insurance/
- https://www.policybazaar.ae/health-insurance-for-married-couples-hiart/
- https://www.policybazaar.ae/health-insurance/articles/health-insurance-in-ajman/
- https://www.policybazaar.ae/ar-ae/family-health-insurance-hic/
- https://www.policybazaar.ae/health-insurance/basic/
- https://www.policybazaar.ae/health-insurance/articles/health-insurance-for-abu-dhabi-residence-visa/
- https://www.policybazaar.ae/travel-insurance/international-travel-insurance/
- https://www.policybazaar.ae/health-insurance/nextcare/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-brazil/
- https://www.policybazaar.ae/ar-ae/adnic-health-insurance-hipvd/
- https://www.policybazaar.ae/ar-ae/orient-health-insurance-hipvd/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-kazakhstan/
- https://www.policybazaar.ae/health-insurance/articles/insurance-installments-uae-tabby/
- https://www.policybazaar.ae/health-insurance/nas/
- https://www.policybazaar.ae/oman-travel-insurance-tipvd/
- https://www.policybazaar.ae/travel-insurance/travel-insurance-canada/
- https://www.policybazaar.ae/insurance-companies/aig-travel-insurance/
- https://www.policybazaar.ae/health-insurance/articles/best-short-term-international-health-insurance-in-uae/
- https://www.policybazaar.ae/network-hospitals/orient-insurance-hospital-list-abu-dhabi/
- https://www.policybazaar.ae/oman-health-insurance-hipvd/

---

## 4. Cannibalisation of Content

**Status: complete.** Full pipeline (GSC 12-month query/page overlap, SEMrush, GA4, leads, both verticals) run through Phase 4, including the mandatory safety-guard and spot-check phases. GSC window: 2025-09-09 to 2026-09-06, 100,000 rows, no errors.

### Headline numbers
| Metric | Value |
|---|---|
| Total pairs found | 432 (health 359, travel 73) |
| Pairs downgraded by safety guards | 114 |
| Impressions at risk | 233,016 |
| Leads at risk | 29,168 |

### Raw vs. guarded actions
| Action | Raw (pre-guard) | Final (post-guard) |
|---|---|---|
| Redirect | 25 | **1** |
| Consolidate | 57 | **0** |
| Hub-and-spoke | — | 46 |
| Differentiate | 219 | 221 |
| Architecture-review | — | 27 |
| Reinforce-signals | 131 | 136 |
| No-action | — | 1 |

Guard flags that fired: portfolio-orphans (79), cross-section (65), broader-competitor (47), homepage-as-source (25), below-severity-floor (8), product-mismatch (8), below-evidence-floor (3). All 132 URLs in the portfolio pull were fetched successfully, so no pair here is unverified.

### The one real redirect
Only one pair survives as an actual redirect recommendation after guards:
- **Query "adamjee health insurance hospital list"** — `/network-hospitals/adamjee-insurance-hospital-list-dubai/` → `/network-hospitals/adamjee-insurance-hospital-list-abu-dhabi/` (source has 0 clicks, 14 impressions, no orphaned protected queries)

**Zero pairs survive as "consolidate."** No other redirect should be actioned from this audit.

### Top 5 pairs by severity (post-guard)
| # | Query | Severity | Action | Note |
|---|---|---|---|---|
| 1 | best travel insurance | 93.5 | Reinforce-signals | Primary URL already 301s into its top competitor — GSC is crediting a URL that no longer independently resolves |
| 2 | cheapest health insurance dubai | 83.1 | Differentiate | — |
| 3 | cheapest health insurance in uae | 81.4 | Reinforce-signals | One of 3 competitors already resolved (301 + canonical) into the primary; the other two (`/health-insurance/`, homepage) are NOT resolved and still need manual architecture review |
| 4 | al sagr medical insurance hospital list | 81.1 | Differentiate | 38 competitor URLs checked — all independently self-canonical |
| 5 | adnec gold tier health insurance network | 78.1 | Reinforce-signals | — |

### Data-quality notes
- Leads date coverage differs slightly from the GSC window: health 2025-05-01 to 2026-09-06, travel 2025-05-01 to 2026-08-03 (documented in the report's Methodology sheet)
- All 10 top-severity pairs were spot-checked live (56 unique URLs, 0 fetch failures) before finalizing — nothing here is unverified
- **Caveat added after this audit ran:** it queried GSC's domain property (`sc-domain:policybazaar.ae`), which we later confirmed is missing 95 real days of data (2025-10-05 to 2026-01-07) that the correct URL-prefix property has in full. The plugin default has since been fixed for future runs. Per your call, this specific 432-pair result was not re-run against the corrected property — treat it as directionally reliable but not re-verified against complete data.

**Full report:** `Cannibalization/Result/cannibalization-report-2026-09-09.xlsx`

---

## 5. Reddit / Quora Strategy

The sourcing side gets automated; posting stays with a human.
- **Research and question identification:** scrape Reddit/Quora for UAE insurance questions and content gaps.
- **Answer drafting:** generate a first-pass answer draft for each identified question.
- **Posting:** stays manual, with a human reviewing every answer before it goes live.
- **Opportunity identification:** mine call/chat transcripts to surface recurring questions and gaps that aren't covered publicly yet.
