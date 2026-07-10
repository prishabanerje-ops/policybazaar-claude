# tools/travel-audit/test_filter_urls.py
import pytest

from filter_urls import STATE_FIELDS, build_rows, classify, make_slug

BASE = "https://www.policybazaar.ae"


def test_arabic_pages_are_out_of_scope():
    assert classify(f"{BASE}/ar-ae/travel-insurance/") is None


def test_confirmed_exclusions_are_out_of_scope():
    assert classify(f"{BASE}/fifty-national-day-uae/") is None
    assert classify(f"{BASE}/ceo-blog/how-insurance-can-help-retain-the-best-talent-in-uae/") is None


def test_each_suffix_maps_to_its_type_and_tier():
    assert classify(f"{BASE}/axa-travel-insurance-tipvd/") == ("provider", "A-core")
    assert classify(f"{BASE}/schengen-travel-insurance-tic/") == ("category", "A-core")


def test_travel_insurance_subfolders_map_to_tiers():
    assert classify(f"{BASE}/travel-insurance/articles/france-schengen-visa/") == ("article", "A-articles")
    assert classify(f"{BASE}/travel-insurance/news-and-update/umrah-insurance/") == ("news", "B")
    assert classify(f"{BASE}/news-and-update/holiday-list-uae/") == ("news", "B")
    assert classify(f"{BASE}/podcast/travel-insurance-a-true-need-or-a-hoax/") == ("podcast", "B")
    assert classify(f"{BASE}/insurance-companies/allianz-travel-insurance/") == ("provider", "A-core")
    assert classify(f"{BASE}/travel-insurance-calculator-uae/") == ("calculator", "A-core")
    assert classify(f"{BASE}/travel-insurance-by-destination/") == ("destination-hub", "A-core")


def test_core_destination_and_visa_pages_are_a_core():
    # Confirmed 2026-07-10: destination + visa template families stay full depth.
    assert classify(f"{BASE}/travel-insurance/") == ("core-page", "A-core")
    assert classify(f"{BASE}/travel-insurance/travel-insurance-uk/") == ("core-page", "A-core")
    assert classify(f"{BASE}/travel-insurance/france-visa/") == ("core-page", "A-core")
    assert classify(f"{BASE}/travel-insurance/single-trip-travel-insurance/") == ("core-page", "A-core")


def test_unrelated_pages_are_out_of_scope():
    assert classify(f"{BASE}/health-insurance/dubai/") is None
    assert classify(f"{BASE}/family-health-insurance-hic/") is None


def test_slug_is_last_segment_and_collisions_get_section_prefix():
    taken = set()
    a = make_slug(f"{BASE}/travel-insurance/articles/uae-visa/", taken)
    taken.add(a)
    b = make_slug(f"{BASE}/travel-insurance/uae-visa/", taken)
    assert a == "uae-visa"
    assert b == "travel-insurance-uae-visa"


def test_build_rows_dedupes_and_marks_pending():
    url = f"{BASE}/schengen-travel-insurance-tic/"
    rows = build_rows([url, url, f"{BASE}/ar-ae/schengen-travel-insurance-tic/"])
    assert len(rows) == 1
    assert rows[0]["status"] == "pending"
    assert rows[0]["slug"] == "schengen-travel-insurance-tic"


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
    urls.write_text("https://www.policybazaar.ae/schengen-travel-insurance-tic/\n")
    monkeypatch.setattr(filter_urls, "STATE_CSV", state)
    monkeypatch.setattr(filter_urls, "URLS_TXT", urls)
    filter_urls.main(force=True)
    assert "schengen-travel-insurance-tic" in state.read_text()


def test_state_fields_interface_is_stable():
    assert len(STATE_FIELDS) == 16
    assert STATE_FIELDS[0] == "url" and STATE_FIELDS[4] == "status"
