"""Validate agent audit JSON before it enters the workbook."""

TOP_KEYS = {
    "url": str, "slug": str, "page_type": str, "tier": str,
    "audit_date": str, "mode": str, "md_file": str, "scores": dict,
    "parameters": list, "findings": list, "fact_checks": list,
    "ledger_entries": list, "schema_audit": list, "priority_recs": list,
}
SCORE_KEYS = {"seo", "geo", "human_likeness", "ymyl", "fact_check", "overall"}
LIST_ITEM_KEYS = {
    "parameters": {"lens", "name", "score", "max", "status", "finding"},
    "findings": {"lens", "severity", "found", "why", "fix"},
    "fact_checks": {"claim", "verification", "correct_value", "source",
                    "source_tier", "status", "fix"},
    "ledger_entries": {"fact_key", "page_value", "verified_value", "source",
                       "source_tier", "status"},
    "schema_audit": {"row_type", "type_or_severity", "parse", "parity", "detail"},
    "priority_recs": {"priority", "issue", "action"},
}


def validate_audit_json(data):
    """Return a list of error strings; empty list means valid."""
    errors = []
    for key, expected in TOP_KEYS.items():
        if key not in data:
            errors.append(f"missing top-level key {key!r}")
        elif not isinstance(data[key], expected):
            errors.append(
                f"{key!r} should be {expected.__name__}, got {type(data[key]).__name__}"
            )
    if isinstance(data.get("scores"), dict):
        missing = SCORE_KEYS - data["scores"].keys()
        if missing:
            errors.append(f"scores missing {sorted(missing)}")
        for name, value in data["scores"].items():
            if not isinstance(value, (int, float)):
                errors.append(f"score {name!r} is not a number")
    for list_key, item_keys in LIST_ITEM_KEYS.items():
        items = data.get(list_key)
        if not isinstance(items, list):
            continue  # missing/wrong type already reported by the TOP_KEYS check
        for i, item in enumerate(items):
            if not isinstance(item, dict):
                errors.append(f"{list_key}[{i}] is not an object")
                continue
            missing = item_keys - item.keys()
            if missing:
                errors.append(f"{list_key}[{i}] missing {sorted(missing)}")
    return errors
