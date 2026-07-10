# Brand Context — Policybazaar UAE

Read this when Step 1 determines the content under audit is for **policybazaar.ae**.
Bundles vertical, regulatory framework, terminology, and known competitors — everything
brand-specific lives here so the five lenses can stay brand-neutral in their rubrics.

---

## Vertical

Insurance aggregator/broker — health, life, motor, travel, and Islamic banking/takaful
content. Overwhelmingly YMYL: coverage decisions affect readers' financial and physical
wellbeing. This drives the Lens 4 (YMYL) framing and Lens 5 (Fact-Check) regulatory checks.

---

## Site Structure — Real URL Data (NEW)

`assets/policybazaar-urls.txt` bundles the **full, real list of ~3,750 live URLs** from
the site's sitemap (snapshot: July 2026). Used by SEO Lens Parameter 7 (Internal Linking)
in URL MODE to check not just whether links are present, but whether an obviously
relevant existing page was missed.

**Known major hubs** (fast path — the asset file is the completeness backstop):
`/health-insurance/`, `/car-insurance/`, `/travel-insurance/`, `/life-insurance/`,
`/term-insurance/`, `/home-insurance/`, `/general-insurance/`, `/critical-illness/`,
`/insurance-companies-in-uae/`, `/network-hospitals/`, `/investment-plans/`, `/funds/`,
`/gold-rate-in-uae/`. Most individual articles are flat root-level slugs with a coded
suffix (`-hiart`, `-ciart`, `-hipvd`, `-hicf`, etc.) rather than nested under category
paths — grep the asset file rather than guessing a nested path.

---

## Regulatory Framework (for Fact-Check Lens Parameter 2)

| Emirate / Scope | Regulator | Notes |
|---|---|---|
| Dubai | **DHA** (Dubai Health Authority) | Sets Dubai's mandatory health insurance minimums |
| Abu Dhabi | **DOH** (Department of Health) — formerly HAAD | Flag "HAAD" as outdated if found in current content |
| Federal / other emirates | **MOHAP** (Ministry of Health & Prevention) | Applies where no emirate-specific authority governs |
| General insurance licensing | UAE Insurance Authority (now part of Central Bank) | Relevant for authoritativeness/licensing claims |

## Named Entities (for Fact-Check Lens Parameter 3)

Insurers/plans to verify for current names and accurate description: Daman / Sukoon
(formerly Oman Insurance — watch for the rebrand), AXA, MetLife, and other UAE-licensed
insurers named in content. For travel-specific entities and rebrand watch items, see
the Travel Insurance section below.

---

## Travel Insurance — Vertical Notes (added 2026-07-10)

Read this section when the Step 1 vertical is **Travel**.

### Authorities (Fact-Check Lens Parameter 2)

Travel insurance has no emirate health-authority mandate (DHA/DOH/MOHAP govern health
plans, not travel policies). The authorities that matter:

| Claim type | Authority | Notes |
|---|---|---|
| Insurer licensing | **Central Bank of the UAE** (absorbed the UAE Insurance Authority) | For "licensed insurer/broker" claims |
| Visa coverage minimums | **Destination consulate/embassy rules** | e.g. Schengen minimums come from the EU Visa Code, not from any UAE body |
| Insurer policy terms | **The insurer's own policy wording** | Coverage limits/exclusions — never attribute these to a regulator |

**Schengen baseline (verified 2026-07-10, secondary sources — re-verify per audit):**
minimum **€30,000** emergency medical cover including repatriation, valid across all
**29** Schengen states, per EU Regulation (EC) No 810/2009 (Schengen Visa Code). No
coverage-minimum increase was planned for 2026 at verification date. A policy meeting
the minimum is a visa *requirement*, never a visa *guarantee* — approval stays with
the consulate.

### Travel Entities & Rebrand Watch (Fact-Check Lens Parameter 3)

PB.ae's own travel URLs still carry pre-rebrand insurer names — treat any current-name
claim in content as a fact-check item:

| Old name (still in PB URLs) | Current name | Rebrand (verified 2026-07-10) |
|---|---|---|
| RSA (Middle East) | **Liva** | RSA ME + NLGIC rebranded Sept 2023, GCC-wide |
| AXA (Gulf) | **GIG Gulf** | Acquisition Sept 2021, rebrand completed June 2022 |
| Oman Insurance | **Sukoon** | Same rebrand watch as health |

Other insurers named on PB.ae travel provider pages (verify per audit, names as listed
July 2026): Allianz, AIG, World Nomads, Union, Emirates Insurance, Dnata, Adamjee,
HSBC, MetLife, DIC (Dubai Insurance Company).

### Travel Terminology

Single-trip vs. annual multi-trip, inbound vs. outbound cover, policy excess,
territorial validity, Schengen-compliant policy, trip cancellation vs. curtailment,
cancel-for-any-reason (CFAR) cover, emergency medical evacuation, repatriation,
per-item baggage limit, claim documentation deadline, pre-existing condition exclusion,
adventure/hazardous-activity exclusion.

### Travel YMYL Framing (Lens 4)

Harm category is **financial + visa-compliance** (and medical when the content gives
destination-health advice): inadequate medical cover abroad, policies that don't satisfy
visa requirements, and missed claim conditions all carry real consequences. Disclaimers
should point readers to the insurer's policy wording and official consulate guidance.

---

## Terminology

Deductible, co-pay, co-insurance, network hospital, pre-authorization, waiting period,
pre-existing condition exclusion, basic vs. enhanced plan, open enrollment, takaful,
rider, sum insured, claim settlement ratio.

---

## Known Competitors

For cross-checking content that names or compares against competitors — not a substitute
for the Fact-Check lens's live `web_search` verification.

Bayzat, GIG (Gulf Insurance Group), InsuranceMarket.ae (licensed brokerage, est. 1995),
Yallacompare (formerly Compareit4me).

---

## E-E-A-T Credential Pattern

Credentials that carry weight: licensed insurance advisor, DHA- or DOH-familiar reviewer,
certified insurance professional.
