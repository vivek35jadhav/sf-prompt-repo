# Apex – Queueable Class

## Role
You are a senior Salesforce Developer with deep expertise in asynchronous Apex, specifically Queueable Apex.

## Context (fill before use)
- Trigger/entry point for this queueable job (e.g. called from a trigger, LWC, or scheduled job):
- Object(s)/data being processed:
- Business logic required:
- Does this need to make a callout (`Database.AllowsCallouts`):
- Does this need to chain into another queueable job:
- API version:

## Task
Generate:
- [ ] A class implementing `Queueable` (and `Database.AllowsCallouts` if needed)
- [ ] Bulkified logic handling a `List<sObject>` or `Set<Id>` passed via constructor
- [ ] Job chaining logic if required (with a safeguard against infinite chaining)
- [ ] A test class using `Test.startTest()`/`Test.stopTest()` to execute the queueable synchronously, including a mock callout class if callouts are involved

## Constraints
- Respect the limit of 50 queueable jobs chained per transaction (and be mindful this can be lower in some contexts)
- Must not be enqueued from inside a loop without safeguards (avoid hitting `System.LimitException: Too many queueable jobs added`)
- If called from a trigger, ensure it isn't enqueued multiple times unnecessarily for bulk operations (enqueue once with the full set of records)

## Output Format
1. Queueable class code
2. Mock HTTP callout class (if applicable)
3. Test class code
4. Plain-English explanation of when/why Queueable was chosen over Future methods or Batch Apex
5. Edge cases (chaining limits, callout timeouts, retry logic)

## Example Input/Output
See `/examples/apex/` (add your own once generated)
