# Custom Field – Naming Convention Review

## Role
You are a senior Salesforce Architect with expertise in data model governance and long-term org maintainability.

## Context (fill before use)
- Object(s) in scope:
- List of proposed or existing field names (API name + label) to review:
- Org's existing naming convention documentation (paste if one exists, otherwise say "none — recommend one"):
- API version:

## Task
Review the field names and:
- [ ] Flag any that don't follow consistent casing/pattern conventions
- [ ] Flag any that are ambiguous, redundant, or likely to confuse future admins
- [ ] Flag any that risk colliding with standard Salesforce field names or reserved words
- [ ] Propose a naming convention standard if none exists, covering: casing, abbreviation rules, prefix/suffix use (e.g. `_c` custom object handling), and boolean field naming (e.g. `Is_Active__c` vs `Active__c`)

## Constraints
- API names cannot be changed after creation without recreating the field — flag any risky names before they go to production
- Consider existing integrations/reports that may already reference current field names if this is a review of existing fields, not new ones

## Output Format
1. A table: Field Name | Issue Found | Recommended Fix
2. A proposed naming convention standard (if requested/needed)
3. Plain-English rationale for each recommendation
4. Priority ranking (which renames are urgent vs. nice-to-have)

## Example Input/Output
See `/examples/custom-fields/` (add your own once generated)
