# Custom Field – Creation Specification

## Role
You are a senior Salesforce Admin + Salesforce DX deploy assistant.

## Task:
- Create a new Salesforce field and deploy it to my target org.

## Context (fill before use)
- Object: Opportunity
- Field Name: Industry Type
- Business requirement (what data needs to be captured and why): Create field to captue Account Industry Type on accout for opportunity
- Field type expected (Text, Number, Picklist, Checkbox, Date, Lookup, etc. — or "recommend one" if unsure):formula (text)
- Who should see/edit this field (profiles/permission sets): 
- Is this field required: NA
- Target Org Alias: vivek35jadhav
- API version: NA

## What I want you to do:
- Validate if a similar field already exists in project metadata and in target org.
- Create/update metadata file at:
   force-app/main/default/objects/<Object API Name>/fields/<Field API Name>.field-meta.xml
- Use correct API version from sfdx-project.json.
- Deploy only this field with:
   sf project deploy start --source-dir <field file path> --target-org <Target Org Alias> --wait 10
- Verify deployment success and confirm field exists in org (Tooling query on FieldDefinition).
- Return:
   * Created file path
   * Exact deploy command used
   * Deployment result (success/failure)
   * Verification query output
   * Any follow-up actions (layout/FLS)

## Constraints :
- Minimal diff, no unrelated changes.
- Don’t commit or push unless I explicitly ask.
- If blocked, tell me exact error and the fix command.

## Example Input/Output
See `/examples/custom-fields/` (add your own once generated)
