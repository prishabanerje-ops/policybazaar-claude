# tools/health-audit/test_consistency.py
import json

from openpyxl import Workbook, load_workbook

from consistency import judge, near_duplicate_keys, run


def entry(url, page_value, verified_value="", status="Unverifiable",
          key="dubai-ebp-annual-premium"):
    return {"fact_key": key, "page_value": page_value, "verified_value": verified_value,
            "source": "DHA" if verified_value else "", "source_tier": "Primary",
            "status": status, "url": url}


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
    base = {"parameters": [], "findings": [], "fact_checks": [],
            "schema_audit": [], "priority_recs": []}
    (data_dir / "a.json").write_text(json.dumps({**base, "url": "u1", "ledger_entries": [
        entry("u1", "AED 320", "AED 320", "Confirmed")]}))
    (data_dir / "b.json").write_text(json.dumps({**base, "url": "u2", "ledger_entries": [
        entry("u2", "AED 350", "AED 320", "Contradicted")]}))
    xlsx = tmp_path / "master.xlsx"
    wb = Workbook(); wb.save(xlsx)
    report = run(data_dir, xlsx, tmp_path, report_date="2026-08-01")
    assert "truth-violation" in report.read_text()
    ws = load_workbook(xlsx)["Consistency"]
    assert ws.max_row == 3  # header + two entries
