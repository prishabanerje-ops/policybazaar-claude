import json

from openpyxl import load_workbook

from filter_urls import STATE_FIELDS
from state import write_state
from tracker import STATUS_LABELS, build_tracker, main


def row(**over):
    r = {field: "" for field in STATE_FIELDS}
    r.update(url="https://www.policybazaar.ae/health-insurance/dubai/",
             slug="dubai", page_type="core-page", tier="A-core", status="pending")
    r.update(over)
    return r


def test_tracker_sheet_has_one_row_per_state_row():
    rows = [row(), row(url="https://www.policybazaar.ae/health-insurance/abu-dhabi/",
                       slug="abu-dhabi", status="done", overall="82",
                       audit_date="2026-07-10",
                       md_file="policybazaar-abu-dhabi-content-audit-2026-07-10.md")]
    wb = build_tracker(rows, "Health Insurance")
    ws = wb["Tracker"]
    assert ws.max_row == 3  # header + 2 rows
    assert ws.cell(row=1, column=1).value == "URL"
    done_row = [c.value for c in ws[3]]
    assert done_row[0] == "https://www.policybazaar.ae/health-insurance/abu-dhabi/"
    assert done_row[4] == STATUS_LABELS["done"]
    assert done_row[6] == "82"
    assert done_row[7] == "policybazaar-abu-dhabi-content-audit-2026-07-10.md"


def test_status_labels_are_human_readable():
    for status in ("pending", "in_progress", "done", "failed"):
        assert row(status=status)["status"] == status  # sanity on fixture
    wb = build_tracker([row(status=s) for s in
                        ("pending", "in_progress", "done", "failed")], "X")
    ws = wb["Tracker"]
    labels = [ws.cell(row=r, column=5).value for r in range(2, 6)]
    assert labels == ["⬜ Pending", "🔄 In Progress", "✅ Done", "❌ Failed"]


def test_summary_sheet_counts_match_state():
    rows = [row(status="done"), row(status="done"), row(status="pending"),
            row(status="failed"), row(status="in_progress")]
    wb = build_tracker(rows, "Health Insurance")
    summary = wb["Summary"]
    values = {summary.cell(row=r, column=1).value: summary.cell(row=r, column=2).value
              for r in range(3, 9)}
    assert values["Total URLs"] == 5
    assert values["Done"] == 2
    assert values["Pending"] == 1
    assert values["Failed"] == 1
    assert values["In Progress"] == 1
    assert values["% Complete"] == "40.0%"


def test_summary_breaks_down_by_tier():
    rows = [row(tier="A-core", status="done"), row(tier="A-core", status="pending"),
            row(tier="B", status="pending")]
    wb = build_tracker(rows, "Health Insurance")
    summary = wb["Summary"]
    header_row = next(r for r in range(1, summary.max_row + 1)
                       if summary.cell(row=r, column=1).value == "By Tier")
    tier_rows = {summary.cell(row=r, column=1).value:
                 [summary.cell(row=r, column=c).value for c in range(2, 7)]
                 for r in range(header_row + 1, summary.max_row + 1)}
    assert tier_rows["A-core"][0] == 2  # total
    assert tier_rows["A-core"][1] == 1  # done
    assert tier_rows["B"][0] == 1


def test_main_writes_file_and_replaces_existing(tmp_path):
    state_csv = tmp_path / "state.csv"
    write_state(state_csv, [row(status="done", overall="70")])
    out = tmp_path / "sub" / "tracker.xlsx"
    main(state_csv, out, "Health Insurance")
    assert out.exists()
    wb = load_workbook(out)
    assert wb["Tracker"].max_row == 2
    # second run overwrites cleanly, no leftover .tmp
    write_state(state_csv, [row(status="done"), row(slug="second", status="pending")])
    main(state_csv, out, "Health Insurance")
    assert load_workbook(out)["Tracker"].max_row == 3
    assert not out.with_name(out.name + ".tmp").exists()
