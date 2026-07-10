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


def test_summary_stores_basename_not_full_path(tmp_path):
    state_csv, data_dir, xlsx, fact_keys = setup_run(tmp_path)
    data = sample_audit()
    data["md_file"] = "/some/absolute/path/policybazaar-health-insurance-content-audit-2026-07-07.md"
    (data_dir / "health-insurance.json").write_text(json.dumps(data))
    collect(state_csv, data_dir, xlsx, fact_keys)
    ws = load_workbook(xlsx)["Summary"]
    assert ws.cell(row=2, column=10).value == "policybazaar-health-insurance-content-audit-2026-07-07.md"


def test_rows_match_real_workbook_layout(tmp_path):
    state_csv, data_dir, xlsx, fact_keys = setup_run(tmp_path)
    collect(state_csv, data_dir, xlsx, fact_keys)
    wb = load_workbook(xlsx)
    url, day = sample_audit()["url"], sample_audit()["audit_date"]
    # Lens Scores: Status before Score; Score folded as "score/max"
    assert [c.value for c in wb["Lens Scores"][2]] == [
        url, day, "seo", "Title Tag", "warn", "8/10", "Title exceeds 60 chars"]
    # Fact-Check: source + audit date folded into the Correct Value cell
    assert wb["Fact-Check"].cell(row=2, column=5).value == f"AED 320 (DHA, {day})"
    # Schema: real workbook taxonomy from the new schema_audit fields
    assert [c.value for c in wb["Schema"][2]] == [
        url, day, "implemented", "FAQPage", "valid", "matches page", "8 Q-A pairs"]
    # Priority Recs: issue folded into the Action cell
    assert [c.value for c in wb["Priority Recs"][2]] == [
        url, day, "High", "meta → rewrite"]
    # Verification Ledger: global registry row
    assert [c.value for c in wb["Verification Ledger"][2]] == [
        "dha-ebp-annual-premium", "AED 320", "DHA", "Primary", url, day]


def test_shared_fact_key_appends_one_ledger_row(tmp_path):
    state_csv, data_dir, xlsx, fact_keys = setup_run(tmp_path)
    second = sample_audit()
    second["url"] = "https://www.policybazaar.ae/health-insurance/dubai/"
    second["slug"] = "dubai"
    rows = read_state(state_csv)
    extra = {field: "" for field in STATE_FIELDS}
    extra.update(url=second["url"], slug="dubai", tier="A-core",
                 page_type="core-page", status="in_progress")
    write_state(state_csv, rows + [extra])
    (data_dir / "dubai.json").write_text(json.dumps(second))
    done, failed = collect(state_csv, data_dir, xlsx, fact_keys)
    assert len(done) == 2 and failed == []
    ledger = load_workbook(xlsx)["Verification Ledger"]
    assert ledger.max_row == 2  # header + exactly one row for the shared fact_key


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


def test_corrupt_json_fails_its_row_without_poisoning_the_batch(tmp_path):
    state_csv, data_dir, xlsx, fact_keys = setup_run(tmp_path)
    second = sample_audit()
    second["url"] = "https://www.policybazaar.ae/health-insurance/dubai/"
    second["slug"] = "dubai"
    rows = read_state(state_csv)
    extra = {field: "" for field in STATE_FIELDS}
    extra.update(url=second["url"], slug="dubai", tier="A-core",
                 page_type="core-page", status="in_progress")
    write_state(state_csv, rows + [extra])
    (data_dir / "dubai.json").write_text(json.dumps(second))
    (data_dir / "health-insurance.json").write_text('{"truncated": ')
    done, failed = collect(state_csv, data_dir, xlsx, fact_keys)
    assert len(done) == 1 and len(failed) == 1
    by_slug = {r["slug"]: r for r in read_state(state_csv)}
    assert by_slug["dubai"]["status"] == "done"
    assert by_slug["health-insurance"]["status"] == "failed"
    assert "corrupt json" in by_slug["health-insurance"]["failure_reason"]


def test_ledger_dedupes_across_separate_collect_runs(tmp_path):
    state_csv, data_dir, xlsx, fact_keys = setup_run(tmp_path)
    collect(state_csv, data_dir, xlsx, fact_keys)  # first batch commits the fact_key
    second = sample_audit()
    second["url"] = "https://www.policybazaar.ae/health-insurance/dubai/"
    second["slug"] = "dubai"
    rows = read_state(state_csv)
    extra = {field: "" for field in STATE_FIELDS}
    extra.update(url=second["url"], slug="dubai", tier="A-core",
                 page_type="core-page", status="in_progress")
    write_state(state_csv, rows + [extra])
    (data_dir / "dubai.json").write_text(json.dumps(second))
    done, failed = collect(state_csv, data_dir, xlsx, fact_keys)  # second batch, same fact_key
    assert done and not failed
    ledger = load_workbook(xlsx)["Verification Ledger"]
    assert ledger.max_row == 2  # header + one row — fact_key already registered


def test_interlink_rows_land_in_interlinks_sheet(tmp_path):
    state_csv, data_dir, xlsx, fact_keys = setup_run(tmp_path)
    collect(state_csv, data_dir, xlsx, fact_keys)
    ws = load_workbook(xlsx)["Interlinks"]
    url, day = sample_audit()["url"], sample_audit()["audit_date"]
    assert [c.value for c in ws[2]] == [
        url, day, "outbound", "https://www.policybazaar.ae/health-insurance/dubai/",
        "health insurance in Dubai", "Coverage by emirate section",
        "page discusses Dubai mandates but never links the Dubai hub",
        "verified-target"]


def test_legacy_json_without_interlinks_key_still_collects(tmp_path):
    state_csv, data_dir, xlsx, fact_keys = setup_run(tmp_path)
    data = sample_audit()
    del data["interlink_opportunities"]
    (data_dir / "health-insurance.json").write_text(json.dumps(data))
    done, failed = collect(state_csv, data_dir, xlsx, fact_keys)
    assert len(done) == 1 and failed == []
    assert load_workbook(xlsx)["Interlinks"].max_row == 1  # header only


def test_legacy_workbook_gains_interlinks_sheet(tmp_path):
    state_csv, data_dir, xlsx, fact_keys = setup_run(tmp_path)
    from openpyxl import Workbook
    wb = Workbook()
    wb.remove(wb.active)
    for name, cols in SHEET_COLUMNS.items():
        if name == "Interlinks":
            continue  # simulate a workbook created before the sheet existed
        wb.create_sheet(name).append(cols)
    wb.save(xlsx)
    done, failed = collect(state_csv, data_dir, xlsx, fact_keys)
    assert len(done) == 1 and failed == []
    ws = load_workbook(xlsx)["Interlinks"]
    assert [c.value for c in ws[1]] == SHEET_COLUMNS["Interlinks"]
    assert ws.max_row == 2  # header + the audit's interlink row


def test_header_mismatch_exits_loudly_before_any_append(tmp_path):
    import pytest
    state_csv, data_dir, xlsx, fact_keys = setup_run(tmp_path)
    from openpyxl import Workbook
    wb = Workbook()
    wb.remove(wb.active)
    for name, cols in SHEET_COLUMNS.items():
        wb.create_sheet(name).append(cols)
    wb["Summary"].cell(row=1, column=8).value = "WRONG"
    wb.save(xlsx)
    with pytest.raises(SystemExit):
        collect(state_csv, data_dir, xlsx, fact_keys)
