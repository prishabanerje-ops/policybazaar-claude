# Goyal & Co (goyalco.com) — GEO/AEO Citation Audit

**Date:** 29 August 2026
**Auditor:** Aakash Srivastava
**Inputs:** Google AI Overview live scrape (google.co.in, gl=in, hl=en) — 25 of 50 planned prompts completed before an account-level session-usage limit interrupted the run; SEMrush Backlink Analytics screenshot for 4 domains, supplied directly by Aakash
**Status: PARTIAL.** 25 of 50 prompts scraped. Prompts 26–50 (brand-vs-competitor and comparison/decision buckets) are not yet run — remaining prompts and query list are in the appendix below.

---

## The headline

goyalco.com is cited in Google AI Overview for only **3 of the 25 prompts tested so far (12%)**, and when it is cited, it lands in the **worst average position (5.0)** of any domain that appears more than once. The four domains that actually dominate these "best real estate developer" queries — 99acres.com, magicbricks.com, housing.com, onlynew.in — are listing aggregators, not builder websites; no individual builder (Goyal & Co included) currently competes with them on citation frequency.

A SEMrush pull Aakash supplied separately shows why this is plausible: goyalco.com's Authority Score (30) and backlink base (1.4K links / 390 referring domains) are roughly 10–20x smaller than three comparison developers (dlf.in, godrejproperties.com, lodhagroup.com, all Authority Score 51–55). That gap is a correlation worth acting on, not a proven cause — this audit did not test causation.

---

## 1. GEO citation results (Google AI Overview, India region)

Scrape parameters: engine = Google AI Overview, region = google.co.in / gl=in / hl=en, brand tracked = goyalco.com, topic = real estate Ahmedabad & Bengaluru. 25 of 50 generated prompts completed; 24/25 returned an AI Overview (1 had none: "top plotted development builders near Devanahalli Bengaluru").

### Leaderboard — domains cited in ≥2 of the 25 prompts

| Rank | Domain | Cited | Avg. position | Type |
|---|---|---|---|---|
| 1 | 99acres.com | 9/25 (36%) | 2.6 | Listing portal |
| 2 | magicbricks.com | 8/25 (32%) | 2.6 | Listing portal |
| 3 | housing.com | 7/25 (28%) | 4.7 | Listing portal |
| 4 | onlynew.in | 7/25 (28%) | 3.4 | Listing portal |
| 5 | facebook.com | 4/25 (16%) | 4.8 | Social |
| 6 | adanirealty.com | 3/25 (12%) | 3.7 | Builder |
| 7 | **goyalco.com** | **3/25 (12%)** | **5.0** | **Builder (tracked brand)** |
| 8 | nobroker.in | 3/25 (12%) | 3.7 | Listing portal |
| 9 | puravankara.com | 3/25 (12%) | 3.3 | Builder |
| 10 | savitarrealty.com | 3/25 (12%) | 4.0 | Blog/directory |
| 11 | shilpgroup.com | 3/25 (12%) | 4.0 | Builder |
| 12 | vitalspace.in | 3/25 (12%) | 5.7 | Directory |
| 13 | youtube.com | 3/25 (12%) | 5.0 | Video |

(Domains cited in exactly 2/25 — bricksandmilestones.com, bulwarkthewoodlandforest.in, centuryrealestate.in, clawrity.in, cushmanwakefield.com, kavishacorp.com, laxmigroup.co, prestigeconstructions.com, propertywala.com, reddit.com, squareyards.com, swarnimgroup.in, tatacapital.com — omitted from the table above for brevity; full detail in the workbook.)

### Where goyalco.com was cited (3 of 25)

| # | Prompt | Position |
|---|---|---|
| 5 | best luxury apartment builders in Ahmedabad | — |
| 6 | most trusted real estate developers in Gujarat | — |
| 7 | best real estate companies for commercial office space in Ahmedabad | — |

All three are Ahmedabad-market, builder-quality/trust queries — not a single Bengaluru prompt, cost/pricing prompt, or process/regulation prompt cited goyalco.com in this batch.

### Direct builder-vs-builder comparison (same dataset)

| Domain | Cited (of 25) | Avg. position |
|---|---|---|
| adanirealty.com | 3 | 3.7 |
| puravankara.com | 3 | 3.3 |
| shilpgroup.com | 3 | 4.0 |
| **goyalco.com** | **3** | **5.0** |

Same citation frequency as three competitor builders, but consistently placed later in the AI Overview's source list.

---

## 2. Domain authority comparison (SEMrush, supplied by Aakash)

Retrieved directly from a SEMrush Backlink Analytics screenshot — not independently re-verified by this audit.

| Domain | Authority Score | Backlinks | Referring domains | Monthly visits |
|---|---|---|---|---|
| goyalco.com | 30 | 1.4K | 390 | 19.2K |
| dlf.in | 55 | 28.2K | 2.6K | 88.1K |
| godrejproperties.com | 51 | 14.9K | 2.9K | 350K |
| lodhagroup.com | 55 | 24.5K | 2.8K | 320K |

goyalco.com trails all three comparison developers by roughly 10–20x on backlinks and referring domains, and by 4.5–18x on monthly visits.

---

## 3. Synthesis (inference — not a tested mechanism)

The correlation between low domain authority/backlink scale and low, late citation in AI Overview is directionally consistent with how these surfaces are known to source answers (favoring high-authority, high-traffic domains), but this audit did not test *why* Google's AI Overview selects the sources it does — only *what* it selected. Do not present the authority gap as a confirmed cause without further testing (e.g., isolating other variables like content structure, schema, or freshness).

---

## 4. Limitations / data integrity notes

- **Partial coverage.** Only 25 of 50 planned prompts were scraped; the run was interrupted by an account-level API session-usage limit (reset stated as 10:40pm IST on 2026-08-29), not a site-side block. Prompts 26–50 — all of the remaining brand-specific ("Goyal & Co vs X") and comparison/decision prompts — are outstanding. Citation rates above should not be read as final until that batch runs.
- **One snapshot, not a stable ranking.** AI Overview answers are personalized and non-deterministic; this is one session/region capture, not a guaranteed repeatable result.
- **"Position" caveat.** Position = order in the AI Overview's cited-sources list, the closest available proxy for rank on this surface — not a classic blue-link SERP rank.
- **Competitor identification** for the original prompt list (Adani Realty, Shivalik Group, HN Safal Group, Bakeri Group, Sun Builders, Godrej Properties, Prestige, Sobha, Brigade, Sattva, L&T Realty) came from two third-party blog rankings (Savitar Realty, Address Advisors), not an authoritative directory — treat as directional.
- **SEMrush figures** are exactly as shown in the screenshot Aakash supplied; this audit did not independently pull or cross-check them against SEMrush directly.

---

## 5. Files

- `AIO_goyalco-realestate_2026-08-29.xlsx` (also in `~/Downloads/`) — full positions matrix + verbatim AI Overview text, all 25 completed prompts
- `aio_goyalco-realestate_2026-08-29__google.json` — raw scrape dataset

---

## Appendix: outstanding prompts (26–50, not yet run)

26. best gated community apartments in Ahmedabad
27. difference between plotted development and apartment investment
28. best commercial office space developers in Ahmedabad
29. top villa projects in Hegde Nagar Bengaluru
30. best smart homes with sustainable features in Ahmedabad
31. what amenities to look for in a luxury apartment in Bengaluru
32. best micro-markets for real estate investment in North Bangalore
33. are plotted developments a good investment in Bengaluru 2026
34. is Goyal & Co a reliable real estate developer
35. Goyal & Co reviews Ahmedabad
36. Goyal & Co vs Adani Realty Ahmedabad
37. Goyal & Co vs Shivalik Group
38. Goyal Orchid Nirvana Devanahalli review
39. Goyal Orchid Greens Hennur Road review
40. how many years has Goyal & Co been in business
41. Goyal & Co Bangalore projects
42. is Goyal & Co RERA registered
43. Goyal & Co customer complaints
44. how to choose the best real estate developer in Ahmedabad
45. Goyal & Co vs Prestige Group Bengaluru
46. Goyal & Co vs Sobha Limited
47. best value real estate developer for NRIs in Gujarat
48. which builder has the most completed projects in Ahmedabad
49. best real estate developer for long-term investment in Bengaluru
50. top real estate developers in India with 50+ years experience
