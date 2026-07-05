---
name: deploy
description: Deploy this project safely. Use when the user asks to deploy, release, or ship to staging or production.
---

# Deploy

## Process

1. Confirm the target environment. If the user didn't specify, assume **staging** — never assume production.
2. Pre-flight: clean git tree, `npm run lint`, `npm test`, `npm run build` all green. Abort and report on the first failure.
3. Staging: `npm run deploy:staging`, then hit the health endpoint and confirm the new version is live.
4. Production: show the outgoing commit list and get explicit confirmation from the user before running `npm run deploy:production`.
5. After any deploy, watch the logs for 2 minutes of output for errors and report the result.

## Rollback

If the health check fails after deploy, run `npm run deploy:rollback -- <env>` immediately and tell the user what happened before doing anything else.
