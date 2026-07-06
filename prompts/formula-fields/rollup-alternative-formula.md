# Formula Field – Roll-Up Alternative (Lookup Relationships)

## Role
You are a senior Salesforce Architect with expertise in working around Salesforce's native limitation that roll-up summary fields only work on master-detail relationships.

## Context (fill before use)
- Parent object:
- Child object:
- Relationship type (must be lookup, since this prompt is for the workaround case):
- Aggregation needed (SUM, COUNT, MAX, MIN, AVG):
- Field on child object being aggregated:
- Any filter criteria on which child records to include:
- API version:

## Task
Since roll-up summary fields are not natively available on lookup relationships, recommend and generate the best-fit solution:
- [ ] Option A: Flow (record-triggered) that updates a stored field on the parent — provide the Flow logic description and the field it writes to
- [ ] Option B: Apex trigger/handler that performs the aggregation — provide the Apex code if this is the better fit for volume/complexity
- [ ] Option C: Declarative Lookup Rollup Summaries (DLRS) managed package — mention as a no-code option if appropriate
- [ ] Clearly state which option is recommended for the described scenario and why

## Constraints
- Consider data volume (Flow may hit limits on very high-volume objects; Apex is more scalable)
- Consider real-time vs. near-real-time requirements
- Must be bulk-safe if Apex is chosen (handle multiple parent records in a single transaction)

## Output Format
1. Recommended approach with justification
2. Full solution (Flow steps described, or Apex code, or DLRS configuration steps)
3. Plain-English explanation of the logic
4. Edge cases (child record deletion, re-parenting, bulk data loads)

## Example Input/Output
See `/examples/formula-fields/` (add your own once generated)
