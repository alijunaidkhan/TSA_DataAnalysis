# controller.py
import csv
import os
from pathlib import Path
import time
import numpy as np
import pandas as pd
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from tabulate import tabulate
from model import Model
from view import ResampleDialog, View, DataInfoDialog, SetIndexDialog, SetFrequencyDialog,QDialog
from PyQt6.QtGui import QIcon,QPixmap,QPainter
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt6.QtCore import QDateTime
from PyQt6.QtCore import pyqtSignal, QObject,Qt
import os
import pandas as pd
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from PyQt6.QtGui import QIcon,QFont,QColor
from PyQt6.QtCore import QThread, pyqtSignal, QObject
class CustomMessageBox(QMessageBox):
    def __init__(self, icon_color, message_text, window_title, icon_text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle(window_title)
        self.setText(message_text)
        self.setIconPixmap(self.create_custom_icon(icon_color, icon_text))

    def create_custom_icon(self, color, icon_text):
        size = 29  # Small icon size
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # Enable antialiasing for smooth edges
        painter.setBrush(color)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(0, 0, size, size)

        # Draw user-specified text in the center
        painter.setPen(Qt.GlobalColor.white)
        font = QFont()
        font.setBold(True)
        font.setPointSize(12)  # Adjust font size to fit the small icon
        painter.setFont(font)
        painter.drawText(pixmap.rect(), Qt.AlignmentFlag.AlignCenter, icon_text)

        painter.end()

        return pixmap

# Signals class for safe communication from the thread to the main GUI
class LoaderSignals(QObject):
    data_loaded = pyqtSignal(pd.DataFrame)
    update_status = pyqtSignal(str)
    loading_error = pyqtSignal(str)
    update_combobox = pyqtSignal(list)
    progress = pyqtSignal(int)  # Add this line for progress updates

# Thread class for loading data
class DataLoadThread(QThread):
    def __init__(self,loaded_file_name, file_path, file_type, model):
        super(DataLoadThread, self).__init__()
        self.file_path = file_path
        self.file_type = file_type
        self.model = model
        self.signals = LoaderSignals()
        self.load=loaded_file_name

    def run(self):
        try:
            data = self.model.load_data(self.file_path, self.load,self.file_type)

            #self.model.profile_load_data(self.file_path, self.file_type)
            for step in range(1, 101):  # Example loop to represent progress
             self.signals.progress.emit(step)  # Emit progress update
             time.sleep(0.001) 
            # Emit signals to update GUI safely
            self.signals.data_loaded.emit(data)
            shape_message = f"Data Loaded: {data.shape[0]} rows, {data.shape[1]} columns"

            self.signals.update_status.emit(shape_message)
            if self.model.data_frame is not None:
                columns = self.model.data_frame.columns.tolist()
                

                self.signals.update_combobox.emit(columns)
        except Exception as e:
            self.signals.loading_error.emit(str(e))
   

# Ensure to replace 'YourClass' with the actual name of your class and adjust the method implementations to fit your actual class structure and method names.


class Controller:
    """
    The Controller component in the MVC architecture, responsible for handling user interactions,
    updating the model, and reflecting changes in the view.

    This class creates and manages the connections between the model and the view, ensuring the
    separation of the GUI and the business logic/data handling.
    """


    def load_data(self):
        """
        Opens a file dialog for the user to select a file and loads the data into the model.
        """
        file_dialog = QFileDialog(self.view)
        icon_path = os.path.abspath('images/load_data_icon.svg')
        self.view.setWindowIcon(QIcon(icon_path))

        initial_directory = self.model.working_directory if self.model.working_directory else ""

        file_path, _ = file_dialog.getOpenFileName(self.view, "Open File", initial_directory, "CSV Files (*.csv);;Excel Files (*.xlsx)")
        
        if file_path:
            file_name = os.path.basename(file_path)
            if file_path.endswith('.csv'):
                file_type = 'csv'
            elif file_path.endswith('.xlsx'):
                file_type = 'excel'
            else:
                custom_color = QColor("#B22222")  # OrangeRed color
                message_text = "Unsupported file format"
                window_title = "Error"
                icon_text = "X"
                CustomMessageBox(custom_color, message_text, window_title, icon_text, self.view).exec()
                return
            
            self.view.copy_data_frame = None
            self.view.file_path = file_path
            self.view.train_data = None
            self.view.test_data = None
            self.view.actual_data = self.model.data_frame
            self.view.getValuesthreshold = {}

            # Create and start the data loading thread
            self.thread = DataLoadThread(file_name, file_path, file_type, self.model)
            self.thread.signals.data_loaded.connect(self.view.display_data)
            self.thread.signals.update_status.connect(self.view.update_status_bar)
            self.thread.signals.loading_error.connect(lambda e: CustomMessageBox(QColor("#B22222"), f"Error loading data: {e}", "Loading Error", "X", self.view).exec())
            self.thread.signals.update_combobox.connect(self.update_combobox_items)
            self.thread.start()
            self.thread.signals.progress.connect(self.update_progress_bar)
            self.view.resetLayout()

        icon_path = os.path.abspath('images/bulb_icon.png')
        self.view.setWindowIcon(QIcon(icon_path))
    def update_combobox_items(self, columns):
        self.view.comboBox.clear()
        self.view.comboBox.addItems(columns)
        self.view.comboBox2.clear()
        for column_name in columns:
            is_numeric = self.view.is_column_numeric(column_name)
            self.view.comboBox2.addItem(column_name, is_numeric)
    def __init__(self):
        """
        Initializes the Controller component.

        Creates instances of the Model and the View, and sets up the necessary connections between them.
        """
        self.model = Model()
        self.view = View(self)
        self.loaded_file_path = None  # Initialize loaded_file_path
    def onSubsetGenerated(self):
        self.view.subsetTableButton.setVisible(False)
        self.view.subset_button.setVisible(True)
        self.view.subset_controls_widget.setVisible(True)
        self.view.comboBox2.setVisible(True)
        self.view.label2.setVisible(True)
        self.view.unselect_button.setVisible(True)
        self.view.subsetCreated = False

        #QMessageBox.information(self, "Subset Created", "Your subset has been generated. You can view it using the 'Latest Subset Table' button.")
    

    def save_as(self):
        if self.model.data_frame is None:
            # Display a warning message if no data is loaded
            icon_path = os.path.abspath('images/save_as_icon.svg')
            self.view.setWindowIcon(QIcon(icon_path))
            custom_color = QColor("#B22222")  # OrangeRed color
            message_text = "Please load data first before accessing this feature."  # Example message text
            window_title = "Data Not Loaded"  # Example window title
            icon_text = "X"  # Example icon text
       
            #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
            # Optionally, set a specific icon to indicate the need for action or an error state
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec()  # Use the desired color for the custom icon

            icon_path = os.path.abspath('images/bulb_icon.png')
            self.view.setWindowIcon(QIcon(icon_path))
            return
        icon_path = os.path.abspath('images/save_as_icon.svg')
        self.view.setWindowIcon(QIcon(icon_path))
        try:            
            icon_path = os.path.abspath('images/save_as_icon.svg')
            self.view.setWindowIcon(QIcon(icon_path))

            # Check if data is loaded
            if self.model.data_frame.empty:

                custom_color = QColor("#B22222")  # OrangeRed color
                message_text = "No data to save."  # Example message text
                window_title = "Error"  # Example window title
                icon_text = "X"  # Example icon text
        
                #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
                # Optionally, set a specific icon to indicate the need for action or an error state
                CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec()  # Use the desired color for the custom icon

                    
                icon_path = os.path.abspath('images/bulb_icon.png')
                self.view.setWindowIcon(QIcon(icon_path))
                return

            # Get the loaded file name
            loaded_file_name = Path(self.loaded_file_path).name if self.loaded_file_path else "Untitled"

            # Open a file dialog to get the save path
            file_dialog = QFileDialog()
            selected_file, _ = file_dialog.getSaveFileName(self.view, "Save As", f"TSA_{loaded_file_name}", "CSV Files (*.csv);;All Files (*)")

            # Check if the user canceled the save operation
            if not selected_file:
                icon_path = os.path.abspath('images/bulb_icon.png')
                self.view.setWindowIcon(QIcon(icon_path))    
                return

            # Save data to the selected file
            self.model.data_frame.to_csv(selected_file, index=False)

            # Update the status bar
            self.view.update_status_bar(f"Data saved to {selected_file} successfully.")
            custom_color = QColor("#5cb85c")  # OrangeRed color
            message_text = f"Data saved to {selected_file}" # Example message text
            window_title = "Success"  # Example window title
            icon_text = "✔"  # Example icon text
       
            #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
            # Optionally, set a specific icon to indicate the need for action or an error state
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec()  # Use the desired color for the custom icon

            #QMessageBox.information(self.view, "Success", f"Data saved to {selected_file}")
            icon_path = os.path.abspath('images/bulb_icon.png')
            self.view.setWindowIcon(QIcon(icon_path))
        except Exception as e:
                custom_color = QColor("#B22222")  # OrangeRed color
                message_text =f"Error in save_as: {e}"  # Example message text
                window_title = "Error"  # Example window title
                icon_text = "X"  # Example icon text
        
                #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
                # Optionally, set a specific icon to indicate the need for action or an error state
                CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec()  # Use the desired color for the custom icon

                    
        icon_path = os.path.abspath('images/bulb_icon.png')
        self.view.setWindowIcon(QIcon(icon_path))
    def delete_columns(self, columns):
        """
        Deletes the specified columns from the data frame.
        """
        icon_path = os.path.abspath('images/bulb_icon.png')
        self.view.setWindowIcon(QIcon(icon_path))  
        if self.model.data_frame is not None:
            self.model.data_frame.drop(columns=columns, inplace=True)
            self.view.display_data(self.model.data_frame)
            custom_color = QColor("#5cb85c")  # OrangeRed color
            message_text =  f"Successfully deleted {columns}"# Example message text
            window_title = "Success"  # Example window title
            icon_text = "✔"  # Example icon text
       
            #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
            # Optionally, set a specific icon to indicate the need for action or an error state
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec()  # Use the desired color for the custom icon
        icon_path = os.path.abspath('images/delete_icon.ico')
        self.view.setWindowIcon(QIcon(icon_path))  
    def apply_fill(self, columns, method):
        """
        Applies the specified fill method to the specified columns.
        """
        icon_path = os.path.abspath('images/bulb_icon.png')
        self.view.setWindowIcon(QIcon(icon_path)) 
        if self.model.data_frame is not None:
            if method == "forward":
                self.model.data_frame[columns] = self.model.data_frame[columns].ffill()
            elif method == "backward":
                self.model.data_frame[columns] = self.model.data_frame[columns].bfill()
            # No fill case is handled by simply not modifying the data_frame

            self.view.display_data(self.model.data_frame)
            custom_color = QColor("#5cb85c")  # OrangeRed color
            message_text =  f"Successfully done {method} filled {columns}!"# Example message text
            window_title = "Success"  # Example window title
            icon_text = "✔"  # Example icon text
       
            #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
            # Optionally, set a specific icon to indicate the need for action or an error state
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec()  # Use the desired color for the custom icon
        icon_path = os.path.abspath('images/imputation_icon.ico')
        self.view.setWindowIcon(QIcon(icon_path))   

    def run(self):
        """
        Starts the application by displaying the view.
        """
        self.view.show()

    def set_directory(self):
        """
        Opens a dialog for the user to select a directory and updates the model's working directory.
        """
        icon_path = os.path.abspath('images/set_directory_icon.svg')
        self.view.setWindowIcon(QIcon(icon_path))
        
        directory = QFileDialog.getExistingDirectory(self.view, "Select Directory")
        if directory:  # check if a directory was selected
            try:
                self.model.set_working_directory(directory)
                # Display success message using CustomMessageBox
                custom_color = QColor("#5cb85c")  # ForestGreen color
                message_text = f"Directory '{directory}' set successfully."
                window_title = "Directory Set"
                icon_text = "✔"
                CustomMessageBox(custom_color, message_text, window_title, icon_text, self.view).exec()
            except Exception as e:
                # Display error message in case of failure using CustomMessageBox
                custom_color = QColor("#B22222")  # OrangeRed color
                message_text = f"Error: {str(e)}"
                window_title = "Error"
                icon_text = "X"
                CustomMessageBox(custom_color, message_text, window_title, icon_text, self.view).exec()
                
        icon_path = os.path.abspath('images/bulb_icon.png')
        self.view.setWindowIcon(QIcon(icon_path))

    def change_theme(self):
        """
        Handles the logic to change the application's theme.

        This method is a placeholder and should be implemented to modify the view's appearance according to the selected theme.
        """
        pass
    def get_dataframe(self):
        """
        Returns the current DataFrame loaded in the model.

        This method provides access to the DataFrame for operations that require it,
        such as plotting, data analysis, or further manipulation in the view or other components.

        Returns:
            pandas.DataFrame: The current DataFrame loaded in the model.
        """
        return self.model.data_frame
    def handle_subset_button(self):
     thresholds = {}
     for column, (min_input, max_input) in self.view.thresholds_inputs.items():
        try:
            min_val = float(min_input.text())
            max_val = float(max_input.text())
            thresholds[column] = (min_val, max_val)
        except ValueError:
            # Handle invalid input
            continue
    
     subsets = self.split_into_subsets(self.model.data_frame, thresholds)
    # Now, subsets contain the indices of rows that meet the criteria.
    # You can further process these subsets as needed.
######################################################## trying Functionalities for docked widget#####################################################
    def update_column_names(self):
     if self.model.data_frame is not None:
        columns = self.model.data_frame.columns
        
        # Update comboBox
        self.view.comboBox.clear()
        self.view.comboBox.addItems(columns)
        
        # Clear comboBox2 and add items with checkboxes
        self.view.comboBox2.clear()
        for column_name in columns:
            is_numeric = self.view.is_column_numeric(column_name)
            self.view.comboBox2.addItem(column_name, is_numeric)


    def calculate_nans(self):
     try:
        selected_column = self.view.comboBox.currentText()

        if selected_column in self.model.data_frame.columns:
            # Directly calculate the number of NaN values using pandas functions
            nan_count = self.model.data_frame[selected_column].isna().sum()

            self.view.output_display.setText(
                "====================\n"
                "Number of NaNs\n"
                "====================\n" + str(nan_count)
            )
        else:
            self.view.output_display.setText(f"Column {selected_column} not found in DataFrame.")

     except Exception as e:
        # Handle the exception - print an error message or log it
        self.view.output_display.setText(f"An exception occurred: {e}")

    def calculate_dtype(self):
     try:
        selected_column = self.view.comboBox.currentText()

        if selected_column in self.model.data_frame.columns:
            # Access the data directly from the pandas DataFrame for the selected column
            column_data = self.model.data_frame[selected_column]

            # Update dtype_map with Boolean and datetime64[ns] for DateTime
            dtype_map = {
                'int64': int,
                'float64': float,
                'object': str,  # Assuming 'object' dtype could contain strings, Booleans, or DateTime
                'bool': bool,
                'datetime64[ns]': pd.Timestamp,  # pandas datetime
                # Consider adding 'timedelta[ns]' if your data includes timedelta values
            }

            # Special handling for 'object' dtype which might include mixed types
            if column_data.dtype == 'string':
                if all(isinstance(v, bool) for v in column_data.dropna()):
                    inferred_dtype = bool
                elif pd.api.types.infer_dtype(column_data) == 'datetime':
                    inferred_dtype = pd.Timestamp
                else:
                    inferred_dtype = str  # Default to str for mixed or unidentified object types
            else:
                # Direct mapping for non-object dtypes
                pandas_dtype = column_data.dtype
                inferred_dtype = dtype_map.get(str(pandas_dtype), None)

            if inferred_dtype:
                self.view.output_display.setText(
                    "====================\n"
                    "Data Type\n"
                    "====================\n" + f"{inferred_dtype.__name__}"
                )
            else:
                self.view.output_display.setText(
                    "====================\n"
                    "Data Type\n"
                    "====================\n" + "Unknown or unsupported data type"
                )

        else:
            self.view.output_display.setText(f"Column {selected_column} not found in DataFrame.")

     except Exception as e:
        self.view.output_display.setText(f"An exception occurred: {e}")

    def calculate_statistics(self):
     try:
        selected_column = self.view.comboBox.currentText()

        if selected_column in self.model.data_frame.columns:
            # Directly work with pandas Series for the selected column
            numeric_data = pd.to_numeric(self.model.data_frame[selected_column], errors='coerce').dropna()

            if not numeric_data.empty:
                statistics = {
                    "Count": numeric_data.count(),
                    "Mean": numeric_data.mean(),
                    "Std Dev": numeric_data.std(),
                    "Min": numeric_data.min(),
                    "25th Percentile": numeric_data.quantile(0.25),
                    "Median": numeric_data.median(),
                    "75th Percentile": numeric_data.quantile(0.75),
                    "Max": numeric_data.max(),
                }

                # Format the statistics for display
                formatted_stats = "\n".join([f"{label}: {value:.2f}" for label, value in statistics.items()])

                # Add header with separator lines
                separator = "=" * 30
                display_text = (
                    f"{separator}\n     Descriptive Statistics\n{separator}\n{formatted_stats}\n{separator}"
                )

                self.view.output_display.setText(display_text)
            else:
                self.view.output_display.setText("No numeric data to calculate statistics.")
        else:
            self.view.output_display.setText(f"Column '{selected_column}' not found in DataFrame.")

     except Exception as e:
        self.view.output_display.setText(f"An exception occurred: {e}")
    def calculate_unique(self):
     try:
        selected_column = self.view.comboBox.currentText()

        if selected_column in self.model.data_frame.columns:
            # Directly work with pandas Series for the selected column
            unique_values = self.model.data_frame[selected_column].nunique()

            formatted_output = (
                "====================\n"
                "Unique Values Count\n"
                "====================\n"
                f"{unique_values}"
            )

            self.view.output_display.setText(formatted_output)
        else:
            self.view.output_display.setText(f"Column '{selected_column}' not found in DataFrame.")

     except Exception as e:
        self.view.output_display.setText(f"An exception occurred: {e}")
    def calculate_missing(self):
     try:
        selected_column = self.view.comboBox.currentText()

        if selected_column in self.model.data_frame.columns:
            # Calculate the number of missing values using pandas
            missing_count = self.model.data_frame[selected_column].isna().sum()

            self.view.output_display.setText(
                "====================\n"
                "Number of Missing Values\n"
                "====================\n" + str(missing_count)
            )
        else:
            self.view.output_display.setText(f"Column {selected_column} not found in DataFrame.")
     except Exception as e:
         # Handle the exception - print an error message or log it
        self.view.output_display.setText(f"An exception occurred: {e}")

    def calculate_shape(self):
     try:
        selected_column = self.view.comboBox.currentText()

        if selected_column in self.model.data_frame.columns:
            # The shape of a DataFrame column is the total number of rows in the DataFrame
            row_count = self.model.data_frame.shape[0]

            self.view.output_display.setText(
                "====================\n"
                f"Shape of column: {selected_column}\n"
                "====================\n"
                f"{row_count} Rows"
            )
        else:
            self.view.output_display.setText(f"Column {selected_column} not found in DataFrame.")
     except Exception as e:
        # Handle the exception - print an error message or log it
        self.view.output_display.setText(f"An exception occurred: {e}")



##########################################################################################################
############################### Explore menu #############################################################
    def open_data_info(self):
     try:
        if self.model.data_frame is None:
            icon_path = os.path.abspath('images/data_info_icon.svg')
            self.view.setWindowIcon(QIcon(icon_path))
            custom_color = QColor("#B22222")  # OrangeRed color
            message_text = "Please load data first before accessing this feature."  # Example message text
            window_title = "Data Not Loaded"  # Example window title
            icon_text = "X"  # Example icon text
       
            #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
            # Optionally, set a specific icon to indicate the need for action or an error state
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec()  # Use the desired color for the custom icon

            icon_path = os.path.abspath('images/bulb_icon.png')
            self.view.setWindowIcon(QIcon(icon_path))
            return

        columns = list(self.model.data_frame.columns)
        data_types = []
        missing_values = []

        for column in self.model.data_frame.columns:
            column_data = self.model.data_frame[column]

            # Check if column contains only string values
            is_str = column_data.apply(lambda x: isinstance(x, str)).all()
            if is_str:
                data_types.append('string')
            else:
                # Check data types for other cases
                is_float = column_data.apply(lambda x: isinstance(x, float)).all()
                is_int = column_data.apply(lambda x: isinstance(x, int)).all()
                
                data_type = 'float' if is_float else ('int' if is_int else 'str')
                data_types.append(data_type)

            # Count missing values
            missing_count = column_data.isnull().sum()
            missing_values.append(missing_count)

        data_info = {
            'columns': columns,
            'data_types': data_types,
            'missing_values': missing_values
        }

        # Open the DataInfoDialog and populate it with data_info
        dialog = DataInfoDialog(self)  # Pass the controller instance
        dialog.populate_data_info(data_info)
        dialog.exec()
     except Exception as e:

        custom_color = QColor("#B22222")  # OrangeRed color
        message_text = f"An error occurred: {str(e)}"  # Example message text
        window_title = "Error"  # Example window title
        icon_text = "X"  # Example icon text

        #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
        # Optionally, set a specific icon to indicate the need for action or an error state
        CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec()  # Use the desired color for the custom icon

    def _is_float(self, s):
      try:
        float(s)
        return True
      except ValueError:
        return False

    def _is_int(self, s):
      try:
        int(s)
        return True
      except ValueError:
        return False
 


    def convert_columns_data(self, column_names, new_dtype):
        for col_name in column_names:
            try:
                if new_dtype == 'Float':
                     self.model.data_frame[col_name] = pd.to_numeric(self.model.data_frame[col_name], errors='coerce').astype(float)

                elif new_dtype == 'Integer':
                    self.model.data_frame[col_name] = pd.to_numeric(self.model.data_frame[col_name], errors='coerce')
                    self.model.data_frame[col_name] = self.model.data_frame[col_name].fillna(0).astype(int)
                elif new_dtype == 'Boolean':
                    self.model.data_frame[col_name] = self.model.data_frame[col_name].astype(bool)
                elif new_dtype == 'String':
                    self.model.data_frame[col_name] = self.model.data_frame[col_name].astype(str)
                elif new_dtype == 'Date Time':
                    self.model.data_frame[col_name] = pd.to_datetime(self.model.data_frame[col_name], errors='coerce')
                print(f"Column {col_name} converted to {new_dtype}.")
                self.view.display_data(self.model.data_frame)
                self.update_combobox_items(self.model.data_frame.columns)
            except Exception as e:
                
                custom_color = QColor("#B22222")  # OrangeRed color
                message_text = f"Error converting column {col_name} to {new_dtype}: {e}" # Example message text
                window_title = "Conversion Error"  # Example window title
                icon_text = "X"  # Example icon text

                #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
                # Optionally, set a specific icon to indicate the need for action or an error state
                CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec()  # Use the desired color for the custom icon


        self.refresh_data_view()

        if column_names:
            message = f"Columns {' '.join(column_names)} were successfully converted to {new_dtype}."
            custom_message_box = CustomMessageBox(icon_color=QColor('#5cb85c'),  # Specify the color for the information icon (green color)
                                                message_text=message,
                                                window_title="Successfully Done Conversion",
                                                icon_text='✔',
                                                parent=self.view)  # Assuming self.view is the parent widget
            custom_message_box.exec()

        else:
            custom_color = QColor("#B22222")  # OrangeRed color
            message_text = "No columns were converted." # Example message text
            window_title = "Conversion Error"  # Example window title
            icon_text = "X"  # Example icon text

            #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
            # Optionally, set a specific icon to indicate the need for action or an error state
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec()  # Use the desired color for the custom icon

    def refresh_data_view(self):
        data_info = {
            'columns': self.model.data_frame.columns.tolist(),
            'data_types': [str(dtype) for dtype in self.model.data_frame.dtypes],
            'missing_values': self.model.data_frame.isnull().sum().tolist()
        }
        if hasattr(self.view, 'data_info_dialog'):
            self.view.data_info_dialog.populate_data_info(data_info)
        else:
            print("Data info dialog is not available.")

    # Assuming convert_value is used elsewhere and needs to be part of the class
    def convert_value(self, value, new_dtype):
        try:
            if new_dtype == 'Integer':
                converted = pd.to_numeric(value, errors='coerce')
                return np.int32(0 if np.isnan(converted) else converted)
            elif new_dtype == 'Float':
                converted = pd.to_numeric(value, errors='coerce')
                return float(0.0 if np.isnan(converted) else converted)
            elif new_dtype == 'Date Time':
                date_formats = [
                    "yyyy-MM-dd", "dd-MM-yyyy", "MM-dd-yyyy",
                    "yyyy/MM/dd", "dd/MM/yyyy", "MM/dd/yyyy",
                    "yyyy-MM-dd HH:mm:ss", "dd-MM-yyyy HH:mm:ss", "MM-dd-yyyy HH:mm:ss",
                    "yyyy/MM/dd HH:mm:ss", "dd/MM/yyyy HH:mm:ss", "MM/dd/yyyy HH:mm:ss",
                    "yyyy-MM-dd'T'HH:mm:ssZ", "yyyy-MM-dd'T'HH:mm:ss.SSSZ", "yyyy-MM-dd'T'HH:mm:ss'Z'",
                    "EEEE, MMMM d, yyyy"
                ]
                for format in date_formats:
                    converted_date = QDateTime.fromString(value, format)
                    if converted_date.isValid():
                        return converted_date.toString(format)
                print(f"Invalid date/time format: {value}")
                return value
            elif new_dtype == 'Boolean':
                return bool(value)
            else:
                return value
        except Exception as e:
            custom_color = QColor("#B22222")  # OrangeRed color
            message_text = f"Error during conversion: {e}" # Example message text
            window_title = "Conversion Error"  # Example window title
            icon_text = "X"  # Example icon text

            #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
            # Optionally, set a specific icon to indicate the need for action or an error state
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec()  # Use the desired color for the custom icon

            return value

    def set_index(self):
        """
        Opens a dialog for the user to select a column to set as the index of the DataFrame.
        """
        icon_path = os.path.abspath('images/set_index_icon.svg')
        self.view.setWindowIcon(QIcon(icon_path))

        if self.model.data_frame is not None:
            # Check if there are any datetime columns
            datetime_columns = [col for col in self.model.data_frame.columns if pd.api.types.is_datetime64_any_dtype(self.model.data_frame[col])]
            if not datetime_columns:
                # Display a warning message if no datetime columns are found
                custom_color = QColor("#B22222")  # OrangeRed color
                message_text = "The dataset does not contain any datetime columns. Please go to the Data Info > Data Conversion menu and convert a column to datetime format."
                window_title = "No Datetime Columns"
                icon_text = "!"
                CustomMessageBox(custom_color, message_text, window_title, icon_text, self.view).exec()

                icon_path = os.path.abspath('images/bulb_icon.png')
                self.view.setWindowIcon(QIcon(icon_path))

                return

            # Create and show the SetIndexDialog
            dialog = SetIndexDialog(self.model.data_frame.columns.tolist(), self.view)
            if dialog.exec():
                selected_column = dialog.get_selected_column()
                if selected_column:
                    # Check if the selected column is a datetime column
                    if not pd.api.types.is_datetime64_any_dtype(self.model.data_frame[selected_column]):
                        custom_color = QColor("#B22222")  # OrangeRed color
                        message_text = f"Column '{selected_column}' is not a datetime column. Please select a valid datetime column."
                        window_title = "Invalid Column Type"
                        icon_text = "!"
                        CustomMessageBox(custom_color, message_text, window_title, icon_text, self.view).exec()

                        icon_path = os.path.abspath('images/bulb_icon.png')
                        self.view.setWindowIcon(QIcon(icon_path))

                        return

                    try:
                        # Set the selected column as index and preserve its position
                        self.model.set_index_and_preserve_column(selected_column)
                        # Refresh the display to show changes
                        self.view.display_data(self.model.data_frame)
                        # Display success message using CustomMessageBox
                        custom_color = QColor("#5cb85c")  # ForestGreen color
                        message_text = f"Column '{selected_column}' set as index."
                        window_title = "Index Set"
                        icon_text = "✔"
                        CustomMessageBox(custom_color, message_text, window_title, icon_text, self.view).exec()
                    except Exception as e:
                        # Display error message in case of failure using CustomMessageBox
                        custom_color = QColor("#B22222")  # OrangeRed color
                        message_text = f"Error: {str(e)}"
                        window_title = "Error"
                        icon_text = "X"
                        CustomMessageBox(custom_color, message_text, window_title, icon_text, self.view).exec()
        else:
            # Display an error message if no data is loaded
            custom_color = QColor("#B22222")  # OrangeRed color
            message_text = "Please load data first before accessing this feature."
            window_title = "Data Not Loaded"
            icon_text = "X"
            CustomMessageBox(custom_color, message_text, window_title, icon_text, self.view).exec()

        icon_path = os.path.abspath('images/bulb_icon.png')
        self.view.setWindowIcon(QIcon(icon_path))

    def setup_signals(self):
     self.view.table_widget.itemChanged.connect(self.on_item_changed)

    def on_item_changed(self, item):
    # Get row and column number from the item
     row = item.row()
     column = item.column()
    
     # Get the new value from the item
     new_value = item.text()
    
    # Convert new value to appropriate type, e.g., int, float, etc. as required
    # This step depends on the data type of your DataFrame column
     try:
        new_value = type(self.model.data_frame.iloc[row, column])(new_value)
     except ValueError:
        # Handle the case where conversion fails, e.g., invalid input
        return
    
    # Update the DataFrame
     self.model.data_frame.iloc[row, column] = new_value
    # In controller.py
     # In your controller class
    def check_index_frequency(self):
     freq = self.model.get_index_frequency()
     self.view.show_message("Index Frequency Check", f"The frequency of the DataFrame's index is: {freq}")

    def check_frequency(self):
    
     icon_path = os.path.abspath('images/set_frequency_icon.svg')
     self.view.setWindowIcon(QIcon(icon_path))
     if self.model.data_frame is not None:
        current_freq = self.model.data_frame.index.freq
        freq_str = 'None' if current_freq is None else current_freq.freqstr
        self.view.show_message("Current Frequency", f"The current frequency is: {freq_str}")
     else:
        self.view.show_message("Error", "DataFrame is not loaded or index is not datetime.")
     icon_path = os.path.abspath('images/bulb_icon.png')
     self.view.setWindowIcon(QIcon(icon_path))
    def set_frequency(self):
     icon_path = os.path.abspath('images/set_frequency_icon.svg')
     self.view.setWindowIcon(QIcon(icon_path))
    # Check if data is loaded
     if self.model.data_frame is None:
        custom_color = QColor("#B22222")  # OrangeRed color
        message_text = "Please load data first before accessing this feature."  # Example message text
        window_title = "Data Not Loaded"  # Example window title
        icon_text = "X"  # Example icon text

        #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
        # Optionally, set a specific icon to indicate the need for action or an error state
        CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec()  # Use the desired color for the custom icon
        icon_path = os.path.abspath('images/bulb_icon.png')
        self.view.setWindowIcon(QIcon(icon_path))

        return  # Exit the function early

     dialog = SetFrequencyDialog(self.view)
     if dialog.exec():
        frequency = dialog.get_frequency()
        try:
            # Use asfreq if the data conforms to the frequency
            if frequency.endswith('T'):  # For minute data
                self.model.data_frame = self.model.data_frame.asfreq(frequency)
            else:
                # For non-conforming data, resample without aggregation
                self.model.data_frame = self.model.data_frame.resample(frequency).asfreq()
            self.view.show_message("Frequency Updated", f"Frequency set to: {frequency}")
        except ValueError as e:
            custom_color = QColor("#B22222")  # OrangeRed color
            message_text = str(e) # Example message text
            window_title = "Error"  # Example window title
            icon_text = "X"  # Example icon text

            #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
            # Optionally, set a specific icon to indicate the need for action or an error state
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 
            
     icon_path = os.path.abspath('images/bulb_icon.png')
     self.view.setWindowIcon(QIcon(icon_path))




        
        

#############################################################################################################################
    def open_line_plot_dialog(self):
     icon_path = QPixmap('images/line_plot_icon.svg')
     self.view.setWindowIcon(QIcon(icon_path))

     if self.model.data_frame is not None:
        # Access the lineplotting dialog from the view
        self.view.lineplotting_dialog.populate_columns(self.model.data_frame.columns)
        self.view.lineplotting_dialog.show()
     else:
        custom_color = QColor("#B22222")  # OrangeRed color
        message_text = "Please load data first before accessing this feature."  # Example message text
        window_title = "Data Not Loaded"  # Example window title
        icon_text = "X"  # Example icon text

        #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
        # Optionally, set a specific icon to indicate the need for action or an error state
        CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 
        icon_path = os.path.abspath('images/bulb_icon.png')
        self.view.setWindowIcon(QIcon(icon_path))
    def plot_selected_columns(self, selected_columns):
     if selected_columns:
        valid_columns = [col for col in selected_columns if self.is_numeric_column(col)]
        if valid_columns:
            data_to_plot = self.model.get_data_for_columns(valid_columns)
            self.view.lineplotting_dialog.plot_data(data_to_plot)
        else:
            custom_color = QColor("#B22222")  # OrangeRed color
            message_text = "Selected columns must be of type float or int." # Example message text
            window_title = "Type Error"  # Example window title
            icon_text = "X"  # Example icon text

            #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
            # Optionally, set a specific icon to indicate the need for action or an error state
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 
            
     else:
        custom_color = QColor("#B22222")  # OrangeRed color
        message_text = "No columns selected for plotting."  # Example message text
        window_title = "Warning"  # Example window title
        icon_text = "!"  # Example icon text

        #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
        # Optionally, set a specific icon to indicate the need for action or an error state
        CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 
    def is_numeric_column(self, column_name):
     column_data = self.model.data_frame[column_name]
     return column_data.dtype in ['float64', 'int64']  # Adjust dtype check as needed

##########################################################################################
    """For Decomposition of Series"""           
##########################################################################################            
            
    def open_seasonal_decompose_dialog(self):
        """Opens the Seasonal Decompose Dialog."""
        icon_path = os.path.abspath('images/seasonal_decompose_icon.svg')
        self.view.setWindowIcon(QIcon(icon_path))
        if self.model.data_frame is not None:
            series_list = self.model.data_frame.columns.tolist()
            self.view.seasonal_decompose_dialog.populate_series(series_list)
            self.view.seasonal_decompose_dialog.show()
        else:
            custom_color = QColor("#B22222")  # OrangeRed color
            message_text = "Please load data first before accessing this feature."  # Example message text
            window_title = "Data Not Loaded"  # Example window title
            icon_text = "X"  # Example icon text
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 

        icon_path = os.path.abspath('images/bulb_icon.png')
        self.view.setWindowIcon(QIcon(icon_path))

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
            custom_color = QColor("#B22222")  # OrangeRed color
            message_text = str(e) # Example message text
            window_title = "Error"  # Example window title
            icon_text = "X"  # Example icon text
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 


    """ End of Decomposition"""
            

##########################################################################################
    """For ACF/PACF and Lag Plot"""           
##########################################################################################  

    def open_lag_acf_pacf_dialog(self):
        icon_path = os.path.abspath('images/acf_icon.svg')
        self.view.setWindowIcon(QIcon(icon_path))
        """Opens the window for the lag, acf, and pacf plots."""
        if self.model.data_frame is not None:
            series_list = self.model.data_frame.columns.tolist()
            self.view.lag_acf_pacf_dialog.populate_series(series_list)
            self.view.lag_acf_pacf_dialog.show()
        else:
            custom_color = QColor("#B22222")  # OrangeRed color
            message_text = "Please load data first before accessing this feature."  # Example message text
            window_title = "Data Not Loaded"  # Example window title
            icon_text = "X"  # Example icon text
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 
        icon_path = os.path.abspath('images/bulb_icon.png')
        self.view.setWindowIcon(QIcon(icon_path))

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
            self.view.lag_acf_pacf_dialog.plot_lag(series_data, number_of_lags)
            self.view.lag_acf_pacf_dialog.plot_acf(series_data, number_of_lags)
            self.view.lag_acf_pacf_dialog.plot_pacf(series_data, number_of_lags)
        except Exception as e:
            custom_color = QColor("#B22222")  # OrangeRed color
            message_text = str(e) # Example message text
            window_title = "Error"  # Example window title
            icon_text = "X"  # Example icon text
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 



############################################################################################################
    """The lines of code below are for ADF and KPSS unit root hypothesis testing"""
############################################################################################################

    def open_unit_root_test_dialog(self):

        icon_path = os.path.abspath('images/unit_root.svg')
        self.view.setWindowIcon(QIcon(icon_path))
        if self.model.data_frame is None:
                custom_color = QColor("#B22222")  # OrangeRed color
                message_text = "Please load data first before accessing this feature."  # Example message text
                window_title = "Data Not Loaded"  # Example window title
                icon_text = "X"  # Example icon text
                CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 
 
                icon_path = os.path.abspath('images/bulb_icon.png')
                self.view.setWindowIcon(QIcon(icon_path))
                return

        try:
            self.view.unit_root_test_dialog.populate_columns(self.model.get_column_names())
            self.view.unit_root_test_dialog.show()
        except Exception as e:
            custom_color = QColor("#B22222")  # OrangeRed color
            message_text = str(e) # Example message text
            window_title = "Error"  # Example window title
            icon_text = "X"  # Example icon text
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 

        icon_path = os.path.abspath('images/bulb_icon.png')
        self.view.setWindowIcon(QIcon(icon_path))

    def perform_adf_test(self, column_name):
        result = self.model.perform_adf_test(column_name)
        self.view.unit_root_test_dialog.display_test_result(result)

    def perform_kpss_test(self, column_name):
        result = self.model.perform_kpss_test(column_name)
        self.view.unit_root_test_dialog.display_test_result(result)
    def open_resample_dialog(self):
     icon_path = os.path.abspath('images/resample_icon.ico')
     self.view.setWindowIcon(QIcon(icon_path))
     if self.loaded_file_path:
        dialog = ResampleDialog(self.view)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            if dialog.custom_freq_radio.isChecked():  # Corrected method call with parentheses
                freq = dialog.custom_freq_lineedit.text().strip()
            else:
                freq = dialog.common_freq_combo.currentText()
            if freq:  # Ensure freq is not empty or None
                agg_method = dialog.aggregation_combo.currentText()
                self.resample_data(freq, agg_method)
            else:
                custom_color = QColor("#B22222")  # OrangeRed color
                message_text = "Frequency is not specified."  # Example message text
                window_title = "Input Error"  # Example window title
                icon_text = "X"  # Example icon text
                CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 


        else:
                custom_color = QColor("#B22222")  # OrangeRed color
                message_text = "Operation cancelled by user."  # Example message text
                window_title = "Resampling Cancelled"  # Example window title
                icon_text = "X"  # Example icon text
                CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 


     else:
            custom_color = QColor("#B22222")  # OrangeRed color
            message_text = "Please load data first before accessing this feature."  # Example message text
            window_title = "Data Not Loaded"  # Example window title
            icon_text = "X"  # Example icon text
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 


     icon_path = os.path.abspath('images/bulb_icon.png')
     self.view.setWindowIcon(QIcon(icon_path))
    def resample_data(self, freq, agg_method):
        try:
            icon_path = os.path.abspath('images/resample_icon.ico')
            self.view.setWindowIcon(QIcon(icon_path))
            
            if self.loaded_file_path:
                # Assuming the time column is named 'Time' and is the first column
                self.model.data_frame['Time'] = pd.to_datetime(self.model.data_frame['Time'])
                self.model.data_frame.set_index('Time', inplace=True)
                
                numeric_cols = self.model.data_frame.select_dtypes(include=[np.number]).columns
                
                if agg_method in ['mean', 'max', 'min', 'sum', 'first', 'last']:
                    resampled_df = self.model.data_frame[numeric_cols].resample(freq).agg(agg_method)
                else:
                    resampled_df = self.model.data_frame.resample(freq).agg(agg_method)
                
                resampled_df.reset_index(inplace=True)
                self.view.display_data(resampled_df)
            else:
                custom_color = QColor("#B22222")  # OrangeRed color
                message_text = "Please load data first before accessing this feature."  # Example message text
                window_title = "Data Not Loaded"  # Example window title
                icon_text = "X"  # Example icon text
                CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 

        except Exception as e:
            custom_color = QColor("#B22222")  # OrangeRed color
            message_text = str(e) # Example message text
            window_title = "Resampling Error"  # Example window title
            icon_text = "X"  # Example icon text
            CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 

        finally:
            icon_path = os.path.abspath('images/bulb_icon.png')
            self.view.setWindowIcon(QIcon(icon_path))
    
    def update_progress_bar(self, value):
        self.view.progressBar.setValue(value)
        if value == 100:
            self.view.progressBar.hide()
        else:
            self.view.progressBar.show()
    def save_resampled_data_as_csv(self, freq, agg_method):
        icon_path = os.path.abspath('images/resample_icon.ico')
        self.view.setWindowIcon(QIcon(icon_path))
        if self.model.data_frame is not None and not self.model.data_frame.empty:
            try:
                numeric_only = True if agg_method != 'mean' else None
                resampled_data = self.model.data_frame.resample(freq).agg(agg_method, numeric_only=numeric_only)
                filepath, _ = QFileDialog.getSaveFileName(self.view, "Save File", "", "CSV Files (*.csv)")
                if filepath:
                    resampled_data.to_csv(filepath)
                    custom_color = QColor("#5cb85c")  # OrangeRed color
                    message_text =  "Data saved successfully."# Example message text
                    window_title = "Success"  # Example window title
                    icon_text = "✔"  # Example icon text
            
                    #QMessageBox.warning(self.view, "Data Not Loaded", "Please load data first before accessing this feature.")
                    # Optionally, set a specific icon to indicate the need for action or an error state
                    CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 
              
            except Exception as e:
                custom_color = QColor("#B22222")  # OrangeRed color
                message_text = str(e) # Example message text
                window_title = "Resampling Error"  # Example window title
                icon_text = "X"  # Example icon text
                CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 

        else:
                custom_color = QColor("#B22222")  # OrangeRed color
                message_text = "Please load data first before accessing this feature."  # Example message text
                window_title = "Data Not Loaded"  # Example window title
                icon_text = "X"  # Example icon text
                CustomMessageBox(custom_color,message_text, window_title, icon_text, self.view).exec() 

        icon_path = os.path.abspath('images/bulb_icon.png')
        self.view.setWindowIcon(QIcon(icon_path))