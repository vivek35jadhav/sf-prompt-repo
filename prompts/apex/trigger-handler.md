# Apex – Trigger Handler Pattern

## Role
You are a senior Salesforce Developer with deep expertise in Apex trigger design following the Trigger Handler framework pattern (one trigger per object, logic in handler classes).

## Context (fill before use)
- Object:
- Trigger events needed (before insert, after insert, before update, after update, before delete, after delete, after undelete):
- Business logic required per event:
- Existing triggers/handlers on this object (paste if any, to avoid duplicate trigger conflicts):
- API version:

## Task
Generate:
- [ ] A single trigger file (one trigger per object, delegating to a handler class)
- [ ] A handler class implementing the required logic, split by context (beforeInsert, afterUpdate, etc.)
- [ ] Bulkified logic — no SOQL or DML inside loops
- [ ] A recursion-prevention mechanism (static boolean flag or similar)
- [ ] A corresponding test class with at least 3 test methods covering positive, negative, and bulk (200 records) scenarios

## Constraints
- Must respect governor limits (SOQL: 100 queries/txn, DML: 150 statements/txn)
- Must not duplicate logic if a trigger/handler already exists — extend it instead
- Follow one-trigger-per-object best practice
- Include field-level security / CRUD checks if the trigger touches fields conditionally editable by profile

## Output Format
1. Trigger file (`ObjectNameTrigger.trigger`)
2. Handler class (`ObjectNameTriggerHandler.cls`)
3. Test class (`ObjectNameTriggerHandlerTest.cls`)
4. Plain-English explanation of the logic and execution order
5. Edge cases (recursive updates, bulk API inserts, order of execution with other automation like Flows)

## Example Input/Output
See `/examples/apex/example-trigger-output.md`
