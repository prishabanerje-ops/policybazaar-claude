# Salary Band Conversion Trend — January to August 2026

**Date prepared:** 2026-09-03
**Prepared by:** Aakash Srivastava
**Related report:** `health-conversion-drop-investigation-2026-09-03.md` (Section 5 of that report covers this same "pocket size" claim over Jun-Aug only; this file extends the check back to January).

**Source:** Metabase, `leadenrichedreport_health` (table 16772), same lead/booking definitions and channel filter as the `Health_detailed_Conversion_source_Salary_band` dashboard card, queried ad hoc for a monthly breakdown (the live card itself has no date dimension). Not saved as a Metabase asset.

**Window:** January 1 – August 31, 2026 (8 full months).

---

## 1. Leads by salary band and month

| Salary band | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug |
|---|---|---|---|---|---|---|---|---|
| Below AED 4K | 7,208 | 6,272 | 4,171 | 6,250 | 5,967 | 6,792 | 7,105 | 6,456 |
| AED 4K-5K | 8,255 | 7,338 | 5,139 | 7,094 | 5,913 | 7,603 | 7,974 | 6,972 |
| AED 5K-6K | 1,618 | 1,440 | 863 | 1,309 | 993 | 1,198 | 1,294 | 1,181 |
| AED 6K-7K | 1,022 | 851 | 553 | 839 | 695 | 815 | 805 | 774 |
| AED 7K-8K | 1,109 | 934 | 574 | 878 | 753 | 860 | 1,011 | 839 |
| AED 8K-9K | 570 | 511 | 309 | 487 | 410 | 533 | 554 | 489 |
| AED 9K-10K | 1,063 | 1,020 | 589 | 964 | 845 | 1,022 | 1,230 | 1,032 |
| Above AED 10K | 5,825 | 5,086 | 2,739 | 4,623 | 4,194 | 5,310 | 5,483 | 5,104 |
| **Total** | **26,670** | **23,452** | **14,937** | **22,444** | **19,770** | **24,133** | **25,456** | **22,847** |

## 2. Bookings by salary band and month

| Salary band | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug |
|---|---|---|---|---|---|---|---|---|
| Below AED 4K | 8 | 10 | 9 | 4 | 1 | 2 | 0 | 1 |
| AED 4K-5K | 1,624 | 1,537 | 1,096 | 1,459 | 1,172 | 1,447 | 1,431 | 1,404 |
| AED 5K-6K | 346 | 401 | 236 | 313 | 231 | 262 | 296 | 263 |
| AED 6K-7K | 260 | 201 | 147 | 227 | 204 | 208 | 239 | 242 |
| AED 7K-8K | 324 | 286 | 181 | 246 | 213 | 234 | 242 | 213 |
| AED 8K-9K | 130 | 131 | 67 | 97 | 94 | 115 | 100 | 121 |
| AED 9K-10K | 258 | 275 | 127 | 235 | 184 | 201 | 237 | 198 |
| Above AED 10K | 1,667 | 1,438 | 721 | 1,271 | 1,217 | 1,374 | 1,435 | 1,524 |

## 3. Derived: conversion % by band and month

| Salary band | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug |
|---|---|---|---|---|---|---|---|---|
| Below AED 4K | 0.11% | 0.16% | 0.22% | 0.06% | 0.02% | 0.03% | 0% | 0.02% |
| AED 4K-5K | 19.68% | 20.95% | 21.33% | 20.57% | 19.82% | 19.03% | 17.95% | 20.14% |
| Above AED 10K | 28.62% | 28.28% | 26.32% | 27.49% | 29.02% | 25.88% | 26.17% | 29.86% |

(Other bands not tabulated here — checked and found similarly stable across the 8 months; available on request.)

## 4. Derived: "tight budget" segment share of total leads

Below AED 4K + AED 4K-5K combined, as a % of that month's total leads:

| Jan | Feb | Mar | Apr | May | Jun | Jul | Aug |
|---|---|---|---|---|---|---|---|
| 58.0% | 58.0% | 62.3% | 59.5% | 60.1% | 59.7% | 59.2% | 58.8% |

---

## 5. Findings

- **March 2026 is a real outlier in total volume**: 14,937 leads, ~44% below January (26,670) and well below every neighboring month. This report does not confirm a cause — flagging as unconfirmed context, not a verified finding — but the timing coincides with Ramadan, which commonly reduces UAE-market lead volume. This has not been independently verified and should not be treated as established fact.
- The "tight budget" segment (Below AED 4K + AED 4K-5K) holds a **58-62% share of leads every month**, with no rising trend. The one elevated month (March, 62.3%) tracks with that month's overall low volume, not a genuine mix shift.
- **Below AED 4K conversion** (bookings are single digits every month — treat as directional only, not statistically reliable): there is a real step-down after March (0.11%→0.16%→0.22% Jan-Mar, then 0.06% or lower every month April onward). Directionally real, but the absolute counts (0-10 bookings/month) are too small to be a material driver of overall conversion.
- **Above AED 10K conversion** (28.6% → 28.3% → 26.3% → 27.5% → 29.0% → 25.9% → 26.2% → 29.9%) and **AED 4K-5K conversion** (19.7% → 21.0% → 21.3% → 20.6% → 19.8% → 19.0% → 18.0% → 20.1%) are both stable across all 8 months — no decline in either.

## 6. Conclusion

Extending the "pocket size" check from 3 months to 8 months does not change the earlier verdict: **there is no evidence that salary mix or income-band conversion is deteriorating over January-August 2026.** Mix and conversion by income band are largely flat outside the March seasonal dip. The one real signal — the already-near-zero Below-AED-4K segment getting even closer to zero after March — is directionally genuine but too small in absolute terms to be material to the overall funnel.
