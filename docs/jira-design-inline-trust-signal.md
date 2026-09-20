# Design the Inline Trust Signal Component

**Type:** Design task
**Vertical:** Health (incl. Critical Illness) and Travel

## Description

Design a small, reusable inline trust signal that sits under the byline on Health and Travel content pages. It carries our regulatory credentials as links to the source certificates, plus a one-line advice caveat.

Copy is final. This is a visual and layout task only.

## Where it goes

Directly beneath the byline block, above the first body heading. Renders on 1,510 pages.

## What it has to hold

Two rows.

**Row 1 — credentials.** Two or three items separated by `·`, each with a linked number. The count varies by vertical, so the layout cannot assume three.

Health, three items, ~140 characters:
> Licensed by the Central Bank of the UAE (**Registration No. 123**) · DHA Health Insurance Intermediary Permit No. **BRK-00041** · Emirates Insurance Federation Membership No. **B81**

Travel, two items, ~105 characters:
> Licensed by the Central Bank of the UAE (**Registration No. 123**) · Emirates Insurance Federation Membership No. **B81**

**Row 2 — advice caveat with a link.**
> Information on this page is for general guidance only — not personalised financial or medical advice. Speak to one of our advisors →

Bold above marks the linked strings. Each opens a PDF or a regulator page in a new tab.

## Requirements

1. Design for 390px mobile and 1440px desktop. The health credential row wraps to roughly three lines at 390px, so decide whether items wrap inline or stack, and where the `·` separators go when they do.
2. Handle both the two-item and three-item variants without a layout break.
3. Mirror for Arabic (RTL). Latin-script numbers stay left-to-right inside the right-to-left line.
4. Give the links a visible affordance. They leave the page, so signal that they open a document.
5. Keep it visually subordinate to the primary quote CTA. This is a reassurance element, not a conversion element.
6. Do not push first body content below the fold on mobile.
7. Link tap targets meet 44×44px on mobile even though they sit inside a text run.
8. Text and any background meet WCAG AA contrast at the chosen size.

## Deliverables

- Figma frames: mobile and desktop, three-item and two-item variants, English and Arabic
- Spacing, type size, weight and colour tokens
- Wrap behaviour at 390px specified, not left to the browser
- Redline or notes handed to dev alongside the content ticket

## Acceptance

- [ ] All four combinations of variant × breakpoint reviewed, plus Arabic
- [ ] Links are identifiable as links without hover
- [ ] Component does not visually compete with the quote CTA on the same viewport
- [ ] Signed off by Compliance that no credential is truncated or abbreviated in any state

## Reference

Copy and markup: `docs/disclaimer-health-2026-07-31.md`, `docs/disclaimer-travel-2026-07-31.md`
Rollout ticket: `docs/jira-disclaimer-licence-links-health-travel.md`
