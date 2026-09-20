# Philippines Temporary Visit Visa — URL, Title, Description, H1 & Internal Links

**Status:** NEW page, no live URL yet
**Date:** 2026-08-17
**Input:** new-page draft (`Philippines Temporary Visit Visa (1).md`)
**Parent hub:** https://www.policybazaar.ae/travel-insurance/philippines-visa/ (live, 200)

## Verification status

| Item | Method | Result |
|---|---|---|
| Existing Philippines cluster | 3 URLs fetched, headings extracted | All 200 — hub, destination page, places-to-visit |
| Overlap with parent hub | Full visible text pulled and term-searched | 28,968 chars analysed, see §6 |
| Proposed slugs | 2 URLs fetched | Both **404 — available** |
| Candidate link targets | 18 URLs fetched individually | All 200, no redirects |
| URL inventory | `sitemap-travel-insurance.xml` | 434 URLs; 13 visa hubs, 101 visa articles |
| Character counts | Computed | Shown per option |

Because this page does not exist yet, there is no current title, description or H1 to critique. Everything below is a recommendation rather than a fix.

Not run: GSC (no data exists for an unpublished URL). Keyword demand for "philippines temporary visit visa" vs "philippines 9a visa" is unmeasured.

---

## 1. The page has a parent, and the parent is already waiting for it

`/travel-insurance/philippines-visa/` is live and contains this sentence inside its "What are the Different Types of Philippine Visas?" section:

> "Get a detailed overview of the Philippines Temporary Visitor Visa, including purpose-specific requirements and the complete list of supporting documents."

That is an unfulfilled handoff. Somebody wrote the hub expecting this spoke to exist. So the cannibalisation question resolves cleanly: **this is a legitimate spoke, not a duplicate**, and there is already a specific sentence on the hub that should become the inbound link.

I checked the hub's full text for overlap. It does **not** cover:

| Term | Hits on hub |
|---|---|
| `9(a)` / `9a` | 0 |
| `59 days` / `29 days` | 0 |
| `eTravel` | 0 |
| `extension` | 0 |
| `Bureau of Immigration` | 0 |
| `LSVVE` | 0 |

The hub does cover, and this page should **not** repeat: the full list of Philippine visa types, the e-Visa online application walkthrough, application tracking, processing time, rejection reasons, and reapplication.

**Territory for the new page:** the 9(a) designation itself, the 59 + 29 day arithmetic, purpose-by-purpose document lists, the extension process at the Bureau of Immigration, the long-stay extension, and eTravel. That is exactly what the draft covers, so the scoping is right.

---

## 2. URL

**Recommended**

```
/travel-insurance/articles/philippines-temporary-visit-visa/
```
Verified available (404).

The convention across the section is consistent: hubs sit at `/travel-insurance/<country>-visa/` (13 of them), and spokes sit at `/travel-insurance/articles/<visa-topic>/` (101 of them). Existing spokes follow the same shape as this one, for example `schengen-visit-visa`, `schengen-business-visa`, `schengen-transit-visa`, `schengen-visa-france`.

`/travel-insurance/articles/philippines-9a-visa/` is also free, but "temporary visit visa" is the plain-language term people search and the term the hub already uses in its handoff sentence. Keep 9(a) in the title and H1 rather than the slug.

Do **not** put this at `/travel-insurance/philippines-temporary-visit-visa/`. That namespace is for country hubs, and using it would set this spoke up to compete with its own parent.

---

## 3. Meta title

**Recommended**

```
Philippines Temporary Visit Visa (9a) for UAE Residents
```
55 characters. Names the visa, the 9(a) code, and the audience.

**Alternates**

| # | Title | Chars | Note |
|---|---|---|---|
| A | `Philippines Temporary Visit Visa (9a) for UAE Residents` | 55 | Default. |
| B | `Philippines Temporary Visit Visa from UAE \| Docs & Process` | 58 | Leads on the document lists, which are the page's bulk. |
| — | `Philippines 9(a) Temporary Visit Visa \| Requirements from UAE` | 61 | Rejected, over. |
| — | `Philippines Temporary Visit Visa: Requirements & How to Apply` | 61 | Rejected, over. |
| — | `Philippines Temporary Visit Visa - Documents, Fees & Extension` | 62 | Rejected, over. |

Write `9a` rather than `9(a)` in the title. Parentheses inside a title tag survive fine but add two characters for no search benefit, and you are close to the limit. Keep the formal `9(a)` in the H1 and body.

Note the parent hub's title is `Visa for the Philippines - Type, Process, Document Required`. Leading this page with "Philippines Temporary Visit Visa" keeps the two visibly distinct in a SERP.

---

## 4. Meta description

**Recommended**

```
The Philippines 9(a) visa covers stays over 30 days. See document requirements by visit purpose, how to apply from the UAE, and the rules for extending a stay.
```
159 characters.

**Alternates**

| # | Description | Chars |
|---|---|---|
| A | `The Philippines 9(a) visa covers stays over 30 days. See document requirements by visit purpose, how to apply from the UAE, and the rules for extending a stay.` | 159 |
| B | `Apply for a Philippines temporary visit visa (9a) from the UAE. Document lists by visit purpose, processing time, and how to extend your stay past 59 days.` | 155 |
| C | `Planning a longer trip to the Philippines? See who needs a 9(a) temporary visit visa from the UAE, the documents required by purpose, and how extensions work.` | 158 |

Option A leads with the 30-day threshold, which is the single fact that tells a reader whether this page applies to them at all.

Avoid the pattern used on the parent hub and on the Azerbaijan page — "This article will explore…", "We will explore the significance of…". Those describe the article instead of answering the question, and they are the descriptions Google most often discards.

---

## 5. H1

**Recommended**

```
Philippines Temporary Visit Visa for UAE Residents
```
50 characters.

Strip `(New Page)` from the draft's working heading before publish.

### Heading fixes in the draft

1. **`What are the Types of the Philippines Temporary Visit Visa?` does not match its content.** The section lists visit *purposes* (business, tourism, medical, study, conferences, entertainment), not visa types. There is one visa type here, the 9(a). Retitle to `Who Can Apply for a 9(a) Visa? Accepted Purposes of Visit` or similar, otherwise it reads as though there are several 9(a) sub-visas.
2. **`What are the Requirements for Each Type of 9(a) Visa Categories?` is ungrammatical.** "Each Type of … Categories" doubles the plural. Use `What Documents Does Each 9(a) Category Require?`.
3. **Heading levels jump from H2 to H4.** The document sub-sections (`Business Visitors Visa`, `Tourism or Leisure Visitors Visa`, `Filmmaking Visitors`, and so on) are marked `####` (H4) directly under an H2, skipping H3 entirely. Promote them to H3. The `How to Apply` steps correctly use H3, so the document blocks should match.
4. **Redundant bold restatements.** Under `#### Tourism or Leisure Visitors Visa` sits `**Requirements for Tourism Visa**`, and the same pattern repeats in five more sections. The heading already says it. Delete the bold lines.
5. **`Frequently Asked Questions` should be H2** with each question as H3. Currently the questions are bold paragraphs, so nothing is nested.
6. **The FAQ answers open with `Ans:`.** Drop it. It adds nothing for readers and pollutes the answer text that gets extracted into AI answers and snippets.

---

## 6. Internal linking

### 6a. The one link that matters most is inbound

Add a link from the parent hub, on the sentence that is already written for it:

| Source | Anchor (already on the page) | Target |
|---|---|---|
| `/travel-insurance/philippines-visa/` | `detailed overview of the Philippines Temporary Visitor Visa` | this new page |

That single link does more than any outbound work here, because the hub is established and this page has zero inbound links on day one.

Then add contextual inbound links from the other two Philippines pages, both live:

| Source | Suggested anchor | Priority |
|---|---|---|
| `/travel-insurance/travel-insurance-philippines/` | its `Important Documents Necessary for Philippines Visa from UAE` section | **High** |
| `/travel-insurance/articles/best-places-to-visit-in-philippines/` | in `Smart Travel Tips for UAE Residents`, on a stay-length or visa mention | Medium |

### 6b. Outgoing links

Anchors taken from the draft's own sentences. All targets verified 200.

**Back to the cluster — do these first**

| Anchor (in draft) | Target | Priority |
|---|---|---|
| needs copy edit: open by pointing at the hub for other visa categories | `/travel-insurance/philippines-visa/` | **High** |
| needs copy edit: in the Points to Remember section | `/travel-insurance/travel-insurance-philippines/` | **High** |
| needs copy edit: in the tourism-purpose block, on `Travel Itinerary` | `/travel-insurance/articles/best-places-to-visit-in-philippines/` | Medium |

A spoke that does not link back to its hub leaks the relationship. The hub link is not optional.

**Visa-status and eligibility context**

| Anchor (in draft) | Target | Priority |
|---|---|---|
| `Emiratis get free entry access` / `visa-exempt` framing | `/travel-insurance/articles/visa-free-countries-for-uae-residents/` | **High** |
| needs copy edit: where the draft addresses non-Emirati residents (see F1) | `/travel-insurance/articles/visa-on-arrival-for-uae-residents/` | **High** |
| needs copy edit: for Filipino residents of the UAE | `/travel-insurance/articles/schengen-visa-for-filipinos/` | Medium |
| `valid UAE residence permit` context in the requirements | `/travel-insurance/articles/uae-residence-visa/` | Medium |

`schengen-visa-for-filipinos` is worth noting: PB already publishes visa content aimed specifically at Filipino residents of the UAE. That is a direct signal about who reads Philippines content on this site, and it reinforces F1 below.

**Insurance links — the commercial reason the page exists**

| Anchor (in draft) | Target | Priority |
|---|---|---|
| `Health insurance policy (if any)` (medical-treatment documents) | `/travel-insurance/travel-medical-insurance/` | **High** |
| needs copy edit: add a line on cover for the trip itself | `/travel-insurance/` | **High** |
| needs copy edit: in the medical-treatment block, on UAE cover not travelling | `/health-insurance/` | Medium |
| `stay of less than 30 days` / short-trip framing | `/travel-insurance/single-trip-travel-insurance/` | Medium |
| `Letter of permission from a parent (applicable to a minor travelling alone)` | `/travel-insurance/family-travel-insurance/` | Medium |
| `Educational and training programmes` | `/travel-insurance/student-travel-insurance/` | Medium |
| `Latest 6 months' pension statements (applicable to retirees)` | `/travel-insurance/senior-citizen-travel-insurance/` | Medium |

**This is the draft's biggest structural weakness.** It is a 2,500-word visa guide on an insurance site that never once mentions travel insurance. Every sibling Philippines page has a travel-insurance section: the hub has `Do You Need Travel Insurance from the UAE to Visit the Philippines?`, the destination page has `Why Buy Travel Insurance for the Philippines Online?`, and even the places-to-visit article has `Why Do You Need Travel Insurance for the Philippines from the UAE?`. This page has nothing.

Add one short section, roughly 80 to 120 words, covering why travel insurance matters for a longer Philippine stay. The natural hooks are already in the draft: the medical-treatment visitor category, the "Health insurance policy (if any)" document line, and the fact that a 9(a) stay can run to 88 days or beyond.

**Density note:** the draft is long, roughly 2,500 words, and heavily list-based. The High-priority rows come to about 8 links, well under one per 200 words. There is room for every Medium row too, since the document lists are dense and unlinked.

### 6c. Do not link

**The four Reference Links in the draft must not ship.** Two are third-party commercial sites, and one carries live ad-tracking parameters:

| Reference link | Problem |
|---|---|
| `etravel-hub.com/etravel-philippines?gad_source=1&gad_campaignid=…&gclid=…` | Not a government domain, and the URL carries Google Ads click-tracking parameters. See F2. |
| `visa-philippines.info/philippines-temporary-visitor's-visa/` | Private third-party site, not authoritative. |
| `evisa.gov.ph/page/policy?...` | Genuine government source. Fine as a citation, but strip the query string. |
| `immigration.gov.ph/visas/visa-waiver/` | Genuine government source. Fine as a citation. |

Strip the whole block. If you want outbound authority links, cite `evisa.gov.ph` and `immigration.gov.ph` inline as clean URLs, the way the draft's own disclaimer already points readers at the Philippine Consulate General Dubai.

---

## 7. Content flags

**F1 — the page is written for the smallest part of the audience.** The draft addresses Emiratis almost throughout: "UAE nationals only need to apply for this non-immigrant visa if…", "Emiratis get free entry access", "If you're an Emirati, you don't need a visa", "allowing UAE nationals to stay in the Philippines for up to 36 months".

Policybazaar.ae's readership is overwhelmingly expat residents, not UAE nationals. The parent hub already handles this correctly:

> "UAE expatriates may need a temporary visit visa, unless their nationality is mentioned in the Philippines' visa-exempt list."

The new page never tells an Indian, Pakistani, Egyptian or Filipino UAE resident what applies to them, which is the question most readers arrive with. Filipino nationals need no Philippine visa at all, and PB already publishes `schengen-visa-for-filipinos`, so that audience is known to the business.

This is the most consequential fix on the page. Add an explicit "who this applies to" block near the top, splitting UAE passport holders from expatriate residents by nationality, and keep the Emirati-specific figures clearly labelled as such.

**F2 — the draft calls a non-government site "the official government portal".** The eTravel section says: "Know how to register yourself through the official government portal of eTravel Hub: 1. Visit eTravel Hub". The reference link given for it is `etravel-hub.com` carrying `gad_source`, `gad_campaignid` and `gclid` parameters, which are Google Ads click-tracking parameters. A `.com` domain running paid search is not a government portal. The draft's own other two citations use `.gov.ph` (`evisa.gov.ph`, `immigration.gov.ph`), which is the actual government pattern.

Directing readers to a paid third-party intermediary while calling it official is a trust and accuracy failure on a YMYL page, and it is the kind of thing that draws a manual action. Verify the correct official eTravel domain with a person before publish and correct the instruction. Philippine government domains are not reachable from this environment, so I cannot confirm the right URL myself.

**F3 — the 36-month extension figure omits the nationality split.** The draft says the long-stay extension allows "UAE nationals to stay in the Philippines for up to 36 months in total". The parent hub is more precise, citing Immigration Memorandum Circular No. SBM-2013-003: "visa-required nationals can extend their stay up to 24 months. Non-visa-required nationals may extend their stay for up to 36 months."

So 36 months applies to non-visa-required nationals, and 24 months to visa-required ones. Since most UAE expat residents fall in the second group, the draft omits the figure that applies to most of its readers, and the two pages will appear to contradict each other. Adopt the hub's framing and cite the same circular.

**F4 — the "Types" section is not about types.** Covered in §5, but it is a substantive issue as well as a heading one: a reader scanning for "which 9(a) do I need" will find a list of visit purposes and may conclude there are multiple visa products. There is one.

**F5 — the medical-treatment document list has broken indentation.** Under "A guarantee letter from the sponsor with financial proof", three items are nested as sub-bullets that do not belong to it: "Valid proof of hotel accommodation or lodging", "Health insurance policy (if any)". Those are standalone requirements, not properties of the guarantee letter. Same problem appears in the yachtsmen block. Re-level the lists.

**F6 — processing time is stated three times and hedged differently each time.** The steps say "5–10 working days", the FAQ says "5-10 business days", and both then add a caveat about additional documents. Pick one form (working days or business days), state it once with the caveat, and reference it from the FAQ rather than restating.

**F7 — visa figures need a date stamp and a human check.** The 30-day visa-free entry, 59-day validity, 29-day extension, 6-month long-stay extension, and 36/24-month caps all change by circular without notice. The draft's disclaimer is good and should stay. Add a "checked [Month Year]" line, and have someone verify against `evisa.gov.ph` and `immigration.gov.ph` before publish, since those domains are unreachable from here.

**F8 — no fee figures at all.** Step 3 says "you have to pay the visa fee at the embassy or consulate. Note that the fee varies as per your duration and purpose of the stay", and the extension list says "Applicable visa extension fees". A visa guide with no numbers will lose to competitors that have them. Either source current consular fees or say plainly that fees are set by the Consulate and link there.

**F9 — the trailing image has no alt text.** Same as the last two pages: embedded base64 image, no alt attribute, no caption. Add descriptive alt text and replace the inline data URI with an optimised asset.

**F10 — a bonus error on the parent hub.** While checking overlap I found the hub's own description of the Temporary Visitors Visa reads: "This visa is exclusively for those travelling to **the UAE** for medical treatment, attending conferences, meetings, seminars…". It should say the Philippines. Worth a one-line fix on `/travel-insurance/philippines-visa/` while you are linking the two pages together.

**F11 — FAQ schema.** The six questions are well formed and answer-first once `Ans:` is stripped. Emit `FAQPage` for machine readability, but do not expect FAQ rich results: Google restricts those to government and health-authority sites, which does not include commercial aggregators.
