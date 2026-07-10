---
name: content-audit
description: >
  Use when the user invokes /content audit or /content-audit, pastes a content URL, uploads a .md or Word file for review,
  or asks to "audit this content", "check this for SEO", "is this GEO-ready", "does this sound AI",
  "review this article", "score this page", "audit for E-E-A-T", or "fact-check this content/article".
  Also trigger when the user wants to check any written content — blog posts, insurance guides, landing
  pages, comparison pages — from an SEO, GEO (generative engine optimization), AI-detection, or factual
  accuracy lens, including verifying claims, prices, or regulatory statements via web search. Scoped to
  Policybazaar UAE (policybazaar.ae) HEALTH and TRAVEL insurance content only — the vertical (health vs
  travel) is inferred from the content or URL. Other verticals (motor/life/home) and Paisabazaar UAE are
  out of scope. This skill audits content that already exists — for a pre-writing brief
  on a topic that hasn't been drafted yet, use /content brief instead.
---

# SEO Content Audit Skill

Runs a five-lens content audit: **SEO**, **GEO** (AI search citation readiness), **AI Detection**,
**YMYL / Helpful Content**, and **Fact-Check** (live verification via web search). Outputs a
scored report with line-level evidence, issue explanations, and specific recommendations.

Covers **Policybazaar UAE** (policybazaar.ae) **health insurance** and **travel insurance**
content only. The vertical is detected in Step 1; everything vertical-specific (regulator,
terminology, competitors, schema expectations, save folder) comes from the matching context
file, not hardcoded into the lens rubrics. Motor/life/home insurance and Paisabazaar UAE
content are **out of scope** — if the input is one of those, say so and stop rather than
auditing with the wrong rubric.

Invoke command: `/content audit` (via the content hub; `/content-audit` also routes here)

---

## Step 0 — Receive Input & Detect Input Mode

Accept content via any of:
- Pasted text (markdown, plain) → **FILE MODE**
- Uploaded `.md` file → **FILE MODE**
- Uploaded Word (`.docx`) file → **FILE MODE** (extract text before auditing)
- A URL → **URL MODE** (fetch the page and extract body text)

**This matters — FILE MODE and URL MODE have different parameter sets. Declare the mode at
the top of the report.**

If input is unclear, ask: "Please share the content as text, file, or URL." If the person
doesn't have content yet and wants a pre-writing check instead, point them to the
content hub's brief playbook (`/content brief <topic>`).

---

## Step 1 — Auto-Detect Content Type & Brand

Classify the content. State the detected type and brand at the top of the report.

| Type | Signals |
|---|---|
| **Landing page** | Short, conversion-focused, CTA-heavy, product/price mentions |
| **Blog / guide** | Headings, 600+ words, informational intent, "how to / what is" structure |
| **Comparison page** | Tables, "vs", multiple products/plans side by side |
| **Review page** | Star ratings, pros/cons, user quotes, verdict sections |
| **FAQ page** | Question-answer pairs dominate the structure |

If ambiguous, default to **Blog / guide** and note it.

**Vertical** — infer from content/URL, then read the matching context file(s) before scoring:

| Signal | Vertical | Read |
|---|---|---|
| health insurance, medical cover, basic plan/EBP, DHA/DOH/MOHAP, `/health-insurance/` in URL | **Health** | `references/policybazaar-context.md` + `references/schema-expectations-health.md` |
| travel insurance, Schengen/visa cover, trip cancellation, baggage, inbound/outbound, `/travel-insurance/` in URL | **Travel** | `references/policybazaar-context.md` (incl. its Travel section) + `references/schema-expectations-travel.md` |

**Out of scope:** any other Policybazaar vertical (motor/car, life, home, SME) and all
Paisabazaar UAE content (loans/credit/banking). If the input is one of these, STOP and
say it's out of scope for this skill — don't audit it with health/travel rubrics.
If genuinely ambiguous between health and travel, ask. The vertical determines which
regulator, named entities, and schema expectations apply in Lenses 1, 4, and 5 below.

---

## Step 2 — Run the Five-Lens Audit

Score each lens independently. Then combine into an **Overall Content Score**.

---

### Lens 1: SEO Score (0–100)

Read `references/seo-parameters.md` for full parameter definitions and scoring rubrics.

**⚠️ FILE MODE — skip parameters marked [URL ONLY]. Redistribute their points into the
remaining parameters proportionally so the SEO score still totals 100.**

| # | Parameter | Max Points | Mode |
|---|---|---|---|
| 1 | Title Tag | 10 | **URL ONLY** |
| 2 | Meta Description | 8 | **URL ONLY** |
| 3 | Heading Hierarchy (H1–H6) | 10 | Both |
| 4 | Keyword Usage & Density | 10 | Both |
| 5 | Content Depth & Length | 10 | Both |
| 6 | Readability Score | 8 | Both |
| 7 | Internal Linking | 8 | **URL ONLY** |
| 8 | Image Alt Text | 6 | Both |
| 9 | Duplicate / Thin Content Risk | 10 | Both |
| 10 | Structured Data Signals | 10 | **URL ONLY** |
| 11 | CTA Clarity | 5 | **URL ONLY** |
| 12 | Mobile / UX Red Flags in Copy | 5 | Both |

**FILE MODE active parameters:** 3, 4, 5, 6, 8, 9, 12 → rescale to 100.
**URL MODE:** all 12 parameters → score as written.

**Evidence format for every flagged parameter:**
```
❌ / ⚠️  [Parameter name]   [X/Max]
   FOUND: "[exact line or phrase from content]"
   WHY: [one sentence explaining why this is an issue]
   FIX: [specific rewrite or action]
```

**SEO Score: X / 100**

---

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

**Evidence format — same as SEO lens:**
```
❌ / ⚠️  [Parameter name]   [X/Max]
   FOUND: "[exact line from content]"
   WHY: [why this hurts GEO citation potential]
   FIX: [specific rewrite or addition]
```

**GEO Score: X / 100**

---

### Lens 3: AI Detection (Human-Likeness Score, 0–100)

Read `references/ai-detection-parameters.md` for full signal definitions.

This lens flags signals that reduce credibility with readers and lower GEO citation
probability. It does NOT judge AI use as inherently bad.

**⚠️ Read before scoring — two things this lens is NOT:**
1. **Not a verdict.** Commercial AI detectors score identical human-written text anywhere
   from 0% to 54%, and published accuracy ranges 55–97% across tools (full figures in the
   reference file). This lens's signal-scoring sits in that same category — report the
   score and the patterns found, but never state or imply certainty that content "is
   AI-written." Treat it as a tool for tightening generic prose, not a pass/fail gate.
2. **Not the same question as "will this rank."** Google penalizes thin, generic, or
   manipulative content — not AI assistance itself. Human-sounding-but-generic content is
   still a ranking risk; that risk is scored separately in **SEO Parameter 9** and
   **GEO Parameter 7**, not here. This lens stays focused on linguistic register only.

See `references/ai-detection-parameters.md` → "Detector Reliability" for the full case
behind both points before writing up findings.

Score each of the 9 signals 0–3:

| Signal | Max |
|---|---|
| A. Perplexity (word predictability) | 3 |
| B. Burstiness deficit | 3 |
| C. Hedge density | 3 |
| D. Structural tells | 3 |
| E. Specificity deficit | 3 |
| F. Transition word fingerprint | 3 |
| G. Punctuation fingerprint | 3 |
| H. Voice / register collapse | 3 |
| I. Rhetorical scaffolding (RLHF) | 3 |

`Human-Likeness Score = ((27 - raw_signal) / 27) × 100`

**Evidence format — for EVERY signal scored > 0:**
```
[Signal letter]. [Signal name]   [score/3]
   FOUND: "[exact line or phrase from content]"
   WHY THIS IS AI: [one sentence — which specific pattern this matches]
   FIX: "[suggested rewrite of that exact line]"
```

Estimate **AI-Edited Fraction:**
- Pure human (~0%) / Lightly AI-assisted (~10–30%) / Mixed authorship (~30–60%)
- Heavily AI-edited (~60–90%) / Pure AI (~100%)

**Human-Likeness Score: X / 100**

---

### Lens 4: YMYL & Helpful Content Score (0–100)

Read `references/ymyl-helpful-content.md` for full parameter definitions.

This lens applies to all in-scope content because both verticals are YMYL: health
insurance content can impact a person's health and medical-cost decisions, and travel
insurance content impacts financial protection and visa-mandated medical cover decisions —
both classified as YMYL by Google (content that can impact a person's health or financial
wellbeing). Google's December 2025 Core Update applied maximum scrutiny to YMYL sites.
AI Overviews now appear on ~89% of healthcare queries, and financial YMYL content gets
comparable scrutiny. Read `references/policybazaar-context.md` before scoring — the
harm framing differs between health (medical + financial) and travel (financial +
visa-compliance).

| # | Parameter | Max Points |
|---|---|---|
| 1 | Medical / Financial Accuracy | 20 |
| 2 | No Harmful or Misleading Claims | 20 |
| 3 | Balanced & Complete Coverage | 15 |
| 4 | Disclaimer Present (Medical or Financial) | 10 |
| 5 | People-First Intent (Google Helpful Content) | 20 |
| 6 | Content Consensus Alignment | 15 |

**Evidence format — same pattern:**
```
❌ / ⚠️  [Parameter name]   [X/Max]
   FOUND: "[exact line from content]"
   WHY: [why this is a YMYL risk or helpful content failure]
   FIX: [specific correction]
```

**YMYL Score: X / 100**

---

### Lens 5: Fact-Check Score (0–100)

Read `references/fact-check-parameters.md` for full parameter definitions and the
verification process.

This lens actively verifies factual claims using the `web_search` tool — it does not
score from memory. Applies in both FILE MODE and URL MODE.

| # | Parameter | Max Points |
|---|---|---|
| 1 | Numerical Accuracy (prices, %, limits, deadlines) | 25 |
| 2 | Regulatory Claims Accuracy (DHA/MOHAP/DOH) | 25 |
| 3 | Provider / Plan Name Accuracy | 15 |
| 4 | Statistical & Study Citation Accuracy | 15 |
| 5 | Outdated Information Risk | 10 |
| 6 | General Factual Claims | 10 |

**Process:** Extract every checkable claim, run a targeted `web_search` per claim
(or per cluster of related claims), and assign a status: ✅ Confirmed, ❌ Contradicted,
⚠️ Outdated, or ⚠️ Unverifiable. Unverifiable claims should be flagged for human
review, not penalized as if confirmed false. Never fabricate a source or a
confirmation. If web search is unavailable in this context, say so at the top of
this lens and score only on internal-consistency checks.

**Disambiguate regulatory vs. platform figures before assigning Contradicted:** work
out what the page is actually claiming — a **regulatory/mandated figure** (verify
against the regulator's or scheme's own source) vs. the **brand's own platform figure**
(e.g. "plans from AED X on Policybazaar.ae" — external search cannot contradict internal
platform data; mark it ⚠️ Unverifiable-external and recommend attribution + as-of date
instead). If the page doesn't say which it means, flag the ambiguity itself as the issue.

**Source tiers — every CORRECT VALUE must carry one:**
- **Primary** — read directly from the regulator's/provider's own page
- **Secondary — verify internally** — a named third party (broker, news, industry guide)
- **Snippet-only — must verify internally** — search-summary layer, no named page read

**Evidence format:**
```
✅ / ⚠️ / ❌  [Parameter name]   [X/Max]
   CLAIM: "[exact line or phrase from content]"
   VERIFICATION: [search query used] → [what was found, paraphrased, with source]
   CORRECT VALUE: [verified current value + source name + date. Required for every
   Contradicted/Outdated claim — a fact-check that says "wrong" without supplying
   the right figure is half-done. "n/a" only if Unverifiable.]
   SOURCE TIER: Primary / Secondary — verify internally / Snippet-only — must verify internally
   STATUS: Confirmed / Contradicted / Outdated / Unverifiable
   FIX: [correction needed, or "—" if confirmed]
```

**Fact-Check Score: X / 100**

---

## Step 3 — Calculate Overall Score

```
Overall Score = (SEO × 0.20) + (GEO × 0.25) + (Human-Likeness × 0.15) + (YMYL × 0.20) + (Fact-Check × 0.20)
```

**Rating thresholds:**

| Score | Rating |
|---|---|
| 85–100 | ✅ Publish-ready |
| 70–84 | 🟡 Minor fixes needed |
| 55–69 | 🟠 Significant improvements needed |
| 0–54 | 🔴 Major rework required |

---

## Step 4 — Output Format

**Always output the full report in markdown.** Use the exact structure below —
headers, tables, and inline code for quoted content. No plain-text blocks,
no ASCII borders.

---

### Header block

```markdown
# 📋 Content Audit Report — `/content-audit`

| Field | Detail |
|---|---|
| **Mode** | FILE MODE / URL MODE |
| **Brand** | Policybazaar UAE |
| **Vertical** | Health insurance / Travel insurance |
| **Content Type** | [Detected type] |
| **Source** | [URL or filename] |
| **Word Count** | [Approx] |
```

---

### Scores at a Glance

```markdown
## 🎯 Scores at a Glance

| Lens | Score | Rating |
|---|---|---|
| SEO | XX / 100 | 🟢 / 🟡 / 🟠 / 🔴 [label] |
| GEO | XX / 100 | 🟢 / 🟡 / 🟠 / 🔴 [label] |
| Human-Likeness | XX / 100 | 🟢 / 🟡 / 🟠 / 🔴 [label] |
| YMYL / Helpful | XX / 100 | 🟢 / 🟡 / 🟠 / 🔴 [label] |
| Fact-Check | XX / 100 | 🟢 / 🟡 / 🟠 / 🔴 [label] |
| **OVERALL** | **XX / 100** | **🟢 / 🟡 / 🟠 / 🔴 [label]** |
```

Rating labels by score: 85–100 = 🟢 Publish-ready · 70–84 = 🟡 Minor fixes ·
55–69 = 🟠 Needs work · 0–54 = 🔴 Major rework required.

---

### Lens 1 — SEO

```markdown
## 🔍 Lens 1 — SEO Audit `XX/100`

> FILE MODE — Title Tag, Meta, Internal Linking, Structured Data, CTA skipped.
> (Remove this line in URL MODE)

| Parameter | Status | Score | Finding |
|---|---|---|---|
| [Parameter name] | ✅/⚠️/❌ | X/Max | One-line summary of finding. |
| ... | | | |

### ❗ Top SEO Issues

| # | Found | Why | Fix |
|---|---|---|---|
| 1 | *"exact line from content"* | One sentence: why this is an SEO problem. | Specific rewrite or action. |
| 2 | *"exact line"* | Explanation. | Fix. |
| 3 | *"exact line"* | Explanation. | Fix. |
```

Only include the Top Issues table for parameters scored ⚠️ or ❌.
Always use *italics* for quoted content from the source.

---

### Lens 2 — GEO

```markdown
## 🌐 Lens 2 — GEO Audit `XX/100`

| Parameter | Status | Score | Finding |
|---|---|---|---|
| [Parameter name] | ✅/⚠️/❌ | X/Max | One-line summary. |
| ... | | | |

### ❗ Top GEO Issues

| # | Found | Why | Fix |
|---|---|---|---|
| 1 | *"exact line"* | Why this hurts GEO citation potential. | Specific rewrite. |
| 2 | *"exact line"* | Explanation. | Fix. |
| 3 | *"exact line"* | Explanation. | Fix. |
```

---

### Lens 3 — AI Detection

```markdown
## 🤖 Lens 3 — AI Detection `Human-Likeness: XX/100`

> Pattern-match label, not a claim about authorship — see Detector Reliability note.

| Pattern-Match Label | AI-Edited Fraction |
|---|---|
| Human-consistent / Mostly human-consistent / Mixed signals / AI-pattern-heavy / Strongly AI-pattern-heavy | [bucket] |

| Signal | Score | Finding |
|---|---|---|
| A. Perplexity | X/3 | One-line summary of what fired. |
| B. Burstiness Deficit | X/3 | ... |
| C. Hedge Density | X/3 | ... |
| D. Structural Tells | X/3 | ... |
| E. Specificity Deficit | X/3 | ... |
| F. Transition Fingerprint | X/3 | ... |
| G. Punctuation Fingerprint | X/3 | ... |
| H. Voice / Register | X/3 | ... |
| I. Rhetorical Scaffolding | X/3 | ... |

### ❗ Top AI Detection Issues

| # | Found | Pattern Matched | Fix |
|---|---|---|---|
| 1 | *"exact line"* | Which specific signal this matches. | *"Rewritten version adding a fact, name, or detail."* |
| 2 | *"exact line"* | Pattern explanation. | *"Rewrite."* |
| 3 | *"exact line"* | Pattern explanation. | *"Rewrite."* |
```

Only list signals scored > 0 in the signal table.
Fix column should add substance (data/example/detail), not just swap words — see
`references/ai-detection-parameters.md` → "Fix Guidance."

---

### Lens 4 — YMYL & Helpful Content

```markdown
## ⚕️ Lens 4 — YMYL & Helpful Content `XX/100`

| Parameter | Status | Score | Finding |
|---|---|---|---|
| Medical / Financial Accuracy | ✅/⚠️/❌ | X/20 | One-line summary. |
| No Harmful / Misleading Claims | ✅/⚠️/❌ | X/20 | ... |
| Balanced & Complete Coverage | ✅/⚠️/❌ | X/15 | ... |
| Disclaimer Present | ✅/⚠️/❌ | X/10 | ... |
| People-First Intent | ✅/⚠️/❌ | X/20 | ... |
| Content Consensus Alignment | ✅/⚠️/❌ | X/15 | ... |

### ❗ Top YMYL Issues

| # | Found | Why | Fix |
|---|---|---|---|
| 1 | *"exact line"* | Why this is a YMYL risk or helpful content failure. | Specific correction. |
| 2 | *"exact line"* | Explanation. | Fix. |
| 3 | *"exact line"* | Explanation. | Fix. |
```

---

### Lens 5 — Fact-Check

```markdown
## 🔎 Lens 5 — Fact-Check `XX/100`

> Claims verified via web search. ⚠️ Unverifiable claims flagged for human review, not penalized as false.
> (If web search was unavailable, replace this line with: "⚠️ Web search unavailable — scored on internal consistency only.")

| Parameter | Status | Score | Finding |
|---|---|---|---|
| Numerical Accuracy | ✅/⚠️/❌ | X/25 | One-line summary. |
| Regulatory Claims Accuracy | ✅/⚠️/❌ | X/25 | ... |
| Provider / Plan Name Accuracy | ✅/⚠️/❌ | X/15 | ... |
| Statistical & Study Citation Accuracy | ✅/⚠️/❌ | X/15 | ... |
| Outdated Information Risk | ✅/⚠️/❌ | X/10 | ... |
| General Factual Claims | ✅/⚠️/❌ | X/10 | ... |

### ❗ Top Fact-Check Issues

| # | Claim | Verification | Correct Value (source, date) | Source Tier | Status | Fix |
|---|---|---|---|---|---|---|
| 1 | *"exact line"* | [Search query] → what was found, paraphrased, with source. | AED 635/yr (Sukoon DHA-EBP page, Jul 2026) | Primary | Contradicted / Outdated / Unverifiable | Specific correction. |
| 2 | *"exact line"* | ... | AED 725/yr upper bound (egsh.ae, Pacific Prime, Jul 2026) | Secondary — verify internally | ... | ... |
| 3 | *"exact line"* | ... | ... | Snippet-only — must verify internally | ... | ... |
```

Only include the Top Issues table for claims scored ⚠️ or ❌.
Cite sources by name (e.g. "per DHA's official site"), never reproduce search-result
text verbatim.

---

### Priority Recommendations

```markdown
## 🚦 Priority Recommendations

| Priority | Issue | Action |
|---|---|---|
| 🔴 Critical | [Issue label] | Specific action — what to write/delete/add. |
| 🔴 Critical | ... | ... |
| 🟠 High | ... | ... |
| 🟡 Medium | ... | ... |
| 🟢 Quick Win | [Issue label] | Low-effort, high-impact action. |

---

> **Follow-up options:** Reply with `Humanize this content` · `Fix SEO issues` · `GEO rewrite` · `Fix YMYL issues` · `Fix Fact-Check issues` · `Full rewrite`
```

After outputting the report on-screen, follow Step 4.5 to save the .md and append the
master workbook.

---

## Step 4.5 — Save the Report Files (Policybazaar URL audits)

Besides the on-screen markdown report (Step 4), every URL MODE audit saves two files:

**File 1 — per-URL detailed report (.md), dated:**
`policybazaar-<page-slug>-content-audit-YYYY-MM-DD.md`
Full Step 4 report content, plus the schema deep-dive and a verification ledger
(figures + source + tier). One file per URL per audit date.

**File 2 — rolling master workbook (.xlsx), undated:**
`policybazaar-insurance-content-audit.xlsx` — ONE per vertical folder.
- If it exists: `openpyxl.load_workbook()` and APPEND rows — NEVER overwrite,
  never create a dated copy. Re-audits of the same URL append a new row
  (keeps before/after history).
- If missing: create with these 7 sheets, every sheet carrying URL + Audit Date
  columns and auto-filters:

  | Sheet | Layout |
  |---|---|
  | Summary | One row per URL: lens scores, OVERALL, rating, .md filename |
  | Lens Scores | One row per URL × parameter (all five lenses) |
  | Findings | URL · Lens · Severity · Found · Why · Fix |
  | Fact-Check | URL · Claim · Verification · Correct Value (source, date) · Source Tier · Status · Fix |
  | Schema | URL · inventory + findings from the implemented-schema audit |
  | Priority Recs | URL · Priority · Action |
  | Verification Ledger | Vertical-wide verified figures with source + tier |

**Save locations (verified — the doubled "Documents/Documents" is correct):**

| Vertical | Folder |
|---|---|
| Health insurance | `/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result/` |
| Travel insurance | `/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Travel Insurance/Result/` |
| Any other vertical | Out of scope for this skill — do not audit or save |

Note: the master shares the same filename in every vertical folder by design — the
folder, not the filename, identifies the vertical.

FILE MODE audits (pasted text/drafts): on-screen report only, unless asked to save.

---

## Step 5 — Optional Follow-up Actions

After delivering the report, offer:

1. **"Humanize this content"** → Fix AI detection signals using the FOUND lines as targets.
   Prioritize fixes that add substance — original data, named examples, firsthand detail,
   varied sentence rhythm, brand voice — over surface rewording. Synonym-swapping and
   generic "humanizer" rewrites barely move detector scores (they target vocabulary;
   detectors weigh structure) and can read worse. See `references/ai-detection-parameters.md`
   → "Fix Guidance" for what actually works vs. what doesn't.
2. **"Fix SEO issues"** → Rewrite title, meta, headings per flagged findings
3. **"GEO rewrite"** → Restructure for AI citation readiness
4. **"Fix YMYL issues"** → Address accuracy, disclaimer, and helpful content gaps
5. **"Fix Fact-Check issues"** → Correct or remove claims flagged Contradicted/Outdated; resolve Unverifiable claims with the user or remove them
6. **"Full rewrite"** → All five improvements in one revised draft

---

## Reference Files

Read the relevant file before scoring each lens:

- `references/policybazaar-context.md` — vertical, regulator, terminology, competitors for policybazaar.ae content
- `references/seo-parameters.md` — 12 SEO parameters, scoring rubrics, FILE vs URL MODE rules, UAE examples
- `references/schema-expectations-health.md` — page-type schema stacks, known bugs, and excluded/blocklisted types for policybazaar.ae health URLs (distilled from workspace SCHEMA-PLAN.md, 2026-07-06)
- `references/schema-expectations-travel.md` — same for travel URLs: implemented-today baseline, expected stacks per page type, travel-specific bugs (T1–T11), blocklist (built from live fetches of 12 representative pages, 2026-07-10)
- `references/geo-parameters.md` — 9 GEO parameters, FILE MODE E-E-A-T scope, UAE insurance context
- `references/ai-detection-parameters.md` — 9 AI signals, evidence format, detector-reliability caveats, insurance-specific banned vocab
- `references/eeat-framework.md` — Full E-E-A-T rubric for YMYL/insurance; FILE MODE vs URL MODE split
- `references/ymyl-helpful-content.md` — YMYL compliance + Google Helpful Content parameters (NEW)
- `references/fact-check-parameters.md` — 6 Fact-Check parameters, web_search verification process, status buckets (NEW)

## Assets

- `assets/policybazaar-urls.txt` — full live URL list for policybazaar.ae (~3,750 URLs, July 2026 snapshot) — used by SEO Parameter 7's missed-opportunity check; grep it, don't load it wholesale
