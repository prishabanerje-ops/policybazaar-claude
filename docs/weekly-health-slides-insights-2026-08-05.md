# Weekly Health Insurance deck — slide copy

**Prepared:** 5 August 2026 · **Deck:** Weekly Health_Insurance_Weekly, slides 3 and 6
**Basis:** full Jul 2026 vs full Jun 2026. Both subtitles need changing off MTD / 1st–15th.

---

## SLIDE 3 — MoM Performance, Health Insurance

Subtitle: `Jul 2026 vs Jun 2026`

### KEY INSIGHTS

**Schema and on-page work is showing up in rank; CTR is now the gap**

- Top 10 Companies page (ItemList/Carousel schema) - clicks 11 → 66, impressions 19.5K → 40.1K, rank 16.5 → 13.1
- Companies head terms all climbed but return nothing - "best health insurance in UAE" 21.3 → 14.7 on 1,101 impressions and 0 clicks; "best medical insurance in UAE" 20.0 → 15.3 on 564 impressions and 1 click
- Fewer impressions, converting harder - clicks −12% and impressions −31%, but CTR 0.39% → 0.50% and organic sessions 4,427 → 4,838 (+9%)
- Two pages gave back the gain - status-check article 784 → 504 clicks (rank 6.2 → 7.4); Medical Insurance hub flat at 220 clicks as rank slid 16.0 → 21.4

### ACTIVITIES

**Refurbished Medical Insurance hub, DIC & Hayah provider pages**

- Rewrote Title/Meta/H1 on Health & Medical Insurance hub pages
- Internal linking pass (~3,914 link mappings)
- Added ItemList/Carousel schema to Top 10 Companies page
- Widget placement change on hub page

---

## SLIDE 6 — ChatGPT Channel, Health Insurance

Subtitle: `Jul 2026 vs Jun 2026`

### KEY INSIGHT

- Health took more of the channel - sessions 491 → 612 (+25%) against site-wide ChatGPT +13%; health share 17.2% → 18.9%
- Conversion outpaced traffic - key events 630 → 1,051 (+67%), 1.28 → 1.72 per session
- Breadth stopped shrinking - 219 health pages drew sessions in both Jun and Jul, against 496 in Jan. Volume recovered on fewer, stronger pages

### ACTIVITIES

**Refurbished the status-check article for impression recovery**

Added Service, InsuranceAgency, FinancialService schema + expanded existing schema - structured data aimed at AI-agent/LLM discoverability, the surface ChatGPT draws citations from

- Queued: strip trailing double-slashes at the routing layer - 91 of 612 health sessions (15%) land on `/health-insurance//` style URLs. They return 200 and canonical correctly, so rank is safe, but reporting splits into two rows per page

**Compared with Jan**

- Breadth halved, then held - ChatGPT drew sessions across 496 health pages in Jan, 219 in Jun, 219 in Jul
- One page died - cheapest-expat article now 301-redirects to medical-insurance, 0 GSC impressions
- One page recovered - top-10-companies page back to 14.7 and 15.3 on "best health insurance in UAE" and "best medical insurance in UAE", from 21.3 and 20.0 in Jun

---

## Notes

- Metric cards (Leads, Bookings, APE, ATS, CR, V2L) are internal BI and still need a full-July refresh. No lead figures are carried in the copy above, so nothing on these slides depends on an unverified number.
- Health scope for GSC and GA4 is regex `health-insurance|medical-insurance|hiart|hipvd|hic/` on property `https://www.policybazaar.ae/` and GA4 `309894472`. This includes group-health (`*-hic/`) and Arabic (`/ar-ae/`) pages. Direction holds either way; absolute clicks move if you exclude them.
- The 16th–31st July activity log was not available, so ACTIVITIES covers the first half plus the queued routing fix.
- Dropped from the previous draft: the "#2 organic" claim (full-July GSC average is 5.5, not 2 or 3) and the "95 → 45 pages" figure (GA4 gives 496 → 219 on this regex).
