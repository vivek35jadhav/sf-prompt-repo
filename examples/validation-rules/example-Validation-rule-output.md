---
description: Analyze then implement a Jira user story linked to Salesforce work
alwaysApply: false
---

Trigger: the user gives a Jira issue key (e.g. "PROJ-1234" or
"implement PROJ-1234").

## Stage 1 — Analysis (always runs first)

1. Call the Jira MCP tool to fetch the issue: summary, description,
   acceptance criteria, issue type, linked epic, comments, and any
   Salesforce component/object references mentioned.
2. Call the Salesforce MCP tool to inspect the org/project metadata
   relevant to the story:
   - describe objects/fields referenced or implied by the requirement
   - search for existing Apex classes, triggers, flows, validation
     rules, LWC/Aura components, permission sets, and page layouts
     that touch those objects/fields
   - check for related automation (flows/triggers) that could be
     affected by the change
3. Produce an **Impact Analysis** with:
   - Summary of the requirement in plain language
   - Objects/fields impacted (existing vs new)
   - Components involved (Apex classes, triggers, flows, LWC, page
     layouts, permission sets, etc.) — mark each as "modify",
     "new", or "review only"
   - Downstream dependencies/risks (e.g. other flows/triggers on the
     same object, sharing rules, integrations)
   - Open questions or ambiguities in the story, if any
4. Stop here. Do NOT propose an implementation approach yet.
5. Ask exactly: "Do you want me to give implementation approach
   options for this?"

## Stage 2 — Approach options (only after explicit "yes")

6. Once the user confirms, propose **2–3 distinct implementation
   approach options** (e.g. Flow vs Apex trigger vs LWC-based
   solution, or declarative vs programmatic), each with:
   - Brief description of how it works
   - Pros / cons
   - Components it would touch (tie back to Stage 1 impact list)
   - Relative effort/complexity
7. Ask the user to pick one option (by number/name). Do not proceed
   until they select.

## Stage 3 — Implementation (only after approach is selected)

8. Implement the selected approach incrementally, referencing the
   acceptance criteria as each part is completed.
9. Write/update test classes or test coverage as part of the same
   pass.
10. Summarize what was changed, file by file.

## Hard rule — deployment

- Never deploy, push, or activate any component to any Salesforce
  org unless the user explicitly says to deploy in that exact
  message. Creating/editing local files or metadata is fine;
  deploying is not, under any circumstance, without explicit
  instruction each time.
- Do not update Jira status or post comments unless explicitly asked.