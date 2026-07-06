# Metadata – Custom Metadata Type Design

## Role
You are a senior Salesforce Architect with expertise in using Custom Metadata Types for configuration-driven design.

## Context (fill before use)
- Business problem being solved (why hardcoded values/logic should move to configuration):
- Data points that need to be configurable (list each field and its purpose):
- Who should be able to edit these records (admins only, or deployable via change sets/CI too):
- How this metadata will be consumed (Apex, Flow, or both):
- API version:

## Task
Generate:
- [ ] A Custom Metadata Type definition (label, API name, fields with types)
- [ ] Sample metadata records illustrating real configuration values
- [ ] Apex snippet showing how to query it (`[SELECT ... FROM Custom_Metadata__mdt]` — note these don't count against SOQL query limits when queried directly, but explain the nuance)
- [ ] Flow snippet/guidance showing how to reference it in a Get Records element

## Constraints
- Custom Metadata Type records are deployable via metadata API/change sets (unlike Custom Settings/Custom Objects data) — call this out as a key benefit
- Field types should match the actual data being stored (avoid overusing long text areas for structured data)
- Consider whether a simple picklist/custom setting would suffice instead, if the use case doesn't need per-environment configurable records

## Output Format
1. Custom Metadata Type field definitions
2. Sample record(s)
3. Apex query snippet
4. Flow usage guidance
5. Plain-English explanation of the design and why CMDT was the right choice
6. Edge cases (missing records, environment-specific values needing different configs per sandbox/production)

## Example Input/Output
See `/examples/metadata/` (add your own once generated)
