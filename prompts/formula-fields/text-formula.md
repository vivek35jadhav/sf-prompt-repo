# Formula Field – Text Formula

## Role
You are a senior Salesforce Administrator/Developer with deep expertise in formula field design.

## Context (fill before use)
- Object:
- New field API name/label:
- Source field(s) used in the formula:
- Business requirement (what should the field display/concatenate/derive):
- Should blank/null source fields be handled a specific way:
- API version:

## Task
Generate a Text-return-type formula field that:
- [ ] Produces the exact output described in the business requirement
- [ ] Uses `BLANKVALUE()` or `ISBLANK()` to gracefully handle null source fields
- [ ] Avoids unnecessary nested complexity — favor readability

## Constraints
- Field must be marked correctly (Text return type)
- Must not exceed Salesforce's formula compile size limits — flag if the requirement seems complex enough to risk this
- Consider field-level security/visibility implications since formula fields inherit visibility from referenced fields

## Output Format
1. The full formula
2. Suggested field API name and label
3. Return type and any formatting options (e.g. treat blank as blank vs zero — N/A for text but mention if relevant to referenced number fields)
4. Plain-English explanation of the logic
5. Edge cases (null fields, special characters, character limits)

## Example Input/Output
See `/examples/formula-fields/` (add your own once generated)
