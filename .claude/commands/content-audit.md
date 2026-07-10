---
description: Five-lens content audit (SEO + GEO + AI-detection + YMYL + fact-check) for Policybazaar UAE health & travel insurance content
argument-hint: <url | pasted text | .md/.docx file>
---

Run the five-lens content audit on: $ARGUMENTS

Read `.claude/skills/content/content-audit/SKILL.md` and follow it exactly — do not
audit from memory of this command file.

- Input above may be a URL (URL MODE) or pasted text / an attached .md or .docx file (FILE MODE) — the skill's Step 0 defines the mode rules.
- If $ARGUMENTS is empty and no file is attached, ask for the content as text, file, or URL before doing anything else.
- Vertical (Health vs Travel insurance, policybazaar.ae only) is auto-detected in the
  skill's Step 1. Other verticals and Paisabazaar are out of scope — the skill will say
  so and stop.
