# CI/CD API Testing Project

A hands-on API test automation project built with **Python + pytest + requests**, covering REST API testing from basics to advanced patterns, with automated CI via GitHub Actions.

## What's Inside

| Day | Topic |
|-----|-------|
| Day 1 | HTTP methods: GET, POST, PUT, DELETE |
| Day 2 | Request body, fixtures, json-server mock API |
| Day 3 | Path params & query params |
| Day 4 | Authentication: Bearer token, Basic Auth, Digest Auth, API Key |
| Day 6 | Parsing & validating complex JSON responses |
| Day 7 | XML parsing, JSON schema validation, XML schema validation |
| Day 8 | Chaining API calls, fake data generation |
| Day 9 | Data-driven testing with JSON, CSV, and Excel |

## Tech Stack

- **Python 3.12**
- **pytest** — test runner
- **requests** — HTTP client
- **json-server** — local mock REST API (Node.js)
- **xmltodict** — XML to dict conversion
- **Faker** — fake data generation
- **GitHub Actions** — CI pipeline

## Getting Started

### Prerequisites

- Python 3.12+
- Node.js 20+

### Install dependencies

```bash
pip install -r requirements.txt
npm install -g json-server@1.0.0-beta.3
```

### Start the mock API server

```bash
cd Day2
json-server --watch students.json --port 3000
```

### Run tests (in a separate terminal)

```bash
pytest --ignore=Day5 -k "not test_open_app and not test_calculation" -v
```

## Required GitHub Secrets

To run in GitHub Actions, add the following secret in your repository:

**Settings → Secrets and variables → Actions → New repository secret**

| Secret name | Description | Where to get it |
|-------------|-------------|-----------------|
| `GITHUB_TOKEN_AUTH` | Personal GitHub access token | GitHub → Settings → Developer settings → Personal access tokens |

> **Note:** Never paste tokens directly into code. Always use GitHub Secrets.

## CI Pipeline

The GitHub Actions workflow (`.github/workflows/api-tests.yml`) runs automatically on every `push` and `pull_request`. It:

1. Spins up a `json-server` mock API on port 3000
2. Installs Python dependencies
3. Runs all tests (excluding UI and Day5 tests)
4. Reports results in the Actions tab

## Project Structure

```
.
├── Day1/       # HTTP method basics
├── Day2/       # Fixtures, request body, mock API data
├── Day3/       # URL parameters
├── Day4/       # Authentication methods
├── Day6/       # Complex JSON validation
├── Day7/       # XML & schema validation
├── Day8/       # API chaining & fake data
├── Day9/       # Data-driven tests
├── requirements.txt
└── .github/
    └── workflows/
        └── api-tests.yml
```
