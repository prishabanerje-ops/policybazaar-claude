# social-performance (FB/IG Reporting) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `social-performance` Claude Code skill — a read-only Facebook + Instagram performance-reporting tool (Graph API pull → derived metrics → dated report + rolling spreadsheet → approval-gated email) — as a standalone, portable git repo that will be handed to another PolicyBazaar UAE team member via GitHub.

**Architecture:** A small set of focused, pure-function Python modules (`config`, `snapshot_store`, `graph_client`, `metrics`, `quality_score`, `report`, `email_draft`) wired together by one orchestrator (`run_report.py`), all under `scripts/`. Network I/O (Graph API) and side effects (file writes) are isolated to `graph_client.py`, `snapshot_store.py`, and `report.py` so `metrics.py` and `quality_score.py` stay pure and trivially testable. No posting/publish capability exists anywhere in this codebase — it is architecturally impossible to send a create/update/delete call to the Graph API from this client, not just policy.

**Tech Stack:** Python 3, stdlib `urllib` for HTTP (no `requests` — matches this workspace's existing skills), `openpyxl` for the rolling `.xlsx` (the one non-stdlib dependency, matching `tools/health-audit`'s convention), `pytest` + `unittest.mock`/`monkeypatch` for tests.

**Spec:** `docs/superpowers/specs/2026-09-11-social-performance-design.md`

## Global Constraints

- No committed secrets: `.env` and `config.json` are gitignored; only `.env.example` and `config.example.json` are committed, with no real credential or email values.
- No hard dependency on other skills in this workspace (e.g. `content-audit`) — everything this skill needs at runtime lives inside its own repo.
- No write/publish Graph API calls anywhere in `graph_client.py` — this client only ever performs `GET` requests.
- Every raised exception states what was attempted and with what input (this workspace's error-message convention).
- No snapshot tests for logic; test names describe behavior, not implementation (this workspace's testing convention).
- A metric that cannot be computed (no prior snapshot, a failed/unconfirmed Graph API field) is explicitly marked `"insufficient history"` or `"insufficient data"` — never a fabricated zero or omitted silently.
- The Meta Graph API version used throughout is `v21.0` — this was Meta's current stable version as late as 2025; **verify against https://developers.facebook.com/docs/graph-api/changelog at setup time** and update `GRAPH_API_VERSION` in `graph_client.py` if a newer version is current, since this was not re-confirmed live for this plan.

---

## File Structure

```
.claude/skills/social-performance/        # own git repo, gitignored from the main workspace repo
├── SKILL.md
├── README.md
├── .env.example
├── .gitignore
├── config.example.json
├── scripts/
│   ├── config.py
│   ├── snapshot_store.py
│   ├── graph_client.py
│   ├── metrics.py
│   ├── quality_score.py
│   ├── report.py
│   ├── email_draft.py
│   └── run_report.py
├── references/
│   └── metric-definitions.md
├── data/                                  # gitignored — created at runtime
│   ├── snapshots/
│   └── reports/
└── tests/
    ├── conftest.py
    ├── test_config.py
    ├── test_snapshot_store.py
    ├── test_graph_client.py
    ├── test_metrics.py
    ├── test_quality_score.py
    ├── test_report.py
    ├── test_email_draft.py
    └── test_run_report.py
```

---

### Task 1: Scaffold the skill repo + config loader

**Files:**
- Create: `.claude/skills/social-performance/.gitignore`
- Create: `.claude/skills/social-performance/.env.example`
- Create: `.claude/skills/social-performance/config.example.json`
- Create: `.claude/skills/social-performance/scripts/config.py`
- Create: `.claude/skills/social-performance/tests/conftest.py`
- Create: `.claude/skills/social-performance/tests/test_config.py`
- Modify: `.gitignore` (main workspace repo, add the new skill directory)

**Interfaces:**
- Produces: `config.ConfigError`, `config.parse_env_file(path: Path) -> dict`, `config.load_credentials(env_path: Path) -> dict` (keys: `page_access_token`, `page_id`, `ig_business_account_id`), `config.load_report_config(config_path: Path) -> dict` (keys: `cadence`, `recipients`, `report_period_days`), `config.CADENCE_DAYS: dict`

- [ ] **Step 1: Create the skill directory and its own git repo**

```bash
mkdir -p "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills/social-performance/scripts"
mkdir -p "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills/social-performance/tests"
mkdir -p "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills/social-performance/references"
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills/social-performance"
git init
```

- [ ] **Step 2: Write the skill repo's own `.gitignore`**

```gitignore
.env
config.json
data/
__pycache__/
*.pyc
.pytest_cache/
```

- [ ] **Step 3: Write `.env.example`**

```
# Copy this file to .env and fill in real values. .env is gitignored — never commit it.
# Generated by creating your own Meta Developer App: see README.md for the full walkthrough.
META_PAGE_ACCESS_TOKEN=
META_PAGE_ID=
META_IG_BUSINESS_ACCOUNT_ID=
```

- [ ] **Step 4: Write `config.example.json`**

```json
{
  "cadence": "weekly",
  "recipients": ["you@example.com"],
  "report_period_days": 7
}
```

- [ ] **Step 5: Add the skill directory to the main workspace's `.gitignore`**

Read the current `.gitignore` at `/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.gitignore` first (it already excludes `.claude/skills/linkedin/` — follow the same pattern), then add:

```gitignore
.claude/skills/social-performance/
```

- [ ] **Step 6: Write the failing tests for `config.py`**

```python
# tests/test_config.py
import json

import config as cfg


def test_parse_env_file_reads_key_value_pairs(tmp_path):
    env_path = tmp_path / ".env"
    env_path.write_text("META_PAGE_ID=123\nMETA_PAGE_ACCESS_TOKEN=abc\n")
    values = cfg.parse_env_file(env_path)
    assert values == {"META_PAGE_ID": "123", "META_PAGE_ACCESS_TOKEN": "abc"}


def test_parse_env_file_ignores_comments_and_blank_lines(tmp_path):
    env_path = tmp_path / ".env"
    env_path.write_text("# comment\n\nMETA_PAGE_ID=123\n")
    assert cfg.parse_env_file(env_path) == {"META_PAGE_ID": "123"}


def test_parse_env_file_returns_empty_dict_when_file_missing(tmp_path):
    assert cfg.parse_env_file(tmp_path / "missing.env") == {}


def test_load_credentials_raises_naming_missing_vars(tmp_path):
    env_path = tmp_path / ".env"
    env_path.write_text("META_PAGE_ID=123\n")
    try:
        cfg.load_credentials(env_path)
        assert False, "expected ConfigError"
    except cfg.ConfigError as e:
        assert "META_PAGE_ACCESS_TOKEN" in str(e)
        assert "META_IG_BUSINESS_ACCOUNT_ID" in str(e)


def test_load_credentials_succeeds_with_all_vars_present(tmp_path):
    env_path = tmp_path / ".env"
    env_path.write_text(
        "META_PAGE_ACCESS_TOKEN=tok\nMETA_PAGE_ID=1\nMETA_IG_BUSINESS_ACCOUNT_ID=2\n"
    )
    creds = cfg.load_credentials(env_path)
    assert creds == {
        "page_access_token": "tok", "page_id": "1", "ig_business_account_id": "2",
    }


def test_load_report_config_raises_when_file_missing(tmp_path):
    try:
        cfg.load_report_config(tmp_path / "missing.json")
        assert False, "expected ConfigError"
    except cfg.ConfigError as e:
        assert "missing.json" in str(e)


def test_load_report_config_raises_on_invalid_cadence(tmp_path):
    path = tmp_path / "config.json"
    path.write_text(json.dumps({"cadence": "hourly", "recipients": ["a@b.com"]}))
    try:
        cfg.load_report_config(path)
        assert False, "expected ConfigError"
    except cfg.ConfigError as e:
        assert "hourly" in str(e)


def test_load_report_config_raises_on_empty_recipients(tmp_path):
    path = tmp_path / "config.json"
    path.write_text(json.dumps({"cadence": "weekly", "recipients": []}))
    try:
        cfg.load_report_config(path)
        assert False, "expected ConfigError"
    except cfg.ConfigError as e:
        assert "recipient" in str(e)


def test_load_report_config_defaults_period_days_from_cadence(tmp_path):
    path = tmp_path / "config.json"
    path.write_text(json.dumps({"cadence": "monthly", "recipients": ["a@b.com"]}))
    result = cfg.load_report_config(path)
    assert result["report_period_days"] == 30
```

```python
# tests/conftest.py
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
```

- [ ] **Step 7: Run the tests to verify they fail**

Run: `cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills/social-performance" && python3 -m pytest tests/test_config.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'config'`

- [ ] **Step 8: Write `scripts/config.py`**

```python
"""Load and validate .env credentials and config.json settings for social-performance."""
import json
import os

REQUIRED_ENV_VARS = ["META_PAGE_ACCESS_TOKEN", "META_PAGE_ID", "META_IG_BUSINESS_ACCOUNT_ID"]
CADENCE_DAYS = {"daily": 1, "weekly": 7, "biweekly": 14, "monthly": 30}


class ConfigError(Exception):
    pass


def parse_env_file(path):
    """Parse a simple KEY=VALUE .env file into a dict. Ignores blank lines and '#' comments.
    Returns {} if path does not exist."""
    values = {}
    if not path.exists():
        return values
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        values[key.strip()] = value.strip()
    return values


def load_credentials(env_path):
    """Load Meta API credentials from env_path, merged with os.environ (os.environ wins).
    Raises ConfigError naming every missing required variable."""
    values = parse_env_file(env_path)
    values.update({k: v for k, v in os.environ.items() if k in REQUIRED_ENV_VARS})
    missing = [name for name in REQUIRED_ENV_VARS if not values.get(name)]
    if missing:
        raise ConfigError(
            f"Missing required credentials in {env_path}: {', '.join(missing)}. "
            f"Copy .env.example to .env and fill in real values."
        )
    return {
        "page_access_token": values["META_PAGE_ACCESS_TOKEN"],
        "page_id": values["META_PAGE_ID"],
        "ig_business_account_id": values["META_IG_BUSINESS_ACCOUNT_ID"],
    }


def load_report_config(config_path):
    """Load cadence + recipients + report_period_days from config_path (JSON).
    Raises ConfigError if the file is missing, cadence is invalid, or recipients is empty."""
    if not config_path.exists():
        raise ConfigError(
            f"Missing config file at {config_path}. "
            f"Copy config.example.json to config.json and fill in real values."
        )
    data = json.loads(config_path.read_text())
    cadence = data.get("cadence")
    if cadence not in CADENCE_DAYS:
        raise ConfigError(
            f"Invalid cadence {cadence!r} in {config_path}: must be one of {list(CADENCE_DAYS)}"
        )
    recipients = data.get("recipients") or []
    if not recipients:
        raise ConfigError(f"{config_path} must list at least one recipient email")
    report_period_days = data.get("report_period_days") or CADENCE_DAYS[cadence]
    return {"cadence": cadence, "recipients": recipients, "report_period_days": report_period_days}
```

- [ ] **Step 9: Run the tests to verify they pass**

Run: `python3 -m pytest tests/test_config.py -v`
Expected: PASS (9 tests)

- [ ] **Step 10: Commit**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills/social-performance"
git add .gitignore .env.example config.example.json scripts/config.py tests/
git commit -m "feat: scaffold social-performance skill and add config loader"
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude"
git add .gitignore
git commit -m "chore: ignore social-performance skill (own git repo)"
```

---

### Task 2: Snapshot history store

**Files:**
- Create: `.claude/skills/social-performance/scripts/snapshot_store.py`
- Create: `.claude/skills/social-performance/tests/test_snapshot_store.py`

**Interfaces:**
- Produces: `snapshot_store.SnapshotStoreError`, `snapshot_store.load_history(path) -> list`, `snapshot_store.save_history(path, history) -> None`, `snapshot_store.append_period(path, record: dict) -> list`, `snapshot_store.find_prior_period(history, target_date: str, days_back: int, tolerance_days: int = 3) -> dict | None`

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_snapshot_store.py
import snapshot_store as ss


def test_load_history_returns_empty_list_when_file_missing(tmp_path):
    assert ss.load_history(tmp_path / "missing.json") == []


def test_append_period_creates_file_and_persists_record(tmp_path):
    path = tmp_path / "facebook.json"
    history = ss.append_period(path, {"period_end": "2026-09-11", "reach": 100})
    assert history == [{"period_end": "2026-09-11", "reach": 100}]
    assert ss.load_history(path) == [{"period_end": "2026-09-11", "reach": 100}]


def test_append_period_replaces_existing_record_for_same_period_end(tmp_path):
    path = tmp_path / "facebook.json"
    ss.append_period(path, {"period_end": "2026-09-11", "reach": 100})
    history = ss.append_period(path, {"period_end": "2026-09-11", "reach": 200})
    assert history == [{"period_end": "2026-09-11", "reach": 200}]


def test_append_period_raises_without_period_end(tmp_path):
    try:
        ss.append_period(tmp_path / "facebook.json", {"reach": 100})
        assert False, "expected SnapshotStoreError"
    except ss.SnapshotStoreError as e:
        assert "period_end" in str(e)


def test_find_prior_period_returns_none_when_no_history():
    assert ss.find_prior_period([], "2026-09-11", days_back=7) is None


def test_find_prior_period_finds_closest_record_within_tolerance():
    history = [
        {"period_end": "2026-09-03", "reach": 50},
        {"period_end": "2026-08-20", "reach": 10},
    ]
    result = ss.find_prior_period(history, "2026-09-11", days_back=7, tolerance_days=3)
    assert result == {"period_end": "2026-09-03", "reach": 50}


def test_find_prior_period_returns_none_when_outside_tolerance():
    history = [{"period_end": "2026-08-01", "reach": 50}]
    result = ss.find_prior_period(history, "2026-09-11", days_back=7, tolerance_days=3)
    assert result is None
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_snapshot_store.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'snapshot_store'`

- [ ] **Step 3: Write `scripts/snapshot_store.py`**

```python
"""Local JSON history of period snapshots per account, used to compute period-over-period
deltas (growth rates, follower deltas) since the Graph API only exposes current totals,
not historical deltas across arbitrary windows."""
import json
from datetime import date, timedelta


class SnapshotStoreError(Exception):
    pass


def load_history(path):
    """Return the list of period records stored at path, or [] if the file does not exist
    yet (cold start)."""
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as e:
        raise SnapshotStoreError(f"Corrupt snapshot history at {path}: {e}")


def save_history(path, history):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(history, indent=2, sort_keys=True))


def append_period(path, record):
    """Append record (must include 'period_end': 'YYYY-MM-DD') to the history at path,
    replacing any existing record with the same period_end, and persist. Returns the
    updated history, sorted by period_end."""
    if "period_end" not in record:
        raise SnapshotStoreError(f"Snapshot record missing required 'period_end' key: {record}")
    history = load_history(path)
    history = [r for r in history if r.get("period_end") != record["period_end"]]
    history.append(record)
    history.sort(key=lambda r: r["period_end"])
    save_history(path, history)
    return history


def find_prior_period(history, target_date, days_back, tolerance_days=3):
    """Return the record in history whose period_end is closest to
    (target_date - days_back), within tolerance_days, or None if no such record exists
    (the caller should treat None as 'insufficient history')."""
    target = date.fromisoformat(target_date) - timedelta(days=days_back)
    best = None
    best_diff = None
    for record in history:
        record_date = date.fromisoformat(record["period_end"])
        diff = abs((record_date - target).days)
        if diff <= tolerance_days and (best_diff is None or diff < best_diff):
            best = record
            best_diff = diff
    return best
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_snapshot_store.py -v`
Expected: PASS (7 tests)

- [ ] **Step 5: Commit**

```bash
git add scripts/snapshot_store.py tests/test_snapshot_store.py
git commit -m "feat: add snapshot history store for period-over-period deltas"
```

---

### Task 3: Graph API client core (HTTP, pagination, media listing, classification)

**Files:**
- Create: `.claude/skills/social-performance/scripts/graph_client.py`
- Create: `.claude/skills/social-performance/tests/test_graph_client.py`

**Interfaces:**
- Consumes: nothing from earlier tasks
- Produces: `graph_client.GraphAPIError`, `graph_client.GraphClient(access_token)` with methods `_get(path, params=None) -> list`, `get_follower_count(account_id) -> int`, `list_media(account_id, since, until, edge="media") -> list[dict]`; module function `graph_client.classify_media_type(item, platform) -> str`; `graph_client._http_get(url)` (monkeypatch seam for tests); `graph_client.GRAPH_API_VERSION`, `graph_client.GRAPH_API_BASE`

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_graph_client.py
import graph_client as gc


def test_get_follows_pagination_and_concatenates_data(monkeypatch):
    pages = [
        {"data": [{"id": "1"}], "paging": {"next": "https://next.example/page2"}},
        {"data": [{"id": "2"}]},
    ]
    calls = []

    def fake_http_get(url):
        calls.append(url)
        return pages.pop(0)

    monkeypatch.setattr(gc, "_http_get", fake_http_get)
    client = gc.GraphClient("tok")
    items = client._get("/123/media", {"fields": "id"})
    assert items == [{"id": "1"}, {"id": "2"}]
    assert len(calls) == 2


def test_get_raises_graph_api_error_on_http_error(monkeypatch):
    def fake_http_get(url):
        raise gc.GraphAPIError(f"GET {url} failed: HTTP 400: boom")

    monkeypatch.setattr(gc, "_http_get", fake_http_get)
    client = gc.GraphClient("tok")
    try:
        client._get("/123/media")
        assert False, "expected GraphAPIError"
    except gc.GraphAPIError as e:
        assert "400" in str(e)


def test_get_follower_count_returns_value(monkeypatch):
    monkeypatch.setattr(gc, "_http_get", lambda url: {"followers_count": 42})
    client = gc.GraphClient("tok")
    assert client.get_follower_count("123") == 42


def test_get_follower_count_raises_when_field_missing(monkeypatch):
    monkeypatch.setattr(gc, "_http_get", lambda url: {})
    client = gc.GraphClient("tok")
    try:
        client.get_follower_count("123")
        assert False, "expected GraphAPIError"
    except gc.GraphAPIError as e:
        assert "followers_count" in str(e)


def test_list_media_uses_media_edge_for_instagram(monkeypatch):
    captured = {}

    def fake_get(self, path, params=None):
        captured["path"] = path
        captured["params"] = params
        return []

    monkeypatch.setattr(gc.GraphClient, "_get", fake_get)
    client = gc.GraphClient("tok")
    client.list_media("123", "2026-09-01", "2026-09-11", edge="media")
    assert captured["path"] == "/123/media"
    assert "media_type" in captured["params"]["fields"]


def test_list_media_uses_feed_edge_for_facebook(monkeypatch):
    captured = {}

    def fake_get(self, path, params=None):
        captured["path"] = path
        captured["params"] = params
        return []

    monkeypatch.setattr(gc.GraphClient, "_get", fake_get)
    client = gc.GraphClient("tok")
    client.list_media("123", "2026-09-01", "2026-09-11", edge="feed")
    assert captured["path"] == "/123/feed"
    assert "type" in captured["params"]["fields"]


def test_classify_media_type_instagram():
    assert gc.classify_media_type({"media_type": "VIDEO"}, "instagram") == "video"
    assert gc.classify_media_type({"media_type": "IMAGE"}, "instagram") == "static"
    assert gc.classify_media_type({"media_type": "CAROUSEL_ALBUM"}, "instagram") == "carousel"
    assert gc.classify_media_type({"media_type": "UNKNOWN"}, "instagram") == "other"


def test_classify_media_type_facebook():
    assert gc.classify_media_type({"type": "video"}, "facebook") == "video"
    assert gc.classify_media_type({"type": "photo"}, "facebook") == "static"
    assert gc.classify_media_type({"type": "link"}, "facebook") == "link"
    assert gc.classify_media_type({"type": "status"}, "facebook") == "other"


def test_classify_media_type_raises_on_unknown_platform():
    try:
        gc.classify_media_type({}, "tiktok")
        assert False, "expected ValueError"
    except ValueError as e:
        assert "tiktok" in str(e)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_graph_client.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'graph_client'`

- [ ] **Step 3: Write `scripts/graph_client.py`**

```python
"""Read-only Meta Graph API client for Facebook Page + Instagram Business Account
insights. This client has no publish/write methods by design — this tool is
reporting-only; posting is handled by an external agency (see the design spec)."""
import json
import urllib.error
import urllib.parse
import urllib.request

# Verify this against https://developers.facebook.com/docs/graph-api/changelog at setup
# time — v21.0 was Meta's current stable version as late as 2025 but was not re-confirmed
# live for this plan.
GRAPH_API_VERSION = "v21.0"
GRAPH_API_BASE = f"https://graph.facebook.com/{GRAPH_API_VERSION}"


class GraphAPIError(Exception):
    pass


def _http_get(url):
    """Thin wrapper around urllib so tests can monkeypatch a single function."""
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read()[:500] if hasattr(e, "read") else b""
        raise GraphAPIError(f"GET {url} failed: HTTP {e.code}: {body!r}")
    except urllib.error.URLError as e:
        raise GraphAPIError(f"GET {url} failed: {e.reason}")


class GraphClient:
    def __init__(self, access_token):
        self.access_token = access_token

    def _get(self, path, params=None):
        """GET path (e.g. '/{id}/media') with params, following pagination via the
        response's paging.next link, returning every page's 'data' items concatenated.
        Raises GraphAPIError (via _http_get) with the endpoint and status on failure."""
        params = dict(params or {})
        params["access_token"] = self.access_token
        url = f"{GRAPH_API_BASE}{path}?{urllib.parse.urlencode(params)}"
        items = []
        while url:
            body = _http_get(url)
            items.extend(body.get("data", []))
            url = body.get("paging", {}).get("next")
        return items

    def get_follower_count(self, account_id):
        """Return the current follower count for account_id (Page or IG Business Account)."""
        params = {"fields": "followers_count", "access_token": self.access_token}
        url = f"{GRAPH_API_BASE}/{account_id}?{urllib.parse.urlencode(params)}"
        body = _http_get(url)
        if "followers_count" not in body:
            raise GraphAPIError(
                f"GET {url} succeeded but response had no 'followers_count' field: {body}"
            )
        return body["followers_count"]

    def list_media(self, account_id, since, until, edge="media"):
        """List media/posts published on account_id between since and until (YYYY-MM-DD),
        via the given edge ('media' for Instagram, 'feed' for a Facebook Page)."""
        fields = "id,media_type,media_product_type,timestamp,permalink" if edge == "media" \
            else "id,type,attachments,created_time,permalink_url"
        return self._get(f"/{account_id}/{edge}", {
            "fields": fields, "since": since, "until": until,
        })


def classify_media_type(item, platform):
    """Classify a raw media/post dict as 'video', 'static', 'carousel', 'link', or 'other'.
    platform must be 'instagram' or 'facebook'."""
    if platform == "instagram":
        media_type = item.get("media_type", "")
        if media_type == "VIDEO":
            return "video"
        if media_type == "CAROUSEL_ALBUM":
            return "carousel"
        if media_type == "IMAGE":
            return "static"
        return "other"
    if platform == "facebook":
        post_type = item.get("type", "")
        if post_type == "video":
            return "video"
        if post_type == "photo":
            return "static"
        if post_type == "link":
            return "link"
        return "other"
    raise ValueError(f"Unknown platform {platform!r}: must be 'instagram' or 'facebook'")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_graph_client.py -v`
Expected: PASS (9 tests)

- [ ] **Step 5: Commit**

```bash
git add scripts/graph_client.py tests/test_graph_client.py
git commit -m "feat: add Graph API client core, pagination, and media classification"
```

---

### Task 4: Direct insights (confirmed-stable metrics only)

**Files:**
- Modify: `.claude/skills/social-performance/scripts/graph_client.py`
- Modify: `.claude/skills/social-performance/tests/test_graph_client.py`

**Interfaces:**
- Consumes: `GraphClient._get` (Task 3)
- Produces: `GraphClient.get_media_insights(media_id, metrics: list[str]) -> dict`, `GraphClient.get_account_insights(account_id, metrics, period="day", since=None, until=None) -> dict`

- [ ] **Step 1: Add the failing tests**

Append to `tests/test_graph_client.py`:

```python
def test_get_media_insights_maps_metric_names_to_first_value(monkeypatch):
    def fake_get(self, path, params=None):
        assert path == "/999/insights"
        assert params["metric"] == "reach,likes"
        return [
            {"name": "reach", "values": [{"value": 50}]},
            {"name": "likes", "values": [{"value": 3}]},
        ]

    monkeypatch.setattr(gc.GraphClient, "_get", fake_get)
    client = gc.GraphClient("tok")
    assert client.get_media_insights("999", ["reach", "likes"]) == {"reach": 50, "likes": 3}


def test_get_media_insights_returns_none_for_metric_with_no_values(monkeypatch):
    monkeypatch.setattr(
        gc.GraphClient, "_get",
        lambda self, path, params=None: [{"name": "reach", "values": []}],
    )
    client = gc.GraphClient("tok")
    assert client.get_media_insights("999", ["reach"]) == {"reach": None}


def test_get_account_insights_maps_metric_names_to_last_value(monkeypatch):
    monkeypatch.setattr(
        gc.GraphClient, "_get",
        lambda self, path, params=None: [
            {"name": "reach", "values": [{"value": 10}, {"value": 20}]},
        ],
    )
    client = gc.GraphClient("tok")
    assert client.get_account_insights("123", ["reach"]) == {"reach": 20}


def test_get_account_insights_passes_since_until_when_given(monkeypatch):
    captured = {}

    def fake_get(self, path, params=None):
        captured["params"] = params
        return []

    monkeypatch.setattr(gc.GraphClient, "_get", fake_get)
    client = gc.GraphClient("tok")
    client.get_account_insights("123", ["reach"], since="2026-09-01", until="2026-09-11")
    assert captured["params"]["since"] == "2026-09-01"
    assert captured["params"]["until"] == "2026-09-11"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_graph_client.py -v`
Expected: FAIL with `AttributeError: 'GraphClient' object has no attribute 'get_media_insights'`

- [ ] **Step 3: Add the methods to `scripts/graph_client.py`**

Add inside the `GraphClient` class, after `list_media`:

```python
    def get_media_insights(self, media_id, metrics):
        """Return {metric_name: value} for the given Instagram/Facebook media_id.
        Only pass metric names confirmed current in references/metric-definitions.md —
        this client does not validate metric names itself, since that list changes
        over time and is tracked in one place there."""
        items = self._get(f"/{media_id}/insights", {"metric": ",".join(metrics)})
        result = {}
        for item in items:
            values = item.get("values", [])
            result[item["name"]] = values[0]["value"] if values else None
        return result

    def get_account_insights(self, account_id, metrics, period="day", since=None, until=None):
        """Return {metric_name: value} for account-level insights, using the last value
        in each metric's series (the current/most recent value for the period)."""
        params = {"metric": ",".join(metrics), "period": period}
        if since:
            params["since"] = since
        if until:
            params["until"] = until
        items = self._get(f"/{account_id}/insights", params)
        result = {}
        for item in items:
            values = item.get("values", [])
            result[item["name"]] = values[-1]["value"] if values else None
        return result
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_graph_client.py -v`
Expected: PASS (13 tests)

- [ ] **Step 5: Commit**

```bash
git add scripts/graph_client.py tests/test_graph_client.py
git commit -m "feat: add media and account insights using confirmed-current metrics"
```

---

### Task 5: Repeat-engager fetch (Loyalty/Retention Rate input)

**Files:**
- Modify: `.claude/skills/social-performance/scripts/graph_client.py`
- Modify: `.claude/skills/social-performance/tests/test_graph_client.py`

**Interfaces:**
- Consumes: `GraphClient._get` (Task 3)
- Produces: `GraphClient.list_post_engagers(media_id) -> list[str]`

**Known risk (from the spec's Open Risks):** fetching commenter/liker identity lists may
be rate-limited or restricted for some account types — this is not yet verified against
the real account. This task implements the mechanism; the orchestrator (Task 11) is
responsible for treating an empty/failed result as `"insufficient data"`, never as zero.

- [ ] **Step 1: Add the failing tests**

Append to `tests/test_graph_client.py`:

```python
def test_list_post_engagers_dedupes_likers_and_commenters(monkeypatch):
    def fake_get(self, path, params=None):
        if path.endswith("/likes"):
            return [{"id": "u1"}, {"id": "u2"}]
        if path.endswith("/comments"):
            return [{"from": {"id": "u2"}}, {"from": {"id": "u3"}}]
        raise AssertionError(f"unexpected path {path}")

    monkeypatch.setattr(gc.GraphClient, "_get", fake_get)
    client = gc.GraphClient("tok")
    assert client.list_post_engagers("999") == ["u1", "u2", "u3"]


def test_list_post_engagers_handles_missing_from_field_on_comment(monkeypatch):
    def fake_get(self, path, params=None):
        if path.endswith("/likes"):
            return [{"id": "u1"}]
        if path.endswith("/comments"):
            return [{"text": "no from field"}]
        raise AssertionError(f"unexpected path {path}")

    monkeypatch.setattr(gc.GraphClient, "_get", fake_get)
    client = gc.GraphClient("tok")
    assert client.list_post_engagers("999") == ["u1"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_graph_client.py -v`
Expected: FAIL with `AttributeError: 'GraphClient' object has no attribute 'list_post_engagers'`

- [ ] **Step 3: Add the method to `scripts/graph_client.py`**

```python
    def list_post_engagers(self, media_id):
        """Return a de-duplicated, sorted list of user IDs who liked or commented on
        media_id. FEASIBILITY RISK (see the design spec's Open Risks): fetching
        commenter/liker identity lists may be rate-limited or restricted by Meta for
        some account types — verify this against the real account before relying on
        it. Callers must treat an empty result as potentially 'insufficient data'
        rather than assuming zero engagement."""
        likers = self._get(f"/{media_id}/likes", {"fields": "id"})
        commenters = self._get(f"/{media_id}/comments", {"fields": "from"})
        ids = {item["id"] for item in likers if "id" in item}
        ids |= {item["from"]["id"] for item in commenters if "from" in item and "id" in item["from"]}
        return sorted(ids)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_graph_client.py -v`
Expected: PASS (15 tests)

- [ ] **Step 5: Commit**

```bash
git add scripts/graph_client.py tests/test_graph_client.py
git commit -m "feat: add repeat-engager fetch for Loyalty/Retention Rate"
```

---

### Task 6: Video retention metrics (Hook Rate / Hold Rate / Average Watch Time) — unverified field names, graceful degradation

**Files:**
- Modify: `.claude/skills/social-performance/scripts/graph_client.py`
- Modify: `.claude/skills/social-performance/tests/test_graph_client.py`

**Interfaces:**
- Consumes: `GraphClient.get_media_insights` (Task 4)
- Produces: `GraphClient.get_video_retention_metrics(media_id) -> dict`, `graph_client.VIDEO_RETENTION_METRIC_CANDIDATES: list[str]`

**Why this task looks different from the others:** per the design spec's Open Risks
(updated 2026-09-11 after checking Meta's live docs), Hook Rate, Hold Rate, and Average
Watch Time are confirmed to exist as *concepts* for Instagram Reels (skip rate, average
watch time, total video view time) but their exact `metric=` parameter strings were not
confirmed. Rather than assert an unverified field name as fact, this method tries each
candidate individually and silently omits any that fail — it must be re-run against a
real IG Business Account early in rollout, with `references/metric-definitions.md`
updated to record which candidates actually worked (Task 12).

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_graph_client.py`:

```python
def test_get_video_retention_metrics_skips_failing_candidates(monkeypatch):
    def fake_get_media_insights(self, media_id, metrics):
        assert len(metrics) == 1
        if metrics[0] == "ig_reels_avg_watch_time":
            return {"ig_reels_avg_watch_time": 12.5}
        raise gc.GraphAPIError(f"unknown metric {metrics[0]}")

    monkeypatch.setattr(gc.GraphClient, "get_media_insights", fake_get_media_insights)
    client = gc.GraphClient("tok")
    result = client.get_video_retention_metrics("999")
    assert result == {"ig_reels_avg_watch_time": 12.5}


def test_get_video_retention_metrics_returns_empty_dict_when_all_candidates_fail(monkeypatch):
    def fake_get_media_insights(self, media_id, metrics):
        raise gc.GraphAPIError("unknown metric")

    monkeypatch.setattr(gc.GraphClient, "get_media_insights", fake_get_media_insights)
    client = gc.GraphClient("tok")
    assert client.get_video_retention_metrics("999") == {}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_graph_client.py -v`
Expected: FAIL with `AttributeError: 'GraphClient' object has no attribute 'get_video_retention_metrics'`

- [ ] **Step 3: Add to `scripts/graph_client.py`**

```python
# Candidate Reels metric names for Hook Rate / Hold Rate / Average Watch Time.
# NOT CONFIRMED against a live account as of 2026-09-11 — Meta's Instagram Platform
# docs describe these metrics conceptually (Reels skip rate = % of viewers who bail in
# the first 3 seconds; average watch time; total video view time) but do not give an
# exact `metric=` parameter string in the pages checked. Verify against a real IG
# Business Account with get_video_retention_metrics() before trusting these; update
# this list and references/metric-definitions.md with whichever names actually return
# data (Task 12).
VIDEO_RETENTION_METRIC_CANDIDATES = [
    "ig_reels_avg_watch_time",
    "ig_reels_video_view_total_time",
]
```

Add inside the `GraphClient` class, after `get_account_insights`:

```python
    def get_video_retention_metrics(self, media_id):
        """Attempt each candidate in VIDEO_RETENTION_METRIC_CANDIDATES individually
        against media_id. Returns {metric_name: value} only for candidates that
        succeeded — failed candidates are omitted, not raised, since some are expected
        to be wrong until verified against a live account. Never fabricates a value for
        a metric that failed."""
        result = {}
        for metric in VIDEO_RETENTION_METRIC_CANDIDATES:
            try:
                result.update(self.get_media_insights(media_id, [metric]))
            except GraphAPIError:
                continue
        return result
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_graph_client.py -v`
Expected: PASS (17 tests)

- [ ] **Step 5: Commit**

```bash
git add scripts/graph_client.py tests/test_graph_client.py
git commit -m "feat: add video retention metrics with graceful degradation for unverified fields"
```

---

### Task 7: Metrics engine (pure functions)

**Files:**
- Create: `.claude/skills/social-performance/scripts/metrics.py`
- Create: `.claude/skills/social-performance/tests/test_metrics.py`

**Interfaces:**
- Consumes: nothing at runtime (pure functions); conceptually consumes classified media
  items (`{"type": "video"|"static"|...}` from `graph_client.classify_media_type`) and
  snapshot records (`{"period_end", "reach", "total_followers"}` from `snapshot_store`)
- Produces: `metrics.INSUFFICIENT_HISTORY`, `metrics.INSUFFICIENT_DATA` (string sentinels),
  `metrics.video_output_count(media_items) -> int`,
  `metrics.static_output_count(media_items) -> int`,
  `metrics.engagement_rate(likes, comments, shares, saves, reach) -> float`,
  `metrics.reach_per_video(total_video_reach, video_count) -> float | str`,
  `metrics.reach_growth_rate(current_reach, prior_reach) -> float | str`,
  `metrics.net_new_followers(current_followers, prior_followers) -> int | str`,
  `metrics.repeat_engager_rate(engager_ids_by_post: dict[str, list[str]]) -> float | str`

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_metrics.py
import metrics as m


def test_video_output_count():
    items = [{"type": "video"}, {"type": "static"}, {"type": "video"}]
    assert m.video_output_count(items) == 2


def test_static_output_count():
    items = [{"type": "video"}, {"type": "static"}, {"type": "static"}]
    assert m.static_output_count(items) == 2


def test_engagement_rate_zero_when_reach_zero():
    assert m.engagement_rate(likes=5, comments=1, shares=0, saves=0, reach=0) == 0.0


def test_engagement_rate_computes_correctly():
    assert m.engagement_rate(likes=10, comments=5, shares=3, saves=2, reach=100) == 0.2


def test_reach_per_video_insufficient_data_when_no_videos():
    assert m.reach_per_video(total_video_reach=0, video_count=0) == m.INSUFFICIENT_DATA


def test_reach_per_video_computes_average():
    assert m.reach_per_video(total_video_reach=300, video_count=3) == 100.0


def test_reach_growth_rate_insufficient_history_when_no_prior():
    assert m.reach_growth_rate(current_reach=100, prior_reach=None) == m.INSUFFICIENT_HISTORY


def test_reach_growth_rate_insufficient_data_when_prior_zero():
    assert m.reach_growth_rate(current_reach=100, prior_reach=0) == m.INSUFFICIENT_DATA


def test_reach_growth_rate_computes_percentage():
    assert m.reach_growth_rate(current_reach=150, prior_reach=100) == 0.5


def test_net_new_followers_insufficient_history_when_no_prior():
    assert m.net_new_followers(current_followers=100, prior_followers=None) == m.INSUFFICIENT_HISTORY


def test_net_new_followers_computes_delta():
    assert m.net_new_followers(current_followers=120, prior_followers=100) == 20


def test_repeat_engager_rate_insufficient_data_when_empty():
    assert m.repeat_engager_rate({}) == m.INSUFFICIENT_DATA


def test_repeat_engager_rate_computes_fraction():
    engager_ids_by_post = {
        "post1": ["u1", "u2"],
        "post2": ["u2", "u3"],
    }
    # u2 engaged with both posts (repeat); u1 and u3 engaged with one each.
    assert m.repeat_engager_rate(engager_ids_by_post) == 1 / 3
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_metrics.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'metrics'`

- [ ] **Step 3: Write `scripts/metrics.py`**

```python
"""Pure functions computing social-performance metrics from raw Graph API data plus
snapshot history. No network calls live here — see graph_client.py for that boundary."""
from collections import Counter

INSUFFICIENT_HISTORY = "insufficient history"
INSUFFICIENT_DATA = "insufficient data"


def video_output_count(media_items):
    return sum(1 for item in media_items if item["type"] == "video")


def static_output_count(media_items):
    return sum(1 for item in media_items if item["type"] == "static")


def engagement_rate(likes, comments, shares, saves, reach):
    if reach == 0:
        return 0.0
    return (likes + comments + shares + saves) / reach


def reach_per_video(total_video_reach, video_count):
    if video_count == 0:
        return INSUFFICIENT_DATA
    return total_video_reach / video_count


def reach_growth_rate(current_reach, prior_reach):
    if prior_reach is None:
        return INSUFFICIENT_HISTORY
    if prior_reach == 0:
        return INSUFFICIENT_DATA
    return (current_reach - prior_reach) / prior_reach


def net_new_followers(current_followers, prior_followers):
    if prior_followers is None:
        return INSUFFICIENT_HISTORY
    return current_followers - prior_followers


def repeat_engager_rate(engager_ids_by_post):
    """engager_ids_by_post: {post_id: [user_id, ...]} for every post in the period.
    Returns the fraction of unique engagers across the period who engaged with more
    than one post, or INSUFFICIENT_DATA if there were no engagers at all."""
    counts = Counter()
    for ids in engager_ids_by_post.values():
        for uid in set(ids):
            counts[uid] += 1
    if not counts:
        return INSUFFICIENT_DATA
    repeat = sum(1 for c in counts.values() if c > 1)
    return repeat / len(counts)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_metrics.py -v`
Expected: PASS (13 tests)

- [ ] **Step 5: Commit**

```bash
git add scripts/metrics.py tests/test_metrics.py
git commit -m "feat: add pure metrics engine with insufficient-data/history sentinels"
```

---

### Task 8: Content Quality Score

**Files:**
- Create: `.claude/skills/social-performance/scripts/quality_score.py`
- Create: `.claude/skills/social-performance/tests/test_quality_score.py`

**Interfaces:**
- Produces: `quality_score.QualityScoreError`, `quality_score.DEFAULT_FAIL_FLOOR`,
  `quality_score.DEFAULT_PERFORMANCE_WEIGHT`, `quality_score.DEFAULT_TIME_SENSITIVITY_WEIGHT`,
  `quality_score.compute_quality_score(fact_check_passed, performance_percentile, time_sensitivity_score, fail_floor=DEFAULT_FAIL_FLOOR, performance_weight=DEFAULT_PERFORMANCE_WEIGHT, time_sensitivity_weight=DEFAULT_TIME_SENSITIVITY_WEIGHT) -> float`,
  `quality_score.average_quality_scores(scores: list[float]) -> float | str` (returns `"insufficient data"` if `scores` is empty)

**Note on the fact-check gate:** deciding *whether* a post passes fact-check and *what*
its time-sensitivity score is requires judgment about the post's actual content — that
judgment is made by Claude at the SKILL.md level (Task 13 documents the rubric), not by
this module. This module only implements the resulting formula, which is why it stays a
pure, unit-testable function taking `fact_check_passed`/`time_sensitivity_score` as inputs
rather than deriving them itself.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_quality_score.py
import quality_score as qs


def test_returns_fail_floor_when_fact_check_failed_regardless_of_inputs():
    result = qs.compute_quality_score(
        fact_check_passed=False, performance_percentile=1.0, time_sensitivity_score=1.0,
    )
    assert result == qs.DEFAULT_FAIL_FLOOR


def test_computes_weighted_blend_when_fact_check_passed():
    result = qs.compute_quality_score(
        fact_check_passed=True, performance_percentile=0.8, time_sensitivity_score=0.5,
    )
    assert result == 0.7 * 0.8 + 0.3 * 0.5


def test_raises_when_performance_percentile_out_of_range():
    try:
        qs.compute_quality_score(True, performance_percentile=1.5, time_sensitivity_score=0.5)
        assert False, "expected QualityScoreError"
    except qs.QualityScoreError as e:
        assert "performance_percentile" in str(e)


def test_raises_when_time_sensitivity_score_out_of_range():
    try:
        qs.compute_quality_score(True, performance_percentile=0.5, time_sensitivity_score=-0.1)
        assert False, "expected QualityScoreError"
    except qs.QualityScoreError as e:
        assert "time_sensitivity_score" in str(e)


def test_raises_when_weights_do_not_sum_to_one():
    try:
        qs.compute_quality_score(
            True, performance_percentile=0.5, time_sensitivity_score=0.5,
            performance_weight=0.5, time_sensitivity_weight=0.6,
        )
        assert False, "expected QualityScoreError"
    except qs.QualityScoreError as e:
        assert "weight" in str(e)


def test_average_quality_scores_insufficient_data_when_empty():
    assert qs.average_quality_scores([]) == qs.INSUFFICIENT_DATA


def test_average_quality_scores_computes_mean():
    # 0.25/0.5/0.75 are exact binary fractions, so the mean is bit-exact too —
    # avoids floating-point equality flakiness from non-exact decimals like 0.2/0.4/0.6.
    assert qs.average_quality_scores([0.25, 0.5, 0.75]) == 0.5
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_quality_score.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'quality_score'`

- [ ] **Step 3: Write `scripts/quality_score.py`**

```python
"""Content Quality Score: a fact-check pass/fail gate, then a weighted blend of
normalized post performance and time-sensitivity. Fact-checking and time-sensitivity
judgment happen at the SKILL.md level (Claude reviews each post's actual claims/timing);
this module only implements the resulting formula, keeping it a pure, testable function."""

INSUFFICIENT_DATA = "insufficient data"
DEFAULT_FAIL_FLOOR = 0.1
DEFAULT_PERFORMANCE_WEIGHT = 0.7
DEFAULT_TIME_SENSITIVITY_WEIGHT = 0.3


class QualityScoreError(Exception):
    pass


def compute_quality_score(
    fact_check_passed,
    performance_percentile,
    time_sensitivity_score,
    fail_floor=DEFAULT_FAIL_FLOOR,
    performance_weight=DEFAULT_PERFORMANCE_WEIGHT,
    time_sensitivity_weight=DEFAULT_TIME_SENSITIVITY_WEIGHT,
):
    """performance_percentile and time_sensitivity_score must each be in [0, 1].
    Raises QualityScoreError if either is out of range or if the weights don't sum to 1.
    A failed fact-check caps the score at fail_floor regardless of the other inputs."""
    if not (0.0 <= performance_percentile <= 1.0):
        raise QualityScoreError(
            f"performance_percentile must be in [0, 1], got {performance_percentile}"
        )
    if not (0.0 <= time_sensitivity_score <= 1.0):
        raise QualityScoreError(
            f"time_sensitivity_score must be in [0, 1], got {time_sensitivity_score}"
        )
    if abs((performance_weight + time_sensitivity_weight) - 1.0) > 1e-9:
        raise QualityScoreError(
            f"performance_weight + time_sensitivity_weight must equal 1.0, "
            f"got {performance_weight} + {time_sensitivity_weight}"
        )
    if not fact_check_passed:
        return fail_floor
    return performance_weight * performance_percentile + time_sensitivity_weight * time_sensitivity_score


def average_quality_scores(scores):
    """Mean of a period's per-post quality scores, or INSUFFICIENT_DATA if scores is
    empty (e.g. no posts published that period, or fact-check judgments not yet made)."""
    if not scores:
        return INSUFFICIENT_DATA
    return sum(scores) / len(scores)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_quality_score.py -v`
Expected: PASS (7 tests)

- [ ] **Step 5: Commit**

```bash
git add scripts/quality_score.py tests/test_quality_score.py
git commit -m "feat: add Content Quality Score formula (fact-check gate + weighted blend)"
```

---

### Task 9: Report rendering (dated Markdown + rolling Excel)

**Files:**
- Create: `.claude/skills/social-performance/scripts/report.py`
- Create: `.claude/skills/social-performance/tests/test_report.py`

**Interfaces:**
- Consumes: nothing from earlier tasks directly (takes plain dicts)
- Produces: `report.XLSX_COLUMNS: list[str]`,
  `report.render_markdown_report(period_label, platform_metrics: dict, output_path: Path) -> Path`,
  `report.append_to_rolling_xlsx(xlsx_path: Path, period_label, platform_metrics: dict) -> None`

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_report.py
from openpyxl import load_workbook

import report as rpt


def test_render_markdown_report_writes_expected_sections(tmp_path):
    output_path = tmp_path / "report.md"
    rpt.render_markdown_report(
        "2026-09-11",
        {"facebook": {"reach": 100}, "instagram": {"reach": 200}},
        output_path,
    )
    content = output_path.read_text()
    assert "2026-09-11" in content
    assert "Facebook" in content
    assert "Instagram" in content
    assert "reach" in content
    assert "100" in content
    assert "200" in content


def test_append_to_rolling_xlsx_creates_file_with_header_and_row(tmp_path):
    xlsx_path = tmp_path / "rolling.xlsx"
    rpt.append_to_rolling_xlsx(
        xlsx_path, "2026-09-11", {"facebook": {"reach": 100, "total_followers": 500}},
    )
    wb = load_workbook(xlsx_path)
    ws = wb["Facebook"]
    assert [c.value for c in ws[1]] == rpt.XLSX_COLUMNS
    assert ws.cell(row=2, column=1).value == "2026-09-11"


def test_append_to_rolling_xlsx_appends_without_overwriting_existing_rows(tmp_path):
    xlsx_path = tmp_path / "rolling.xlsx"
    rpt.append_to_rolling_xlsx(xlsx_path, "2026-09-04", {"facebook": {"reach": 50}})
    rpt.append_to_rolling_xlsx(xlsx_path, "2026-09-11", {"facebook": {"reach": 100}})
    wb = load_workbook(xlsx_path)
    ws = wb["Facebook"]
    assert ws.cell(row=2, column=1).value == "2026-09-04"
    assert ws.cell(row=3, column=1).value == "2026-09-11"


def test_append_to_rolling_xlsx_creates_new_sheet_per_platform(tmp_path):
    xlsx_path = tmp_path / "rolling.xlsx"
    rpt.append_to_rolling_xlsx(xlsx_path, "2026-09-11", {"facebook": {"reach": 100}})
    rpt.append_to_rolling_xlsx(xlsx_path, "2026-09-11", {"instagram": {"reach": 200}})
    wb = load_workbook(xlsx_path)
    assert set(wb.sheetnames) == {"Facebook", "Instagram"}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_report.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'report'`

- [ ] **Step 3: Write `scripts/report.py`**

```python
"""Renders the period report as a dated Markdown file plus an append to a rolling,
undated Excel workbook (one sheet per platform) — matching this workspace's existing
content-audit report convention: dated .md per run, rolling .xlsx appended, never
overwritten."""
from openpyxl import Workbook, load_workbook

XLSX_COLUMNS = [
    "period_end", "video_output", "static_output", "content_quality_score",
    "reach_growth_rate", "reach", "reach_per_video", "engagement_rate",
    "net_new_followers", "repeat_engager_rate", "total_followers",
]


def render_markdown_report(period_label, platform_metrics, output_path):
    """platform_metrics: {"facebook": {metric_name: value, ...}, "instagram": {...}}.
    Writes a Markdown report to output_path and returns output_path."""
    lines = [f"# Social Performance Report — {period_label}", ""]
    for platform, platform_data in platform_metrics.items():
        lines.append(f"## {platform.title()}")
        lines.append("")
        lines.append("| Metric | Value |")
        lines.append("|---|---|")
        for name, value in platform_data.items():
            lines.append(f"| {name} | {value} |")
        lines.append("")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines))
    return output_path


def append_to_rolling_xlsx(xlsx_path, period_label, platform_metrics):
    """Appends one row per platform in platform_metrics to xlsx_path (one sheet per
    platform), creating the workbook/sheets if they don't exist yet. Never rewrites or
    removes existing rows."""
    xlsx_path.parent.mkdir(parents=True, exist_ok=True)
    if xlsx_path.exists():
        wb = load_workbook(xlsx_path)
    else:
        wb = Workbook()
        wb.remove(wb.active)
    for platform, platform_data in platform_metrics.items():
        sheet_name = platform.title()
        if sheet_name not in wb.sheetnames:
            ws = wb.create_sheet(sheet_name)
            ws.append(XLSX_COLUMNS)
        else:
            ws = wb[sheet_name]
        row = [period_label] + [platform_data.get(col, "") for col in XLSX_COLUMNS[1:]]
        ws.append(row)
    wb.save(xlsx_path)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_report.py -v`
Expected: PASS (4 tests)

- [ ] **Step 5: Commit**

```bash
git add scripts/report.py tests/test_report.py
git commit -m "feat: add dated Markdown + rolling Excel report rendering"
```

---

### Task 10: Email draft rendering

**Files:**
- Create: `.claude/skills/social-performance/scripts/email_draft.py`
- Create: `.claude/skills/social-performance/tests/test_email_draft.py`

**Interfaces:**
- Produces: `email_draft.render_email_draft(period_label, platform_metrics: dict, recipients: list[str]) -> dict` (keys: `subject`, `body`, `recipients`)

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_email_draft.py
import pytest

import email_draft as ed


def test_render_email_draft_raises_without_recipients():
    with pytest.raises(ValueError, match="recipient"):
        ed.render_email_draft("2026-09-11", {"facebook": {"reach": 100}}, [])


def test_render_email_draft_includes_subject_period_and_all_metrics():
    draft = ed.render_email_draft(
        "2026-09-11", {"facebook": {"reach": 100}}, ["a@b.com", "c@d.com"],
    )
    assert "2026-09-11" in draft["subject"]
    assert "Facebook" in draft["body"]
    assert "reach" in draft["body"]
    assert "100" in draft["body"]
    assert draft["recipients"] == ["a@b.com", "c@d.com"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_email_draft.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'email_draft'`

- [ ] **Step 3: Write `scripts/email_draft.py`**

```python
"""Renders the email subject/body for a report. Sending itself happens at the skill
level via the installer's own authorized Gmail connector, after explicit human
approval — this module only produces draft content and never sends anything."""


def render_email_draft(period_label, platform_metrics, recipients):
    """Returns {"subject": str, "body": str, "recipients": list[str]}.
    Raises ValueError if recipients is empty."""
    if not recipients:
        raise ValueError("render_email_draft requires at least one recipient")
    subject = f"Social Performance Report — {period_label}"
    lines = [f"Social Performance Report for {period_label}", ""]
    for platform, platform_data in platform_metrics.items():
        lines.append(f"{platform.title()}:")
        for name, value in platform_data.items():
            lines.append(f"  {name}: {value}")
        lines.append("")
    return {"subject": subject, "body": "\n".join(lines), "recipients": list(recipients)}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_email_draft.py -v`
Expected: PASS (2 tests)

- [ ] **Step 5: Commit**

```bash
git add scripts/email_draft.py tests/test_email_draft.py
git commit -m "feat: add email draft rendering (draft-only, never sends)"
```

---

### Task 11: Report orchestrator (`run_report.py`)

**Files:**
- Create: `.claude/skills/social-performance/scripts/run_report.py`
- Create: `.claude/skills/social-performance/tests/test_run_report.py`

**Interfaces:**
- Consumes: `config.load_credentials`, `config.load_report_config` (Task 1);
  `snapshot_store.load_history`, `snapshot_store.find_prior_period`, `snapshot_store.append_period` (Task 2);
  `graph_client.GraphClient`, `graph_client.classify_media_type` (Tasks 3-6);
  `metrics.*` (Task 7); `quality_score.average_quality_scores` (Task 8);
  `report.render_markdown_report`, `report.append_to_rolling_xlsx` (Task 9);
  `email_draft.render_email_draft` (Task 10)
- Produces: `run_report.build_platform_metrics(client, account_id, platform, period_end, period_days, snapshot_path, judgments=None) -> dict`,
  `run_report.run(period_end, skill_dir, judgments=None) -> dict` (keys: `markdown_path`, `xlsx_path`, `email_draft`),
  `run_report.cli_main(argv=None) -> int`

**On Content Quality Score:** since fact-check/time-sensitivity judgment requires
reviewing each post's actual content (a job for Claude, per Task 13's rubric — not this
mechanical script), `run` accepts an optional `judgments` dict
(`{post_id: {"fact_check_passed": bool, "time_sensitivity_score": float}}`). Performance
percentile is computed mechanically (each post's engagement rate ranked against the
period's posts on the same platform). When `judgments` is omitted, Content Quality Score
is reported as `"insufficient data (fact-check not yet performed)"` rather than a
fabricated number — SKILL.md's flow (Task 13) runs this twice: once to gather post
content for Claude to review, once with `judgments` filled in for the final report.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_run_report.py
from pathlib import Path
from unittest.mock import MagicMock

import pytest

import run_report as rr


def _fake_client(media_items, insights_by_id, follower_count, engagers_by_id=None):
    client = MagicMock()
    client.list_media.return_value = media_items
    client.get_media_insights.side_effect = lambda media_id, metrics: insights_by_id[media_id]
    client.get_follower_count.return_value = follower_count
    client.list_post_engagers.side_effect = lambda media_id: (engagers_by_id or {}).get(media_id, [])
    return client


def test_build_platform_metrics_computes_expected_shape(tmp_path):
    media_items = [
        {"id": "p1", "media_type": "IMAGE"},
        {"id": "p2", "media_type": "VIDEO"},
    ]
    insights_by_id = {
        "p1": {"reach": 100, "likes": 10, "comments": 2, "saved": 1, "shares": 0},
        "p2": {"reach": 200, "likes": 20, "comments": 5, "saved": 2, "shares": 1},
    }
    client = _fake_client(media_items, insights_by_id, follower_count=1000)
    snapshot_path = tmp_path / "instagram.json"

    result = rr.build_platform_metrics(
        client, "ig123", "instagram", "2026-09-11", 7, snapshot_path,
    )

    assert result["video_output"] == 1
    assert result["static_output"] == 1
    assert result["reach"] == 300
    assert result["reach_per_video"] == 200.0
    assert result["total_followers"] == 1000
    assert result["reach_growth_rate"] == "insufficient history"
    assert result["net_new_followers"] == "insufficient history"
    # A snapshot must now exist for next period's comparison.
    history = rr.snapshot_store.load_history(snapshot_path)
    assert history == [{"period_end": "2026-09-11", "reach": 300, "total_followers": 1000}]


def test_build_platform_metrics_computes_quality_score_when_judgments_given(tmp_path):
    media_items = [
        {"id": "p1", "media_type": "IMAGE"},
        {"id": "p2", "media_type": "VIDEO"},
    ]
    insights_by_id = {
        # engagement rate p1 = (10+2+0+1)/100 = 0.13, p2 = (20+5+1+2)/200 = 0.14
        "p1": {"reach": 100, "likes": 10, "comments": 2, "saved": 1, "shares": 0},
        "p2": {"reach": 200, "likes": 20, "comments": 5, "saved": 2, "shares": 1},
    }
    client = _fake_client(media_items, insights_by_id, follower_count=1000)
    judgments = {
        "p1": {"fact_check_passed": True, "time_sensitivity_score": 1.0},
        "p2": {"fact_check_passed": True, "time_sensitivity_score": 1.0},
    }

    result = rr.build_platform_metrics(
        client, "ig123", "instagram", "2026-09-11", 7, tmp_path / "instagram.json",
        judgments=judgments,
    )

    # p1 has the lower engagement rate (percentile 0.5), p2 the higher (percentile 1.0):
    # scores = 0.7*0.5 + 0.3*1.0 = 0.65, and 0.7*1.0 + 0.3*1.0 = 1.0 -> mean 0.825
    assert result["content_quality_score"] == pytest.approx(0.825)


def test_run_writes_report_files_and_returns_email_draft(tmp_path, monkeypatch):
    skill_dir = tmp_path
    (skill_dir / ".env").write_text(
        "META_PAGE_ACCESS_TOKEN=tok\nMETA_PAGE_ID=1\nMETA_IG_BUSINESS_ACCOUNT_ID=2\n"
    )
    (skill_dir / "config.json").write_text(
        '{"cadence": "weekly", "recipients": ["a@b.com"], "report_period_days": 7}'
    )
    monkeypatch.setattr(
        rr, "build_platform_metrics",
        lambda client, account_id, platform, period_end, period_days, snapshot_path, judgments=None: {
            "reach": 100, "total_followers": 50,
        },
    )
    monkeypatch.setattr(rr.graph_client, "GraphClient", lambda token: MagicMock())

    result = rr.run("2026-09-11", skill_dir=skill_dir)

    assert Path(result["markdown_path"]).exists()
    assert Path(result["xlsx_path"]).exists()
    assert result["email_draft"]["recipients"] == ["a@b.com"]
    assert "2026-09-11" in result["email_draft"]["subject"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest tests/test_run_report.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'run_report'`

- [ ] **Step 3: Write `scripts/run_report.py`**

```python
#!/usr/bin/env python3
"""CLI orchestrator: loads config/credentials, pulls Graph API data for both platforms,
computes every metric, renders the report, and returns an email draft — it never sends
anything itself. SKILL.md (Task 13) is responsible for showing the draft to the user and
calling the Gmail connector only after explicit approval."""
import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

import config as cfg
import email_draft
import graph_client
import metrics
import quality_score
import report
import snapshot_store

SKILL_DIR = Path(__file__).resolve().parent.parent


def build_platform_metrics(client, account_id, platform, period_end, period_days, snapshot_path, judgments=None):
    since = (date.fromisoformat(period_end) - timedelta(days=period_days)).isoformat()
    edge = "media" if platform == "instagram" else "feed"
    raw_items = client.list_media(account_id, since, period_end, edge=edge)
    typed_items = [
        {**item, "type": graph_client.classify_media_type(item, platform)} for item in raw_items
    ]

    video_items = [i for i in typed_items if i["type"] == "video"]
    total_video_reach = 0
    reach_total = likes_total = comments_total = shares_total = saves_total = 0
    engager_ids_by_post = {}
    engagement_rates_by_post = {}

    for item in typed_items:
        insights = client.get_media_insights(item["id"], ["reach", "likes", "comments", "saved", "shares"])
        item_reach = insights.get("reach") or 0
        item_likes = insights.get("likes") or 0
        item_comments = insights.get("comments") or 0
        item_shares = insights.get("shares") or 0
        item_saves = insights.get("saved") or 0

        reach_total += item_reach
        likes_total += item_likes
        comments_total += item_comments
        shares_total += item_shares
        saves_total += item_saves
        if item["type"] == "video":
            total_video_reach += item_reach

        engager_ids_by_post[item["id"]] = client.list_post_engagers(item["id"])
        engagement_rates_by_post[item["id"]] = metrics.engagement_rate(
            item_likes, item_comments, item_shares, item_saves, item_reach,
        )

    follower_count = client.get_follower_count(account_id)
    history = snapshot_store.load_history(snapshot_path)
    prior = snapshot_store.find_prior_period(history, period_end, period_days)
    prior_reach = prior["reach"] if prior else None
    prior_followers = prior["total_followers"] if prior else None

    quality_scores = []
    if judgments:
        rates = sorted(engagement_rates_by_post.values())
        for post_id, judgment in judgments.items():
            rate = engagement_rates_by_post.get(post_id)
            if rate is None:
                continue
            percentile = (rates.index(rate) + 1) / len(rates) if rates else 0.0
            quality_scores.append(quality_score.compute_quality_score(
                fact_check_passed=judgment["fact_check_passed"],
                performance_percentile=percentile,
                time_sensitivity_score=judgment["time_sensitivity_score"],
            ))

    result = {
        "video_output": metrics.video_output_count(typed_items),
        "static_output": metrics.static_output_count(typed_items),
        "content_quality_score": (
            quality_score.average_quality_scores(quality_scores) if judgments
            else "insufficient data (fact-check not yet performed)"
        ),
        "reach": reach_total,
        "reach_per_video": metrics.reach_per_video(total_video_reach, len(video_items)),
        "engagement_rate": metrics.engagement_rate(
            likes_total, comments_total, shares_total, saves_total, reach_total,
        ),
        "reach_growth_rate": metrics.reach_growth_rate(reach_total, prior_reach),
        "net_new_followers": metrics.net_new_followers(follower_count, prior_followers),
        "repeat_engager_rate": metrics.repeat_engager_rate(engager_ids_by_post),
        "total_followers": follower_count,
    }
    snapshot_store.append_period(snapshot_path, {
        "period_end": period_end, "reach": reach_total, "total_followers": follower_count,
    })
    return result


def run(period_end, skill_dir=SKILL_DIR, judgments=None):
    creds = cfg.load_credentials(skill_dir / ".env")
    report_cfg = cfg.load_report_config(skill_dir / "config.json")
    client = graph_client.GraphClient(creds["page_access_token"])

    platform_metrics = {
        "facebook": build_platform_metrics(
            client, creds["page_id"], "facebook", period_end,
            report_cfg["report_period_days"], skill_dir / "data/snapshots/facebook.json",
            judgments=judgments.get("facebook") if judgments else None,
        ),
        "instagram": build_platform_metrics(
            client, creds["ig_business_account_id"], "instagram", period_end,
            report_cfg["report_period_days"], skill_dir / "data/snapshots/instagram.json",
            judgments=judgments.get("instagram") if judgments else None,
        ),
    }

    md_path = skill_dir / f"data/reports/report-{period_end}.md"
    xlsx_path = skill_dir / "data/reports/rolling-report.xlsx"
    report.render_markdown_report(period_end, platform_metrics, md_path)
    report.append_to_rolling_xlsx(xlsx_path, period_end, platform_metrics)
    draft = email_draft.render_email_draft(period_end, platform_metrics, report_cfg["recipients"])
    return {"markdown_path": str(md_path), "xlsx_path": str(xlsx_path), "email_draft": draft}


def cli_main(argv=None):
    parser = argparse.ArgumentParser(description="Generate the social-performance report.")
    parser.add_argument("--period-end", default=date.today().isoformat())
    parser.add_argument("--judgments-file", default=None,
                         help="Path to a JSON file of per-platform fact-check/time-sensitivity judgments")
    args = parser.parse_args(argv)
    judgments = json.loads(Path(args.judgments_file).read_text()) if args.judgments_file else None
    result = run(args.period_end, judgments=judgments)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(cli_main())
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest tests/test_run_report.py -v`
Expected: PASS (3 tests)

- [ ] **Step 5: Run the full test suite**

Run: `python3 -m pytest -v`
Expected: PASS (all tests across every module — roughly 54 tests)

- [ ] **Step 6: Commit**

```bash
git add scripts/run_report.py tests/test_run_report.py
git commit -m "feat: add run_report orchestrator tying all modules together"
```

---

### Task 12: `references/metric-definitions.md`

**Files:**
- Create: `.claude/skills/social-performance/references/metric-definitions.md`

**Deliverable:** one row per metric in the spec's table, with the exact Graph API field(s)
or computation used, and a status column. This is the single place the "needs
verification" items get resolved once real API access exists — Task 6 and Task 4's
docstrings both point here.

- [ ] **Step 1: Write `references/metric-definitions.md`**

```markdown
# Metric Definitions & Verification Status

Status values: `verified` (confirmed against Meta's live docs or a real API call),
`needs verification` (implemented but not yet confirmed against a real account),
`computed` (derived entirely from other confirmed values, no direct API dependency).

| Metric | Platform(s) | Source | Status |
|---|---|---|---|
| Video Output per Week | FB, IG | `graph_client.classify_media_type` + `metrics.video_output_count` | computed |
| Static Output per Week | FB, IG | `graph_client.classify_media_type` + `metrics.static_output_count` | computed |
| Content Quality Score | FB, IG | `quality_score.compute_quality_score` (fact-check judgment from SKILL.md + mechanical performance percentile) | computed |
| Total Reach Growth Rate | FB, IG | `metrics.reach_growth_rate` using `snapshot_store` history | computed |
| Reach | FB, IG | Graph API `insights` metric `reach` | verified (2026-09-11, Meta Instagram Platform docs) |
| Reach per Video | FB, IG | `reach` averaged over video posts (`metrics.reach_per_video`) — replaces "Impressions per Video" since `impressions` is deprecated for media created after 2024-07-02 | verified (2026-09-11) |
| Hook Rate | IG | `graph_client.VIDEO_RETENTION_METRIC_CANDIDATES` via `get_video_retention_metrics` | needs verification |
| Hold Rate | IG | `graph_client.VIDEO_RETENTION_METRIC_CANDIDATES` via `get_video_retention_metrics` | needs verification |
| Average Watch Time | FB, IG | `graph_client.VIDEO_RETENTION_METRIC_CANDIDATES` via `get_video_retention_metrics` | needs verification |
| AVT (Long Videos) | FB | Same candidates, filtered by video duration once a duration field is confirmed | needs verification |
| AVT (Short Videos) | FB | Same candidates, filtered by video duration once a duration field is confirmed | needs verification |
| Engagement Rate (ER) | FB, IG | `metrics.engagement_rate` from `likes`, `comments`, `shares`, `saved`, `reach` | verified (2026-09-11) |
| Total Shares | IG | Graph API `insights` metric `shares` | verified (2026-09-11) |
| Net New Followers MoM | FB, IG | `metrics.net_new_followers` using `snapshot_store` history | computed |
| Loyalty/Retention Rate | FB, IG | `metrics.repeat_engager_rate` from `graph_client.list_post_engagers` | needs verification (rate-limit/availability of engager identity lists not yet confirmed at scale) |
| Total Followers | FB, IG | Graph API `followers_count` field on the account object | verified (2026-09-11) |

## First-live-run checklist

Run through this once real Meta credentials exist, before trusting a report for
decision-making:

1. Call `GraphClient(token).get_video_retention_metrics(<a real video media id>)` and
   record which of `VIDEO_RETENTION_METRIC_CANDIDATES` actually returned data. Update
   the table above and `graph_client.py`'s candidate list/docstring accordingly.
2. Call `GraphClient(token).list_post_engagers(<a real media id>)` on a post with known
   engagement and confirm it returns a non-empty, sensible list (not rate-limited/empty
   for reasons unrelated to actual engagement).
3. Confirm `GRAPH_API_VERSION` in `graph_client.py` is still current at
   https://developers.facebook.com/docs/graph-api/changelog.
```

- [ ] **Step 2: Commit**

```bash
git add references/metric-definitions.md
git commit -m "docs: add metric definitions and verification status reference"
```

---

### Task 13: `SKILL.md`

**Files:**
- Create: `.claude/skills/social-performance/SKILL.md`

**Deliverable:** the skill entry point — frontmatter, invocation, the fact-check/
time-sensitivity rubric Claude follows (self-contained, no dependency on `content-audit`),
and the full report-generation flow including the two-pass Content Quality Score handoff
and the approval-gated email/cron behavior from the spec.

- [ ] **Step 1: Write `SKILL.md`**

```markdown
---
name: social-performance
description: >
  Generates a Facebook + Instagram performance report using the official Meta Graph
  API (read-only — posting is handled by an external agency and is out of scope).
  Pulls reach, engagement, follower growth, and a custom Content Quality Score, then
  renders a dated Markdown report plus an append to a rolling Excel workbook. Always
  drafts the report email and asks for explicit approval before sending anything,
  whether run manually or via a scheduled cron job. Invoke as "/social-performance
  report" or "/social-performance report --period-end YYYY-MM-DD".
user-invokable: true
argument-hint: "report [--period-end YYYY-MM-DD]"
metadata:
  author: Aakash Srivastava
  version: "1.0.0"
  category: social
---

# Social Performance Report

One mode in v1: **report** — generate the Facebook + Instagram performance report for
the configured cadence's period, ending on `--period-end` (default: today).

## Prerequisites

Before first use, `.env` and `config.json` must exist (copied from `.env.example` and
`config.example.json` and filled in) — see `README.md` for the full setup walkthrough.
If either file is missing, `scripts/config.py` raises a clear error naming exactly
what's missing; surface that error to the user rather than guessing values.

## Flow

This runs in two passes because the Content Quality Score's fact-check and
time-sensitivity components require reviewing each post's actual content — a judgment
call, not something a mechanical script can make on its own.

### Pass 1 — pull data, gather posts for review

```bash
cd "$(dirname "$0")"  # the skill's own directory
python3 scripts/run_report.py --period-end <period-end>
```

This writes the dated Markdown report and rolling `.xlsx` with every metric except
Content Quality Score, which will read `"insufficient data (fact-check not yet
performed)"` at this point. It prints an email draft as JSON — do not send it yet.

### Fact-check + time-sensitivity review (Claude's judgment, self-contained)

For each post that was included in the period (read them from the Markdown report or
directly via the Graph API media list), assess:

1. **Fact-check (pass/fail):** does the post make any factual claim that is
   unverifiable or contradicted by better evidence — insurance premium figures,
   regulatory citations, coverage claims, statistics? If a claim can't be verified,
   treat it as a fail rather than assuming it's correct. This mirrors the standard
   this workspace already holds written content to (see CLAUDE.md's Data Integrity
   section) — never wave through an unverified figure just because it's a social post.
2. **Time-sensitivity (0.0-1.0):** was the post still relevant/current when it went
   live? A post referencing a seasonal offer, a regulatory deadline, or a promotional
   window that had already passed at publish time scores low (near 0.0); a
   general-evergreen or genuinely timely post scores high (near 1.0). Use judgment —
   this is a graded score, not a binary.

Write these judgments to a JSON file, one entry per post ID, per platform:

```json
{
  "facebook": {
    "<post_id>": {"fact_check_passed": true, "time_sensitivity_score": 0.8}
  },
  "instagram": {
    "<post_id>": {"fact_check_passed": false, "time_sensitivity_score": 0.3}
  }
}
```

### Pass 2 — final report with Content Quality Score

```bash
python3 scripts/run_report.py --period-end <period-end> --judgments-file <path-to-judgments.json>
```

This re-runs the full pull (Graph API insights are re-fetched; this is a reporting
tool, not a high-frequency job, so re-fetching is simpler and safer than caching raw
insights between passes) and produces the final report with Content Quality Score
computed, plus the final email draft.

## Sending the email — always requires explicit approval

Whether Pass 2 was triggered manually or by a scheduled cron job (see README.md for
cron setup), **never call the Gmail connector to send without the user's explicit
go-ahead first**:

- **Manual invocation:** show the email draft (subject + body) in the response and ask
  "send this now?" before sending.
- **Cron-triggered invocation:** generate the report, then send a notification to the
  installer summarizing what was generated (not the full email) and wait — do not send
  the email until the installer responds with approval in a follow-up turn.

Only after approval, send via the installer's own authorized Gmail connector, to the
recipients in `config.json`.

## Non-goals (do not do these even if asked in passing)

- No posting/publishing to Facebook or Instagram — `graph_client.py` has no write
  methods; do not add any, even for a one-off "just post this" request. Posting is
  owned by an external agency, per the design spec.
- No personal-profile automation.
- No relying on the `content-audit` skill for the fact-check step — this skill must
  work standalone even if `content-audit` isn't installed on the target machine.
```

- [ ] **Step 2: Commit**

```bash
git add SKILL.md
git commit -m "docs: add SKILL.md with report flow, fact-check rubric, and approval gate"
```

---

### Task 14: `README.md` (setup walkthrough)

**Files:**
- Create: `.claude/skills/social-performance/README.md`

**Deliverable:** a self-sufficient setup guide — this is the document the other team
member follows with zero other context, per the spec's portability requirement.

- [ ] **Step 1: Write `README.md`**

```markdown
# social-performance

Facebook + Instagram performance reporting via the official Meta Graph API. Read-only —
does not post or publish anything. See `docs/superpowers/specs/2026-09-11-social-performance-design.md`
in the main PolicyBazaar Claude repo for the full design rationale (not included in this
repo, since this repo is meant to stand alone).

## One-time setup (do this yourself — it can't be done on your behalf)

### 1. Create a Meta Developer App

1. Go to https://developers.facebook.com/apps and create a new app (type: "Business").
2. Under "Add products," add **Facebook Login for Business** (or the relevant Instagram
   product flow current at the time — Meta's app-creation UI changes; look for whatever
   lets you request Page and Instagram permissions).
3. Request these permissions for your app: `pages_read_engagement`, `read_insights`,
   `instagram_basic`, `instagram_manage_insights`.
4. Under your app's Business settings, link the PolicyBazaar UAE Facebook Page and its
   connected Instagram Business Account.
5. Generate a long-lived Page access token (via the Graph API Explorer or your app's
   token generation flow — exchange a short-lived token for a long-lived one using the
   `oauth/access_token` endpoint with `grant_type=fb_exchange_token`).
6. Note down: the Page access token, the Facebook Page ID, and the Instagram Business
   Account ID linked to that Page (find it via `GET /{page-id}?fields=instagram_business_account`).

### 2. Configure credentials

```bash
cp .env.example .env
```

Edit `.env` and fill in the three values from step 1:

```
META_PAGE_ACCESS_TOKEN=<your long-lived token>
META_PAGE_ID=<your page id>
META_IG_BUSINESS_ACCOUNT_ID=<your ig business account id>
```

`.env` is gitignored — never commit it.

### 3. Configure cadence and recipients

```bash
cp config.example.json config.json
```

Edit `config.json`:

```json
{
  "cadence": "weekly",
  "recipients": ["you@example.com", "someone-else@example.com"],
  "report_period_days": 7
}
```

`cadence` must be one of `daily`, `weekly`, `biweekly`, `monthly`. `report_period_days`
is optional — it defaults from `cadence` if omitted. `config.json` is gitignored.

### 4. Authorize your Gmail connector

The email step sends via your own Claude Code Gmail connector, not a shared account —
authorize it yourself in your claude.ai connector settings before trying to send a
report email. This session (or any session) cannot complete this OAuth step for you.

### 5. Install Python dependencies

```bash
pip install openpyxl pytest
```

(`urllib`, used for all Graph API calls, is part of the Python standard library — no
extra HTTP client dependency.)

### 6. Verify everything works

```bash
python3 -m pytest -v
```

All tests should pass without any real Meta credentials (they're fully mocked). Then
run a real report:

```bash
python3 scripts/run_report.py --period-end $(date +%Y-%m-%d)
```

Check `references/metric-definitions.md`'s "First-live-run checklist" — some metrics
(Hook Rate, Hold Rate, Average Watch Time, Loyalty/Retention Rate) are implemented
against best-known Graph API field names that were not confirmed against a live account
when this was built; that checklist tells you how to confirm/fix them with your own
real data.

## Running it

See `SKILL.md` for the full report flow (it's a two-pass process — the second pass
needs your fact-check/time-sensitivity judgments for the Content Quality Score).

## Scheduling

To run this automatically on a cadence, set up a scheduled Claude Code agent (via the
`/schedule` skill or `CronCreate`) that invokes `/social-performance report` on your
chosen cadence. The scheduled run will generate the report and notify you — it will
not email anyone without your explicit approval in that notification's follow-up, by
design (see SKILL.md's "Sending the email" section).
```

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "docs: add self-sufficient setup README for installer handoff"
```

---

### Task 15: Push to GitHub (requires explicit confirmation before running)

**This task is a visible, hard-to-reverse action** (creates a new public/private GitHub
repo and pushes code) — confirm with Aakash which visibility (private strongly
recommended, since `.env`/`config.json` patterns and real account IDs will eventually
live alongside this code on the recipient's machine) and the exact repo name before
running anything below. Do not run these commands unattended.

**Files:** none (git/GitHub operations only)

- [ ] **Step 1: Confirm with Aakash**

Ask: repo name (suggest `social-performance`), visibility (private recommended), and
which GitHub account/org to create it under (per this workspace's memory, `gh` CLI is
already authenticated as Aakash's account).

- [ ] **Step 2: Create the GitHub repo and push**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/skills/social-performance"
gh repo create social-performance --private --source=. --remote=origin
git push -u origin main
```

- [ ] **Step 3: Verify**

```bash
gh repo view social-performance --web
```

Confirm the pushed repo does **not** contain `.env`, `config.json`, or anything under
`data/` (all gitignored) — run `git log --all --full-history -- .env config.json` in
the repo and confirm it returns nothing.

- [ ] **Step 4: Hand off**

Share the repo URL/access with the team member per Aakash's usual process (this step is
outside Claude Code's scope — invitation/access management on GitHub is a manual step
for Aakash to complete).
