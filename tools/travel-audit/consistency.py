"""Task 2 — cross-site consistency engine over audit-data JSONs."""
import json
import os
import sys
from collections import defaultdict
from datetime import date
from itertools import combinations
from pathlib import Path

from openpyxl import load_workbook

from schema import validate_audit_json

CONSISTENCY_COLUMNS = ["Fact Key", "Canonical Value", "Source", "Source Tier",
                       "URL", "Page Value", "Verdict", "Fix"]


def load_entries(audit_data_dir):
    entries = []
    for path in sorted(Path(audit_data_dir).glob("*.json")):
        try:
            data = json.loads(path.read_text())
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            print(f"skipping invalid audit json {path.name}: {exc}")
            continue
        errors = validate_audit_json(data)
        if errors:
            print(f"skipping invalid audit json {path.name}: {errors[:1]}")
            continue
        for e in data.get("ledger_entries", []):
            entries.append({**e, "url": data["url"]})
    return entries


def norm(value):
    return " ".join(str(value).lower().split())


def near_duplicate_keys(keys):
    """Pairs of fact keys whose kebab-token sets overlap >= 60% — merge candidates."""
    tokens = {k: set(k.split("-")) for k in keys}
    pairs = []
    for a, b in combinations(sorted(keys), 2):
        union = tokens[a] | tokens[b]
        if union and len(tokens[a] & tokens[b]) / len(union) >= 0.6:
            pairs.append((a, b))
    return pairs


def judge(group):
    """Classify one fact_key group.

    Returns (canonical_value, source, source_tier, rows) where each row is
    (url, page_value, verdict, fix) and verdict is one of:
    consistent | truth-violation | internal-disagreement | verified-source-conflict.
    """
    verified = [e for e in group if norm(e.get("verified_value", "")) not in ("", "n/a")]
    if verified:
        verified_values = {norm(e["verified_value"]) for e in verified}
        if len(verified_values) > 1:
            fix = ("Multiple verified sources disagree for this fact — resolve manually "
                   "before treating one as canonical.")
            return "", "", "", [(e["url"], e["page_value"], "verified-source-conflict", fix)
                                for e in group]
        counts = defaultdict(int)
        for e in verified:
            counts[norm(e["verified_value"])] += 1
        canonical_norm = max(counts, key=counts.get)
        best = next(e for e in verified if norm(e["verified_value"]) == canonical_norm)
        canonical, source, tier = best["verified_value"], best["source"], best["source_tier"]
        rows = []
        for e in group:
            if norm(e["page_value"]) == canonical_norm:
                rows.append((e["url"], e["page_value"], "consistent", ""))
            else:
                rows.append((e["url"], e["page_value"], "truth-violation",
                             f"Update to {canonical} (per {source})"))
        return canonical, source, tier, rows
    values = {norm(e["page_value"]) for e in group}
    if len(values) <= 1:
        return "", "", "", [(e["url"], e["page_value"], "consistent", "") for e in group]
    fix = ("Pages disagree and no external source arbitrates — pick one platform figure, "
           "attribute it, add an as-of date")
    return "", "", "", [(e["url"], e["page_value"], "internal-disagreement", fix)
                        for e in group]


def run(audit_data_dir, xlsx_path, result_dir, report_date=None):
    report_date = report_date or date.today().isoformat()
    entries = load_entries(audit_data_dir)
    if not entries:
        sys.exit(f"no ledger entries found under {audit_data_dir} — run Task 1 audits first")
    groups = defaultdict(list)
    for e in entries:
        groups[e["fact_key"]].append(e)
    merge_candidates = near_duplicate_keys(groups.keys())

    xlsx_path = Path(xlsx_path)
    wb = load_workbook(xlsx_path)
    if "Consistency" in wb.sheetnames:
        wb.remove(wb["Consistency"])
    ws = wb.create_sheet("Consistency")
    ws.append(CONSISTENCY_COLUMNS)

    lines = [f"# Travel Insurance Cross-Site Consistency Report — {report_date}", ""]
    if merge_candidates:
        lines += ["## ⚠️ Fact-key merge candidates (review, merge in JSONs, re-run)", ""]
        lines += [f"- `{a}` ↔ `{b}`" for a, b in merge_candidates] + [""]
    issue_count = 0
    for key in sorted(groups):
        canonical, source, tier, rows = judge(groups[key])
        for url, value, verdict, fix in rows:
            ws.append([key, canonical, source, tier, url, value, verdict, fix])
        flagged = [r for r in rows if r[2] != "consistent"]
        if not flagged:
            continue
        issue_count += len(flagged)
        lines += [f"## `{key}`", ""]
        if canonical:
            lines.append(f"**Canonical value:** {canonical} — {source} ({tier})")
        lines += ["", "| URL | Page value | Verdict | Fix |", "|---|---|---|---|"]
        lines += [f"| {url} | {value} | {verdict} | {fix} |"
                  for url, value, verdict, fix in flagged]
        lines.append("")
    lines.append(f"---\n\n**{issue_count} inconsistencies across {len(groups)} facts, "
                 f"{len(entries)} ledger entries.**")
    ws.auto_filter.ref = ws.dimensions

    report = Path(result_dir) / f"policybazaar-travel-consistency-report-{report_date}.md"
    report.write_text("\n".join(lines))
    tmp = xlsx_path.with_name(xlsx_path.name + ".tmp")
    wb.save(tmp)
    os.replace(tmp, xlsx_path)
    print(f"{issue_count} inconsistencies across {len(groups)} facts → {report}")
    return report


if __name__ == "__main__":
    from config import AUDIT_DATA_DIR, MASTER_XLSX, RESULT_DIR

    run(AUDIT_DATA_DIR, MASTER_XLSX, RESULT_DIR)
