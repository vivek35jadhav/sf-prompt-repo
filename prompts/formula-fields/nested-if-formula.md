# Formula Field – Nested IF / CASE Formula

## Role
You are a senior Salesforce Administrator/Developer with deep expertise in complex conditional formula logic.

## Context (fill before use)
- Object:
- New field API name/label:
- Source field(s) driving the conditions:
- Full list of conditions and their corresponding outputs (be exhaustive — list every branch):
- Default/fallback value if no condition matches:
- API version:

## Task
Generate a formula field that:
- [ ] Evaluates all conditions listed and returns the correct output for each
- [ ] Uses `CASE()` instead of nested `IF()` where possible for readability and performance, unless the logic requires compound conditions that `CASE()` can't express
- [ ] Includes a sensible default/fallback value
- [ ] Is formatted for readability (line breaks between conditions, consistent indentation)

## Constraints
- Must not exceed Salesforce's formula size/complexity limits — if the requirement has a large number of branches, flag this and suggest a helper (e.g. a custom metadata type lookup) as an alternative
- Must not conflict with existing formula fields
- Consider whether picklist values referenced might change over time (formula would need updates)

## Output Format
1. The full formula
2. Suggested field API name, label, and return type
3. Plain-English explanation mapping each condition to its output
4. A note if the branch count/complexity suggests a different design (e.g. custom metadata-driven approach)
5. Edge cases (unmatched values, blank source fields, future picklist value additions)

## Example Input/Output
See `/examples/formula-fields/` (add your own once generated)
