# tools/health-audit/test_consistency.py
import json

from openpyxl import Workbook, load_workbook

from consistency import judge, near_duplicate_keys, run


def entry(url, page_value, verified_value="", status="Unverifiable",
          key="dubai-ebp-annual-premium"):
    return {"fact_key": key, "page_value": page_value, "verified_value": verified_value,
            "source": "DHA" if verified_value else "", "source_tier": "Primary",
            "status": status, "url": url}


def audit_json(url, ledger_entries):
    """Minimal but schema-valid audit JSON payload (see schema.TOP_KEYS)."""
    return {
        "url": url, "slug": url, "page_type": "page", "tier": "1",
        "audit_date": "2026-08-01", "mode": "full", "md_file": f"{url}.md",
        "scores": {"seo": 80, "geo": 80, "human_likeness": 80, "ymyl": 80,
                   "fact_check": 80, "overall": 80},
        "parameters": [], "findings": [], "fact_checks": [],
        "ledger_entries": ledger_entries, "schema_audit": [], "priority_recs": [],
    }


def test_truth_violation_when_page_contradicts_verified_value():
    group = [entry("u1", "AED 320", "AED 320", "Confirmed"),
             entry("u2", "AED 350", "AED 320", "Contradicted")]
    canonical, source, tier, rows = judge(group)
    assert canonical == "AED 320"
    verdicts = {url: verdict for url, _, verdict, _ in rows}
    assert verdicts == {"u1": "consistent", "u2": "truth-violation"}


def test_internal_disagreement_when_unverifiable_values_differ():
    group = [entry("u1", "AED 500"), entry("u2", "AED 600")]
    canonical, _, _, rows = judge(group)
    assert canonical == ""
    assert all(verdict == "internal-disagreement" for _, _, verdict, _ in rows)


def test_matching_unverifiable_values_are_consistent():
    group = [entry("u1", "AED 500"), entry("u2", "aed 500")]
    _, _, _, rows = judge(group)
    assert all(verdict == "consistent" for _, _, verdict, _ in rows)


def test_near_duplicate_keys_flags_overlapping_token_sets():
    pairs = near_duplicate_keys(["dubai-ebp-annual-premium", "dubai-ebp-yearly-premium",
                                 "abu-dhabi-fine-monthly"])
    assert pairs == [("dubai-ebp-annual-premium", "dubai-ebp-yearly-premium")]


def test_run_writes_report_and_consistency_sheet(tmp_path):
    data_dir = tmp_path / "audit-data"
    data_dir.mkdir()
    (data_dir / "a.json").write_text(json.dumps(audit_json("u1", [
        entry("u1", "AED 320", "AED 320", "Confirmed")])))
    (data_dir / "b.json").write_text(json.dumps(audit_json("u2", [
        entry("u2", "AED 350", "AED 320", "Contradicted")])))
    xlsx = tmp_path / "master.xlsx"
    wb = Workbook(); wb.save(xlsx)
    report = run(data_dir, xlsx, tmp_path, report_date="2026-08-01")
    assert "truth-violation" in report.read_text()
    ws = load_workbook(xlsx)["Consistency"]
    assert ws.max_row == 3  # header + two entries


def test_verified_source_conflict_when_sources_disagree():
    group = [entry("u1", "AED 320", "AED 320", "Confirmed"),
             entry("u2", "AED 350", "AED 999", "Confirmed")]
    canonical, source, tier, rows = judge(group)
    assert canonical == "" and source == "" and tier == ""
    assert all(verdict == "verified-source-conflict" for _, _, verdict, _ in rows)
    assert {url for url, _, _, _ in rows} == {"u1", "u2"}


def test_run_twice_does_not_duplicate_consistency_rows(tmp_path):
    data_dir = tmp_path / "audit-data"
    data_dir.mkdir()
    (data_dir / "a.json").write_text(json.dumps(audit_json("u1", [
        entry("u1", "AED 320", "AED 320", "Confirmed")])))
    (data_dir / "b.json").write_text(json.dumps(audit_json("u2", [
        entry("u2", "AED 350", "AED 320", "Contradicted")])))
    xlsx = tmp_path / "master.xlsx"
    wb = Workbook(); wb.save(xlsx)
    run(data_dir, xlsx, tmp_path, report_date="2026-08-01")
    first_count = load_workbook(xlsx)["Consistency"].max_row
    run(data_dir, xlsx, tmp_path, report_date="2026-08-01")
    second_count = load_workbook(xlsx)["Consistency"].max_row
    assert second_count == first_count == 3  # header + two entries, not doubled


def test_run_skips_invalid_audit_json(tmp_path):
    data_dir = tmp_path / "audit-data"
    data_dir.mkdir()
    (data_dir / "valid.json").write_text(json.dumps(audit_json("u1", [
        entry("u1", "AED 320", "AED 320", "Confirmed")])))
    (data_dir / "invalid.json").write_text(json.dumps({"url": "u2"}))  # missing required keys
    xlsx = tmp_path / "master.xlsx"
    wb = Workbook(); wb.save(xlsx)
    report = run(data_dir, xlsx, tmp_path, report_date="2026-08-01")
    ws = load_workbook(xlsx)["Consistency"]
    assert ws.max_row == 2  # header + entry from the valid file only
    assert "u2" not in report.read_text()
