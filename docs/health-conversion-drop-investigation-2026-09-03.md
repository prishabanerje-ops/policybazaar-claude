# Health Insurance Conversion Drop — Investigation Report

**Date prepared:** 2026-09-03
**Prepared by:** Aakash Srivastava
**Trigger:** Manager's email raising 4 possible causes behind softening health insurance conversion, requesting the sales/marketing team validate before pulling levers across Paid Marketing, Brand/Social and Organic.

---

## 1. The four claims being tested

The manager's email, based on conversations with the Health Sales team, raised:

1. **Nationality mix has changed** — fewer Europeans (shorter lead-to-booking cycle), more Indian & Indian Subcontinent customers (longer cycle, slower decision-making).
2. **Pocket size is an issue** — customers increasingly conscious about conserving cash.
3. **PED leads have declined** — impacting overall ATS and conversion opportunity.

This report checks each claim against real data and, where a real problem was found (the "West" nationality segment), traces it to a root cause.

---

## 2. Data sources and scope

| Source | What it provided | Access level |
|---|---|---|
| Metabase, dashboard 129 ("Detailed Conversion health Expanded view"), cards 2158-2161, source table `leadenrichedreport_health` | Lead/booking counts, conversion %, ATS/APE, by salary band, nationality, customer type (PED), age, and funnel step | Logged in via Aakash's Metabase account; data pulled via the Metabase query API, not screen-scraped |
| Google Search Console, property `sc-domain:policybazaar.ae` | Organic impressions, clicks, average position, by country, page, and query | API Tier 1 (service account) |
| Google Analytics 4, property `309894472` | Real sessions by country/month | API Tier 2 |

**Time window:** June 1 – August 31, 2026 (three full months). September 2026 data exists in the underlying queries but is **excluded from all trend conclusions** — as of this report's date (Sept 3), September has only 3 days of data and would distort any month-over-month comparison.

**Known gaps:**
- No Google Ads API access (Tier 3) — actual ad spend by channel/country could not be retrieved. Where "paid channel" behavior is discussed below, it is inferred from lead-source counts and organic-health data, not from spend figures.
- The Salary_band Metabase card has no native date breakdown; a monthly version was built ad hoc for this report (not saved as a permanent Metabase asset).
- GA4's own "conversions" metric was collected but is **not used** in this report as a stand-in for actual leads — leads are a CRM/Metabase concept, not a GA4 event count.

---

## 3. Executive summary

| Claim | Verdict |
|---|---|
| Fewer Europeans | **Not supported.** Europe's overall lead share held flat (~6%) across all 3 months; Western Europe leads were actually up. |
| More Indian/Indian Subcontinent, longer cycle | **Share claim not supported** (flat ~53-55%, not rising). **Conversion-gap mechanism confirmed**: this group converts at 17-23% vs. 23-34% for European-origin leads, every month. |
| Pocket size / cash-conscious | **Not supported.** No shift toward lower income bands; conversion for the highest income band actually improved. |
| PED leads declined | **Share claim not supported** (flat ~7.3%/month). **ATS-sensitivity mechanism confirmed**: PED bookings carry 4-8x the average ticket size, so small swings matter disproportionately. |
| Real, verified problem found | **US/UK/Canada/Australia ("West") leads fell 30%** (424 → 299, Jun→Aug). Root-caused below: it is a top-of-funnel volume issue, not a conversion or agent-quality issue, and only partly explained by softer real traffic. |

---

## 4. Claim 1 & 2: Nationality mix

### 4.1 Data (Metabase, card "Health_detailed_Conversion_source_Nationality", exact query pull)

| Nationality group | Jun leads | Jul leads | Aug leads | Jun conv% | Jul conv% | Aug conv% |
|---|---|---|---|---|---|---|
| Western Europe | 874 | 928 | 953 | 28.4% | 29.3% | 30.3% |
| Eastern Europe | 215 | 198 | 189 | 23.3% | 26.8% | 27.0% |
| West (US/UK/Canada/Australia) | 424 | 368 | 299 | 32.8% | 34.0% | 34.4% |
| Indian | 9,887 | 9,671 | 8,743 | 18.5% | 18.5% | 20.3% |
| Pakistani | 2,492 | 2,723 | 2,456 | 17.8% | 17.6% | 22.9% |
| South Asian | 975 | 1,025 | 885 | 21.4% | 19.1% | 17.2% |
| **Total, all groups** | **24,133** | **25,456** | **22,847** | 15.9% | 15.6% | 17.4% |

### 4.2 Derived shares

| Group | Jun share | Jul share | Aug share |
|---|---|---|---|
| Western Europe + Eastern Europe | 4.5% | 4.4% | 5.0% |
| + West | 6.3% | 5.9% | 6.3% |
| Indian + Pakistani + South Asian | 55.3% | 52.7% | 52.9% |

### 4.3 Finding

- Europe's combined share of leads is **flat at ~6%**, not shrinking. Western Europe specifically is up (874→953).
- The only nationality group with a real decline is **"West"** (US/UK/Canada/Australia): 424 → 299 leads, **-30%**. This is investigated separately in Section 6.
- The Indian/Pakistani/South Asian combined share is flat-to-slightly-down (55.3%→52.9%), **not rising** as claimed.
- What **is** consistently true every month: Indian/Pakistani/South Asian leads convert at 17-23%, while European-origin leads (Western Europe, Eastern Europe, West) convert at 23-34%. This gap is real and stable — it supports the underlying mechanism behind the manager's point, even though the "mix is changing" framing does not hold in this 3-month window.

---

## 5. Claim 3: Pocket size / cash-conscious customers

### 5.1 Lifetime data (Metabase card "Health_detailed_Conversion_source_Salary_band" — no date breakdown natively)

| Salary band | Leads | Bookings | Conversion % | ATS | APE |
|---|---|---|---|---|---|
| AED 4K-5K | 331,188 | 49,356 | 14.9% | 1,901.18 | 93,834,683.06 |
| AED 5K-6K | 65,196 | 11,791 | 18.09% | 2,597.22 | 30,623,764.69 |
| AED 6K-7K | 40,607 | 7,992 | 19.68% | 2,709.56 | 21,654,767.18 |
| AED 7K-8K | 47,507 | 9,578 | 20.16% | 3,090.76 | 29,603,289.53 |
| AED 8K-9K | 25,487 | 4,709 | 18.48% | 2,860.88 | 13,471,884.82 |
| AED 9K-10K | 45,201 | 8,304 | 18.37% | 3,153.27 | 26,184,785.49 |
| Above AED 10K | 219,326 | 49,045 | 22.36% | 4,496.93 | 220,551,837.32 |
| Below AED 4K | 358,013 | 199 | 0.06% | 1,317.67 | 262,215.52 |
| **Grand totals** | **1,132,525** | **140,974** | **12.45%** | **3,094.10** | **436,187,227.61** |

### 5.2 Monthly view (built ad hoc for this report — not saved in Metabase)

| Salary band | Jun leads | Jul leads | Aug leads | Jun bookings | Jul bookings | Aug bookings |
|---|---|---|---|---|---|---|
| Below AED 4K | 6,792 | 7,105 | 6,456 | 2 | 0 | 1 |
| AED 4K-5K | 7,603 | 7,974 | 6,972 | 1,447 | 1,431 | 1,404 |
| AED 5K-6K | 1,198 | 1,294 | 1,181 | 262 | 296 | 263 |
| AED 6K-7K | 815 | 805 | 774 | 208 | 239 | 242 |
| AED 7K-8K | 860 | 1,011 | 839 | 234 | 242 | 213 |
| AED 8K-9K | 533 | 554 | 489 | 115 | 100 | 121 |
| AED 9K-10K | 1,022 | 1,230 | 1,032 | 201 | 237 | 198 |
| Above AED 10K | 5,310 | 5,483 | 5,104 | 1,374 | 1,435 | 1,524 |
| **Total** | **24,133** | **25,456** | **22,847** | — | — | — |

### 5.3 Finding

- Below AED 4K + AED 4K-5K ("tight budget" segment) share of total leads: **59.7% → 59.2% → 58.8%** — flat, not growing.
- Below AED 4K conversion: 0.03% → 0% → 0.02% — already near zero, not visibly worsening further.
- Above AED 10K conversion: **25.9% → 26.2% → 29.9%** — improving, the opposite of what a worsening "cash-consciousness" trend would predict.
- **No evidence in the last 3 months that salary mix or income-band conversion is deteriorating.** The claim is not supported by the data currently available.

---

## 6. Claim 4: PED leads declined

**Field-mapping note:** the dashboard uses a field called `pec_status` (values: Yes / No / Not Declared) as the closest available proxy for "PED" (pre-existing disease/condition). This mapping is **inferred** from field names on the source table (`pec_status`, `isped`, `isped_uhd` all exist on `leadenrichedreport_health`) — there is no explicit label confirming `pec_status` = "PED" in Metabase's metadata. Treat the PED-specific numbers below as a reasonable proxy, not a confirmed 1:1 mapping.

### 6.1 Data (Metabase, `pec_status`, summed across `isped_uhd`)

| pec_status | Jun leads | Jul leads | Aug leads | Jun APE | Jul APE | Aug APE |
|---|---|---|---|---|---|---|
| No | 18,350 | 19,060 | 17,067 | 9,652,237.98 | 9,565,209.56 | 9,633,335.51 |
| Not Declared | 4,047 | 4,505 | 4,117 | 2,470,864.91 | 2,505,981.07 | 2,660,723.12 |
| **Yes (PED proxy)** | **1,736** | **1,891** | **1,663** | 188,635.67 | 343,276.36 | 395,854.63 |
| **Total** | **24,133** | **25,456** | **22,847** | 12,311,738.56 | 12,414,466.99 | 12,689,913.26 |

### 6.2 Derived

| | Jun | Jul | Aug |
|---|---|---|---|
| PED share of total leads | 7.19% | 7.43% | 7.28% |
| APE per booking, PED | ~14,510 | ~14,930 | ~24,740 |
| APE per booking, non-PED | ~3,020 | ~2,940 | ~3,000 |
| PED : non-PED ticket size ratio | ~4.8x | ~5.1x | ~8.3x |

### 6.3 Finding

- PED share of total leads is **flat (~7.2-7.4%)** — no clean multi-month decline. August was down 12% vs. July in absolute PED lead count, slightly more than the 10% drop in total leads that month, but this is one month, not a trend.
- What **is** strongly confirmed: a PED-flagged booking carries **4 to 8 times** the average premium (APE) of a regular booking. Small swings in PED volume move blended ATS more than the raw lead numbers suggest — this is the real, data-backed mechanism behind the manager's point, independent of whether PED volume is actually declining.

---

## 7. Deep dive: the West segment (US/UK/Canada/Australia) drop

This is the one claim area with a real, verified decline (Section 4). The rest of this section traces it to a cause, including a correction made mid-investigation once better data came in.

### 7.1 Channel breakdown for West leads (Metabase, filtered to `nationality_group = "West"`)

| Channel | Jun | Jul | Aug | Change (Jun→Aug) |
|---|---|---|---|---|
| Google Search | 155 | 136 | 120 | -22.6% |
| Google Brand | 71 | 55 | 40 | -43.7% |
| SEO | 45 | 38 | 33 | -26.7% |
| Direct + Homepage | 46 | 35 | 35 | -23.9% |
| CRM | 36 | 35 | 23 | -36.1% |
| Bing | 14 | 12 | 8 | -42.9% |
| Agent Refer | 14 | 15 | 10 | -28.6% |
| Google Display | 12 | 8 | 10 | -16.7% |
| FB Display | 4 | 24 | 7 | -75% (after a July spike) |
| Others (small, one-off: FB Video, Social Organic, Footer, Brand, Affiliate, Google Video) | — | — | — | single-digit, mostly one-month blips |
| **Total** | **424** | **368** | **299** | **-29.5%** |

**Observation:** the decline is broad-based across nearly every channel simultaneously (paid search, organic, direct, CRM), not concentrated in one campaign. This pattern is more consistent with a shared upstream cause (traffic or visibility) than a single channel being paused.

### 7.2 First hypothesis: organic ranking collapse (Google Search Console)

Initial GSC pull for the four countries, June–August 2026 (exact API data):

| Country | Impressions Jun→Jul→Aug | Change | Avg. position Jun→Jul→Aug |
|---|---|---|---|
| USA | 437,187 → 171,912 → 139,360 | **-68%** | 8.3 → 13.6 → **15.2** |
| Canada | 20,250 → 13,597 → 10,807 | -47% | 12.5 → 11.8 → 12.4 |
| UK | 68,107 → 66,704 → 80,731 | flat/up | 29.9 → 26.4 → **21.4** (improving) |
| Australia | 12,180 → 12,090 → 10,609 | -13% | 30.8 → 34.5 → 30.1 |

For comparison, the site's largest markets over the same window: UAE impressions 1.93M→1.98M→2.01M (stable/up, position ~10-11), India 149k→175k→179k (up). This ruled out a sitewide algorithmic hit — the pattern looked USA-specific.

Top USA pages by impressions showed four core health-insurance pages losing real ranking position over the same window:

| Page | Position Jun → Aug |
|---|---|
| /health-insurance/ | 8.3 → 18.7 |
| /health-insurance/tpa/ | 4.2 → 13.1 |
| /daman-health-insurance-hipvd/ | 5.9 → 10.6 |
| /health-insurance/medical-insurance/ | 19.9 → 48.7 |

**This looked at first like a genuine USA-specific SEO ranking problem.**

### 7.3 Correction: the ranking signal was mostly noise

Pulling query-level detail for those four pages (USA only) revealed that most of the query volume behind them was **not real human search queries** — it consisted of `site:policybazaar.ae "..."` operator searches and unnaturally comprehensive multi-word phrasings (e.g. *"credible medical condition treatment information platforms uae"*, *"best medical condition and treatment information platforms uae"*) — a pattern consistent with an automated system (most likely Google's AI Overview query fan-out, or another bot/agent) generating multiple synthetic query variants, not organic customer search behavior.

Splitting the same four pages' USA impressions into recognizable human queries vs. this synthetic-looking pattern:

| | Jun | Jul | Aug |
|---|---|---|---|
| Real, recognizable human-query impressions | 567 | 310 | 530 |
| Synthetic-looking query impressions | 4,230 | 2,042 | **230** |

Real human search demand for these pages is **flat/noisy (567→530)**, not declining. The synthetic-looking query volume collapsed 95% (4,230→230) and accounts for nearly the entire apparent "ranking decline" reported in Section 7.2.

**Conclusion: the organic/SEO ranking explanation does not hold up once the bot/AI noise is removed. This finding was retracted before being included in any communication to the manager.**

### 7.4 Real traffic check (Google Analytics 4)

Site-wide sessions by country, June–August 2026 (exact GA4 API data, `properties/309894472`):

| Country | Sessions Jun → Jul → Aug | Change |
|---|---|---|
| USA | 13,229 → 12,579 → 12,012 | -9.2% |
| UK | 2,680 → 2,352 → 2,332 | -13.0% |
| Canada | 746 → 853 → 652 | -12.6% (noisy — up then down) |
| Australia | 219 → 277 → 215 | -1.8% (flat/noisy) |

**Note:** GA4's "conversions" metric was also pulled but is deliberately excluded from this table and from any leads-related conclusion — it is not a substitute for the CRM lead count.

**Finding:** real traffic from all four countries did soften genuinely, by roughly 9-13%. This is a real signal, but it is smaller than the 30% lead decline seen in the CRM data — traffic alone does not fully explain the gap.

### 7.5 Funnel/conversion-rate check (Metabase, `highest_step_name`, West segment only)

| Funnel stage reached | Jun | Jul | Aug |
|---|---|---|---|
| CHECKOUT_STEP (furthest, closest to booking) | 38 (9.0% of leads) | 24 (6.5%) | 20 (6.7%) |
| QUOTE_STEP | 176 (41.5%) | 178 (48.4%) | 136 (45.5%) |
| UNKNOWN (no meaningful digital progress) | 209 (49.3%) | 165 (44.8%) | 140 (46.8%) |

Overall lead-to-booking conversion for the West segment, for comparison (from Section 4.1):

| | Jun | Jul | Aug |
|---|---|---|---|
| Leads | 424 | 368 | 299 |
| Bookings | 139 | 125 | 103 |
| Conversion % | 32.8% | 34.0% | **34.4%** |

**Finding:**
- Self-service progress to CHECKOUT_STEP declined (9.0%→6.7% of leads) — a real drop, roughly double the rate of the overall lead-count decline.
- Despite that, **overall lead-to-booking conversion for this segment is stable to slightly improving (32.8%→34.4%)** — agents are converting whichever leads arrive at least as well as before, likely picking up by phone what isn't self-served through checkout.
- **Conclusion: there is no funnel-quality or agent-performance problem.** The West-segment decline is a pure top-of-funnel volume issue.

### 7.6 Section conclusion

- Leads from US/UK/Canada/Australia fell 30% (424→299), concentrated in this one nationality group.
- Real traffic from these countries fell too, but only 9-13% — smaller than the lead decline.
- The initial SEO-ranking explanation for the traffic/visibility side does not hold up — it was mostly a collapse in bot/AI-style synthetic search queries, not real demand or real ranking loss.
- The funnel itself (lead → booking) is healthy; conversion rate is unchanged or better.
- **Open / unresolved:** the gap between the ~9-13% real traffic decline and the 30% lead decline is not yet explained by anything checked in this investigation. The most likely remaining candidates — not yet verified — are a session-to-lead-form conversion drop specific to these markets, or a lead-capture/attribution issue on the site for this segment.

---

## 8. Overall conclusions

| Theme | Status |
|---|---|
| Nationality mix ("fewer Europeans") | Not supported by 3 months of data |
| Indian/Subcontinent share rising | Not supported (flat), but the conversion-rate gap behind it is real and confirmed |
| Pocket size / cash-conscious | Not supported by 3 months of data |
| PED leads declined | Volume-share claim not supported (flat), but the ATS-sensitivity mechanism is real and confirmed |
| West-segment (US/UK/CA/AU) drop | **Real and verified.** Root cause is a top-of-funnel volume gap, not a conversion, agent, or (contrary to first appearances) an SEO ranking problem. Partially explained by real traffic softening (9-13%); the remainder is unexplained. |

---

## 9. Open questions / not yet verified

- What explains the gap between the West segment's real traffic decline (9-13%, GA4) and its lead decline (30%, CRM)? Candidates: session-to-lead-form conversion rate for these markets specifically (not yet measured), or a lead-capture/attribution issue.
- No Google Ads spend data was available (Tier 3 API not configured) — the paid-channel side of the West-segment channel breakdown (Google Brand, Bing declines) has not been confirmed as a spend/bidding decision vs. a demand-side effect.
- The `pec_status` = "PED" mapping is inferred from field naming, not an explicit confirmed label.
- Whether the nationality or salary-band mix has shifted over a longer period than 3 months (e.g., year-over-year) has not been checked — this dashboard's cards are hard-filtered to a rolling 3-month window.

---

## 10. Data appendix

Raw pulls referenced in this report are Metabase card queries (cards 2158–2161, via `/api/card/:id/query`), an ad-hoc Metabase query against `leadenrichedreport_health` (table 16772) for the monthly salary-band view and the West-segment channel/funnel breakdowns, and Google Search Console / Google Analytics 4 API pulls for `sc-domain:policybazaar.ae` / `properties/309894472`. All figures in this report were retrieved directly from these sources during this investigation; none are estimated or extrapolated unless explicitly marked as "inferred" above.
