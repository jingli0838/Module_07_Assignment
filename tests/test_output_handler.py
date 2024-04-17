import unittest
from unittest import TestCase
from unittest.mock import patch, mock_open
from output_handler.output_handler import OutputHandler


class TestOutputHandler(TestCase):
    """Your test class documentation."""

    ACCOUNT_SUMMARIES = { '1001': {'account_number': '1001', 'balance': 50, 
                            'total_deposits': 100, 'total_withdrawals': 50},
                            '1002': {'account_number': '2', 'balance': 200, 
                            'total_deposits': 200, 'total_withdrawals': 0}}
    
    SUSPICIOUS_TRANSACTIONS = [{"Transaction ID":"1" ,"Account number":"1001" ,
                            "Date":"2023-03-14" ,"Transaction type": "deposit",
                            "Amount":250,"Currency":"XRP","Description":"crypto investment"}  ]

    TRANSACTION_STATISTICS = {'deposit': {'total_amount': 300, 'transaction_count': 2}, 
                            'withdrawal': {'total_amount': 50, 'transaction_count': 1}}

    @patch("output_handler.output_handler.csv.writer")
    @patch("output_handler.output_handler.open", new_callable=mock_open)
    def test_write_account_summaries_to_csv(self, mock_open, mock_csv_writer):
        # Arrange
        output_handler = OutputHandler(self.ACCOUNT_SUMMARIES, self.SUSPICIOUS_TRANSACTIONS, self.TRANSACTION_STATISTICS)
        file_path = "test_account_summaries.csv"

        # Act
        output_handler.write_account_summaries_to_csv(file_path)

        # Assert
        mock_open.assert_called_once_with(file_path, 'w', newline='')
        mock_csv_writer.return_value.writerow.assert_called()
        self.assertEqual(mock_csv_writer.return_value.writerow.call_count, len(self.ACCOUNT_SUMMARIES) + 1)

    @patch("output_handler.output_handler.csv.writer")
    @patch("output_handler.output_handler.open", new_callable=mock_open)
    def test_write_suspicious_transactions_to_csv(self, mock_open, mock_csv_writer):
        # Arrange
        output_handler = OutputHandler(self.ACCOUNT_SUMMARIES, self.SUSPICIOUS_TRANSACTIONS, self.TRANSACTION_STATISTICS)
        file_path = "test_suspicious_transactions.csv"

        # Act
        output_handler.write_suspicious_transactions_to_csv(file_path)

        # Assert
        mock_open.assert_called_once_with(file_path, 'w', newline='')
        mock_csv_writer.return_value.writerow.assert_called()
        self.assertEqual(mock_csv_writer.return_value.writerow.call_count, len(self.SUSPICIOUS_TRANSACTIONS) + 1)

    @patch("output_handler.output_handler.csv.writer")
    @patch("output_handler.output_handler.open", new_callable=mock_open)
    def test_write_transaction_statistics_to_csv(self, mock_open, mock_csv_writer):
        # Arrange
        output_handler = OutputHandler(self.ACCOUNT_SUMMARIES, self.SUSPICIOUS_TRANSACTIONS, self.TRANSACTION_STATISTICS)
        file_path = "test_transaction_statistics.csv"

        # Act
        output_handler.write_transaction_statistics_to_csv(file_path)

        # Assert
        mock_open.assert_called_once_with(file_path, 'w', newline='')
        mock_csv_writer.return_value.writerow.assert_called()
        self.assertEqual(mock_csv_writer.return_value.writerow.call_count, len(self.TRANSACTION_STATISTICS) + 1)


if __name__ == "__main__":
    unittest.main()
