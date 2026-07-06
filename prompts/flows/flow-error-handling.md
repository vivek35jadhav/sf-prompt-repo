# Flow – Error Handling Design

## Role
You are a senior Salesforce Automation Architect with expertise in Flow fault paths and error monitoring.

## Context (fill before use)
- Flow being reviewed/designed (name and purpose):
- Elements in the flow that perform DML, callouts, or Get Records (list them):
- Who should be notified when a failure occurs (admin, record owner, a queue/email):
- Is there an existing error logging mechanism in the org (custom object, email alerts, third-party tool):
- API version:

## Task
Generate a fault-handling design that includes:
- [ ] A fault path attached to every DML/callout-capable element (never left unhandled)
- [ ] A reusable error-logging approach (e.g. a Create Records element writing to a custom "Flow Error Log" object, or a Send Email action)
- [ ] Clear, actionable fault messages (avoid generic "an error occurred")
- [ ] Recommendation on whether to use a subflow for centralized error logging across multiple flows

## Constraints
- Every element capable of failure (Create/Update/Delete Records, Action calls, HTTP callouts) must have a fault connector — no silent failures
- Error logs should capture: Flow name, element that failed, error message, record ID(s) involved, timestamp
- Consider governor limits when logging errors (don't create excessive log records in bulk failure scenarios)

## Output Format
1. Fault path design for each risky element
2. Error logging object/mechanism specification (fields needed if a custom object is proposed)
3. Notification logic (who gets notified, how)
4. Plain-English explanation
5. Edge cases (bulk failures creating log record volume issues, recursive error logging failures)

## Example Input/Output
See `/examples/flows/` (add your own once generated)
