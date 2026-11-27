# Week 4 - Test Traceability and Automation Coverage Report

## 1. Project Information

| Item | Details |
|---|---|
| Project Name | Swag Labs |
| Testing Scope | Week 1 Manual Test Cases |
| UI Automation Framework | Playwright |
| Programming Language | Python |
| Test Framework | Pytest |
| Total Manual Test Cases | 17 |

## 2. Test Traceability Matrix

| Test Case ID | Test Scenario | Manual Result | Automation Status | Automated Test Function |
|---|---|---|---|---|
| TC001 | Successful Login | PASS | Automated UI | `test_valid_login` |
| TC002 | Product Information | PASS | Automated UI | `test_inventory_products_elements` |
| TC003 | Add Multiple Products to Cart | PASS | Automated UI | `test_verify_cart_contents` |
| TC004 | Complete Checkout | PASS | Automated UI | `test_complete_checkout_process` |
| TC005 | Logout | PASS | Automated UI | `test_logout_from_product_page` |
| TC006 | Product Sorting | PASS | Automated UI | `test_product_sorting` |
| TC007 | Repeated Add and Remove | PASS | Automated UI | `test_repeated_add_remove_product` |
| TC008 | Cart Badge Updates | PASS | Partially Automated | `test_verify_cart_contents` |
| TC009 | Empty First Name | PASS | Automated UI | `test_checkout_empty_first_name` |
| TC010 | Empty Last Name | PASS | Manual Only | - |
| TC011 | Empty Postal Code | PASS | Manual Only | - |
| TC012 | Invalid Login Credentials | PASS | Automated UI | `test_invalid_login` |
| TC013 | Valid Username, Invalid Password | PASS | Manual Only | - |
| TC014 | Empty Username | PASS | Manual Only | - |
| TC015 | Empty Password | PASS | Manual Only | - |
| TC016 | Locked-out Account | PASS | Automated UI | `test_invalid_login` |
| TC017 | Checkout with Empty Cart | FAIL | Manual Only | - |

## 3. Automation Coverage Summary

| Metric | Result |
|---|---:|
| Total Week 1 Test Cases | 17 |
| Fully Automated UI Test Cases | 10 |
| Partially Automated Test Cases | 1 |
| Manual Only Test Cases | 6 |
| Full UI Automation Coverage | 58.82% |

### Coverage Calculation

Full UI Automation Coverage:

(10 / 17) × 100 = 58.82%

Partially automated test cases are not included in the full automation coverage calculation.

## 4. Manual-Only and Partial Coverage Details

The following test cases have not been fully automated:

| Test Case ID | Reason |
|---|---|
| TC008 | The current automation verifies the cart badge after adding three products, but does not verify the badge decreasing after removal or disappearing when the cart becomes empty. |
| TC010 | Empty Last Name validation has not yet been implemented in the Playwright test suite. |
| TC011 | Empty Postal Code validation has not yet been implemented in the Playwright test suite. |
| TC013 | Login with a valid username and invalid password has not yet been implemented in the Playwright test suite. |
| TC014 | Empty Username validation has not yet been implemented in the Playwright test suite. |
| TC015 | Empty Password validation has not yet been implemented in the Playwright test suite. |
| TC017 | Empty-cart checkout validation has not yet been implemented in the Playwright test suite. |

These scenarios remain covered by the Week 1 manual testing activities.

## 5. API Automation Scope

A separate API test suite was developed using Python Requests and Pytest against the public PokéAPI.

The API suite contains eight test cases covering:

- Successful GET requests.
- Invalid resource requests and HTTP 404 responses.
- Response schema and data validation.
- Nested JSON response validation.
- API response-time verification.

**Important scope clarification:** The PokéAPI test suite is a separate supplementary API testing project. It does not represent API automation coverage for Swag Labs and is therefore excluded from the Week 1 Swag Labs automation coverage calculation.

## 6. Known Gaps and Risks

- Six Week 1 test cases remain manual only.
- TC008 has partial automation coverage.
- TC017 identified an issue where checkout could be completed with an empty shopping cart.
- The current UI automation suite does not cover every Week 1 manual test scenario.
- The API automation suite targets PokéAPI rather than the Swag Labs application.
- Further automation is needed to improve overall UI test coverage.

## 7. Conclusion

The Week 1 Swag Labs test suite contains 17 manual test cases. Of these, 10 have been fully automated using Playwright, one has partial automation coverage, and six remain manual only.

The resulting full UI automation coverage is 58.82%.

A separate eight-test API automation suite was also developed using PokéAPI as its target. Both UI and API test suites have been integrated into a combined GitHub Actions workflow.

This report reflects the actual automation implementation and distinguishes between fully automated, partially automated, and manual-only test cases.