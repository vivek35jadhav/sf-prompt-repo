# Integration – Outbound Callout Design (Trigger/Flow → External System)

## Role
You are a senior Salesforce Integration Architect with expertise in designing reliable outbound integrations from Salesforce automation to external systems.

## Context (fill before use)
- Triggering event in Salesforce (record created/updated on which object):
- External system being notified and what it needs to receive:
- Should this be real-time (synchronous-ish via async Apex) or is near-real-time acceptable (e.g. via scheduled batch):
- Retry/failure handling expectations (should failed callouts be retried, logged, alerted):
- API version:

## Task
Recommend and generate the appropriate design:
- [ ] Since triggers cannot make synchronous callouts, confirm the pattern: Trigger → Queueable (`Database.AllowsCallouts`) → external system
- [ ] Request/response wrapper classes
- [ ] Error handling and retry strategy (e.g. logging failures to a custom object for manual/automated retry)
- [ ] Test class with `HttpCalloutMock`

## Constraints
- Trigger context can never make direct synchronous callouts — must hand off to async Apex (Queueable/Future)
- Respect the 100-callout-per-transaction limit and external system rate limits
- Consider idempotency on the external system side (could the same record update trigger a duplicate callout, and does that matter)

## Output Format
1. Architecture summary (Trigger → Queueable → Callout flow diagram in text form)
2. Queueable class code with callout logic
3. Error logging/retry mechanism design
4. Test class with mock callout
5. Plain-English explanation
6. Edge cases (external system downtime, duplicate triggers from bulk updates, retry storms)

## Example Input/Output
See `/examples/integration/` (add your own once generated)
