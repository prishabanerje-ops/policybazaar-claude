---
description: Run pre-deploy checks and deploy to the given environment
argument-hint: <staging|production>
allowed-tools: Bash(npm run build), Bash(npm test:*), Bash(npm run lint), Bash(git status), Bash(git log:*)
---

Deploy to the **$ARGUMENTS** environment.

## Pre-flight checks (all must pass before deploying)

1. Working tree must be clean: !`git status --short`
2. Run `npm run lint` and `npm test` — abort if either fails.
3. Run `npm run build` — abort on build errors.

## Deploy

- For **staging**: run `npm run deploy:staging`.
- For **production**: STOP and ask me to confirm first, showing the commits
  being deployed (`git log origin/production..HEAD --oneline`). Only after I
  confirm, run `npm run deploy:production`.

Afterwards, report what was deployed and paste any deploy output that looks like a warning or error.
