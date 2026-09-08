# Metabase MCP Server (from scratch) — Design

**Date:** 2026-09-08
**Owner:** Aakash Srivastava
**Status:** Approved (brainstorming session 2026-09-08)

## Goal

Build an original, from-scratch MCP server that lets Claude query and browse
Aakash's own Metabase instance (`https://metabase.policybazaar.ae/`), so Claude
Code can be used to search dashboards/cards/collections and run read-only SQL
against Metabase databases directly from a session.

This is a deliberate rewrite, not a fork. A third-party server
(`@jerichosequitin/metabase-mcp`, audited earlier this session and found safe to
install) already does this and is installed locally as `metabase` via
`claude mcp add`. This project exists because Aakash wants a version that is
genuinely his own work, not a renamed copy — see the "not a replica" note under
Non-goals.

## Non-goals

- **Not a replica of `@jerichosequitin/metabase-mcp`.** No code, file
  structure, or prose is copied from that project. Only the *category* of
  functionality (a Metabase MCP server) and the Metabase REST API itself — a
  public, documented API anyone can build against — are shared.
- **Not a write-capable tool.** No INSERT/UPDATE/DELETE/DDL execution, no
  Metabase admin actions (creating/editing dashboards, cards, permissions,
  users). Read-only, enforced in code, no env flag to disable it.
- **Not an export/file-generation tool.** No CSV/XLSX file writing in v1 (per
  the "Query + browse" scope decision). Results are returned to Claude as
  structured data in the chat, not written to disk.
- **Not a replacement for the existing `metabase` connector** unless Aakash
  later chooses to swap them — both can coexist under different MCP server
  names in the interim.

## Architecture

Single Python project, own git repo, living at `.claude/mcp/metabase-mcp/`
(same placement pattern as the existing `GoogleTrendsMCP`). Uses the official
`mcp` Python SDK's `FastMCP` class over stdio transport — no HTTP server, no
Docker, no build step. Two files carry all the logic:

```
.claude/mcp/metabase-mcp/
├── server.py              # MCP tool definitions (thin wrappers)
├── metabase_client.py     # All Metabase REST calls + auth + read-only guard
├── requirements.txt       # mcp, requests, python-dotenv
├── .env.example
├── .gitignore
├── README.md
├── LICENSE                # MIT, Aakash Srivastava
└── tests/
    └── test_metabase_client.py
```

`server.py` never talks to Metabase directly — every tool function calls into
`metabase_client.py` and returns its result. This keeps the MCP protocol layer
(which can't be unit-tested without spinning up a client) separate from the
HTTP logic (which can be tested in full by mocking `requests`).

## Auth

Config is read from environment variables at startup via `python-dotenv`:

| Variable | Required? | Purpose |
|---|---|---|
| `METABASE_URL` | Yes | Base URL, e.g. `https://metabase.policybazaar.ae` |
| `METABASE_API_KEY` | One of these two auth methods | Sent as `x-api-key` header on every request |
| `METABASE_EMAIL` + `METABASE_PASSWORD` | required | Exchanged for a session token via `POST /api/session` |

Resolution order: if `METABASE_API_KEY` is set, use it exclusively (no
session call at all). Otherwise require both `METABASE_EMAIL` and
`METABASE_PASSWORD`, call `POST /api/session` once at startup, cache the
returned session `id`, and send it as the `X-Metabase-Session` header on
every subsequent call.

Session tokens expire; Metabase returns `401` when that happens mid-run.
`metabase_client.py` catches exactly one `401` per outer call, re-runs the
`POST /api/session` exchange, retries the original request once, and raises
if it still fails — no infinite retry loop.

## Tools exposed to Claude

All defined in `server.py` via `@mcp.tool()`, each a thin call into
`metabase_client.py`:

| Tool | Metabase endpoint | Notes |
|---|---|---|
| `search(query, models=None)` | `GET /api/search` | `models` optionally filters to `card`, `dashboard`, `collection`, `database`, `table` |
| `list_databases()` | `GET /api/database` | |
| `list_tables(database_id)` | `GET /api/database/{id}/metadata` | |
| `list_collections()` | `GET /api/collection` | |
| `get_dashboard(dashboard_id)` | `GET /api/dashboard/{id}` | |
| `get_card(card_id)` | `GET /api/card/{id}` | Returns the saved question's definition, not its data |
| `run_card(card_id, parameters=None)` | `POST /api/card/{id}/query` | Executes an existing saved question. No extra guardrail needed — the query itself was already defined and vetted in Metabase, this just runs it |
| `run_sql(database_id, sql)` | `POST /api/dataset` (native query) | See read-only guard below |

## Read-only guard (for `run_sql`)

Before `run_sql` sends anything to Metabase, `metabase_client.py` validates
the SQL client-side:

1. Strip leading whitespace/comments, uppercase the first keyword.
2. Accept only statements starting with `SELECT` or `WITH` (for CTEs that
   terminate in a `SELECT`).
3. Reject (raise, do not send to Metabase) anything starting with `INSERT`,
   `UPDATE`, `DELETE`, `DROP`, `ALTER`, `CREATE`, `TRUNCATE`, `GRANT`,
   `REVOKE`, or containing a stacked statement (a bare `;` followed by more
   non-whitespace content).

This is defense-in-depth on top of whatever permissions the Metabase account
already has — it does not rely on Metabase-side configuration, so it holds
even if the account's DB permissions are ever loosened.

## Error handling

Every raised exception states what was attempted and with what input, e.g.:

```python
raise MetabaseError(
    f"Failed to run SQL against database {database_id}: "
    f"{response.status_code} {response.text}"
)
```

No bare `except: pass` or silently-swallowed failures — a failed Metabase
call always surfaces to Claude as a clear error, never an empty/fabricated
result.

## Testing

`tests/test_metabase_client.py` uses `unittest.mock` to mock `requests` calls
— no real network access in the test suite. Per this workspace's testing
convention (mock at the boundary, assert on specific values, name tests by
behavior):

- `run_sql` rejects a `DELETE` statement without making any HTTP call.
- `run_sql` rejects a stacked statement (`SELECT 1; DROP TABLE x`).
- `run_sql` accepts a `WITH ... SELECT` CTE.
- A mocked `401` on any authenticated call triggers exactly one re-auth
  (`POST /api/session`) and one retry — a second `401` after retry raises.
- API-key auth mode never calls `POST /api/session`.
- Each tool method sends the request to the expected endpoint/method with
  the expected params, and returns the mocked response body unchanged.

## Open questions / risks

- **Metabase API version drift**: this design targets the REST endpoints as
  documented publicly for self-hosted Metabase; no live call against
  `metabase.policybazaar.ae` has been made yet to confirm exact response
  shapes. First implementation pass should verify each endpoint against the
  real instance (with a real, least-privilege LDAP account) before the tools
  are considered done.
- **Two Metabase MCP servers installed at once** (`metabase` = the audited
  third-party one, plus this new one under a different name) could confuse
  tool selection in a session. Recommend giving this one a distinct name at
  `claude mcp add` time (e.g. `metabase-own`) and deciding later whether to
  keep both or retire one.
