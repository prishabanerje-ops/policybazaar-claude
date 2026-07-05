# Testing

- Every bug fix ships with a regression test that fails without the fix.
- Test files live next to the code: `quote-service.ts` → `quote-service.test.ts`.
- Test names describe behavior, not implementation:
  ✅ `returns 404 when the policy does not exist`
  ❌ `test getPolicy error case`
- Mock at the boundary (HTTP, DB), never mock internal services.
- No snapshot tests for logic — assert on specific values.
- Run the single affected test file while iterating; run the full suite before declaring done.
