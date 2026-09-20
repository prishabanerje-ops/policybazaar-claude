# Health Insurance Conversion Trends — January–August 2026 Investigation Report

**Date prepared:** 2026-09-03
**Prepared by:** Aakash Srivastava
**Purpose:** Extends the original 3-month check (`health-conversion-drop-investigation-2026-09-03.md`, which covered June–August 2026 only) back to January 2026, for the same three themes: nationality mix, pocket size, and PED leads. This wider window changes two of the three conclusions — flagged clearly below rather than left buried in tables.

---

## 1. Data sources and scope

| Source | What it provided |
|---|---|
| Metabase, source table `leadenrichedreport_health` (table 16772) | Lead/booking counts, conversion %, APE, by nationality, salary band, and PED (`pec_status`) |

Same lead/booking definitions and marketing-channel filter used throughout the original investigation (only `Lead`/`Booking` rows attributed to the standard digital/CRM channel list; excludes Renewal, Retention, agent_upload, Inbound, and similar non-acquisition sources). All queries below were built ad hoc for this report and are not saved as permanent Metabase assets.

**Window:** January 1 – August 31, 2026 (8 full months). September is excluded — as of this report's date (Sept 3), it has only 3 days of data.

**Consistency check:** monthly lead totals summed independently from the nationality breakdown and the salary-band breakdown match exactly for every month checked (e.g. January: 26,670 both ways) — confirming both are drawing from the same underlying lead population.

---

## 2. Findings against each of the four factors

Based on the full January–August 2026 data (see Section 4 onward for the underlying detail):

**Nationality mix — fewer Europeans.** Not supported as a continuous trend. There was a real step-down in combined Europe + West share from ~7.3-7.4% in January-February to ~5.8-6.3% from March onward (Section 4.3), but it has held flat at that lower level for the six months since — a one-time shift early in the year, not an ongoing "changing mix." The West segment (US/UK/Canada/Australia) specifically has a confirmed, concrete driver behind part of its swing, not just unexplained volatility (Section 4.4).

**Higher share of Indian & Indian Subcontinent customers, longer cycle.** The share claim is not supported: Indian + Pakistani + South Asian leads have held a flat 52-55% of the total lead base in every one of the 8 months, not risen. What *is* confirmed, and strongly: this group converts at 15.6-24.0% every month, while European-origin leads convert at 23.3-43.2% every month, with zero exceptions across all 8 months (Section 4.2). This is the most robust finding in the whole investigation — the conversion-speed mechanism the sales team is describing is real, even though the "mix is changing" framing isn't.

**Pocket size is an issue.** Not supported over 8 months. Income-band mix and conversion by band are both stable; the lowest-income segment's already-near-zero conversion did step down further after a March volume dip, but the absolute numbers involved (0-10 bookings/month) are too small to be a material driver of overall conversion (full detail in `health-salary-band-trend-jan-aug-2026.md`).

**PED leads have declined.** **Contradicted by the data.** PED's share of total leads did not decline — it rose, from ~5.3% of leads in January-May to ~7.3% in June-August (Section 6.3). Part of that rise (roughly 0.5 percentage points) is a mechanical side-effect of a marketing channel loss described below, not a real behavior change — but even after adjusting for that, a real increase remains. PED bookings also carry a consistent 3.5x-9x ticket-size premium over regular bookings, in every month checked. PED is a growing part of the lead base with an outsized effect on blended ATS, not a shrinking one.

**A cross-cutting finding that affects several of the above: a major lead channel disappeared entirely.** WhatsApp-sourced leads ran 2,185-3,105 per month sitewide from January through April, then dropped to zero every month from May onward — not a gradual decline, a clean cutoff. This is confirmed and quantified in Section 4.4. WhatsApp is banned for insurance solicitation in the UAE, which explains the clean regulatory-driven cutoff rather than a tracking break. Worth confirming what, if anything, has replaced this ~2,500 leads/month gap since the ban took effect.

**On levers across Paid Marketing, Brand/Social and Organic:** the confirmed findings point to specific, data-backed areas rather than a broad push across all three channels:
1. The Indian-subcontinent conversion gap — confirmed and robust across all 8 months — is worth investigating for what in the funnel or messaging is driving the longer cycle for this segment specifically.
2. PED is growing, not shrinking, and carries a large ticket-size premium — worth treating as a segment to protect and grow, not one to "recover."
3. The WhatsApp channel's disappearance is explained (banned for insurance solicitation in the UAE), but the resulting ~2,500 leads/month gap is real and larger than any of the four original factors. Worth confirming what channel, if any, has been built to replace that volume.

No lever recommendations are made for the nationality-mix or pocket-size claims, since the data does not show an ongoing problem there to fix.

---

## 3. Executive summary — what changed vs. the 3-month report

| Theme | 3-month (Jun-Aug) verdict | 8-month (Jan-Aug) verdict |
|---|---|---|
| Nationality mix / Europe | Not supported — Europe flat | **Still not supported for Europe overall — but see West-segment correction below.** |
| Indian/Subcontinent share | Not supported — flat ~53-55% | **Confirmed still not supported** — flat ~52-55% across all 8 months. |
| Conversion gap (Indian-subcontinent vs. European-origin) | Confirmed | **Still confirmed**, now over 8 months. |
| Pocket size | Not supported | **Still not supported** — see dedicated file `health-salary-band-trend-jan-aug-2026.md` for full 8-month tables. |
| PED leads declined | Share flat ~7.2-7.4%/month | **Correction: PED share was NOT flat — it rose.** Jan-May averaged ~5.3% of leads; Jun-Aug averaged ~7.3%. The 3-month window happened to sit entirely inside the higher plateau, which made it look flat. Over 8 months, PED share is *up*, not down and not flat. |
| West segment (US/UK/CA/AU) | "Real, verified" 30% decline, Jun (424) → Aug (299), root-caused as a top-of-funnel volume gap | **Correction: not a clean decline.** West leads were 486 (Jan) → 410 (Feb) → 199 (Mar) → 315 (Apr) → 259 (May) → 424 (Jun) → 368 (Jul) → 299 (Aug). Three concrete contributors identified: the WhatsApp channel going to zero from May, a sitewide March seasonal dip, and an unexplained Google Brand spike in June. See Section 4.4. |
| Sitewide channel loss (WhatsApp) | Not checked | **New finding.** 2,185-3,105 leads/month sitewide, Jan-Apr, then zero every month from May onward. Explained: WhatsApp is banned for insurance solicitation in the UAE. Larger in volume than any of the four original factors. |

**The three corrections above (PED, West, and the WhatsApp channel loss) are the important takeaways from this wider window.**

---

## 4. Nationality mix

### 4.1 Leads by nationality group and month

| Nationality group | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug |
|---|---|---|---|---|---|---|---|---|
| Indian | 10,177 | 8,831 | 5,474 | 8,896 | 8,302 | 9,887 | 9,671 | 8,743 |
| Pakistani | 2,936 | 2,655 | 1,787 | 2,348 | 1,900 | 2,492 | 2,723 | 2,456 |
| South Asian | 1,033 | 900 | 542 | 883 | 764 | 975 | 1,025 | 885 |
| Arab | 2,541 | 2,206 | 1,536 | 2,198 | 1,759 | 2,202 | 2,607 | 2,383 |
| Western Europe | 1,212 | 1,082 | 536 | 812 | 771 | 874 | 928 | 953 |
| Eastern Europe | 258 | 239 | 135 | 171 | 164 | 215 | 198 | 189 |
| West (US/UK/Canada/Australia) | 486 | 410 | 199 | 315 | 259 | 424 | 368 | 299 |
| Africa | 625 | 613 | 350 | 506 | 523 | 555 | 640 | 520 |
| Philippines | 1,797 | 1,510 | 962 | 1,349 | 1,267 | 1,832 | 2,164 | 1,660 |
| Middle East (Non-Arab) | 444 | 415 | 236 | 335 | 329 | 380 | 446 | 411 |
| Russia | 211 | 200 | 171 | 157 | 136 | 167 | 157 | 165 |
| South American | 150 | 132 | 77 | 113 | 119 | 105 | 132 | 136 |
| China | 47 | 46 | 37 | 40 | 35 | 48 | 71 | 41 |
| Unknown | 4,753 | 4,213 | 2,895 | 4,321 | 3,442 | 3,977 | 4,326 | 4,006 |
| **Total** | **26,670** | **23,452** | **14,937** | **22,444** | **19,770** | **24,133** | **25,456** | **22,847** |

### 4.2 Conversion % — Indian-subcontinent group vs. European-origin group, by month

| Group | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug |
|---|---|---|---|---|---|---|---|---|
| Indian | 18.7% | 20.7% | 20.6% | 19.9% | 19.8% | 18.5% | 18.5% | 20.3% |
| Pakistani | 19.4% | 18.9% | 18.3% | 18.7% | 15.6% | 17.8% | 17.6% | 22.9% |
| South Asian | 19.4% | 20.6% | 21.8% | 24.0% | 19.9% | 21.4% | 19.1% | 17.2% |
| Western Europe | 35.1% | 33.6% | 32.5% | 34.1% | 27.5% | 28.4% | 29.3% | 30.3% |
| Eastern Europe | 34.5% | 31.0% | 35.6% | 39.2% | 31.7% | 23.3% | 26.8% | 27.0% |
| West | 35.4% | 43.2% | 35.7% | 33.0% | 27.0% | 32.8% | 34.0% | 34.4% |

**Finding:** across all 8 months, the Indian/Pakistani/South Asian group converts in a 15.6-24.0% range, while the three European-origin groups convert in a 23.3-43.2% range. The gap holds in every single month with no exception — this is the most robust finding in the entire investigation, now confirmed over 8 months instead of 3.

### 4.3 Derived shares of total leads

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug |
|---|---|---|---|---|---|---|---|---|
| Indian + Pakistani + South Asian | 53.0% | 52.8% | 52.2% | 54.0% | 55.5% | 55.3% | 52.7% | 52.9% |
| Western Europe + Eastern Europe | 5.5% | 5.6% | 4.5% | 4.4% | 4.7% | 4.5% | 4.4% | 5.0% |
| Western Europe + Eastern Europe + West | 7.3% | 7.4% | 5.8% | 5.8% | 6.0% | 6.3% | 5.9% | 6.3% |

**Finding:** the Indian-subcontinent share is flat/noisy in a 52-55% band all year — no rising trend. The combined European + West share shows a mild step-down from ~7.3-7.4% in January-February to ~5.8-6.3% from March onward, then holds roughly flat for the remaining 6 months. This is a real pattern but it is a one-time step in Q1, not a continuous "getting worse" trend through the year.

### 4.4 West segment (US/UK/Canada/Australia) — what actually explains the pattern

The original investigation (Jun-Aug only) found West leads falling 424→368→299 and treated this as a confirmed, real decline worth a full root-cause investigation (GSC, GA4, funnel — see the original report, Section 7). Extending back to January changes the picture:

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug |
|---|---|---|---|---|---|---|---|---|
| West leads | 486 | 410 | 199 | 315 | 259 | **424** | 368 | 299 |
| West bookings | 172 | 177 | 71 | 104 | 70 | 139 | 125 | 103 |
| West conversion % | 35.4% | 43.2% | 35.7% | 33.0% | 27.0% | 32.8% | 34.0% | 34.4% |

West lead volume is volatile across the whole 8 months (low of 199 in March, high of 486 in January), and June (424) is itself a local peak coming out of a May trough (259) — not the start of a decline. Rather than leaving this as "it's just volatile," the channel breakdown for West across all 8 months identifies three concrete, verified contributors:

**1. A sitewide channel disappeared — WhatsApp.** Within West specifically, this channel delivered 59 (Jan), 43 (Feb), 17 (Mar), 37 (Apr) leads, then **zero every month from May onward**. Checking the same channel across the *entire* lead base (not just West) confirms this is not West-specific: sitewide WhatsApp volume was 3,105 (Jan), 2,817 (Feb), 2,185 (Mar), 2,751 (Apr), then zero from May onward — a clean, total cutoff, not a gradual decline. WhatsApp is banned for insurance solicitation in the UAE, which explains this as a regulatory-driven shutdown rather than a tracking break.

**2. Google Search for West tracks the sitewide seasonal pattern.** West's Google Search leads by month — Jan 192, Feb 153, Mar 61, Apr 109, May 102, Jun 155, Jul 136, Aug 120 — dip hardest in March and partially recover afterward — the same shape seen in total sitewide lead volume across every dimension checked in this report (see the March-dip note in Sections 4.3 and 6.3, and the dedicated salary-band file). This portion of West's swing is consistent with a sitewide seasonal effect, not something specific to West.

**3. Google Brand for West peaked in June specifically (71 leads, its high for the entire 8-month window) and has since declined to 40 by August.** This does not track the WhatsApp cutoff (which happened in May) or the general seasonal pattern, and no cause for this specific spike-and-decline has been identified in this investigation. This remains open.

**Bottom line for West:** part of the pattern (the WhatsApp loss, roughly 17-59 leads/month depending on the month) is a real, confirmed, sitewide cause; part of it (the March dip) tracks a sitewide seasonal effect rather than anything West-specific; and part of it (the Google Brand June spike and subsequent decline) remains unexplained. Combined with West being under 2% of total leads every month (naturally higher relative variance from small numbers), there is no basis for calling this a clean, isolated "30% decline" — but it is also not simply unexplainable noise. The real GA4 traffic-softening and corrected GSC/bot-noise findings from Section 7 of the original report remain accurate observations about June-August specifically.

---

## 5. Pocket size (salary band)

Full 8-month tables (leads, bookings, conversion % by band, and the "tight budget" share) are in the companion file `health-salary-band-trend-jan-aug-2026.md`. Summary: no evidence of a worsening trend in either the income-band mix (flat 58-62% "tight budget" share every month) or conversion by band (both AED 4K-5K and Above-AED-10K conversion are stable across all 8 months). One real but statistically fragile signal: Below-AED-4K conversion (already near zero) stepped down further after a March dip in absolute lead volume — see that file for the full breakdown and the unconfirmed Ramadan-timing note on the March dip.

---

## 6. PED leads (`pec_status`) — correction from the 3-month finding

### 6.1 Data

| pec_status | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug |
|---|---|---|---|---|---|---|---|---|
| **Yes (PED proxy) — leads** | 1,426 | 1,171 | 651 | 1,171 | 1,169 | 1,736 | 1,891 | 1,663 |
| Yes — bookings | 16 | 15 | 8 | 16 | 10 | 13 | 23 | 16 |
| Yes — APE | 437,722.96 | 407,993.44 | 112,870.44 | 271,978.90 | 105,834.67 | 188,635.67 | 343,276.36 | 395,854.63 |
| No — leads | 20,231 | 17,775 | 10,955 | 16,685 | 15,114 | 18,350 | 19,060 | 17,067 |
| No — APE | 12,614,631.12 | 10,946,403.17 | 6,782,783.86 | 9,499,506.33 | 7,824,467.07 | 9,652,237.98 | 9,565,209.56 | 9,633,335.51 |

### 6.2 Derived

| | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug |
|---|---|---|---|---|---|---|---|---|
| PED share of total leads | 5.35% | 4.99% | 4.36% | 5.22% | 5.91% | **7.19%** | **7.43%** | **7.28%** |
| PED conversion % | 1.12% | 1.28% | 1.23% | 1.37% | 0.86% | 0.75% | 1.22% | 0.96% |
| APE per booking, PED | ~27,360 | ~27,200 | ~14,110 | ~17,000 | ~10,580 | ~14,510 | ~14,930 | ~24,740 |
| APE per booking, non-PED | ~3,285 | ~3,020 | ~3,125 | ~2,985 | ~2,815 | ~3,020 | ~2,940 | ~3,000 |

### 6.3 Finding — this is the headline correction of this report

**PED share of total leads did not decline, and was not flat — it rose.** January-May averages ~5.3% (ranging 4.4-5.9%); June-August averages ~7.3% (ranging 7.2-7.4%). The original 3-month report checked exactly the window where the share had already stepped up and stayed there, which is why it looked "flat" — it was flat *at an elevated level*, and that elevation itself is the real story once you look further back.

**Part of this rise has a confirmed, mechanical explanation, not a behavioral one.** Section 4.4 identifies that WhatsApp-sourced leads (2,185-3,105/month sitewide, Jan-Apr) disappeared entirely from May onward. Checking that channel's own composition (Jan-Apr): only 1.4% of its leads were PED-declared (152 of 10,858), well below the ~5.3% sitewide average over the same period — WhatsApp leads skewed heavily toward "No" or "Not Declared" PED status, likely because a low-friction bot channel does not prompt for a health declaration the way other channels do. Removing a large pool of disproportionately non-PED leads mechanically raises the PED share of what remains. Applying WhatsApp's Jan-Apr PED ratio to April's actual volume as an estimate: April's real PED share was 5.22%; with WhatsApp removed from the denominator, the estimated share rises to ~5.75% — accounting for roughly 0.5 percentage points of the total ~2-point increase seen by June-August. **The remaining ~1.5 percentage points of increase (from an adjusted ~5.75% baseline to ~7.3%) is not explained by this channel loss and has no confirmed cause yet.**

The ticket-size premium finding still holds and is now confirmed over a longer window: PED bookings carry roughly 3.5x to 9x the APE of a non-PED booking, in every single month checked, with no exception.

**Net: PED leads have not declined — their share has grown, and only part of that growth is a measurement artifact.** This is the most actionable correction in this report.

---

## 7. Overall conclusions

- The Indian-subcontinent vs. European-origin conversion gap is the single most robust finding in this entire investigation — confirmed in every one of 8 months, no exceptions.
- Pocket size shows no worsening trend over 8 months, consistent with the 3-month check.
- **PED leads have not declined — their share of the lead base rose from ~5.3% (Jan-May) to ~7.3% (Jun-Aug), the opposite of the original claim.** Roughly a quarter of that rise is a mechanical side-effect of the WhatsApp channel loss (Section 6.3); the rest is a real, unexplained increase. Combined with the already-confirmed ticket-size premium, PED is a growing, not shrinking, factor in blended ATS.
- **The West-segment pattern has a real, partly-identified cause, not just "volatility."** The WhatsApp channel (~2,200-3,100 leads/month sitewide) went to zero starting in May, which affected West's Jan-Apr baseline; a March dip tracks the same sitewide seasonal pattern seen everywhere in this report; and a June spike in Google Brand leads for West has no identified cause. The root-cause work already done on the traffic/SEO/funnel side for June-August (original report, Section 7) is not invalidated by any of this.
- **The disappearance of the WhatsApp channel (sitewide, ~2,200-3,100 leads/month, gone entirely from May onward) is the single biggest event found in this investigation** — larger in volume than any of the four original factors. It is explained (WhatsApp is banned for insurance solicitation in the UAE), but the resulting lead-volume gap is real and worth addressing.

---

## 8. Open questions / not yet verified

- WhatsApp's disappearance is explained (banned for insurance solicitation in the UAE). Still open: **has any replacement channel been built for the ~2,200-3,100 leads/month gap this left**, and if so, is it captured under a different `parent_customutmsource` value that would need to be added to the standard channel filter used throughout this report and the original investigation?
- What explains the remaining ~1.5 percentage-point rise in PED share (Section 6.3) after accounting for the WhatsApp mix-shift effect — no cause identified yet.
- What caused Google Brand leads for West to peak in June specifically (71, the 8-month high) and decline afterward (Section 4.4) — not checked; would need actual spend/bid data, which is not available (no Google Ads API access).
- The March-wide volume dip (visible in every dimension checked — total leads, nationality, salary band, and within West's own Google Search channel) still has no confirmed cause; the Ramadan-timing note remains unverified context, not fact.
- The `pec_status` = "PED" field mapping is still inferred from field naming, not an explicit confirmed label (see the original report, Section 6, for detail).

---

## 9. Data appendix

All figures in this report were retrieved via ad-hoc Metabase queries against `leadenrichedreport_health` (table 16772) during this session, using the same lead/booking/channel definitions as the original investigation's cards. None are estimated or extrapolated unless explicitly marked as inferred or unconfirmed above.
