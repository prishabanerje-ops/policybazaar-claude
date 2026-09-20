# Weekly Health deck — slides 7, 9 and 10

**Prepared:** 5 August 2026 · **Deck:** `Weekly Health_Insurance_Weekly.pptx`, 11 slides
**Slide 7 source:** `prompt_rankings_2026-08-05_05-50.csv` - 36 prompts × 2 engines × 19 daily passes, pulled 05:50 on 5 Aug
**Slides 9 and 10 source:** the same CSV, plus `weekly-health-slides-insights-2026-08-05.md` (full Jul vs full Jun GSC/GA4), the byline crawl of 31 Jul, and the five-lens audit state file
**Companion:** `weekly-health-slides-insights-2026-08-05.md` covers slides 3 and 6

Slides 9 and 10 are currently the July monthly deck's slides 10 and 11, carried over unchanged. Every figure on them predates 16 July. Copy below replaces them.

**Built deck:** `~/Downloads/Weekly Health_Insurance_Weekly - slides 7-9-10 updated.pptx` - the same 11-slide deck with slides 7, 9 and 10 rewritten in place. Text was written into the existing runs, so every font, size, colour and shape position is inherited. Verified: 11 slides in and out, zero shape-count or geometry differences.

## Two judgement calls in the built deck

1. **Slide 7's right-panel chips show ChatGPT visibility, not the gap.** The chip boxes are 1.07" wide, which will not reliably hold `53% → 0%` at 16pt. So the chips read `53%` `42%` `42%` `26%` and the panel header carries the other half: "Won on ChatGPT, zero on Google's AI". If you would rather the chip show the zero, widen those four boxes to 1.43" first, to match the left panel.
2. **Slide 9's status chips were left untouched, which fixed the card order.** The pill fill colour encodes status (green for shipped/live, amber for in progress), and the fill is not something the text swap changes. So each card was assigned to a slot whose existing status already matched. Two consequences worth knowing: the five-lens card keeps a `LIVE` chip although the pipeline is stalled, with "No batches since 13 Jul" in the detail line; and the disclaimer card sits in a `SHIPPED` slot because the copy is approved and the credentials verified, not because it is deployed. Deployment is on slide 10's queued note. Change either chip if that reads wrong to you.

Fit was checked numerically, paragraph by paragraph, against the string each one replaced. Nothing came out longer in estimated line count. No renderer is installed on this machine, so that is an estimate rather than a visual check - worth a quick look at the three slides before you present, especially in Google Slides, whose autofit differs from PowerPoint's.

---

## Read this before you present

1. **Slide 7 is not a like-for-like update.** The old slide came from 30 prompts × 5 passes, Google AI Overview only, scored as position in the cited-sources panel. The new file is 36 prompts × 19 passes across two engines, scored as share of answers plus average cite position. Only 3 of the 7 prompts on the current slide appear in the new file. Do not present any prompt as improved or declined against the June slide.
2. **The slide 9 footer cites the wrong Search Console property.** It reads `sc-domain:policybazaar.ae`. That property is missing 95 consecutive days of its own reporting, 5 Oct 2025 to 7 Jan 2026. Switch both footers to `https://www.policybazaar.ae/`, which is what the July-vs-June figures below were measured on.
3. **Do not quote the CSV's `Topic Volume` column as search volume.** All 36 prompt/topic pairs carry a different volume on the ChatGPT row than on the AI Overview row for the same prompt and topic. `affordable health insurance in dubai` reads 997 on one and 66,600 on the other. It is a per-engine cluster figure, not prompt demand.
4. **4 of the 36 prompts are not UAE prompts.** `cheap health insurance` and `health insurance for kids` resolve to topic "US Health Insurance Marketplace", `health insurance for senior citizens` to "Senior Health Insurance in India", `health insurance for family` to "Health Care & Health Insurance". So the 31.6% on `cheap health insurance` is not UAE demand. Excluding all four: ChatGPT 21 of 32, AI Overview 7 of 32. Localise or drop them before the next pull.
5. **Deck-wide date inconsistency.** Slides 1, 3, 6, 8 and 11 still say June 2026 or "1st-15th Jul". The content is July. Slide 8's divider reads "Health Insurance · June 2026".

---

# SLIDE 7 — rebuilt on the new data

Eyebrow (Shape 186), title (187), citation explainer (213), standfirst (188), left panel of 3 rows (189-198), right panel of 4 rows (199-209), methodology box (212). Copy below maps one-to-one onto those shapes, so it is a text swap with no layout change.

## Eyebrow — Shape 186

`WHERE WE WIN`

Unchanged. It still fits the 2.20" box. If you want the sharper frame, `AI CITATIONS` also fits.

## Title — Shape 187

> **Cited at #2 when we appear. ChatGPT finds us, Google's AI mostly does not.**

## Citation explainer — Shape 213

> **What's a citation?** When ChatGPT or Google's AI Overview answers a question, it lists the sources it drew from. Being cited means PB.ae's content helped answer the query. Two numbers here: how *often* we are cited across repeated runs of the same prompt, and our average *place* in that source list. Neither is classic blue-link ranking.

## Standfirst — Shape 188

> Across 36 UAE health prompts run 19 times each, ChatGPT cites Policybazaar.ae on 64% of prompts and Google's AI Overview on 22% - at average cite position 2.3 and 2.2 respectively.

## Left panel — Shape 191 header + 3 rows

Header: **`Where ChatGPT cites us most`**

| Row label | Rank chip | Sub-label |
|---|---|---|
| health insurance companies in dubai | `95%` | cited in 18 of 19 answers · avg place 2.1 |
| affordable health insurance in dubai | `79%` | cited in 15 of 19 answers · avg place 1.7 |
| health insurance quotes uae | `74%` | cited in 14 of 19 answers · avg place 1.1 |

`health insurance quotes uae` at average place 1.1 is the best cite position in the whole file. It is almost always first when it appears.

## Right panel — Shape 201 header + 4 rows

Header: **`Won on ChatGPT, invisible on Google's AI`**

| Row label | Rank chip |
|---|---|
| individual health insurance dubai | `53% → 0%` |
| medical insurance dubai | `42% → 0%` |
| health insurance companies in uae | `42% → 0%` |
| cheapest medical insurance in uae | `26% → 0%` |

Chip reads ChatGPT visibility → AI Overview visibility. These 4 are the clearest of 17 prompts that ChatGPT cites and AI Overview never does. Only 2 prompts go the other way.

## Methodology box — Shape 212

> Ran 36 UAE health prompts on ChatGPT and Google AI Overview, 19 passes each, 5 Aug 2026. "Visibility" is the share of those passes that cited PB.ae. "Place" is our average position in the cited-sources list, not blue-link rank.
>
> Treat as directional. AI answers are personalised and non-deterministic, so track the monthly trend, not a single number. On 9 of 36 prompts Google returned no AI Overview on some days, so the ceiling on those is below 100%.

## If you want a fourth panel row, or a callout

The single strongest finding in the file is geographic:

> **Dubai works, Abu Dhabi is blank.** The 9 Dubai prompts average 42.1% ChatGPT visibility. All three Abu Dhabi prompts return zero on AI Overview, and zero or 5.3% on ChatGPT.

And the one that will surprise the room:

> **Arabic beats English on Google's AI.** `أرخص شركة تأمين صحي في الإمارات` is the strongest AI Overview result in the whole set at 47.4% and place 1.7, ahead of every English prompt. The Abu Dhabi equivalent returns zero on both engines.

## Likely question: "but we rank for those terms"

Cross-check the CSV against this deck's own slide 5 keyword tracker. Ranking does not carry into AI citation.

| Keyword | PB organic rank, slide 5 | ChatGPT | AI Overview |
|---|---|---|---|
| health insurance abu dhabi | **4** | **0%** | **0%** |
| best medical insurance in uae | **4** | 10.5% | **0%** |
| best health insurance in uae | 10 | **0%** | **0%** |
| medical insurance uae | 18 | **0%** | **0%** |
| health insurance dubai cost * | **1** | 10.5% | **0%** |
| health insurance dubai | 16 | **52.6%** | 9.1% |

\* Slide 5 tracks `health insurance dubai cost`; the CSV prompt is `health insurance in dubai cost`. Near-match, not the identical string.

Two directions in one table. We rank 4th for `health insurance abu dhabi` and are never cited. We rank 16th for `health insurance dubai` and are cited in over half of ChatGPT's answers. Whatever earns citations is not position.

---

# SLIDE 9 — Working on AI Search & Editorial Authority

Two columns. Left "AI OVERVIEW TACTICS", 5 cards. Right "EDITORIAL AUTHORITY (E-E-A-T)", 3 cards. Each card is title, one line of detail, one metric line.

**Rename the left column** to `AI SEARCH TACTICS`. It now covers two engines, and the July title understates the work.

## Left column — AI SEARCH TACTICS

**1 · AI citation tracking, two engines** · `LIVE`
36 UAE prompts × 19 passes on ChatGPT and Google AI Overview, up from 30 × 5 on AI Overview alone.
Cited at avg place 2.3 and 2.2 · ChatGPT 23 of 36 prompts, AI Overview 8 of 36

**2 · Close the Google AI Overview gap** · `PLANNED`
17 prompts are cited by ChatGPT and never by AI Overview. Only 2 go the other way.
ChatGPT visibility 18.4% vs AI Overview 4.8% · the gap, not placement, is the problem

**3 · ItemList / Carousel schema — Top 10 page** · `SHIPPED`
Schema and speed work landed. Rank recovered and the page is now our most-cited asset on ChatGPT.
Clicks 11 → 66 · impr 19.5K → 40.1K · pos 16.5 → 13.1 · cited in 95% of ChatGPT answers for "health insurance companies in dubai"

**4 · AI-agent schema expansion** · `SHIPPED · UNDER REVIEW`
Service, InsuranceAgency and FinancialService schema on the status-check article. The mid-July gain did not hold over the full month.
Status-check article clicks 784 → 504, pos 6.2 → 7.4 full Jul vs full Jun · July's "+181% clicks/day" was MTD and has reversed

**5 · Restore ChatGPT citation breadth** · `IN PROGRESS`
Cited-page count halved in H1 and has since held. Volume recovered on fewer, stronger pages.
496 pages Jan → 219 Jun → 219 Jul · sessions 491 → 612 (+25%) · key events 630 → 1,051 (+67%)

Card 4 is a correction, not a walk-back of the schema work. Say it plainly: the July slide quoted a month-to-date number and the full month went the other way. Two pages gave back the gain, per slide 3.

## Right column — EDITORIAL AUTHORITY (E-E-A-T)

**1 · Five-lens content audit at scale** · `STALLED`
Claude pipeline scoring SEO, GEO, AI-detection, YMYL and fact-check per page. No batches have run since 13 July.
45 of 990 health pages · mean GEO 48/100, the weakest of the five lenses · travel (435 URLs) not started

**2 · Written-by / Reviewed-by byline rollout** · `READY · 1 BLOCKER`
Live crawl of 1,537 URLs found the component already correct on 23 pages, so this is a rollout plus a schema fix, not a new build.
1,474 of 1,510 pages need bylines · today 23 correct, 13 visible-no-schema, 336 author-only, 1,138 nothing

**3 · Licence-linked trust signal and disclaimer** · `READY TO SHIP`
Closes the P1 commission-disclosure gap. Three credentials verified against source documents and hyperlinked.
CBUAE Reg. 123 · DHA permit BRK-00041 · EIF membership B81 · Health copy approved, Travel awaiting Compliance · 1,510 pages

**Blocker to name out loud:** Richa Bansal is the assigned reviewer for Travel content, but her profile page and her `reviewedBy` designation across Travel pages still read "Business Development Manager- Home Insurance". Her page also carries no `Person` schema and is absent from every sitemap. The byline rollout depends on that fix.

## The thread between slides 7 and 9

Mean GEO score across the 45 audited pages is 48 out of 100, the lowest of the five lenses, while AI Overview cites us on 22% of prompts. Same gap measured two ways, once on the page and once in the answer. Worth saying if someone asks why the audit matters.

---

# SLIDE 10 — Ranking-Improvement Roadmap

Left "⚡ CRITICAL & URGENT FIXES", 5 numbered cards. Right "✓ MOVED TO WINS THIS CYCLE" (2), "🚀 NEW CONTENT PIPELINE" (4), and a footnote.

Reordered on full-July data. Three of July's five have moved: Emirates ID stabilised, the cost hub belongs in the pipeline, and InsuranceProduct schema has been folded into the CTR fix where the evidence now is.

## Left column — CRITICAL & URGENT FIXES

**1 · Medical Insurance hub — rank regression** · `NEW`
Rank slid while clicks stayed flat. This and the status-check article gave back the month's gain.
pos 16.0 → 21.4 · clicks flat at 220 · full Jul vs full Jun

**2 · Head terms rank but return nothing** · `IN PROGRESS`
Title, meta and InsuranceProduct + FAQ schema on the Companies cluster. Rank improved and clicks did not follow.
"best health insurance in UAE" pos 21.3 → 14.7 on 1,101 impr and **0 clicks** · "best medical insurance in UAE" 20.0 → 15.3 on 564 impr and 1 click

**3 · Zero AI citations on terms we already rank for** · `NEW`
Organic position is not producing citations. Needs answer-first blocks and extractable summaries, not more rank.
`health insurance abu dhabi` organic 4 → 0% on both engines · `best health insurance in uae` organic 10 → 0% · `medical insurance uae` organic 18 → 0%

**4 · Family Health page — LCP, CLS, schema** · `PLANNED`
Slowest page in the set and on page 2. Figures are from 16 July and need a re-measure before the next cycle.
Field LCP 4.2s (SLOW) · Perf 44/100 · clicks −40% (45 → 27) · pos 20.2

**5 · hreflang on /ar-ae/health-insurance/** · `IN PROGRESS`
Got worse last cycle, and Arabic is where AI Overview performs best for us, so the upside is real.
pos 13.6 → 16.9 · impr −24% · Arabic UAE prompt is our strongest AI Overview result at 47.4%, Arabic Abu Dhabi is zero

**Queued, not on the slide:** strip trailing double slashes at the routing layer. 91 of 612 health ChatGPT sessions (15%) land on `/health-insurance//` style URLs. They return 200 and canonical correctly so rank is safe, but reporting splits into two rows per page. Emirates ID page has stabilised (pos 6.8 → 6.3, clicks 624 → 635) and drops off the critical list.

## Right column — MOVED TO WINS THIS CYCLE

**Health hub rescue — /health-insurance/** · `SHIPPED`
Meta/H1 rewrite plus a 3,914-link internal pass.
Clicks +62% · "health insurance" pos 30.7 → 18.6

**Top-10 Companies page** · `SHIPPED`
Schema and speed work, now compounding into AI citations as well as rank.
pos 16.5 → 13.1 · clicks 11 → 66 · cited in 95% of ChatGPT answers for "health insurance companies in dubai" at place 2.1

## Right column — NEW CONTENT PIPELINE

Reordered so every item carries evidence from the citation file. Each is a category where AI is already answering the question and we have no dedicated page.

**Health Insurance Cost Hub 2026** · `PLANNED`
cost cluster wpos 8.2 · no page exists · `how much does health insurance cost in dubai` already cited on both engines

**Health Insurance for Parents** · `PLANNED`
strongest validated gap · already 31.6% ChatGPT visibility with no dedicated page

**Maternity / Pregnancy UAE** · `PLANNED`
`maternity insurance uae` zero on both engines · `pregnancy insurance uae` 10.5% ChatGPT, zero AI Overview

**Abu Dhabi and visitor coverage** · `PLANNED`
`health insurance abu dhabi`, `health insurance for visitors in uae` and the Arabic Abu Dhabi prompt all return zero on both engines

**What I swapped out, and why you should push back if you disagree:** July listed "Doctor & specialization page" and "Mental Health Insurance UAE". Neither appears in the 36-prompt set, so this file says nothing about them either way. Absence of evidence is not evidence of absence. If they are already committed, keep them and drop the Cost Hub row, which is the one that overlaps most with existing coverage.

## Footnote

> Dropped: "Cheap Health Insurance Abu Dhabi" - live GSC shows ~25 impressions/28d against 2,124 on the June slide, and the prompt draws 5.3% ChatGPT visibility with zero on AI Overview. Re-verify seasonality before re-adding.

## Footer, both slides

> policybazaar.ae · Aug 2026 Weekly Review   |   Source: GSC `https://www.policybazaar.ae/` · full Jul vs full Jun · AI citations: 36 prompts × 19 passes, ChatGPT + Google AI Overview, 5 Aug 2026 · † GA4 metric

Property changed from `sc-domain:policybazaar.ae`, which has a 95-day reporting hole. Window changed off "28d Jun 16–Jul 13". The `† pending verification` tag is dropped from figures that have since been verified against full-July GSC, and kept only on GA4 metrics.

---

## Supporting tables for slide 7

### Engine comparison

| | ChatGPT | Google AI Overview |
|---|---|---|
| Prompts tracked | 36 | 36 |
| Prompts with a PB citation | **23 (64%)** | **8 (22%)** |
| Average visibility | **18.4%** | **4.8%** |
| Average place when cited | **2.3** | **2.2** |

Six prompts are cited on both engines. Seventeen on ChatGPT only. Two on AI Overview only (`which health insurance is best in uae` 10.5%, `health insurance cost in uae` 5.3%). Eleven on neither.

### Zero on both engines

| Prompt | Note |
|---|---|
| health insurance in uae | Head term |
| medical insurance uae | Head term, organic rank 18 |
| health insurance abu dhabi | Abu Dhabi, organic rank 4 |
| `أرخص شركة تأمين صحي في أبوظبي` | Abu Dhabi, Arabic |
| best health insurance in uae | Comparison intent, organic rank 10 |
| health insurance plans for family uae | Family cluster |
| health insurance for visitors in uae | Visitor cluster, no page |
| maternity insurance uae | Maternity cluster, no page |
| critical illness insurance cost uae 2026 | UAE variant absent; the Dubai variant draws 5.3% |
| health insurance for kids | Resolves to a US topic |
| health insurance for family | Resolves to a non-UAE topic |

### Where AI Overview did not always fire

Nine AI Overview rows carry fewer than 19 passes, so their visibility sits on a smaller base and their ceiling is below 100%: `health insurance companies in dubai` 9, `cheap health insurance` 10, `health insurance for family` 10, `health insurance dubai` 11, `best health insurance in uae` 11, `health insurance uae` 12, `medical insurance uae` 15, `best medical insurance in uae` 18, `cheapest health insurance in uae` 18.

### Five-lens audit, 45 completed pages

| Lens | Mean | Min | Max |
|---|---|---|---|
| SEO | 63.1 | 46 | 81 |
| **GEO** | **48.2** | 27 | 88 |
| AI-detection (human-likeness) | 66.2 | 41 | 89 |
| YMYL | 59.4 | 36 | 80 |
| Fact-check | 77.7 | 39 | 97 |
| **Overall** | **62.1** | 50.1 | 79.5 |

45 done, 945 pending. Last batch 13 July. 22 A-core pages and 23 tier-B pages.

## Data provenance

| Figure set | Source | Status |
|---|---|---|
| AI citations, both engines | `prompt_rankings_2026-08-05_05-50.csv` | Parsed, 72 rows, single window |
| Full Jul vs full Jun GSC/GA4 | `weekly-health-slides-insights-2026-08-05.md` | Carried over, property `https://www.policybazaar.ae/` |
| PB organic ranks in the cross-check | This deck's own slide 5 keyword tracker | Read from the deck, not re-measured |
| Byline coverage | Live crawl of 1,537 URLs, 31 Jul, `byline-eeat-health-travel-2026-07-31.md` | Measured, 100% HTTP 200 |
| Licence credentials | `disclaimer-health-2026-07-31.md` | Verified against source documents 31 Jul |
| Five-lens scores | `audit-state.csv`, 45 rows with `status=done` | Read from the state file |
| Family Health LCP, Emirates ID, hreflang | July monthly deck, measured 16 Jul | **Not re-measured. Three weeks old.** |

The last row is the weak spot. If anyone challenges the Family Health page numbers, say they are the 16 July measurement and a re-run is due.
