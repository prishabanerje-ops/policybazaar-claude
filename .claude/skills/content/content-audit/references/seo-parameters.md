# SEO Parameters — Scoring Reference

Full definitions and rubrics for the 12 SEO parameters used in `/content-audit`.
All examples are calibrated to Policybazaar UAE health and travel insurance content —
the mechanics below (title length, heading structure, schema types) apply equally to
both verticals; only the illustrative examples differ.

---

## 1. Title Tag (10 pts)

**What to check:**
- Is a title tag present and visible in the content or page source?
- Length: 50–60 characters (Google truncates beyond ~60)
- Contains the primary keyword naturally (not stuffed)
- Unique — not duplicated across site pages
- Compelling for CTR — conveys value, not just a label

**Scoring:**
| Condition | Points |
|---|---|
| Title present, correct length, keyword included, compelling | 10 |
| Title present, minor issue (slight over/under length) | 7–9 |
| Title present but missing keyword or too generic | 4–6 |
| Title absent, duplicate, or keyword-stuffed | 0–3 |

**Title tag examples:**
- ✅ "Best Health Insurance in UAE 2025 | Compare Plans | Policybazaar UAE" (58 chars)
- ✅ "Travel Insurance UAE 2026 | Compare Plans | Policybazaar" (56 chars)
- ❌ "Health Insurance" (too short, no differentiator)
- ❌ "Health Insurance UAE Health Insurance Plans Compare Health Insurance UAE" (stuffed)

---

## 2. Meta Description (8 pts)

**What to check:**
- Present and 140–160 characters
- Contains primary or secondary keyword
- Includes a value proposition or CTA
- Not duplicate across pages
- Reads naturally for humans — not a keyword list

**Scoring:**
| Condition | Points |
|---|---|
| Present, correct length, keyword + CTA, unique | 8 |
| Present, minor issues | 5–7 |
| Present but too short/long or generic | 3–4 |
| Missing or duplicate | 0–2 |

---

## 3. Heading Hierarchy — H1–H6 (10 pts)

**What to check:**
- Exactly one H1 per page, reflects the main topic
- H2s used for major sections, H3s for subsections — logical hierarchy
- No heading levels skipped (H1 → H3 without H2)
- Headings contain meaningful keywords (not keyword-stuffed)
- No "heading as decoration" (bold text that should be a proper H-tag)

**Scoring:**
| Condition | Points |
|---|---|
| One H1, logical H2–H6 hierarchy, keywords present | 10 |
| Minor hierarchy issue (one skipped level) | 7–9 |
| Multiple H1s, or flat heading structure | 4–6 |
| No headings, or heading chaos | 0–3 |

---

## 4. Keyword Usage & Density (10 pts)

**What to check:**
- Primary keyword appears in: H1, first 100 words, naturally throughout body
- Keyword density: 1–2% (not stuffed, not absent)
- LSI / semantic keywords present (related terms, synonyms)
- No exact-match anchor stuffing
- Keywords in image alt text where relevant

**How to estimate density from pasted text:**
Count keyword occurrences ÷ total word count × 100.

**Scoring:**
| Condition | Points |
|---|---|
| Keyword in H1 + intro + natural distribution, density 1–2%, LSI present | 10 |
| Keyword present but density slightly off or LSI thin | 6–9 |
| Keyword missing from H1 or intro, or over-optimised | 3–5 |
| Keyword absent or stuffed beyond 3% | 0–2 |

**UAE insurance note:** Watch for keyword conflation. "Health insurance UAE" and "medical insurance UAE" are distinct terms — flag if both are being targeted on the same page without differentiation.

---

## 5. Content Depth & Length (10 pts)

**What to check:**
- Word count appropriate to content type:
  - Landing page: 400–800 words
  - Blog / guide: 1,200–2,500 words (aim for 1,500+ for GEO)
  - Comparison page: 800–1,500 words
  - FAQ page: 600–1,200 words
- Topic covered comprehensively — no obvious subtopics left out
- Unique insights vs. generic coverage
- Content matches search intent (informational / commercial / transactional)
- **Density over length:** word count is a floor, not the target. A shorter page dense
  with specifics should score at least as well as a longer one padded with restatement —
  don't reward hitting a word count by adding generic filler.

**Scoring:**
| Condition | Points |
|---|---|
| Appropriate length, comprehensive, unique angles, intent-matched | 10 |
| Correct length but thin on depth or originality | 6–9 |
| Too short for content type, or right length but shallow | 3–5 |
| Under 300 words or clearly padded with no substance | 0–2 |

---

## 6. Readability Score (8 pts)

**What to check:**
- Flesch-Kincaid Grade Level target: 8–10 for UAE English insurance audience
  (English is often a second language; aim for clarity over sophistication)
- Sentence length: average 15–20 words; no sentence longer than 35 words without a break
- Paragraph length: 2–4 sentences max; no walls of text
- Passive voice: under 15% of sentences
- Jargon: defined on first use (e.g., "copay", "deductible", "network hospital")

**Estimate from text:**
- Long sentences (35+ words) = flag each one
- Paragraphs over 5 sentences = flag
- Insurance jargon without explanation = flag

**Scoring:**
| Condition | Points |
|---|---|
| Varied sentence length, short paragraphs, jargon explained, conversational | 8 |
| Mostly readable, minor issues (1–2 long sentences or paragraphs) | 5–7 |
| Dense prose, frequent jargon, long blocks | 3–4 |
| Unreadable walls of text or severe jargon load | 0–2 |

---

## 7. Internal Linking (8 pts)

**What to check:**
- At least 2–3 contextual internal links present (or flagged as missing if text-only)
- Anchor text is descriptive (not "click here" or "read more")
- Links point to relevant related pages (not random)
- No orphan-page risk signals (if URL context is provided)
- **Missed-opportunity check (NEW):** `grep` the URL asset
  (`assets/policybazaar-urls.txt`) for 2–3 keyword fragments drawn from the page's
  own subtopics. If
  a clearly relevant, real existing page turns up that the content does NOT link to,
  flag it as a missed opportunity — don't just score what's present, catch what's absent.
  This parameter only SCORES the gap; the full actionable list (anchor text, placement,
  inbound candidates) goes in the skill's Step 2.6 Interlink Opportunities section.

**Scoring:**
| Condition | Points |
|---|---|
| 3+ contextual internal links, descriptive anchors | 8 |
| 1–2 internal links, mostly good anchors | 5–7 |
| Links present but generic anchors ("click here") | 3–4 |
| No internal links visible in content | 0–2 |

**Note:** If content is provided as raw text without HTML, flag internal links as "cannot verify — check in CMS" and award partial credit if the content has natural linking opportunities identified. The missed-opportunity grep check still applies even here, since it doesn't depend on the content having live HTML links.

---

## 8. Image Alt Text (6 pts)

**What to check:**
- Images (if present) have alt text
- Alt text is descriptive and includes relevant keyword where natural
- Alt text is not stuffed ("health insurance UAE health insurance plans UAE")
- Decorative images use empty alt (`alt=""`)

**If no images in the content:** Award full 6 pts and note "No images detected — alt text not applicable."

**Scoring:**
| Condition | Points |
|---|---|
| All images have descriptive, keyword-relevant alt text | 6 |
| Most images have alt text, minor issues | 4–5 |
| Alt text present but generic or missing on key images | 2–3 |
| No alt text on content images | 0–1 |

---

## 9. Duplicate / Thin Content Risk (10 pts)

**What to check:**
- Content has a unique angle — not just a rephrased version of "what is health insurance"
- No near-duplicate sections within the same piece
- No obvious copy-paste from competitor pages or generic boilerplate
- Thin content signals: generic definitions without examples, no original data, no author perspective
- **The find-and-replace test:** could this draft be published on a competitor's site with
  just the brand name swapped out? If yes, that's the clearest possible signal of thin or
  undifferentiated content — flag it here regardless of word count.

**AI-generated thin content pattern (for UAE insurance):**
Generic structure → "Health insurance covers medical expenses. It is important to have health insurance in UAE. There are many plans available. You should compare plans before buying." → Flag as thin/generic.

**Scoring:**
| Condition | Points |
|---|---|
| Unique angle, original examples/data, no duplicate passages, fails the find-and-replace test (i.e. clearly couldn't be published on a competitor's site as-is) | 10 |
| Mostly unique but 1–2 generic filler sections | 6–9 |
| Heavy reliance on generic content, boilerplate definitions | 3–5 |
| Near-duplicate, scraped, or fully generic content — passes the find-and-replace test | 0–2 |

---

## 10. Structured Data Signals (10 pts)

**URL ONLY — this parameter audits the schema actually implemented on the live page.**
(Content-signal schema-readiness — "does the structure map to schema types" — is scored
by GEO Parameter 6 in both modes; don't double-score it here.)

**What to check:**
- Extract the page's actual JSON-LD (`<script type="application/ld+json">` blocks) from
  the fetched HTML and list every `@type` found (including inside `@graph`)
- Parse check: does each block parse as valid JSON? A block that doesn't parse counts as absent
- Parity check: does the markup match the visible page? (e.g. every FAQPage question
  appears on-page with a matching answer; aggregateRating matches the displayed rating;
  Article author/date match the byline)
- Coverage check: any obvious missing type for this content? (FAQ section with no FAQPage
  markup; author + date with no Article markup; plans with prices but no
  InsuranceProduct/FinancialProduct; page hierarchy with no BreadcrumbList)
- Scope: obvious gaps only — full property-level validation against Google's
  rich-results requirements is `/seo schema`'s job; recommend routing there when
  implemented markup is present but this check raises doubts
- **Page-type expectations (policybazaar.ae health-insurance URLs only):** identify the
  page type and compare the implemented stack against
  `references/schema-expectations-health.md`. Expected-but-missing types,
  present-but-wrong types, any known bug from that file, and any recommendation of a
  blocklisted type (HowTo, SearchAction, etc.) are findings. For non-health URLs, run
  the generic checks above only.

**Scoring:**
| Condition | Points |
|---|---|
| 3+ valid schema types implemented, markup matches visible content, no obvious missing type | 10 |
| Schema implemented but 1 parity gap or 1 obvious missing type | 6–9 |
| Only 1 basic type implemented despite clear opportunities, or markup stale/mismatched with the page | 3–5 |
| No JSON-LD despite clear schema opportunities, or markup that doesn't parse / contradicts the page | 0–2 |

---

## 11. CTA Clarity (5 pts)

**What to check:**
- Is there a clear call to action?
- CTA matches intent: informational content → "Learn more / Compare plans"; transactional → "Get a quote / Buy now"
- CTA is specific ("Compare health insurance plans in UAE") not generic ("Click here")
- CTA placed logically (not buried at the bottom of a 2,000-word guide as the only one)

**Scoring:**
| Condition | Points |
|---|---|
| Clear, specific, intent-matched CTA, well-placed | 5 |
| CTA present but generic or slightly misaligned | 3–4 |
| CTA buried, vague, or missing | 0–2 |

---

## 12. Mobile / UX Red Flags in Copy (5 pts)

**What to check** (from content alone, not code):
- No "as you can see in the table above" references to missing visuals
- No "click the button below" with no button in the content
- Lists are not excessively long (20+ bullet points in a row = mobile UX problem)
- No horizontal scroll risk (no very long unbroken strings or code blocks in prose content)
- Copy doesn't assume desktop-only experience

**Scoring:**
| Condition | Points |
|---|---|
| No UX red flags in copy | 5 |
| 1 minor UX issue | 3–4 |
| 2+ UX issues | 0–2 |
