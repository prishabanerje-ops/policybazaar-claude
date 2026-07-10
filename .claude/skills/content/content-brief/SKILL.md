---
name: content-brief
description: >
  Use when the user invokes /content-brief, or wants a pre-writing content brief BEFORE
  anything is drafted — e.g. "help me plan this piece", "give me a brief on [topic]",
  "what should I write about [keyword]", "should I write this", "go/no-go on this content
  idea", or shares a topic/keyword and asks what angle or outline to take. This actively
  researches competitors and current facts via web search and produces a full brief:
  target keyword/intent, what's already ranking and the gap to fill, a stated
  differentiation angle, verified facts/figures with sources, a section-by-section
  outline, and a completeness go/no-go check. Covers both Policybazaar UAE (insurance)
  and Paisabazaar UAE (personal loans/credit/banking) — infers which brand from the
  topic. Use this INSTEAD of the content-audit sub-skill when the content doesn't exist
  yet — content-audit scores finished drafts; this skill plans what to write before
  drafting starts.
---

# Content Brief Skill

Produces a research-backed pre-writing brief so a content writer knows the target
keyword, the angle that differentiates the piece from what's already ranking, the facts
they'll need (already sourced), and a section-by-section outline — before they write a
single sentence. Closes with a completeness self-check.

Covers both **Policybazaar UAE** (insurance) and **Paisabazaar UAE** (personal loans,
credit cards, banking) — the two sister brands under PB Fintech. Brand is inferred from
the topic in Step 0; everything brand-specific (regulator, terminology, competitors,
site domain) comes from the matching context file, not hardcoded into the workflow.

This is the generative counterpart to the sibling `content-audit` sub-skill: this skill
plans content that doesn't exist yet; `/content audit` scores content that does. Once a
piece is drafted from this brief, run `/content audit` on it for the full five-lens score.

Invoke command: `/content brief` (also `/content-brief`)

---

## Step 0 — Receive Input

Required: a topic or target keyword. If neither is given, ask for one.

Optional, use if given, don't block on it: page type, outline notes already in mind,
competitors already known, emirate/audience focus, any draft angle already being
considered.

**Determine the brand** — policybazaar.ae (insurance) or paisabazaar.ae (personal
loans/credit/banking). Infer from the topic where possible:

| Signal | Brand |
|---|---|
| health/life/motor/travel insurance, takaful, coverage, premium, DHA/DOH/MOHAP | **Policybazaar** |
| personal loan, credit card, EMI, credit score, savings account, bank | **Paisabazaar** |

If genuinely ambiguous (or the topic spans both, e.g. "financial planning for expats in
Dubai"), ask which brand this brief is for. This determines which context file to read
next — `references/policybazaar-context.md` or `references/paisabazaar-context.md` —
and everything brand-specific downstream (regulator, terminology, competitors, the
`site:` domain for searches) comes from that file. Read it now, before Step 1.

**Determine page type** — Commercial or Article. Infer from the keyword where possible:

| Signal | Type |
|---|---|
| "apply", "buy", "get quote", "compare plans", a named product/plan | **Commercial** |
| "how to", "what is", "guide", "eligibility", "vs" as a concept comparison | **Article** |

If genuinely ambiguous, ask which — don't guess on this one, since Steps 1–4 branch on it.

---

## Step 1 — Competitor & SERP Research

Don't skip to summarizing snippets — actually read the pages, since the whole point of
this step is finding a *specific* gap, and snippets rarely show it.

1. `web_search` the target keyword (add "UAE" or the relevant emirate if not already in
   the keyword).
2. `web_fetch` the top 2–3 organic results — read what they actually cover, not just the
   snippet. Cross-check names against the "Known Competitors" table in the brand-context
   file loaded in Step 0 — it won't be exhaustive, but it catches obvious misspellings
   or a competitor you'd otherwise miss.
3. Check for cannibalization: `grep -i` the target keyword against the brand's bundled
   URL asset (`assets/policybazaar-urls.txt` or `assets/paisabazaar-urls.txt`, per Step 0)
   to see whether an existing internal page already targets this exact keyword or
   cluster. Fall back to a live `site:` search only if the topic is plausibly newer than
   the asset's July 2026 snapshot. Carry the result into Step 5's cannibalization check.
4. Optionally, check `references/news-and-trends.md` for a current regulatory/rate
   change worth folding into the Angle or Facts table — skip if nothing relevant turns up.
5. If nothing directly competing turns up (plausible for a genuinely new angle or a
   low-volume long-tail term), say so explicitly rather than forcing a comparison — note
   it as a likely content-gap opportunity instead.
6. **Source real questions for the FAQ block and H2s (NEW):** `web_search` the target
   topic alongside "reddit" and separately alongside "quora," and search the topic
   phrase directly to surface Google's "People Also Ask" pattern. Pull 3–5 genuinely
   real questions from what comes back — don't invent plausible-sounding ones. Carry
   these into Step 4's FAQ block and H2 phrasing. If a search genuinely turns up nothing
   usable, say so rather than presenting an invented question as if it were sourced.

Build the snapshot:

```markdown
## 🔎 What's Already Ranking

| Rank | Page | Format | Covers | Gap |
|---|---|---|---|---|
| 1 | [competitor/page name] | Guide / Table / FAQ / Landing | [what it already covers, in your own words] | [what it's missing] |
| 2 | ... | | | |
| 3 | ... | | | |
```

Summarize each competitor's coverage in your own words — don't quote their copy. One
short paraphrase per page is enough; the "Gap" column is what actually matters here.

---

## Step 2 — Determine the Angle

From the "Gap" column, state **one** concrete sentence: the specific thing this piece
will do that the competitors don't. This is the single most important line in the brief —
it's what separates a real brief from a keyword with a to-do list attached.

**Concrete, not vague:**
- ✅ "Competitor pages give one UAE-wide waiting-period figure; this piece breaks it down
  by emirate since DHA/DOH/MOHAP timelines actually differ — that's the gap."
- ❌ "This piece will be more comprehensive and better than competitors."

If Step 1 found no real competing pages, the angle can instead state what makes this a
useful first-mover piece (what question it answers that nothing else currently does).

```markdown
## 🎯 The Angle

[One sentence.]
```

---

## Step 3 — Facts to Verify

List every claim type the piece will plausibly need — pull the regulator names and
terminology from Step 0's brand-context file rather than assuming; don't wait for a
draft to exist to start checking these:
- AED prices, premiums/rates, fees, coverage minimums or credit limits, eligibility bands
- Regulator claims — DHA/DOH/MOHAP for Policybazaar topics, CBUAE/AECB for Paisabazaar
  topics (per the brand-context file loaded in Step 0)
- Named providers — insurers/plans for Policybazaar, banks/lenders/cards for Paisabazaar
  — check for rebrands (e.g. Oman Insurance → Sukoon)

Run a targeted `web_search` per claim or tight cluster of related claims (same approach
as the Fact-Check lens in the `content-audit` sub-skill). Never fabricate a figure or a source — if a
search doesn't turn up a reliable current answer, say so in the table rather than
guessing.

For regulatory or product figures, prefer fetching the regulator's/provider's own page
over relying on search snippets. Label every value with a source tier — **Primary**
(read directly from the regulator's/provider's own page), **Secondary — verify
internally** (a named third party), or **Snippet-only — must verify internally**
(search-summary layer, no named page read) — and never hand a writer an unlabeled
search-summary figure.

```markdown
## 📊 Facts & Figures to Use

| Claim Needed | Current Value Found | Source | Source Tier |
|---|---|---|---|
| DHA minimum coverage (Dubai) / AECB credit score range | [value] | [source name] | Primary / Secondary — verify internally / Snippet-only — must verify internally |
| [Insurer or bank/card] name — current | [name] | [source name] | ... |
| ... | | | |
```

Cite sources by name (e.g. "per DHA's official site" or "per Central Bank of the UAE");
paraphrase what you find, don't reproduce search-result text verbatim.

---

## Step 4 — Build the Outline

Branch by page type determined in Step 0.

### If Article:

```markdown
## 📐 Outline — Article

- **H1:** [semantic, keyword-bearing — not a vanity heading]
- **Intro:** direct answer to the core query in 2–3 sentences (don't bury the lede)
- **H2:** [question-phrased heading, drawn from Step 1's real-question research where
  possible — avoid generic templated headings like "Overview," "Benefits," or "Why
  Choose Us" with no topic attached] — direct-answer lead, then: [bullets of what to
  cover here, pulled from the Facts table and the Angle]
- **H2:** [repeat per subtopic — cover every major subtopic a reader would need]
- **FAQ block:** [3–5 questions sourced in Step 1 from PAA/Reddit/Quora — not invented —
  each with a 1-line note on what the concise answer should cover]
- **Internal links:** [2–3 existing pages this should link to/from, with suggested
  anchor text — not "click here". See `references/internal-linking-guide.md` for the
  research method — don't leave this as a guess.]
- **Schema flags:** [FAQ / Article / HowTo — whichever the structure supports]
```

### If Commercial:

```markdown
## 📐 Outline — Commercial

- **Hero:** value-prop headline + the ONE primary CTA, stated once
- **Format:** comparison table vs. explainer — [pick one, and say why, based on
  whether the keyword signals transactional or research intent]
- **Comparison block:** [named plans/insurers to include, pulled from the Facts table]
- **Eligibility/coverage section:** [bullets, pulled from the Facts table]
- **Differentiator section:** [The Angle, rewritten as actual copy direction for this page]
- **Trust section:** author/reviewer credential, license signal, one trust stat (give
  this a specific heading tied to what it actually says — avoid defaulting to generic
  templated headings like "Why Buy From Us" or "Why Choose Us")
- **Schema flags:** [FinancialProduct / InsuranceProduct / Review — whichever applies]
```

---

## Step 5 — Completeness Self-Audit

Read `references/pre-writing-checklist.md` for the full Commercial/Article parameter
tables and verdict logic.

Confirm each of the six parameters for the matching page type against what Steps 1–4
actually established — this should mostly come back ✅, since Steps 1–4 exist specifically
to answer these. A ⚠️ or ❌ here means a real gap slipped through, not a formality.

```markdown
## ✅ Brief Completeness Check

| Parameter | Status | Confirmed By |
|---|---|---|
| [Parameter name] | ✅/⚠️/❌ | [Which section resolves it, or what's still missing] |
| ... | | |

**Verdict:** ✅ Go / 🟡 Conditional Go / 🔴 No-Go
```

Only elaborate on rows marked ⚠️ or ❌ — for those, add one line on what's needed to close
the gap.

---

## Step 6 — Assemble & Output

Output the full brief as one markdown document, in this order: Header → SERP Snapshot →
The Angle → Facts & Figures → Outline → Completeness Check.

```markdown
# 📝 Content Brief — [Working Title]

| Field | Detail |
|---|---|
| **Brand** | Policybazaar UAE / Paisabazaar UAE |
| **Page Type** | Commercial / Article |
| **Target Keyword** | [primary] |
| **Secondary Keywords** | [2–4 related/LSI terms] |
| **Search Intent** | Informational / Commercial / Transactional |
| **Word Count Target** | [range] — a floor, not a target; density beats padding |
| **Author/Reviewer Needed** | [role + credential — see the brand-context file's "E-E-A-T Credential Pattern"] |
| **Update Trigger** | [what would make this stale] |
| **Update Owner** | [who re-checks it] |

[SERP Snapshot from Step 1]

[The Angle from Step 2]

[Facts & Figures from Step 3]

[Outline from Step 4]

[Completeness Check from Step 5]

---

> Once drafted, run `/content audit` on the finished piece for the full five-lens score.
```

---

## Step 7 — Optional Follow-up

After delivering the brief, offer:
1. **"Different angle"** → re-run Step 2 with a different gap from the SERP snapshot, or dig into a competitor more closely
2. **"More competitor research"** → widen Step 1 beyond the top 3
3. **"Draft this"** → write a first draft directly from the assembled brief
4. **"Adjust for [emirate]"** → narrow facts/regulatory citations to a specific emirate instead of UAE-wide

---

## Reference Files

- `references/policybazaar-context.md` — vertical, regulator, terminology, competitors, site structure for policybazaar.ae briefs
- `references/paisabazaar-context.md` — vertical, regulator, terminology, competitors, site structure for paisabazaar.ae briefs
- `references/internal-linking-guide.md` — research method for the outline's internal-linking line (grep-based, using the bundled URL assets)
- `references/news-and-trends.md` — sourcing current regulatory/rate hooks for the Angle and Facts
- `references/pre-writing-checklist.md` — Commercial & Article completeness self-audit tables, verdict logic

## Assets

- `assets/policybazaar-urls.txt` — full live URL list for policybazaar.ae (~3,750 URLs, July 2026 snapshot) — grep this, don't load it wholesale
- `assets/paisabazaar-urls.txt` — full live URL list for paisabazaar.ae (~2,930 URLs, July 2026 snapshot) — grep this, don't load it wholesale
