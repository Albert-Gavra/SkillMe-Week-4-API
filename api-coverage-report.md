
# API Test Coverage Report

## 1. Project Information

| Item | Details |
|---|---|
| Project Name | SkillMe Week 4 - API Testing |
| API Under Test | PokéAPI |
| Base URL | https://pokeapi.co/api/v2 |
| Testing Framework | Pytest |
| HTTP Client | Python Requests |
| Programming Language | Python |
| Total API Test Cases | 8 |

## 2. API Test Coverage Matrix

| Test ID | Endpoint | Test Scenario | Test Type | Expected Result | Status |
|---|---|---|---|---|---|
| API-001 | GET /pokemon/{name} | Retrieve Pokémon details using a valid name | Positive | HTTP 200 and correct Pokémon information | PASS |
| API-002 | GET /pokemon/{name} | Validate required fields in Pokémon response | Schema Validation | All required fields are present | PASS |
| API-003 | GET /pokemon/{name} | Verify API response time | Performance | Response time is below 2 seconds | PASS |
| API-004 | GET /pokemon/{name} | Request a nonexistent Pokémon | Negative | HTTP 404 Not Found | PASS |
| API-005 | GET /pokemon/{id} | Request Pokémon using an invalid ID | Negative | HTTP 404 Not Found | PASS |
| API-006 | GET /pokemon | Retrieve and validate the Pokémon list | Positive / Response Validation | HTTP 200 and valid list structure | PASS |
| API-007 | GET /type/{id} | Retrieve Pokémon type information | Positive / Response Validation | HTTP 200 and valid type information | PASS |
| API-008 | GET /ability/{id} | Retrieve Pokémon ability information | Positive / Response Validation | HTTP 200 and valid ability information | PASS |

## 3. Coverage Summary

| Metric | Result |
|---|---:|
| Total Test Cases | 8 |
| Passed Test Cases | 8 |
| Failed Test Cases | 0 |
| Pass Rate | 100% |

### Pass Rate Calculation

Pass Rate = (Passed Test Cases / Total Test Cases) × 100

Pass Rate = (8 / 8) × 100 = 100%

## 4. Testing Coverage

The API test suite covers the following areas:

- Successful GET requests using valid resource names and IDs.
- Negative testing using nonexistent Pokémon names and invalid IDs.
- Response schema validation.
- Response field and data type validation.
- API response time verification.
- Collection endpoint validation.
- Nested JSON response validation.

## 5. Limitations and Known Gaps

- Testing is limited to the GET endpoints provided by PokéAPI.
- POST, PUT, PATCH, and DELETE operations are not covered.
- Authentication and authorization testing are not applicable to the selected public API scenarios.
- Response time may vary depending on internet connectivity and server conditions.
- The response time test uses a threshold of less than 2 seconds.

## 6. Test Execution Result

All 8 API test cases passed during the latest successful test execution.

The HTML test report is available at:

`reports/api-test-report.html`