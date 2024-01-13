# model.py
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QToolButton

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
            return pd.read_csv(file_path)
        elif file_type == 'excel':
            return pd.read_excel(file_path)
        # Add database loading logic here if needed
        else:
            raise ValueError("Unsupported file type")
   
