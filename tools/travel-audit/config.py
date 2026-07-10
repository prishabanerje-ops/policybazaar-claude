"""Shared paths for the travel-insurance audit pipeline."""
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
# Seed list: Aakash's provided travel URL list, cross-checked against
# sitemap-travel-2026-07-10.txt (in this directory) before seeding state.
URLS_TXT = Path(__file__).resolve().parent / "travel-urls.txt"

RESULT_DIR = Path(
    "/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Travel Insurance/Result"
)
# Final Audit/ is the pipeline's self-contained working directory (moved here
# 2026-07-10) — ledger, per-URL JSON, master xlsx, tracker, and per-URL .md
# reports all live under it. Result/ root holds only older/unrelated files.
FINAL_AUDIT_DIR = RESULT_DIR / "Final Audit"
AUDIT_DATA_DIR = FINAL_AUDIT_DIR / "audit-data"
STATE_CSV = FINAL_AUDIT_DIR / "audit-state.csv"
MASTER_XLSX = FINAL_AUDIT_DIR / "policybazaar-insurance-content-audit.xlsx"
FACT_KEYS_MD = AUDIT_DATA_DIR / "fact-keys.md"

VERTICAL_LABEL = "Travel Insurance"
TRACKER_XLSX = FINAL_AUDIT_DIR / "policybazaar-travel-audit-tracker.xlsx"
