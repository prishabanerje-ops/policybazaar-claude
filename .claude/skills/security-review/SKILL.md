---
name: security-review
description: Security review of code changes. Use when the user asks for a security review, mentions auth/secrets/injection concerns, or before merging changes that touch authentication, payment, or user-data handling.
---

# Security Review

Review the target code (the current diff by default, or the files the user names) for security issues.

## Checklist

1. **Injection** — SQL built by string concatenation, unescaped HTML, shell commands with user input.
2. **Auth** — endpoints missing auth middleware; authorization checks that trust client-supplied IDs (IDOR).
3. **Secrets** — hardcoded keys/tokens/passwords; secrets logged or returned in responses.
4. **Input validation** — request bodies used without schema validation; file uploads without type/size limits.
5. **Sensitive data** — PII in logs; missing masking of PAN/Aadhaar/card numbers; caching of personal data.
6. **Dependencies** — newly added packages: check they're well-known and pinned.

## Output format

For each finding report: severity (critical/high/medium/low), file:line, the vulnerable pattern, and a concrete fix. Verify each finding by reading the surrounding code — do not report from the diff alone. If nothing is found, state what was checked so the "all clear" is meaningful.
