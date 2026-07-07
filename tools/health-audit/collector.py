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
    "Lens Scores": ["URL", "Audit Date", "Lens", "Parameter", "Score", "Max",
                    "Status", "Finding"],
    "Findings": ["URL", "Audit Date", "Lens", "Severity", "Found", "Why", "Fix"],
    "Fact-Check": ["URL", "Audit Date", "Claim", "Verification", "Correct Value",
                   "Source", "Source Tier", "Status", "Fix"],
    "Schema": ["URL", "Audit Date", "Item", "Status", "Finding"],
    "Priority Recs": ["URL", "Audit Date", "Priority", "Issue", "Action"],
    "Verification Ledger": ["Fact Key", "Page Value", "Verified Value", "Source",
                            "Source Tier", "Status", "URL", "Audit Date"],
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


def rows_for(d):
    url, day, s = d["url"], d["audit_date"], d["scores"]
    return {
        "Summary": [[url, day, s["seo"], s["geo"], s["human_likeness"], s["ymyl"],
                     s["fact_check"], s["overall"], rating(s["overall"]), d["md_file"]]],
        "Lens Scores": [[url, day, p["lens"], p["name"], p["score"], p["max"],
                         p["status"], p["finding"]] for p in d["parameters"]],
        "Findings": [[url, day, f["lens"], f["severity"], f["found"], f["why"],
                      f["fix"]] for f in d["findings"]],
        "Fact-Check": [[url, day, c["claim"], c["verification"], c["correct_value"],
                        c["source"], c["source_tier"], c["status"], c["fix"]]
                       for c in d["fact_checks"]],
        "Schema": [[url, day, i["item"], i["status"], i["finding"]]
                   for i in d["schema_audit"]],
        "Priority Recs": [[url, day, r["priority"], r["issue"], r["action"]]
                          for r in d["priority_recs"]],
        "Verification Ledger": [[e["fact_key"], e["page_value"], e["verified_value"],
                                 e["source"], e["source_tier"], e["status"], url, day]
                                for e in d["ledger_entries"]],
    }


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
    done, failed, ingested = [], [], []
    for row in rows:
        if row["status"] != "in_progress":
            continue
        json_path = audit_data_dir / f"{row['slug']}.json"
        if not json_path.exists():
            continue  # agent still running or died before writing — reset-stale handles it
        data = json.loads(json_path.read_text())
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
