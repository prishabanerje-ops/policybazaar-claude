"""Shared paths for the health-insurance audit pipeline."""
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
URLS_TXT = WORKSPACE / ".claude/skills/content/content-audit/assets/policybazaar-urls.txt"

RESULT_DIR = Path(
    "/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result"
)
# Final Audit/ is the pipeline's self-contained working directory (moved here
# 2026-07-10) — ledger, per-URL JSON, master xlsx, tracker, and per-URL .md
# reports all live under it. Result/ root holds only older/unrelated files.
FINAL_AUDIT_DIR = RESULT_DIR / "Final Audit"
AUDIT_DATA_DIR = FINAL_AUDIT_DIR / "audit-data"
STATE_CSV = FINAL_AUDIT_DIR / "audit-state.csv"
MASTER_XLSX = FINAL_AUDIT_DIR / "policybazaar-insurance-content-audit.xlsx"
FACT_KEYS_MD = AUDIT_DATA_DIR / "fact-keys.md"

VERTICAL_LABEL = "Health Insurance"
TRACKER_XLSX = FINAL_AUDIT_DIR / "policybazaar-health-audit-tracker.xlsx"
