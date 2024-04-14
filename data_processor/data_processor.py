class DataProcessor:
    """
    A class for processing transactional data to identify suspicious transactions,
    summarize account activities, and compute transaction statistics.
    Attributes:
    __input_data (list): A list of transaction dictionaries.
    __account_summaries (dict): A dictionary mapping account numbers to their summaries.
    __suspicious_transactions (list): A list of transactions that are deemed suspicious.
    __transaction_statistics (dict): A dictionary summarizing transaction statistics.

    Constants:
    LARGE_TRANSACTION_THRESHOLD (int): Threshold amount above which transactions are considered large.
    UNCOMMON_CURRENCIES (list): List of currency codes considered uncommon.
    """

    LARGE_TRANSACTION_THRESHOLD = 10000
    UNCOMMON_CURRENCIES = ['XRP', 'LTC']

    def __init__(self, input_data: list):
        """
        Initializes the DataProcessor with the given input data.
        Parameters:
        input_data (list): A list of transaction dictionaries.
        """
        self.__input_data = input_data
        self.__account_summaries = {}
        self.__suspicious_transactions = []
        self.__transaction_statistics = {}

    @property
    def input_data(self):
        """
        list: Returns the input transaction data.
        """
        return self.__input_data
    
    @property
    def account_summaries(self):
        """
        dict: Returns a dictionary of account summaries.
        """
        return self.__account_summaries
    
    @property
    def suspicious_transactions(self):
        """
        list: Returns a list of suspicious transactions.
        """
        return self.__suspicious_transactions
    
    @property
    def transaction_statistics(self):
        """
        dict: Returns transaction statistics.
        """
        return self.__transaction_statistics


    def process_data(self) -> dict:
        """
        Processes the input data to update account summaries, check for suspicious transactions,
        and update transaction statistics.
        Returns:
        dict: A dictionary containing the account summaries, suspicious transactions, and transaction statistics.
        """
        for row in self.__input_data:
            self.update_account_summary(row)
            self.check_suspicious_transactions(row)
            self.update_transaction_statistics(row)

        return {
            "account_summaries": self.__account_summaries,
            "suspicious_transactions": self.__suspicious_transactions,
            "transaction_statistics": self.__transaction_statistics
        }

    def update_account_summary(self, row: dict) -> None:
        """
        Updates the summary information for an account based on a single transaction.
        Parameters:
        row (dict): A dictionary representing a single transaction.
        """
        account_number = row['Account number']
        transaction_type = row['Transaction type']
        amount = float(row['Amount'])
        # Initialize account summary if not already present
        if account_number not in self.__account_summaries:
            self.__account_summaries[account_number] = {
                "account_number": account_number,
                "balance": 0,
                "total_deposits": 0,
                "total_withdrawals": 0
            }
        # Update account balance and totals based on transaction type    
        if transaction_type == "deposit":
            self.__account_summaries[account_number]["balance"] += amount
            self.__account_summaries[account_number]["total_deposits"] += amount
        elif transaction_type == "withdrawal":
            self.__account_summaries[account_number]["balance"] -= amount
            self.__account_summaries[account_number]["total_withdrawals"] += amount

    def check_suspicious_transactions(self, row: dict) -> None:
        """
        Checks if a transaction is suspicious and adds it to the list of suspicious transactions if so.
        Parameters:
        row (dict): A dictionary representing a single transaction.
        """
        amount = float(row['Amount'])
        currency = row['Currency']

        if amount > self.LARGE_TRANSACTION_THRESHOLD or currency in self.UNCOMMON_CURRENCIES:
            self.__suspicious_transactions.append(row)
        # A transaction is suspicious if above a threshold or in uncommon currencies
    def update_transaction_statistics(self, row: dict) -> None:
        """
        Updates statistics for a given transaction type.
        Parameters:
        row (dict): A dictionary representing a single transaction.
        """
        transaction_type = row['Transaction type']
        amount = float(row['Amount'])
        # Initialize transaction type statistics if not already present
        if transaction_type not in self.__transaction_statistics:
            self.__transaction_statistics[transaction_type] = {
                "total_amount": 0,
                "transaction_count": 0
            }
        # Update total amount and transaction count for the type
        self.__transaction_statistics[transaction_type]["total_amount"] += amount
        self.__transaction_statistics[transaction_type]["transaction_count"] += 1
        
    def get_average_transaction_amount(self, transaction_type: str) -> float:
        """
        Calculates the average amount for a given transaction type.

        Parameters:
        transaction_type (str): The type of transaction to calculate the average amount for.

        Returns:
        float: The average transaction amount for the specified type.
        """
        total_amount = self.__transaction_statistics[transaction_type]["total_amount"]
        transaction_count = self.__transaction_statistics[transaction_type]["transaction_count"]
        # Calculate average; avoid division by zero
        if transaction_count == 0:
            average = 0
        else:
            average = total_amount / transaction_count
        
        return average
