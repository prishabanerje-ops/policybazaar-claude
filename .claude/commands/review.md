---
description: Review the current changes for bugs, style, and test coverage
allowed-tools: Bash(git diff:*), Bash(git status), Read, Grep, Glob
---

Review the current working-tree changes.

## Context

- Current status: !`git status --short`
- Current diff: !`git diff HEAD`

## Your task

1. Check the diff for correctness bugs (null handling, edge cases, off-by-one, race conditions).
2. Check it follows our conventions in `.claude/rules/code-style.md` and `.claude/rules/api-conventions.md`.
3. Flag any changed logic that has no corresponding test.
4. Report findings ordered by severity. If there are no findings, say so plainly.

Do NOT make any edits — this is a read-only review.
