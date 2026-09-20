# Broken Prev/Next Article Navigation Links Across Multiple Verticals

**Type:** Bug · **Component:** Article prev/next navigation (Health Insurance, Travel Insurance, News & Updates) · **Priority:** Medium
**Labels:** `content-integrity` `broken-link`

## Description

Multiple article pages across at least three sections of the site (`/health-insurance/articles/`, `/travel-insurance/articles/`, `/news-and-update/`) have a "Previous" or "Next" navigation link that resolves to a **404**. In one case the link is an obvious leftover test slug; in the other two, the anchor text and slug look like real articles but the target page no longer exists (deleted/renamed without the prev/next reference being updated). Same class of bug in all four confirmed cases: a stale or placeholder URL in the prev/next field.

## Current state (retrieved live 2026-09-07)

| Page | Broken link | Anchor text | Target URL | Status |
|---|---|---|---|---|
| `/health-insurance/articles/nipah-virus-in-uae/` | Next | "Is the Nipah Virus Outbreak a Concern for UAE Travellers?" | `.../health-insurance/articles/test1/` | **404** — literal test slug |
| `/news-and-update/unemployment-insurance-scheme-2022-uae/` | Next | "Cardless Cash Transaction in the UAE: An Overview" | `.../news-and-update/cardless-cash-transaction-in-the-uae/` | **404** |
| `/news-and-update/holiday-list-uae/` | Previous | "Is Travel Insurance compulsory for travelling Test Page?" | `.../travel-insurance/news-and-update/test-page/` | **404** — literal test slug |
| `/travel-insurance/articles/travel-insurance-for-asia-from-uae/` | Previous | "AIG Travel Insurance Contact Number" | `.../travel-insurance/articles/aig-travel-insurance-contact-number/` | **404** |

Confirmed working on the same four pages (no action needed): Nipah's "Previous" is simply absent; the other side of each of the other three pages' prev/next (unemployment page's "Previous" → Dubai World Cup 2022, holiday-list's "Next" → 4 Summer Travel Insurance Hacks, Asia-travel page's "Next" → Average Cost of Travel Insurance with Cancer) all returned live HTTP 200 with real content.

## Why it matters

- Four confirmed dead outbound links on live, indexed pages across three different site sections — this is a template/data pattern, not a one-off typo.
- Two of the four use an unmistakable test slug (`test1`, `test-page`), indicating placeholder data shipped to production. The other two point to real-looking articles that were likely deleted or renamed without updating the pages that reference them as prev/next — a second, related failure mode (stale reference, not just leftover test data).

## Requirements

1. Fix all four links above to point to a real, live article (or a genuine adjacent article if the current previous/next assignment logic allows a different pick).
2. Sweep prev/next fields across all three sections (`/health-insurance/articles/`, `/travel-insurance/articles/`, `/news-and-update/`) for the same two failure modes: literal test slugs (`test1`, `test-page`, etc.) and stale references to deleted/renamed articles. This has only been spot-checked on four pages — not exhaustive.
3. Determine whether there's a shared cause (e.g., a template that defaults to a test article when no next-in-sequence exists, or no cleanup step when an article is deleted/renamed) so the fix isn't just four manual edits that recur later.

## Acceptance criteria

- All four links above resolve to a real, live (HTTP 200) article with anchor text matching that article's actual title.
- No `/articles/test*` or `/news-and-update/test*` placeholder URLs remain in prev/next navigation anywhere on the site.
- A documented sweep (or automated check) confirms no other prev/next link across the three sections 404s.

## Verification note

All statuses above were confirmed live on 2026-09-07 via direct fetch of each linked URL (HTTP status + content check), not inferred from anchor text or slug naming.
