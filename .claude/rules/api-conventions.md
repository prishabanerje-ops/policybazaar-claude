# API Conventions

- REST routes are plural nouns: `/policies/:id/quotes`, never `/getQuote`.
- All responses use the envelope: `{ "data": ..., "error": null }` or `{ "data": null, "error": { "code", "message" } }`.
- Error codes are SCREAMING_SNAKE strings (`POLICY_NOT_FOUND`), not just HTTP status.
- Validate every request body with zod at the route layer; services receive typed, validated input only.
- Breaking changes require a new version prefix (`/v2/...`) — never change an existing response shape.
- All timestamps are ISO-8601 UTC strings in responses; store as `timestamptz` in Postgres.
