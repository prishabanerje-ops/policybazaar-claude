# AI Detection Parameters — Scoring Reference

Full definitions for the 9 AI detection signals used in `/content-audit`.

Grounded in: Wu et al. 2025, Mitchell et al. 2023, Kujur 2025, AAAI 2025 shared task,
Wikipedia:Signs of AI writing, and the Copyleaks/GPTZero methodology literature.

This lens does NOT judge AI use as inherently bad. It flags signals that:
1. Reduce reader trust and credibility
2. Lower GEO citation probability (AI engines deprioritize AI-sounding sources)
3. Dilute the Policybazaar UAE brand voice

---

## Detector Reliability — Read Before Scoring

Two findings from internal testing and published research should shape how this lens's
output gets reported, not just what it measures:

**1. No single detector score is a verdict.** Two live, unedited Policybazaar/Paisabazaar
articles run through commercial detectors (ZeroGPT, QuillBot, HumanizeAI.pro, GPTZero,
Grammarly) — 8 detector runs total — scored the *same text* anywhere from 0% to 54% "AI."
Independent published benchmarks confirm this isn't a fluke: detector accuracy ranges
55–97% depending on text type (Weber-Wulff et al.), false-positive rates vary by up to
3,800× between tools (~0.01% to 38% on the same benchmark set), and Turnitin discloses its
own margin of error as ±15 points — meaning a "50% AI" score could genuinely mean anywhere
from 35% to 65%. This lens's linguistic-signal scoring is one more methodology in that
same category. Report it the same way: a score plus the specific patterns that drove it,
never a flat claim that content "is AI-written" or "is human."

**Why the scores diverge:** most detectors measure perplexity (word predictability) and
burstiness (sentence-length variation), not "AI-ness" directly. Concise, fact-dense human
writing — the kind insurance copy should be — can score like AI on these metrics, while
lightly-edited AI text can score like a human. A fact like "the minimum age for this plan
is 18" only has one correct way to say it; humans and AI converge on similar phrasing
because the fact is fixed, not because one copied the other. Watch for this especially on
short, numeric-heavy UAE insurance content (eligibility bands, coverage limits).

**2. AI-sounding ≠ ranking risk.** Google's own guidance is that it penalizes low-quality,
thin, or manipulative content — regardless of who or what produced it — not AI assistance
itself. In practice, AI content is roughly half of new web publishing volume but only ~14%
of top-ranking Google results and ~18% of AI-chatbot citations; a real penalty case
(a publisher auto-posting 500 AI articles overnight, 80% traffic drop in 2 weeks) traced to
*scale without review*, not AI use. What actually predicts ranking success is original
data/experience, visible author credentials, specific rather than generic answers, and
information density — not the AI/human split. That means this lens should stay scoped to
*linguistic register* (does the prose read machine-generated); genericness and thinness are
scored on their own merits by SEO Parameter 9 (Duplicate/Thin Content Risk) and GEO
Parameter 7 (Content Depth & Original Angle) — don't let a clean Human-Likeness score
here imply the content is safe from that separate risk, or vice versa.

---

**Scoring scale per signal:**
- 0 = No signal (human-consistent)
- 1 = Weak signal (possible AI, could be human)
- 2 = Moderate signal (likely AI pattern)
- 3 = Strong signal (near-certain AI pattern)

**Double-counting policy:** A single phrase can fire at most two distinct signals
when genuinely diagnostic for both.

**Total raw score: 0–27. Convert to Human-Likeness score: ((27 - raw) / 27) × 100**

---

## Signal A: Perplexity (Word Predictability)

AI picks the statistically safest word. Human writers pick the most precise or
interesting word given their specific context.

**Flags:**
- Generic verbs where domain-specific ones belong ("address" instead of "untangle"; "provides" instead of "covers" for insurance)
- Adjectives that describe without adding information ("significant improvements", "notable progress", "key challenges")
- Hedged assertions swapping specificity for safety ("can often lead to", "may result in")
- Canonical AI vocabulary — flag any instance. **This is the single canonical vocabulary
  list for this skill** (there used to be a second, out-of-sync list at the bottom of
  this file — it's been merged in here and removed, so nothing should fall through again):

**Generic AI filler (both verticals):**
```
delve, leverage (verb), utilize, robust, comprehensive, streamline, foster, facilitate,
pivotal, nuanced, notable, notably, enduring, garner, multifaceted, vibrant, tapestry,
testament (figurative), interplay, intricate, showcase, highlight/highlighted (standalone),
underscore (standalone), unlock, explore, customised, simply, in the realm of,
the landscape of / landscape (abstract), a myriad of, a plethora of, overall, absolutely,
typically (overused), various (as filler)
```

**Insurance-specific AI vocabulary to flag (Policybazaar):**
```
holistic coverage, tailor-made solutions, tailor-made, seamless claims process,
seamless experience, empowering individuals, empowering you to, ensuring peace of mind,
peace of mind, comprehensive protection, comprehensive protection plan,
financial protection, ensuring your well-being, navigate the complexities,
in today's dynamic market, the ever-evolving insurance landscape, a wide range of options,
a plethora of plans, diverse needs, personalized approach, your unique needs
```

**Travel-specific AI vocabulary to flag:**
```
stress-free journey, hassle-free travel, seamless travel experience, wanderlust,
your dream vacation, dream destination, hidden gems, embark on your journey,
embark on an adventure, ultimate travel companion, explore with confidence,
travel with peace of mind, unforeseen circumstances, whether you're a frequent
flyer or an occasional traveler, from bustling cities to serene beaches,
a world of possibilities, your perfect getaway
```

**Hedge-phrase clusters (both verticals — see also Signal C for the reasoning-level flag):**
```
it is important to note, it is worth noting, it is worth mentioning, it's worth noting,
in many cases, generally speaking, it can be argued, various factors, multiple considerations
```

**Cite the exact word or phrase that fired.**

---

## Signal B: Burstiness Deficit (Sentence Uniformity)

AI produces sentences of uniform length (~15–20 words). Human writing alternates
between short punchy sentences and longer compound thoughts.

**Flags:**
- Three or more consecutive sentences within 5 words of the same length
- No sentence shorter than 8 words in any 150-word block
- Metronomic rhythm — reading aloud produces a steady pulse rather than natural variation
- No fragments used for emphasis at all

**How to report:** List the sentence lengths in sequence e.g. "14, 16, 13, 15, 17 —
five consecutive sentences within 4 words of each other."

---

## Signal C: Hedge Density

AI over-hedges to avoid being wrong. Human writers are direct when they know something.

**Flags:**
- "often", "generally", "typically", "in many cases", "it can be argued" where direct assertion is warranted
- "it is important to note that", "it is worth mentioning", "one might consider"
- Diplomatic framing of obvious tradeoffs: "while X has benefits, it also presents challenges"
- Uncertainty expressed as institutional hedging ("results may vary") vs. human uncertainty ("I'm not sure this holds when...")

**Report:** Quote each hedge and note whether warranted by genuine uncertainty or reflexive softening.

**Legitimate hedging note:** Some hedging is legally required — in insurance copy
(e.g., "subject to policy terms and conditions") and in lending copy (e.g., "rates
subject to bank approval and eligibility criteria"). Do not flag legally-mandated
disclaimers. Flag hedging that obscures facts the writer clearly knows.

---

## Signal D: Structural Tells

AI imposes document architecture regardless of content needs.

**Flags:**
- Bullet list where prose would serve better
- Topic sentence + evidence + restatement of topic sentence (humans skip the restatement)
- "In conclusion / To summarize / In summary" openers on closing paragraphs
- "In this article / guide, I will..." openers
- Numbered steps for content that isn't genuinely sequential
- Three-part micro-structure imposed on every paragraph (intro → body → conclusion)
- **Tricolon parallel structure:** three identical grammatical examples in a row. Real writers use two or vary the shape. Severity: strong.
- **Perfect paragraph-per-idea arc:** every paragraph does exactly one job and lands cleanly. Real writing has a paragraph that meanders, does two jobs, or doesn't resolve. Severity: moderate.
- **Strawman pivot:** "It's not about X, it's about Y" — leading with what something is NOT. Real writers lead with the actual point. Severity: moderate.
- **Trailing benefit-participle:** a clause tacked onto the end of a sentence — "...,
  making/helping/allowing [it/you] [ideal for / easier to / able to] X" — that explains
  a benefit or implication as an afterthought instead of stating it directly. Example:
  *"CAGR provides a clearer picture of annual growth, making it ideal for long-term
  planning."* A human writer more often states the benefit directly ("CAGR is better for
  long-term planning") or cuts the tail entirely. Severity: moderate.
- **Generic/templated section headings:** headings like "Why Buy From Us," "Why Choose
  Us," "Benefits," "Key Features," "How It Works," or "Get Started" that would fit
  unchanged on an article about a completely different topic. See GEO Parameter 8
  (`geo-parameters.md`) for the full list and the underlying test — a generic heading is
  as much a "sounds machine-templated" tell here as it is a citation-readiness problem
  there; both signals firing on the same heading is expected, not double-counting.
  Severity: moderate.

---

## Signal E: Specificity Deficit

AI generates claims that are technically true but apply to everyone and name nothing.

**Flags:**
- Abstract claim with no number, name, time reference, or example: "Many people find health insurance confusing..."
- **Passive voice, widened scope:** not just constructions that obscure the actor
  ("it has been found that", "research suggests"), but passive voice more broadly —
  "the policy is designed to cover X" instead of "the policy covers X"; "claims are
  processed within 48 hours" instead of "we process claims within 48 hours." Flag when
  passive constructions appear in more than roughly a third of a paragraph's sentences,
  or whenever a more direct active alternative is clearly available.
  **Exception — don't flag:** regulatory/legal phrasing that's conventionally passive
  ("coverage is provided subject to...", "the policy is governed by UAE law") — that's
  standard legal register, not an AI tell.
- Universalist framing: "expats often find", "families frequently face" (specific to no one)
- Named examples that are suspiciously generic or perfectly illustrative

**Insurance-specific specificity flags (Policybazaar):**
- "Insurance companies in UAE offer various plans" → name them
- "Prices vary depending on factors" → name the factors and give example price ranges
- "Many residents in Dubai have health insurance" → cite a statistic or source

**Travel-specific specificity flags:**
- "Travel insurance covers various situations" → name the covered events and the limits
- "Premiums vary depending on factors" → name the factors (age, destination, trip length,
  coverage tier) and give example premium ranges
- "Many UAE residents travel abroad every year" → cite a statistic or source

**Report:** Quote each unanchored claim.

---

## Signal F: Transition Word Fingerprint

AI uses formulaic connective tissue between paragraphs.

**Strong AI signals (cite each):**
- "Furthermore," as paragraph opener
- "Moreover," as paragraph opener
- "Additionally," as paragraph opener
- "It is clear that"
- "This highlights / underscores / demonstrates the importance of"
- "As previously mentioned"
- "In addition to the above"
- "It goes without saying"
- "Needless to say"

**Moderate signals:**
- "However," more than once per 200 words
- "Therefore," as a mechanical connector (not earned)
- "Turns out" / "it turns out that" as a pivot — AI uses this to fake discovery
- Tutorial-voice transitions: "The standard approach is...", "The common method is..."
- Announcement-colon patterns: "The key thing to know:", "Here's what matters:"
- Pattern announcement: stating a pattern exists before describing it

---

## Signal G: Punctuation Fingerprint

AI overuses em dashes and semicolons as rhetorical tools.

**Flags:**
- Em dashes used as dramatic pivots mid-sentence: "Health insurance — something every expat needs — can be..."
- Semicolons linking clauses that should just be separate sentences
- Colons used mid-sentence to introduce a single element (not a list)
- Multiple em dashes per paragraph

**Note:** Em dashes alone are not diagnostic. Flag only when combined with other signals
or appearing more than twice per 200 words.

---

## Signal H: Voice / Register Collapse

AI-generated content often collapses multiple registers into one unnatural blend,
or adopts an "AI assistant" register (helpful, neutral, slightly formal, never opinionated).

**Flags:**
- Content that reads like a press release when it should read like expert advice
- Perfectly neutral tone on topics where a real expert would have a view
- "Helpful assistant" framing: "This guide will help you understand...", "By reading this, you will..."
- Register mismatch: informal keywords ("best health insurance UAE") but corporate body copy
- No domain-specific voice markers (a real insurance expert would reference specific plans, name common pitfalls, mention regulatory nuances)

**UAE register notes:** Real insurance advisors say things like "the DHA mandate covers
only basic emergency care — you'll be underinsured for specialist visits without a
rider." Generic AI says "health insurance covers various medical expenses." Real lending
advisors say things like "a lower EMI with a longer tenure usually costs more overall —
check the total repayment amount, not just the monthly figure." Generic AI says
"personal loans offer flexible repayment options to suit your needs."

**Fix template — use this exact structure when writing a FIX for this signal:**

`[Specific regulatory/product fact] — [specific, concrete consequence for the reader] without [the missing product/action].`

- Health example: *"The DHA mandate covers only basic emergency care — you'll be
  underinsured for specialist visits without a rider."*
- Travel example: *"Standard cancellation cover pays out only for the listed reasons in
  the policy wording — you'll absorb the full cost of a change-of-mind cancellation
  without cancel-for-any-reason cover."*

This works because it replaces the generic-AI shape (a vague claim, no stakes, nothing
named as missing) with three things a template can't produce without real domain
knowledge: a specific fact, a specific consequence, and a specific gap. When Signal H
fires, build the FIX around this shape rather than a generic "sound more expert" rewrite
— the em dash separates the fact from the stakes, and "without [X]" names the exact
missing piece.

---

## Signal I: Rhetorical Scaffolding (RLHF Artifacts)

The hardest signals — patterns AI learned from skilled human writing during instruction-tuning.
They *sound* good but are formulaic.

**Flags:**
- Aphoristic closer: the final sentence of a section or article is a tight, memorable
  maxim that wraps everything up cleanly. Real writing doesn't always land this cleanly.
- "More like X than Y" comparative framing in a casual register
- Wisdom-dispensing tone: the narrator has seen it all and shares hard-won lessons
- Fake humility: "I'll admit", "to be honest", "frankly" used as rhetorical devices without genuine concession
- Escalating three-beat rhythm: "X. Then Y. Then Z." where each beat is slightly more dramatic
- Pseudo-paradox framing: "The best [X] is actually [Y]" — AI loves this structure
- **Vulnerability performance:** sharing a difficulty or failure that is perfectly framed and neatly resolved
- The content addresses the reader ("you") throughout in a way that feels coached, not personal

---

## Scoring Thresholds

| Total raw score (0–27) | Human-Likeness Score | Pattern-Match Label |
|---|---|---|
| 0–4 | 85–100 | Human-consistent |
| 5–8 | 70–82 | Mostly human-consistent |
| 9–13 | 52–67 | Mixed signals |
| 14–19 | 30–48 | AI-pattern-heavy |
| 20–27 | 0–26 | Strongly AI-pattern-heavy |

**Report the label as a description of the patterns found, not a claim about who or what
wrote the content** — see "Detector Reliability" above. Two real, unedited human-written
UAE finance articles scored anywhere from 0% to 54% "AI" across commercial detectors; this
lens's own scoring carries the same kind of uncertainty.

---

## Fix Guidance — What Actually Moves the Score (and What Doesn't)

When a follow-up asks to "humanize" flagged content, prioritize fixes in this order:

**Works:**
- Add what a template can't know: original data, named examples, firsthand process detail
- Vary sentence rhythm — mix short and long sentences naturally, don't smooth to uniform length
- Cut generic summary/restatement lines — these are exactly what the signals above flag
- Edit for the Policybazaar UAE brand voice, not just grammatical correctness

**Doesn't work (avoid recommending these):**
- Generic "AI humanizer" tools — fool weak detectors, often fail stronger ones, can read worse
- Synonym-swapping — detectors weigh sentence structure, not vocabulary choice; barely moves scores
- Chasing a 0% score — given the margin of error above, this optimizes for noise, not quality

The FIX field for each flagged signal should point toward the "Works" list — a specific
rewrite that adds a fact, name, or detail — not a like-for-like word substitution.

---

## Calibration Notes

- **Short texts (<100 words):** fewer signals available — cap confidence at Medium
- **Insurance / lending / legal copy:** legitimate hedges and formal register exist — don't penalize
  legally required disclaimers or policy/rate-standard language
- **ESL writing:** UAE content may have non-native English patterns that resemble AI
  (uniform sentence length, hedge-heavy). Note if plausible.
- **Iteratively paraphrased text:** if the user says content was rewritten from AI,
  down-weight all signals — paraphrased AI bypasses most detectors
- **Mixed authorship** is the common real-world case: AI draft + human edit.
  Report the AI-edited fraction estimate separately from the label.
