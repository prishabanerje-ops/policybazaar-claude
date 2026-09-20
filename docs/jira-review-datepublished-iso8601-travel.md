# Convert Review `datePublished` to ISO-8601 in the Travel Review Schema Block

**Type:** Bug · **Component:** Travel Insurance — review schema block (`Organization.review[]`) · **Priority:** High
**Labels:** `seo` `structured-data` `travel-insurance`

## Description

Every `Review` node in the travel review block sets `datePublished` to a plain-English date string instead of ISO-8601. Schema.org requires ISO-8601 (`Date`/`DateTime`) for this property, so the values are not machine-readable and are ignored by consumers.

The same six reviews are stamped on every travel page, so this is one template fix, not a per-page one.

Reported in the `/travel-insurance/` content audit, 2026-08-11 — bug **T3** in `references/schema-expectations-travel.md`, originally logged 2026-07-10 and unchanged since.

## Current state (retrieved live 2026-08-11)

Identical values on `/travel-insurance/`, `/travel-insurance/uae/` and `/travel-insurance/travel-insurance-dubai/`:

| Author | Current `datePublished` | Should be |
|---|---|---|
| Javed Khan | `"12 February 2026"` | `"2026-02-12"` |
| Khaled Mohammad Khan | `"12 February 2026"` | `"2026-02-12"` |
| Abdul | `"12 January 2026"` | `"2026-01-12"` |
| Razia Khatun | `"12 January 2026"` | `"2026-01-12"` |
| Ravish | `"5 June 2025"` | `"2025-06-05"` |
| Nadeem | `"5 June 2025"` | `"2025-06-05"` |

Also confirmed carrying non-ISO review dates: `/schengen-travel-insurance-tic/` (6), `/travel-insurance/single-trip-travel-insurance/` (6), `/travel-insurance/senior-citizen-travel-insurance/` (4). Not an exhaustive sweep — assume every page rendering the review block is affected.

Current markup:

```json
{
  "@type": "Review",
  "name": "Seamless travel insurance",
  "datePublished": "12 February 2026",
  "author": { "@type": "Person", "name": "Javed Khan" }
}
```

Target:

```json
{
  "@type": "Review",
  "name": "Seamless travel insurance",
  "datePublished": "2026-02-12",
  "author": { "@type": "Person", "name": "Javed Khan" }
}
```

**The same page already emits ISO dates correctly elsewhere** — `WebPage.datePublished: "2021-01-07"` and `WebPage.dateModified: "2026-08-04"`. So the formatter exists; the review block just isn't using it.

## Why it matters

1. Review dates are how consumers judge whether social proof is current. Unparseable dates mean recency is discarded — reviews from Feb 2026 and Jun 2025 are treated identically.
2. Schema.org defines `datePublished` as a `Date`/`DateTime`. A plain-English string is invalid, not merely unconventional.
3. `"5 June 2025"` is ambiguous across locales in a way `2025-06-05` is not.

Note: this does **not** affect Google review rich results — those were already unavailable here, because the `AggregateRating` sits on an `Organization` node named after the page topic (bug **T2**, separate ticket needed). The value of this fix is entity understanding and AI-search consumption, not stars in the SERP.

## Requirements

1. Emit `datePublished` as `YYYY-MM-DD` for every `Review` node, using the same date formatter the `WebPage` node already uses.
2. Fix in the shared review-block template so it applies to every page rendering it, not page by page.
3. Convert from the stored source date, not by parsing the display string — the visible on-page date can stay in its current human format.
4. If any review has no reliable stored date, omit `datePublished` rather than emit an invalid or guessed value.

## Acceptance criteria

- Every `Review.datePublished` on the three cluster pages matches `^\d{4}-\d{2}-\d{2}$`.
- No non-ISO `datePublished` remains on any page rendering the review block.
- Visible on-page review dates are unchanged.
- Google Rich Results Test reports no date-format errors on the review block.

## Related (do not bundle)

- **T2** — `AggregateRating` 4.7 / 43,419 stamped on an `Organization` node named after the page topic ("Travel Insurance", "Travel Insurance UAE", "Travel Insurance Dubai"). Needs its own ticket; it is the reason this block earns no rich result.
- **Duplicate review content** — the identical body *"For a quick and easy process to buy travel insurance online, always choose from Policybazaar…"* is published under both **Javed Khan** and **Ravish**. Content issue, tracked in `todo/travel-cluster-2026-08-11/travel-hub-tasks.csv`.

## Verification note

All values above were read from live JSON-LD on three pages fetched 2026-08-11 (each HTTP 200). The additional three pages were checked by pattern match on their live HTML the same day.
