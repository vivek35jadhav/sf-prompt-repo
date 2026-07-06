# Integration – Platform Event Design

## Role
You are a senior Salesforce Integration Architect with expertise in event-driven architecture using Platform Events.

## Context (fill before use)
- Business event being modeled (e.g. "Order Shipped", "Inventory Updated"):
- Publisher (what triggers this event — Apex, Flow, or an external system via API):
- Subscriber(s) (what should react — Apex trigger on the event, Flow, external system via CometD/Pub-Sub API, or another Salesforce org):
- Data payload needed on the event:
- Publish behavior needed (Publish Immediately vs Publish After Commit):
- API version:

## Task
Generate:
- [ ] Platform Event object definition (label, API name, fields with types)
- [ ] Publishing code/logic (Apex `EventBus.publish()` snippet, or Flow "Create Records" guidance if publishing declaratively)
- [ ] Subscriber logic (Apex trigger on the event object, and/or Flow platform event-triggered flow)
- [ ] Guidance on Publish Behavior choice and its implications

## Constraints
- Platform Events are immutable once published — ensure the payload includes everything subscribers need (no follow-up queries back to the publisher context)
- Consider event replay/retention (24-hour retention window) if subscribers might be offline/delayed
- Bulkify publishing (batch multiple events in a single `EventBus.publish(List<SObject>)` call rather than one at a time)

## Output Format
1. Platform Event object field definitions
2. Publisher code/logic
3. Subscriber trigger/flow logic
4. Plain-English explanation of the event flow end-to-end
5. Edge cases (publish failures, subscriber processing failures, event replay for missed events)

## Example Input/Output
See `/examples/integration/` (add your own once generated)
