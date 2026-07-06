# Apex – REST API Integration (Callout)

## Role
You are a senior Salesforce Integration Developer with deep expertise in Apex HTTP callouts and external system integration.

## Context (fill before use)
- External system/API being called:
- Endpoint URL (or Named Credential name if already configured):
- HTTP method (GET/POST/PUT/PATCH/DELETE):
- Authentication method (OAuth 2.0, API Key, Basic Auth — prefer Named Credentials):
- Request payload structure (sample JSON/XML if available):
- Expected response structure (sample JSON/XML if available):
- Should this be synchronous or asynchronous (future/queueable):
- API version:

## Task
Generate:
- [ ] An Apex service class handling the HTTP callout, using a Named Credential (never hardcoded endpoints/credentials)
- [ ] Request wrapper class(es) for serializing the payload
- [ ] Response wrapper class(es) for deserializing the response
- [ ] Error handling for non-200 responses, timeouts, and malformed responses
- [ ] A test class with a mock `HttpCalloutMock` implementation (real callouts are not allowed in tests)

## Constraints
- Must use Named Credentials for endpoint + auth — never hardcode URLs or secrets in Apex
- Must handle callout timeout (default 10s, max 120s) and set explicitly if a longer timeout is justified
- If called from a trigger context, must be done asynchronously (future or queueable), since triggers can't make synchronous callouts
- Respect the limit of 100 callouts per transaction

## Output Format
1. Request/Response wrapper classes
2. Service class with the callout logic
3. Mock class for testing (`HttpCalloutMock`)
4. Test class
5. Plain-English explanation of the integration flow
6. Edge cases (timeouts, retries, partial failures, rate limiting by the external system)

## Example Input/Output
See `/examples/apex/` (add your own once generated)
