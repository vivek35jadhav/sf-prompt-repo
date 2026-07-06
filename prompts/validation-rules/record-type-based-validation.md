# Validation Rule – Record-Type-Based Validation

## Role
You are a senior Salesforce Administrator/Developer with expertise in record type strategy and page layout-driven validation.

## Context (fill before use)
- Object(s):
- Record Type(s) this rule should apply to:
- Field(s) involved:
- Business requirement (e.g. "Field X is required only on the 'Enterprise' record type"):
- Existing validation rules on this object:
- API version:

## Task
Generate a validation rule that:
- [ ] Correctly references `RecordType.DeveloperName` (not the Label, which can change/be translated)
- [ ] Applies only to the specified record type(s)
- [ ] Does not affect other record types on the same object

## Constraints
- Must not conflict with existing validation rules
- Flag if this logic would be better handled via page layout field-level requiredness instead of a validation rule (e.g. if it's purely a UI concern, not a data integrity concern)
- Consider API-created records that may bypass page layout enforcement — explain why the validation rule is still the safer choice for true data integrity

## Output Format
1. The full validation rule formula
2. Suggested rule name and error message text
3. Plain-English explanation of the logic
4. Edge cases (e.g. record type changes after creation, API inserts, data migration tools)

## Example Input/Output
See `/examples/validation-rules/` (add your own once generated)
