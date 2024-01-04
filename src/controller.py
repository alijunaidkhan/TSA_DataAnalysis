# controller.py
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QToolButton
from model import Model
from view import View


class Controller:
    """
    The Controller component in the MVC architecture, responsible for handling user interactions,
    updating the model, and reflecting changes in the view.

    This class creates and manages the connections between the model and the view, ensuring the
    separation of the GUI and the business logic/data handling.
    """

    def __init__(self):
        """
        Initializes the Controller component.

        Creates instances of the Model and the View, and sets up the necessary connections between them.
        """
        self.model = Model()
        self.view = View(self)

    def run(self):
        """
        Starts the application by displaying the view.
        """
        self.view.show()

    def set_directory(self):
        """
        Opens a dialog for the user to select a directory and updates the model's working directory.
        """
        directory = QFileDialog.getExistingDirectory(self.view, "Select Directory")
        if directory:  # check if a directory was selected
            self.model.set_working_directory(directory)

    def load_data(self):
        """
        Opens a file dialog for the user to select a file and loads the data.
        """
        file_dialog = QFileDialog(self.view)
        file_path, _ = file_dialog.getOpenFileName(
            self.view, "Open File", "", "Excel Files (*.xlsx);;CSV Files (*.csv)")

        if file_path:
            if file_path.endswith('.csv'):
                file_type = 'csv'
            elif file_path.endswith('.xlsx'):
                file_type = 'excel'
            else:
                self.view.show_message("Unsupported file format")
                return

            try:
                data = self.model.load_data(file_path, file_type)
                self.view.display_data(data)
                shape_message = f"Data Loaded: {data.shape[0]} rows, {data.shape[1]} columns"
                self.view.update_status_bar(shape_message)
            except Exception as e:
                self.view.show_message(f"Error loading data: {e}")

    def save_as(self):
        """
        Handles the logic to save data from the model.

        This method is a placeholder and should be implemented to allow the model to save data to a file or other destinations.
        """
        pass

    def change_theme(self):
        """
        Handles the logic to change the application's theme.

        This method is a placeholder and should be implemented to modify the view's appearance according to the selected theme.
        """
        pass

# Additional code and imports would go here
