export const meta = {
  name: 'health-audit-batch',
  description: 'Fan out one content-audit agent per health-insurance URL in the batch',
  phases: [{ title: 'Audit' }],
}
// args: { batch: [{url, slug, page_type, tier}], promptTemplate: string, auditDate: string }
// Some invocation paths deliver args as a JSON-encoded string — normalize before use.
const input = typeof args === 'string' ? JSON.parse(args) : args
const RESULT_SCHEMA = {
  type: 'object',
  properties: {
    url: { type: 'string' },
    status: { enum: ['done', 'failed'] },
    overall: { type: 'number' },
    md_file: { type: 'string' },
    json_file: { type: 'string' },
    failure_reason: { type: 'string' },
  },
  required: ['url', 'status'],
}
phase('Audit')
const results = await parallel(input.batch.map(item => () => {
  const prompt = input.promptTemplate
    .replaceAll('{URL}', item.url)
    .replaceAll('{SLUG}', item.slug)
    .replaceAll('{PAGE_TYPE}', item.page_type)
    .replaceAll('{TIER}', item.tier)
    .replaceAll('{AUDIT_DATE}', input.auditDate)
  return agent(prompt, { label: `audit:${item.slug}`, schema: RESULT_SCHEMA })
}))
log(`batch done: ${results.filter(Boolean).length}/${input.batch.length} agents returned`)
return results.filter(Boolean)
