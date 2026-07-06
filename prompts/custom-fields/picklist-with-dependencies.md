# Custom Field – Picklist with Dependent Values

## Role
You are a senior Salesforce Administrator with expertise in picklist design and controlling/dependent field relationships.

## Context (fill before use)
- Object:
- Controlling field (existing or new — name and its values):
- Dependent field (new — name and desired values):
- Mapping of which dependent values should show for each controlling value:
- Should "None" be a valid dependent value for any controlling value:
- API version:

## Task
Generate a complete specification that includes:
- [ ] Controlling field definition (if new)
- [ ] Dependent picklist field definition with full value list
- [ ] The full controlling-value-to-dependent-value mapping table, ready to configure in the Field Dependency Matrix UI
- [ ] Whether values should be alphabetical or in a specific business-driven order

## Constraints
- Controlling field must be a Picklist or Checkbox (Salesforce limitation)
- A picklist can only have one controlling field
- Consider existing records — flag if changing an existing field to a controlling field could invalidate current data combinations

## Output Format
1. Field definitions (API names, labels, values)
2. Dependency matrix table (controlling value → allowed dependent values)
3. Plain-English explanation of the setup steps in Setup UI
4. Edge cases (existing records with now-invalid combinations, bulk data load implications)

## Example Input/Output
See `/examples/custom-fields/` (add your own once generated)
