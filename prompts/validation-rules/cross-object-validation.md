# Validation Rule – Cross-Object Validation

## Role
You are a senior Salesforce Administrator/Developer with expertise in relationship-based validation logic.

## Context (fill before use)
- Object where the rule will live:
- Related object(s) being referenced:
- Relationship type (lookup / master-detail):
- Field(s) on the related object being checked:
- Business requirement:
- Existing validation rules on this object:
- API version:

## Task
Generate a validation rule that:
- [ ] References the related object's field(s) correctly (dot notation, e.g. `Account.Industry`)
- [ ] Handles cases where the relationship field itself is blank (avoid null pointer-style formula errors)
- [ ] Follows Salesforce limitations (validation rules can only traverse relationships, not aggregate child records — flag if a Flow or Apex trigger is actually needed instead)

## Constraints
- Cross-object formulas only work through parent relationships (lookup/master-detail upward), not child relationships — call this out if the requirement actually needs child record data
- Must not conflict with existing validation rules
- Consider performance if the relationship chain is long (multiple lookups deep)

## Output Format
1. The full validation rule formula
2. Suggested rule name and error message text
3. Plain-English explanation of the logic
4. A clear note if this requirement actually requires Flow/Apex instead of a validation rule (e.g. child-to-parent aggregation)
5. Edge cases to double check

## Example Input/Output
See `/examples/validation-rules/` (add your own once generated)
