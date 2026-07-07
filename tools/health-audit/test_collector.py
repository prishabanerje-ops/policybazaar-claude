import json

from openpyxl import load_workbook

from collector import SHEET_COLUMNS, collect, rating
from filter_urls import STATE_FIELDS
from state import read_state, write_state
from test_schema import sample_audit


def setup_run(tmp_path):
    state_csv = tmp_path / "state.csv"
    data_dir = tmp_path / "audit-data"
    data_dir.mkdir()
    xlsx = tmp_path / "master.xlsx"
    fact_keys = data_dir / "fact-keys.md"
    row = {field: "" for field in STATE_FIELDS}
    row.update(url=sample_audit()["url"], slug="health-insurance", tier="A-core",
               page_type="core-page", status="in_progress")
    write_state(state_csv, [row])
    (data_dir / "health-insurance.json").write_text(json.dumps(sample_audit()))
    return state_csv, data_dir, xlsx, fact_keys


def test_rating_thresholds():
    assert rating(90).endswith("Publish-ready")
    assert rating(70).endswith("Minor fixes")
    assert rating(55).endswith("Needs work")
    assert rating(54).endswith("Major rework")


def test_collect_appends_all_sheets_and_marks_done(tmp_path):
    state_csv, data_dir, xlsx, fact_keys = setup_run(tmp_path)
    done, failed = collect(state_csv, data_dir, xlsx, fact_keys)
    assert len(done) == 1 and failed == []
    wb = load_workbook(xlsx)
    assert set(wb.sheetnames) == set(SHEET_COLUMNS)
    assert wb["Summary"].max_row == 2  # header + one audit
    row = read_state(state_csv)[0]
    assert row["status"] == "done"
    assert row["overall"] == "69"
    assert "dha-ebp-annual-premium" in fact_keys.read_text()


def test_second_collect_run_is_a_noop(tmp_path):
    state_csv, data_dir, xlsx, fact_keys = setup_run(tmp_path)
    collect(state_csv, data_dir, xlsx, fact_keys)
    done, failed = collect(state_csv, data_dir, xlsx, fact_keys)
    assert done == [] and failed == []
    assert load_workbook(xlsx)["Summary"].max_row == 2  # no duplicate rows


def test_invalid_json_marks_row_failed_not_appended(tmp_path):
    state_csv, data_dir, xlsx, fact_keys = setup_run(tmp_path)
    (data_dir / "health-insurance.json").write_text(json.dumps({"url": "x"}))
    done, failed = collect(state_csv, data_dir, xlsx, fact_keys)
    assert done == [] and len(failed) == 1
    row = read_state(state_csv)[0]
    assert row["status"] == "failed"
    assert "invalid json" in row["failure_reason"]


def test_dry_run_writes_nothing(tmp_path):
    state_csv, data_dir, xlsx, fact_keys = setup_run(tmp_path)
    collect(state_csv, data_dir, xlsx, fact_keys, dry_run=True)
    assert not xlsx.exists()
    assert read_state(state_csv)[0]["status"] == "in_progress"
