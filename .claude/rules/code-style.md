# Code Style

- TypeScript strict mode; no `any` — use `unknown` and narrow it.
- Prefer named exports; default exports only for page/route components.
- Functions over classes unless state genuinely needs encapsulating.
- Early returns over nested if/else.
- No commented-out code — delete it, git remembers.
- Error messages must include context: what was attempted and with what input.

## Naming

- Files: `kebab-case.ts`; React components: `PascalCase.tsx`
- Booleans read as questions: `isActive`, `hasQuote`, `canRenew`
- Async functions that fetch are `fetchX` / `loadX`, never `getX`
