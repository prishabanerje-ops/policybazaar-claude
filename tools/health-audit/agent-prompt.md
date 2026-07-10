You are auditing ONE policybazaar.ae page as part of a batched health-insurance content audit.

- Page URL: {URL}
- Slug: {SLUG}
- Page type: {PAGE_TYPE}
- Tier: {TIER}
- Audit date: {AUDIT_DATE}

## Procedure

1. Read `/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills/content/content-audit/SKILL.md`
   and the reference files it lists per lens. Brand is Policybazaar UAE — read
   `references/policybazaar-context.md` and `references/schema-expectations-health.md`.
2. Run the URL MODE five-lens audit on {URL} at the depth for tier {TIER}:
   - **A-core / A-articles** — full depth: all five lenses including per-claim web fact-check.
   - **B** — light pass: title/meta/H1, page-specific facts (hospital/insurer names,
     locations, form links resolve), duplicate/thin-content risk; fact-check ONLY claims
     unique to this page. Score all five lenses but write "Tier B light audit" under the
     report header. Template-level findings are covered by the family's representative
     page — do not repeat them.

   Then run the skill's Step 2.6 two-way interlink analysis: OUTBOUND suggestions
   verified against the URL asset / sitemap snapshot (never invent a URL), INBOUND
   candidates marked "candidate-verify-source". Tier A: both directions. Tier B:
   outbound only, max 3.
3. Write the full report (skill Step 4 format) to:
   `/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result/policybazaar-{SLUG}-content-audit-{AUDIT_DATE}.md`
4. Write the structured JSON to:
   `/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result/audit-data/{SLUG}.json`
   Top-level keys (ALL required): url, slug, page_type, tier, audit_date, mode ("URL"),
   md_file, scores {seo, geo, human_likeness, ymyl, fact_check, overall — numbers},
   parameters [{lens, name, score, max, status, finding}],
   findings [{lens, severity, found, why, fix}],
   fact_checks [{claim, verification, correct_value, source, source_tier, status, fix}],
   ledger_entries [{fact_key, page_value, verified_value, source, source_tier, status}],
   schema_audit [{row_type, type_or_severity, parse, parity, detail}],
   priority_recs [{priority, issue, action}],
   interlink_opportunities [{direction ("outbound"|"inbound-candidate"), other_url,
   anchor_text, placement, rationale, status ("verified-target"|"candidate-verify-source")}]
   — empty list if no genuine opportunities.
   
   The schema_audit field contains one entry per schema row from the implemented-schema deep-dive.
   row_type indicates whether a row is "implemented" or "expected-missing"; type_or_severity captures the @type or severity label; parse indicates whether it parses validly; parity indicates whether it matches visible page content; detail provides a one-line note.
   
   Every checkable fact on the page (price, %, limit, deadline, regulatory claim,
   platform figure) gets a ledger_entry. fact_key is a normalized kebab-case key for the
   UNDERLYING fact, not the page's phrasing. FIRST read
   `/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result/audit-data/fact-keys.md`
   (if it doesn't exist, treat the registry as empty) and reuse an existing key when the
   fact matches; if none matches, invent a precise new key (the collector registers it).
   For facts with
   no external arbiter (platform figures like "plans from AED X on Policybazaar"), set
   verified_value to "n/a" and status to "Unverifiable".
5. TOOL FAILURE POLICY (hard rule): if the page fetch or a verification tool fails,
   do NOT fabricate or infer. If the page itself cannot be fetched, write NO files and
   return status "failed" with the exact failure in failure_reason. If only some
   verifications fail, mark those claims Unverifiable and continue.
6. Your final structured output: {url, status ("done"|"failed"), overall (number),
   md_file, json_file, failure_reason (empty string if done)}. Return "done" ONLY when
   both files are written.
