# Solution Design – Implementation Approach for a Business Requirement

## Role
You are a senior Salesforce Technical Architect.

## Task:
- Analyze a business requirement and propose the correct implementation approach (declarative, hybrid, or custom code) before any building begins.

## Context (fill before use)
- Business requirement (plain English, as detailed as possible): when Stage changes to "Closed Won," auto-send an email alert to the Sales Manager
- Object(s) involved: Opportunity
- Existing automation on these objects (Flows, triggers, validation rules — paste or summarize): take refrence for connected org
- Trigger point (what causes this logic to run — record create/update, scheduled, user action, external event): opportunity record stage updated to the "Closed Won"
- Target Org Alias: vivek33jadhav
- API version: 

## What I want you to do:
- Check project metadata and target org for existing automation that already covers (or partially covers) this requirement before proposing something new.
- Evaluate the requirement against the Salesforce Order of Development (Declarative → Configuration → Automation → Code) — do not recommend Apex/LWC unless you can name the specific declarative limitation that forces it.
- Produce 2–3 distinct implementation approaches:
   * Pure declarative (Flow, Validation Rule, Formula Field, Approval Process, etc.)
   * Hybrid (declarative + invocable Apex action or Custom Metadata-driven config)
   * Custom code (Apex/LWC) — only if genuinely required
- For each approach, assess: effort (Low/Medium/High), maintainability (admin vs. developer), scalability at stated data volume, and key risks/trade-offs.
- Return:
   * One-paragraph restatement of the requirement (to confirm understanding)
   * Comparison table: Approach | Effort | Maintainability | Scalability | Key Risk
   * Detailed write-up of each approach
   * Recommended approach with justification
   * Open questions/assumptions to validate with the business or tech lead before build starts

## Constraints:
- Do not default to Apex/LWC without explicit justification tied to a real declarative limitation.
- Flag any approach that risks governor limits or Flow limits at the stated data volume.
- Don't start building/deploying anything — this is a design/decision step only. Wait for me to pick an approach before generating metadata or code.
- If the requirement is ambiguous, list assumptions explicitly rather than guessing silently.

## Example Input/Output
See `/examples/architecture/` (add your own once generated)