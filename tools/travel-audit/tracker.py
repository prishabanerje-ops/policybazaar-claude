"""Generate the human-facing Excel tracker from audit-state.csv.

This file is a GENERATED VIEW, not a second source of truth. audit-state.csv
(driven by state.py) remains authoritative. Run this after every collector.py
pass (or any time) to refresh the tracker — it always fully rewrites the sheet
from current state, so any manual edits made directly in the tracker xlsx will
be lost on the next run. Edit progress via the pipeline (state.py/collector.py),
never by hand in the tracker.
"""
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter

from state import read_state

TRACKER_COLUMNS = [
    "URL", "Slug", "Page Type", "Tier", "Status", "Audit Date",
    "Overall Score", "Report File", "Batch ID", "Failure Reason",
]

STATUS_LABELS = {
    "pending": "⬜ Pending",
    "in_progress": "🔄 In Progress",
    "done": "✅ Done",
    "failed": "❌ Failed",
}

STATUS_FILL = {
    "pending": PatternFill(fill_type="solid", fgColor="FFF2F2F2"),
    "in_progress": PatternFill(fill_type="solid", fgColor="FFFFF3CD"),
    "done": PatternFill(fill_type="solid", fgColor="FFD4EDDA"),
    "failed": PatternFill(fill_type="solid", fgColor="FFF8D7DA"),
}


def tracker_row(row):
    return [
        row["url"], row["slug"], row["page_type"], row["tier"],
        STATUS_LABELS.get(row["status"], row["status"]),
        row["audit_date"] or "", row["overall"] or "",
        row["md_file"] or "", row["batch_id"] or "", row["failure_reason"] or "",
    ]


def build_tracker(rows, vertical_label):
    wb = Workbook()

    ws = wb.active
    ws.title = "Tracker"
    ws.append(TRACKER_COLUMNS)
    for cell in ws[1]:
        cell.font = Font(bold=True)
    for row in rows:
        ws.append(tracker_row(row))
        fill = STATUS_FILL.get(row["status"])
        if fill:
            ws.cell(row=ws.max_row, column=5).fill = fill
    ws.auto_filter.ref = ws.dimensions
    ws.freeze_panes = "A2"
    widths = [60, 26, 16, 10, 16, 13, 14, 46, 20, 30]
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

    summary = wb.create_sheet("Summary")
    total = len(rows)
    done = sum(1 for r in rows if r["status"] == "done")
    failed = sum(1 for r in rows if r["status"] == "failed")
    in_progress = sum(1 for r in rows if r["status"] == "in_progress")
    pending = sum(1 for r in rows if r["status"] == "pending")
    pct = round(100 * done / total, 1) if total else 0.0

    summary.append([f"{vertical_label} — Audit Progress"])
    summary["A1"].font = Font(bold=True, size=14)
    summary.append([])
    summary.append(["Total URLs", total])
    summary.append(["Done", done])
    summary.append(["In Progress", in_progress])
    summary.append(["Pending", pending])
    summary.append(["Failed", failed])
    summary.append(["% Complete", f"{pct}%"])
    summary.append([])
    summary.append(["By Tier", "Total", "Done", "Pending", "In Progress", "Failed"])
    for cell in summary[summary.max_row]:
        cell.font = Font(bold=True)
    tiers = sorted({r["tier"] for r in rows})
    for tier in tiers:
        tier_rows = [r for r in rows if r["tier"] == tier]
        summary.append([
            tier, len(tier_rows),
            sum(1 for r in tier_rows if r["status"] == "done"),
            sum(1 for r in tier_rows if r["status"] == "pending"),
            sum(1 for r in tier_rows if r["status"] == "in_progress"),
            sum(1 for r in tier_rows if r["status"] == "failed"),
        ])
    for col, w in zip("ABCDEF", [14, 10, 8, 10, 12, 8]):
        summary.column_dimensions[col].width = w

    return wb


def main(state_csv, out_path, vertical_label):
    rows = read_state(state_csv)
    wb = build_tracker(rows, vertical_label)
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = out_path.with_name(out_path.name + ".tmp")
    wb.save(tmp)
    tmp.replace(out_path)
    done = sum(1 for r in rows if r["status"] == "done")
    print(f"wrote {len(rows)} rows ({done} done) → {out_path}")


if __name__ == "__main__":
    from config import STATE_CSV, TRACKER_XLSX, VERTICAL_LABEL

    main(STATE_CSV, TRACKER_XLSX, VERTICAL_LABEL)
