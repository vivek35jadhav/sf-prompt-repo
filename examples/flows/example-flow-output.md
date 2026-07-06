# Example Output – Record-Triggered Flow (Case)

This is a sample output generated from `/prompts/flows/record-triggered-flow.md`, using this filled-in context:

- Object: Case
- Trigger: before save, on create and update
- Entry condition: Priority = "High" AND Status = "New"
- Logic: Set `SLA_Due_Date__c` to `NOW() + 4 hours`

## Flow design summary

**Trigger type:** Before-Save (Record-Triggered Flow) — chosen because this only updates a field on the same record, so no separate DML/after-save step is needed.

**Entry Conditions:**
```
Priority EQUALS "High"
AND Status EQUALS "New"
```

**Elements:**
1. **Trigger** — Case, before save, create and update
2. **Decision: "Is SLA Already Set?"** — checks `{!$Record.SLA_Due_Date__c} IS NULL` to avoid overwriting on every subsequent edit
3. **Assignment: "Set SLA Due Date"** — `{!$Record.SLA_Due_Date__c}` = `ADDHOURS({!$Flow.CurrentDateTime}, 4)`

**Fault handling:** Not required for before-save field assignments (no DML performed by the flow itself; the triggering save operation handles fault reporting).

This is a trimmed illustrative example. Use it as a reference for the expected shape and level of detail in real output.
