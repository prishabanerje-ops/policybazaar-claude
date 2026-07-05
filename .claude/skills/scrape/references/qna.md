---
name: scrape-qna
description: Scrape Reddit UAE subreddits, Quora, and Twitter/X for questions and discussions people are posting about a topic. Shows all results, then runs live GSC + sitemap coverage check with 3-tier classification and two-way interlinking suggestions. Best for finding FAQ and content gap opportunities.
---

Ask these three questions IN ORDER before doing anything:

1. "What topic do you want to research?" (e.g. "Health Insurance")
2. "What location? (default: UAE)"
3. "Optional regex to narrow the coverage check — this filters GSC and sitemap pages only, your scraped results are always shown in full. Leave blank to check all policybazaar.ae pages. (e.g. `health|insurance|medical`)"

---

### Step 1 — Run the scraper

```bash
cd ~/Documents/scraper && npm run scrape -- --query="<QUERY>" --location="<LOCATION>" --type=qna
```

Read the terminal output. Get the saved file path and result count.

---

### Step 2 — Read results

Read the full output MD file. Show all results as-is — do NOT filter by regex.

---

### Step 3 — Fetch live GSC + sitemap

**A. Live GSC data (real-time, last 30 days):**
```bash
python3 ~/.claude/plugins/claude-seo/scripts/gsc_query.py \
  --property sc-domain:policybazaar.ae \
  --days 30 \
  --dimensions query,page \
  --json 2>/dev/null
```
Each row has: `query`, `page` (URL), `clicks`, `impressions`, `ctr`, `position`.
If regex provided → keep only rows where `query` OR `page` URL matches the regex.

**B. Sitemap:**
WebFetch `https://www.policybazaar.ae/sitemap.xml`
If `<sitemapindex>`, fetch up to 3 relevant child sitemaps.
Extract all `<loc>` URLs.
If regex provided → keep only URLs matching the regex.

---

### Step 4 — Classify each result (3 tiers)

For each scraped question, extract:
- **Topic** — clean label from the question title
- **Source URL** — original question URL

Check against filtered GSC + sitemap:

| Tier | Condition | GSC Data to show |
|---|---|---|
| 🔄 UPDATE | Page found in GSC AND is ranking — add FAQ section | Clicks · Position |
| 🆕 CREATE | No page in GSC or sitemap — write a dedicated FAQ/article page | Impressions/mo if related query exists (🔥 if >1000); "no demand yet" if not |
| 🔧 FIX | Page in sitemap but absent from GSC — rewrite/reindex | "not ranking" |

---

### Step 5 — Two-way interlinking

For every **CREATE** and **FIX** item, invoke `/seo-interlinking` with the topic:

**Link From These Pages** (incoming — builds authority of new/fixed page):
- Contextual: existing pages whose body copy mentions the topic
- Structural: pages in the same section/category

**Link to These Pages** (outgoing — builds pillar authority):
- Identify the most relevant policybazaar.ae pillar pages
- Suggest anchor text for each
- Suggest placement in the new content body

For **UPDATE** items: "page already exists — no new incoming links needed" in Link From. Still suggest outgoing pillar links.

---

### Step 6 — Build coverage table

```markdown
## Coverage Analysis — policybazaar.ae (Live GSC · Last 30 days)
Regex on GSC/sitemap: [pattern or "none"] | GSC rows checked: N | Sitemap URLs: N

| Topic | Source URL | Action | GSC Data | Link From These Pages | Link to These Pages | Placement |
|---|---|---|---|---|---|---|
```

---

### Step 7 — Write summary (from scraped content only)

- **Top themes:** (recurring subjects across questions)
- **Recurring questions:** (asked multiple times — use these verbatim as H1s or FAQ headings)
- **Keyword signals:** (exact terms the audience uses — use in content verbatim)

---

### Step 8 — Update the MD file

1. Replace summary placeholder with real summary
2. Append Coverage Analysis table at the end

---

### Step 9 — Report to user

- "N questions found"
- Coverage: "M updates · K creates · J fixes"
- File: `<path>`
- "CREATE items with 🔥 impressions are highest priority — queries already getting demand with no landing page."

If GSC call fails: save results without coverage, report the error.
If zero results: "Nothing new found for '<QUERY>' in '<LOCATION>' in the last 30 days."
