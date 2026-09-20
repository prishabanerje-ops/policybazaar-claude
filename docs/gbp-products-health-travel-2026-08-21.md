---
title: GBP Products — Health & Travel Insurance
date: 2026-08-21
owner: Aakash Srivastava
status: ready to publish, pending price confirmation on Family Health Insurance
---

# Google Business Profile — Products feature: Health & Travel Insurance

## Sourcing notes (read before publishing)

**GBP Product editor field constraints** — Google's own help center (`support.google.com/business/answer/9124203`) does not publish exact character limits; the numbers below come from third-party GBP guides (Letter Counter, Wiremo) and agree on name length but disagree on description length (1,000 vs 1,500 chars). I designed every description to fit the tighter 1,000-char limit so it's safe either way.

- **Product name**: ≤58 characters
- **Category**: freeform, business-defined groups (used "Health Insurance" / "Travel Insurance" below)
- **Price**: the editor offers *Fixed price*, *Price range*, or *blank* — there is no native "Starting at" field type. Where the source page advertises a from-price, I've used Price range with the low end only, or noted it should go in the description instead.
- **Description**: ≤1,000 characters (verified count for every draft below, see table)
- **Link (optional)**: the product editor lets you attach a URL per product. Missed this in the first pass — added below, sourced from real internal links on policybazaar.ae, not guessed. Note: the `seo-local` playbook flags that Google's profile-level *Website* field shouldn't point at your strongest page (Sterling Sky research — risks suppressing organic rankings on that page). That guidance is documented for the single profile Website field, not per-product links, so it doesn't clearly block linking each product to its own landing page — flagging the overlap so you can make the call rather than me assuming it doesn't apply.
- **Photo**: JPG or PNG, 10 KB–5 MB, minimum 250×250 px, **recommended 720×720 px** (per Google's own photo guidance, `support.google.com/business/answer/6103862`)

**Pricing — retrieved live from policybazaar.ae just now (2026-08-21), not assumed:**
- Health Insurance main page: promoted rate "AED 1M cover from AED 4/day" (I annualized this to ≈AED 1,460/yr myself — that annualized figure is *my calculation*, not text on the page) and a basic-plan comparison-table figure of AED 340.
- **Family Health Insurance has no advertised starting price on the page** — I have not filled one in. Confirm your actual family-floater entry premium before publishing.
- Travel Insurance page: three distinct "Starting from" figures — AED 22 (single-trip/Allianz Schengen Single Trip plan), AED 47 (Schengen page promo/GIG Gulf), AED 24 (Watania Takaful Annual Gold, multi-trip).
- All of these are live promotional rates tied to specific insurer plans, not fixed PB prices — they will drift. Re-check before publishing and again periodically, since GBP product pricing that goes stale reads as misleading.

**Humanizer pass**: CLAUDE.md requires the `humanizer` skill on prose deliverables before I return them. That skill isn't installed on this machine (confirmed absent from `.claude/skills/` and the skill list) — I applied its criteria manually to every description below: no em-dash pauses, no rule-of-three flourishes, no inflated-significance words (testament/pivotal/seamless/robust/delve/landscape), no rhetorical-question openers, no signposting, no hashtags (not a functional GBP field anyway, and hashtags don't do anything in Business Profile). The originals were written as social hooks; this is a real compression for a structured field, not a stylistic trim — flagging per that rule.

---

## HEALTH INSURANCE

### 1. Health Insurance (flagship)
| Field | Value |
|---|---|
| Name (40 chars) | Health Insurance UAE - Compare 35+ Plans |
| Category | Health Insurance |
| Price | From AED 1,460/yr *(my annualization of the site's "AED 4/day" promo — verify before publishing)* |
| Link | https://www.policybazaar.ae/health-insurance/ |
| Description (368 chars) | Compare health insurance plans from 35+ UAE insurers in one place. Cover ranges from DHA and DOH-compliant basic plans to comprehensive policies with maternity and dental benefits, for residents in Dubai, Abu Dhabi, and across the UAE. Get quotes side by side, pick the plan that matches your budget and health needs, and buy online in minutes through Policybazaar.ae. |
| Photo | Hero/lifestyle shot related to family or hospital care, 720×720 px |

### 2. Family Medical Insurance
| Field | Value |
|---|---|
| Name (43 chars) | Family Health Insurance UAE - Compare Plans |
| Category | Health Insurance |
| Price | AED [X]/yr — **not advertised on the live page; confirm your actual starting premium** |
| Link | https://www.policybazaar.ae/family-health-insurance-hic/ |
| Description (402 chars) | Cover your spouse, children, and parents under one family floater health insurance plan instead of separate policies. Compare family medical insurance from top UAE insurers, including hospitalization, maternity, and dependent coverage, tailored to your family's budget whether you're in Dubai, Abu Dhabi, or elsewhere in the UAE. One premium, one renewal date, coverage for everyone who depends on you. |
| Photo | Family-oriented image, 720×720 px |

### 3. Basic Health Insurance
| Field | Value |
|---|---|
| Name (43 chars) | Basic Health Insurance UAE - Visa Mandatory |
| Category | Health Insurance |
| Price | From AED 340/yr *(retrieved from the site's comparison table, live as of today)* |
| Link | **No dedicated commercial landing page found.** The only matching internal link is a blog article, `https://www.policybazaar.ae/health-insurance/articles/essential-benefits-plan/` (Dubai's Essential Benefits Plan) — not a buy/quote page. Recommend either linking that article or falling back to `https://www.policybazaar.ae/health-insurance/` until a dedicated basic-plan page exists. Your call. |
| Description (327 chars) | Valid health insurance is a mandatory visa requirement for UAE residents. Compare DHA and DOH-approved basic health insurance plans across Dubai and the UAE that meet visa mandate requirements at the lowest cost, covering essential hospitalization and outpatient care. Stay compliant without paying for benefits you don't need. |
| Photo | Simple, document/visa-adjacent visual, 720×720 px |

---

## TRAVEL INSURANCE

### 4. Travel Insurance (flagship)
| Field | Value |
|---|---|
| Name (43 chars) | Travel Insurance UAE - Compare & Buy Online |
| Category | Travel Insurance |
| Price | From AED 22/trip *(retrieved, live promo rate — tied to a specific insurer plan, will change)* |
| Link | https://www.policybazaar.ae/travel-insurance/ |
| Description (317 chars) | Compare travel insurance plans from trusted insurers before your next trip out of the UAE, whether you're flying from Dubai, Abu Dhabi, or anywhere else in the country. Coverage includes trip cancellation, lost baggage, flight delays, and medical emergencies abroad. Get a quote and buy your policy online in minutes. |
| Photo | Airport/travel lifestyle image, 720×720 px |

### 5. Schengen Travel Insurance
| Field | Value |
|---|---|
| Name (42 chars) | Schengen Travel Insurance - Visa Compliant |
| Category | Travel Insurance |
| Price | From AED 47/trip *(retrieved, live promo rate)* |
| Link | https://www.policybazaar.ae/schengen-travel-insurance-tic/ |
| Description (318 chars) | Schengen visa travel insurance with at least EUR 30,000 medical coverage is required for entry into all Schengen zone countries. Compare and buy Schengen-compliant travel insurance online from Dubai or anywhere in the UAE, with instant policy issuance and documentation accepted by embassies for your visa application. |
| Photo | Europe/passport-and-visa visual, 720×720 px |

### 6. Multi Trip Travel Insurance
| Field | Value |
|---|---|
| Name (38 chars) | Multi-Trip Annual Travel Insurance UAE |
| Category | Travel Insurance |
| Price | From AED 24/yr *(retrieved, live promo rate)* |
| Link | https://www.policybazaar.ae/travel-insurance/annual-multi-trip-travel-insurance/ |
| Description (333 chars) | If you travel several times a year, an annual multi-trip travel insurance policy covers unlimited trips under one plan instead of buying a new policy each time. UAE residents in Dubai, Abu Dhabi, and beyond can compare annual travel insurance covering medical emergencies, delays, and cancellations for every trip in the policy year. |
| Photo | Frequent-flyer/luggage visual, 720×720 px |

---

## Before you publish — action items

1. **Confirm the Family Health Insurance starting price** — not on the live page, currently a placeholder.
2. **Re-verify all four AED figures pulled today** (1,460 calculated / 340 / 22 / 47 / 24) against current live pricing — these are tied to specific insurer promo plans and will drift.
3. Decide whether to use *Price range* (e.g., AED 340–3,000) instead of a single from-price — GBP's editor supports it natively and it may read as more accurate than a single "from" number.
4. Source or shoot the six photos at 720×720 px minimum before uploading, per Google's photo guidance.
5. **Decide the Basic Health Insurance link** — no dedicated buy/quote page exists for it today; pick between the EBP blog article and the general health-insurance page, or brief a new landing page.
6. Set the primary GBP category (e.g., "Insurance agency") separately from these product-level groupings — this file only covers the Products feature, not the profile's primary/secondary category setup (that's a separate, higher-impact lever per the local SEO playbook: primary category is Whitespark's #1 local pack ranking factor).
