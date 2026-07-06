# Apex – Test Class

## Role
You are a senior Salesforce Developer with deep expertise in Apex unit testing and code coverage best practices.

## Context (fill before use)
- Class/Trigger being tested (paste the code, or its file name if already known to the AI in this conversation):
- Key methods/logic paths that need coverage:
- Any callouts, async processes (Batch/Queueable/Future), or DML-heavy logic involved:
- API version:

## Task
Generate a test class that:
- [ ] Uses `@isTest` annotation and a `TestSetup` method for shared test data where appropriate
- [ ] Creates test data using `Test.startTest()`/`Test.stopTest()` around any async logic
- [ ] Covers positive scenarios, negative/error scenarios, and bulk scenarios (200+ records)
- [ ] Includes `System.assert`/`Assert.areEqual` statements verifying actual outcomes, not just "no exception thrown"
- [ ] Mocks any callouts using `HttpCalloutMock` (never makes real callouts)
- [ ] Avoids `SeeAllData=true` — creates all necessary test data explicitly

## Constraints
- Target minimum 90%+ coverage of the class/trigger's logic branches (75% is Salesforce's deployment minimum, but aim higher for quality)
- Must not depend on any existing org data
- Must be bulk-safe and runnable independently of test execution order

## Output Format
1. The full test class code
2. A coverage summary explaining which methods/branches are tested by which test method
3. Plain-English explanation of the test data setup strategy
4. Edge cases still worth adding if scope allows (mention them even if not fully implemented)

## Example Input/Output
See `/examples/apex/` (add your own once generated)
