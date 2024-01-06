# controller.py
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QToolButton
from model import Model
from view import View
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QToolButton
from PyQt6.QtCore import pyqtSlot

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

        # Connect the custom signal to the select_column method
        #self.view.columnSelected.connect(self.select_column)
    @pyqtSlot(str)
    def select_column(self, column_name):
        """
        Handles the selection of a single column from the custom signal.
        """
        # Placeholder code for processing the selected column
        print(f"Selected Column: {column_name}")
        # You can add more logic here to handle the selected column


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

    def select_column(self, column_name):
        """
        Handles the selection of a single column from the combobox.
        """
        # Placeholder code for processing the selected column
        print(f"Selected Column: {column_name}")
        # You can add more logic here to handle the selected column

    def save_as(self):
        """
        Opens a file dialog for the user to select a location to save the current data.
        """
        if hasattr(self.model, 'data'):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_path, _ = QFileDialog.getSaveFileName(self.view, "Save As...", "", "CSV Files (*.csv);;Excel Files (*.xlsx)", options=options)

            if file_path:
                try:
                    self.model.save_data(self.model.data, file_path)
                    self.view.update_status_bar("Data saved successfully.")
                except Exception as e:
                    self.view.show_message(f"Error saving data: {e}")
        else:
            self.view.show_message("No data to save.")
    def change_theme(self):
        """
        Handles the logic to change the application's theme.

        This method is a placeholder and should be implemented to modify the view's appearance according to the selected theme.
        """
        pass
    def set_light_theme(self):
        # Placeholder implementation
        self.setStyleSheet("""
            /* Light Theme Styles */
            background-color: #FFFFFF;
            color: #000000;
        """)

    def set_dark_theme(self):
        # Placeholder implementation
        self.setStyleSheet("""
            /* Dark Theme Styles */
            background-color: #1E1E1E;
            color: #FFFFFF;
        """)
    def show_about_software(self):
        # Placeholder implementation
        QMessageBox.information(self, "About Software", "This is a placeholder for the About Software information.")

    def show_documentation(self):
        # Placeholder implementation
        QMessageBox.information(self, "Documentation", "This is a placeholder for the Documentation information.")
    # Controller class

    def show_used_cases(self):
        # Placeholder implementation
        QMessageBox.information(self, "Used Cases", "This is a placeholder for the Used Cases information.")

    def show_feedback(self):
        # Placeholder implementation
        QMessageBox.information(self, "Feedback", "This is a placeholder for the Feedback information.")

    def show_updates(self):
        # Placeholder implementation
        QMessageBox.information(self, "Updates", "This is a placeholder for the Updates information.")
    def on_data_loaded(self, data):
        self.data = data
        self.create_column_menu()
        self.statusbar.showMessage(
            f"Shape: {self.data.shape[0]} Rows × {self.data.shape[1]} Columns")
        # Update the QLineEdit with the selected file name
        self.file_path_line_edit.setText(self.file_name)
        # Change button colors to green after successful data load
        self.set_buttons_to_green()
        self.progress_dialog.setValue(100)  # Final value indicating completion

    def on_data_load_error(self, error_message):
        self.progress_dialog.cancel()  # Close the progress dialog in case of an error
        self.statusbar.showMessage(f"Error importing data: {error_message}")

    def select_directory(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Set Directory")
        if dir_name:
            global IMAGE_DIRECTORY
            IMAGE_DIRECTORY = dir_name
            self.statusbar.showMessage(f"Directory set to: {IMAGE_DIRECTORY}")

    def set_light_theme(self):
        # Call the method on the view
        self.view.set_light_theme()

    def set_dark_theme(self):
        # Call the method on the view
        self.view.set_dark_theme()

   