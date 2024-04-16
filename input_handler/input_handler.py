import csv
import json

class InputHandler:
    """
    Handles input operations for reading data from specified file paths.
    
    This class supports reading from both CSV and JSON file formats. It provides methods to read data
    into a structured list and determine the file format based on the file extension.

    Attributes:
        file_path (str): The full path to the file from which data is to be read.
    """

    def __init__(self, file_path: str):
        """
        Initializes the InputHandler with the specified file path.
        
        Args:
            file_path (str): The full path to the file that data will be read from.
        """
        self.__file_path = file_path

    @property
    def file_path(self):
        """
        Gets the private file path set for this instance.

        Returns:
            str: The file path.
        """
        return self.__file_path

    def get_file_format(self) -> str:
        """
        Determines the file format by extracting the extension from the file path.
        
        Returns:
            str: The file extension (e.g., 'csv', 'json') of the file. If no extension is present,
                 an empty string is returned.
        """
        return self.__file_path.split('.')[-1] if '.' in self.__file_path else ''

    def read_input_data(self) -> list:
        """
        Reads data from the file based on its format (either CSV or JSON).
        
        This method dispatches to either `read_csv_data` or `read_json_data` depending on the file format.
        
        Returns:
            list: A list of dictionaries where each dictionary represents a row of data.
        
        Raises:
            ValueError: If the file format is neither 'csv' nor 'json'.
        """
        data = []
        file_format = self.get_file_format()
        if file_format == 'csv':
            data = self.read_csv_data()
        elif file_format == 'json':
            data = self.read_json_data()
        else:
            raise ValueError("Unsupported file format. Please provide a .csv or .json file.")
        return data

    def read_csv_data(self) -> list:
        """
        Reads data from a CSV file and organizes it into a list of dictionaries.
        
        Each dictionary represents a row from the CSV file with keys as the column headers.

        Returns:
            list: A list of dictionaries containing the data read from the CSV file.
        
        Raises:
            FileNotFoundError: If the CSV file specified does not exist.
        """
        input_data = []
        try:
            with open(self.__file_path, 'r') as input_file:
                reader = csv.DictReader(input_file)
                for row in reader:
                    input_data.append(row)
            return input_data
        
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")

    def read_json_data(self) -> list:
        """
        Reads data from a JSON file and returns it as a list or a dictionary,
        depending on the structure of the JSON.

        Returns:
            list/dict: The data extracted from the JSON file, structured as a list or dictionary.
        
        Raises:
            FileNotFoundError: If the JSON file specified does not exist.
        """
        try:
            with open(self.__file_path, 'r') as input_file:
                input_data = json.load(input_file)
            return input_data
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self.__file_path} does not exist.")
