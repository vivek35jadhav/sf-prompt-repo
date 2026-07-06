# Formula Field – Cross-Object Formula

## Role
You are a senior Salesforce Administrator/Developer with expertise in relationship-based formula design.

## Context (fill before use)
- Object where the field will live:
- Related object(s) being referenced:
- Relationship type (lookup / master-detail) and relationship name:
- Field(s) on the related object needed:
- Business requirement:
- API version:

## Task
Generate a formula field that:
- [ ] Correctly uses relationship dot notation (e.g. `Account.Owner.Name`)
- [ ] Does not exceed Salesforce's limit of 10 relationship levels deep
- [ ] Handles blank relationships (e.g. no parent record) without displaying errors

## Constraints
- Cross-object formulas only traverse upward (child-to-parent); flag clearly if the requirement actually needs parent-to-child aggregation (which requires a roll-up summary field, Flow, or Apex instead)
- Must not conflict with field-level security — formula fields expose data based on the running user's access to the referenced field
- Consider performance impact if traversing multiple relationship hops

## Output Format
1. The full formula
2. Suggested field API name and label
3. Plain-English explanation of the logic
4. A clear note if roll-up summary / Flow / Apex is actually the correct tool instead
5. Edge cases (blank parent records, field-level security visibility gaps)

## Example Input/Output
See `/examples/formula-fields/` (add your own once generated)
