"""Shared paths for the travel-insurance audit pipeline."""
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
# Seed list: Aakash's provided travel URL list, cross-checked against
# sitemap-travel-2026-07-10.txt (in this directory) before seeding state.
URLS_TXT = Path(__file__).resolve().parent / "travel-urls.txt"

RESULT_DIR = Path(
    "/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Travel Insurance/Result"
)
AUDIT_DATA_DIR = RESULT_DIR / "audit-data"
STATE_CSV = RESULT_DIR / "audit-state.csv"
MASTER_XLSX = RESULT_DIR / "policybazaar-insurance-content-audit.xlsx"
FACT_KEYS_MD = AUDIT_DATA_DIR / "fact-keys.md"
