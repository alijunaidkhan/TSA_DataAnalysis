# model.py
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf





class Model:
    """
    The Model part of the MVC architecture. It is responsible for managing the data, logic, and rules of the application.

    Attributes:
        working_directory (str): Stores the current working directory for file operations.
    """

    def __init__(self):
        """
        Initializes the Model with default values.
        """
        self.working_directory = None
        self.data_frame = None  # Initialize the data_frame attribute

    def set_working_directory(self, directory):
        """
        Sets the working directory where file operations are performed.

        Args:
            directory (str): The path of the directory to set as the working directory.
        """
        self.working_directory = directory

    def load_data(self, file_path, file_type):
        """
        Loads data from the specified file into a pandas DataFrame.
        Args:
            file_path (str): Path of the file to be loaded.
            file_type (str): Type of the file ('csv', 'excel', or 'database').
        Returns:
            pd.DataFrame: The loaded data.
        """
        if file_type == 'csv':
            self.data_frame = pd.read_csv(file_path)
        elif file_type == 'excel':
            self.data_frame = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file type")
        return self.data_frame  # Return the loaded DataFrame

    def save_data(self, data, file_path):
        """
        Saves data to a specified file.

        Placeholder method to be implemented.

        Args:
            data: Data to be saved.
            file_path (str): The path of the file to save data to.
        """
        pass
######################################################## trying Functionalities for docked widget#####################################################
#
#
####################################################################################################################################################

    def set_index_and_preserve_column(self, column_name):
        """
        Sets the specified column as the index of the DataFrame, while preserving the column in the data.
        Args:column_name (str): The name of the column to set as the index.
        """
        if self.data_frame is not None and column_name in self.data_frame.columns:
            # Create a copy of the column to be used as index
            self.data_frame['index_'] = self.data_frame[column_name]
            # Set the column as index
            self.data_frame.set_index(column_name, inplace=True)

        else:
            raise ValueError("Column not found in DataFrame")

    def set_frequency(self, freq):
        """
        Sets the frequency of the DataFrame index.
        Args: freq (str): The frequency string to set."""

        if self.data_frame is not None:
            # Assuming the index is already a datetime-like index
            self.data_frame.index.freq = freq
            print(self.data_frame.index.freq)
        else:
            raise ValueError("DataFrame is not loaded or index is not datetime.")

    def get_data_for_columns(self, columns):
        """Fetch data for the specified columns."""
        if self.data_frame is not None and all(col in self.data_frame.columns for col in columns):
            return self.data_frame[columns]
        else:
            raise ValueError("One or more selected columns are not in the DataFrame")



    def seasonal_decompose(self, series_name, period, model_type):
            """
            Perform seasonal decomposition on a time series.
            Args:
                series_name (str): The name of the series to decompose.
                period (int): The period of the seasonal component.
                model_type (str): Type of decomposition model ('additive' or 'multiplicative').

            Returns:
                DecomposeResult: The result of the decomposition.
            """
            if series_name not in self.data_frame.columns:
                raise ValueError(f"Series '{series_name}' not found in data.")

            series = self.data_frame[series_name]
            result = seasonal_decompose(series, model=model_type, period=period)
            return result
    ############################################################################################



    def get_series_data(self, series_name):
        """
        Retrieve the time series data for the given series name.

        Args:
            series_name (str): The name of the series to retrieve.

        Returns:
            pd.Series: The requested time series data.
        """
        if series_name not in self.data_frame.columns:
            raise ValueError(f"Series '{series_name}' not found in the DataFrame.")
        return self.data_frame[series_name]