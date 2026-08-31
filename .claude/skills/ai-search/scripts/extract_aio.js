/*
 * AI Overview extraction function — inject into the Google results page.
 *
 * Run it via the browser MCP's JS-evaluation tool:
 *   - Playwright MCP:      browser_evaluate  with  function = (the whole arrow fn below)
 *   - Chrome DevTools MCP:  evaluate_script   with  function = (the whole arrow fn below)
 *
 * It is idempotent and self-contained: detects a CAPTCHA, detects whether an
 * AI Overview is present, expands "Show more" (body) and "Show all" (sources),
 * then returns the full verbatim text plus citation data at TWO levels:
 *   - a flat, ordered, de-duplicated `hosts` list (same shape callers already use)
 *   - `sectionCitations`: which specific answer bullet/paragraph each inline
 *     citation chip is attached to — this is what proves/measures "fan-out"
 *     (Google citing a different source per sub-facet of the question, not one
 *     flat list for the whole answer).
 *
 * WHY THIS ISN'T HREF-BASED ANYMORE (2026-08-31 rewrite):
 *   Google's current AI Overview UI renders zero static <a href> citation
 *   links — confirmed by walking 6 DOM ancestor levels up from a source card
 *   and finding no href/data-url/ping anywhere. Citations are click-handler-only
 *   (Google's own JS resolves the destination). So this script identifies
 *   citations by their STRUCTURAL role instead (verified against the live page,
 *   not guessed from rendered text — an earlier text-pattern-only approach was
 *   tried and discarded because it misfired on section headings):
 *     - inline citation chip   = span.WBgIic.Wg1cdb.notranslate (has a favicon,
 *       text = "Publisher Name" or "Publisher Name +N")
 *     - trailing source card   = .cRH23c.g7lqo.sYLMkd wrapper, containing
 *       .gpZmoc.Hnm1Fe (article title) + .xWZV4e (publisher name)
 *     - section label for a chip = nearest preceding strong.rQesXe.MPyX
 *       (a bullet's bolded lead-in, e.g. "Allianz Care:") or [role="heading"]
 *   Since no URL is ever exposed, publisher NAME is resolved to a domain via
 *   KNOWN_PUBLISHERS below — a small curated map for the fixed UAE health/
 *   travel insurance competitive set. A name not in the map is reported as
 *   {host: null, needsReview: true} rather than guessed — extend the map
 *   when `unresolved` shows real competitors you recognize.
 *   NOTE: this selector set is tied to Google's current class names, which are
 *   not permanent — if `sectionCitations`/`trailingSources` come back empty
 *   while `hasAIO` is true, Google's markup has likely changed again and this
 *   script needs re-verifying against a live page before trusting its output.
 *
 * Returns one of:
 *   { hasCaptcha: true }                                  -> STOP, report a block
 *   { hasAIO: false, hasCaptcha: false }                  -> no Overview for this query (record honestly)
 *   { hasAIO: true, hasCaptcha: false, error }             -> AI Overview heading found but body container not resolved
 *   { hasAIO: true, hasCaptcha: false, text, citationCount, hosts,
 *     sectionCitations, trailingSources, unresolved, mentionedNotCited }
 *
 * Never fabricate a result when this errors or returns hasCaptcha — report the failure.
 */
async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const bodyText = document.body.innerText || "";

  const hasCaptcha =
    /unusual traffic|not a robot|recaptcha|systems have detected/i.test(bodyText) ||
    !!document.querySelector("form#captcha-form");
  if (hasCaptcha) return { hasCaptcha: true };

  const hasAIO = /AI Overview/i.test(bodyText);
  if (!hasAIO) return { hasAIO: false, hasCaptcha: false };

  // Expand the Overview body ("Show more") AND open the full ranked sources list
  // ("Show all") so every citation loads.
  const clickByText = (re) =>
    Array.from(
      document.querySelectorAll(
        'div[role="button"], button, a[role="button"], span[role="button"], div[role="link"], a'
      )
    )
      .filter((e) => re.test((e.innerText || "").trim()))
      .forEach((e) => { try { e.click(); } catch (_) {} });
  clickByText(/^\s*show more\s*$/i);
  clickByText(/^\s*show all\s*$/i);
  await sleep(1500);

  // --- Locate the AI Overview body container ---
  const all = Array.from(document.querySelectorAll("div,h1,h2,h3,span"));
  const heading = all.find(
    (e) =>
      (e.childElementCount === 0 || /H[123]/.test(e.tagName)) &&
      /^\s*AI Overview\s*$/i.test((e.innerText || "").trim())
  );
  let bodyContainer = null;
  let text = "";
  if (heading) {
    bodyContainer = heading;
    for (let i = 0; i < 8; i++) {
      if (bodyContainer.parentElement) bodyContainer = bodyContainer.parentElement;
      if ((bodyContainer.innerText || "").length > 600) break;
    }
    text = (bodyContainer.innerText || "").replace(/^\s*AI Overview\s*/i, "").trim();
  }
  if (!bodyContainer) return { hasAIO: true, hasCaptcha: false, error: "heading not found" };

  // Curated publisher-name -> domain map for the UAE health/travel insurance
  // competitive set, seeded from prior verified scrapes. Extend as new
  // competitors show up in `unresolved` — never guess a mapping here.
  const KNOWN_PUBLISHERS = {
    "pacific prime": "pacificprime.com",
    "hayah insurance": "hayah.com", "hayah": "hayah.com",
    "expat network": "expatnetwork.com",
    "sukoon insurance": "direct.sukoon.com", "sukoon": "direct.sukoon.com",
    "insurancehub.ae": "insurancehub.ae", "insurancehub": "insurancehub.ae",
    "allianz care": "allianzcare.com",
    "shory insurance": "shory.com", "shory": "shory.com",
    "lifecare international": "lifecareinternational.com",
    "insurancemarket.ae": "insurancemarket.ae", "insurancemarket": "insurancemarket.ae",
    "takaful emarat": "takafulemarat.com",
    "policybazaar uae": "policybazaar.ae", "policybazaar": "policybazaar.ae",
    "esanad insurance": "esanad.com", "esanad": "esanad.com",
    "metlife uae": "metlife.ae", "metlife": "metlife.ae",
    "tata aig": "tataaig.com",
    "seven insurance brokers": "seveninsurancebrokers.com",
    "gargash insurance": "gargashinsurance.com",
    "savington": "savington.ae",
    "dubai insurance": "dubins.ae",
    "feather insurance": "feather-insurance.com",
    "tameen insurance": "tameeninsurance.ae", "tameen": "tameeninsurance.ae",
  };
  const resolveHost = (label) => KNOWN_PUBLISHERS[(label || "").trim().toLowerCase()] || null;

  // --- Inline (primary) citations: chip -> nearest preceding section label ---
  const flowEls = Array.from(
    bodyContainer.querySelectorAll(
      'strong.rQesXe.MPyX, [role="heading"], span.WBgIic.Wg1cdb.notranslate'
    )
  );
  const sectionCitations = [];
  let currentSection = "";
  for (const el of flowEls) {
    if (el.matches("span.WBgIic.Wg1cdb.notranslate")) {
      const raw = (el.innerText || "").replace(/\s+/g, " ").trim();
      const m = raw.match(/^(.*?)\s*\+(\d+)$/);
      const citedAs = (m ? m[1] : raw).trim();
      const additionalCount = m ? parseInt(m[2], 10) : 0;
      if (!citedAs) continue;
      const host = resolveHost(citedAs);
      sectionCitations.push({
        answerSection: currentSection.slice(0, 100),
        citedAs,
        additionalCount,
        host,
        needsReview: !host,
      });
    } else {
      const t = (el.innerText || "").replace(/\s+/g, " ").trim();
      if (t && !/^ai overview$/i.test(t)) currentSection = t;
    }
  }

  // --- Trailing source cards (the "Show all" list) ---
  const trailingSources = Array.from(bodyContainer.querySelectorAll(".cRH23c.g7lqo.sYLMkd"))
    .map((c) => {
      const citedAs = (c.querySelector(".xWZV4e")?.innerText || "").replace(/\s+/g, " ").trim();
      const title = (c.querySelector(".gpZmoc.Hnm1Fe")?.innerText || "").replace(/\s+/g, " ").trim();
      const host = resolveHost(citedAs);
      return { citedAs, title, host, needsReview: !host };
    })
    .filter((c) => c.citedAs);

  // --- Flat, ordered, de-duplicated hosts list (kept for existing callers) ---
  const seen = new Set();
  const hosts = [];
  [...sectionCitations, ...trailingSources].forEach((c) => {
    if (c.host && !seen.has(c.host)) { seen.add(c.host); hosts.push(c.host); }
  });

  // --- Publisher names that couldn't be resolved -> KNOWN_PUBLISHERS needs updating ---
  const unresolved = [
    ...new Set(
      [...sectionCitations, ...trailingSources].filter((c) => c.needsReview).map((c) => c.citedAs)
    ),
  ];

  // --- Brand named in the answer prose but not cited as a source anywhere ---
  const mentionedNotCited = !hosts.includes("policybazaar.ae") && /\bpolicy\s*bazaar\b/i.test(text);

  return {
    hasAIO: true,
    hasCaptcha: false,
    text,
    citationCount: hosts.length,
    hosts,
    sectionCitations,
    trailingSources,
    unresolved,
    mentionedNotCited,
  };
}
