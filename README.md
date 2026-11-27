# Week 4 – API Testing Project

## Project Overview

This repository contains an API testing suite developed as part of the SkillMe Software Quality Virtual Internship – Week 4.

The project focuses on testing REST API endpoints using Python, Requests, and Pytest. The test suite uses the public PokéAPI to validate HTTP responses, response data, schema structure, negative scenarios, and response time.

This API project is maintained separately from the Swag Labs UI automation project. Therefore, the PokéAPI tests are supplementary API testing exercises and are not considered API coverage for Swag Labs.

## Tools and Technologies

- **Python 3.12 / 3.14:** Programming language used for API automation.
- **Requests:** HTTP library for sending API requests.
- **Pytest:** Testing framework.
- **pytest-html:** HTML test report generation.
- **GitHub Actions:** Continuous Integration (CI).
- **GitHub:** Source code management and project hosting.

## Project Structure

```text
SkillMe-Week-4-API/
│
├── .github/
│   └── workflows/
│       └── api-test.yaml
│
├── api_tests/
│   ├── conftest.py
│   ├── test_pokemon.py
│   └── test_pokemon_negative.py
│
├── reports/
│   └── api-test-report.html
│
├── api-coverage-report.md
├── final-qa-summary.md
├── pytest.ini
├── requirements.txt
└── README.md
```

## API Test Coverage

The test suite contains eight automated API test cases.

| Test Case ID | Test Scenario | Expected Result |
|---|---|---|
| API-001 | Retrieve Pokémon by valid name | HTTP 200 and correct Pokémon data |
| API-002 | Validate Pokémon response schema | Expected response fields are present |
| API-003 | Validate API response time | Response time is below 2 seconds |
| API-004 | Retrieve Pokémon using a nonexistent name | HTTP 404 |
| API-005 | Retrieve Pokémon using an invalid ID | HTTP 404 |
| API-006 | Retrieve Pokémon list with pagination | Valid pagination fields and results |
| API-007 | Retrieve Pokémon by type | Valid type information and Pokémon entries |
| API-008 | Retrieve Pokémon by ability | Valid ability information and Pokémon entries |

## How to Run the Tests

### 1. Clone the Repository

```bash
git clone https://github.com/Albert-Gavra/SkillMe-Week-4-API.git
```

### 2. Navigate to the Project Directory

```bash
cd SkillMe-Week-4-API
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the API Test Suite

```bash
python -m pytest
```

## Generate an HTML Test Report

To execute the tests and generate an HTML report:

```bash
python -m pytest --html=reports/api-test-report.html --self-contained-html
```

After execution, open `reports/api-test-report.html` in a web browser to view the test results.

## Continuous Integration – GitHub Actions

A combined GitHub Actions workflow is configured to execute:

- Swag Labs UI automation tests using Playwright and Pytest.
- PokéAPI automated tests using Requests and Pytest.

The workflow runs on pushes and pull requests to this API repository.

The workflow also uploads the API HTML test report as a downloadable artifact.

Both UI and API jobs passed in the latest confirmed workflow execution.

An intentional API assertion failure was introduced and tested to verify that the CI workflow correctly detects failed tests. The original assertion was restored afterward.

## Test Results

| Metric | Result |
|---|---:|
| Total API Test Cases | 8 |
| Passed | 8 |
| Failed | 0 |
| Pass Rate | 100% |

These results represent the latest confirmed successful test execution. API response times may vary depending on network and server conditions.

## Additional Documentation

- `api-coverage-report.md` – API test coverage details.
- `final-qa-summary.md` – Overall QA activities and results from Weeks 1–4.

## Notes and Limitations

- This project uses the public PokéAPI as its API testing target.
- The API tests do not represent API coverage for Swag Labs.
- The response-time test depends on external network and server performance.
- The combined CI workflow is triggered by changes to this API repository. Changes made only to the separate UI repository do not independently trigger the workflow.

## Author

**Albert Gavra Septiawan**

GitHub: [Albert-Gavra](https://github.com/Albert-Gavra)