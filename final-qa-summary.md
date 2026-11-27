# Final QA Summary – SkillMe Software Quality Virtual Internship

## 1. Project Overview

This report summarizes the software testing activities conducted throughout Weeks 1–4 of the SkillMe Software Quality Virtual Internship.

The project involved manual testing, UI automation, API testing, test documentation, and Continuous Integration (CI) implementation.

Two separate testing targets were used:
- **Swag Labs:** Manual testing and Playwright UI automation.
- **PokéAPI:** Supplementary API testing using Python Requests and Pytest.

## 2. Test Execution Summary

### Week 1 – Manual Testing

| Metric | Result |
|---|---:|
| Total Test Cases | 17 |
| Passed | 16 |
| Failed | 1 |
| Pass Rate | 94.12% |

### Week 3 – UI Automation

| Metric | Result |
|---|---:|
| Total Week 1 Test Cases | 17 |
| Fully Automated | 10 |
| Partially Automated | 1 |
| Manual Only | 6 |
| Full UI Automation Coverage | 58.82% |

The UI automation suite was implemented using Playwright, Python, and Pytest.

### Week 4 – API Testing

| Metric | Result |
|---|---:|
| Total API Test Cases | 8 |
| Passed | 8 |
| Failed | 0 |
| API Test Pass Rate | 100% |

The API test suite used Python Requests and Pytest against the public PokéAPI.

## 3. Bug Summary

A total of six bugs were documented during Week 2. No additional bugs were reported during Week 3.

| Bug ID | Description | Severity | Priority | Status |
|---|---|---|---|---|
| BUG-001 | Add to Cart button not clickable for certain products | High | High | NEW |
| BUG-002 | Remove button not clickable for certain products | High | High | NEW |
| BUG-003 | Product sorting does not update correctly | Medium | Medium | NEW |
| BUG-004 | Incorrect product prices displayed | High | High | NEW |
| BUG-005 | Finish button not clickable on Checkout Overview | Critical | High | NEW |
| BUG-006 | Checkout can be completed with an empty cart | High | High | NEW |

All six bugs remain documented with NEW status based on the available bug report records.

## 4. Automation Coverage

The Swag Labs UI automation suite fully covers 10 of the original 17 manual test cases.

- Full UI automation coverage: 58.82%
- Partial automation coverage: 1 test case
- Manual-only coverage: 6 test cases

The separate PokéAPI test suite contains eight API test cases. These are not included in Swag Labs UI automation coverage because they target a different application.

## 5. Continuous Integration

A combined GitHub Actions workflow was implemented to execute both UI and API test suites.

The workflow includes:
- Checking out the Swag Labs UI automation repository.
- Installing Python dependencies.
- Installing Playwright Chromium.
- Executing the UI automation tests.
- Installing API testing dependencies.
- Executing the API test suite.
- Generating and uploading the API HTML test report.

Both UI and API jobs completed successfully in the latest confirmed workflow execution.

An intentional API test assertion failure was also introduced to verify that the CI workflow correctly detects failed tests. The original assertion was subsequently restored, and the workflow passed again.

## 6. Known Gaps and Risks

- Six Swag Labs test cases remain manual only.
- One test case has partial automation coverage.
- BUG-001 through BUG-006 remain in NEW status.
- The UI automation suite does not cover every Week 1 manual scenario.
- The API test suite targets PokéAPI and does not represent Swag Labs API coverage.
- API response time can vary depending on network and server conditions.
- The current combined workflow is triggered by changes to the Week 4 API repository; changes made only to the separate UI repository do not independently trigger it.

## 7. Conclusion

The four-week testing activities covered manual testing, UI automation, API automation, bug reporting, and CI integration.

The Swag Labs project achieved 58.82% full UI automation coverage based on the original 17 manual test cases.

The supplementary PokéAPI test suite successfully executed all eight API test cases, achieving a 100% pass rate in the latest confirmed local execution.

The combined GitHub Actions workflow successfully executed both UI and API test suites, demonstrating the integration of separate automated testing projects within one CI pipeline.

This summary reflects the documented test results, automation implementation, and known limitations at the time of reporting.