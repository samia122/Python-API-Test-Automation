# User Management API Testing Project

## Overview

This project demonstrates real-world API testing using Python by performing data-driven user creation and validation against a REST API. It simulates backend test automation workflows where user data is dynamically read from a CSV file, processed via API requests, and validated through response verification.

The project also includes logging, retry mechanisms, and error handling to reflect production-level test automation practices.

---

## Features

- Data-driven API testing using CSV input  
- Automated user creation via POST requests  
- User verification via GET requests  
- Retry mechanism for handling transient API failures  
- Centralized logging (console + file)  
- Robust exception handling  
- Response validation and data integrity checks  
- Lightweight CI/CD-ready structure  

---

## Tech Stack

- Python 3  
- Requests (HTTP client)  
- CSV Module  
- Logging Module  
- Git & GitHub  
- GitHub Actions (basic CI execution)  

## Project Structure
UserManagementAPI/
│
├── users.csv # Test data source
├── api_test.py # Main API test script
├── app.log # Execution logs (auto-generated)
├── README.md # Project documentation

## Test Data

User data is maintained in a CSV file for data-driven testing.

name,email
John Doe,john@test.com
Jane Smith,jane@test.com

## Installation

Clone the repository:

git clone <repository-url>
cd <repository-name>

Install dependencies:

pip install requests

## Running the Project

Execute the test script:

python api_test.py

## Test Workflow

- Load user data from users.csv
- Send POST requests to create users
- Retry failed API calls (up to 3 attempts)
- Log execution results
- Fetch user data using GET request
- Validate expected vs actual response data
- Generate final verification report in logs

## Logging

The framework provides dual logging:

Console output (real-time visibility)
File logging (app.log) for traceability

Example log:

2026-06-09 13:45:20 - INFO - User created: john@test.com

Error Handling

The project is designed to handle:

Network timeouts
API failures (4xx / 5xx responses)
Invalid CSV records
Unexpected runtime exceptions

## Note

This project uses the JSONPlaceholder API:

https://jsonplaceholder.typicode.com

It is a mock API used for learning purposes. While POST requests return success responses, data is not persisted permanently. Therefore, GET-based validation reflects API behavior limitations.

## Learning Outcomes

This project demonstrates practical knowledge of:

- REST API automation testing
- HTTP methods (GET, POST)
- Data-driven testing approach
- Retry and resilience strategies
- Logging and debugging practices
- Exception handling in automation
- CSV-based test data management
- CI-ready test automation structure

## Future Improvements
- Add Pytest framework integration
- Generate HTML / Allure test reports
- Implement schema validation (JSON Schema)
- Add authentication-based API testing
- Expand CI/CD pipeline with test reporting artifacts
- Add parallel test execution support

## Author

Samia Sultana
Software Quality Assurance Engineer
