---
name: cover-page-content
description: >
  Audit a Policybazaar UAE /health-insurance/cover/ hub or spoke page draft against the
  approved specialty-cover spec, and return the meta title, meta description, H1, internal
  linking plan, cannibalisation verdict and content flags. Use this whenever the user invokes
  /cover-page-content, or shares a draft, .md file, or pasted copy for any URL under
  /health-insurance/cover/ — the hub itself or any of the 30 spokes (orthopedic, optical, ent,
  dermatology, cardiac, gp, alternative-medicine, ivf, mental-health, paediatric, neurology,
  gastro, diabetes-thyroid, urology, gynaecology, physiotherapy, allergy, dental, emergency,
  cancer, kidney, maternity, respiratory, diagnostics, rheumatology, bariatric, surgery,
  cosmetic-reconstructive, vaccinations, pre-approval). Also trigger when the user asks to
  "check cannibalisation" on a cover page, asks for title/description/H1 for a cover slug, asks
  whether an existing page should redirect into a cover spoke, or says things like "do the same
  analysis" while working through the cover launch. Trigger even when they only paste content and
  a slug with no explicit instruction, because the whole launch runs page by page through this
  same audit.
---

# Cover page content audit

You are auditing one page in a 31-page launch (`/health-insurance/cover/` plus 30 spokes)
that **already has an approved spec**. The single most useful thing you do is read that spec
and re-verify it, rather than inventing metadata. Across the audits done so far, the spec's
title and description were already correct to the character every time; what drafts got wrong
was framing, figures, missing blocks and links.

So the job is less "write me a title" and more "does this draft match what was decided, and
what will break if it ships".

Read `references/audit-rules.md` at the start. It holds the block lists, the seven decisions,
the linking rules, the cannibalisation method and the recurring defects, with pointers into the
four source docs in `docs/`. Those docs win any disagreement with the reference.

Use `scripts/pbcheck.py` for the mechanical checks rather than hand-rolling them:

```bash
python3 scripts/pbcheck.py status /health-insurance/cover/dental/ /health-insurance/basic/
python3 scripts/pbcheck.py page  /health-insurance/articles/dental-insurance-in-uae/
python3 scripts/pbcheck.py peg   367 1102 35990 67941
printf '%s\n' "Candidate title" | python3 scripts/pbcheck.py count
```

## Workflow

### 1. Identify the page and pull its spec row

Get the slug from the draft (it is usually the first line, in bold). Then grep the spec for it:

```bash
grep -n -A22 "cover/dental/" docs/specialty-cover-url-title-h1-spec-2026-08-05.md
```

Record: URL, wave, title with its stated char count, description, H1, primary keyword, demand
tier, schema, and the "existing overlap" line. Also capture the measured `⬤` and proposed `○`
secondary keywords — drafts often carry these verbatim in a `Keywords-` footer, which tells you
whether the writer had the spec.

Then re-verify the counts yourself with `pbcheck.py count`. Report them as confirmed or
differing. The house rule is ≤60 characters **before** the ` | Policybazaar.ae` suffix, and
140–160 for the description. With the suffix a title runs past 60 and the SERP truncates the
brand — that is intended, so note it once so nobody later "fixes" the length by cutting the
geo qualifier instead.

### 2. Check availability and the state of the cluster

```bash
python3 scripts/pbcheck.py status /health-insurance/cover/<slug>/ /health-insurance/cover/ /health-insurance/cover/pre-approval/
```

A 404 on the target slug confirms it is free. The hub and sibling spokes will mostly 404 early
in the launch, which is what blocks three of the four linking rules — say so rather than
recommending links that cannot resolve.

### 3. Settle the disposition of every overlapping page — before writing linking advice

This is the step that changes the most and gets skipped. Pull the overlap rows:

```bash
awk -F',' 'NR==1 || $1=="dental"' docs/specialty-cover-disposition-2026-08-05.csv
```

Then **fetch each overlapping URL and read its title, description and H1** with
`pbcheck.py page`. The CSV assigns topics by keyword seed, and seeds produce homonym false
positives — one is already confirmed (`joint-health-insurance` filed under orthopedic is about
joint policies for couples, not joints). If the topic doesn't match the page, exclude it from the
cluster totals and say the disposition row needs its own ticket. Getting this wrong means
recommending that someone rebuild a working page about a different product.

The disposition label decides your linking advice, so resolve it first:

- `REWRITE IN PLACE` / `KEEP + UPGRADE` — page stays, **safe to link**
- `DIFFERENTIATE` — both live, enforce the split in the draft
- `FOLD` / `CONSOLIDATE` / `REDIRECT` — URL is going away, **never link it**

If the user states a redirect that contradicts the CSV, treat their decision as current but
quantify what it costs using that row's own impressions, CTR and position. A page ranking on
page 1 that converts poorly is usually a title-and-snippet problem, which is fixable in place;
a redirect to a brand-new URL spends a real ranking to solve it. Say which one the numbers
support, then defer to them.

### 4. Measure the draft against the block list

Hub = 14 blocks, spoke = 23. Produce a table of block / required / present-or-not. Do not
paraphrase the block list from memory — read it from the structure doc.

Pay particular attention to the two ⭐ ADD blocks, because drafts skip them almost every time:
the **direct answer** (40–60 words, written first) and, on spokes, the **insurer matrix**. When
the cannibalisation report shows an AIO pattern for this page's keywords — real impressions, good
position, zero clicks — those two blocks are the entire point of the page. Explain that ranking
harder cannot fix an answer being lifted above the results.

### 5. Scan for the hard blockers

Two of the seven decisions block publication, so check them explicitly:

**Undeliverable promises (Decision 1).** Grep the draft for `find a doctor`, `find the right`,
`browse`, `book a`, `near me`, `are the doctors`, `licensed specialists across`. PB has no doctor
database and no booking. On spokes this usually shows up as a "How to Find a [specialty] Doctor"
section that should be a cover-confirmation section, with the "read reviews and compare clinics"
step cut because PB has no review data.

**Unsourced figures (Decision 4).** Run every AED value through `pbcheck.py peg`. If they resolve
to round USD, the table is a converted foreign price list rather than UAE provider data — that has
happened, and false precision like "AED 367" implies rigour that isn't there. Also compare the
same treatment's price across the spec, the Figma table in the briefs, and any sibling draft;
three documents giving three answers has already occurred.

Then check schema against Decision 5: `MedicalWebPage`, `author` and `reviewedBy` are blocked
until a DHA-licensed reviewer is engaged, and `/author/*` soft-404s. Recommend
`Article + BreadcrumbList + FAQPage` until then.

### 6. Build the linking plan

Anchors come from the draft's own sentences — find the sentence containing the target concept and
take the shortest 3–7 word phrase. Where no suitable phrase exists, mark the row "needs copy
edit" and propose wording. Invented anchors are copy the writer never agreed to.

Verify every target with `pbcheck.py status` before recommending it. Group by where in the draft
the link goes, so the writer can work down the page.

### 7. Write the report

Save to `docs/<slug>-title-desc-h1-interlinks-<YYYY-MM-DD>.md` and summarise in chat. Use this
structure:

```markdown
# <Page> — Title, Description, H1 & Internal Links
**Status:** <NEW / live URL> · **Date:** · **Input:** · **⚠️ Already specced** — <spec ref>

## Verification status        <- table: item / method / result. Every claim traceable.
## 1. <the finding that matters most>
## 2. Meta title              <- spec value, recounted, plus alternates with char counts
## 3. Meta description
## 4. H1 (+ structure gaps against the block list)
## 5. Internal linking
## 6. Cannibalisation
## 7. Content flags           <- F1, F2… hard blockers first
```

Lead section 1 with whatever would do the most damage if it shipped, not with the metadata. If
the draft repeats a rejected framing, or every price is unsourced, that belongs above the title
recommendation.

## What makes these audits useful

**Verify, don't assume.** Every number and status in the report should come from a command you
ran. If a fetch fails, say so and stop rather than filling the gap — a confident guess about a
regulator or a price on a YMYL insurance page is worse than an admitted gap. Government domains
(`mohre.gov.ae`, `dha.gov.ae`, `doh.gov.ae`, `icp.gov.ae`) are unreachable from this
environment, so route those verifications to a person and say why.

**Separate the specced from the judged.** When the spec already fixed a value, say you
re-verified it. When you are making a call the spec doesn't cover, say that too. The user needs
to know which recommendations carry the weight of a prior decision.

**Give the reasoning, then defer.** These are the user's decisions. Quantify the cost of the
option you would not pick, then let them choose. Where a question needs data you don't have —
usually GSC for a keyword split — name it as the open input instead of guessing.

**Report the good parts.** Drafts get things right, and saying so tells the writer what to keep.
A FAQ block that lands inside the 40–60 word rule, or a section the structure doc calls the best
in the design, is worth a line.
