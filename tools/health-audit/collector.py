"""Serial collector: append validated audit JSONs to the master workbook, update state."""
import json
import os
import sys
from pathlib import Path

from openpyxl import Workbook, load_workbook

from schema import validate_audit_json
from state import read_state, write_state

SHEET_COLUMNS = {
    "Summary": ["URL", "Audit Date", "SEO", "GEO", "Human-Likeness", "YMYL",
                "Fact-Check", "OVERALL", "Rating", "Detailed Report (.md)"],
    "Lens Scores": ["URL", "Audit Date", "Lens", "Parameter", "Status", "Score",
                    "Finding"],
    "Findings": ["URL", "Audit Date", "Lens", "Severity", "Found", "Why", "Fix"],
    "Fact-Check": ["URL", "Audit Date", "Claim", "Verification",
                   "Correct Value (source, date)", "Source Tier", "Status", "Fix"],
    "Schema": ["URL", "Audit Date", "Row Type", "@type / Severity", "Parse",
               "Parity", "Detail"],
    "Priority Recs": ["URL", "Audit Date", "Priority", "Action"],
    "Verification Ledger": ["Figure", "Value", "Source", "Tier",
                            "First Verified For", "Date"],
}
SCORE_FIELDS = ("seo", "geo", "human_likeness", "ymyl", "fact_check", "overall")


def rating(overall):
    if overall >= 85:
        return "🟢 Publish-ready"
    if overall >= 70:
        return "🟡 Minor fixes"
    if overall >= 55:
        return "🟠 Needs work"
    return "🔴 Major rework"


def fold_correct_value(c, day):
    """Real workbook folds source+date into the Correct Value cell."""
    if c["correct_value"] == "n/a" or not c["source"]:
        return c["correct_value"]
    return f"{c['correct_value']} ({c['source']}, {day})"


def rows_for(d):
    """Per-audit rows for every sheet except Verification Ledger (global registry)."""
    url, day, s = d["url"], d["audit_date"], d["scores"]
    return {
        "Summary": [[url, day, s["seo"], s["geo"], s["human_likeness"], s["ymyl"],
                     s["fact_check"], s["overall"], rating(s["overall"]), d["md_file"]]],
        "Lens Scores": [[url, day, p["lens"], p["name"], p["status"],
                         f"{p['score']}/{p['max']}", p["finding"]]
                        for p in d["parameters"]],
        "Findings": [[url, day, f["lens"], f["severity"], f["found"], f["why"],
                      f["fix"]] for f in d["findings"]],
        "Fact-Check": [[url, day, c["claim"], c["verification"],
                        fold_correct_value(c, day), c["source_tier"], c["status"],
                        c["fix"]] for c in d["fact_checks"]],
        "Schema": [[url, day, i["row_type"], i["type_or_severity"], i["parse"],
                    i["parity"], i["detail"]] for i in d["schema_audit"]],
        "Priority Recs": [[url, day, r["priority"], f"{r['issue']} → {r['action']}"]
                          for r in d["priority_recs"]],
    }


def ledger_rows(d, known_figures):
    """Verification Ledger is a global unique-fact registry: one row per fact_key.

    Appends only verified facts (verified_value not empty/"n/a") whose fact_key is
    not already in the Figure column; mutates known_figures so a single batch
    cannot append duplicates. Per-page values stay in the audit JSONs — the
    consistency engine reads those, not this sheet.
    """
    rows = []
    for e in d["ledger_entries"]:
        if e["verified_value"] in ("", "n/a") or e["fact_key"] in known_figures:
            continue
        known_figures.add(e["fact_key"])
        rows.append([e["fact_key"], e["verified_value"], e["source"],
                     e["source_tier"], d["url"], d["audit_date"]])
    return rows


def ensure_workbook(path):
    if path.exists():
        wb = load_workbook(path)
        for name, cols in SHEET_COLUMNS.items():
            if name not in wb.sheetnames:
                sys.exit(f"master workbook {path} is missing sheet {name!r} — "
                         "align SHEET_COLUMNS with the existing workbook before collecting")
            header = [c.value for c in wb[name][1]]
            if header != cols:
                sys.exit(f"sheet {name!r} header mismatch:\n  workbook: {header}\n"
                         f"  expected: {cols}")
        return wb
    wb = Workbook()
    wb.remove(wb.active)
    for name, cols in SHEET_COLUMNS.items():
        wb.create_sheet(name).append(cols)
    return wb


def update_fact_keys(fact_keys_md, datas):
    """Update fact-keys.md with new fact_keys from ledger_entries.

    fact-keys.md is the SEEN-keys registry for agent key reuse (includes all facts,
    verified and unverified, by design). The Verification Ledger sheet holds only
    verified facts. This function records every fact_key encountered so future runs
    can deduplicate across batches.
    """
    known = set()
    if fact_keys_md.exists():
        known = {line.split("`")[1] for line in fact_keys_md.read_text().splitlines()
                 if line.count("`") >= 2}
    new_lines = []
    for d in datas:
        for e in d["ledger_entries"]:
            if e["fact_key"] not in known:
                known.add(e["fact_key"])
                new_lines.append(f"- `{e['fact_key']}` — first seen: {d['url']}")
    if new_lines:
        with fact_keys_md.open("a") as fh:
            fh.write("\n".join(new_lines) + "\n")


def collect(state_csv, audit_data_dir, xlsx_path, fact_keys_md, dry_run=False):
    audit_data_dir, xlsx_path = Path(audit_data_dir), Path(xlsx_path)
    rows = read_state(state_csv)
    wb = ensure_workbook(xlsx_path)
    ledger_ws = wb["Verification Ledger"]
    known_figures = {r[0] for r in ledger_ws.iter_rows(min_row=2, values_only=True)
                     if r and r[0]}
    done, failed, ingested = [], [], []
    for row in rows:
        if row["status"] != "in_progress":
            continue
        json_path = audit_data_dir / f"{row['slug']}.json"
        if not json_path.exists():
            continue  # agent still running or died before writing — reset-stale handles it
        try:
            data = json.loads(json_path.read_text())
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            row.update(status="failed",
                       failure_reason=f"corrupt json {json_path.name}: {exc}")
            failed.append(row["url"])
            continue
        errors = validate_audit_json(data)
        if errors:
            row.update(status="failed",
                       failure_reason="invalid json: " + "; ".join(errors[:3]))
            failed.append(row["url"])
            continue
        for sheet, sheet_rows in rows_for(data).items():
            ws = wb[sheet]
            for r in sheet_rows:
                ws.append(r)
            ws.auto_filter.ref = ws.dimensions
        new_ledger = ledger_rows(data, known_figures)
        if new_ledger:
            for r in new_ledger:
                ledger_ws.append(r)
            ledger_ws.auto_filter.ref = ledger_ws.dimensions
        row.update(status="done", audit_date=data["audit_date"],
                   md_file=data["md_file"], json_file=json_path.name,
                   **{k: str(data["scores"][k]) for k in SCORE_FIELDS})
        done.append(row["url"])
        ingested.append(data)
    if dry_run:
        print(f"dry-run: would append {len(done)} audits, mark {len(failed)} failed")
        return done, failed
    tmp = xlsx_path.with_name(xlsx_path.name + ".tmp")
    wb.save(tmp)
    os.replace(tmp, xlsx_path)
    update_fact_keys(Path(fact_keys_md), ingested)
    write_state(state_csv, rows)
    print(f"collected {len(done)} audits, {len(failed)} invalid → {xlsx_path}")
    return done, failed


if __name__ == "__main__":
    from config import AUDIT_DATA_DIR, FACT_KEYS_MD, MASTER_XLSX, STATE_CSV

    collect(STATE_CSV, AUDIT_DATA_DIR, MASTER_XLSX, FACT_KEYS_MD,
            dry_run="--dry-run" in sys.argv)
