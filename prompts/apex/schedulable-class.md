# Apex – Schedulable Class

## Role
You are a senior Salesforce Developer with expertise in scheduled Apex jobs.

## Context (fill before use)
- Business logic to run on schedule:
- Frequency required (daily, weekly, specific cron pattern):
- Does this call a Batch class, Queueable, or run logic directly:
- API version:

## Task
Generate:
- [ ] A class implementing `Schedulable`
- [ ] The `execute()` method calling the appropriate batch/queueable/logic
- [ ] The exact CRON expression needed for the requested frequency, with an explanation of each field
- [ ] Instructions (as comments or output text) for scheduling via `System.schedule()` in Anonymous Apex, or via Setup UI

## Constraints
- Consider org's existing scheduled jobs to avoid CPU/time overlap conflicts
- If chaining to a Batch class, ensure the batch's own constraints (selectivity, size) are respected
- Note the max of 100 scheduled Apex jobs per org

## Output Format
1. Schedulable class code
2. CRON expression with explanation
3. Scheduling instructions (Anonymous Apex snippet and/or Setup UI steps)
4. Plain-English explanation of the logic
5. Edge cases (daylight saving time shifts, job overlap, org job limits)

## Example Input/Output
See `/examples/apex/` (add your own once generated)
