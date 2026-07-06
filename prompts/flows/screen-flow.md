# Flow – Screen Flow

## Role
You are a senior Salesforce Automation Architect with expertise in Screen Flows and user-facing process design.

## Context (fill before use)
- Where this flow will be launched from (Lightning page, quick action, community/portal, etc.):
- Who is the end user (internal user, community user, specific profile):
- Business process to guide the user through (list the steps):
- Data to collect and/or display on each screen:
- Any records to create/update/query as part of the process:
- API version:

## Task
Generate a description of a Screen Flow that includes:
- [ ] Screen-by-screen breakdown (what's displayed, what's collected)
- [ ] Input validation on each screen (required fields, formula-based validation)
- [ ] Navigation logic (Next/Previous/Finish behavior, any conditional branching between screens)
- [ ] Record operations needed (Get/Create/Update Records elements) and where they occur in the flow
- [ ] Confirmation/success screen content

## Constraints
- Keep screens focused — avoid overloading a single screen with too many fields (mention if the design should be split into multiple screens)
- Use appropriate input components (Lightning-native components over plain text where relevant, e.g. picklists, lookups)
- Consider accessibility (clear labels, helpful error messages)
- Bulkify any backend record operations if the flow could process multiple records

## Output Format
1. Screen-by-screen breakdown
2. Element-by-element logic flow (decisions, record operations, assignments)
3. Plain-English explanation of the user experience
4. Fault handling / error message recommendations
5. Edge cases (user abandons mid-flow, validation failures, concurrent edits)

## Example Input/Output
See `/examples/flows/` (add your own once generated)
