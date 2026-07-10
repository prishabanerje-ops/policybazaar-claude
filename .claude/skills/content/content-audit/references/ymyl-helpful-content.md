# YMYL & Helpful Content Parameters — Scoring Reference

Used in Lens 4 of `/content-audit`. Applies to all Policybazaar UAE **health insurance**
and **travel insurance** content, because both verticals are explicitly YMYL (Your Money
or Your Life) — content that directly impacts a person's financial wellbeing, and for
health (and travel medical cover), physical wellbeing too.

Read `references/policybazaar-context.md` before scoring this lens — several parameters
below branch by which harm category dominates: **medical/insurance** (health pages) or
**financial/visa-compliance** (travel pages). Don't apply medical-consensus checks to a
purely financial travel-coverage page, or skip them on a health-advice page.

**Why this lens matters now:**
- Google's December 2025 Core Update caused ~67% of health-related websites to see
  significant ranking changes — healthcare was the most impacted category
- AI Overviews appear on ~89% of healthcare queries (BrightEdge, late 2025)
- YMYL pages face maximum scrutiny in both traditional ranking and AI citation decisions
- Google's Quality Rater Guidelines (updated September 2025) explicitly expanded YMYL
  to include financial and lending decisions alongside medical content

---

## 1. Medical / Financial Accuracy (20 pts)

**What it is:** YMYL content that contains factual errors, outdated information, or
unverifiable claims can directly harm readers — and Google penalises it hard. Which
facts matter depends on the vertical.

**What to check — Health (medical/insurance):**
- Are medical claims consistent with current scientific/medical consensus?
  (e.g., if the content says Vitamin C "cures" infections vs. "supports immune function")
- Are insurance/regulatory facts accurate? (correct DHA/DOH/MOHAP coverage mandates,
  accurate deductible definitions, correct plan tiers — see brand-context file)
- No absolute claims that aren't supportable:
  - ❌ "Breastfeeding guarantees immunity against all infections"
  - ✅ "Breastfeeding provides antibodies that reduce infection risk in newborns"

**What to check — Travel (financial/visa-compliance):**
- Are visa-mandated coverage requirements accurate and attributed to the right authority?
  (e.g., Schengen minimum medical-cover requirements — verify against current official
  consulate/embassy guidance, never from memory)
- Are coverage limits, claim conditions, and exclusions (trip cancellation, baggage,
  medical emergencies abroad, pre-existing conditions) stated accurately per named plans?
- No absolute claims that aren't supportable:
  - ❌ "Travel insurance guarantees your visa approval"
  - ✅ "Schengen visa applications require proof of qualifying travel medical insurance;
    approval remains at the consulate's discretion"

**Both:** are statistics cited and verifiable? Not invented or outdated (pre-2022 stats
for fast-moving topics)? Are financial figures accurate if quoted?

**Scoring:**
| Condition | Points |
|---|---|
| All medical/financial facts verifiable and current; no absolute unsupported claims | 20 |
| Mostly accurate; 1 minor unverified claim | 14–19 |
| 2–3 inaccuracies or outdated stats | 8–13 |
| Material factual errors or misleading financial/medical claims | 0–7 |

**Evidence format:**
```
FOUND: "[exact claim from content]"
WHY: [what is inaccurate or unverifiable]
FIX: [corrected version with suggested source]
```

---

## 2. No Harmful or Misleading Claims (20 pts)

**What it is:** Content that could lead someone to make a harmful health or financial
decision fails YMYL at the highest level. This goes beyond inaccuracy — it covers
framing, omissions, and implications.

**What to check — Health:**
- No health advice that could delay or replace professional medical care
- No misleading insurance framing (e.g., implying a basic plan covers specialist visits
  when the DHA mandate doesn't require this; "all insurance covers vaccinations" — not
  true for all plans)
- No omission of critical exclusions (waiting periods, pre-existing condition exclusions)
- Medical disclaimer present and prominent — required when content gives health advice,
  not necessarily for purely factual coverage-comparison content

**What to check — Travel:**
- No framing that implies a policy covers scenarios it commonly excludes (pre-existing
  conditions, adventure sports, travel against medical advice, known events)
- No misleading visa framing (e.g., implying any travel policy satisfies Schengen or
  other visa requirements when specific coverage minimums/territorial validity apply)
- No omission of claim conditions (documentation deadlines, non-refundable vs. refundable
  bookings for cancellation cover, per-item baggage limits)
- No burying of policy excess/deductibles while headlining low premiums

**Both:** no fear-based or alarmist language designed to pressure a purchasing decision.

**Scoring:**
| Condition | Points |
|---|---|
| No misleading claims; appropriate scope; disclaimer present where needed | 20 |
| 1 minor framing issue; disclaimer present | 14–19 |
| Missing disclaimer where needed OR 1 meaningful misleading omission | 8–13 |
| Harmful framing, missing disclaimer, or actively misleading claims | 0–7 |

**Evidence format:**
```
FOUND: "[exact line]"
WHY: [why this could mislead or harm]
FIX: [safer, accurate rewrite]
```

---

## 3. Balanced & Complete Coverage (15 pts)

**What it is:** Google's Helpful Content guidance specifically asks: "Does the content
provide a complete or comprehensive description of the topic?" For YMYL, incomplete
coverage is dangerous — a reader who only gets half the picture may make a bad decision.
This parameter is brand-agnostic in structure; only the examples differ.

**What to check:**
- Are obvious counterpoints or caveats acknowledged? (Health: a guide on "boosting
  immunity naturally" should note when supplements are actually needed. Travel: a guide
  on "cheapest travel insurance" should note when minimum cover is inadequate for the
  destination or trip type.)
- Are known exceptions or edge cases addressed? (Health: pre-existing conditions,
  waiting periods. Travel: senior travelers, pre-existing conditions, multi-trip vs.
  single-trip suitability, adventure activities.)
- Is the scope honest? Does the title promise more than the content delivers?
- Does the content avoid cherry-picking only the positive angle?
- Are exclusions, limitations, and policy excess mentioned alongside benefits?

**Scoring:**
| Condition | Points |
|---|---|
| Genuinely balanced; counterpoints and exceptions addressed; scope matches title | 15 |
| Mostly complete; 1 notable omission | 10–14 |
| One-sided or significant gaps in coverage | 5–9 |
| Heavily one-sided, misleading scope, or material omissions | 0–4 |

---

## 4. Disclaimer Present (10 pts)

**What it is:** Google's quality raters check explicitly for disclaimers on YMYL content
that gives advice or recommendations. Which disclaimer applies depends on the vertical
and on whether the content actually gives advice (a pure plan/price listing needs less
than a piece recommending a specific action).

**What to check — Health:** for content touching medical topics (immunity, child
health, vaccinations) or recommending a course of action, is a medical disclaimer
present? ("This content is for informational purposes only and does not constitute
medical advice. Consult a qualified doctor for guidance.")

**What to check — Travel:** for content recommending coverage decisions or stating
visa requirements, is an appropriate disclaimer present? ("Coverage details, premiums,
and visa requirements are indicative and subject to change — verify against the
insurer's policy wording and the destination's official consulate guidance.")

**Both:** is it placed prominently — near the top or at minimum easily findable, not
buried in a site-wide footer? Is it plain English, not legal boilerplate no one reads?

**Scoring:**
| Condition | Points |
|---|---|
| Clear disclaimer present (where the content type requires one), prominently placed | 10 |
| Disclaimer present but buried or generic | 6–9 |
| Disclaimer missing where the content clearly requires one | 0–5 |

**Note:** correct example for a medical/advice context:
✅ *"This blog is for informational purposes only and does not constitute medical advice.
Always consult a qualified paediatrician for guidance specific to your child's health needs."*

Correct example for a travel-coverage/advice context:
✅ *"Premiums, coverage limits, and visa requirements mentioned are indicative and subject
to change. Always verify against the insurer's policy wording and official consulate
guidance before purchasing."*

---

## 5. People-First Intent — Google Helpful Content (20 pts)

**What it is:** Google's Helpful Content system (now integrated into core ranking)
evaluates whether content was created primarily to help people or primarily to rank.
The self-assessment questions from Google's official documentation
(developers.google.com/search/docs/fundamentals/creating-helpful-content) form the basis.
This parameter is brand-agnostic in structure.

**Google's "Who, How, Why" framework — check all three:**

**WHO:** Is it clear who created this content and why they're qualified? Does the content
demonstrate firsthand experience or genuine domain knowledge? Would the target audience
(UAE residents/expats buying health insurance, or UAE-based travelers buying travel
cover) find this directly useful?

**HOW:** Does it feel written for people, or assembled for search engines? Does it
provide original information, analysis, or perspective — or just repackage what's
already on page 1? Does it avoid "SEO content" tells: keyword-stuffed headings, padded
word count, generic definitions that add no insight?

**WHY:** Does the content leave the reader satisfied, or will they need to search again?
Is there a clear, genuine purpose for this article existing on this specific brand's site
(not just any generic insurance or finance site)?

**Scoring:**
| Condition | Points |
|---|---|
| Clear people-first intent; original angle; satisfying coverage; purpose evident | 20 |
| Mostly helpful; 1–2 SEO-assembly tells or minor gaps | 14–19 |
| Mixed intent visible — some genuinely helpful sections, some filler | 8–13 |
| Clearly assembled for search, not readers; no original value; padded | 0–7 |

**UAE-specific check:** does the content have a signal it was written specifically for
UAE residents — or could it be from any English-language site? Look for at least 2–3
UAE-specific signals: for health, climate/DHA/DOH/local-provider references; for travel,
UAE departure context (visa rules for UAE residents, named UAE insurers, local claim
processes) rather than generic global travel advice.

---

## 6. Content Consensus Alignment (15 pts)

**What it is:** YMYL content that contradicts established consensus is actively risky
and gets penalised by Google's systems. Which consensus applies depends on the vertical.

**What to check — Health:** does health advice align with current medical/
paediatric guidance (WHO, MOHAP)? Are any debunked or outdated claims still stated as
fact? Does the content avoid anti-vaccination or alternative-medicine claims that
contradict mainstream consensus? Do coverage descriptions align with actual DHA/DOH/
MOHAP requirements?

**What to check — Travel:** do visa-requirement statements align with current official
consulate/embassy guidance (not outdated thresholds or superseded rules)? Do coverage
descriptions align with how the named insurers' policies actually work? Is travel-health
advice (vaccinations, destination health risks) consistent with mainstream guidance?

**Scoring:**
| Condition | Points |
|---|---|
| Fully aligned with current medical/regulatory or lending consensus | 15 |
| Mostly aligned; 1 minor outdated claim | 10–14 |
| 1–2 claims that contradict or deviate from consensus | 5–9 |
| Multiple consensus violations or active misinformation | 0–4 |

---

## YMYL Quick Reference — Common Failures

| Failure | Health Example | Travel Example | Fix |
|---|---|---|---|
| Missing disclaimer | Health article with no disclaimer | Visa-requirement article with no verify-with-consulate note | Add disclaimer at top of post |
| Absolute claims | "X boosts immunity guaranteed" | "Guaranteed visa approval with this policy" | Add "may help" / "subject to approval" + cite source |
| Missing critical exclusions | Coverage listed without waiting periods | Cancellation cover listed without documentation/deadline conditions | Add the omitted condition explicitly |
| No UAE specificity | Generic global health advice | Generic global travel advice with no UAE-departure context | Add DHA/DOH/named-insurer/UAE-visa specifics |
| Misleading scope | "Insurance covers all your child's health needs" | "This policy covers everything that can go wrong on your trip" | State what's actually covered/true, with limits |
| Outdated guidance | Pre-2020 nutrition/immunity claims | Superseded visa coverage thresholds or old plan names | Update to current guidance |
| People-last content | Exists only to rank, no UAE-specific value | Exists only to rank, no UAE-specific value | Add firsthand context, UAE-specific data, real examples |
