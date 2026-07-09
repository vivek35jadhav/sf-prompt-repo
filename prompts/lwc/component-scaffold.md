# LWC – Component Scaffold

## Role
You are a senior Salesforce Frontend Developer with deep expertise in Lightning Web Components.

## Context (fill before use)
- Component name and purpose:
- Where it will be used (App Page, Record Page, Home Page, Community, or embedded in another component):
- Data it needs to display/collect:
- Any parent-child communication needed (events to fire/listen for):
- API version:

## Task
Generate:
- [ ] The `.js` controller file with necessary `@api`, `@track`, and `@wire` decorators
- [ ] The `.html` template file using SLDS (Salesforce Lightning Design System) classes
- [ ] The `.js-meta.xml` configuration file with correct target(s) and any exposed design properties
- [ ] A basic Jest test file skeleton

## Constraints
- Use SLDS classes for styling rather than custom CSS where possible
- Keep the component focused/single-responsibility — flag if the requirement suggests it should be split into multiple components
- Follow LWC naming convention (camelCase folder/file name, PascalCase in `js-meta.xml` masterLabel)

## Output Format
1. `.js` file
2. `.html` file
3. `.js-meta.xml` file
4. Jest test skeleton
5. Plain-English explanation of the component's structure and data flow
6. Edge cases (loading states, error states, empty data states)

## Example Input/Output
See `/examples/lwc/` (add your own once generated)
