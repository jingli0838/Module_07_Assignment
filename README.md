# Assignment 7
Description
Group Financial Data Processing assignment.

# Authors
- Developer 1: {Md Apurba Khan}
- Developer 2: {Jing Li}
- Developer 3: {Abdul Rahman Bangura}

# Milestone 1
## Developer 1 Tasks (Issue 1):
## Developer 2 Tasks (Issue 2):
- Created a branch specifically for adding documentation and tests to the DataProcessor class.
- Reviewed and understood the DataProcessor class functions.
- Wrote comprehensive docstrings and inline comments in the `data_processor.py` file following PEP-8 documentation guidelines.
- Modified `test_data_processor.py` in the tests directory to include various unit tests:
  - Test to verify correct balance and total deposits in `update_account_summary` for deposits.
  - Test to verify correct balance and total withdrawals in `update_account_summary` for withdrawals.
  - Test to verify that large transaction amounts are identified as suspicious in `check_suspicious_transactions`.
  - Test to verify that transactions in an uncommon currency are identified as suspicious in `check_suspicious_transactions`.
  - Test to verify the accuracy of transaction statistics in `update_transaction_statistics`.
  - Test to calculate and verify average transaction amounts for deposits and withdrawals in `get_average_transaction_amount`.
- Ensured all tests pass and the code adheres to project standards.
## Developer 3 Tasks (Issue 3): Added Documentation and Tests for OutputHandler class
# Milestone 2
## Developer 1 Tasks (Issue 4):
## Developer 2 Tasks (Issue 5):
 Created a branch and set up git environment for logging feature.
- Developed a logging mechanism within the DataProcessor class to handle events, warnings, and errors.
- Modified the `__init__` method of the DataProcessor class to include logging level, format, and file as optional parameters with default settings.
- Updated the `process_data`, `update_account_summary`, `check_suspicious_transactions`, and `update_transaction_statistics` methods to incorporate logging at appropriate levels.
- Created unit tests to ensure the logging mechanism works correctly, including tests using `assertLogs()` to check the logging output.
- Integrated logging into the main workflow, ensuring logs are written successfully.
## Developer 3 Tasks (Issue 6):
