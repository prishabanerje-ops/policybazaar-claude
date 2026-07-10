# Pre-Writing Checklist — Completeness Self-Audit

The closing step of a content brief (`/content-brief`). By the time you reach this file,
Steps 1–4 of the brief (competitor/SERP research, the stated angle, fact verification, and
the outline) should have already produced real answers to most of these — this is a
self-audit confirming the brief actually did its job, not a cold checklist filled in from
guesswork. Commercial and Article pages carry different risks, so they get separate
tables — use the one matching the page type from Step 0.

The two failure modes this catches are the ones that are cheap to fix in a brief and
expensive to fix after publish: a generic/undifferentiated angle, and a fact that turns
out wrong or stale. Both are far easier to catch here than after a page is written,
reviewed, and published.

**Evidence format for every parameter:**
```
✅ / ⚠️ / ❌  [Parameter name]
   CONFIRMED BY: [which part of the brief resolves this — e.g. "SERP Snapshot + The Angle"]
   IF STILL UNRESOLVED: [the fails-if condition — why it matters]
   ACTION: [what to do — assign it, flag for human decision, or research further]
```

Mark ✅ only when an earlier section of the brief actually resolved it — not because it
seems like a reasonable guess. If research genuinely turned up nothing (e.g. no clear
existing page to compare against for a brand-new topic), that's a legitimate ⚠️, not a
reason to force a ✅.

---

## Commercial Pages

*Product, category, and landing pages with a direct conversion goal — e.g. "Best Health
Insurance Plans in Dubai" or "Compare Travel Insurance UAE" (Policybazaar), or "DIB Zero
Balance Account" or "Best Credit Cards in UAE" (Paisabazaar).*

| # | Parameter | Question the Brief Must Answer | Fails If… |
|---|---|---|---|
| 1 | **Search intent match** | Is the user ready to apply/compare/buy, or still researching? Does the planned page format match (comparison table vs. long explainer)? | The plan is a generic explainer when the keyword signals transactional intent ("apply," "best," "compare"). |
| 2 | **Live, verifiable numbers** | What are today's actual rates/fees/eligibility figures for every product mentioned — sourced from the bank/insurer or a search, not memory? | Any rate, fee, or eligibility figure in the Facts table isn't confirmed against a current source. |
| 3 | **Differentiation vs. competitors** | What will this page say that the top 3 ranking competitor pages for the same keyword don't already say? | The Angle section could be published on a competitor's site with a find-and-replace of the brand name. |
| 4 | **E-E-A-T signals** | Who is the named author/reviewer, and what's their credential for this specific product category? | No named author is assigned in the Header, or the assigned author's credential is unrelated to finance/insurance. |
| 5 | **Conversion path clarity** | What is the one action the page wants the user to take, and is it stated once, clearly? | The outline has a vague CTA, repeats the same ask 4+ times, or has multiple equally-weighted asks competing with each other. |
| 6 | **Cannibalization check** | Does an existing live page already target this exact keyword/cluster? | The URL asset wasn't grepped for this keyword before finalizing the brief, or it surfaced a conflict that wasn't resolved. |

---

## Article Pages

*Informational guides, comparisons, and explainers built to rank and inform, not convert
directly — e.g. "Waiting Periods in UAE Health Insurance Explained" or "DHA vs. DOH:
What's the Difference?" (Policybazaar), or "Personal Loan Eligibility" or "How to Check
Credit Score" (Paisabazaar).*

| # | Parameter | Question the Brief Must Answer | Fails If… |
|---|---|---|---|
| 1 | **Search intent match** | Is this informational (how/why/what) or comparison intent? Does the planned structure (steps, FAQ, table) match what's already ranking for this query? | The outline is a listicle for a query where ranking pages are step-by-step guides, or vice versa. |
| 2 | **Original angle** | What's the one fact, example, or data point this draft will include that isn't already on the top 3 ranking pages? | The Angle section is just a reorganized version of what competitors already say. |
| 3 | **Source-backed claims** | For every factual claim planned (rates, eligibility, dates, regulations), what's the source — official site, regulator, or internal data? | A row in the Facts table has no source, or the source is "memory"/assumption. |
| 4 | **Sentence-level variety check** | Will the finished draft be checked for AI-typical patterns (generic openers, formulaic transitions, restated summaries, repeated adjectives) before publish? | No check is planned — flag this as a reminder for whoever runs `/content-audit` after drafting. |
| 5 | **Internal linking plan** | Which 2–3 existing pages should this article link to/from, and is the anchor text specific (not "click here")? | The outline would leave the article an orphan page, or linking only to the homepage. |
| 6 | **Update trigger & owner** | What would make this article outdated (rate change, regulation change, seasonal offer), and who owns re-checking it? | The Header's Update Trigger or Update Owner field is blank. |

---

## Verdict Logic

Count parameters marked ⚠️ or ❌ across the six rows for the applicable page type:

| Unresolved parameters | Verdict | Meaning |
|---|---|---|
| 0 | ✅ **Go** | Brief is specific and checkable enough to draft from now |
| 1–2 | 🟡 **Conditional Go** | Draft can start, but resolve these in parallel — don't publish until they're ✅ |
| 3+ | 🔴 **No-Go** | Too much is unresolved — go back and finish the research steps before finalizing |

Parameter 3 (Differentiation / Original Angle) and Parameter 6 (Cannibalization / Update
Owner) deserve extra weight if forced to prioritize — they're the two the source case
study ties most directly to real ranking and duplication risk, versus the others, which
are more about execution quality.

---

## Sources

Adapted from an internal case study, "AI in Content (Analysis, Use Case & Recommendation),"
prepared for Paisabazaar.ae (June 2026), which synthesizes:
- Graphite.io AI-content-prevalence reporting
- Ahrefs AI content prevalence study (April 2025)
- Axios reporting on AI vs. human-authored web content (Oct 2025)
- Originality.ai AI Detection Accuracy Studies meta-analysis
- GradPilot AI Detector False Positive Rates (2026 data)
- University of Chicago Booth School, "Artificial Writing and Automated Detection" (2025)
- Weber-Wulff et al., AI detector benchmark study (2023)
- Google Search Central guidance on AI-generated content and Helpful Content
- Live detector testing on two Paisabazaar.ae articles (ZeroGPT, QuillBot, HumanizeAI.pro,
  GPTZero, Grammarly — June 2026)
