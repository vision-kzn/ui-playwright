# Python UI tests

Create and activate a virtual environment:

```shell
python -m venv venv # Create virtual environment
source venv/bin/activate # Activate on macOS/Linux
venv\Scripts\activate # Activate on Windows
```

Install dependencies:

```shell
pip install --upgrade pip # Upgrade pip to the latest version
pip install -r requirements.txt # Install required dependencies
playwright install # Install playwright dependencies
```

## Running Tests

To run UI tests using pytest:

```shell
pytest -m regression --numprocesses 2 # Run regression tests in parallel
```

## Generating Allure Reports

Run tests and generate Allure results:

```shell
pytest -m regression --alluredir=allure-results
```