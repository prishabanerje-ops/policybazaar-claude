# Brand Context — Paisabazaar UAE

Read this when Step 0 determines the brief is for **paisabazaar.ae**. Same business
group as Policybazaar UAE, but a different vertical, regulator, and competitor set —
don't reuse Policybazaar's insurance framing here.

---

## Vertical

Personal finance marketplace — personal loans, credit cards, savings/bank accounts,
business loans, credit score (AECB) products, and comparison content across UAE banks.
Also YMYL: borrowing and credit decisions directly affect readers' financial wellbeing.

**Site for internal-link and cannibalization searches:** `site:paisabazaar.ae` (fallback
only — see "Site Structure" below for the preferred method)

---

## Site Structure — Real URL Data (NEW)

`assets/paisabazaar-urls.txt` bundles the **full, real list of ~2,930 live URLs** from
the site's sitemap (snapshot: July 2026). Use this instead of a live `site:` search for
internal-linking and cannibalization lookups — it's instant, complete, and costs no
search quota. See `references/internal-linking-guide.md` for exactly how to query it.

**Known major hubs** (fast path for common topics — the asset file is the completeness
backstop for anything not listed here):

| Category | Hub URL |
|---|---|
| Credit cards | `/credit-cards/`, `/credit-cards/articles/`, `/credit-cards/reviews/` |
| Personal loans | `/personal-loans/`, `/personal-loans/articles/`, `/personal-loans/reviews/` |
| Bank accounts | `/bank-accounts/`, `/bank-accounts/articles/`, `/bank-accounts/reviews/`, `/bank-accounts/debit-card/` |
| Car loans | `/car-loans/`, `/car-loans/articles/`, `/car-loans/reviews/` |
| Mortgage loans | `/mortgage-loan/`, `/mortgage-loan/articles/`, `/mortgage-loan/reviews/` |
| Credit score | `/credit-score/`, `/credit-score/articles/`, `/credit-score/reviews/`, `/credit-score/news-and-update/` |
| Gold rate | `/gold-rate/` (+ per-emirate sub-pages, e.g. `/gold-rate/gold-rate-dubai-today/`) |
| Bank hub pages | `/emirates-nbd/`, `/fab/`, `/hsbc-bank/`, `/dubai-islamic-bank/`, `/abu-dhabi-islamic-bank/`, `/abu-dhabi-commercial-bank/`, `/citibank/`, `/commercial-bank-of-dubai/`, `/rakbank/`, `/emirates-islamic-bank/`, `/al-hilal-bank/`, `/deem-bank/`, `/ajman-bank/`, `/standard-chartered-bank/`, `/national-bank-of-fujairah/`, `/mashreq-neo-bank/` |

Note: bank-specific product pages follow a `[bank-name]-[product-type]-bact` pattern
(e.g. `/emirates-nbd-savings-account-bact/`, `/adcb-current-account-bact/`) — these are
real, numerous, and not worth listing individually here; grep the asset file for the
specific bank + product combination instead.

---

## Regulatory Framework

| Scope | Regulator / Body | Notes |
|---|---|---|
| Bank lending, consumer credit rules | **Central Bank of the UAE (CBUAE)** | Governs interest rate disclosure, lending caps, consumer protection |
| Credit scoring / credit reports | **AECB** (Al Etihad Credit Bureau) | The UAE-wide credit bureau — cite for anything about credit scores/reports |
| Product providers | Individual banks (ADCB, FAB, Emirates NBD, HSBC, DIB, and others) | These are partner/source entities, not competitors — treat them like Policybazaar treats named insurers |

Confusing AECB (credit bureau) with a bank, or citing a bank's policy as if it were a
CBUAE-wide rule, is a Fact-Check-lens-severity error.

---

## Terminology

APR (annual percentage rate), flat rate vs. reducing rate, EMI (equated monthly
installment), credit limit, credit utilization ratio, salary transfer, debt-to-income
ratio, foreclosure/early settlement, minimum salary requirement, unsecured loan, AECB
credit score/report, debt consolidation.

---

## Known Competitors

Use this to sanity-check live SERP research, not as a replacement for it — always still
run Step 1's `web_search`/`web_fetch`, since rankings shift.

| Competitor | Positioning |
|---|---|
| **Souqalmal** | Long-established UAE comparison platform (loans, cards, insurance) — likely the single most consistent competitor |
| **Yallacompare** (formerly Compareit4me) | Cross-vertical comparison site — also competes with Policybazaar UAE on insurance content, so it can show up regardless of which brand a brief is for |
| **Compare4Benefit** | Comparison site for cards, mortgages, loans |
| **Soulwallet** | Credit card comparison-focused |

Note: some third-party roundups list Policybazaar UAE itself alongside these as a loan
comparison option — the two sister brands aren't fully walled off from each other in
the market, so don't be surprised if Policybazaar UAE shows up in a Paisabazaar SERP.

---

## E-E-A-T Credential Pattern

Author/reviewer credentials that carry weight here: banking/fintech industry experience,
credit/lending background, or a named editorial lead with stated experience translating
financial products into consumer-facing content.
