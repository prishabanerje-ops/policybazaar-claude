# GEO Lens — AI Citation Ranking Factors — Design

**Date:** 2026-07-17
**Owner:** Aakash Srivastava
**Status:** Approved (brainstorming session 2026-07-17)

## Goal

Extend `/content-audit`'s **Lens 2 (GEO)** rubric with two AI-citation ranking factors —
**Fan-out Rank** and **Freshness** — sourced from a Zyppy Signal chart ("AI Citation
Ranking Factors," analysis of 55 experiments/patents/case studies) that Aakash shared.
The chart lists 23 weighted factors; most map onto GEO parameters this skill already
scores. Two are genuinely uncaptured today and are content-assessable (don't require
live crawling or rank data): Fan-out Rank and Freshness-as-an-explicit-signal.

## Non-goals

- No 6th lens. The 5-lens structure and its `Overall Score` weighting
  (SEO ×0.20 + GEO ×0.25 + Human-Likeness ×0.15 + YMYL ×0.20 + Fact-Check ×0.20) is
  unchanged — these two factors live inside the existing GEO lens's 100-point budget.
- No new parameter for **Preview Control**, **Explicit Phrasing**, or **Self-Contained
  Passages** — their content-relevant essence already overlaps **Direct-Answer
  Formatting** and **Statistics & Citations**; adding dedicated parameters would risk
  double-scoring the same underlying signal under a new name.
- No attempt to score the chart's technical/off-page factors — **URL Accessibility**,
  **Search Rank**, **Content Visibility** (JS-rendering), **Domain Authority**,
  **llms.txt** — this skill audits pasted/fetched *content*, not live crawl or
  rank-tracking data. These stay explicitly out of scope, with a pointer to the `seo`
  skill's technical audit.

## 1. Two new GEO parameters (`references/geo-parameters.md`)

### Fan-out Rank (12 pts)

AI systems answer a query by internally "fanning out" into several related
sub-questions before composing a response (e.g. "travel insurance UAE" fans into cost,
coverage limits, claims process, visa requirements). Content that already answers the
likely fan-out sub-questions — either within the page itself, or via a well-linked
topic cluster — gets pulled into more parts of an AI-generated answer, not cited once
for only the headline question.

**What to check:**
- Does the page anticipate and answer adjacent sub-questions a research-mode AI would
  ask about this topic, not just the primary query?
- FILE MODE: judge from the content alone — does this piece cover the topical
  neighborhood, or stop at the headline question?
- URL MODE: also check whether the page is part of a linked topic cluster (sibling
  pages covering sub-questions this page doesn't) — ties into the existing Step 2.6
  interlink analysis; a strong hub+spoke structure counts even if this exact page
  doesn't answer every sub-question itself.

| Condition | Points |
|---|---|
| Directly answers 4+ likely fan-out sub-questions, or is clearly part of a linked cluster covering them | 12 |
| Answers 2–3 sub-questions directly | 8–11 |
| Answers 1 sub-question beyond the primary query | 4–7 |
| Only the primary query answered, no cluster linking | 0–3 |

### Freshness (8 pts)

Split out of E-E-A-T's Trustworthiness sub-check into its own scored signal (E-E-A-T's
max drops 15→11 accordingly).

**What to check:**
- Last-updated/published date present and genuinely recent for the vertical
- Time-sensitive claims (prices, regulatory limits) carry an "as of" qualifier
- No stale year references or regulatory figures inconsistent with current rules
- FILE MODE carve-out (mirrors E-E-A-T's existing one): score whether the *draft*
  signals its own currency (as-of framing on time-sensitive claims), not the publish
  date itself — dates are added at deployment, not by the writer.

| Condition | Points |
|---|---|
| Recent date/as-of qualifier on all time-sensitive claims; content reflects current rules/prices | 8 |
| Date present but 1–2 time-sensitive claims lack as-of framing, or minor staleness | 5–7 |
| No clear freshness signal; some outdated-info risk | 2–4 |
| Stale/outdated regulatory or pricing info stated as current | 0–1 |

**Required differentiation note** (prevents double-scoring, same pattern as the
existing SEO/GEO genericness-overlap note in `ai-detection-parameters.md`): Freshness
here scores the *presence of a currency signal* (dates, as-of framing). The existing
Fact-Check Lens parameter **Outdated Information Risk** scores whether a *specific
verified claim* is actually stale, via live `web_search`. Same topic area, different
question — a page can score well on Freshness (dates everywhere) while still failing
Outdated Information Risk (the dated figure is wrong), and vice versa.

## 2. Repointing the GEO lens (9 → 11 parameters, still totals 100)

| Parameter | Old | New | Why changed |
|---|---|---|---|
| Direct-Answer Formatting | 15 | 15 | unchanged — already covers the chart's top 3 factors (Query-Answer Match, Intent-Format Match, Answer Near Top) |
| E-E-A-T Signals | 15 | 11 | Freshness split out into its own parameter |
| Entity Clarity | 10 | 6 | chart's own analog (Entity Consistency, 5.8) sits near the bottom of the chart's 23 factors |
| Conversational Q&A Coverage | 15 | 15 | unchanged |
| Statistics & Citations | 10 | 10 | unchanged — chart analogs (Cites Sources 8.0, Factually Specific 8.3) are high-weighted |
| Schema/Structured Data Mentions | 10 | 6 | chart's Structured Data (5.6) is near the bottom |
| Content Depth & Original Angle | 10 | 8 | chart's Length sub-signal (6.7) is mid-low |
| Semantic Heading Use | 10 | 6 | no strong chart analog above mid-range |
| Brand/Source Credibility | 5 | 3 | chart's Known Source (5.4) / Domain Authority (5.0) are the two lowest-weighted factors on the whole chart |
| **Fan-out Rank (NEW)** | — | 12 | chart weight 9.3 — tied for 3rd highest of all 23 factors |
| **Freshness (NEW)** | — | 8 | chart weight 7.0 — currently unscored as its own signal |

Total: 15+11+6+15+10+6+8+6+3+12+8 = 100.

## 3. Out-of-scope note

Add to `geo-parameters.md`'s background section, and cross-reference from `SKILL.md`'s
Lens 2 intro:

> Site-wide/technical AI-citation factors — URL crawler accessibility, live AI
> Overview/ChatGPT search rank, JS-rendering/content visibility, domain authority,
> llms.txt presence — require live crawling and rank-tracking data this skill doesn't
> fetch. Use the `seo` skill's technical audit for those.

## 4. Mechanical propagation (no new decisions)

- `SKILL.md` Lens 2 parameter table: 9 rows → 11 rows, updated point values.
- Step 4 report template's Lens 2 markdown table: add 2 rows (Fan-out Rank, Freshness).
- `Overall Score` formula: **unchanged** — GEO stays weighted ×0.25 as a whole lens;
  only its internal 100-point distribution changes.
- Master workbook's **Lens Scores** sheet: no schema change needed — it's already
  "one row per URL × parameter (all five lenses)," so the 2 new parameter rows flow
  through automatically for future audits. Rows from *before* this change (used the
  old 9-parameter GEO breakdown) are historical and not backfilled.

## Testing / verification

This is a documentation/rubric change to markdown reference files consumed by an LLM
skill, not executable code — no unit tests apply. Verification is: run `/content-audit`
against one already-audited health-insurance URL and one travel-insurance URL, confirm
the Lens 2 output shows 11 parameters summing to 100, Fan-out Rank and Freshness each
carry evidence-formatted findings, and the out-of-scope note appears once (not
duplicated across files).
