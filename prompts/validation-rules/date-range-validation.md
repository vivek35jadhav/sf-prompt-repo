# Validation Rule – Date Range Validation

## Role
You are a senior Salesforce Administrator/Developer with deep expertise in declarative validation logic.

## Context (fill before use)
- Object(s):
- Date field(s) involved (e.g. Start Date, End Date):
- Business requirement (e.g. "End Date cannot be before Start Date", "Start Date cannot be in the past"):
- Should this apply on create only, edit only, or both:
- Existing validation rules on this object:
- API version:

## Task
Generate a validation rule that:
- [ ] Enforces the date logic described above
- [ ] Handles blank date fields gracefully (don't fire on incomplete records unless required elsewhere)
- [ ] Uses `ISNEW()` / `ISCHANGED()` if the rule should only apply in specific save contexts
- [ ] Follows Salesforce best practices for readable, maintainable formulas

## Constraints
- Must not conflict with existing validation rules
- Consider time zone implications if using DATETIME fields vs DATE fields
- Consider whether the rule should be bypassed for specific profiles/integration users

## Output Format
1. The full validation rule formula
2. Suggested rule name and error message text
3. Recommended error location
4. Plain-English explanation of the logic
5. Edge cases (e.g. null dates, bulk data loads, timezone differences)

## Example Input/Output
See `/examples/validation-rules/` (add your own once generated)
