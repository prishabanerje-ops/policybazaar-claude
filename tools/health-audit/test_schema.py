from schema import validate_audit_json


def sample_audit():
    return {
        "url": "https://www.policybazaar.ae/health-insurance/",
        "slug": "health-insurance",
        "page_type": "core-page",
        "tier": "A-core",
        "audit_date": "2026-07-07",
        "mode": "URL",
        "md_file": "policybazaar-health-insurance-content-audit-2026-07-07.md",
        "scores": {"seo": 70, "geo": 65, "human_likeness": 80, "ymyl": 75,
                   "fact_check": 60, "overall": 69},
        "parameters": [{"lens": "seo", "name": "Title Tag", "score": 8, "max": 10,
                        "status": "warn", "finding": "Title exceeds 60 chars"}],
        "findings": [{"lens": "seo", "severity": "high", "found": "x", "why": "y", "fix": "z"}],
        "fact_checks": [{"claim": "AED 320", "verification": "query -> found",
                         "correct_value": "AED 320", "source": "DHA",
                         "source_tier": "Primary", "status": "Confirmed", "fix": "-"}],
        "ledger_entries": [{"fact_key": "dha-ebp-annual-premium", "page_value": "AED 320",
                            "verified_value": "AED 320", "source": "DHA",
                            "source_tier": "Primary", "status": "Confirmed"}],
        "schema_audit": [{"item": "FAQPage", "status": "ok", "finding": "present"}],
        "priority_recs": [{"priority": "High", "issue": "meta", "action": "rewrite"}],
    }


def test_complete_audit_json_is_valid():
    assert validate_audit_json(sample_audit()) == []


def test_missing_top_level_key_is_reported():
    data = sample_audit()
    del data["scores"]
    assert any("scores" in e for e in validate_audit_json(data))


def test_missing_score_key_is_reported():
    data = sample_audit()
    del data["scores"]["overall"]
    assert any("overall" in e for e in validate_audit_json(data))


def test_non_numeric_score_is_reported():
    data = sample_audit()
    data["scores"]["seo"] = "seventy"
    assert any("seo" in e for e in validate_audit_json(data))


def test_list_item_missing_field_is_reported():
    data = sample_audit()
    del data["ledger_entries"][0]["fact_key"]
    assert any("ledger_entries[0]" in e for e in validate_audit_json(data))


def test_non_list_value_reports_one_type_error_not_per_character_noise():
    data = sample_audit()
    data["findings"] = "oops-a-string"
    errors = validate_audit_json(data)
    assert any("'findings' should be list" in e for e in errors)
    assert not any("findings[" in e for e in errors)
