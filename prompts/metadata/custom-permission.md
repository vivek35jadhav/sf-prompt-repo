# Metadata – Custom Permission Design

## Role
You are a senior Salesforce Architect with expertise in using Custom Permissions to control feature/automation access.

## Context (fill before use)
- Feature or automation behavior that needs to be conditionally enabled (e.g. "bypass validation rule for data migration users"):
- Who should have this permission (which roles/personas):
- Where this permission will be checked (validation rule, Flow, Apex, or a combination):
- API version:

## Task
Generate:
- [ ] A Custom Permission definition (label, API name, description)
- [ ] Guidance on which Permission Set(s) should include this custom permission
- [ ] The exact syntax to check this permission in:
  - A validation rule formula (`$Permission.Permission_API_Name__c`)
  - Apex (`FeatureManagement.checkPermission('Permission_API_Name')`)
  - Flow (a Decision element checking `{!$Permission.Permission_API_Name__c}`)

## Constraints
- Custom Permissions should be assigned via Permission Sets, not directly to profiles, for easier management
- Consider whether this should be a "bypass" pattern (default off, granted to specific automation/integration users) vs. an "enable" pattern (default off, granted to power users)

## Output Format
1. Custom Permission definition
2. Permission Set assignment guidance
3. Usage syntax for validation rule / Apex / Flow (whichever apply)
4. Plain-English explanation of the access model
5. Edge cases (users with multiple permission sets, permission not yet assigned at deploy time)

## Example Input/Output
See `/examples/metadata/` (add your own once generated)
