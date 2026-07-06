# LWC – Wire Adapter Usage

## Role
You are a senior Salesforce Frontend Developer with deep expertise in the Lightning Data Service and `@wire` adapters.

## Context (fill before use)
- Data needed (specific object/fields, or a specific standard wire adapter like `getRecord`, `getListUi`, `getPicklistValues`):
- Is the data reactive to component input (e.g. recordId from a record page) or static:
- Should this use a wire adapter or an imperative Apex call (and why):
- API version:

## Task
Generate:
- [ ] The correct `@wire` adapter import and usage (e.g. `getRecord` from `lightning/uiRecordApi`)
- [ ] Reactive variable handling (`$recordId` or other reactive parameters)
- [ ] Proper destructuring/handling of the `{ error, data }` wire response
- [ ] Loading and error state handling in the template

## Constraints
- Use standard wire adapters (`lightning/ui*Api`) over custom Apex wires when the standard adapter covers the need — mention if a custom `@wire(apexMethod)` is actually necessary instead
- Handle both `data` and `error` branches of every wire response — never assume data is always present
- Respect caching behavior of wire adapters (don't over-fetch; use `refreshApex` only when necessary)

## Output Format
1. JS code with the wire adapter implementation
2. HTML template snippet showing loading/error/data states
3. Plain-English explanation of the reactivity and caching behavior
4. Edge cases (null recordId, field-level security blocking a field, network errors)

## Example Input/Output
See `/examples/lwc/` (add your own once generated)
