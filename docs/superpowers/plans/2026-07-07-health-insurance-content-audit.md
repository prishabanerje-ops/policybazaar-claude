# Health Insurance Content Audit at Scale — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Audit ~990 English health-insurance URLs on policybazaar.ae with the five-lens `/content-audit` skill (per-URL dated `.md` + rolling master xlsx), then run a cross-site fact-consistency engine.

**Architecture:** Python tooling under `tools/health-audit/` drives a resumable `audit-state.csv`. Each session: take a batch of pending URLs → fan out parallel subagents via a Workflow script (each writes one `.md` report + one structured JSON) → a serial openpyxl collector appends the master workbook and updates state. After all batches, `consistency.py` groups ledger entries by fact key and flags truth violations and internal disagreements.

**Tech Stack:** Python 3 (stdlib + openpyxl, pytest for tests), Claude Workflow orchestration (`workflow-batch.js`), existing `/content-audit` skill for the audit logic itself.

**Spec:** `docs/superpowers/specs/2026-07-07-health-insurance-content-audit-design.md`

## Global Constraints

- **Never fabricate on tool failure** — a failed fetch/verification marks the row `failed` with a reason; no inferred data enters reports, JSON, or the workbook.
- **Master workbook is append-only** — `openpyxl.load_workbook()` then append; never overwrite, never create dated copies. Collector writes to a `.tmp` file and `os.replace()`s.
- **Output folder (the doubled `Documents/Documents` is correct):** `/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result/`
- **English pages only** — any URL containing `/ar-ae/` is out of scope.
- **Anchored filter only** — suffixes `-hipvd/ -hiart/ -hic/ -hinh/ -hicf/` matched at end-of-URL; paths `/health-insurance/` and `/network-hospitals/` matched anywhere. The raw unanchored regex is known to over-match ("which", "vehicles").
- **Report filename convention:** `policybazaar-<slug>-content-audit-YYYY-MM-DD.md`, date = actual run date.
- Python: stdlib + `openpyxl` only. Tests live next to code (`test_<module>.py`), names describe behavior, run with `python3 -m pytest`.
- Code lives in `tools/health-audit/` (committed); outputs live in the Result folder (outside the repo, never committed).

---

### Task 1: URL filter, tiering, and state-file initialisation

**Files:**
- Create: `tools/health-audit/config.py`
- Create: `tools/health-audit/filter_urls.py`
- Test: `tools/health-audit/test_filter_urls.py`

**Interfaces:**
- Consumes: `.claude/skills/content/content-audit/assets/policybazaar-urls.txt` (one URL per line).
- Produces: `STATE_FIELDS` (list of 16 column names — every later task uses it), `classify(url) -> tuple[str, str] | None`, `build_rows(urls) -> list[dict]`, and on-disk `audit-state.csv`.

- [ ] **Step 1: Verify the Python environment**

Run: `python3 -c "import openpyxl, pytest; print('ok')"`
Expected: `ok`. If ImportError: `python3 -m pip install --user openpyxl pytest` and re-run.

- [ ] **Step 2: Write `config.py`** (no test — pure constants)

```python
"""Shared paths for the health-insurance audit pipeline."""
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
URLS_TXT = WORKSPACE / ".claude/skills/content/content-audit/assets/policybazaar-urls.txt"

RESULT_DIR = Path(
    "/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result"
)
AUDIT_DATA_DIR = RESULT_DIR / "audit-data"
STATE_CSV = RESULT_DIR / "audit-state.csv"
MASTER_XLSX = RESULT_DIR / "policybazaar-insurance-content-audit.xlsx"
FACT_KEYS_MD = AUDIT_DATA_DIR / "fact-keys.md"
```

- [ ] **Step 3: Write the failing tests**

```python
# tools/health-audit/test_filter_urls.py
from filter_urls import build_rows, classify, make_slug

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
```

- [ ] **Step 4: Run tests to verify they fail**

Run: `cd "tools/health-audit" && python3 -m pytest test_filter_urls.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'filter_urls'`

- [ ] **Step 5: Write `filter_urls.py`**

```python
"""Build the health-insurance audit URL set and initialise audit-state.csv."""
import csv
import sys

from config import STATE_CSV, URLS_TXT

STATE_FIELDS = [
    "url", "slug", "page_type", "tier", "status",
    "seo", "geo", "human_likeness", "ymyl", "fact_check", "overall",
    "md_file", "json_file", "audit_date", "batch_id", "failure_reason",
]

SUFFIX_RULES = [
    ("-hipvd/", "provider", "A-core"),
    ("-hiart/", "article", "A-articles"),
    ("-hic/", "category", "A-core"),
    ("-hinh/", "hospital-listing", "B"),
    ("-hicf/", "claim-form", "B"),
]

PATH_RULES = [
    ("/network-hospitals/", "hospital-listing", "B"),
    ("/health-insurance/hospitals/", "hospital-listing", "B"),
    ("/health-insurance/glossary/", "glossary", "B"),
    ("/health-insurance/news-and-update/", "news", "B"),
    ("/health-insurance/articles/", "article", "A-articles"),
    ("/health-insurance/tpa/", "tpa", "A-core"),
    ("/health-insurance/health-guide/", "health-guide", "A-core"),
]


def classify(url):
    """Return (page_type, tier), or None when the URL is out of scope."""
    if "/ar-ae/" in url:
        return None
    for suffix, page_type, tier in SUFFIX_RULES:
        if url.endswith(suffix):
            return page_type, tier
    for fragment, page_type, tier in PATH_RULES:
        if fragment in url:
            return page_type, tier
    if "/health-insurance/" in url:
        return "core-page", "A-core"
    return None


def make_slug(url, taken):
    """Last path segment; on collision prefix the parent segment."""
    path = url.split("policybazaar.ae", 1)[-1]
    segments = [s for s in path.split("/") if s]
    slug = segments[-1]
    if slug in taken and len(segments) >= 2:
        slug = f"{segments[-2]}-{segments[-1]}"
    if slug in taken:
        raise ValueError(f"slug collision unresolved for {url}: {slug!r} already taken")
    return slug


def build_rows(urls):
    rows = []
    taken = set()
    for url in sorted({u.strip() for u in urls if u.strip()}):
        result = classify(url)
        if result is None:
            continue
        page_type, tier = result
        slug = make_slug(url, taken)
        taken.add(slug)
        row = {field: "" for field in STATE_FIELDS}
        row.update(url=url, slug=slug, page_type=page_type, tier=tier, status="pending")
        rows.append(row)
    return rows


def main(force=False):
    if STATE_CSV.exists() and not force:
        sys.exit(
            f"{STATE_CSV} already exists — refusing to overwrite a live audit state. "
            "Re-run with --force to rebuild from scratch."
        )
    rows = build_rows(URLS_TXT.read_text().splitlines())
    STATE_CSV.parent.mkdir(parents=True, exist_ok=True)
    with STATE_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=STATE_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {STATE_CSV}")


if __name__ == "__main__":
    main(force="--force" in sys.argv)
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `cd "tools/health-audit" && python3 -m pytest test_filter_urls.py -v`
Expected: 6 passed

- [ ] **Step 7: Sanity-check the real count (no file written)**

Run: `cd "tools/health-audit" && python3 -c "from config import URLS_TXT; from filter_urls import build_rows; rows = build_rows(URLS_TXT.read_text().splitlines()); print(len(rows)); import collections; print(collections.Counter(r['tier'] for r in rows))"`
Expected: total ≈ 990; tiers roughly A-core ≈ 300, A-articles ≈ 410, B ≈ 280. If wildly off, stop and investigate before committing.

- [ ] **Step 8: Commit**

```bash
git add tools/health-audit/config.py tools/health-audit/filter_urls.py tools/health-audit/test_filter_urls.py
git commit -m "feat(health-audit): URL filter, tiering, state-file init"
```

---

### Task 2: State helpers (resumable batching)

**Files:**
- Create: `tools/health-audit/state.py`
- Test: `tools/health-audit/test_state.py`

**Interfaces:**
- Consumes: `STATE_FIELDS` from `filter_urls`.
- Produces: `read_state(path) -> list[dict]`, `write_state(path, rows)`, `next_batch(rows, size, tiers=None) -> list[dict]`, `mark(rows, urls, **updates)`, `reset_stale(rows, audit_data_dir) -> int`. CLI: `python3 state.py summary | reset-stale | take <size> [tiers] [batch_id] | fail <url> <reason>`.

- [ ] **Step 1: Write the failing tests**

```python
# tools/health-audit/test_state.py
import pytest

from filter_urls import STATE_FIELDS
from state import mark, next_batch, read_state, reset_stale, write_state


def make_row(**overrides):
    row = {field: "" for field in STATE_FIELDS}
    row.update(status="pending", **overrides)
    return row


def test_state_roundtrips_through_csv(tmp_path):
    path = tmp_path / "state.csv"
    rows = [make_row(url="https://x/a/", slug="a", tier="A-core")]
    write_state(path, rows)
    assert read_state(path) == rows


def test_next_batch_takes_only_pending_of_requested_tiers():
    rows = [
        make_row(url="u1", tier="A-core"),
        make_row(url="u2", tier="B"),
        make_row(url="u3", tier="A-core", status="done"),
        make_row(url="u4", tier="A-core"),
    ]
    batch = next_batch(rows, size=5, tiers=["A-core"])
    assert [r["url"] for r in batch] == ["u1", "u4"]


def test_mark_raises_when_a_url_is_missing_from_state():
    rows = [make_row(url="u1")]
    with pytest.raises(ValueError):
        mark(rows, ["u1", "ghost"], status="in_progress")


def test_reset_stale_returns_in_progress_rows_without_json_to_pending(tmp_path):
    (tmp_path / "has-json.json").write_text("{}")
    rows = [
        make_row(url="u1", slug="has-json", status="in_progress"),
        make_row(url="u2", slug="no-json", status="in_progress"),
    ]
    assert reset_stale(rows, tmp_path) == 1
    assert rows[0]["status"] == "in_progress"
    assert rows[1]["status"] == "pending"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd "tools/health-audit" && python3 -m pytest test_state.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'state'`

- [ ] **Step 3: Write `state.py`**

```python
"""Read/update audit-state.csv — the resumable backbone of the audit run."""
import csv
import json
import sys
from collections import Counter
from pathlib import Path

from filter_urls import STATE_FIELDS


def read_state(path):
    with open(path, newline="") as fh:
        return list(csv.DictReader(fh))


def write_state(path, rows):
    with open(path, "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=STATE_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def next_batch(rows, size, tiers=None):
    pending = [
        r for r in rows
        if r["status"] == "pending" and (tiers is None or r["tier"] in tiers)
    ]
    return pending[:size]


def mark(rows, urls, **updates):
    urls = set(urls)
    hit = 0
    for row in rows:
        if row["url"] in urls:
            row.update({k: str(v) for k, v in updates.items()})
            hit += 1
    if hit != len(urls):
        raise ValueError(
            f"mark() matched {hit} of {len(urls)} urls — batch and state file are out of sync"
        )
    return rows


def reset_stale(rows, audit_data_dir):
    """in_progress rows with no JSON on disk died mid-run — return them to pending."""
    audit_data_dir = Path(audit_data_dir)
    count = 0
    for row in rows:
        if row["status"] == "in_progress" and not (audit_data_dir / f"{row['slug']}.json").exists():
            row["status"] = "pending"
            count += 1
    return count


if __name__ == "__main__":
    from config import AUDIT_DATA_DIR, STATE_CSV

    rows = read_state(STATE_CSV)
    cmd = sys.argv[1] if len(sys.argv) > 1 else "summary"
    if cmd == "summary":
        print(Counter(r["status"] for r in rows))
        print(Counter((r["tier"], r["status"]) for r in rows))
    elif cmd == "reset-stale":
        n = reset_stale(rows, AUDIT_DATA_DIR)
        write_state(STATE_CSV, rows)
        print(f"reset {n} stale rows to pending")
    elif cmd == "take":
        size = int(sys.argv[2])
        tiers = sys.argv[3].split(",") if len(sys.argv) > 3 else None
        batch_id = sys.argv[4] if len(sys.argv) > 4 else "batch"
        batch = next_batch(rows, size, tiers)
        mark(rows, [r["url"] for r in batch], status="in_progress", batch_id=batch_id)
        write_state(STATE_CSV, rows)
        print(json.dumps(
            [{k: r[k] for k in ("url", "slug", "page_type", "tier")} for r in batch]
        ))
    elif cmd == "fail":
        mark(rows, [sys.argv[2]], status="failed", failure_reason=sys.argv[3])
        write_state(STATE_CSV, rows)
        print(f"marked failed: {sys.argv[2]}")
    else:
        sys.exit(f"unknown command {cmd!r} — use summary | reset-stale | take | fail")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd "tools/health-audit" && python3 -m pytest test_state.py -v`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add tools/health-audit/state.py tools/health-audit/test_state.py
git commit -m "feat(health-audit): state helpers with CLI (summary/take/reset-stale/fail)"
```

---

### Task 3: Audit-JSON validator

**Files:**
- Create: `tools/health-audit/schema.py`
- Test: `tools/health-audit/test_schema.py`

**Interfaces:**
- Consumes: nothing (stdlib only).
- Produces: `validate_audit_json(data) -> list[str]` (empty list = valid) and the canonical key sets `TOP_KEYS`, `SCORE_KEYS`, `LIST_ITEM_KEYS` — Task 5's agent prompt embeds the same field names; they must stay in sync.

- [ ] **Step 1: Write the failing tests**

```python
# tools/health-audit/test_schema.py
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd "tools/health-audit" && python3 -m pytest test_schema.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'schema'`... **caution:** Python has a stdlib-adjacent PyPI package named `schema`; here the local file wins on `sys.path` — that is intended.

- [ ] **Step 3: Write `schema.py`**

```python
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
    "schema_audit": {"item", "status", "finding"},
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
        for i, item in enumerate(data.get(list_key) or []):
            if not isinstance(item, dict):
                errors.append(f"{list_key}[{i}] is not an object")
                continue
            missing = item_keys - item.keys()
            if missing:
                errors.append(f"{list_key}[{i}] missing {sorted(missing)}")
    return errors
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd "tools/health-audit" && python3 -m pytest test_schema.py -v`
Expected: 5 passed

- [ ] **Step 5: Commit**

```bash
git add tools/health-audit/schema.py tools/health-audit/test_schema.py
git commit -m "feat(health-audit): audit-JSON validator"
```

---

### Task 4: Serial collector (JSON → master workbook + state update)

**Files:**
- Create: `tools/health-audit/collector.py`
- Test: `tools/health-audit/test_collector.py`

**Interfaces:**
- Consumes: `validate_audit_json` (Task 3), `read_state`/`write_state` (Task 2), audit JSONs shaped per Task 3's `sample_audit()`.
- Produces: `collect(state_csv, audit_data_dir, xlsx_path, fact_keys_md, dry_run=False) -> tuple[list, list]` (done urls, failed urls); maintains `fact-keys.md`. CLI: `python3 collector.py [--dry-run]`.

- [ ] **Step 1: Write the failing tests**

```python
# tools/health-audit/test_collector.py
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd "tools/health-audit" && python3 -m pytest test_collector.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'collector'`

- [ ] **Step 3: Write `collector.py`**

```python
"""Serial collector: append validated audit JSONs to the master workbook, update state."""
import json
import os
import sys
from pathlib import Path

from openpyxl import Workbook, load_workbook

from schema import validate_audit_json
from state import read_state, write_state

SHEET_COLUMNS = {
    "Summary": ["URL", "Audit Date", "SEO", "GEO", "Human-Likeness", "YMYL",
                "Fact-Check", "Overall", "Rating", "MD File"],
    "Lens Scores": ["URL", "Audit Date", "Lens", "Parameter", "Score", "Max",
                    "Status", "Finding"],
    "Findings": ["URL", "Audit Date", "Lens", "Severity", "Found", "Why", "Fix"],
    "Fact-Check": ["URL", "Audit Date", "Claim", "Verification", "Correct Value",
                   "Source", "Source Tier", "Status", "Fix"],
    "Schema": ["URL", "Audit Date", "Item", "Status", "Finding"],
    "Priority Recs": ["URL", "Audit Date", "Priority", "Issue", "Action"],
    "Verification Ledger": ["Fact Key", "Page Value", "Verified Value", "Source",
                            "Source Tier", "Status", "URL", "Audit Date"],
}
SCORE_FIELDS = ("seo", "geo", "human_likeness", "ymyl", "fact_check", "overall")


def rating(overall):
    if overall >= 85:
        return "🟢 Publish-ready"
    if overall >= 70:
        return "🟡 Minor fixes"
    if overall >= 55:
        return "🟠 Needs work"
    return "🔴 Major rework"


def rows_for(d):
    url, day, s = d["url"], d["audit_date"], d["scores"]
    return {
        "Summary": [[url, day, s["seo"], s["geo"], s["human_likeness"], s["ymyl"],
                     s["fact_check"], s["overall"], rating(s["overall"]), d["md_file"]]],
        "Lens Scores": [[url, day, p["lens"], p["name"], p["score"], p["max"],
                         p["status"], p["finding"]] for p in d["parameters"]],
        "Findings": [[url, day, f["lens"], f["severity"], f["found"], f["why"],
                      f["fix"]] for f in d["findings"]],
        "Fact-Check": [[url, day, c["claim"], c["verification"], c["correct_value"],
                        c["source"], c["source_tier"], c["status"], c["fix"]]
                       for c in d["fact_checks"]],
        "Schema": [[url, day, i["item"], i["status"], i["finding"]]
                   for i in d["schema_audit"]],
        "Priority Recs": [[url, day, r["priority"], r["issue"], r["action"]]
                          for r in d["priority_recs"]],
        "Verification Ledger": [[e["fact_key"], e["page_value"], e["verified_value"],
                                 e["source"], e["source_tier"], e["status"], url, day]
                                for e in d["ledger_entries"]],
    }


def ensure_workbook(path):
    if path.exists():
        wb = load_workbook(path)
        for name, cols in SHEET_COLUMNS.items():
            if name not in wb.sheetnames:
                sys.exit(f"master workbook {path} is missing sheet {name!r} — "
                         "align SHEET_COLUMNS with the existing workbook before collecting")
            header = [c.value for c in wb[name][1]]
            if header != cols:
                sys.exit(f"sheet {name!r} header mismatch:\n  workbook: {header}\n"
                         f"  expected: {cols}")
        return wb
    wb = Workbook()
    wb.remove(wb.active)
    for name, cols in SHEET_COLUMNS.items():
        wb.create_sheet(name).append(cols)
    return wb


def update_fact_keys(fact_keys_md, datas):
    known = set()
    if fact_keys_md.exists():
        known = {line.split("`")[1] for line in fact_keys_md.read_text().splitlines()
                 if line.count("`") >= 2}
    new_lines = []
    for d in datas:
        for e in d["ledger_entries"]:
            if e["fact_key"] not in known:
                known.add(e["fact_key"])
                new_lines.append(f"- `{e['fact_key']}` — first seen: {d['url']}")
    if new_lines:
        with fact_keys_md.open("a") as fh:
            fh.write("\n".join(new_lines) + "\n")


def collect(state_csv, audit_data_dir, xlsx_path, fact_keys_md, dry_run=False):
    audit_data_dir, xlsx_path = Path(audit_data_dir), Path(xlsx_path)
    rows = read_state(state_csv)
    wb = ensure_workbook(xlsx_path)
    done, failed, ingested = [], [], []
    for row in rows:
        if row["status"] != "in_progress":
            continue
        json_path = audit_data_dir / f"{row['slug']}.json"
        if not json_path.exists():
            continue  # agent still running or died before writing — reset-stale handles it
        data = json.loads(json_path.read_text())
        errors = validate_audit_json(data)
        if errors:
            row.update(status="failed",
                       failure_reason="invalid json: " + "; ".join(errors[:3]))
            failed.append(row["url"])
            continue
        for sheet, sheet_rows in rows_for(data).items():
            ws = wb[sheet]
            for r in sheet_rows:
                ws.append(r)
            ws.auto_filter.ref = ws.dimensions
        row.update(status="done", audit_date=data["audit_date"],
                   md_file=data["md_file"], json_file=json_path.name,
                   **{k: str(data["scores"][k]) for k in SCORE_FIELDS})
        done.append(row["url"])
        ingested.append(data)
    if dry_run:
        print(f"dry-run: would append {len(done)} audits, mark {len(failed)} failed")
        return done, failed
    tmp = xlsx_path.with_name(xlsx_path.name + ".tmp")
    wb.save(tmp)
    os.replace(tmp, xlsx_path)
    update_fact_keys(Path(fact_keys_md), ingested)
    write_state(state_csv, rows)
    print(f"collected {len(done)} audits, {len(failed)} invalid → {xlsx_path}")
    return done, failed


if __name__ == "__main__":
    from config import AUDIT_DATA_DIR, FACT_KEYS_MD, MASTER_XLSX, STATE_CSV

    collect(STATE_CSV, AUDIT_DATA_DIR, MASTER_XLSX, FACT_KEYS_MD,
            dry_run="--dry-run" in sys.argv)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd "tools/health-audit" && python3 -m pytest test_collector.py -v`
Expected: 5 passed

- [ ] **Step 5: Reconcile with the EXISTING master workbook**

The real master already exists (first audit appended 2026-07-06). Inspect its actual layout:

Run:
```bash
python3 - <<'EOF'
from openpyxl import load_workbook
wb = load_workbook("/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result/policybazaar-insurance-content-audit.xlsx", read_only=True)
for ws in wb:
    print(repr(ws.title), [c.value for c in ws[1]])
EOF
```

Decision rule: if the printed sheet names/headers differ from `SHEET_COLUMNS`, the workbook wins (append-only contract) — update `SHEET_COLUMNS` and the corresponding `rows_for()` orderings to match the existing headers exactly, re-run `python3 -m pytest test_collector.py -v` (tests build a fresh workbook from `SHEET_COLUMNS`, so they stay valid), and note the change in the commit message. If the workbook is missing entirely, keep the plan's layout.

- [ ] **Step 6: Commit**

```bash
git add tools/health-audit/collector.py tools/health-audit/test_collector.py
git commit -m "feat(health-audit): serial collector (JSON -> master xlsx, append-only)"
```

---

### Task 5: Agent prompt template, fact-key seed, and batch workflow script

**Files:**
- Create: `tools/health-audit/agent-prompt.md`
- Create: `tools/health-audit/workflow-batch.js`
- Create (at runtime, first batch): `<Result>/audit-data/fact-keys.md` seed

**Interfaces:**
- Consumes: placeholders `{URL} {SLUG} {PAGE_TYPE} {TIER} {AUDIT_DATE}`; the JSON field names from Task 3 (`TOP_KEYS`/`LIST_ITEM_KEYS` — keep in sync).
- Produces: each agent writes `policybazaar-{SLUG}-content-audit-{AUDIT_DATE}.md` + `audit-data/{SLUG}.json`, and returns `{url, status, overall, md_file, json_file, failure_reason}` — consumed by the runbook (Task 6) to mark failures.

- [ ] **Step 1: Write `agent-prompt.md`**

````markdown
You are auditing ONE policybazaar.ae page as part of a batched health-insurance content audit.

- Page URL: {URL}
- Slug: {SLUG}
- Page type: {PAGE_TYPE}
- Tier: {TIER}
- Audit date: {AUDIT_DATE}

## Procedure

1. Read `/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills/content/content-audit/SKILL.md`
   and the reference files it lists per lens. Brand is Policybazaar UAE — read
   `references/policybazaar-context.md` and `references/schema-expectations-health.md`.
2. Run the URL MODE five-lens audit on {URL} at the depth for tier {TIER}:
   - **A-core / A-articles** — full depth: all five lenses including per-claim web fact-check.
   - **B** — light pass: title/meta/H1, page-specific facts (hospital/insurer names,
     locations, form links resolve), duplicate/thin-content risk; fact-check ONLY claims
     unique to this page. Score all five lenses but write "Tier B light audit" under the
     report header. Template-level findings are covered by the family's representative
     page — do not repeat them.
3. Write the full report (skill Step 4 format) to:
   `/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result/policybazaar-{SLUG}-content-audit-{AUDIT_DATE}.md`
4. Write the structured JSON to:
   `/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result/audit-data/{SLUG}.json`
   Top-level keys (ALL required): url, slug, page_type, tier, audit_date, mode ("URL"),
   md_file, scores {seo, geo, human_likeness, ymyl, fact_check, overall — numbers},
   parameters [{lens, name, score, max, status, finding}],
   findings [{lens, severity, found, why, fix}],
   fact_checks [{claim, verification, correct_value, source, source_tier, status, fix}],
   ledger_entries [{fact_key, page_value, verified_value, source, source_tier, status}],
   schema_audit [{item, status, finding}],
   priority_recs [{priority, issue, action}].
   Every checkable fact on the page (price, %, limit, deadline, regulatory claim,
   platform figure) gets a ledger_entry. fact_key is a normalized kebab-case key for the
   UNDERLYING fact, not the page's phrasing. FIRST read
   `.../Result/audit-data/fact-keys.md` and reuse an existing key when the fact matches;
   if none matches, invent a precise new key (the collector registers it). For facts with
   no external arbiter (platform figures like "plans from AED X on Policybazaar"), set
   verified_value to "n/a" and status to "Unverifiable".
5. TOOL FAILURE POLICY (hard rule): if the page fetch or a verification tool fails,
   do NOT fabricate or infer. If the page itself cannot be fetched, write NO files and
   return status "failed" with the exact failure in failure_reason. If only some
   verifications fail, mark those claims Unverifiable and continue.
6. Your final structured output: {url, status ("done"|"failed"), overall (number),
   md_file, json_file, failure_reason (empty string if done)}. Return "done" ONLY when
   both files are written.
````

- [ ] **Step 2: Write `workflow-batch.js`**

```javascript
export const meta = {
  name: 'health-audit-batch',
  description: 'Fan out one content-audit agent per health-insurance URL in the batch',
  phases: [{ title: 'Audit' }],
}
// args: { batch: [{url, slug, page_type, tier}], promptTemplate: string, auditDate: string }
const RESULT_SCHEMA = {
  type: 'object',
  properties: {
    url: { type: 'string' },
    status: { enum: ['done', 'failed'] },
    overall: { type: 'number' },
    md_file: { type: 'string' },
    json_file: { type: 'string' },
    failure_reason: { type: 'string' },
  },
  required: ['url', 'status'],
}
phase('Audit')
const results = await parallel(args.batch.map(item => () => {
  const prompt = args.promptTemplate
    .replaceAll('{URL}', item.url)
    .replaceAll('{SLUG}', item.slug)
    .replaceAll('{PAGE_TYPE}', item.page_type)
    .replaceAll('{TIER}', item.tier)
    .replaceAll('{AUDIT_DATE}', args.auditDate)
  return agent(prompt, { label: `audit:${item.slug}`, schema: RESULT_SCHEMA })
}))
log(`batch done: ${results.filter(Boolean).length}/${args.batch.length} agents returned`)
return results.filter(Boolean)
```

- [ ] **Step 3: Write the fact-keys seed content** (created on disk during the pilot, Task 7 Step 2 — content defined here)

```markdown
# Fact-key registry — health insurance audit

One line per canonical fact. Agents REUSE an existing key when the fact matches;
the collector appends newly seen keys automatically. Seed keys below are naming
examples — every value must still be verified on first use.

- `dubai-ebp-annual-premium` — Dubai Essential Benefits Plan yearly premium
- `dubai-no-insurance-fine-monthly` — Dubai monthly fine for uninsured residents
- `uae-basic-scheme-premium-aed-320` — AED 320 basic scheme figure (verified Jul 2026, see memory)
- `health-insurance-mandatory-dubai` — whether health insurance is mandatory in Dubai
- `health-insurance-mandatory-abu-dhabi` — whether health insurance is mandatory in Abu Dhabi
```

- [ ] **Step 4: Verify the prompt's JSON fields match `schema.py`**

Run: `cd "tools/health-audit" && python3 -c "
from schema import TOP_KEYS, LIST_ITEM_KEYS
text = open('agent-prompt.md').read()
missing = [k for k in TOP_KEYS if k not in text] + [f for keys in LIST_ITEM_KEYS.values() for f in keys if f not in text]
print('MISSING FROM PROMPT:', missing or 'none')"`
Expected: `MISSING FROM PROMPT: none`

- [ ] **Step 5: Commit**

```bash
git add tools/health-audit/agent-prompt.md tools/health-audit/workflow-batch.js
git commit -m "feat(health-audit): agent prompt template + batch workflow script"
```

---

### Task 6: Batch-session runbook (`/health-audit-batch` command)

**Files:**
- Create: `.claude/commands/health-audit-batch.md`

**Interfaces:**
- Consumes: `state.py` CLI (Task 2), `workflow-batch.js` + `agent-prompt.md` (Task 5), `collector.py` CLI (Task 4).
- Produces: the repeatable per-session loop any future Claude session follows.

- [ ] **Step 1: Write `.claude/commands/health-audit-batch.md`**

````markdown
# /health-audit-batch — run one batch of the health-insurance content audit

Working dir for all commands: `tools/health-audit/` in the PolicyBazaar Claude workspace.
State + outputs live in `/Users/aakashsrivastava/Documents/Documents/PolicyBazaar Research/Health Insurance/Result/`.

## Per-session loop

1. **Status:** `python3 state.py summary` — report counts to Aakash. If zero pending and
   zero in_progress → Task 1 is complete: stop and propose running the consistency engine
   (`python3 consistency.py`).
2. **Recover:** `python3 state.py reset-stale` — returns crashed in_progress rows to pending.
3. **Take a batch:** priority order A-core → A-articles → B. Sizes: 12 for tier A,
   40 for tier B.
   `python3 state.py take 12 A-core batch-YYYY-MM-DD-N` (falls through to
   `A-articles` then `B` when the tier is exhausted). The JSON it prints is the batch.
4. **Run the workflow:** Read `agent-prompt.md`, then invoke the Workflow tool with
   `scriptPath: tools/health-audit/workflow-batch.js` and
   `args: { batch: <the JSON from step 3>, promptTemplate: <agent-prompt.md content>,
   auditDate: "<today YYYY-MM-DD>" }`.
5. **Mark failures:** for every workflow result with status "failed":
   `python3 state.py fail "<url>" "<failure_reason>"`.
6. **Collect:** `python3 collector.py --dry-run` (sanity), then `python3 collector.py`.
7. **Report to Aakash:** done/failed counts this batch, cumulative summary
   (`python3 state.py summary`), score range, and any URL that failed twice
   (needs manual attention — do NOT silently retry forever).

## Hard rules

- Never fabricate audit data after a tool failure — mark failed, report, move on.
- Never touch the master xlsx except through `collector.py` (append-only).
- One collector run at a time; the workflow agents never write xlsx/state themselves.
````

- [ ] **Step 2: Commit**

```bash
git add .claude/commands/health-audit-batch.md
git commit -m "feat(health-audit): per-session batch runbook command"
```

---

### Task 7: Pilot batch (5 URLs, end-to-end validation) — REVIEW GATE

**Files:**
- Create (runtime): `<Result>/audit-state.csv`, `<Result>/audit-data/fact-keys.md`
- No code changes.

**Interfaces:**
- Consumes: everything from Tasks 1–6.
- Produces: 5 real `.md` reports, 5 JSONs, first collector append, validated pipeline. **Aakash reviews before any scale-up.**

- [ ] **Step 1: Initialise real state**

Run: `cd "tools/health-audit" && python3 filter_urls.py && python3 state.py summary`
Expected: ~990 rows written; all pending. (If `audit-state.csv` already exists it refuses — that's correct; only `--force` on Aakash's explicit say-so.)

- [ ] **Step 2: Seed fact-keys.md**

Write the Task 5 Step 3 content to `<Result>/audit-data/fact-keys.md` (create `audit-data/` first).

- [ ] **Step 3: Hand-pick the 5 pilot URLs (one per page family) and mark them**

Pick from `audit-state.csv`: 1 `core-page`, 1 `provider` (-hipvd), 1 `article`, 1 `hospital-listing`, 1 `claim-form` (-hicf). Then per URL:
`python3 - <<'EOF'` … or simpler, run five times:
`python3 state.py take 1 A-core pilot`, `python3 state.py take 1 A-articles pilot`, etc. — but for exact page-family coverage, mark by hand:

```bash
python3 - <<'EOF'
from config import STATE_CSV
from state import read_state, write_state, mark
rows = read_state(STATE_CSV)
picked, seen = [], set()
for row in rows:
    if row["page_type"] in ("core-page", "provider", "article", "hospital-listing", "claim-form") \
            and row["page_type"] not in seen and row["status"] == "pending":
        picked.append(row["url"]); seen.add(row["page_type"])
mark(rows, picked, status="in_progress", batch_id="pilot")
write_state(STATE_CSV, rows)
import json
print(json.dumps([{k: r[k] for k in ("url", "slug", "page_type", "tier")}
                  for r in rows if r["batch_id"] == "pilot"]))
EOF
```

- [ ] **Step 4: Run the pilot workflow**

Follow runbook steps 4–6 (Workflow with the 5-item batch → mark failures → `collector.py --dry-run` → `collector.py`).

- [ ] **Step 5: Verify outputs**

- 5 dated `.md` files exist in the Result folder and follow the skill's Step 4 report format.
- 5 JSONs in `audit-data/`, all validated (collector reported 0 invalid).
- Master workbook opens; new rows appended on every sheet; the pre-existing 2026-07-06 rows untouched.
- `audit-state.csv`: 5 rows done (or failed with honest reasons).

- [ ] **Step 6: STOP — Aakash reviews the pilot**

Present: the 5 reports, workbook state, any failures, and observed per-audit duration. Do not proceed to Task 8/9 until Aakash approves quality and (if needed) adjusts tier depth or batch sizes.

---

### Task 8: Consistency engine (Task 2 of the spec)

**Files:**
- Create: `tools/health-audit/consistency.py`
- Test: `tools/health-audit/test_consistency.py`

**Interfaces:**
- Consumes: all `audit-data/*.json` (ledger_entries), master workbook.
- Produces: `run(audit_data_dir, xlsx_path, result_dir, report_date) -> Path` (report path); appends a **Consistency** sheet; writes `policybazaar-health-consistency-report-YYYY-MM-DD.md`.

- [ ] **Step 1: Write the failing tests**

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd "tools/health-audit" && python3 -m pytest test_consistency.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'consistency'`

- [ ] **Step 3: Write `consistency.py`**

```python
"""Task 2 — cross-site consistency engine over audit-data JSONs."""
import json
import os
import sys
from collections import defaultdict
from datetime import date
from itertools import combinations
from pathlib import Path

from openpyxl import load_workbook

CONSISTENCY_COLUMNS = ["Fact Key", "Canonical Value", "Source", "Source Tier",
                       "URL", "Page Value", "Verdict", "Fix"]


def load_entries(audit_data_dir):
    entries = []
    for path in sorted(Path(audit_data_dir).glob("*.json")):
        data = json.loads(path.read_text())
        for e in data.get("ledger_entries", []):
            entries.append({**e, "url": data["url"]})
    return entries


def norm(value):
    return " ".join(str(value).lower().split())


def near_duplicate_keys(keys):
    """Pairs of fact keys whose kebab-token sets overlap >= 60% — merge candidates."""
    tokens = {k: set(k.split("-")) for k in keys}
    pairs = []
    for a, b in combinations(sorted(keys), 2):
        union = tokens[a] | tokens[b]
        if union and len(tokens[a] & tokens[b]) / len(union) >= 0.6:
            pairs.append((a, b))
    return pairs


def judge(group):
    """Classify one fact_key group.

    Returns (canonical_value, source, source_tier, rows) where each row is
    (url, page_value, verdict, fix) and verdict is one of:
    consistent | truth-violation | internal-disagreement.
    """
    verified = [e for e in group if norm(e.get("verified_value", "")) not in ("", "n/a")]
    if verified:
        counts = defaultdict(int)
        for e in verified:
            counts[norm(e["verified_value"])] += 1
        canonical_norm = max(counts, key=counts.get)
        best = next(e for e in verified if norm(e["verified_value"]) == canonical_norm)
        canonical, source, tier = best["verified_value"], best["source"], best["source_tier"]
        rows = []
        for e in group:
            if norm(e["page_value"]) == canonical_norm:
                rows.append((e["url"], e["page_value"], "consistent", ""))
            else:
                rows.append((e["url"], e["page_value"], "truth-violation",
                             f"Update to {canonical} (per {source})"))
        return canonical, source, tier, rows
    values = {norm(e["page_value"]) for e in group}
    if len(values) <= 1:
        return "", "", "", [(e["url"], e["page_value"], "consistent", "") for e in group]
    fix = ("Pages disagree and no external source arbitrates — pick one platform figure, "
           "attribute it, add an as-of date")
    return "", "", "", [(e["url"], e["page_value"], "internal-disagreement", fix)
                        for e in group]


def run(audit_data_dir, xlsx_path, result_dir, report_date=None):
    report_date = report_date or date.today().isoformat()
    entries = load_entries(audit_data_dir)
    if not entries:
        sys.exit(f"no ledger entries found under {audit_data_dir} — run Task 1 audits first")
    groups = defaultdict(list)
    for e in entries:
        groups[e["fact_key"]].append(e)
    merge_candidates = near_duplicate_keys(groups.keys())

    xlsx_path = Path(xlsx_path)
    wb = load_workbook(xlsx_path)
    if "Consistency" not in wb.sheetnames:
        wb.create_sheet("Consistency").append(CONSISTENCY_COLUMNS)
    ws = wb["Consistency"]

    lines = [f"# Health Insurance Cross-Site Consistency Report — {report_date}", ""]
    if merge_candidates:
        lines += ["## ⚠️ Fact-key merge candidates (review, merge in JSONs, re-run)", ""]
        lines += [f"- `{a}` ↔ `{b}`" for a, b in merge_candidates] + [""]
    issue_count = 0
    for key in sorted(groups):
        canonical, source, tier, rows = judge(groups[key])
        for url, value, verdict, fix in rows:
            ws.append([key, canonical, source, tier, url, value, verdict, fix])
        flagged = [r for r in rows if r[2] != "consistent"]
        if not flagged:
            continue
        issue_count += len(flagged)
        lines += [f"## `{key}`", ""]
        if canonical:
            lines.append(f"**Canonical value:** {canonical} — {source} ({tier})")
        lines += ["", "| URL | Page value | Verdict | Fix |", "|---|---|---|---|"]
        lines += [f"| {url} | {value} | {verdict} | {fix} |"
                  for url, value, verdict, fix in flagged]
        lines.append("")
    lines.append(f"---\n\n**{issue_count} inconsistencies across {len(groups)} facts, "
                 f"{len(entries)} ledger entries.**")
    ws.auto_filter.ref = ws.dimensions

    report = Path(result_dir) / f"policybazaar-health-consistency-report-{report_date}.md"
    report.write_text("\n".join(lines))
    tmp = xlsx_path.with_name(xlsx_path.name + ".tmp")
    wb.save(tmp)
    os.replace(tmp, xlsx_path)
    print(f"{issue_count} inconsistencies across {len(groups)} facts → {report}")
    return report


if __name__ == "__main__":
    from config import AUDIT_DATA_DIR, MASTER_XLSX, RESULT_DIR

    run(AUDIT_DATA_DIR, MASTER_XLSX, RESULT_DIR)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd "tools/health-audit" && python3 -m pytest test_consistency.py -v`
Expected: 5 passed

- [ ] **Step 5: Run the full suite**

Run: `cd "tools/health-audit" && python3 -m pytest -v`
Expected: all tests pass (filter 6, state 4, schema 5, collector 5, consistency 5 = 25).

- [ ] **Step 6: Commit**

```bash
git add tools/health-audit/consistency.py tools/health-audit/test_consistency.py
git commit -m "feat(health-audit): cross-site consistency engine (truth + agreement)"
```

---

### Task 9: Full run to completion (operational)

**Files:** none (runtime outputs only).

**Interfaces:**
- Consumes: the runbook (`/health-audit-batch`), all tooling above.
- Produces: ~990 audited URLs, complete master workbook, consistency report.

- [ ] **Step 1: Scale-up batches** — after pilot approval, repeat the `/health-audit-batch` runbook loop each session: A-core first (~24 sessions × 12), then A-articles (~34 × 12), then B (~7 × 40). Aakash re-invokes or `/loop`s sessions.
- [ ] **Step 2: Failure sweep** — when pending hits zero, review all `failed` rows with Aakash: retry transient ones (`status` back to pending via `python3 state.py` mark, or re-take), accept permanent ones (e.g. gov-blocked fetches) explicitly.
- [ ] **Step 3: Fact-key merge pass** — before the consistency run, show Aakash `fact-keys.md`; merge near-duplicate keys by editing the affected JSONs (`ledger_entries[].fact_key`), guided by `near_duplicate_keys()` output.
- [ ] **Step 4: Run Task 2** — `python3 consistency.py`. Deliver the consistency report + Consistency sheet to Aakash with a prioritized fix list (core pages first).

---

## Self-Review (done at plan time)

- **Spec coverage:** filter/tiering → T1; state backbone → T1/T2; agent JSON contract → T3/T5; collector + append-only workbook + fact-key registry → T4; parallel workflow → T5; runbook/batching → T6; pilot gate → T7; consistency engine (truth + agreement, report + sheet) → T8; full-run ops + failure sweep + key merge → T9. Error handling embedded in T2 (reset-stale), T4 (validate/failed/tmp-save), T5 (tool-failure policy in prompt).
- **Placeholder scan:** none — every code step ships complete code; the one execution-time unknown (existing workbook headers) has a concrete inspection script and decision rule (T4 S5).
- **Type consistency:** `STATE_FIELDS` names = collector `SCORE_FIELDS` = `scores` keys = state CSV columns (`human_likeness` everywhere); `sample_audit()` in T3 is reused by T4 tests; prompt fields checked against `schema.py` mechanically (T5 S4).
