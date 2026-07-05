---
description: Fetch a GitHub issue and implement a fix for it
argument-hint: <issue-number>
allowed-tools: Bash(gh issue view:*), Bash(git checkout:*), Bash(npm test:*), Read, Edit, Write, Grep, Glob
---

Fix GitHub issue #$ARGUMENTS.

## Steps

1. Run `gh issue view $ARGUMENTS` to read the issue description and comments.
2. Create a branch: `git checkout -b fix/issue-$ARGUMENTS`.
3. Locate the relevant code and understand the root cause before changing anything.
4. Implement the smallest fix that resolves the issue — follow `.claude/rules/code-style.md`.
5. Add or update a test that fails without the fix and passes with it (`.claude/rules/testing.md`).
6. Run `npm test` and `npm run lint` — both must pass.
7. Summarize the root cause and the fix. Do not commit unless I ask.
