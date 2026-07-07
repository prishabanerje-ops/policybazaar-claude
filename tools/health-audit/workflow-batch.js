export const meta = {
  name: 'health-audit-batch',
  description: 'Fan out one content-audit agent per health-insurance URL in the batch',
  phases: [{ title: 'Audit' }],
}
// args: { batch: [{url, slug, page_type, tier}], promptTemplate: string, auditDate: string }
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
const results = await parallel(args.batch.map(item => () => {
  const prompt = args.promptTemplate
    .replaceAll('{URL}', item.url)
    .replaceAll('{SLUG}', item.slug)
    .replaceAll('{PAGE_TYPE}', item.page_type)
    .replaceAll('{TIER}', item.tier)
    .replaceAll('{AUDIT_DATE}', args.auditDate)
  return agent(prompt, { label: `audit:${item.slug}`, schema: RESULT_SCHEMA })
}))
log(`batch done: ${results.filter(Boolean).length}/${args.batch.length} agents returned`)
return results.filter(Boolean)
