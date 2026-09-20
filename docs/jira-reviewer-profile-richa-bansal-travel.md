# Fix Richa Bansal's Reviewer Profile to Reflect Travel Insurance, Not Home Insurance

## Description

Richa Bansal is the assigned `reviewedBy` for Travel Insurance content, confirmed by Aakash. Her live profile page and the shared designation string used in her `reviewedBy` byline across Travel pages both still read "Business Development Manager- Home Insurance." This is Blocker 1 in `docs/jira-byline-eeat-health-travel-ci.md` and is documented in more detail in `docs/byline-eeat-health-travel-2026-07-31.md` (Travel section, line ~181, and the "Suggested fifth ticket" section). This ticket is the content/schema fix for her profile page specifically; the byline rollout ticket depends on it.

Retrieved live 2026-08-03: `https://www.policybazaar.ae/reviewer/richa-bansal/`, 788,564 bytes.

## Current state (retrieved, not inferred)

| Element | Current value |
|---|---|
| URL | `https://www.policybazaar.ae/reviewer/richa-bansal/` — live, HTTP 200 |
| H1 | Richa Bansal |
| Designation (H3) | "Business Development Manager- Home Insurance" |
| Photo | 1 headshot (`richa-bansal.jpg`) |
| Social | 1 LinkedIn link only: `https://www.linkedin.com/in/richa-bansal-15a134205/` (could not fetch — blocked, HTTP 999) |
| Bio ("About Me") | 1 paragraph, ~57 words, entirely about home insurance: "Richa Bansal brings over 15 years of extensive experience in the insurance sector, with a strong focus on product operations and management. At Policybazaar.ae, she spearheads the home insurance, leveraging her industry expertise to deliver customer-centric solutions. Her strategic insight and in-depth market knowledge help us to deliver customised home insurance solutions to the UAE residents that safeguard their most valuable asset." |
| Schema | No `Person` markup. Page only carries a generic `Organization` + `BreadcrumbList` node. |
| Breadcrumb bug | Her breadcrumb `ListItem` resolves to `https://www.policybazaar.ae/reviewer` (the hub), not her own URL. |
| `<title>` / meta description | Generic, shared with the reviewer hub: "Policybazaar.ae Reviewers \| Meet Our Insurance Experts" / "Meet the expert reviewers at Policybazaar.ae who verify and review insurance and investment content to ensure accuracy, transparency, and reliability." Not personalized. |
| Content list | None. No list of pages she has reviewed. |
| Sitemap | Not present in `sitemap.xml` or any child sitemap (per `docs/byline-eeat-health-travel-2026-07-31.md`). |

## Confirmed sitewide propagation

The stale designation is not limited to her profile page. Checked `reviewedBy` on 3 live Travel pages (2026-08-03):

| Page | `reviewedBy.jobTitle` |
|---|---|
| `/travel-insurance/` (hub) | "Business Development Manager- Home Insurance" |
| `/schengen-travel-insurance-tic/` | "Business Development Manager- Home Insurance" |
| `/travel-insurance/articles/10-best-travel-insurance-companies-in-uae/` | "Business Development Manager- Home Insurance" |

All three pull the same string from a shared source. Fixing it once (wherever the reviewer-designation field is stored) should propagate to all three automatically. Fixing only the profile page content leaves the byline on these pages showing the wrong vertical.

## Related, pre-existing technical note (not new — from `docs/byline-eeat-health-travel-2026-07-31.md`)

- `/author/richa-bansal/` (a different URL namespace) soft-404s — confirmed there as byte-equivalent to a fake-slug control test. Her real, live profile is under `/reviewer/`, not `/author/`.
- **Open item for dev:** confirm whether the byline component's bio popup (`author-reviewer-popup`) links to `/author/richa-bansal/` (broken) or `/reviewer/richa-bansal/` (live, the page this ticket fixes). If it links to the former, fixing this page doesn't fix what users see on click-through.

## Reference: NerdWallet author page structure

Retrieved live (not from memory): `https://www.nerdwallet.com/author/katia-iervasi` (Katia Pinkett, Managing Editor, insurance specialist).

**Person schema:**
```json
{
  "@type": "Person",
  "name": "Katia Pinkett",
  "jobTitle": "Managing Editor",
  "description": "...specialized in insurance. She holds a B.A. in communication... Her work has been featured in The Washington Post, Forbes, Yahoo, Entrepreneur, Best Company and FT Advisor.",
  "sameAs": ["mailto:kiervasi@nerdwallet.com", "https://www.linkedin.com/in/katia-iervasi-923531134/"],
  "alumniOf": {"@type": "EducationalOrganization", "name": "Griffith University"},
  "memberOf": [
    {"@type": "Organization", "name": "Society of American Business Editors and Writers"},
    {"@type": "Organization", "name": "Investigative Reporters and Editors"}
  ],
  "knowsAbout": ["Life insurance, disability insurance, health insurance, personal finance"],
  "publishingPrinciples": "https://www.nerdwallet.com/l/nerdwallet-editorial-guidelines"
}
```

**Visible page, top to bottom:** an editorial-independence / "how we make money" blurb → H1 name → specialty topic tags → social link → past employers + professional memberships → "Articles reviewed by [name]" list with live links, paginated.

## Requirements

**Content (visible page)**
1. Change the visible designation from "Business Development Manager- Home Insurance" to **"Business Development Manager – Travel & Home Insurance"** (revised 2026-08-03, second pass — see note above).
2. Replace the "About Me" paragraph with the Travel & Home bio below — confirmed final, no open items remaining.
3. Add specialty topic tags under the name (mirrors NerdWallet's tag row), e.g. "Travel Insurance," "Home Insurance," "Schengen & Visa Requirements," "Trip Cancellation Cover." She covers both verticals (revised) — include Home Insurance tags, not Travel-only.
4. Add a "Content reviewed by Richa Bansal" module. Confirmed real candidates to seed it: [Travel Insurance hub](https://www.policybazaar.ae/travel-insurance/), [Schengen Travel Insurance](https://www.policybazaar.ae/schengen-travel-insurance-tic/), [10 Best Travel Insurance Companies in UAE](https://www.policybazaar.ae/travel-insurance/articles/10-best-travel-insurance-companies-in-uae/). Should populate dynamically from actual `reviewedBy` assignments, not be hand-maintained, so it doesn't go stale the way the designation string did.
5. Add a short commercial-disclosure line (how Policybazaar UAE is compensated by partner insurers), scaled down from NerdWallet's block. Benefits YMYL Trustworthiness sitewide, not just this page.
6. Fix the breadcrumb `ListItem` to resolve to `/reviewer/richa-bansal/`.
7. Give the page its own `<title>` and meta description instead of the shared generic reviewer-hub one.

**Structured data**
8. Add a `Person` schema node — currently absent entirely. Minimum: `jobTitle`, `description`, `sameAs` (LinkedIn), `knowsAbout: ["Travel Insurance"]`. Matches what `/author/mousree-das/` already has (noted as a gap for both reviewer profiles in the existing ticket).
9. `memberOf` / `alumniOf`: not applicable — confirmed no certifications, education, or professional memberships to list (Aakash, 2026-08-03).

**Upstream (blocks the real fix, not on this page)**
10. Update the shared designation string at its source so it propagates correctly to all Travel `reviewedBy` bylines, not just this profile page.
11. Confirm and, if needed, fix the `author-reviewer-popup` link target (see Related Technical Note above).

## "About Me" — confirmed final (revised 2026-08-03, second pass)

Aakash's first pass (2026-08-03, earlier same day) confirmed: title, "15 years / product operations and management" framing, **Travel as her sole focus (no longer split with Home)**, no certifications/education/achievements to add.

A second revision the same day changed two of those: experience is **17 years** (not 15), and she covers **both Travel and Home Insurance**, not Travel alone — this reverses the "sole focus on Travel" answer above. Flagging explicitly since it changes this ticket's original premise (see note below).

> Richa Bansal brings over 17 years of experience in the insurance sector, with a strong focus on product operations and management. At Policybazaar.ae, she leads travel and home insurance, working with UAE-licensed insurers to shape policies that fit real situations, from a family holiday abroad to protecting a home in Dubai or Abu Dhabi. Her focus is on getting the coverage details, exclusions, and claim conditions right before they reach the plan page, so UAE residents know exactly what they're buying, whether they're insuring a trip or a home.

**Designation to ship: "Business Development Manager – Travel & Home Insurance"** (supersedes "Business Development Manager – Travel Insurance" from the first pass).

**⚠️ Note on this ticket's premise:** This ticket was opened because her page/byline said "Home Insurance" when she was supposed to be Travel-only. With the second-pass answer, she's confirmed to be both — so the fix is no longer a full vertical swap, it's adding Travel alongside the existing Home Insurance framing. Requirement 3 (specialty tags) and Requirement 10 (upstream designation string) below should be read as "Travel & Home," not "Travel only."

## Resolved — former open questions

1. ~~Exact new designation/title~~ → "Business Development Manager – Travel & Home Insurance" (revised from "– Travel Insurance")
2. ~~Does the "15 years" framing still apply~~ → Revised to 17 years
3. ~~Sole focus on Travel, or still split with Home~~ → Revised: **covers both Travel and Home**, not sole-Travel as first confirmed
4. ~~Certifications, education, or professional memberships~~ → None
5. Any notable achievements or media mentions — not asked this round; still open if there are any worth adding.
6. Full, current list of Travel pages she actually reviews, if broader than the 3 confirmed in this doc — still open; the "Content reviewed by" module (Requirement 4) should populate dynamically from actual `reviewedBy` assignments rather than depend on this being enumerated by hand.

## Verification note

Attempted to pull background from her LinkedIn (`linkedin.com/in/richa-bansal-15a134205/`) for additional confirmed detail — request was blocked (HTTP 999, bot detection), returned no usable content. Nothing in this doc is drawn from LinkedIn.
