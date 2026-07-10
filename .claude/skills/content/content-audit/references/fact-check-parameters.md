# Fact-Check Parameters — Scoring Reference

Full definitions and rubrics for the 6 Fact-Check parameters used in `/content-audit`.

This lens verifies factual claims against live sources using `web_search` — it does not
rely on memory alone. For YMYL insurance content, an inaccurate premium figure, an
outdated regulation, or a misattributed statistic is a higher-severity failure than a
weak heading or a missing meta description, because it can mislead a reader on a
health or financial decision.

---

## Background: Why Fact-Check Matters

- Policybazaar UAE content cites regulator rules (DHA, MOHAP, DOH), premium ranges,
  coverage minimums, and named providers (Daman, AXA, Oman Insurance/Sukoon, MetLife,
  etc.) — all of which change over time and are easy to get subtly wrong or copy stale.
- Travel insurance content cites visa coverage requirements (Schengen and other
  destinations), premium ranges, coverage limits, and named insurers' travel plans —
  same staleness risk, plus visa rules that change at the destination's end.
- AI Overviews and chat assistants increasingly surface numbers and claims verbatim;
  a wrong figure that gets cited upstream compounds the damage.
- Google's Helpful Content and YMYL scrutiny treats factual accuracy as a trust signal,
  not just a nice-to-have — see `references/ymyl-helpful-content.md`.
- This lens overlaps with YMYL Lens 4 ("Medical / Financial Accuracy") but goes further:
  YMYL judges accuracy *in principle* from domain knowledge; Fact-Check actively
  searches to confirm or contradict specific claims with current sources.

---

## How to Verify (process, not a parameter)

Before scoring, extract every checkable factual claim from the content: numbers (AED
prices, percentages, coverage limits, age limits, deadlines), named entities (regulator
names, insurer names, plan names, hospital networks), cited statistics or studies, and
any general (non-insurance) facts stated in passing.

For each claim:
1. Run a `web_search` with a short, targeted query (e.g. `"DHA minimum health insurance coverage AED 2026"` or `"Daman Thiqa network hospitals"` for health content; `"Schengen visa travel insurance minimum coverage 2026"` or `"Sukoon travel insurance plans UAE"` for travel content).
2. Compare the claim against what the search returns.
3. Assign one status:

| Status | Meaning |
|---|---|
| ✅ **Confirmed** | Current sources support the claim as stated |
| ❌ **Contradicted** | Current sources show the claim is wrong or outdated |
| ⚠️ **Outdated** | Was true at some point but rules/prices/figures have since changed |
| ⚠️ **Unverifiable** | No reliable source found either way — flag for human review, don't assume false |

Do not penalize **Unverifiable** claims as heavily as **Contradicted** ones — absence of
search coverage isn't proof of falsehood. Never fabricate a source or confirmation;
if search access is unavailable, say so explicitly in the report and score this lens
based on internal-consistency checks only, noting the limitation at the top of the lens.

**Supply the correct value, tiered by source.** For every claim marked Contradicted or
Outdated, the report must state the verified current value with source name and date —
a fact-check that says "wrong" without the right figure is half-done. Label each
correct value with a source tier:

| Tier | Meaning |
|---|---|
| **Primary** | Read directly from the regulator's/provider's own page |
| **Secondary — verify internally** | A named third party (broker, news, industry guide) |
| **Snippet-only — must verify internally** | Search-summary layer; no named page was actually read |

**Disambiguate regulatory vs. platform figures before assigning Contradicted:** decide
what the page is actually claiming — a regulatory/mandated figure (verify against the
regulator's or scheme's own source) vs. the brand's own platform figure (e.g. "plans
from AED X on Policybazaar.ae" — external search cannot contradict internal platform
data; mark it ⚠️ Unverifiable-external and recommend attribution + as-of date instead).
If the page doesn't say which it means, flag the ambiguity itself as the issue.

Follow standard citation/copyright rules when referencing what a search found: paraphrase,
don't reproduce search-result text verbatim, and don't quote more than short fragments.

---

## 1. Numerical Accuracy (25 pts)

**What it is:** Prices, percentages, coverage limits, age bands, and deadlines are the
most consequential and most perishable facts in insurance content.

**What to check:**
- AED premium ranges, deductibles, co-pay percentages
- Minimum coverage amounts mandated by law (e.g. emergency care minimums)
- Age eligibility bands, waiting periods, claim deadlines
- Any number presented as current ("as of 2026", "this year") — verify it's actually current

**Scoring:**
| Condition | Points |
|---|---|
| All numerical claims confirmed current via search | 25 |
| 1 minor numerical claim outdated/unverifiable, rest confirmed | 18–24 |
| 2–3 numerical claims contradicted or outdated | 8–17 |
| Numbers are systematically wrong, outdated, or unverifiable | 0–7 |

---

## 2. Regulatory Claims Accuracy (25 pts)

**What it is:** Claims about what a regulator or authority requires. Which authority
applies depends on the vertical — check `references/policybazaar-context.md` before scoring.

**What to check — Health (DHA/MOHAP/DOH):**
- Is the named regulator correct for the emirate in question? (DHA = Dubai, DOH = Abu Dhabi, MOHAP = federal/other emirates)
- Are mandate descriptions accurate ("mandatory for all residents", "employer-provided", etc.)?
- Are renewal/visa-linked insurance rules described correctly and currently?
- Any reference to a superseded body (e.g. HAAD, which became DOH)?

**What to check — Travel (visa/destination authorities):**
- Is a coverage requirement correctly attributed? (a visa-mandated minimum comes from
  the destination's consulate/embassy rules; a plan feature comes from the insurer's
  policy wording — the two are not interchangeable)
- Are visa insurance requirements (e.g. Schengen minimums, territorial validity,
  covered-country lists) described correctly and currently?
- Are UAE-side requirements (if claimed, e.g. for inbound visitors) attributed to the
  right authority and verifiable?

**Scoring:**
| Condition | Points |
|---|---|
| All regulatory claims confirmed against current rules | 25 |
| 1 minor regulatory claim outdated/unverifiable | 18–24 |
| A regulator is misnamed or a rule is materially wrong | 8–17 |
| Multiple contradicted regulatory claims, or confidently wrong on a mandate | 0–7 |

---

## 3. Provider / Plan Name Accuracy (15 pts)

**What it is:** Named entities must exist and be described correctly — easy to mis-cite
or use post-rebrand. Which entities dominate depends on the vertical.

**What to check — Health:**
- Do named insurers currently operate in the UAE under that name? (e.g. Oman Insurance rebranded to Sukoon)
- Are plan names spelled and attributed to the correct insurer?
- Are claimed network hospitals/clinics actually in that insurer's network?

**What to check — Travel:**
- Do named insurers currently offer the described travel product? (discontinued or
  renamed plans still being referenced is a common failure)
- Are travel plan names/tiers spelled and attributed to the correct insurer?
- Are claimed coverage limits, benefits, or assistance services attributed to the
  right named plan?

**Scoring:**
| Condition | Points |
|---|---|
| All provider/plan names confirmed accurate and current | 15 |
| 1 stale name (pre-rebrand or discontinued product) or minor mismatch | 10–14 |
| A named provider or plan doesn't match search results | 5–9 |
| Multiple incorrect or fabricated-sounding provider/plan references | 0–4 |

---

## 4. Statistical & Study Citation Accuracy (15 pts)

**What it is:** Any cited statistic, survey, or study should match its claimed source
and figure — not just exist in general.

**What to check:**
- Does the cited figure match what the named source actually reports?
- Is the source itself real and findable?
- Is the statistic current, or quietly stale (a 2019 figure presented as current)?
- Are GEO-lens statistics (see `references/geo-parameters.md` Parameter 5) cross-checked here for accuracy, not just presence?

**Scoring:**
| Condition | Points |
|---|---|
| All cited statistics confirmed accurate to source | 15 |
| 1 statistic unverifiable but plausible, rest confirmed | 10–14 |
| A statistic doesn't match its claimed source, or source not found | 5–9 |
| Statistics appear fabricated or systematically unverifiable | 0–4 |

---

## 5. Outdated Information Risk (10 pts)

**What it is:** Even confirmed-at-the-time content can decay. This parameter flags
claims that are structurally at risk of going stale (laws, prices, eligibility rules)
even where a search didn't directly contradict them.

**What to check:**
- Are time-sensitive claims dated or qualified ("as of [year]") so future readers can judge freshness?
- Does the content rely on rules/prices that change annually (premiums, coverage minimums) without a visible "last reviewed" signal?
- Any claim search results suggest is "in transition" (e.g. a regulation under proposed change)?

**Scoring:**
| Condition | Points |
|---|---|
| Time-sensitive claims are dated/qualified; no decay risk flagged by search | 10 |
| Minor decay risk on 1 claim, undated but currently still accurate | 6–9 |
| Several undated time-sensitive claims with real risk of going stale | 3–5 |
| Content presents change-prone facts as permanent/undated throughout | 0–2 |

---

## 6. General Factual Claims (10 pts)

**What it is:** Non-insurance facts mentioned in passing (geography, health/medical
background facts, historical claims) still need to be correct — errors here undermine
overall credibility even if the insurance-specific facts are fine.

**What to check:**
- Any general claim that's simply wrong (e.g. misstated population figures, incorrect medical background used to motivate the insurance topic)
- Claims presented as universal/timeless that are actually time-bound or region-specific

**Scoring:**
| Condition | Points |
|---|---|
| No general factual claims, or all confirmed accurate | 10 |
| 1 minor general inaccuracy, low impact | 6–9 |
| A general claim is wrong and materially affects the argument | 3–5 |
| Multiple general factual errors | 0–2 |
