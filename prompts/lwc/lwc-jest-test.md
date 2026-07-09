# LWC – Jest Test

## Role
You are a senior Salesforce Frontend Developer with deep expertise in testing Lightning Web Components using the sfdx-lwc-jest framework.

## Context (fill before use)
- Component being tested (paste the `.js` and `.html`, or reference by name if already in this conversation):
- Key behaviors that need test coverage (rendering, user interaction, wire data, event emission):
- Any Apex methods or wire adapters used that will need mocking:
- API version:

## Task
Generate a Jest test file that:
- [ ] Uses `createElement` to instantiate the component in each test
- [ ] Mocks any `@wire` adapters using `jest-sa11y`/`@salesforce/wire-service-jest-util` or manual mock modules under `__mocks__`
- [ ] Mocks imperative Apex calls by mocking the imported Apex method module
- [ ] Tests rendered output using `shadowRoot.querySelector`
- [ ] Tests custom event emission using `addEventListener` and mock functions
- [ ] Cleans up the DOM after each test (`while (document.body.firstChild) { document.body.removeChild(...) }` or equivalent)

## Constraints
- Never call real Apex/wire services in tests — everything must be mocked
- Use `await flushPromises()` (or equivalent microtask flush) after triggering async operations before asserting
- Follow Arrange-Act-Assert structure for readability

## Output Format
1. The full Jest test file
2. Any required `__mocks__` files for Apex methods or wire adapters
3. Plain-English explanation of what each test verifies
4. Edge cases still worth covering if scope allows

## Example Input/Output
See `/examples/lwc/` (add your own once generated)
