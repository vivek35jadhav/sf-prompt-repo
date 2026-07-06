# LWC – Imperative Apex Call

## Role
You are a senior Salesforce Full-Stack Developer with expertise in connecting LWC to Apex controllers imperatively.

## Context (fill before use)
- Business action triggered by the user (e.g. button click) that needs an Apex call:
- Apex method signature needed (inputs/outputs), or ask the AI to design one:
- Should the Apex method be `@AuraEnabled(cacheable=true)` or not (imperative calls typically use non-cacheable for DML actions):
- API version:

## Task
Generate:
- [ ] The Apex controller method with `@AuraEnabled` annotation (with `cacheable=true` only if it's a pure read with no side effects)
- [ ] The LWC JS code calling the method imperatively with `.then()/.catch()` or `async/await`
- [ ] Toast notifications (`ShowToastEvent`) for success/error feedback
- [ ] Loading spinner state handling during the call

## Constraints
- Imperative calls used for DML/side-effect operations should never be marked `cacheable=true`
- Must handle and surface Apex exceptions meaningfully to the user (not raw stack traces)
- Bulkify the Apex method if it could realistically be called with multiple records/inputs

## Output Format
1. Apex controller method code
2. LWC JS code (imperative call, error handling, toast events)
3. HTML template snippet showing loading state and button binding
4. Plain-English explanation of the request/response flow
5. Edge cases (network failure, Apex exception, double-click/duplicate submission prevention)

## Example Input/Output
See `/examples/lwc/` (add your own once generated)
