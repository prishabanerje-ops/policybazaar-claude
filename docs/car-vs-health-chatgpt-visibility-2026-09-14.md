# Car Insurance vs Health Insurance — ChatGPT Visibility Deep Dive
Date: 2026-09-14 | Prepared for: Aakash Srivastava

## Data sources used (and their limits)

| Source | Coverage | What it actually measures |
|---|---|---|
| GA4 export (`download.csv`) | ChatGPT-referral segment, whole site, **Aug 1–31, 2026** | Real sessions/leads/key-events landing from chatgpt.com, by page path |
| Leads export (`query_result_...csv`) | CRM enquiries, `utm_source=chatgpt`, **Sep 1–14, 2026** | Real enquiry volume + downstream booking status, by product |
| `aio_car-insurance_2026-07-22__google.json` / `aio_health-insurance_2026-07-22__google.json` | **Google AI Overview**, 25 car prompts / 102 health prompts, one-time scrape from 2026-07-22 | Citation presence/position in Google's AI Overview — **not ChatGPT** |

**No live ChatGPT citation scrape exists for either vertical** (only `__google.json` datasets are on disk for car/health). So "ranking in ChatGPT" below is answered with real ChatGPT *referral outcomes* (GA + Leads — the strongest evidence we have, since it's actual users ChatGPT sent us), plus the Google AIO snapshot as a directional proxy for citation-share dynamics, clearly labeled as a different engine. If you want an actual ChatGPT-engine citation panel to confirm the "why," that requires a fresh logged-in-Chrome scrape via `/ai-search` — I did not run that this turn.

The GA and Leads windows don't overlap (Aug vs Sep) — treated as two independent confirmations, not one dataset.

## Headline: Car Insurance outperforms Health Insurance by ~2x on every real ChatGPT-referral metric

| Metric | Car Insurance | Health Insurance | Ratio |
|---|---|---|---|
| GA sessions from ChatGPT (Aug 2026) | 2,404 | 1,272 | 1.9x |
| GA lead count (Aug 2026) | 568 (23.6%) | 265 (20.8%) | 2.1x |
| CRM leads, utm_source=chatgpt (Sep 1–14) | 516 | 223 | 2.3x |
| Booking/Sale-Complete rate on those leads | 2.3% | 2.2% | ~equal |

The gap is consistent and real. The last row matters: **once a lead comes in, both verticals convert to a sale equally poorly (~2.3%)** — so the problem isn't sales follow-up, it's upstream: how much ChatGPT sends, and to what.

## Why: content shape, not brand strength

### 1. Car has utility/checker articles that ChatGPT loves; Health doesn't
Car's top ChatGPT-referred *article* pages are practical lookup tools:
- `/car-insurance/articles/how-to-check-car-accident-history-in-uae/` — 61 sessions
- `/car-insurance/articles/check-car-history-with-chassis-number-in-the-uae/` — 21 sessions
- `/car-insurance/articles/chassis-number-check-uae/` — 15 sessions

These three alone pulled ~100 ChatGPT sessions in a month. Health's equivalent articles are descriptive, not tool-shaped, and pull far less:
- `/health-insurance/articles/insurance-installments-uae-tabby/` — 19 sessions
- `/health-insurance/articles/maternity-insurance-in-uae/` — 11 sessions

ChatGPT (and AI answers generally) over-index on citing pages that directly resolve a specific how-do-I task. Car has several; Health has none at that level of specificity.

### 2. Health is nearly invisible on the highest-volume head terms (Google AIO proxy)

| | Car Insurance | Health Insurance |
|---|---|---|
| Prompts tested | 25 | 102 |
| AI Overview fired | 19 | 85 |
| PB cited when it fired | 6 (32%) | 11 (13%) |
| Avg citation position | 8.2 | 6.4 |

Health is asked about far more (102 vs 25 prompts) but cited proportionally less than half as often. And the prompts where PB is **completely absent** are exactly the category-defining ones a buyer actually types first:
- "health insurance dubai" / "health insurance uae" / "health insurance in uae"
- "medical insurance uae" / "medical insurance dubai"
- "best health insurance in uae" / "best medical insurance in uae"
- "compare medical insurance dubai"

Car also misses some broad terms ("cheap car insurance," "best car insurance company in uae") but wins the specific-task queries that Health has no content for at all.

### 3. Health's buy-funnel leaks more before a lead is even logged
Health's mid-funnel steps (`buy-insurance/comparison/...`, `buy-insurance/proposal/...`, `buy-insurance/quotes/...`) each show sessions with **zero** leads/key-events (5–13 sessions, 0 leads apiece). Car's funnel doesn't show the same pattern at comparable volume. Worth a UX check independent of the content-gap story above.

## Missing opportunities (ranked)

1. **Build 3–5 health-insurance "checker/how-to" articles mirroring the chassis-number pattern** — e.g., how to check health insurance card/policy validity in UAE, how to check Daman/DHA claim status, golden-visa health insurance requirement checklist. This is the single highest-leverage fix: it's the exact content shape already proven to pull ChatGPT referral traffic in the car vertical.
2. **Target the head terms Health is losing outright**: "health insurance dubai/uae," "medical insurance uae/dubai," "best health insurance in uae," "compare medical insurance dubai." These had zero PB presence in the July snapshot despite being the most-asked prompts in the set — a dedicated, well-structured comparison/cost page for each is the direct fix.
3. **Audit the Health buy-funnel drop-off** (comparison → proposal → quotes steps with 0 leads) — separate from the AI-visibility story, but it's real revenue leaking from the traffic Health already gets.
4. **Re-run this analysis with an actual ChatGPT-engine scrape** (`/ai-search`, ChatGPT mode, logged into chatgpt.com) for both verticals — everything above about "why ChatGPT specifically" is inferred from GA/Leads (real) + a Google AIO proxy (different engine); a same-engine comparison would confirm or correct the content-gap theory directly.

## Update — full August CRM data added (query_result_2026-09-14T20_16_34...csv)

The Sep 1–14 leads file was a partial month with a low sample on bookings. Adding full August CRM leads (1,328 rows, `utm_source=chatgpt`, Aug 1–31) cross-checks and sharpens the picture:

| Metric (August, full month) | Car Insurance | Health Insurance | Ratio |
|---|---|---|---|
| CRM leads, utm_source=chatgpt | 867 | 461 | 1.88x |
| Booking/Sale-Complete rate | 5.1% (44/867) | 4.3% (20/461) | 1.19x |

The CRM ratio (1.88x) independently lands almost exactly on the GA session ratio (1.9x) from the same month — two separately-computed sources agreeing this closely means the ~2x gap is real, not a data artifact. With the fuller sample, Car also converts to sale modestly better than Health (5.1% vs 4.3%) — the earlier partial-Sep view that conversion was "equal" doesn't hold once volume is adequate.

**Weekly trend, ISO weeks 31–38 (Aug 1 – Sep 14), lead ratio Car:Health:**
41:24 → 170:103 → 159:110 → 191:95 → 261:113 → 264:98 → 263:133 (week 38 is a partial 1-day week, excluded from the read)

The ratio bounces between 1.5x and 2.7x but shows no trend of closing — this is a stable, structural gap over 7 weeks, not a recent dip or a one-off.

**New evidence — Health actually wins on Arabic queries.** Re-checking which health prompts *did* cite policybazaar.ae in the AIO snapshot: three of the eleven citations are Arabic-language queries, and one of them — "أفضل تأمين صحي في الإمارات" (best health insurance in the Emirates) — has PB as the **sole citation, position 1**. Two more Arabic queries cite PB at position 2. Meanwhile PB is absent from essentially every English head term tested. That's a 3-for-3 strong showing on Arabic vs near-total absence on English — a genuine, evidenced asymmetry, not a guess.

## Correction — sitemap check, 2026-09-14

Aakash flagged that pages for the 4 target terms already exist. Checked the live sitemap (`https://www.policybazaar.ae/sitemap/sitemap-health-insurance.xml`, verified 200 OK, 1,065 URLs) directly:

| Target term | Sitemap reality |
|---|---|
| "health insurance dubai/uae" | Covered by the flagship `/health-insurance/` page + ~158 long-tail articles. No gap. |
| "medical insurance uae/dubai" | Dedicated `/health-insurance/medical-insurance/` page exists. No gap. |
| "best health insurance in uae" | `/top-10-health-insurance-companies-in-uae-hiart/` exists and directly targets this — **originally missed, corrected below.** |
| "compare medical insurance dubai" | Still genuinely absent — no matching URL anywhere in the sitemap. |

**On `/top-10-health-insurance-companies-in-uae-hiart/` specifically** — checked the live page and robots.txt directly:
- Title/H1/meta all target "Best Health Insurance Companies in Dubai, UAE" directly; 16 H2 sections (one per insurer), 17 comparison tables, 30 AED price mentions, author schema present, `dateModified` = 2026-08-13 (updated last month, not stale).
- `robots.txt` explicitly allows GPTBot, Google-Extended, ClaudeBot, PerplexityBot, OAI-SearchBot, and anthropic-ai; no noindex tag on the page. **Not a crawlability or blocking issue.**
- Despite that, it's cited zero times in the July 22 AIO snapshot across "best health insurance in uae," "top 5 health insurance companies in uae," and "top 10 health insurance companies in uae" — bayzat.com, hayah.com, esanad.com, giggulf.ae, insurancemarket.ae, and sukoon.com win those slots instead, consistently. GA confirms the same in real traffic: this page got **3 ChatGPT-referred sessions in all of August, 0 leads.**

So this is not a missing-page or technical-blocking problem — it's **competitive crowding-out**: several of those winning domains are broker/comparison sites like PB itself, and they consistently own the "best of" citation slot across nearly every health insurance prompt in the dataset, not just this one. That's an off-site authority/signal problem, harder to fix than writing new content, and not yet root-caused — a structural comparison against a winning competitor page (e.g. bayzat.com's or insurancemarket.ae's equivalent) would be the next step to actually diagnose it, not assumed here.

**Net effect on the actionables below:** only "compare medical insurance dubai" remains a genuine net-new-page gap. The other three terms need a different fix than "build a page" — either an on-page answer-format change (for the flagship/medical-insurance pages) or an off-site authority push (for the top-10 companies page), not new content from scratch.

## On-page AI-optimization audit — `/top-10-health-insurance-companies-in-uae-hiart/` (2026-09-15)

Checked the live page's structured data and content order directly (not the raw robots/freshness pass from before):

- **Schema is actually strong already**: `FAQPage` (12 Q&A pairs), `ItemList`, `AggregateRating`, `Person` (author), `BreadcrumbList`, `SpeakableSpecification` are all present. Schema is not the gap.
- **`llms.txt` does include this page** (`https://www.policybazaar.ae/llms.txt`, confirmed live) — so it's not invisible to LLM discovery. But the file itself is 3,815 lines, uncurated, and dominated by 210 old car-insurance blog posts (2020-era, `-ciart` slugs) and unrelated content (gold rates, BMW/Ferrari reviews) mixed in with only 119 health entries — no prioritization signal for which pages matter most. Weak, but not the primary blocker for this specific page.
- **Real problem: the page's own content order.** Everything between the H1 and the first H2 is a lead-gen quote widget ("AED 1M cover from AED 4/day... Get a Quote... Rated 4.7/5, 44,090 Reviews") — there is no scannable "top 10 at a glance" list or table before that. The first actual `<table>` (titled "List of Top Health Insurance Companies in UAE") only appears after the intro/widget block. AI Overviews and ChatGPT pull from the first clear, structured answer on a page — PB's page front-loads a sales CTA instead of the answer itself.
- **Zero outbound links to independent third-party sources** anywhere on the page (checked all external links — only social/CDN/internal-account domains, nothing to CBUAE, individual insurer sites, or review sources). Pages that win these citation slots typically read as independent buying guides that cite external sources; a page that only links to itself reads as promotional, which may be part of why competitors are favored for this "best of" slot.

## Actionables, ranked, with why each is expected to work

1. **Build a Health "checker" content set** — e.g., how to check UAE health insurance/Daman card validity, how to check a DHA/Daman claim status, a golden-visa health insurance requirement checklist.
   *Why:* This exact content shape is already proven in-house. Car's three checker articles (`how-to-check-car-accident-history`, `check-car-history-with-chassis-number`, `chassis-number-check-uae`) pulled roughly 100+ ChatGPT-referred GA sessions and dozens of CRM leads in August alone, at zero paid spend. It's not a hypothesis — it's a working pattern on the same domain, same authority, same AI-engine behavior, that Health simply hasn't shipped.

2. **Build the one genuinely missing page — "compare medical insurance plans Dubai"** (confirmed absent from the sitemap). For "health insurance dubai/uae" and "medical insurance uae/dubai," the pages already exist (`/health-insurance/`, `/health-insurance/medical-insurance/`) — the fix there is an on-page answer-format change (a direct, extractable cost/coverage summary near the top), not a new page. See the sitemap correction above.
   *Why:* "Compare medical insurance dubai" is the one term with zero existing coverage — a clean opportunity. The other two already get real ChatGPT referral traffic (154 and ~80 August sessions respectively) but weren't cited for these exact phrasings in the AIO snapshot — sharpening the existing page's answer format is lower-effort than building a duplicate.

3. **Extend the Arabic health content** — more Arabic long-tail pages, and an Arabic version of the checker-article idea from #1.
   *Why:* This is the one place Health already outperforms Car on AI citations (sole citation, position 1, on the top Arabic query tested). Doubling down here extends a demonstrated win instead of starting cold, and is likely lower-effort than winning contested English head terms.

4. **Fix the Health buy-funnel drop** (`buy-insurance/comparison/...`, `/proposal/...`, `/quotes/...` steps showing sessions with zero leads).
   *Why:* Independent of the visibility gap — this is traffic Health already has, leaking before it becomes a lead. Fixing it raises the ROI of #1–3 by converting more of whatever additional traffic they bring.

5. **Run an actual ChatGPT-engine scrape** (`/ai-search`, ChatGPT mode) for both verticals before committing a content budget.
   *Why:* Points 1–3 lean on a Google AI Overview snapshot as a proxy since no ChatGPT-engine dataset exists for either vertical. The GA/Leads referral gap is real and engine-agnostic, but confirming the checker-article and Arabic-content theories on ChatGPT specifically — the engine actually driving the traffic gap — would de-risk the content investment before writing it.

## Caveats
- GA (Aug) and Leads (Sep) are different windows — treated as two independent signals, not combined.
- The AIO dataset is Google AI Overview, one snapshot, one session/region (2026-07-22) — AI answers are personalized and non-deterministic; this is not a stable ranking, and it is not ChatGPT.
- Booking/Sale-Complete counts are low-n (10–12 rows) and reflect an active mid-month CRM export, not a closed period — read the 2.3% figures as directional, not final.
