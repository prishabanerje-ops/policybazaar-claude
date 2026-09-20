# Fix Hardcoded `alt="Salama Insurance"` on Every Insurer Logo in the Travel Plan-Quote Cards

**Type:** Bug · **Component:** Travel Insurance — plan-quote card (`.card-quotes-main`) · **Priority:** High
**Labels:** `seo` `accessibility` `travel-insurance` `content-integrity`

## Description

Every insurer logo rendered inside the travel plan-quote card carries the same hardcoded alt attribute: `alt="Salama Insurance"`. The alt does not describe the logo it sits on. It is identical across all five quote cards, on every travel page tested, regardless of which insurer's logo actually renders.

Salama is a real Policybazaar.ae partner — but in car, health, life, term and business insurance, not travel. There is no Salama travel-insurance URL anywhere in the 3,751-URL sitemap snapshot. The string reads as a default copied in from another vertical's component and never parameterised.

This is a component-level defect, not a content-entry mistake. Editing the five images on the hub page will not fix it.

Reported in the `/travel-insurance/` content audit, 2026-08-11 (`policybazaar-travel-insurance-content-audit-2026-08-11.md`, SEO Lens Parameter 8, scored 3/6). It has been flagged in four consecutive audits — 2026-07-28, 07-29, 08-03, 08-11 — and is unchanged in each.

## Current state (retrieved live 2026-08-11, not inferred)

Every `<img>` carrying `class="img-logo"` on the travel pages tested has an identical alt attribute. Across four pages and 20 images, there are **zero** correct instances:

| Page | `.img-logo` images | Carrying `alt="Salama Insurance"` |
|---|---|---|
| `/travel-insurance/` | 5 | 5 |
| `/schengen-travel-insurance-tic/` | 5 | 5 |
| `/travel-insurance/single-trip-travel-insurance/` | 5 | 5 |
| `/travel-insurance/senior-citizen-travel-insurance/` | 5 | 5 |

All four pages render the same five insurer logos, in the same order, from the same CDN paths.

### The five images on `/travel-insurance/` and the insurer each actually shows

| # | Logo file (CDN) | Plan rendered in the card | Insurer actually shown | Current alt | **Recommended alt** |
|---|---|---|---|---|---|
| 1 | `tnc/travel/AZ_Logo_Twitter_080424.png` | Schengen Single Trip — from AED 22 | **Allianz** | `Salama Insurance` | `alt="Allianz"` |
| 2 | `pbuae/images/insurer-logos/watania_takaful.png` | Annual Gold – Travel Visit Assurance — from AED 24 | **Watania Takaful** | `Salama Insurance` | `alt="Watania Takaful"` |
| 3 | `tnc/travel/RAK_INSURANCE_HORIZONTAL_EN_01_1785242339333.png` | Individual Standard (Hajj & Umrah) — from AED 41 | **RAK Insurance** | `Salama Insurance` | `alt="RAK Insurance"` |
| 4 | `common/images/GIG060624.jpg` | Travel Schengen — from AED 47 | **GIG Gulf** (previously AXA) | `Salama Insurance` | `alt="GIG Gulf"` |
| 5 | `tnc/travel/1783592805780-ba679f2e-…_1_1783592853522.png` | Standard Traveler — from AED 184 | **QIC** | `Salama Insurance` | `alt="QIC"` |

Markup as served today (identical on all five, only `src` varies) — note that the correct insurer name is already sitting in the sibling `<span>`:

```html
<div class="fr--left">
  <div class="logo--prod">
    <img class="img-logo" loading="lazy" alt="Salama Insurance"
         src="https://cdn.policybazaar.ae/tnc/travel/AZ_Logo_Twitter_080424.png">
  </div>
  <span class="product-name fw--normal">Allianz</span>
</div>
```

Target markup:

```html
<div class="fr--left">
  <div class="logo--prod">
    <img class="img-logo" loading="lazy" alt="Allianz"
         src="https://cdn.policybazaar.ae/tnc/travel/AZ_Logo_Twitter_080424.png">
  </div>
  <span class="product-name fw--normal">Allianz</span>
</div>
```

### Why the insurer name, and not `alt=""`

Because the insurer name renders as visible text in `.product-name` right beside the logo, a strict WCAG reading would allow marking the logo decorative with `alt=""` — the information is already available to assistive tech, so the alt is technically redundant. That is a defensible option, and it is worth naming so it doesn't get raised late in review as a cheaper fix.

The recommendation is still the insurer name, for two reasons:

1. `alt=""` forfeits the image-search and AI-entity value that motivated the finding. Five insurer logos on a commercial comparison module are informative content, not page furniture.
2. The redundancy cost is small — a screen reader announces the name twice — whereas today's cost is a *contradiction*: "Salama Insurance" immediately followed by "Allianz".

### Name only, not "X Logo"

All five files were opened and inspected on 2026-08-11. Every one is a **wordmark** — the company name is rendered as readable text inside the image:

| File | Text rendered in the image | Dimensions |
|---|---|---|
| `AZ_Logo_Twitter_080424.png` | "Allianz" + bar symbol | 438 × 220 |
| `watania_takaful.png` | "Watania Takaful" (two lines) | 120 × 60 |
| `RAK_INSURANCE_HORIZONTAL_EN_01_…png` | "rakInsurance" + red mark | 15025 × 1756 |
| `GIG060624.jpg` | "GIG GULF" + droplet symbol | 640 × 400 |
| `1783592805780-ba679f2e-…png` | "QIC" | 1024 × 361 |

These are images of text, so the alt should be **the text in the image** — `Allianz`, not `Allianz Logo`. "Logo" is not in the image; it describes the element type, which belongs to the same category as "image of" or "photo of" and is already announced by assistive tech. `alt="Allianz Logo"` reads as "Allianz Logo, graphic".

Two practical points reinforce it:

- Binding to `.product-name` yields the bare name for free. Appending "Logo" needs string concatenation, introduces a second value to maintain, and breaks the byte-identical acceptance check below.
- There is no search upside. "allianz logo" is a brand-asset query with no travel-insurance purchase intent.

**The one case where "Logo" would be correct:** a symbol-only mark carrying no text — the Allianz bars on their own, or the GIG droplet on its own. Then the alt describes a graphic rather than transcribing text, and `alt="Allianz logo"` is appropriate. None of the five current files are symbol-only. If a symbol-only variant is ever swapped in, revisit.

Also avoid `alt="Allianz travel insurance"`. It reads as keyword insertion, and it is inaccurate — the image says "Allianz", not "Allianz travel insurance".

### Scope boundary (checked, so the fix isn't scoped wider than it needs to be)

`/health-insurance/` and `/car-insurance/` return **0** `.img-logo` images and **0** instances of the string. Those verticals use a different component. This defect is confined to the travel plan-quote card.

## Why it matters

1. **It names the wrong company on the page's primary commercial module.** The alt text asserts that a competitor-adjacent brand — one Policybazaar does not sell travel cover for — is the provider behind five plans it has nothing to do with. That is a factual misstatement in machine-readable page content, on a YMYL page.
2. **Screen-reader users get a contradiction inside every card.** The card announces "Salama Insurance" from the logo, then "Allianz" from the adjacent `.product-name` span, one immediately after the other — five times, with five different second halves. The information is not blocked (the visible name is exposed correctly), but each card asserts two different providers for the same plan, and a user navigating by image or skimming logos gets the wrong one five times out of five.
3. **Image search and AI extraction learn a false association.** Alt text is a primary signal for image indexing and for LLM extraction of page entities. Five logo files are currently associated with the wrong insurer name sitewide across travel.
4. **It compounds two other confirmed entity errors on the same page** — `"AXA QIC Standard Traveler"` conflating two insurers, and `"Alliance"` for Allianz in FAQ Q8. Together these make the travel hub's insurer data unreliable to any consumer parsing it.

## Root cause (hypothesis for dev to confirm)

The alt value appears to be a literal in the quote-card template rather than a field on the insurer/plan record. Confirming this determines the fix:

- If it is a template literal → bind it to the insurer name the card already renders correctly in `<span class="product-name">`, which sits in the same `.fr--left` parent as the `<img>`. The correct string is already in scope at render time; nothing new needs fetching.
- If it is a per-insurer field that is defaulting → find why the default is `"Salama Insurance"` and why no travel insurer record overrides it.

## Requirements

1. Set each logo's alt to the insurer whose logo is displayed. Target values for the current five: `alt="Allianz"`, `alt="Watania Takaful"`, `alt="RAK Insurance"`, `alt="GIG Gulf"`, `alt="QIC"` (full table above).
2. Bind the alt to the same value that populates `<span class="product-name">` in the same card, so it stays correct when the plan mix changes. Do not hardcode the five names — that reproduces the bug with different content.
3. Use the insurer's current legal or trading name. `GIG Gulf`, not `AXA` (rebrand completed June 2022). If Liva or Sukoon logos enter this carousel later, the same rule applies — `Liva`, not `RSA`; `Sukoon`, not `Oman Insurance`.
4. Use the insurer name alone. Do not append "Logo", and do not append keywords. `alt="Allianz"` is correct; `alt="Allianz Logo"`, `alt="Allianz travel insurance"` and `alt="Allianz travel insurance UAE best travel insurance plans"` are all wrong, in increasing order. See "Name only, not 'X Logo'" above for the reasoning.
5. Apply the fix at the component so it propagates to every page rendering `.card-quotes-main`, not page by page.
6. Remove the `"Salama Insurance"` literal from the travel component entirely once the binding is in place, so it cannot resurface as a fallback.

## Acceptance criteria

- On `/travel-insurance/`, `/schengen-travel-insurance-tic/`, `/travel-insurance/single-trip-travel-insurance/` and `/travel-insurance/senior-citizen-travel-insurance/`, every `.img-logo` alt is byte-identical to the `.product-name` text in its own card.
- `grep -c 'alt="Salama Insurance"'` returns 0 on all four pages.
- Swapping a plan in the quote carousel produces a correct alt for the new insurer without a code change.
- No `.img-logo` renders with a missing alt attribute. `alt=""` is a conscious fallback only (see "Why the insurer name, and not `alt=\"\"`" above) — if it is chosen over the recommendation, it must be applied to all five, not left as an inconsistent mix.

## Related, lower-priority finding on the same page (do not bundle unless convenient)

Decorative icons on `/travel-insurance/` carry non-empty alt text — `alt="next-icon"`, `alt="down-icon"`, `alt="icon-arrow"`, `alt="Prev button"`. These should be `alt=""` so assistive technology skips them. Separate from this ticket because it is an accessibility hygiene item with no factual-accuracy component, but it is in the same template family.

## Open questions

1. Is `alt="Salama Insurance"` a template literal or a defaulting per-insurer field? Determines whether the fix is one line or a data cleanup. (For dev.)
2. Does the same literal appear on travel pages beyond the four tested — country pages, provider `-tipvd` pages, the destination hub? Four pages were checked and all four were affected, so a full-template sweep is likely warranted but has not been run.
3. Was Salama ever a travel-insurance partner whose card this template was built from? Not required to fix the bug, but would explain the origin and flag whether other stale partner references exist in the same component.

## Verification note

All figures above were read from live HTML fetched on 2026-08-11 (`/travel-insurance/`, HTTP 200, 450 KB) and from three additional live travel pages fetched the same day, each HTTP 200. Insurer identification is from `<span class="product-name">` — the card's own visible insurer label, sibling to the `<div class="logo--prod">` wrapping each image — cross-checked against the CDN filename; the two agree on all five. The raw card markup was inspected directly to confirm the span/image relationship rather than inferred from rendered text order. All five logo files were downloaded from the CDN (each HTTP 200) and viewed to confirm they are wordmarks carrying the company name as readable text — this is what settles the "name only vs. X Logo" question above; it was checked, not assumed. The Salama-has-no-travel-URL claim is from `assets/policybazaar-urls.txt` (July 2026 sitemap snapshot, 3,751 URLs) — Salama appears in 27 URLs across car, health, life, term and business, and in none under `/travel-insurance/`. Nothing in this ticket is inferred from a prior audit without re-checking it today.
