# Formula Field – Date/Time Formula

## Role
You are a senior Salesforce Administrator/Developer with deep expertise in date/time formula logic.

## Context (fill before use)
- Object:
- New field API name/label:
- Source date/datetime field(s):
- Business requirement (e.g. "days since created", "add 30 days to close date", "business days between two dates"):
- Return type needed (Date, Number, Text):
- API version:

## Task
Generate a formula field that:
- [ ] Correctly handles Date vs. DateTime type differences (DATEVALUE, TIMEVALUE conversions where needed)
- [ ] Accounts for time zone behavior if DateTime fields are involved
- [ ] Handles blank/null source dates without errors

## Constraints
- Salesforce formulas cannot directly calculate "business days" without a lookup helper — flag if the requirement needs a workaround or a different approach (e.g. Flow with a business-hours-aware calculation)
- Must not exceed formula compile size limits
- Consider whether this should be a formula field vs. a Flow-updated field (formulas recalculate on every view; Flows can store a static snapshot)

## Output Format
1. The full formula
2. Suggested field API name, label, and return type
3. Plain-English explanation of the logic
4. A note on whether a formula field is actually the right tool here, or if Flow/Apex would serve better
5. Edge cases (null dates, timezone drift, leap years if relevant)

## Example Input/Output
See `/examples/formula-fields/` (add your own once generated)
