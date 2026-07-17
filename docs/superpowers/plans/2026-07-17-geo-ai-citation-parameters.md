# GEO Lens AI-Citation Parameters Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add two new parameters — Fan-out Rank and Freshness — to the `/content-audit` skill's GEO lens (Lens 2), repoint the lens's 9 existing parameters to make room within its 100-point budget, and document what the lens explicitly does not score.

**Architecture:** This is a documentation-only change to markdown reference files that an LLM skill reads at run time — there is no application code, build step, or executable logic. "Tests" in this plan are inline Python verification snippets (run via Bash) that parse the markdown tables/headers and assert point totals and cross-file consistency, since the risk in this change is arithmetic/consistency drift across three files, not runtime logic bugs.

**Tech Stack:** Markdown (skill reference files), Python 3 one-off snippets for verification (no dependencies beyond the standard library), git.

## Global Constraints

- No 6th lens — the 5-lens structure and `Overall Score` formula (`SEO×0.20 + GEO×0.25 + Human-Likeness×0.15 + YMYL×0.20 + Fact-Check×0.20`) stays unchanged; both new parameters live inside GEO's existing 100-point budget.
- No new parameter for Preview Control, Explicit Phrasing, or Self-Contained Passages — out of scope per spec (overlaps existing Direct-Answer Formatting / Statistics & Citations).
- No attempt to score technical/off-page factors (URL crawler accessibility, live AI-search rank, JS-rendering visibility, domain authority, `llms.txt`) — explicitly out of scope, documented with a pointer to the `seo` skill.
- Every GEO parameter's point value across `geo-parameters.md` and `SKILL.md` must match exactly and sum to 100 in both files at all times after this work lands.
- Full spec: `docs/superpowers/specs/2026-07-17-geo-ai-citation-parameters-design.md`.

---

### Task 1: Add the two new parameters and the out-of-scope note to `geo-parameters.md`

**Files:**
- Modify: `/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills/content/content-audit/references/geo-parameters.md`

**Interfaces:**
- Consumes: nothing from earlier tasks (first task).
- Produces: two new parameter headers (`## 10. Fan-out Rank (12 pts)`, `## 11. Freshness (8 pts)`) and one new section header (`## Out of Scope: Technical AI-Citation Factors`) that Task 2 and Task 4 will reference by exact text.

This task is purely additive — none of the existing 9 parameters' point values change yet. That happens in Task 2. After this task, the file will (correctly, temporarily) sum to 120 points across 11 parameters; Task 2 brings it back to 100.

- [ ] **Step 1: Insert the out-of-scope note after the Background section, before Parameter 1**

Edit the file. Find this exact text:

```
  and a specific (not generic) angle. Parameter 7 below scores that directly.

---

## 1. Direct-Answer Formatting (15 pts)
```

Replace it with:

```
  and a specific (not generic) angle. Parameter 7 below scores that directly.

---

## Out of Scope: Technical AI-Citation Factors

A number of factors that influence AI-citation ranking are **not** scored by this
lens because they require live crawling or rank-tracking data this skill doesn't
fetch from pasted text or a fetched page body — URL crawler accessibility (can
GPTBot/ChatGPT-User/PerplexityBot actually fetch the page), live AI Overview/ChatGPT
search rank, JS-rendering/content visibility, domain authority, and `llms.txt`
presence. Use the `seo` skill's technical audit for those. This lens stays scoped to
what's assessable from the content itself.

---

## 1. Direct-Answer Formatting (15 pts)
```

- [ ] **Step 2: Append the two new parameter sections at the end of the file**

Find this exact text (the current end of the file — Parameter 9):

```
## 9. Brand / Source Credibility Signals (5 pts)

**What it is:** AI engines assess source credibility before citing. Content from
an identifiable, licensed brand with clear contact signals gets higher citation trust.

**What to check:**
- Is the brand name (Policybazaar UAE) mentioned explicitly?
- Is the brand identified as a licensed insurance aggregator (not just a "comparison site")?
- Is a regulatory or license reference present?
- Is there a trust signal (years in market, number of plans compared, customer reviews)?
- No anonymous authorship ("the team" without a name)

**Scoring:**
| Condition | Points |
|---|---|
| Brand named + licensed aggregator identified + trust signal + author | 5 |
| 2–3 of the above | 3–4 |
| Only brand name present | 1–2 |
| Anonymous or no brand signals | 0 |
```

Replace it with the same block plus the two new sections appended after it:

```
## 9. Brand / Source Credibility Signals (5 pts)

**What it is:** AI engines assess source credibility before citing. Content from
an identifiable, licensed brand with clear contact signals gets higher citation trust.

**What to check:**
- Is the brand name (Policybazaar UAE) mentioned explicitly?
- Is the brand identified as a licensed insurance aggregator (not just a "comparison site")?
- Is a regulatory or license reference present?
- Is there a trust signal (years in market, number of plans compared, customer reviews)?
- No anonymous authorship ("the team" without a name)

**Scoring:**
| Condition | Points |
|---|---|
| Brand named + licensed aggregator identified + trust signal + author | 5 |
| 2–3 of the above | 3–4 |
| Only brand name present | 1–2 |
| Anonymous or no brand signals | 0 |

---

## 10. Fan-out Rank (12 pts)

**What it is:** AI assistants answer a query by internally "fanning out" into several
related sub-questions before composing a response (e.g. a query about "travel
insurance UAE" fans out into sub-questions on cost, coverage limits, claim process,
visa requirements). Content that already answers the likely fan-out sub-queries — on
the same page, or via a well-linked topic cluster — is more likely to be pulled into
multiple parts of an AI-generated answer, not cited once for only the headline query.

**What to check:**
- Does the page anticipate and answer the adjacent sub-questions a research-mode AI
  would ask about this topic, not just the primary query?
- FILE MODE: judge from the content alone — does this piece cover the topical
  neighborhood, or stop at the headline question?
- URL MODE: also check whether the page is part of a linked topic cluster (sibling
  pages covering sub-questions this page doesn't) — this ties into the Step 2.6
  interlink analysis in `SKILL.md`; a strong hub+spoke structure counts even if this
  exact page doesn't answer every sub-question itself.

**Scoring:**
| Condition | Points |
|---|---|
| Directly answers 4+ likely fan-out sub-questions, or is clearly part of a linked cluster covering them | 12 |
| Answers 2–3 sub-questions directly | 8–11 |
| Answers 1 sub-question beyond the primary query | 4–7 |
| Only the primary query answered, no fan-out coverage, no cluster linking | 0–3 |

---

## 11. Freshness (8 pts)

**What it is:** AI engines discount stale sources, especially for YMYL content where
prices, coverage limits, and regulations change. Split out from E-E-A-T's
Trustworthiness pillar (see `eeat-framework.md`) into its own scored signal — it's
weighted independently on the research this rubric addition is based on.

**What to check:**
- Last-updated/published date present and genuinely recent for the vertical
- Time-sensitive claims (prices, regulatory limits) carry an "as of" qualifier
- No stale year references or regulatory figures inconsistent with current rules
- **FILE MODE:** score whether the *draft* signals its own currency (an "as of"
  qualifier attached to time-sensitive claims), not the publish date itself — dates
  are added at deployment, not by the writer (same carve-out logic as Parameter 2).

**Scoring:**
| Condition | Points |
|---|---|
| Recent date/as-of qualifier present on all time-sensitive claims; content reflects current rules/prices | 8 |
| Date present but 1–2 time-sensitive claims lack as-of framing, or minor staleness | 5–7 |
| No clear freshness signal; some outdated-info risk | 2–4 |
| Stale/outdated regulatory or pricing info stated as current | 0–1 |

**Differentiation from Fact-Check Lens:** This parameter scores the *presence of a
currency signal* (dates, as-of framing) — it does not verify whether a claim is
actually still true. The Fact-Check Lens's **Outdated Information Risk** parameter
(`fact-check-parameters.md`) scores whether a *specific verified claim* is stale, via
live `web_search`. A page can score well here (dates everywhere) while still failing
Outdated Information Risk (the dated figure is wrong), and vice versa — both may fire
on the same finding; that's expected overlap between a structural signal and a
verified-fact check, not a duplicate rule to fix.
```

- [ ] **Step 3: Verify the additions (expect 11 headers, 120 total points)**

Run:

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude" && python3 - <<'EOF'
import re
path = ".claude/skills/content/content-audit/references/geo-parameters.md"
text = open(path).read()
assert "## Out of Scope: Technical AI-Citation Factors" in text
assert "## 10. Fan-out Rank (12 pts)" in text
assert "## 11. Freshness (8 pts)" in text
totals = re.findall(r"\(\s*\d+\s*pts\)", text)
nums = [int(re.search(r"\d+", t).group()) for t in totals]
print(len(nums), sum(nums))
EOF
```

Expected: `11 120` (9 original parameters still at their old point values + 2 new = 120; Task 2 brings this to 100).

- [ ] **Step 4: Commit**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude" && git add ".claude/skills/content/content-audit/references/geo-parameters.md" && git commit -m "feat(content-audit): add Fan-out Rank and Freshness GEO parameters"
```

---

### Task 2: Repoint the 6 existing GEO parameters that lose points to fit the new 100-point budget

**Files:**
- Modify: `/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills/content/content-audit/references/geo-parameters.md`

**Interfaces:**
- Consumes: the file as left by Task 1 (11 headers, 120 points).
- Produces: the same 11 headers, now summing to exactly 100, matching the point table in the spec: Direct-Answer Formatting 15 (unchanged), E-E-A-T Signals 11, Entity Clarity 6, Conversational Q&A Coverage 15 (unchanged), Statistics & Citations 10 (unchanged), Schema/Structured Data Mentions 6, Content Depth & Original Angle 8, Semantic Heading Use 6, Brand/Source Credibility 3, Fan-out Rank 12, Freshness 8.

- [ ] **Step 1: Repoint E-E-A-T Signals (15 → 11 pts) — header**

Find:
```
## 2. E-E-A-T Signals (15 pts)
```
Replace with:
```
## 2. E-E-A-T Signals (11 pts)
```

- [ ] **Step 2: Repoint E-E-A-T Signals — Trustworthiness bullet (removes the now-duplicated last-updated-date mention)**

Find:
```
- **Trustworthiness:** Is there a last-updated date? Transparent methodology? No exaggerated claims?
```
Replace with:
```
- **Trustworthiness:** Transparent methodology? No exaggerated claims? (Currency/last-updated date is scored separately — see Parameter 11, Freshness.)
```

- [ ] **Step 3: Repoint E-E-A-T Signals — scoring table**

Find:
```
| Condition | Points |
|---|---|
| Author + credentials + official sources cited + last-updated date + brand license signal | 15 |
| 3 of 4 E-E-A-T pillars demonstrated | 10–14 |
| 2 of 4 pillars | 5–9 |
| Generic content with no E-E-A-T signals | 0–4 |
```
Replace with:
```
| Condition | Points |
|---|---|
| Author + credentials + official sources cited + brand license signal (all 4 E-E-A-T pillars) | 11 |
| 3 of 4 E-E-A-T pillars demonstrated | 7–10 |
| 2 of 4 pillars | 3–6 |
| Generic content with no E-E-A-T signals | 0–2 |
```

- [ ] **Step 4: Repoint Entity Clarity (10 → 6 pts) — header**

Find:
```
## 3. Entity Clarity (10 pts)
```
Replace with:
```
## 3. Entity Clarity (6 pts)
```

- [ ] **Step 5: Repoint Entity Clarity — scoring table**

Find:
```
| Condition | Points |
|---|---|
| All major entities named precisely; regulatory/geographic clarity throughout | 10 |
| Most entities clear; 1–2 vague references | 6–9 |
| Several vague or conflated entities | 3–5 |
| Generic entity usage throughout (just "insurance companies", "the government") | 0–2 |
```
Replace with:
```
| Condition | Points |
|---|---|
| All major entities named precisely; regulatory/geographic clarity throughout | 6 |
| Most entities clear; 1–2 vague references | 4–5 |
| Several vague or conflated entities | 2–3 |
| Generic entity usage throughout (just "insurance companies", "the government") | 0–1 |
```

- [ ] **Step 6: Repoint Schema / Structured Data Mentions (10 → 6 pts) — header**

Find:
```
## 6. Schema / Structured Data Mentions (10 pts)
```
Replace with:
```
## 6. Schema / Structured Data Mentions (6 pts)
```

- [ ] **Step 7: Repoint Schema / Structured Data Mentions — scoring table**

Find:
```
| Condition | Points |
|---|---|
| Content maps to 3+ schema types; author, date, and structured sections present | 10 |
| 2 schema types signaled | 6–9 |
| 1 schema type | 3–5 |
| No schema-friendly structure | 0–2 |
```
Replace with:
```
| Condition | Points |
|---|---|
| Content maps to 3+ schema types; author, date, and structured sections present | 6 |
| 2 schema types signaled | 4–5 |
| 1 schema type | 2–3 |
| No schema-friendly structure | 0–1 |
```

- [ ] **Step 8: Repoint Content Depth & Original Angle (10 → 8 pts) — header**

Find:
```
## 7. Content Depth & Original Angle (10 pts)
```
Replace with:
```
## 7. Content Depth & Original Angle (8 pts)
```

- [ ] **Step 9: Repoint Content Depth & Original Angle — Depth & Density sub-budget (5 → 4 pts)**

Find:
```
**What to check (Depth & Density — up to 5 pts):**
```
Replace with:
```
**What to check (Depth & Density — up to 4 pts):**
```

- [ ] **Step 10: Repoint Content Depth & Original Angle — Original Angle sub-budget (5 → 4 pts)**

Find:
```
**What to check (Original Angle — up to 5 pts):**
```
Replace with:
```
**What to check (Original Angle — up to 4 pts):**
```

- [ ] **Step 11: Repoint Content Depth & Original Angle — scoring table**

Find:
```
| Condition | Points |
|---|---|
| 1,500+ words (or dense equivalent), comprehensive sub-topic coverage, examples, multiple intent angles, AND a clear original angle vs. generic competitor coverage | 9–10 |
| Strong on depth OR original angle, weaker on the other | 6–8 |
| 1,000–1,499 words, mostly comprehensive, but reads as generic/interchangeable with competitors | 3–5 |
| Under 500 words, or comprehensive word count but shallow and could be find-replaced onto any competitor site | 0–2 |
```
Replace with:
```
| Condition | Points |
|---|---|
| 1,500+ words (or dense equivalent), comprehensive sub-topic coverage, examples, multiple intent angles, AND a clear original angle vs. generic competitor coverage | 7–8 |
| Strong on depth OR original angle, weaker on the other | 5–6 |
| 1,000–1,499 words, mostly comprehensive, but reads as generic/interchangeable with competitors | 2–4 |
| Under 500 words, or comprehensive word count but shallow and could be find-replaced onto any competitor site | 0–1 |
```

- [ ] **Step 12: Repoint Semantic Heading Use (10 → 6 pts) — header**

Find:
```
## 8. Semantic Heading Use (10 pts)
```
Replace with:
```
## 8. Semantic Heading Use (6 pts)
```

- [ ] **Step 13: Repoint Semantic Heading Use — scoring table**

Find:
```
| Condition | Points |
|---|---|
| All headings semantic, keyword-rich, informative standalone | 10 |
| Most headings good, 1–2 generic | 6–9 |
| Mixed — half semantic, half generic | 3–5 |
| Generic or vanity headings throughout | 0–2 |
```
Replace with:
```
| Condition | Points |
|---|---|
| All headings semantic, keyword-rich, informative standalone | 6 |
| Most headings good, 1–2 generic | 4–5 |
| Mixed — half semantic, half generic | 2–3 |
| Generic or vanity headings throughout | 0–1 |
```

- [ ] **Step 14: Repoint Brand / Source Credibility Signals (5 → 3 pts) — header**

Find:
```
## 9. Brand / Source Credibility Signals (5 pts)
```
Replace with:
```
## 9. Brand / Source Credibility Signals (3 pts)
```

- [ ] **Step 15: Repoint Brand / Source Credibility Signals — scoring table**

Find:
```
| Condition | Points |
|---|---|
| Brand named + licensed aggregator identified + trust signal + author | 5 |
| 2–3 of the above | 3–4 |
| Only brand name present | 1–2 |
| Anonymous or no brand signals | 0 |
```
Replace with:
```
| Condition | Points |
|---|---|
| Brand named + licensed aggregator identified + trust signal + author | 3 |
| 2–3 of the above | 2 |
| Only brand name present | 1 |
| Anonymous or no brand signals | 0 |
```

- [ ] **Step 16: Verify the repointing (expect 11 headers, 100 total points)**

Run:

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude" && python3 - <<'EOF'
import re
path = ".claude/skills/content/content-audit/references/geo-parameters.md"
text = open(path).read()
totals = re.findall(r"\(\s*\d+\s*pts\)", text)
nums = [int(re.search(r"\d+", t).group()) for t in totals]
print(len(nums), sum(nums))
EOF
```

Expected: `11 100`

- [ ] **Step 17: Commit**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude" && git add ".claude/skills/content/content-audit/references/geo-parameters.md" && git commit -m "refactor(content-audit): repoint GEO lens parameters to fit new 100-pt budget"
```

---

### Task 3: Cross-reference the Freshness split in `eeat-framework.md`

**Files:**
- Modify: `/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills/content/content-audit/references/eeat-framework.md`

**Interfaces:**
- Consumes: nothing from Tasks 1–2 (independent file), but the note's wording references "GEO Parameter 11 (Freshness)" which Task 1 created.
- Produces: an overlap note in the Trustworthiness pillar section that Task 4 does not depend on, but that completes the spec's differentiation requirement.

- [ ] **Step 1: Add the overlap note after the Trustworthiness scoring table**

Find:
```
**Scoring:**
| Signals | Points |
|---|---|
| Updated date + commercial disclosure + balanced coverage + accurate claims | 20–25 |
| 2–3 trust signals | 10–19 |
| 1 trust signal | 5–9 |
| No trust signals, or active red flags (misleading claims) | 0–4 |

---

## E-E-A-T Total Score: 0–100
```
Replace with:
```
**Scoring:**
| Signals | Points |
|---|---|
| Updated date + commercial disclosure + balanced coverage + accurate claims | 20–25 |
| 2–3 trust signals | 10–19 |
| 1 trust signal | 5–9 |
| No trust signals, or active red flags (misleading claims) | 0–4 |

**Overlap note:** GEO Parameter 11 (Freshness, in `geo-parameters.md`) also scores
currency of time-sensitive claims independently. This pillar's "last-updated date
visible" signal is one of several general trustworthiness markers (alongside
commercial disclosure, balanced coverage, accurate claims); GEO Parameter 11
specifically checks whether individual price/regulatory claims carry as-of framing.
Both may fire on the same missing date — that's expected overlap between a general
trust signal and its specific application, not a duplicate rule to fix.

---

## E-E-A-T Total Score: 0–100
```

- [ ] **Step 2: Verify the note was added exactly once**

Run:

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude" && python3 - <<'EOF'
path = ".claude/skills/content/content-audit/references/eeat-framework.md"
text = open(path).read()
assert text.count("GEO Parameter 11 (Freshness") == 1
print("OK")
EOF
```

Expected: `OK`

- [ ] **Step 3: Commit**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude" && git add ".claude/skills/content/content-audit/references/eeat-framework.md" && git commit -m "docs(content-audit): cross-reference GEO Freshness parameter in E-E-A-T Trustworthiness pillar"
```

---

### Task 4: Propagate the new parameter table and out-of-scope note into `SKILL.md`, and verify cross-file consistency

**Files:**
- Modify: `/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills/content/content-audit/SKILL.md`

**Interfaces:**
- Consumes: the final point values from Task 2 (`geo-parameters.md` fully repointed) and the out-of-scope section title from Task 1.
- Produces: `SKILL.md`'s Lens 2 table matching `geo-parameters.md` exactly — this is the last task, and its final verification step is the plan's end-to-end consistency check.

Note: the Step 4 report output template (further down in `SKILL.md`, under "### Lens 2 — GEO") uses a generic 2-row example table (`[Parameter name] | ... | X/Max | ...` plus a `...` row) — it does not hardcode all 9/11 parameter names, so it needs no edit for this change.

- [ ] **Step 1: Replace the Lens 2 intro and parameter table**

Find:
```
### Lens 2: GEO Score (0–100)

Read `references/geo-parameters.md` for full parameter definitions.

| # | Parameter | Max Points |
|---|---|---|
| 1 | Direct-Answer Formatting | 15 |
| 2 | E-E-A-T Signals | 15 |
| 3 | Entity Clarity | 10 |
| 4 | Conversational Q&A Coverage | 15 |
| 5 | Statistics & Citations | 10 |
| 6 | Schema / Structured Data Mentions | 10 |
| 7 | Content Depth & Original Angle (1,500+ words, differentiated) | 10 |
| 8 | Semantic Heading Use | 10 |
| 9 | Brand / Source Credibility Signals | 5 |

**⚠️ E-E-A-T Signals (Parameter 2) — FILE MODE scope:**
In FILE MODE, do NOT check: author name/credentials, publish/last-updated date,
DHA/MOH citations, license signal. These are added at publishing, not by the writer.
Instead, score Parameter 2 only on: firsthand experience signals in the writing,
accurate technical detail, content aligned with current consensus, and transparent
methodology. See `references/eeat-framework.md` for FILE MODE scoring rubric.

In URL MODE, check all E-E-A-T signals as defined in the full rubric.
```
Replace with:
```
### Lens 2: GEO Score (0–100)

Read `references/geo-parameters.md` for full parameter definitions. See that file's
"Out of Scope: Technical AI-Citation Factors" section for what this lens does NOT
score (crawler accessibility, live AI-search rank, JS-rendering visibility, domain
authority, llms.txt) — those belong to the `seo` skill's technical audit.

| # | Parameter | Max Points |
|---|---|---|
| 1 | Direct-Answer Formatting | 15 |
| 2 | E-E-A-T Signals | 11 |
| 3 | Entity Clarity | 6 |
| 4 | Conversational Q&A Coverage | 15 |
| 5 | Statistics & Citations | 10 |
| 6 | Schema / Structured Data Mentions | 6 |
| 7 | Content Depth & Original Angle (1,500+ words, differentiated) | 8 |
| 8 | Semantic Heading Use | 6 |
| 9 | Brand / Source Credibility Signals | 3 |
| 10 | Fan-out Rank | 12 |
| 11 | Freshness | 8 |

**⚠️ E-E-A-T Signals (Parameter 2) — FILE MODE scope:**
In FILE MODE, do NOT check: author name/credentials, publish/last-updated date,
DHA/MOH citations, license signal. These are added at publishing, not by the writer.
Instead, score Parameter 2 only on: firsthand experience signals in the writing,
accurate technical detail, content aligned with current consensus, and transparent
methodology. See `references/eeat-framework.md` for FILE MODE scoring rubric.
Currency/freshness is scored separately under Parameter 11 (Freshness), which has
its own FILE MODE rule.

In URL MODE, check all E-E-A-T signals as defined in the full rubric.
```

- [ ] **Step 2: Verify the SKILL.md table on its own (expect 11 rows, 100 total)**

Run:

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude" && python3 - <<'EOF'
import re
path = ".claude/skills/content/content-audit/SKILL.md"
text = open(path).read()
start = text.index("### Lens 2: GEO Score")
end = text.index("In URL MODE, check all E-E-A-T signals", start)
block = text[start:end]
rows = re.findall(r"\|\s*\d+\s*\|[^|]+\|\s*(\d+)\s*\|", block)
assert "Out of Scope: Technical AI-Citation Factors" in block
print(len(rows), sum(int(r) for r in rows))
EOF
```

Expected: `11 100`

- [ ] **Step 3: Verify cross-file consistency between `geo-parameters.md` and `SKILL.md`**

Run:

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude" && python3 - <<'EOF'
import re

geo_path = ".claude/skills/content/content-audit/references/geo-parameters.md"
skill_path = ".claude/skills/content/content-audit/SKILL.md"

geo_text = open(geo_path).read()
geo_points = [int(p) for p in re.findall(r"^## (?:\d+\. ).+? \((\d+) pts\)$", geo_text, re.M)]

skill_text = open(skill_path).read()
start = skill_text.index("### Lens 2: GEO Score")
end = skill_text.index("In URL MODE, check all E-E-A-T signals", start)
block = skill_text[start:end]
skill_points = [int(p) for p in re.findall(r"\|\s*\d+\s*\|[^|]+\|\s*(\d+)\s*\|", block)]

print("geo:", geo_points, sum(geo_points))
print("skill:", skill_points, sum(skill_points))
assert geo_points == skill_points, "mismatch between geo-parameters.md and SKILL.md point values"
print("MATCH")
EOF
```

Expected output (three lines):
```
geo: [15, 11, 6, 15, 10, 6, 8, 6, 3, 12, 8] 100
skill: [15, 11, 6, 15, 10, 6, 8, 6, 3, 12, 8] 100
MATCH
```

- [ ] **Step 4: Commit**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude" && git add ".claude/skills/content/content-audit/SKILL.md" && git commit -m "docs(content-audit): propagate GEO lens parameter changes into SKILL.md"
```

---

## Optional follow-up (not part of this plan's automated verification)

The spec's own verification note suggests a live smoke test: run `/content-audit` against one already-audited health-insurance URL and one travel-insurance URL, and confirm the Lens 2 output shows 11 parameters summing to 100 with evidence-formatted findings for Fan-out Rank and Freshness. This requires actually invoking the LLM skill (not a scripted check) and is worth doing once after Task 4 lands, but isn't a blocking step in this plan since it can't be automated as a deterministic pass/fail command.
