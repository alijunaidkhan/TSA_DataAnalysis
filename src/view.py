# view.py
import time
import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QToolButton, QMenu, \
    QCheckBox, QTableWidget, QTableWidgetItem, QMenuBar, QHBoxLayout, QWidgetAction, QScrollArea, QLabel, QLineEdit, QGridLayout,\
    QStatusBar, QProgressDialog, QDialog, QGroupBox, QGroupBox, QComboBox, QListWidget, QListWidgetItem, QErrorMessage, QTextEdit,\
    QMessageBox, QStylePainter, QStyleOptionComboBox, QStyle, QStyledItemDelegate, QStyleOptionComboBox, QAbstractItemView, QSplitter, QDockWidget


from PyQt6.QtGui import QIcon, QAction, QFont, QPixmap, QColor, QStandardItem, QStandardItemModel, QPalette
from PyQt6.QtCore import Qt, QSize, QThread, pyqtSignal, QEvent, QTimer


class View(QMainWindow):
    """
    The View component in the MVC architecture, responsible for displaying the user interface.
    This class extends QMainWindow and manages the UI components and their layout.
    Args:
        controller (Controller): An instance of the Controller class to handle user interactions.
    """

    def __init__(self, controller):
        """
        Initializes the View component.
        Args:
            controller (Controller): The controller instance for the view to communicate with.
        """
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        """
        Initializes the user interface components of the application.
        """
        self.setWindowTitle("My Application")
        self.setGeometry(100, 100, 800, 600)

        self.create_menus()
        self.create_status_bar()

        # Create the central widget which will hold the main content
        self.central_widget = QWidget(self)
        # Set sky blue background color
        self.central_widget.setStyleSheet("background-color: #87CEEB;")  # Sky blue
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

    def create_menus(self):
        """
        Creates the menu bar and adds menus to it.
        """
        menu_bar = self.menuBar()  # Use the existing menu bar of QMainWindow
        file_menu = menu_bar.addMenu("&File")

        # Actions for the file menu
        file_menu.addAction(QAction("&Set Directory", self,
                            triggered=self.controller.set_directory))
        file_menu.addAction(QAction("&Load Data", self, triggered=self.controller.load_data))
        file_menu.addAction(QAction("&Save As...", self, triggered=self.controller.save_as))
        file_menu.addAction(QAction("&Themes", self, triggered=self.controller.change_theme))
        file_menu.addAction(QAction("E&xit", self, triggered=self.close))

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
            background-color: #B22222; /* FireBrick red background */
            color: white;              /* White text color */
            font-weight: bold;         /* Bold font for the text */
            border: 1px solid #9B1B1B; /* Darker red border */
            padding: 3px;              /* Padding inside the header */
        }
        """
        self.table_widget.horizontalHeader().setStyleSheet(header_style)

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
        central_widget.setStyleSheet("QWidget#centralWidget { background-color: red; }")

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
        comboBox = QComboBox()
        comboBox.setFixedHeight(30)
        button = QPushButton("Refresh")
        button.setFixedHeight(30)
        column_selection_layout.addWidget(label, 0)
        column_selection_layout.addWidget(comboBox, 1)
        column_selection_layout.addWidget(button, 0)

        # Set layout for buttons_widget
        buttons_layout = QGridLayout(buttons_widget)
        button_labels = ["Shape", "Unique", "Type", "Missing", "Statistics", "NaNs"]
        for i in range(6):
            button = QPushButton(button_labels[i])
            row, col = divmod(i, 2)
            buttons_layout.addWidget(button, row, col)

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

    # ... init_ui and other methods ...
