# controller.py
import pandas as pd
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from model import Model
from view import View, DataInfoDialog, SetIndexDialog, SetFrequencyDialog


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
            #self.view, "Open File", "", "Excel Files (*.xlsx);;CSV Files (*.csv)")
            self.view, "Open File", "", "CSV Files (*.csv);;Excel Files (*.xlsx)")
            
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

                # Update the column names in the view
                self.view.lineplotting_dialog.update_combobox_items(self.model.data_frame.columns)

            except Exception as e:
                self.view.show_message("Loading Error", f"Error loading data: {e}")

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

######################################################## trying Functionalities for docked widget#####################################################
    def update_column_names(self):
        """
        Updates the column names in the combo box based on the loaded DataFrame.
        """
        if self.model.data_frame is not None:
            columns = self.model.data_frame.columns
            self.view.comboBox.clear()
            self.view.comboBox.addItems(columns)

    def calculate_shape(self):
        """
        Calculates the shape of the selected column and displays it.
        """
        selected_column = self.view.comboBox.currentText()
        if selected_column:
            shape = self.model.data_frame[selected_column].shape
            self.view.output_display.setText(f"Shape: {shape}")

    def calculate_dtype(self):
        """
        Calculates the data type of the selected column and displays it.
        """
        selected_column = self.view.comboBox.currentText()
        if selected_column:
            dtype = self.model.data_frame[selected_column].dtype
            self.view.output_display.setText(f"Data Type: {dtype}")

    def calculate_statistics(self):
        """
        Calculates descriptive statistics of the selected column and displays them.
        """
        selected_column = self.view.comboBox.currentText()
        if selected_column:
            statistics = self.model.data_frame[selected_column].describe()
            formatted_stats = statistics.to_string()  # Convert the statistics to a string for display

            # Add header with separator lines
            separator = "=" * 25
            display_text = f"{separator}\nDescriptive Statistics\n{separator}\n{formatted_stats}"

            self.view.output_display.setText(display_text)

    def calculate_unique(self):
        """
        Calculates the number of unique values in the selected column and displays it with formatting.
        """
        selected_column = self.view.comboBox.currentText()
        if selected_column:
            unique_count = self.model.data_frame[selected_column].nunique()
            formatted_output = (
                "====================\n"
                "Unique Values Count\n"
                "====================\n"
                f"{unique_count}"
            )
            self.view.output_display.setText(formatted_output)

    def calculate_missing(self):
        """
        Calculates the number of missing (null) values in the selected column and displays it.
        """
        selected_column = self.view.comboBox.currentText()
        if selected_column:
            missing_count = self.model.data_frame[selected_column].isnull().sum()
            self.view.output_display.setText(f"Number of Missing Values: {missing_count}")

    def calculate_nans(self):
        """
        Calculates the number of NaN values in the selected column and displays it.
        """
        selected_column = self.view.comboBox.currentText()
        if selected_column:
            nan_count = self.model.data_frame[selected_column].isna().sum()
            self.view.output_display.setText(f"Number of NaNs: {nan_count}")

##########################################################################################################
############################### Explore menu #############################################################
    def open_data_info(self):
        """
        Handles the 'Data Info' action. Opens the DataInfoDialog with the current DataFrame info.
        """
        if self.model.data_frame is not None:
            data_info = {
                'columns': self.model.data_frame.columns.tolist(),
                'data_types': [str(dtype) for dtype in self.model.data_frame.dtypes],
                'missing_values': self.model.data_frame.isnull().sum().tolist()
            }
            dialog = DataInfoDialog(self)  # Pass the controller instance
            dialog.populate_data_info(data_info)
            dialog.exec()

    def convert_columns_data(self, column_names, new_dtype):
        # Initialize a list with default values ('False' indicating no conversion initially)
        conversion_status = {col: False for col in self.model.data_frame.columns}

        for column_name in column_names:
            if column_name in self.model.data_frame.columns:
                try:
                    if new_dtype == 'Integer':
                        self.model.data_frame[column_name] = pd.to_numeric(
                            self.model.data_frame[column_name], errors='coerce', downcast='integer')
                    elif new_dtype == 'Float':
                        self.model.data_frame[column_name] = pd.to_numeric(
                            self.model.data_frame[column_name], errors='coerce')
                    elif new_dtype == 'Date Time':
                        # Using astype for datetime conversion
                        self.model.data_frame[column_name] = self.model.data_frame[column_name].astype(
                            'datetime64[ns]')
                    elif new_dtype == 'Boolean':
                        self.model.data_frame[column_name] = self.model.data_frame[column_name].astype(
                            bool)

                    # Mark as successfully converted
                    conversion_status[column_name] = True
                except Exception as e:
                    # Log or handle exceptions as needed.
                    pass

        # Update the View to reflect changes
        successfully_converted = [col for col, status in conversion_status.items() if status]
        if successfully_converted:
            self.view.display_data(self.model.data_frame)
            message = f"Columns {', '.join(successfully_converted)} were successfully converted to {new_dtype}."
            QMessageBox.information(self.view, "Success", message)
        else:
            self.view.show_message("Warning", "No columns were converted.")


# ==============================================================================================================


    def set_index(self):
        """
        Opens a dialog for the user to select a column to set as the index of the DataFrame.
        """
        if self.model.data_frame is not None:
            # Create and show the SetIndexDialog
            dialog = SetIndexDialog(self.model.data_frame.columns.tolist(), self.view)
            if dialog.exec():
                selected_column = dialog.get_selected_column()
                if selected_column:
                    try:
                        # Set the selected column as index and preserve its position
                        self.model.set_index_and_preserve_column(selected_column)
                        # Refresh the display to show changes
                        self.view.display_data(self.model.data_frame)
                        # Display success message
                        self.view.show_message(
                            "Index Set", f"Column '{selected_column}' set as index.")
                    except Exception as e:
                        # Display error message in case of failure
                        self.view.show_message("Error", str(e))
        else:
            # Display an error message if no data is loaded
            self.view.show_message("Error", "No data loaded.")

    def set_frequency(self):
        """
        Shows the set frequency dialog and updates the frequency of the DataFrame index.
        """
        dialog = SetFrequencyDialog(self.view)
        if dialog.exec():
            frequency = dialog.get_frequency()
            try:
                self.model.set_frequency(frequency)
                self.view.show_message("Frequency Updated", f"Frequency set to: {frequency}")
            except ValueError as e:
                self.view.show_message("Error", str(e))

    def stationarity_test_visual(self):
        # Placeholder for Visual Stationarity Test functionality
        # self.view.show_message("Visual Stationarity Test functionality to be implemented.")
        QMessageBox.information("Visual Stationarity Test functionality to be implemented.")

    def stationarity_test_statistical(self):
        # Placeholder for Statistical Stationarity Test functionality
        # self.view.show_message("Statistical Stationarity Test functionality to be implemented.")
        QMessageBox.information("Quantitative Stationarity Test functionality to be implemented.")

#############################################################################################################################

    def open_line_plot_dialog(self):
        if self.model.data_frame is not None:
            # Access the lineplotting dialog from the view
            self.view.lineplotting_dialog.populate_columns(self.model.data_frame.columns)
            self.view.lineplotting_dialog.show()
        else:
            self.view.show_message("Error", "No data loaded.")

    def plot_selected_columns(self, selected_columns):
        if selected_columns:
            data_to_plot = self.model.get_data_for_columns(selected_columns)
            self.view.lineplotting_dialog.plot_data(data_to_plot)
        else:
            self.view.show_message("Warning", "No columns selected for plotting.")


##########################################################################################
    """For Decomposition of Series"""           
##########################################################################################            
            
    def open_seasonal_decompose_dialog(self):
        """Opens the Seasonal Decompose Dialog."""
        if self.model.data_frame is not None:
            series_list = self.model.data_frame.columns.tolist()
            self.view.seasonal_decompose_dialog.populate_series(series_list)
            self.view.seasonal_decompose_dialog.show()
        else:
            self.view.show_message("Warning", "No data loaded for decomposition.")




    def perform_seasonal_decomposition(self, series_name, period, model_type):
        """
        Handles the seasonal decomposition request.

        Args:
            series_name (str): The name of the series to decompose.
            period (int): The period of the seasonal component.
            model_type (str): Type of decomposition model ('additive' or 'multiplicative').
        """
        try:
            decomposition_result = self.model.seasonal_decompose(series_name, period, model_type)
            self.view.seasonal_decompose_dialog.plot_decomposition(decomposition_result)
        except Exception as e:
            self.view.show_message("Error", str(e))

    """ End of Decomposition"""
            

##########################################################################################
    """For ACF/PACF and Lag Plot"""           
##########################################################################################  

    def open_lag_acf_pacf_dialog(self):
        """Opens the window for the lag, acf, and pacf plots."""
        if self.model.data_frame is not None:
            series_list = self.model.data_frame.columns.tolist()
            self.view.lag_acf_pacf_dialog.populate_series(series_list)
            self.view.lag_acf_pacf_dialog.show()
        else:
            QMessageBox.warning(self.view, "Warning", "No data loaded for ACF/PACF analysis.")

    def perform_lag_acf_pacf_analysis(self, series_name, number_of_lags):
        """
        Handles the lag, ACF, and PACF analysis request.

        Args:
            series_name (str): The name of the series to analyze.
            number_of_lags (int): The number of lags to be used in the analysis.
        """
        try:
            # Pass the series data directly to the view's plotting methods
            series_data = self.model.data_frame[series_name]
            self.view.lag_acf_pacf_dialog.plot_lag(series_data)
            self.view.lag_acf_pacf_dialog.plot_acf(series_data, number_of_lags)
            self.view.lag_acf_pacf_dialog.plot_pacf(series_data, number_of_lags)
        except Exception as e:
            QMessageBox.critical(self.view, "Error", str(e))




  
