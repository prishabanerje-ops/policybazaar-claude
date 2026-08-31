---
name: ai-search
description: Scrape AI-search citations for a set of prompts and produce a citation-position competitive analysis (Excel matrix + raw JSON + verbatim text + on-screen leaderboard). Covers Google AI Overviews AND ChatGPT web-search sources. Use whenever the user wants to capture, track, audit, or analyze what sources AI search engines cite — e.g. "scrape AI overview", "/ai-overview", "which sites does Google's AI cite", "are we cited in AI Overviews", "scrape ChatGPT sources", "what does ChatGPT cite for these keywords", "AI Overview citations", "GEO/AEO citation tracking", "LLM citation audit". Invoke even if the user just gives a topic and says they want the AI citation data. Also covers GEO, generative engine optimization, AEO, AI visibility, LLM mentions, Perplexity, SXO, "why isn't my page ranking", and intent mismatch.
---

# AI Search Hub

Three sub-tasks. For `scrape-citations` (the default — "scrape AI overview",
"which sites does the AI cite", citation matrices) continue with THIS file
below. Otherwise Read the mapped file and follow it exactly:

| Intent / `$1` | Read this file |
|---|---|
| optimize for AI engines / GEO / llms.txt — `geo` | `~/.claude/plugins/claude-seo/skills/seo-geo/SKILL.md` |
| SERP intent / page-type mismatch — `sxo` | `~/.claude/plugins/claude-seo/skills/seo-sxo/SKILL.md` |

# /ai-overview — AI-search citation tracker (Google AI Overview + ChatGPT)

Capture AI-search answers for many prompts, then show **who the AI cites and in what order** — so a brand can see its visibility gap. Generic for any topic; tracked brand defaults to **policybazaar.ae**.

The scripts and the scraper agent do the heavy lifting. This file is the orchestration.

## Ask these questions IN ORDER, then act
1. **"What topic do you want to track?"** (e.g. *Health Insurance*)
2. **Stored BU prompt set?** If the topic matches a file in `$SKILL/references/` — currently `prompts-health.md` (Health insurance UAE) and `prompts-travel.md` (Travel insurance UAE) — Read that file, take its numbered prompts verbatim (don't pad, trim, or reword), tell the user you're using the stored set, and **skip question 3**. Exception: if the user already supplied their own prompts, theirs win — go to Branch (1).
3. **"Will you (1) provide the prompts yourself, or (2) should I generate them from the topic?"**
4. **"Which engine(s): (1) Google AI Overview, (2) ChatGPT, or (3) both?"** Default to **Google AI Overview** if unstated.
5. Region: assume **UAE / English** (`google.ae`, `gl=ae`, `hl=en`) unless the user says otherwise or named a different market in step 1. Only ask if genuinely ambiguous.

Optional overrides the user may state anytime — honor silently: prompt count (default **50** when generating), a different brand, region, or output folder.

**If ChatGPT is selected, say this up front:** ChatGPT scraping uses the **Chrome DevTools engine and your logged-in chatgpt.com session** — make sure you're signed into ChatGPT in Chrome. It's **slow and block-prone** (Cloudflare/login can stop it), and many prompts will legitimately return **no sources** (ChatGPT only cites when it actually web-searches). This is the fragile path; Google AI Overview is the reliable one.

## Branch (1) — user provides prompts
Take their list verbatim (one per line). Don't pad or trim. Go to **Scrape**.

## Branch (2) — Claude generates the prompts
Generate **~50** distinct, natural prompts across intent buckets so the analysis is representative (not 50 rewordings of "best X"):
- **Provider/product discovery** — "best / top / cheapest / most affordable <topic>", segment variants (families, expats, seniors, students, SMEs, by city/region).
- **Cost / price** — "how much does <topic> cost", "average price of …".
- **Process / eligibility / regulation** — "how to get/buy/renew <topic>", "is <topic> mandatory", "requirements for …".
- **Types / coverage / features** — "does <topic> cover …", "best <topic> for <specific need>".
- **Specific brand / product** — "is <Brand> good", "<Brand> reviews", "<Brand A> vs <Brand B>".
- **Comparison / decision** — "how to choose <topic>", "X vs Y", "best value …".

Adapt buckets to the topic. Then **scrape immediately — no approval step** (user's chosen default). Show the generated list as you start so they can interrupt if it's off-target.

## Scrape — dispatch the ai-overview-scraper agent (once per selected engine)
Resolve this skill's base directory (announced when the skill loads) as `$SKILL`. Pick `$WORK` (current dir unless the user named one) and today's date (`date +%F`). For **each** selected engine, dispatch the **ai-overview-scraper** agent with: engine (`google` or `chatgpt`), the full prompt list, region, brand (default `policybazaar.ae`), the topic, and:
- google → `extract_fn_path` = `$SKILL/scripts/extract_aio.js`, `out_path` = `$WORK/aio_<slug>_<date>__google.json`
- chatgpt → `extract_fn_path` = `$SKILL/scripts/extract_chatgpt.js`, `out_path` = `$WORK/aio_<slug>_<date>__chatgpt.json`

The agent picks the browser (google: Playwright→Chrome; chatgpt: Chrome only, logged in), scrapes sequentially, writes the dataset JSON, and returns a short summary. If it reports a **block / login wall / no browser MCP**, relay that honestly and stop for that engine — do not fabricate the missing prompts. Run engines sequentially (one browser at a time). For tiny lists (≤ ~5) you may scrape inline with the matching extract script instead of spawning the agent.

## Analyze — build the report (one workbook, a sheet per engine)
Pass each engine's dataset as a `Label=path` pair:
```bash
python3 "$SKILL/scripts/build_matrix.py" \
  --data "Google AIO=$WORK/aio_<slug>_<date>__google.json" "ChatGPT=$WORK/aio_<slug>_<date>__chatgpt.json" \
  --out "$WORK/AIO_<slug>_<date>.xlsx" --brand policybazaar.ae --min-prompts 2
```
(Only include the engines you actually scraped.) Each engine gets a positions matrix sheet + a verbatim-text sheet; columns = domains cited in ≥2 prompts ranked by frequency; brand highlighted; NA = not cited; "cited in" + "avg position" summary rows. **For `google`-engine datasets**, each engine also gets:
- a **fan-out gap sheet**: which domain is cited as the source for a *specific* answer sub-facet ("primary") vs only appearing in the supplementary source list ("trailing-only"), plus a row-by-row list of which sub-facets the brand lost and who won them;
- an **actions sheet**: the same gaps turned into a direct, prioritized to-do list — content gaps ranked by competitor pressure, cases where the brand's own off-site content (e.g. a social post) is winning a citation the website should get, "named but not cited" prompts, and "zero presence" prompts. Every row is derived straight from the dataset — no invented recommendations.

(Both sheets need no extra flag; the script detects `sectionCitations`/`trailingSources` on the dataset automatically and skips them if absent, e.g. for `chatgpt` or older datasets.) The script prints per-engine leaderboards + a cross-engine brand line + fan-out visibility summary (including any `unresolved` competitor publisher names that need adding to `extract_aio.js`'s `KNOWN_PUBLISHERS` map). Copy the `.xlsx` to `~/Downloads/`.

### Target URLs for the actions sheet (optional but recommended)
The actions sheet has a **Target URL** column (which existing page to update, or where new content belongs). Google's search results (like its AI Overview) expose no real `href`s to scrape, so this can't be auto-populated — it needs a verified mapping:
1. For each distinct prompt/topic behind a gap row, search `site:policybazaar.ae <topic keywords>` on `google.ae` and **actually click through** to the top matching result (don't just read the truncated `cite` breadcrumb — it omits the real slug) to confirm the true destination URL.
2. Save the verified mapping as JSON: `{"by_prompt": {"<exact prompt text>": "<url>"}, "by_section_keyword": {"<keyword>": "<url>"}}` (section-keyword match wins when both could apply — it's more specific, e.g. routing "maternity waiting period" to a dedicated article even though the whole prompt maps to a broader page).
3. Pass it to `build_matrix.py` via `--target-urls path.json`.
Without this flag, the Target URL column says "not mapped" — never guess a plausible-looking URL. At full 50-prompt scale this verification step doesn't run itself; budget time for it (or extend the mapping file incrementally across runs) rather than promising a fully-automatic Target URL column.

## Present
- engine(s) used + coverage per engine (e.g. "Google: 48/50 had an Overview, 0 blocks; ChatGPT: 31/50 answered, 18 cited sources, stopped by a login wall at #32"),
- the **leaderboard(s)**,
- **where the tracked brand lands** per engine (coverage + avg position vs top competitors — the visibility gap),
- **for `google` datasets**, the fan-out gap: brand's primary vs trailing-only citation counts, and a few concrete examples of sub-facets lost and who won them (from the fanout gap sheet) — this is the actionable part, not just the leaderboard,
- the **top items from the actions sheet** (content gaps ranked by competitor pressure, any off-site-content findings, named-but-not-cited or zero-presence prompts) — and whether Target URLs were mapped or say "not mapped",
- file paths: the `.xlsx` (+ `~/Downloads` copy) and the raw `.json`(s).

## Non-negotiables (data integrity)
- Never present inferred/guessed AI content as scraped. No Overview / no ChatGPT sources → say so. A block → report exactly how far it got.
- AI answers are **personalized and non-deterministic** — state this is one snapshot from one session/region, not a stable ranking. (ChatGPT especially varies per account/run.)
- "Position" = order in the answer's cited-sources list (closest proxy to rank these surfaces expose), **not** a classic blue-link SERP rank — say so.

## Bundled files
- `references/prompts-health.md` — stored prompt set for Health insurance (UAE BU, supplied by Aakash).
- `references/prompts-travel.md` — stored prompt set for Travel insurance (UAE BU, supplied by Aakash).
- `scripts/extract_aio.js` — Google AI Overview extraction (inject via browser JS-eval).
- `scripts/extract_chatgpt.js` — ChatGPT sources extraction (Chrome DevTools, logged-in).
- `scripts/build_matrix.py` — builds the multi-engine `.xlsx` + leaderboards + fan-out gap/actions sheets (needs `openpyxl`; accepts `--target-urls`).
- Agent: `ai-overview-scraper` (drives the browser per engine, writes the dataset JSON).
