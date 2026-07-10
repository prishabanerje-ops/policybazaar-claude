# Internal Linking Guide

How Step 4's "Internal links" line actually gets populated — this is research against
real site data, not a placeholder to leave for the writer to fill in later.

---

## Method (grep the real asset first)

1. From the target topic, list 2–4 **adjacent** topics — subjects a reader of this piece
   would plausibly go to next, or that this piece depends on for context. Not the exact
   target keyword (that's the cannibalization check in Step 1) — one level broader or
   one level more specific.

   Example: target = "health insurance for diabetics Dubai" → adjacent topics might be
   "health insurance basics", "DHA mandatory", "pre-existing condition", "network
   hospital".

2. Run `bash_tool` with `grep -i` against the brand's bundled URL asset for each
   adjacent-topic keyword fragment:
   ```
   grep -i "pre-existing" assets/policybazaar-urls.txt
   grep -i "network-hospital" assets/policybazaar-urls.txt
   ```
   or for Paisabazaar:
   ```
   grep -i "credit-utilization" assets/paisabazaar-urls.txt
   ```
   This is instant, complete (every live URL at snapshot time), and costs no search
   quota — strongly prefer it over a live `site:` search.

3. Also check the brand-context file's "Known major hubs" table — if grep on a specific
   fragment comes up empty but the topic clearly belongs under a known category, the
   category hub itself (e.g. `/health-insurance/`) is a reasonable fallback link target.

4. From real results, pick the 2–3 strongest candidates — pages that a reader partway
   through the drafted piece would genuinely benefit from clicking to.

5. Write specific anchor text tied to the linking context, not the page's generic title.
   ✅ "see how DHA's mandatory minimums work" → links to the DHA basics page
   ❌ "click here" / "learn more" / "read this article"

## Fallback: live `site:` search

The bundled asset is a **snapshot as of July 2026** — it won't include pages published
after that. If a grep search comes back empty for a topic that plausibly has recent
coverage (a very current product, a just-launched page), fall back to a live
`site:policybazaar.ae [topic]` or `site:paisabazaar.ae [topic]` search before concluding
nothing exists. Don't skip straight to "no candidates found" without this fallback check
on topics where staleness is plausible.

If the person managing these skills re-uploads a refreshed URL export later, replace
`assets/policybazaar-urls.txt` / `assets/paisabazaar-urls.txt` with the new version —
there's no other step needed, every reference to these files reads them fresh each time.

---

## If nothing real comes back (asset AND fallback search both empty)

Say so explicitly — do not invent a plausible-sounding URL or page title. Options to
offer instead:
- Note it as a **pillar-page gap**: "No existing page covers [adjacent topic] — this
  might be worth flagging to the SEO team as a page that doesn't exist yet."
- Suggest linking to the site's closest broader category page as a fallback (e.g., the
  main health insurance hub) rather than fabricating a specific article.

This mirrors the Fact-Check lens's rule elsewhere in these skills: an absence of search
results is not something to paper over with a confident-sounding guess.
