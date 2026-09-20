# Add Licence-Linked Trust Signal and Disclaimer to All Health & Travel Insurance Pages

## Description

Content addition only. Add the inline trust signal and the accordion disclaimer to every Health and Travel page, with each regulatory credential hyperlinked to its source certificate. Health includes Critical Illness.

No template, schema or component changes are in scope. Health copy is already approved. Travel copy is new and needs Compliance sign-off.

## Scope

| BU | Pages |
|---|---|
| Health (incl. Critical Illness) | 1,075 |
| Travel | 435 |
| **Total** | **1,510** |

All 1,510 pages. A regulatory disclaimer does not depend on a page's word count.

## Content to add

Copy and ready markup, English and Arabic, in:

- Health: `docs/disclaimer-health-2026-07-31.md`
- Travel: `docs/disclaimer-travel-2026-07-31.md`

Use the copy exactly as written. Do not paraphrase, re-order the credentials, or drop the `·` separators.

## Placement

| Component | Position |
|---|---|
| Inline trust signal | directly beneath the byline block, above the first body heading |
| Accordion disclaimer | last element before the footer |

Both components appear on the same page.

## Credentials by vertical

| Credential | Number | Health | Travel | Links to |
|---|---|---|---|---|
| Central Bank of the UAE registration | 123 | ✅ | ✅ | `https://cdn.policybazaar.ae/pbuae/images/IA-License-Renewal-2026.pdf` |
| DHA health insurance intermediary permit | BRK-00041 | ✅ | ❌ | `https://www.isahd.ae/Home/PermittedIntermediaries` |
| Emirates Insurance Federation membership | B81 | ✅ | ✅ | `https://static.pbcdn.ae/pbuae/images/Policybazaar-Middle-East-Insurance-Brokers-LLC.pdf` |

The DHA permit is health-specific. Dubai Health Authority does not regulate travel insurance, so it must not appear on any travel page.

External links use `target="_blank" rel="noopener"`. No `nofollow` on the ISAHD link.

## Verification

All three sources fetched and read on 2026-07-31, all HTTP 200.

| Claim | Source says |
|---|---|
| Registration No. 123 | CBUAE Licensing Division, Renewal Certificate in Register of Brokers, Ref. LR-2026-004831, dated 06 Dec 2025: "Registration No.: 123" |
| Permit No. BRK-00041 | ISAHD live permitted intermediaries register, row 48: "BRK-00041 · POLICYBAZAAR MIDDLE EAST INSURANCE BROKERS L.L.C" |
| Membership No. B81 | EIF Membership Registration Certificate for 2026: "EIF No: B 81", cross-confirms "CBUAE No: 123" |

Entity name is "Policybazaar Middle East Insurance Brokers LLC" on all three.

## Notes

- The Dubai DET commercial licence (No. 233354) is not used. Its hosted PDF shows an expiry of `07/02/2026`, which has passed.
- The approved Arabic health disclaimer ended `*تسري الشروط والأحكا`, missing the final `م`. The content file uses the corrected `*تسري الشروط والأحكام.` Confirm with Compliance before the 31 Arabic health pages go live.
- Arabic copy wraps Latin-script numbers in `<bdi>` so `BRK-00041` does not render as `00041-BRK`. Affects 31 Arabic health pages and 1 Arabic travel page.

## Done when

- [ ] Both components render on a sample of each page type in both verticals
- [ ] All links resolve to HTTP 200 and open the correct certificate
- [ ] No travel page renders the DHA permit
- [ ] Arabic pages render `BRK-00041`, `123` and `B81` left-to-right inside right-to-left text
- [ ] Accordion content is in the DOM on load, not injected on expand

## Reference

Health copy: `docs/disclaimer-health-2026-07-31.md`
Travel copy: `docs/disclaimer-travel-2026-07-31.md`
Per-URL page list: `docs/byline-gap-inventory-2026-07-31.csv`
