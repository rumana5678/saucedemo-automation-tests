```
# Saucedemo Automation Tests
Automation tests for SauceDemo scenarios with Allure reports

## Project Structure

saucedemo-tests/
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_q1.py
│   ├── test_q2.py
│   └── test_q3.py
├── requirements.txt
└── README.md

## Pre-requisites

- Python 3.x
- Chrome Browser
- ChromeDriver in PATH
- Install dependencies:

```bash
pip install -r requirements.txt

````

## Run Tests

### Run individual test:

```bash
pytest tests/test_q1.py --alluredir=allure-results
pytest tests/test_q2.py --alluredir=allure-results
pytest tests/test_q3.py --alluredir=allure-results
```

### Run all tests sequentially:

```bash
pytest tests/ --alluredir=allure-results
```

## Generate Allure Report

```bash
allure serve allure-results
```

* This will open a browser with the test report.

````
