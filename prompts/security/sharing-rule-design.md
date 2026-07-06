# Security – Sharing Rule Design

## Role
You are a senior Salesforce Security Architect with expertise in record-level sharing model design.

## Context (fill before use)
- Object:
- Current Org-Wide Default (OWD) for this object (Private, Public Read Only, Public Read/Write):
- Who needs access beyond the OWD, and what level (Read Only or Read/Write):
- Basis for sharing (ownership-based, criteria-based, or based on a related object's sharing):
- API version:

## Task
Generate a sharing rule specification that includes:
- [ ] Recommended rule type (Owner-based vs. Criteria-based Sharing Rule)
- [ ] Rule criteria/logic
- [ ] Share-with target (specific role, role and subordinates, public group, territory)
- [ ] Access level to grant

## Constraints
- Sharing rules can only widen access beyond OWD, never restrict it further — if the requirement is to restrict access, explain that this needs OWD changes, restriction rules, or a different sharing model entirely
- Consider the performance impact of criteria-based sharing rules on very large data volumes (recalculation on every matching record change)
- Consider whether Apex Managed Sharing is more appropriate for complex, dynamic sharing logic that declarative rules can't express

## Output Format
1. Sharing rule specification (type, criteria, share-with, access level)
2. Plain-English explanation of who gains access and why
3. A note if OWD change, restriction rule, or Apex Managed Sharing would be more appropriate
4. Edge cases (role hierarchy changes, ownership transfer, users in multiple sharing groups)

## Example Input/Output
See `/examples/security/` (add your own once generated)
