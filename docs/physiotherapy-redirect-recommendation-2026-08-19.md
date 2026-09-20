# Physiotherapy redirect — recommendation

**Question:** should `/health-insurance/health-guide/physiotherapy-treatment/` be redirected to
`/health-insurance/cover/physiotherapy/`?
**Date:** 2026-08-19 · **Short answer:** the numbers say no. Rewrite it in place.

## What the data says

| | |
|---|---|
| Status today | **200, live** (verified) |
| 360-day performance | **11,248 impressions · 60 clicks · 0.533% CTR · position 8.6** |
| Recorded disposition | **REWRITE IN PLACE** — *"rebuild on the spoke template"*. Not redirect. |
| Pages in the physiotherapy cluster | **1** — this is the only one |
| Demand tier | 🟢 **Proven**, Wave 1 |

The spec's own diagnosis of this cluster (12 query variants, 2,468 impressions, **1 click total**):

| Query | Impr | Clicks | Pos |
|---|---|---|---|
| `physiotherapy is covered under insurance` | 319 | 0 | **2.2** |
| `is physiotherapy included in insurance` | 316 | 0 | **2.6** |
| `physiotherapy insurance coverage` | 307 | 1 | **2.7** |
| `physiotherapy claim insurance` | 288 | 0 | **3.7** |
| `physiotherapy coverage` | 205 | 0 | **2.5** |
| `physiotherapy covered by insurance` | 180 | 0 | **2.5** |

And its conclusion:

> "Ranking in the top three across a dozen variants and earning one click is a **title and
> snippet failure, not a ranking problem.** Confirms physiotherapy in wave 1."

## Why a redirect is the wrong instrument here

1. **The page ranks 2.2 to 2.7 on the money queries.** That is about as good as position gets. A
   redirect points those rankings at a URL with no history and asks it to re-earn them. That
   usually takes weeks to months and is not guaranteed to land back at position 2.
2. **It solves nothing.** The problem is that nobody clicks. That is the title and the snippet,
   both editable today at zero ranking risk. Redirecting spends a page-1 position to fix a
   copywriting problem.
3. **There is nothing to consolidate.** Redirects earn their keep when merging duplicates or
   retiring buried pages. This is the cluster's only page and it is on page 1.
4. **It contradicts the audit.** Only 2 of 105 audited rows were marked REDIRECT, and both were
   genuinely buried — position 70.9 at 0.011% CTR, and a provider-discovery page at 0.234%. This
   page is neither.

## Options

**A — Recommended. Don't build `/cover/physiotherapy/` as a separate page.**
Rewrite the health-guide page in place on the spoke template: new title, new description, add the
direct-answer block and the insurer matrix. Point the hub's cover-by-treatment card at its existing
URL. You get the spoke's content quality and keep positions 2.2 to 2.7. Keep the slug reserved.

**B — Build the spoke and keep both, differentiated.**
Not advisable. Both pages would target "is physiotherapy covered", which is the same intent. That
is cannibalisation by construction, and this cluster cannot afford to split a top-3 position.

**C — Build the spoke and redirect, but sequence it.**
If the folder consistency decision is firm, de-risk it: rewrite the **old** page's title and
description first and watch CTR for four to six weeks. If CTR recovers, the problem is solved for
free and the redirect becomes unnecessary. If CTR stays broken while sitting at position 2, then the
template genuinely is the issue and the redirect is justified on evidence. Costs six weeks, saves a
possible ranking loss.

I would take A, or C if `/cover/` has to be the canonical home for all cover content.

## The same question applies to 13 other pages, and one of them is much bigger

The audit explicitly marked these **KEEP + UPGRADE — "Do not redirect"** because they convert above
the `-hiart` benchmark of 1.227%. Every one maps onto a cover slug you are launching:

| Page | Slug it maps to | Impr | Clicks | CTR | Pos |
|---|---|---|---|---|---|
| `/health-insurance/articles/maternity-insurance-in-uae/` | `maternity` | **138,170** | **1,798** | 1.301% | 8.2 |
| `/is-dermatology-covered-by-health-insurance-hiart/` | `dermatology` | 19,261 | 354 | 1.838% | 7.2 |
| `/health-insurance/articles/health-insurance-for-diabetes/` | `diabetes-thyroid` | 10,412 | 145 | 1.393% | 6.9 |
| `/health-insurance/articles/best-health-insurance-plans-for-cancer-patients-in-uae/` | `cancer` | 10,393 | 145 | 1.395% | 10.8 |
| `/health-insurance/articles/health-insurance-for-heart-patients/` | `cardiac` | 8,412 | 95 | 1.129% | 12.1 |
| `/health-insurance/health-guide/opd-cover/` | `gp` | 7,962 | 82 | 1.030% | 8.4 |
| `/health-insurance/articles/insurance-for-kidney-patients/` | `kidney` | 7,003 | 145 | **2.071%** | 8.4 |
| `/health-insurance/articles/health-insurance-for-skin-treatment/` | `dermatology` | 2,107 | 22 | 1.044% | 6.5 |
| `/heres-how-obesity-affects-your-health-insurance-premiums-hiart/` | `bariatric` | 1,672 | 17 | 1.017% | 15.6 |
| `/does-your-health-insurance-plan-cover-tonsillitis-in-uae-hiart/` | `ent` | 1,368 | 18 | 1.316% | 37.2 |
| `/all-about-health-insurance-for-hypertension-patients-hiart/` | `diabetes-thyroid` | 1,025 | 16 | 1.561% | 14.8 |
| `/does-health-insurance-cover-liver-cirrhosis-hiart/` | `gastro` | 1,010 | 12 | 1.188% | 36.9 |
| `/health-insurance/articles/health-insurance-for-arthritis/` | `rheumatology` | 338 | 4 | 1.183% | 7.0 |

**Two things to decide before the launch, not during it:**

**1. Maternity is the exposure.** That page carries 138,170 impressions and 1,798 clicks at 1.301%
CTR — roughly 12× the physiotherapy page's impressions and 30× its clicks, and it already converts
above benchmark. If it redirects into `/cover/maternity/`, that is the single largest risk in the
whole launch. Treat it as REWRITE IN PLACE unless there is a reason that outweighs 1,798 converting
clicks a year.

**2. `opd-cover` is load-bearing for the internal linking plan.** The structure doc instructs
**every spoke** to link to `/health-insurance/health-guide/opd-cover/`. If it redirects, that
instruction breaks across all 30 spokes at once and every one of them needs its links repointed.
Settle its disposition before the spokes are written, not after.

## The general rule worth adopting

Redirect a page into a cover spoke when it is **buried** (deep positions, negligible CTR) or a
**true duplicate**. Rewrite in place when it **already ranks** and the failure is the title, the
snippet or the template. Position is expensive to buy and cheap to keep.

## Practical consequence for drafts already written

The orthopedic draft was advised to link `Physiotherapy session limits` at the health-guide URL.
If the redirect goes ahead, that becomes a link into a redirect. That doc has been updated to point
at `/health-insurance/cover/physiotherapy/` as a CMS placeholder instead. Any draft that links a
page whose disposition is FOLD, CONSOLIDATE or REDIRECT needs the same treatment — which is why
resolving the disposition now sits ahead of the linking step in the `/cover-page-content` skill.
