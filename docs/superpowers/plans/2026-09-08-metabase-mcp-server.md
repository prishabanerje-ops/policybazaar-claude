# Metabase MCP Server (from scratch) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an original Python MCP server, in Aakash's own name, that gives Claude read-only search/browse/query access to `https://metabase.policybazaar.ae/`.

**Architecture:** Two files carry all logic — `metabase_client.py` (all Metabase REST calls, auth, and the read-only SQL guard, fully unit-testable with mocked HTTP) and `server.py` (thin `FastMCP` tool wrappers with zero Metabase-specific logic of its own). Own git repo at `.claude/mcp/metabase-mcp/`, independent of the main PolicyBazaar Claude repo's git history — same placement pattern as the existing `GoogleTrendsMCP`.

**Tech Stack:** Python 3.10+, official `mcp` SDK (`mcp.server.fastmcp.FastMCP`, stdio transport), `requests`, `python-dotenv`, `pytest` + `unittest.mock`.

**Spec:** `docs/superpowers/specs/2026-09-08-metabase-mcp-server-design.md`

## Global Constraints

- Own git repo at `.claude/mcp/metabase-mcp/` — not part of the main PolicyBazaar Claude repo's git history.
- Python 3.10+, `mcp` SDK's `FastMCP`, stdio transport (verified pattern — see `.claude/mcp/GoogleTrendsMCP/server.py`).
- `run_sql`'s read-only enforcement is hardcoded in `metabase_client.py` — no environment variable can disable it.
- Every raised `MetabaseError` states what was attempted and with what input (endpoint/method, or the rejected SQL) — never a bare exception.
- Automated tests mock the HTTP boundary only (`unittest.mock` on `requests.request`/`requests.post`) — no real network calls in the test suite.
- MIT License, copyright holder "Aakash Srivastava".
- No code, file structure, or prose copied from `@jerichosequitin/metabase-mcp` — this is an original implementation against the public Metabase REST API.

All project paths below are relative to:
`/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp/`

---

### Task 1: Project scaffolding + auth config resolution

**Files:**
- Create: `.gitignore`
- Create: `requirements.txt`
- Create: `.env.example`
- Create: `LICENSE`
- Create: `conftest.py`
- Create: `metabase_client.py` (this task: `MetabaseError`, `MetabaseConfig` only)
- Test: `tests/test_metabase_client.py` (this task: `MetabaseConfig` tests only)

**Interfaces:**
- Produces: `MetabaseError(Exception)`; `MetabaseConfig` with attributes `.url: str`, `.api_key: str | None`, `.email: str | None`, `.password: str | None`, and property `.uses_api_key: bool`. Later tasks construct `MetabaseClient(config: MetabaseConfig)`.

- [ ] **Step 1: Create the project folder, its own git repo, and a virtualenv**

```bash
mkdir -p "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp/tests"
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
git init
python3 -m venv venv
source venv/bin/activate
```

- [ ] **Step 2: Create `.gitignore`**

```
venv/
__pycache__/
*.pyc
*.pyo
*.egg-info/
dist/
build/
.env
.vscode/
*.log
.pytest_cache/
```

- [ ] **Step 3: Create `requirements.txt`**

```
mcp>=1.0.0
requests>=2.31.0
python-dotenv>=1.0.0
pytest>=8.0.0
```

- [ ] **Step 4: Install dependencies**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
source venv/bin/activate
pip install -r requirements.txt
```

Expected: all four packages install with no errors.

- [ ] **Step 5: Create `.env.example`**

```
# Metabase Server Connection Settings
METABASE_URL=https://metabase.policybazaar.ae

# Auth Option 1: API key (preferred if you have one)
METABASE_API_KEY=

# Auth Option 2: LDAP email + password (used only if METABASE_API_KEY is not set)
METABASE_EMAIL=
METABASE_PASSWORD=
```

- [ ] **Step 6: Create `LICENSE`**

```
MIT License

Copyright (c) 2026 Aakash Srivastava

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

- [ ] **Step 7: Create `conftest.py`**

```python
# Empty on purpose: its mere presence in the project root makes pytest add
# this directory to sys.path, so `import metabase_client` resolves from
# tests/ without needing a package layout or sys.path hacks.
```

- [ ] **Step 8: Write the failing tests for `MetabaseConfig`**

```python
# tests/test_metabase_client.py
import pytest

from metabase_client import MetabaseConfig, MetabaseError


def test_config_requires_metabase_url(monkeypatch):
    monkeypatch.delenv("METABASE_URL", raising=False)
    with pytest.raises(MetabaseError, match="METABASE_URL"):
        MetabaseConfig()


def test_config_requires_some_auth_method(monkeypatch):
    monkeypatch.setenv("METABASE_URL", "https://metabase.example.com")
    monkeypatch.delenv("METABASE_API_KEY", raising=False)
    monkeypatch.delenv("METABASE_EMAIL", raising=False)
    monkeypatch.delenv("METABASE_PASSWORD", raising=False)
    with pytest.raises(MetabaseError, match="auth"):
        MetabaseConfig()


def test_config_resolves_api_key_mode(monkeypatch):
    monkeypatch.setenv("METABASE_URL", "https://metabase.example.com")
    monkeypatch.setenv("METABASE_API_KEY", "test-key")
    monkeypatch.delenv("METABASE_EMAIL", raising=False)
    monkeypatch.delenv("METABASE_PASSWORD", raising=False)

    config = MetabaseConfig()

    assert config.uses_api_key is True
    assert config.url == "https://metabase.example.com"


def test_config_resolves_session_mode_and_strips_trailing_slash(monkeypatch):
    monkeypatch.setenv("METABASE_URL", "https://metabase.example.com/")
    monkeypatch.delenv("METABASE_API_KEY", raising=False)
    monkeypatch.setenv("METABASE_EMAIL", "a@b.com")
    monkeypatch.setenv("METABASE_PASSWORD", "secret")

    config = MetabaseConfig()

    assert config.uses_api_key is False
    assert config.url == "https://metabase.example.com"
```

- [ ] **Step 9: Run tests to verify they fail**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
source venv/bin/activate
pytest tests/test_metabase_client.py -v
```

Expected: FAIL with `ModuleNotFoundError: No module named 'metabase_client'` (the file doesn't exist yet).

- [ ] **Step 10: Write the minimal implementation**

```python
# metabase_client.py
"""Metabase REST API client with read-only SQL enforcement."""

import os

from dotenv import load_dotenv

load_dotenv()


class MetabaseError(Exception):
    """Raised when a Metabase API call fails or a query is rejected."""


class MetabaseConfig:
    def __init__(self) -> None:
        url = os.environ.get("METABASE_URL")
        if not url:
            raise MetabaseError(
                "METABASE_URL is not set. Set it in your environment or .env file."
            )
        self.url = url.rstrip("/")

        self.api_key = os.environ.get("METABASE_API_KEY")
        self.email = os.environ.get("METABASE_EMAIL")
        self.password = os.environ.get("METABASE_PASSWORD")

        if not self.api_key and not (self.email and self.password):
            raise MetabaseError(
                "No Metabase auth configured. Set METABASE_API_KEY, or both "
                "METABASE_EMAIL and METABASE_PASSWORD."
            )

    @property
    def uses_api_key(self) -> bool:
        return bool(self.api_key)
```

- [ ] **Step 11: Run tests to verify they pass**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
source venv/bin/activate
pytest tests/test_metabase_client.py -v
```

Expected: all 4 tests PASS.

- [ ] **Step 12: Commit**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
git add .gitignore requirements.txt .env.example LICENSE conftest.py metabase_client.py tests/test_metabase_client.py
git commit -m "feat: scaffold project and add Metabase auth config resolution"
```

---

### Task 2: HTTP request layer — auth headers + one-shot 401 retry

**Files:**
- Modify: `metabase_client.py` (add `MetabaseClient.__init__`, `_authenticate`, `_headers`, `_request`)
- Test: `tests/test_metabase_client.py` (append)

**Interfaces:**
- Consumes: `MetabaseConfig`, `MetabaseError` (Task 1).
- Produces: `MetabaseClient(config: MetabaseConfig | None = None)` with method `_request(method: str, path: str, *, json: dict | None = None, params: dict | None = None) -> Any` — every later Metabase-calling method (Tasks 4–5) calls this.

- [ ] **Step 1: Write the failing tests**

Add to the top of `tests/test_metabase_client.py`, alongside the existing `import pytest`:

```python
from unittest.mock import MagicMock, patch

from metabase_client import MetabaseClient
```

Append these helpers and tests to the end of the file:

```python
def make_config(monkeypatch, *, api_key=None, email=None, password=None):
    monkeypatch.setenv("METABASE_URL", "https://metabase.example.com")
    if api_key:
        monkeypatch.setenv("METABASE_API_KEY", api_key)
    else:
        monkeypatch.delenv("METABASE_API_KEY", raising=False)
    if email:
        monkeypatch.setenv("METABASE_EMAIL", email)
    else:
        monkeypatch.delenv("METABASE_EMAIL", raising=False)
    if password:
        monkeypatch.setenv("METABASE_PASSWORD", password)
    else:
        monkeypatch.delenv("METABASE_PASSWORD", raising=False)
    return MetabaseConfig()


def make_response(status_code, json_body=None, text=""):
    response = MagicMock()
    response.status_code = status_code
    response.json.return_value = json_body if json_body is not None else {}
    response.text = text
    return response


@patch("metabase_client.requests.request")
def test_api_key_mode_never_calls_session_endpoint(mock_request, monkeypatch):
    config = make_config(monkeypatch, api_key="test-key")
    client = MetabaseClient(config)
    mock_request.return_value = make_response(200, {"ok": True})

    with patch("metabase_client.requests.post") as mock_post:
        result = client._request("GET", "/api/database")

    mock_post.assert_not_called()
    assert result == {"ok": True}
    assert mock_request.call_args.kwargs["headers"] == {"x-api-key": "test-key"}


@patch("metabase_client.requests.post")
@patch("metabase_client.requests.request")
def test_session_mode_authenticates_lazily_then_reuses_token(mock_request, mock_post, monkeypatch):
    config = make_config(monkeypatch, email="a@b.com", password="secret")
    client = MetabaseClient(config)
    mock_post.return_value = make_response(200, {"id": "session-token-1"})
    mock_request.return_value = make_response(200, {"ok": True})

    client._request("GET", "/api/database")
    client._request("GET", "/api/collection")

    assert mock_post.call_count == 1
    for call in mock_request.call_args_list:
        assert call.kwargs["headers"] == {"X-Metabase-Session": "session-token-1"}


@patch("metabase_client.requests.post")
@patch("metabase_client.requests.request")
def test_401_triggers_one_reauth_and_retry(mock_request, mock_post, monkeypatch):
    config = make_config(monkeypatch, email="a@b.com", password="secret")
    client = MetabaseClient(config)
    mock_post.side_effect = [make_response(200, {"id": "token-1"}), make_response(200, {"id": "token-2"})]
    mock_request.side_effect = [make_response(401, text="expired"), make_response(200, {"ok": True})]

    result = client._request("GET", "/api/database")

    assert result == {"ok": True}
    assert mock_post.call_count == 2
    assert mock_request.call_count == 2


@patch("metabase_client.requests.post")
@patch("metabase_client.requests.request")
def test_second_401_after_retry_raises(mock_request, mock_post, monkeypatch):
    config = make_config(monkeypatch, email="a@b.com", password="secret")
    client = MetabaseClient(config)
    mock_post.side_effect = [make_response(200, {"id": "token-1"}), make_response(200, {"id": "token-2"})]
    mock_request.side_effect = [make_response(401, text="expired"), make_response(401, text="still expired")]

    with pytest.raises(MetabaseError, match="401"):
        client._request("GET", "/api/database")


@patch("metabase_client.requests.request")
def test_error_response_raises_with_context(mock_request, monkeypatch):
    config = make_config(monkeypatch, api_key="test-key")
    client = MetabaseClient(config)
    mock_request.return_value = make_response(500, text="internal error")

    with pytest.raises(MetabaseError, match=r"GET /api/database"):
        client._request("GET", "/api/database")
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
source venv/bin/activate
pytest tests/test_metabase_client.py -v
```

Expected: the 5 new tests FAIL with `ImportError` / `AttributeError` (`MetabaseClient` doesn't exist yet).

- [ ] **Step 3: Write the minimal implementation**

Append to `metabase_client.py` (add `import requests` and `from typing import Any` to the top of the file, alongside the existing `import os`):

```python
from typing import Any

import requests
```

Then append the class:

```python
class MetabaseClient:
    def __init__(self, config: MetabaseConfig | None = None) -> None:
        self.config = config or MetabaseConfig()
        self._session_token: str | None = None

    def _authenticate(self) -> str:
        response = requests.post(
            f"{self.config.url}/api/session",
            json={"username": self.config.email, "password": self.config.password},
            timeout=30,
        )
        if response.status_code != 200:
            raise MetabaseError(
                f"Failed to authenticate to Metabase as {self.config.email}: "
                f"{response.status_code} {response.text}"
            )
        token = response.json().get("id")
        if not token:
            raise MetabaseError(
                f"Metabase login for {self.config.email} succeeded but returned no session id."
            )
        self._session_token = token
        return token

    def _headers(self) -> dict[str, str]:
        if self.config.uses_api_key:
            return {"x-api-key": self.config.api_key}
        token = self._session_token or self._authenticate()
        return {"X-Metabase-Session": token}

    def _request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
    ) -> Any:
        url = f"{self.config.url}{path}"
        response = requests.request(method, url, headers=self._headers(), json=json, params=params, timeout=60)

        if response.status_code == 401 and not self.config.uses_api_key:
            self._session_token = None
            response = requests.request(method, url, headers=self._headers(), json=json, params=params, timeout=60)

        if response.status_code >= 400:
            raise MetabaseError(
                f"Metabase request failed: {method} {path} -> {response.status_code} {response.text}"
            )

        return response.json()
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
source venv/bin/activate
pytest tests/test_metabase_client.py -v
```

Expected: all 9 tests PASS.

- [ ] **Step 5: Commit**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
git add metabase_client.py tests/test_metabase_client.py
git commit -m "feat: add Metabase HTTP client with auth and one-shot 401 retry"
```

---

### Task 3: Read-only SQL guard

**Files:**
- Modify: `metabase_client.py` (add `validate_readonly_sql`)
- Test: `tests/test_metabase_client.py` (append)

**Interfaces:**
- Produces: `validate_readonly_sql(sql: str) -> None`, raises `MetabaseError` if `sql` is not a single read-only statement. Consumed by `MetabaseClient.run_sql` in Task 5.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_metabase_client.py`:

```python
from metabase_client import validate_readonly_sql


def test_validate_accepts_select():
    validate_readonly_sql("SELECT * FROM policies LIMIT 10")  # must not raise


def test_validate_accepts_cte_with_select():
    validate_readonly_sql("WITH recent AS (SELECT * FROM policies) SELECT * FROM recent")  # must not raise


def test_validate_rejects_empty_sql():
    with pytest.raises(MetabaseError, match="empty"):
        validate_readonly_sql("   ")


def test_validate_rejects_delete():
    with pytest.raises(MetabaseError, match="DELETE"):
        validate_readonly_sql("DELETE FROM policies")


def test_validate_rejects_stacked_statements():
    with pytest.raises(MetabaseError, match="stacked"):
        validate_readonly_sql("SELECT 1; DROP TABLE policies")


def test_validate_rejects_write_keyword_inside_cte():
    with pytest.raises(MetabaseError, match="GRANT"):
        validate_readonly_sql("WITH x AS (SELECT 1) SELECT * FROM x WHERE 1=1 GRANT ALL")
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
source venv/bin/activate
pytest tests/test_metabase_client.py -v
```

Expected: the 6 new tests FAIL with `ImportError` (`validate_readonly_sql` doesn't exist yet).

- [ ] **Step 3: Write the minimal implementation**

Add `import re` to the top of `metabase_client.py`, then append:

```python
WRITE_KEYWORDS = (
    "INSERT", "UPDATE", "DELETE", "DROP", "ALTER",
    "CREATE", "TRUNCATE", "GRANT", "REVOKE",
)


def validate_readonly_sql(sql: str) -> None:
    """
    Raise MetabaseError unless sql is a single read-only SELECT/CTE statement.

    This is a heuristic, not a full SQL parser: it can be fooled by a write
    keyword appearing inside a quoted string literal. It is a defense-in-depth
    layer on top of the Metabase account's own DB permissions, not a
    substitute for least-privilege access.
    """
    stripped = sql.strip()
    if not stripped:
        raise MetabaseError("Cannot run an empty SQL query.")

    first_word_match = re.match(r"[A-Za-z]+", stripped)
    first_word = first_word_match.group(0).upper() if first_word_match else ""

    if first_word not in ("SELECT", "WITH"):
        raise MetabaseError(
            f"Refusing to run non-SELECT statement (starts with '{first_word}'). "
            f"Only SELECT and WITH...SELECT statements are allowed. SQL was: {sql!r}"
        )

    body = stripped.rstrip(";").strip()
    if ";" in body:
        raise MetabaseError(
            f"Refusing to run stacked SQL statements (multiple statements "
            f"separated by ';'). SQL was: {sql!r}"
        )

    upper_body = body.upper()
    for keyword in WRITE_KEYWORDS:
        if re.search(rf"\b{keyword}\b", upper_body):
            raise MetabaseError(
                f"Refusing to run SQL containing write keyword '{keyword}'. "
                f"SQL was: {sql!r}"
            )
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
source venv/bin/activate
pytest tests/test_metabase_client.py -v
```

Expected: all 15 tests PASS.

- [ ] **Step 5: Commit**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
git add metabase_client.py tests/test_metabase_client.py
git commit -m "feat: add read-only SQL guard for native queries"
```

---

### Task 4: Browse methods (search, list, get)

**Files:**
- Modify: `metabase_client.py` (add `search`, `list_databases`, `list_tables`, `list_collections`, `get_dashboard`, `get_card` to `MetabaseClient`)
- Test: `tests/test_metabase_client.py` (append)

**Interfaces:**
- Consumes: `MetabaseClient._request` (Task 2).
- Produces: `MetabaseClient.search(query, models=None)`, `.list_databases()`, `.list_tables(database_id)`, `.list_collections()`, `.get_dashboard(dashboard_id)`, `.get_card(card_id)` — all consumed by `server.py` in Task 6.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_metabase_client.py`:

```python
@patch.object(MetabaseClient, "_request")
def test_search_sends_query_param(mock_request, monkeypatch):
    client = MetabaseClient(make_config(monkeypatch, api_key="test-key"))
    mock_request.return_value = {"data": []}

    result = client.search("premium")

    mock_request.assert_called_once_with("GET", "/api/search", params={"q": "premium"})
    assert result == {"data": []}


@patch.object(MetabaseClient, "_request")
def test_search_with_models_filter(mock_request, monkeypatch):
    client = MetabaseClient(make_config(monkeypatch, api_key="test-key"))
    mock_request.return_value = {"data": []}

    client.search("premium", models=["dashboard", "card"])

    mock_request.assert_called_once_with(
        "GET", "/api/search", params={"q": "premium", "models": ["dashboard", "card"]}
    )


@patch.object(MetabaseClient, "_request")
def test_list_databases(mock_request, monkeypatch):
    client = MetabaseClient(make_config(monkeypatch, api_key="test-key"))
    mock_request.return_value = {"data": [{"id": 1}]}

    result = client.list_databases()

    mock_request.assert_called_once_with("GET", "/api/database")
    assert result == {"data": [{"id": 1}]}


@patch.object(MetabaseClient, "_request")
def test_list_tables(mock_request, monkeypatch):
    client = MetabaseClient(make_config(monkeypatch, api_key="test-key"))
    mock_request.return_value = {"tables": []}

    client.list_tables(7)

    mock_request.assert_called_once_with("GET", "/api/database/7/metadata")


@patch.object(MetabaseClient, "_request")
def test_list_collections(mock_request, monkeypatch):
    client = MetabaseClient(make_config(monkeypatch, api_key="test-key"))
    mock_request.return_value = []

    client.list_collections()

    mock_request.assert_called_once_with("GET", "/api/collection")


@patch.object(MetabaseClient, "_request")
def test_get_dashboard(mock_request, monkeypatch):
    client = MetabaseClient(make_config(monkeypatch, api_key="test-key"))
    mock_request.return_value = {"id": 3}

    client.get_dashboard(3)

    mock_request.assert_called_once_with("GET", "/api/dashboard/3")


@patch.object(MetabaseClient, "_request")
def test_get_card(mock_request, monkeypatch):
    client = MetabaseClient(make_config(monkeypatch, api_key="test-key"))
    mock_request.return_value = {"id": 9}

    client.get_card(9)

    mock_request.assert_called_once_with("GET", "/api/card/9")
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
source venv/bin/activate
pytest tests/test_metabase_client.py -v
```

Expected: the 7 new tests FAIL with `AttributeError` (methods don't exist yet).

- [ ] **Step 3: Write the minimal implementation**

Append these methods inside the `MetabaseClient` class in `metabase_client.py`:

```python
    def search(self, query: str, models: list[str] | None = None) -> Any:
        params: dict[str, Any] = {"q": query}
        if models:
            params["models"] = models
        return self._request("GET", "/api/search", params=params)

    def list_databases(self) -> Any:
        return self._request("GET", "/api/database")

    def list_tables(self, database_id: int) -> Any:
        return self._request("GET", f"/api/database/{database_id}/metadata")

    def list_collections(self) -> Any:
        return self._request("GET", "/api/collection")

    def get_dashboard(self, dashboard_id: int) -> Any:
        return self._request("GET", f"/api/dashboard/{dashboard_id}")

    def get_card(self, card_id: int) -> Any:
        return self._request("GET", f"/api/card/{card_id}")
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
source venv/bin/activate
pytest tests/test_metabase_client.py -v
```

Expected: all 22 tests PASS.

- [ ] **Step 5: Commit**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
git add metabase_client.py tests/test_metabase_client.py
git commit -m "feat: add Metabase browse methods (search, list, get)"
```

---

### Task 5: Query execution methods (run_card, run_sql)

**Files:**
- Modify: `metabase_client.py` (add `run_card`, `run_sql` to `MetabaseClient`)
- Test: `tests/test_metabase_client.py` (append)

**Interfaces:**
- Consumes: `MetabaseClient._request` (Task 2), `validate_readonly_sql` (Task 3).
- Produces: `MetabaseClient.run_card(card_id, parameters=None)`, `.run_sql(database_id, sql)` — consumed by `server.py` in Task 6.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_metabase_client.py`:

```python
@patch.object(MetabaseClient, "_request")
def test_run_card_posts_query_with_parameters(mock_request, monkeypatch):
    client = MetabaseClient(make_config(monkeypatch, api_key="test-key"))
    mock_request.return_value = {"data": {"rows": []}}

    client.run_card(12, parameters=[{"id": "p1", "value": "x"}])

    mock_request.assert_called_once_with(
        "POST", "/api/card/12/query", json={"parameters": [{"id": "p1", "value": "x"}]}
    )


@patch.object(MetabaseClient, "_request")
def test_run_card_defaults_to_empty_parameters(mock_request, monkeypatch):
    client = MetabaseClient(make_config(monkeypatch, api_key="test-key"))
    mock_request.return_value = {"data": {"rows": []}}

    client.run_card(12)

    mock_request.assert_called_once_with("POST", "/api/card/12/query", json={"parameters": []})


@patch.object(MetabaseClient, "_request")
def test_run_sql_sends_native_query(mock_request, monkeypatch):
    client = MetabaseClient(make_config(monkeypatch, api_key="test-key"))
    mock_request.return_value = {"data": {"rows": []}}

    client.run_sql(5, "SELECT * FROM policies LIMIT 10")

    mock_request.assert_called_once_with(
        "POST",
        "/api/dataset",
        json={"type": "native", "native": {"query": "SELECT * FROM policies LIMIT 10"}, "database": 5},
    )


@patch.object(MetabaseClient, "_request")
def test_run_sql_rejects_delete_without_http_call(mock_request, monkeypatch):
    client = MetabaseClient(make_config(monkeypatch, api_key="test-key"))

    with pytest.raises(MetabaseError, match="DELETE"):
        client.run_sql(5, "DELETE FROM policies")

    mock_request.assert_not_called()


@patch.object(MetabaseClient, "_request")
def test_run_sql_rejects_stacked_statements(mock_request, monkeypatch):
    client = MetabaseClient(make_config(monkeypatch, api_key="test-key"))

    with pytest.raises(MetabaseError, match="stacked"):
        client.run_sql(5, "SELECT 1; DROP TABLE policies")

    mock_request.assert_not_called()


@patch.object(MetabaseClient, "_request")
def test_run_sql_accepts_cte(mock_request, monkeypatch):
    client = MetabaseClient(make_config(monkeypatch, api_key="test-key"))
    mock_request.return_value = {"data": {"rows": []}}

    client.run_sql(5, "WITH recent AS (SELECT * FROM policies) SELECT * FROM recent")

    mock_request.assert_called_once()
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
source venv/bin/activate
pytest tests/test_metabase_client.py -v
```

Expected: the 6 new tests FAIL with `AttributeError` (`run_card`/`run_sql` don't exist yet).

- [ ] **Step 3: Write the minimal implementation**

Append these methods inside the `MetabaseClient` class in `metabase_client.py`:

```python
    def run_card(self, card_id: int, parameters: list[dict[str, Any]] | None = None) -> Any:
        body = {"parameters": parameters or []}
        return self._request("POST", f"/api/card/{card_id}/query", json=body)

    def run_sql(self, database_id: int, sql: str) -> Any:
        validate_readonly_sql(sql)
        body = {
            "type": "native",
            "native": {"query": sql},
            "database": database_id,
        }
        return self._request("POST", "/api/dataset", json=body)
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
source venv/bin/activate
pytest tests/test_metabase_client.py -v
```

Expected: all 28 tests PASS.

- [ ] **Step 5: Commit**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
git add metabase_client.py tests/test_metabase_client.py
git commit -m "feat: add run_card and read-only run_sql query methods"
```

---

### Task 6: MCP server layer (server.py)

**Files:**
- Create: `server.py`
- Test: Create `tests/test_server.py`

**Interfaces:**
- Consumes: `MetabaseClient` (Tasks 2, 4, 5).
- Produces: module-level `mcp` (a `FastMCP` instance) with 8 registered tools: `search`, `list_databases`, `list_tables`, `list_collections`, `get_dashboard`, `get_card`, `run_card`, `run_sql`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_server.py
"""Smoke test that server.py registers the expected MCP tools."""

import asyncio

import server


def test_all_expected_tools_are_registered():
    tools = asyncio.run(server.mcp.list_tools())
    tool_names = {tool.name for tool in tools}

    assert tool_names == {
        "search",
        "list_databases",
        "list_tables",
        "list_collections",
        "get_dashboard",
        "get_card",
        "run_card",
        "run_sql",
    }
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
source venv/bin/activate
pytest tests/test_server.py -v
```

Expected: FAIL with `ModuleNotFoundError: No module named 'server'`.

- [ ] **Step 3: Write the minimal implementation**

```python
# server.py
"""MCP server exposing Metabase browse/query tools to Claude."""

from typing import Any

from mcp.server.fastmcp import FastMCP

from metabase_client import MetabaseClient

mcp = FastMCP("Metabase")

_client: MetabaseClient | None = None


def get_client() -> MetabaseClient:
    global _client
    if _client is None:
        _client = MetabaseClient()
    return _client


@mcp.tool()
def search(query: str, models: list[str] | None = None) -> Any:
    """
    Search across all Metabase items: dashboards, saved questions (cards),
    collections, databases, and tables.

    Args:
        query: Free-text search string.
        models: Optional filter, e.g. ["dashboard", "card"]. Omit to search everything.
    """
    return get_client().search(query, models)


@mcp.tool()
def list_databases() -> Any:
    """List all databases connected to this Metabase instance."""
    return get_client().list_databases()


@mcp.tool()
def list_tables(database_id: int) -> Any:
    """
    List all tables (with schema/field metadata) for a given database.

    Args:
        database_id: The Metabase database ID, from list_databases().
    """
    return get_client().list_tables(database_id)


@mcp.tool()
def list_collections() -> Any:
    """List all collections (folders of dashboards/cards) in this Metabase instance."""
    return get_client().list_collections()


@mcp.tool()
def get_dashboard(dashboard_id: int) -> Any:
    """
    Get the full definition of a dashboard, including its cards.

    Args:
        dashboard_id: The Metabase dashboard ID, from search() or list_collections().
    """
    return get_client().get_dashboard(dashboard_id)


@mcp.tool()
def get_card(card_id: int) -> Any:
    """
    Get the definition of a saved question (card) - its query, not its result data.

    Args:
        card_id: The Metabase card ID, from search().
    """
    return get_client().get_card(card_id)


@mcp.tool()
def run_card(card_id: int, parameters: list[dict[str, Any]] | None = None) -> Any:
    """
    Run an existing saved question (card) and return its result data.

    Args:
        card_id: The Metabase card ID to execute.
        parameters: Optional list of Metabase parameter objects to filter the card's query.
    """
    return get_client().run_card(card_id, parameters)


@mcp.tool()
def run_sql(database_id: int, sql: str) -> Any:
    """
    Run a read-only SQL query against a Metabase database. Only SELECT and
    WITH...SELECT statements are allowed - anything else is rejected before
    it reaches Metabase.

    Args:
        database_id: The Metabase database ID to query, from list_databases().
        sql: The SQL SELECT statement to run.
    """
    return get_client().run_sql(database_id, sql)


if __name__ == "__main__":
    mcp.run()
```

- [ ] **Step 4: Run test to verify it passes**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
source venv/bin/activate
pytest tests/test_server.py -v
```

Expected: PASS. (This works without any Metabase env vars set, because `get_client()` only constructs a `MetabaseClient` — which requires `METABASE_URL` — the first time a tool actually runs; merely importing `server` and listing its registered tools never calls `get_client()`.)

- [ ] **Step 5: Run the full test suite**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
source venv/bin/activate
pytest -v
```

Expected: all 29 tests PASS.

- [ ] **Step 6: Commit**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
git add server.py tests/test_server.py
git commit -m "feat: add FastMCP server wiring 8 Metabase tools"
```

---

### Task 7: README

**Files:**
- Create: `README.md`

**Interfaces:**
- None — documentation only.

- [ ] **Step 1: Write `README.md`**

```markdown
# Metabase MCP Server

An original [MCP (Model Context Protocol)](https://modelcontextprotocol.io) server
giving Claude read-only access to a Metabase instance: search dashboards/cards/
collections, browse databases and tables, run existing saved questions, and run
ad hoc read-only SQL.

## Tools

| Tool | Description |
|------|-------------|
| `search` | Search across dashboards, saved questions, collections, databases, tables |
| `list_databases` | List all databases connected to this Metabase instance |
| `list_tables` | List tables + field metadata for a database |
| `list_collections` | List all collections |
| `get_dashboard` | Get a dashboard's full definition |
| `get_card` | Get a saved question's definition (not its data) |
| `run_card` | Execute an existing saved question |
| `run_sql` | Run a read-only SQL query (SELECT / WITH...SELECT only — anything else is rejected before it reaches Metabase) |

## Setup

### Prerequisites

- Python 3.10+
- A Metabase account (API key, or LDAP email + password)

### Install

\`\`\`bash
cd .claude/mcp/metabase-mcp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then fill in your Metabase URL + credentials
\`\`\`

### Run the tests

\`\`\`bash
pytest
\`\`\`

### Register with Claude Code

\`\`\`bash
claude mcp add metabase-own --scope local \\
  -e METABASE_URL=https://metabase.policybazaar.ae/ \\
  -e METABASE_EMAIL='your.email@policybazaar.com' \\
  -e METABASE_PASSWORD='your-password' \\
  -- python3 "$(pwd)/server.py"
\`\`\`

Named `metabase-own` to avoid colliding with the `metabase` connector already
installed from the third-party `@jerichosequitin/metabase-mcp` package.

## Safety

`run_sql` only accepts SELECT / WITH...SELECT statements — INSERT, UPDATE,
DELETE, DROP, ALTER, CREATE, TRUNCATE, GRANT, REVOKE, and stacked statements
are all rejected in code before any request reaches Metabase. There is no
env flag to disable this.

## License

MIT — see [LICENSE](LICENSE)
```

- [ ] **Step 2: Commit**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
git add README.md
git commit -m "docs: add README"
```

---

### Task 8: Manual live verification (run by Aakash, not automated)

This task requires real credentials against production Metabase — it must be run by Aakash in his own terminal, not delegated to an autonomous agent, since it's the first point this code touches `metabase.policybazaar.ae` for real.

**Files:** none (verification only).

- [ ] **Step 1: Populate a real `.env`**

```bash
cd "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp"
cp .env.example .env
```

Edit `.env` and fill in the real `METABASE_URL` and either `METABASE_API_KEY` or `METABASE_EMAIL`/`METABASE_PASSWORD`. This file is gitignored — it will not be committed.

- [ ] **Step 2: Smoke-test each browse method against the real instance**

```bash
source venv/bin/activate
python3 -c "
from metabase_client import MetabaseClient
c = MetabaseClient()
print(c.list_databases())
print(c.list_collections())
print(c.search('policy'))
"
```

Expected: real JSON data printed for each call, no `MetabaseError` raised. If this fails, the endpoint response shapes may differ from what this plan assumed (flagged as an open risk in the design doc) — capture the actual error and adjust `metabase_client.py` accordingly before proceeding.

- [ ] **Step 3: Smoke-test a real read-only query**

Pick a real `database_id` from Step 2's `list_databases()` output, then:

```bash
python3 -c "
from metabase_client import MetabaseClient
c = MetabaseClient()
print(c.run_sql(<real_database_id>, 'SELECT 1'))
"
```

Expected: a real result row returned, no error.

- [ ] **Step 4: Register with Claude Code and test end-to-end**

```bash
claude mcp add metabase-own --scope local \
  -e METABASE_URL=https://metabase.policybazaar.ae/ \
  -e METABASE_EMAIL='<your real email>' \
  -e METABASE_PASSWORD='<your real password>' \
  -- python3 "/Users/aakashsrivastava/Documents/PolicyBazaar Claude/.claude/mcp/metabase-mcp/server.py"

claude mcp list
```

Then, in a Claude Code session, ask "list my Metabase databases using metabase-own" and confirm it returns real data.

- [ ] **Step 5: Report back**

Confirm to Claude which steps passed and paste any error output from a step that didn't — the plan's remaining tasks (if any adjustments are needed to endpoint paths or response parsing) will be scoped from there.
