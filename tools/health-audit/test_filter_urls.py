# tools/health-audit/test_filter_urls.py
import pytest

from filter_urls import STATE_FIELDS, build_rows, classify, make_slug

BASE = "https://www.policybazaar.ae"


def test_arabic_pages_are_out_of_scope():
    assert classify(f"{BASE}/ar-ae/adamjee-health-insurance-hipvd/") is None


def test_bare_hic_substring_does_not_match():
    # "which" and "vehicles" contain "hic" — the raw regex's false positives
    assert classify(f"{BASE}/a-joint-term-plan-which-is-better-trmart/") is None
    assert classify(f"{BASE}/non-gcc-vehicles-affect-car-insurance-premium/") is None


def test_each_suffix_maps_to_its_type_and_tier():
    assert classify(f"{BASE}/adamjee-health-insurance-hipvd/") == ("provider", "A-core")
    assert classify(f"{BASE}/age-limit-for-health-insurance-hiart/") == ("article", "A-articles")
    assert classify(f"{BASE}/family-health-insurance-hic/") == ("category", "A-core")
    assert classify(f"{BASE}/aster-hospital-hinh/") == ("hospital-listing", "B")
    assert classify(f"{BASE}/adamjee-insurance-claim-form-hicf/") == ("claim-form", "B")


def test_health_insurance_subfolders_map_to_tiers():
    assert classify(f"{BASE}/health-insurance/articles/top-10/") == ("article", "A-articles")
    assert classify(f"{BASE}/health-insurance/hospitals/aster-clinic/") == ("hospital-listing", "B")
    assert classify(f"{BASE}/health-insurance/glossary/copayment/") == ("glossary", "B")
    assert classify(f"{BASE}/health-insurance/news-and-update/x/") == ("news", "B")
    assert classify(f"{BASE}/health-insurance/tpa/nas/") == ("tpa", "A-core")
    assert classify(f"{BASE}/health-insurance/health-guide/diabetes/") == ("health-guide", "A-core")
    assert classify(f"{BASE}/network-hospitals/dubai/") == ("hospital-listing", "B")
    assert classify(f"{BASE}/health-insurance/dubai/") == ("core-page", "A-core")


def test_slug_is_last_segment_and_collisions_get_section_prefix():
    taken = set()
    a = make_slug(f"{BASE}/health-insurance/articles/waiting-period/", taken)
    taken.add(a)
    b = make_slug(f"{BASE}/health-insurance/glossary/waiting-period/", taken)
    assert a == "waiting-period"
    assert b == "glossary-waiting-period"


def test_build_rows_dedupes_and_marks_pending():
    url = f"{BASE}/family-health-insurance-hic/"
    rows = build_rows([url, url, f"{BASE}/ar-ae/family-health-insurance-hic/"])
    assert len(rows) == 1
    assert rows[0]["status"] == "pending"
    assert rows[0]["slug"] == "family-health-insurance-hic"


def test_main_refuses_to_overwrite_existing_state(tmp_path, monkeypatch):
    import filter_urls
    state = tmp_path / "audit-state.csv"
    state.write_text("existing")
    monkeypatch.setattr(filter_urls, "STATE_CSV", state)
    monkeypatch.setattr(filter_urls, "URLS_TXT", tmp_path / "urls.txt")
    with pytest.raises(SystemExit):
        filter_urls.main(force=False)
    assert state.read_text() == "existing"


def test_main_force_rebuilds_existing_state(tmp_path, monkeypatch):
    import filter_urls
    state = tmp_path / "audit-state.csv"
    state.write_text("existing")
    urls = tmp_path / "urls.txt"
    urls.write_text("https://www.policybazaar.ae/family-health-insurance-hic/\n")
    monkeypatch.setattr(filter_urls, "STATE_CSV", state)
    monkeypatch.setattr(filter_urls, "URLS_TXT", urls)
    filter_urls.main(force=True)
    assert "family-health-insurance-hic" in state.read_text()


def test_state_fields_interface_is_stable():
    assert len(STATE_FIELDS) == 16
    assert STATE_FIELDS[0] == "url" and STATE_FIELDS[4] == "status"
