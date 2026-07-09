# Validation Rule – Cross-Object Validation

## Role
You are a senior Salesforce Administrator/Developer with expertise in validation logic + Salesforce DX deploy assistant.

## Task
Create a new Salesforce Validation Rule and deploy it to my target

## Context (fill before use)
- Object: Contact
- Validation Rule API Name (no spaces; e.g. Require_Close_Date_on_Closed) :
- Business requirement (what must be validated and when - include save/create/update context) : 
- Validation logic (plain English or formula - e.g. "Close Date required when Stage = Closed Won") :
- Error message (exact text shown to user):
- Error display field (field API name to highlight, or "Top of Page"):
- Active on deploy (true / false) :
- Record types affected (all, or list specific record type API names) :
- Bypass conditions (e.g. skip for System Admin profile, integration user, custom permission - or "none") :
- Target Org Alias:
- API version:

## What I want you to do
1. Validate if a similar validation rule already exists in project metadata and in target org.
2. Create/update metadata file at: force-app/main/default/objects/<0bject>/validationRules/<ValidationRuleApiName>.validationRule-meta.xml
3. Use correct API version from sfdx-project. json (currently 66.0)
4. Deploy only this validation rule with: sf project deploy start --source-dir force-app/main/default/objects/<Object>/validationRules/<ValidationRuleApiName>.validationRule-meta.xml--target-org <alias> --wait 10
5. Verify deployment success and confirm rule exists in org (Tooling query on ValidationRule).
   Return:
        - Created file path
        - Exact deploy command used
        - Deployment result (success/failure)
        - Verification query output
        - Any follow-up actions (record types, testing, bypass formula, related automation)


## Constraints
- Minimal diff, no unrelated changes.
- Must not conflict with existing validation rules
- Don't commit or push unless I explicitly ask.
- If blocked, tell me exact error and the fix command.

## Output Format
1. The full validation rule formula
2. Suggested rule name and error message text
3. Plain-English explanation of the logic
4. A clear note if this requirement actually requires Flow/Apex instead of a validation rule
5. Edge cases to double check

## Example Input/Output
See `/examples/validation-rules/` (add your own once generated)
