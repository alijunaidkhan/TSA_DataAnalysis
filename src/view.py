# view.py
import time
import sys
import pandas as pd
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QToolButton, QMenu, \
    QCheckBox, QTableWidget, QTableWidgetItem, QMenuBar, QHBoxLayout, QWidgetAction, QScrollArea, QLabel, QLineEdit, QGridLayout,\
    QStatusBar, QProgressDialog, QDialog, QGroupBox, QGroupBox, QComboBox, QListWidget, QListWidgetItem, QErrorMessage, QTextEdit,\
    QMessageBox, QStylePainter, QStyleOptionComboBox, QStyle, QStyledItemDelegate, QStyleOptionComboBox, QAbstractItemView, QSplitter, QDockWidget


from PyQt6.QtGui import QIcon, QAction, QFont, QPixmap, QColor, QStandardItem, QStandardItemModel, QPalette
from PyQt6.QtCore import Qt, QSize, QThread, pyqtSignal, QEvent, QTimer

IMAGE_DIRECTORY = 'images'
def get_image_path(image_name):
    """Helper function to get the full path for the image."""
    return f"{IMAGE_DIRECTORY}/{image_name}"
class View(QMainWindow):
    columnSelected = pyqtSignal(str)
    def show_progress_dialog(self):
        self.progress_dialog = QProgressDialog("Loading Data...", None, 0, 95, self)
        self.progress_dialog.setWindowModality(Qt.WindowModality.WindowModal)
        self.progress_dialog.setCancelButton(None)
        self.progress_dialog.show()

    def hide_progress_dialog(self):
        self.progress_dialog.close()
    
    #columnActionRequested = pyqtSignal(str) # Renamed signal for column-related actions

    """
    The View component in the MVC architecture, responsible for displaying the user interface.
    This class extends QMainWindow and manages the UI components and their layout.
    Args:
        controller (Controller): An instance of the Controller class to handle user interactions.
    """
    def update_column_combobox(self, column_name):
        """
        Updates the combobox with the provided column name.
        """
        self.comboBox.clear()
        self.comboBox.addItem(column_name)

    def __init__(self, controller):
        """
        Initializes the View component.
        Args:
            controller (Controller): The controller instance for the view to communicate with.
        """
        super().__init__()
        self.controller = controller
        self.column_data_array = np.array([])  # Initialize an empty array

        self.init_ui()
        self.selected_column_data = None


    def init_ui(self):
        """
        Initializes the user interface components of the application.
        """
        self.setWindowTitle("Data Insight")
        self.setWindowIcon(QIcon(get_image_path('bulb.png')))
        self.setGeometry(100, 100, 800, 600)


        self.create_menus()
        self.create_status_bar()

        # Create the central widget which will hold the main content
        self.central_widget = QWidget(self)
        # Set sky blue background color
        self.central_widget.setStyleSheet("background-color: #C0C0C0;")  # Sky blue
        self.central_layout = QVBoxLayout(self.central_widget)
        self.central_layout.setContentsMargins(50, 50, 50, 50)  # Set margins
        
        # Create an initially empty QTableWidget
        self.table_widget = QTableWidget()
        # Add the table widget to the central layout
        self.central_layout.addWidget(self.table_widget)

        self.setCentralWidget(self.central_widget)

        self.create_docked_widget()
        # Set global stylesheet for buttons and comboboxes
        self.setStyleSheet("""
            QPushButton {
                background-color: #0078D7; /* Blue background */
                color: white;              /* White text */
                border-radius: 7px;       /* Rounded corners */
                padding: 6px;              /* Padding for text */
                font-weight: bold;         /* Bold font */
            }
            QPushButton:hover {
                background-color: #0056b3; /* Darker blue on hover */
            }
            QComboBox {
                border: 2px solid #0078D7; /* Blue border */
                border-radius: 7px;       /* Rounded corners */
                padding: 3px;              /* Padding inside the combobox */
                color: #0078D7;            /* Blue text */
                background-color: white;   /* White background */
            }
            QComboBox::drop-down {
                border: none;              /* No border for the dropdown button */

        """)
        
       # Create the combobox for column selection





    def emit_column_selected_signal(self, logical_index):
        """
        Emits the custom signal with the selected column name.
        """
        
        header_item = self.table_widget.horizontalHeaderItem(logical_index)
        if header_item:
            selected_column = header_item.text()
            
    def create_menus(self):

        menubar = self.menuBar()  # Use the existing menu bar of QMainWindow
                # File Menu
        file_menu = menubar.addMenu("File")
        select_dir_icon = QIcon(get_image_path('folder.png'))
        select_dir_action = QAction(select_dir_icon, "Select Directory", self)
        select_dir_action.setShortcut("Ctrl+W")
        select_dir_action.triggered.connect(self.controller.set_directory)
        file_menu.addAction(select_dir_action)

        # Import Data Action
        import_icon = QIcon(get_image_path('import.png'))
        import_data_action = QAction(import_icon, "Load Data", self)
        import_data_action.setShortcut("Ctrl+N")
        import_data_action.triggered.connect(self.controller.load_data)
        file_menu.addAction(import_data_action)

        # Save Current Data Action
        save_icon = QIcon(get_image_path('save.png'))
        save_data_action = QAction(save_icon, "Save Current Data", self)
        save_data_action.setShortcut("Ctrl+S")
        save_data_action.triggered.connect(self.controller.save_as)
        file_menu.addAction(save_data_action)

        # Theme Menu
        theme_menu = file_menu.addMenu("Theme")

        # Light Theme Action
        light_theme_action = QAction("Light Theme", self)
        light_theme_action.setIcon(QIcon(get_image_path('light.png')))
        light_theme_action.setShortcut("Ctrl+L")
        light_theme_action.triggered.connect(self.controller.set_light_theme)
        theme_menu.addAction(light_theme_action)

        # Dark Theme Action
        dark_theme_action = QAction("Dark Theme", self)
        dark_theme_action.setIcon(QIcon(get_image_path('dark.png')))
        dark_theme_action.setShortcut("Ctrl+D")
        dark_theme_action.triggered.connect(self.controller.set_dark_theme)
        theme_menu.addAction(dark_theme_action)

        # Exit Action
        exit_icon = QIcon(get_image_path('close.png'))
        exit_action = QAction(exit_icon, "Exit", self)
        exit_action.setShortcut("Alt+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Info Menu
        help_menu = menubar.addMenu("Info")

        # About Software Action
        about_icon = QIcon(get_image_path('info.png'))
        about_action = QAction(about_icon, "About Software", self)
        about_action.triggered.connect(self.show_about_software)
        help_menu.addAction(about_action)

        # Documentation Action
        documentation_icon = QIcon(get_image_path('document.png'))
        documentation_action = QAction(documentation_icon, "Documentation", self)
        documentation_action.triggered.connect(self.show_documentation)
        help_menu.addAction(documentation_action)

        # Used Cases Action
        use_cases_icon = QIcon(get_image_path('cases.png'))
        use_cases_action = QAction(use_cases_icon, "Used Cases", self)
        use_cases_action.triggered.connect(self.show_used_cases)
        help_menu.addAction(use_cases_action)

        # Feedback Action
        feedback_icon = QIcon(get_image_path('feedback.png'))
        feedback_action = QAction(feedback_icon, "Feedback", self)
        feedback_action.triggered.connect(self.show_feedback)
        help_menu.addAction(feedback_action)

        # Updates Action
        updates_icon = QIcon(get_image_path('update.png'))
        updates_action = QAction(updates_icon, "Updates", self)
        updates_action.triggered.connect(self.show_updates)
        help_menu.addAction(updates_action)

    def create_status_bar(self):
        """
        Create the status bar with a custom style.
        """
        status_bar = self.statusBar()
        status_bar.showMessage("Ready")
        status_bar.setStyleSheet("""
            QStatusBar {
                background-color: #B22222;
                color: white;
                border: 1px solid #0053A6;
                border-radius: 10px;
                padding: 2px;
                font-size: 10pt;
            }
        """)
        

    def update_status_bar(self, message):
        """
        Updates the status bar with the provided message.
        """
        self.statusBar().showMessage(message)

    def show_message(self, message):
        """
        Displays a message box with the given message.
        """
        QMessageBox.information(self, "Information", message)

    def display_data(self, data_frame):
        """
        Displays the given DataFrame in a QTableWidget, replacing any existing data.
        Args:
            data_frame (pd.DataFrame): The data to display.
        """
        # Check if the table widget already exists
        if not hasattr(self, 'table_widget'):
            self.table_widget = QTableWidget()
            # Add the table widget to the central layout
            self.central_layout.addWidget(self.table_widget)

        # Clear the table widget and set new row and column counts
        self.table_widget.clear()
        self.table_widget.setRowCount(data_frame.shape[0])
        self.table_widget.setColumnCount(data_frame.shape[1])
        self.table_widget.setHorizontalHeaderLabels(data_frame.columns)

        # Styling the header
        header_style = """
        QHeaderView::section {
            background-color: #9B1B1B; /* FireBrick red background */
            color: white;              /* White text color */
            font-weight: bold;         /* Bold font for the text */
            border: 1px solid #9B1B1B; /* Darker red border */
            padding: 3px;              /* Padding inside the header */
        }
        """
        self.table_widget.horizontalHeader().setStyleSheet(header_style)
        #self.table_widget.verticalHeader().setStyleSheet(header_style)

        # Alternating row colors
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setStyleSheet("""
            QTableWidget {
                alternate-background-color: #e8e8e8; /* Beige for alternating rows */
            }
        """)

        # Populate the table with data
        for row in range(data_frame.shape[0]):
            for col in range(data_frame.shape[1]):
                self.table_widget.setItem(
                    row, col, QTableWidgetItem(str(data_frame.iloc[row, col])))
                   
    def get_row_data(self, data_frame, column_name):
 
      if column_name is None:
        raise ValueError("The 'column_name' parameter must be provided.")

      # Check if the table widget already exists
      if not hasattr(self, 'table_widget'):
        self.table_widget = QTableWidget()
        # Add the table widget to the central layout
        self.central_layout.addWidget(self.table_widget)

    # Clear the table widget and set new row count and column count (for a single column)
        self.table_widget.clear()
        self.table_widget.setRowCount(data_frame.shape[0])
        self.table_widget.setColumnCount(1)  # Displaying only one column

    # Set the header label to the specified column name
        self.table_widget.setHorizontalHeaderLabels([column_name])

    # Styling the header (unchanged from your original code)
        header_style = """
    QHeaderView::section {
        background-color: #9B1B1B; /* FireBrick red background */
        color: white;              /* White text color */
        font-weight: bold;         /* Bold font for the text */
        border: 1px solid #9B1B1B; /* Darker red border */
        padding: 3px;              /* Padding inside the header */
    }
    """
        self.table_widget.horizontalHeader().setStyleSheet(header_style)

    # Alternating row colors (unchanged from your original code)
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setStyleSheet("""
        QTableWidget {
            alternate-background-color: #e8e8e8; /* Beige for alternating rows */
        }
    """)

    # Populate the table with data from the specified column
        column_data = data_frame[column_name]

      for row in range(data_frame.shape[0]):
        self.table_widget.setItem(
            row, 0, QTableWidgetItem(str(column_data.iloc[row])))


    def create_docked_widget(self):
        """
        Creates a docked widget with a red background central widget and three container widgets.
        The 'column_selection_widget' contains a label, a combobox, and a button arranged horizontally.
        The 'buttons_widget' contains a grid of six buttons.
        The 'display_results_widget' contains a QTextEdit for displaying output.
        """
        # Create the docked widget with the specified title
        docked_widget = QDockWidget("Exploratory Data Analysis", self)

        # Create the central widget and layout for the docked widget
        central_widget = QWidget()
        central_widget.setObjectName("centralWidget")
        central_widget.setStyleSheet("QWidget#centralWidget { background-color: #9B1B1B; }")

        central_layout = QVBoxLayout(central_widget)
        central_layout.setSpacing(10)
        central_layout.setContentsMargins(5, 5, 5, 5)

        # Create the container widgets
        column_selection_widget = QWidget(central_widget)
        buttons_widget = QWidget(central_widget)
        display_results_widget = QWidget(central_widget)

        # Set layout for column_selection_widget
        column_selection_layout = QHBoxLayout(column_selection_widget)
        label = QLabel("Header")
        label.setStyleSheet("color: white; font-weight: bold;")
        label.setFixedHeight(30)
        self.comboBox = QComboBox()
        self.comboBox.setFixedHeight(30)
        self.central_layout.addWidget(self.comboBox)

        # Connect the table widget's vertical header click event to the update_column_combobox method
        self.table_widget.horizontalHeader().sectionClicked.connect(self.update_column_combobox)

        refresh_button = QPushButton("Refresh", self)
        refresh_button.clicked.connect(self.controller.refresh_data)

    # Add the refresh button to the layout
        self.central_layout.addWidget(refresh_button)
        refresh_button.setFixedHeight(30)
        column_selection_layout.addWidget(label, 0)
        column_selection_layout.addWidget(self.comboBox, 1)
        column_selection_layout.addWidget(refresh_button, 0)
        # Create the button for calculating and displaying the shape
       
        # Set layout for buttons_widget
        buttons_layout = QGridLayout(buttons_widget)
        button_labels = ["Shape", "Unique", "Type", "Missing", "Statistics", "NaNs"]
        for i in range(6):
             button = QPushButton(button_labels[i])
             row, col = divmod(i, 2)
             buttons_layout.addWidget(button, row, col)
             #button.clicked.connect(lambda _, label=button_labels[i]: self.calculate_shape(label))
      


        # Set layout for display_results_widget
        display_results_layout = QVBoxLayout(display_results_widget)
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        display_results_layout.addWidget(self.output_display)

        # Add the container widgets to the central_layout
        central_layout.addWidget(column_selection_widget, 1)
        central_layout.addWidget(buttons_widget, 2)
        central_layout.addWidget(display_results_widget, 6)

        # Set the central widget as the docked widget's content
        docked_widget.setWidget(central_widget)

        # Add the docked widget to the main window
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, docked_widget)
        self.table_widget.itemClicked.connect(self.update_column_combobox)
 
    
    def update_column_combobox(self, logical_index):
        """
        Updates the combobox with the selected column name.
        """
        column_name = self.table_widget.horizontalHeaderItem(logical_index).text()
        self.comboBox.clear()
        self.comboBox.addItem(column_name)
    



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
   # Additional code and imports would go here
