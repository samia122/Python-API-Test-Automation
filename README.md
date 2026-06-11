# User Management API Testing Project

## Overview

This project demonstrates API testing using Python by performing data-driven user creation and validation against a REST API. User data is loaded from a CSV file, sent to the API through POST requests, and verified through GET requests. The project also includes logging, retry mechanisms, and error handling to simulate real-world API testing scenarios.

## Features

* Data-driven testing using CSV files
* User creation through POST API requests
* User verification through GET API requests
* Retry mechanism for failed API calls
* Logging to both console and file
* Exception and error handling
* Simple validation of API response data

## Tech Stack

* Python 3
* Requests
* CSV Module
* Logging Module

## Project Structure

```
project/
│
├── users.csv          # Test data
├── api_test.py        # Main test script
├── app.log            # Generated log file
├── README.md
```

## Test Data

The script reads user data from a CSV file.

Example:

```csv
name,email
John Doe,john@test.com
Jane Smith,jane@test.com
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Install dependencies:

```bash
pip install requests
```

## Running the Project

Execute the script:

```bash
python api_test.py
```

## Test Workflow

1. Load user data from `users.csv`
2. Send POST requests to create users
3. Retry failed requests up to three times
4. Log request results
5. Send GET request to retrieve users
6. Compare expected users against API response
7. Generate verification results

## Logging

The project logs execution details to:

* Console output
* `app.log`

Example log:

```text
2026-06-09 13:45:20 - INFO - User created: john@test.com
```

## Error Handling

The script handles:

* Network failures
* API errors
* Invalid CSV records
* Unexpected runtime exceptions

## Note

This project uses the JSONPlaceholder API:

https://jsonplaceholder.typicode.com

JSONPlaceholder is a mock API used for learning and testing purposes. POST requests return successful responses but do not persist data permanently. Therefore, user verification may not reflect newly created users.

## Learning Outcomes

Through this project, the following concepts are demonstrated:

* REST API Testing
* GET and POST Requests
* Data-Driven Testing
* Retry Logic
* Logging
* Exception Handling
* JSON Processing
* CSV File Handling
* Basic Test Automation with Python

## Future Improvements

* Add PUT and DELETE API testing
* Integrate with Pytest
* Generate HTML test reports
* Add response schema validation
* Implement API authentication
* Add CI/CD pipeline integration using GitHub Actions

## Author

Samia Sultana

Software Quality Assurance Engineer
