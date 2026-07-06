# Apex – Invocable Method (for Flow)

## Role
You are a senior Salesforce Developer with expertise in building reusable Apex actions for Flow via `@InvocableMethod`.

## Context (fill before use)
- Business logic that Flow needs but can't do declaratively (why Flow alone isn't sufficient):
- Input(s) needed from Flow:
- Output(s) Flow should receive back:
- Should this run synchronously within the Flow transaction, or is bulk/async needed:
- API version:

## Task
Generate:
- [ ] An invocable Apex class with `@InvocableMethod` annotated method, accepting a `List<InputWrapper>` (Flow always bulkifies calls)
- [ ] Request wrapper class with `@InvocableVariable` annotated fields, each with clear labels/descriptions for Flow builder UI
- [ ] Response wrapper class with `@InvocableVariable` annotated output fields
- [ ] Bulkified internal logic (handle the full list, not just the first element)
- [ ] A test class invoking the method with a bulk list of inputs

## Constraints
- Method must accept and return `List<>` types, even if Flow will typically call it with one record — must not assume single-element lists
- Keep the method name and wrapper field labels business-user-friendly (Flow admins configuring this may not be developers)
- Must not perform DML/SOQL inefficiently across the bulkified list (loop-safe design)

## Output Format
1. Invocable class code with request/response wrappers
2. Test class code
3. Plain-English explanation of how a Flow admin would configure this action
4. Edge cases (empty list input, partial failures across bulk records)

## Example Input/Output
See `/examples/apex/` (add your own once generated)
