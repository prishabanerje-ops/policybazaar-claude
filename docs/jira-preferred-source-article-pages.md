# Add Google "Preferred Source" Button to Article Page Templates

**Type:** Feature · **Component:** Article page templates — `/articles/` and `/news-and-update/`, all verticals, EN + AR · **Priority:** Low
**Labels:** `seo` `geo` `ai-search` `dev`

## Description

Google's Preferred Sources feature (developers.google.com/search/docs/appearance/preferred-sources) lets a user mark a publication as preferred, giving it a "preferred" badge and more visibility in Top Stories and AI Mode/AI Overviews. It's a two-line snippet — no backend work, no RSS feed, no publication ID to register.

Add it to PB.ae's editorial article templates only. Do not add it to quote, checkout, or comparison/hub pages — the preference is domain-wide regardless of where the button sits (see Scope note), so there's no benefit to placing it outside editorial content, and a "prefer this source" prompt makes no sense on a transactional flow.

**Two article URL patterns both qualify, per the July 2026 sitemap snapshot (`policybazaar-urls.txt`):**

| Pattern | Example | Count |
|---|---|---|
| `/{vertical}/articles/...` | `/health-insurance/articles/health-insurance-mandatory-in-all-emirates/` | 1,391 (incl. `ar-ae/` Arabic variants) |
| `/{vertical}/news-and-update/...` | `/health-insurance/news-and-update/...` | 195 |

Combined ~1,586 pages. Both sampled pages use the same byline pattern ("Written By [Author] \| Reviewed By [Reviewer] \| Last updated on [Date]"), suggesting a shared base template — **dev to confirm** whether `/articles/` and `/news-and-update/` render off the same component before scoping this as one change vs. two.

## Blocking prerequisite — RESOLVED (checked live 2026-08-26, signed in)

Checked `https://www.google.com/preferences/source?q=<domain>` for both PB domains:

- **`policybazaar.ae`** — appears in the tool as **"Policybazaar UAE."** Eligible. (Already showing as a checked/added source on the checking account — confirms presence, not a claim about anyone else's Search personalization.)
- **`policybazaarinsurance.ae`** — **"No results."** Not eligible.

Every URL in scope for this ticket (`/articles/`, `/news-and-update/`) is on `www.policybazaar.ae` — the eligible domain. **No longer a blocker; dev work can proceed.**

The tool's own UI also states: *"Note: Sources that are not updated regularly may be unavailable."* This corroborates the Impact caveat below — Google ties continued source-preference eligibility to publishing cadence, not just Top Stories placement.

## What to add (dev spec)

**1. In `<head>`, once per page (or globally, if the head is shared):**

```html
<script async src="https://news.google.com/swg/js/v1/publisher.js"></script>
```

**2. In `<body>`, inside the article template — place in the byline/date block, next to the "Last updated on" line:**

```html
<div google-add-preferred-source-btn></div>
```

No publication ID or site-URL parameter to fill in — Google auto-detects the domain from where the script loads.

No `integrity` (SRI) attribute on the script tag — Google doesn't publish a hash for this file, and it's an auto-updating library (unversioned URL), so a pinned hash would break the button the next time Google ships an update. Not an oversight.

**Optional attributes on the `<div>`** (not required for launch):
- `data-theme="dark"` — defaults to light
- `data-lang="en"` — defaults to the visitor's browser language; set explicitly per locale if the `ar-ae/` article pages should force `data-lang="ar"` instead of relying on browser detection (confirm with SEO whether that's wanted before adding).

⚠️ Snippet retrieved via automated fetch of Google's live doc, not hand-verified against the rendered page — **dev should confirm the exact tag syntax against developers.google.com/search/docs/appearance/preferred-sources before shipping**, in case the doc has since changed.

## Current state (retrieved live 2026-08-26)

Checked two live pages — one from each URL pattern:
- `/health-insurance/news-and-update/mohap-announces-herpes-zoster-vaccine-for-individuals-over-the-age-of-50-years/` — no button, "Last updated on 25 October 2023."
- `/health-insurance/articles/health-insurance-mandatory-in-all-emirates/` — no button, "Last updated on 29 November 2024."

Neither page has any existing preferred-source markup (`source-preferences`, `google-add-preferred-source-btn`, `publisher.js`, or a follow/prefer button near the byline).

## Scope note

The preference a user sets is domain-level, not per-article or per-section. Placing the button only on article pages is a placement choice — it does not limit which PB content becomes eligible for the boost once a user prefers the domain.

## Requirements

1. Add the `<script>` tag to the shared `<head>` (or the article-template head, if head markup isn't fully global).
2. Add the `<div google-add-preferred-source-btn></div>` to the article template's byline/date block — one template change, not per-page, covering both `/articles/` and `/news-and-update/` if they share a template (confirm first).
3. Do not add to quote, checkout, or comparison hub pages.
4. ~~Confirm domain eligibility~~ — done, see Blocking prerequisite (policybazaar.ae confirmed eligible 2026-08-26).
5. Verify snippet syntax against the live Google doc at implementation time (see ⚠️ above).

## Acceptance criteria

- [x] Domain eligibility confirmed in Google's source-preferences tool before dev work starts — `policybazaar.ae` confirmed eligible 2026-08-26
- [ ] `<script>` tag present in page `<head>` on all `/articles/` and `/news-and-update/` pages
- [ ] Button renders in the byline/date block, every vertical, EN and AR
- [ ] Button does not render on transactional pages
- [ ] No console errors; button behaves per Google's Standard JavaScript integration

## Impact caveat

A spot check of the ~195 `/news-and-update/` articles found "Last updated" stamps from 2023 on the sampled pages; the `/articles/` sample (2024) skewed more recent. Top Stories rewards recency, so actual Top Stories payoff may be limited for the `/news-and-update/` set specifically. Not a blocker for this ticket — sets expectations on impact.

## Verification note

Domain eligibility is confirmed live (2026-08-26, signed-in check — see Blocking prerequisite). Traffic/ranking impact remains unverified — Google's own docs don't claim any, so this stays a low-cost visibility bet, not a confirmed-ROI initiative.
