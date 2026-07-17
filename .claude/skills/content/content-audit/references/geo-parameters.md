# GEO Parameters — Scoring Reference

Full definitions and rubrics for the 9 GEO (Generative Engine Optimization) parameters
used in `/content-audit`.

GEO is the practice of optimizing content so that AI search engines (ChatGPT, Perplexity,
Google AI Overviews, Gemini, Claude) cite it in their responses. The goal shifts from
"ranking on a search results page" to "being the data source an AI assistant trusts enough
to quote."

---

## Background: Why GEO Matters for Policybazaar UAE (Health & Travel)

- AI Overview keywords grew from 1.5% → ~32% of searches in 12 months (Sep 2024–Sep 2025)
- AI search platform visits grew 42.8% YoY vs Google's 2.4%
- YMYL (Your Money or Your Life) content — which both health and travel insurance
  are — gets stricter AI scrutiny
- ChatGPT is now a trackable traffic channel for the brand
- The foundational GEO study (Aggarwal et al., ACM KDD 2024, 10,000 queries) found
  that adding statistics, citations, and quotations improved AI engine visibility by up to 40%
- Despite AI-assisted content being roughly half of new web publishing volume, ~86% of
  top-ranking Google results and ~82% of ChatGPT/Perplexity citations are human-written —
  what separates the winners isn't authorship, it's original data, visible credentials,
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

**What it is:** AI engines scan content for the fastest path to a usable answer.
Content that leads each section with a direct answer (before elaborating) gets cited more.

**What to check:**
- Does the intro paragraph answer the core question within the first 2–3 sentences?
- Do H2/H3 sections start with a direct 1–2 sentence answer before expanding?
- Are definitions given upfront? e.g. "Health insurance in UAE covers..." (not "Health insurance is a complex topic...")
- Is there an "Answer first, context second" structure throughout?
- No buried-lede pattern (answer hidden in paragraph 5 of a 7-paragraph section)

**UAE insurance example:**
✅ "The minimum health insurance requirement in UAE is a basic plan that covers emergency care, as mandated by the Dubai Health Authority for all residents."
❌ "Health insurance requirements in UAE have evolved over the years as regulations have developed across different emirates..."

**Scoring:**
| Condition | Points |
|---|---|
| Every major section leads with a direct answer; intro answers the primary query in 2 sentences | 15 |
| Most sections have direct answers; 1–2 buried-lede violations | 10–14 |
| Some direct answers but inconsistent — half the sections bury the lead | 5–9 |
| No direct-answer structure; everything is context-first | 0–4 |

---

## 2. E-E-A-T Signals (11 pts)

**What it is:** Experience, Expertise, Authoritativeness, Trustworthiness. AI engines
weight YMYL content especially hard on E-E-A-T. See `references/eeat-framework.md`
for the full YMYL/insurance scoring rubric.

**What to check:**
- **Experience:** Does the content show real-world familiarity? (specific examples, edge cases, "from our data")
- **Expertise:** Is there an author attribution with credentials? Expert quotes? Accurate technical detail?
- **Authoritativeness:** Are authoritative sources cited? (DHA, MOH, official UAE government sites, licensed insurers)
- **Trustworthiness:** Transparent methodology? No exaggerated claims? (Currency/last-updated date is scored separately — see Parameter 11, Freshness.)
- Brand signals: is Policybazaar UAE identified as a licensed insurance aggregator?

**Scoring:**
| Condition | Points |
|---|---|
| Author + credentials + official sources cited + brand license signal (all 4 E-E-A-T pillars) | 11 |
| 3 of 4 E-E-A-T pillars demonstrated | 7–10 |
| 2 of 4 pillars | 3–6 |
| Generic content with no E-E-A-T signals | 0–2 |

---

## 3. Entity Clarity (6 pts)

**What it is:** AI engines build knowledge graphs. Content that clearly identifies
entities (brand names, products, places, regulations, people) and their relationships
gets extracted and cited more reliably.

**What to check:**
- Are product/plan names precise? ("Daman Thiqa" not "a network plan")
- Are regulatory bodies named precisely? (DHA, HAAD → now DOH, MOH)
- Are geographic entities specific? ("Abu Dhabi" not "the UAE capital")
- Is Policybazaar UAE identified as a distinct entity from Policybazaar India?
- Are insurance terms defined on first use with their local UAE context?

**Scoring:**
| Condition | Points |
|---|---|
| All major entities named precisely; regulatory/geographic clarity throughout | 6 |
| Most entities clear; 1–2 vague references | 4–5 |
| Several vague or conflated entities | 2–3 |
| Generic entity usage throughout (just "insurance companies", "the government") | 0–1 |

---

## 4. Conversational Q&A Coverage (15 pts)

**What it is:** AI engines are prompted with questions. Content that contains
explicit question-and-answer pairs has a structural advantage for being cited.

**What to check:**
- Are FAQ sections present with real questions (not vanity questions)?
- Do questions match how people actually ask? (conversational, "how much does...", "can I...")
- Are answers concise enough to be quoted? (under 3 sentences is ideal for AI citations)
- Is voice-search phrasing used? ("What is the best health insurance in Dubai for a family of 4?")
- Coverage of long-tail question variants?
- **Verifying "real" vs. invented (NEW):** when auditing a URL and genuine verification
  matters, `web_search` the topic alongside "reddit" or "quora," and search the topic
  phrase directly to check Google's "People Also Ask" pattern. If the page's FAQ
  questions closely match what real users actually ask on these sources, that's a strong
  positive signal. If the questions read as plausible-sounding but don't match anything
  findable in real search behavior, treat that as a specificity/genericness flag, not
  just a phrasing style note. (`content-brief` sources FAQ questions this way at the
  planning stage — see its `SKILL.md` — so content built from a brief should already
  pass this check by construction.)

**Scoring:**
| Condition | Points |
|---|---|
| 5+ genuine Q&A pairs, conversational phrasing, concise answers | 15 |
| 3–4 Q&A pairs, mostly well-phrased | 10–14 |
| 1–2 Q&A pairs, or FAQ section with vague/generic questions | 5–9 |
| No Q&A structure | 0–4 |

---

## 5. Statistics & Citations (10 pts)

**What it is:** The foundational GEO academic study found statistics and citations
improve AI engine visibility by up to 40%. Numbers make claims quotable and verifiable.

**What to check:**
- Are specific statistics present? (percentages, prices, dates, counts)
- Are claims sourced? (even informal attribution: "according to DHA guidelines")
- Are statistics recent? (not "in 2019...")
- Are UAE-specific numbers used vs. generic global statistics?
- No made-up or unverifiable statistics

**Scoring:**
| Condition | Points |
|---|---|
| 3+ UAE-specific, recent, attributed statistics | 10 |
| 2 statistics or 1 well-cited stat | 6–9 |
| 1 vague or unattributed statistic | 3–5 |
| No statistics or only global/generic numbers | 0–2 |

---

## 6. Schema / Structured Data Mentions (6 pts)

**What it is:** Content that signals schema-readiness (through its structure, not
necessarily implemented code) gets better AI parsing. This parameter evaluates
whether the content's architecture maps to schema types.

**What to check:**
- FAQ structure present → FAQ schema-ready
- Numbered steps → HowTo schema-ready
- Author + date → Article schema-ready
- Plan comparisons with prices → FinancialProduct schema-ready
- Reviews / ratings → Review schema-ready
- Breadcrumb logic in content flow

**Scoring:**
| Condition | Points |
|---|---|
| Content maps to 3+ schema types; author, date, and structured sections present | 6 |
| 2 schema types signaled | 4–5 |
| 1 schema type | 2–3 |
| No schema-friendly structure | 0–1 |

---

## 7. Content Depth & Original Angle (8 pts)

**What it is:** AI engines prefer comprehensive, differentiated sources. This parameter
covers two related risks: content too shallow to fully answer the query, and content
that's long enough but says nothing a ranking competitor page doesn't already say.
**Depth is about density, not raw word count** — a tight 1,200-word page with genuine
detail should score higher than a padded 2,000-word page that restates the same point.

**What to check (Depth & Density — up to 4 pts):**
- All major sub-topics covered (no obvious gaps an AI would need to fill from elsewhere)
- Real case studies, examples, or scenarios — not just abstract definitions
- Technical terms defined in context; multiple user intent angles covered
- Word count is a floor to check (1,500+ words for GEO-focused guides/blogs), not the
  scoring target itself — a dense 1,200-word page can outscore a padded 2,000-word one

**What to check (Original Angle — up to 4 pts):**
- Does the content include at least one fact, data point, named example, or firsthand
  detail that isn't standard/generic coverage already on ranking competitor pages?
- **The clearest fail signal:** could this draft be published on a competitor's site with
  a find-and-replace of the brand name? If yes, it has no original angle regardless of length.
- Is there a point of view, not just a restatement of consensus information?

**Scoring:**
| Condition | Points |
|---|---|
| 1,500+ words (or dense equivalent), comprehensive sub-topic coverage, examples, multiple intent angles, AND a clear original angle vs. generic competitor coverage | 7–8 |
| Strong on depth OR original angle, weaker on the other | 5–6 |
| 1,000–1,499 words, mostly comprehensive, but reads as generic/interchangeable with competitors | 2–4 |
| Under 500 words, or comprehensive word count but shallow and could be find-replaced onto any competitor site | 0–1 |

---

## 8. Semantic Heading Use (6 pts)

**What it is:** AI engines use headings as a content map. Headings that contain
question phrases, entity names, and semantic keywords (not just generic labels)
are more likely to be used as citation anchors.

**What to check:**
- Do H2s contain meaningful keywords or question phrases?
- Do headings progress logically (tell a story from general → specific)?
- Are headings informative enough to stand alone as a content summary?
- **The generic-heading test:** would this heading, unchanged, fit equally well on an
  article about a completely different topic? If yes, flag it — regardless of which
  specific phrase is used. This is a test, not just a list, since new templated
  headings show up that won't be in any fixed list.
- No heading-as-clickbait ("You Won't Believe What Health Insurance Costs in UAE")

**Good semantic headings:**
✅ "How Much Does Health Insurance Cost in Dubai? (2025 Prices)"
✅ "What Does UAE Health Insurance Cover by Law?"
✅ "Health Insurance for Expats in Abu Dhabi: What You Need to Know"
✅ "What's the Minimum Salary for a Personal Loan in UAE?"
✅ "How Does Your AECB Credit Score Affect Loan Approval?"

**Generic headings to flag** (fails the test above — not exhaustive, apply the test to
anything not listed):
❌ Introduction / Overview
❌ Conclusion / Summary / In Summary / Final Thoughts / Wrapping Up
❌ More Details / More Information
❌ FAQ Section (redundant phrasing — a bare "FAQs" label is fine, it's a real block, not a vanity heading)
❌ Why Buy From Us / Why Choose Us / Why Choose [Brand]
❌ Benefits / Key Features (bare, with no topic attached)
❌ How It Works (bare, with no topic attached)
❌ Get Started

Note the distinction: "What You Need to Know" is fine when it's attached to a specific
topic (see the good example above) — it's only generic when it's the *entire* heading
with nothing topic-specific in it.

**Scoring:**
| Condition | Points |
|---|---|
| All headings semantic, keyword-rich, informative standalone | 6 |
| Most headings good, 1–2 generic | 4–5 |
| Mixed — half semantic, half generic | 2–3 |
| Generic or vanity headings throughout | 0–1 |

---

## 9. Brand / Source Credibility Signals (3 pts)

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
| Brand named + licensed aggregator identified + trust signal + author | 3 |
| 2–3 of the above | 2 |
| Only brand name present | 1 |
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
