import unittest
# from unittest import TestCase
from data_processor.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    """The following constant has been provided to reduce the amount of 
    code needed when creating DataProcessor class objects in the tests that 
    follow.  To use the constant, prefix it with self.  Examples:
    self.INPUT_DATA
    e.g.:  data_procesor = DataProcessor(self.INPUT_DATA)
    """
    INPUT_DATA = [
        {"Transaction ID": "1", "Account number": "1001", "Date": "2023-03-01", "Transaction type": "deposit", "Amount": "1000", "Currency": "CAD", "Description": "Salary"}, 
        {"Transaction ID": "2", "Account number": "1002", "Date": "2023-03-01", "Transaction type": "deposit", "Amount": "1500", "Currency": "CAD", "Description": "Salary"}
    ]
    def setUp(self):
        # Set up the DataProcessor with empty initial data to emphasize the effects of deposit and withdrawal
        self.data_processor = DataProcessor([])
    # update_account_summary: Test to verify that the balance and total_deposits values in the account_summary dictionary are correct when a deposit row is processed.
    def test_update_account_summary_with_deposit(self): 
        #Act
        deposit_transaction = {
            "Transaction ID": "3", "Account number": "1001", "Date": "2023-03-02",
            "Transaction type": "deposit", "Amount": 500, "Currency": "CAD", "Description": "Additional deposit"}
        self.data_processor.update_account_summary(deposit_transaction)
        # Check that the balance and total deposits are correctly updated
        expected_balance = 500
        expected_total_deposits = 500
        account_summary = self.data_processor.account_summaries[deposit_transaction["Account number"]]
        #Assert
        self.assertEqual(expected_balance, account_summary["balance"])
        self.assertEqual(expected_total_deposits, account_summary["total_deposits"])
    #Test to verify that the balance and total_withdrawals values in the account_summary dictionary are correct when a withdrawal row is processed.
    def test_update_account_summary_with_withdrawal(self):
        #ACT
        withdrawal_transaction = {"Transaction ID": "5", "Account number": "1002",
                        "Date": "2023-03-03","Transaction type": "withdrawal","Amount": 300,  
                        "Currency": "CAD", "Description": "Shopping"}
        self.data_processor.update_account_summary(withdrawal_transaction)
        # verify the balance and total withdrawal are correct
        expected_balance = -300 # Expected balance for account 1001 after withdrawal
        expected_total_withdrawals = 300  # Expected total withdrawals for account 1001 after withdrawal
        # Assert for account 1001 after withdrawal
        account_summary = self.data_processor.account_summaries[withdrawal_transaction["Account number"]]
        self.assertEqual(expected_balance,account_summary["balance"])
        self.assertEqual(expected_total_withdrawals, account_summary["total_withdrawals"])
    #check_suspicious_transactions: Test to verify that a transaction amount considered 'large' is written to the suspicious_transactions list.
    def test_large_transaction_flagged_as_suspicious(self):
        # Transaction that exceeds the large transaction threshold
        large_transaction = {
            "Transaction ID": "11",
            "Account number": "1001",
            "Date": "2023-03-13",
            "Transaction type": "deposit",
            "Amount": "12000", 
            "Currency": "CAD",
            "Description": "Car Sale"}
        # Invoke the method to check for suspicious transactions
        self.data_processor.check_suspicious_transactions(large_transaction)
        ## Assert that the transaction with uncommon currency is added to the list
        self.assertIn(large_transaction,self.data_processor.suspicious_transactions)
    #check_suspicious_transactions: Test to verify that a transaction type considered an 'uncommon currency' is written to the suspicious_transactions list.
    def test_uncommon_currency_flagged_as_suspicious(self):
        # Transaction with uncommon currency
        uncommon_currency_transaction = {
            "Transaction ID": "2",
            "Account number": "1002",
            "Date": "2023-03-01",
            "Transaction type": "withdrawal",
            "Amount": "200",
            "Currency": "XRP",  # This currency is listed as uncommon
            "Description": "Crypto withdrawal"}
        # Invoke the method to check for suspicious transactions
        self.data_processor.check_suspicious_transactions(uncommon_currency_transaction)
        # Assert that the transaction with uncommon currency is added to the list
        self.assertIn(uncommon_currency_transaction, self.data_processor.suspicious_transactions)
    #update_transaction_statistics: Test to verify that transaction statistics are being accurately reported.
    def test_update_transaction_statistics_for_deposit(self):
        transactions = [
            { "Transaction ID": "1","Account number": "1001","Date": "2023-03-01",
            "Transaction type": "deposit","Amount": "1000","Currency": "CAD", "Description": "Salary"},
            {"Transaction ID": "2","Account number": "1002", "Date": "2023-03-02","Transaction type": "withdrawal",
            "Amount": "500","Currency": "CAD","Description": "Rent Payment"}]
        #act
        for transaction in transactions:
            self.data_processor.update_transaction_statistics(transaction)
    # Checking deposit statistics
        deposit_stats = self.data_processor.transaction_statistics.get("deposit")
        self.assertIsNotNone(deposit_stats)
        #expected results
        expected_deposit_amount = 1000 # Sum of all deposits
        expected_deposit_count = 1 # Number of deposits
        # Assert comprehensive statistics updates
        #check deposit statitics
        self.assertEqual(deposit_stats["total_amount"],expected_deposit_amount)
        self.assertEqual(deposit_stats["transaction_count"], expected_deposit_count)
    # Checking withdrawal statistics
        withdrawal_stats = self.data_processor.transaction_statistics.get("withdrawal")
        self.assertIsNotNone(withdrawal_stats)
        #expected results
        expected_withdrawal_amount = 500 # Sum of all withdrawal 
        expected_withdrawal_count = 1 # Number of withdrawals 
        #Assert
        self.assertEqual(withdrawal_stats["total_amount"], expected_withdrawal_amount)
        self.assertEqual(withdrawal_stats["transaction_count"], expected_withdrawal_count)
    # get_average_transaction_amount: Test to verify that the deposit average and withdrawal average are being correctly calculated.
    def test_get_average_transaction_amount(self):
        transactions = [
            {"Transaction ID": "1", "Account number": "1001", "Date": "2023-03-01", 
             "Transaction type": "deposit", "Amount": "2000", "Currency": "CAD", "Description": "Salary"},
            {"Transaction ID": "2", "Account number": "1002", "Date": "2023-03-02",
             "Transaction type": "deposit", "Amount": "1500", "Currency": "CAD", "Description": "Bonus"},
            {"Transaction ID": "3", "Account number": "1001", "Date": "2023-03-03",
             "Transaction type": "withdrawal", "Amount": "500", "Currency": "CAD", "Description": "Rent"},
            {"Transaction ID": "4", "Account number": "1002", "Date": "2023-03-04",
             "Transaction type": "withdrawal", "Amount": "400", "Currency": "CAD", "Description": "Utilities"}
        ]
        # Act
        for transaction in transactions:
            self.data_processor.update_transaction_statistics(transaction)
        average_deposit = self.data_processor.get_average_transaction_amount("deposit")
        average_withdrawal = self.data_processor.get_average_transaction_amount("withdrawal")
        # Expected averages calculated manually
        expected_average_deposit = (2000 + 1500) / 2
        expected_average_withdrawal = (500 + 400) / 2
        #Assert
        self.assertEqual(expected_average_deposit, average_deposit)
        self.assertEqual(expected_average_withdrawal, average_withdrawal)
if __name__ == "__main__":
    unittest.main()

