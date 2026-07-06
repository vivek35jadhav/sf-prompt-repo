# Validation Rule – Conditionally Required Field

## Role
You are a senior Salesforce Administrator/Developer with deep expertise in declarative validation logic and data quality design.

## Context (fill before use)
- Object(s):
- Field(s) involved (the field being made conditionally required):
- Condition under which it becomes required (e.g. "when Status = Closed Won"):
- Business requirement:
- Existing validation rules on this object (paste them if any, to avoid conflicts):
- API version:

## Task
Generate a validation rule that:
- [ ] Makes the target field required only when the specified condition is true
- [ ] Does not block existing records that were saved before this rule was activated (unless explicitly required)
- [ ] Uses ISBLANK()/ISNULL() appropriately based on field type
- [ ] Follows Salesforce best practices (bulkification is N/A for validation rules, but keep formula performant and readable)

## Constraints
- Must not conflict with any existing validation rules on this object
- Must account for: record types, profiles, or automation (Flow/Apex) that might also set this field
- Should not fire during specific automated processes if applicable (e.g. via `$Profile.Name` or a bypass custom permission)

## Output Format
1. The full validation rule formula
2. Suggested rule name (following `Object_ConditionSummary` convention) and error message text
3. Recommended "Error Location" (top of page vs. specific field)
4. A plain-English explanation of the logic
5. Edge cases to double check (e.g. mass update tools, data loader, API-only integrations)

## Example Input/Output
See `/examples/validation-rules/example-conditional-required-output.md` (add your own once generated)
