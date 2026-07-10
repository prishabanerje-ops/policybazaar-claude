# Brand Context — Policybazaar UAE

Read this when Step 0 determines the brief is for **policybazaar.ae**. Bundles vertical,
regulatory framework, terminology, and known competitors in one place — everything
brand-specific for this site lives here so the rest of the skill can stay brand-neutral.

---

## Vertical

Insurance aggregator/broker — health, life, motor, travel, and (increasingly) Islamic
banking/takaful content. Content is overwhelmingly YMYL: coverage decisions affect
readers' financial and physical wellbeing.

**Site for internal-link and cannibalization searches:** `site:policybazaar.ae` (fallback
only — see "Site Structure" below for the preferred method)

---

## Site Structure — Real URL Data (NEW)

`assets/policybazaar-urls.txt` bundles the **full, real list of ~3,750 live URLs** from
the site's sitemap (snapshot: July 2026). Use this instead of a live `site:` search for
internal-linking and cannibalization lookups — it's instant, complete, and costs no
search quota. See `references/internal-linking-guide.md` for exactly how to query it.

**Known major hubs** (fast path for common topics — the asset file is the completeness
backstop for anything not listed here):

| Category | Hub URL |
|---|---|
| Health insurance | `/health-insurance/` |
| Car insurance | `/car-insurance/` |
| Travel insurance | `/travel-insurance/` (+ `/travel-insurance-by-destination/`) |
| Life insurance | `/life-insurance/` |
| Term insurance | `/term-insurance/` |
| Home insurance | `/home-insurance/` |
| General insurance | `/general-insurance/` |
| Critical illness | `/critical-illness/` |
| Bike insurance | `/bike-insurance/` |
| Fleet insurance | `/fleet-insurance/` |
| Vintage car insurance | `/vintage-car-insurance/` |
| Motor warranty | `/motor-warranty/` |
| Network hospitals | `/health-insurance/network-hospitals/`, `/network-hospitals/` |
| Insurance companies directory | `/insurance-companies-in-uae/` |
| Investment plans | `/investment-plans/`, `/investment-calculators/`, `/funds/`, `/sip/` |
| Gold rate | `/gold-rate-in-uae/`, `/gold-rate-dubai/`, `/gold-rate-abu-dhabi/` |
| Car insurance by emirate | `/car-insurance-abu-dhabi/`, `/car-insurance-ajman/`, `/car-insurance-al-ain/`, `/car-insurance-fujairah/`, `/car-insurance-ras-al-khaimah/`, `/car-insurance-sharjah/` |
| Health insurance by emirate | `/health-insurance-abu-dhabi/`, `/health-insurance-in-fujairah/`, `/health-insurance-umm-al-quwain/` |
| Calculators | `/car-insurance-calculator-uae/`, `/travel-insurance-calculator-uae/` |
| RTA / registration | `/rta/` |

Note: most individual articles live as flat root-level slugs with a coded suffix (e.g.
`-hiart` = health insurance article, `-ciart` = car insurance article, `-hipvd` =
health insurance provider page, `-hicf` = claim form, `-trmart` = term insurance
article) rather than nested under their category path — this is a legacy CMS pattern.
Don't assume a topic's URL will be nested; grep the asset file instead of guessing a path.

---

## Regulatory Framework

| Emirate / Scope | Regulator | Notes |
|---|---|---|
| Dubai | **DHA** (Dubai Health Authority) | Sets Dubai's mandatory health insurance minimums |
| Abu Dhabi | **DOH** (Department of Health) — formerly HAAD | Don't use "HAAD" for current content; flag if found |
| Federal / other emirates | **MOHAP** (Ministry of Health & Prevention) | Applies where no emirate-specific authority governs |
| General insurance licensing | UAE Insurance Authority (now part of Central Bank) | Relevant for authoritativeness/licensing claims |

Getting the regulator wrong for the emirate in question (e.g., citing DHA for an
Abu Dhabi–specific claim) is a Fact-Check-lens-severity error, not a minor one.

---

## Terminology

Deductible, co-pay, co-insurance, network hospital, pre-authorization, waiting period,
pre-existing condition exclusion, basic vs. enhanced plan, open enrollment, takaful
(Islamic insurance), rider, sum insured, claim settlement ratio.

---

## Known Competitors

Use this to sanity-check live SERP research, not as a replacement for it — always still
run Step 1's `web_search`/`web_fetch`, since rankings shift.

| Competitor | Positioning |
|---|---|
| **Bayzat** | HR/benefits platform with a strong UAE health insurance comparison arm |
| **GIG (Gulf Insurance Group)** | Direct insurer, also runs comparison-style content |
| **Daman / Sukoon** (formerly Oman Insurance) | Major UAE insurer — watch for the rebrand when citing this name |
| **MetLife** | Direct insurer with UAE-specific content |
| **InsuranceMarket.ae** | Licensed brokerage, founded 1995, direct content competitor |
| **Yallacompare** (formerly Compareit4me) | Cross-vertical comparison site — also competes with Paisabazaar UAE on loans/credit content, so it can show up regardless of which brand a brief is for |

---

## E-E-A-T Credential Pattern

Author/reviewer credentials that carry weight here: licensed insurance advisor, DHA- or
DOH-familiar reviewer, certified insurance professional, or a named editorial lead with
stated insurance-industry experience.
