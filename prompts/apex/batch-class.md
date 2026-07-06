# Apex – Batch Class

## Role
You are a senior Salesforce Developer with deep expertise in Batch Apex for large-volume data processing.

## Context (fill before use)
- Object(s) being processed:
- Selection criteria (the query/scope of records to process):
- Business logic to apply per record/batch:
- Expected record volume:
- Batch size constraints (default 200, or specify a reason for a different size):
- Should this be scheduled to run automatically, and if so how often:
- API version:

## Task
Generate:
- [ ] A Batchable Apex class implementing `Database.Batchable<sObject>` (and `Database.Stateful` if state needs to persist across batches)
- [ ] `start()` method with an efficient, selective query
- [ ] `execute()` method with bulkified logic (no SOQL/DML in loops)
- [ ] `finish()` method handling completion logic (e.g. summary email, chaining another batch)
- [ ] A corresponding Schedulable class if scheduling was requested
- [ ] A test class using `Test.startTest()`/`Test.stopTest()` to execute the batch synchronously, with realistic bulk test data (200+ records)

## Constraints
- Query in `start()` must be selective to avoid timeout on large data volumes
- Must handle governor limits per batch execute (fresh limits per batch, but be mindful of callouts if `Database.AllowsCallouts` is needed)
- Handle partial failures gracefully (consider `Database.executeBatch` with `allOrNone=false` where appropriate)

## Output Format
1. Batch class code
2. Schedulable class code (if applicable)
3. Test class code
4. Plain-English explanation of the batch lifecycle and logic
5. Edge cases (batch failures, retry strategy, chaining considerations, large data volume timeouts)

## Example Input/Output
See `/examples/apex/` (add your own once generated)
