# view.
dark_stylesheet = """
* {
    background-color: #121212;
    color: #E0E0E0;
    border: 1px solid #333;
    font-family: 'Segoe UI', Arial, sans-serif; /* Use a more readable and elegant font */
    font-size: 9pt; /* Adjust size for better readability */
}

QPushButton {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #505050, stop:1 #383838);
    color: #FFFFFF;
    border-radius: 5px;
    padding: 5px;
    border: 1px solid #555;
}

QPushButton:hover {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #636363, stop:1 #4c4c4c);
}

QPushButton:pressed {
    background-color: #333333;
}

QComboBox {
    background-color: #333333;
    color: #FFFFFF;
    border-radius: 4px;
    padding: 3px;
    border: 1px solid #444444;
}

QComboBox::drop-down {
    background-color: #444444;
}

QComboBox::down-arrow {
    image: url('images/dropdown_arrow_icon.svg');
}

QTableWidget {
    gridline-color: #444;
    border: none;
    selection-background-color: #2a2a2a; /* Highlight color for selected items */
}

QTableWidget::item {
    padding-left: 4px;
    padding-right: 4px;
    gridline-color: #444;
}

QHeaderView::section {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #505050, stop:1 #383838);
    color: #FFFFFF;
    padding: 4px;
    border: 1px solid #444444;
    font-weight: bold; /* Make headers bold */
}

QScrollBar:vertical, QScrollBar:horizontal {
    border: 1px solid #2c2c2c;
    background-color: #2c2c2c;
    width: 15px;
    margin: 15px 3px 15px 3px;
    border-radius: 4px;
}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background-color: #5b5b5b;
    min-height: 30px;
    border-radius: 4px;
}

QScrollBar::add-line:vertical, QScrollBar::add-line:horizontal {
    background: none;
}

QScrollBar::sub-line:vertical, QScrollBar::sub-line:horizontal {
    background: none;
}

QStatusBar {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #505050, stop:1 #383838);
    color: #FFFFFF;
    border-top: 1px solid #444;
}
QTableWidget {
    background-color: #181818;  /* Darker background for the table */
    color: #000000;             /* Lighter text for better readability */
    gridline-color: #333;       /* Darker gridlines for a subtle look */
    border: none;               /* Remove border for a flat design */
    selection-background-color: #2a2a2a; /* Darker highlight color for selected items */
    selection-color: #FFFFFF;   /* White text color for selection for contrast */
}

QTableWidget::item {
    padding: 6px;  /* More padding for a modern look */
    border-color: transparent; /* Avoid cell borders for a cleaner look */
}

QHeaderView::section {
    background-color: #202020;  /* Even darker background for headers */
    color: #E0E0E0;             /* Light text color for headers */
    padding: 6px;               /* More padding for headers */
    border: 1px solid #333;     /* Darker borders for a subtle separation */
    font-weight: bold;          /* Bold font for headers */
    font-size: 10pt;            /* Slightly larger font size for headers */
}

QScrollBar:vertical, QScrollBar:horizontal {
    border: 1px solid #2c2c2c;  /* Matching scrollbar border color */
    background-color: #2c2c2c;  /* Scrollbar background */
    width: 12px;                /* Slimmer scrollbars for a modern look */
    border-radius: 6px;         /* Rounded corners for scrollbars */
}

QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background-color: #555;     /* Darker scrollbar handle */
    min-height: 20px;           /* Minimum size for visibility */
    border-radius: 6px;         /* Rounded scrollbar handle */
}
"""

import datetime
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget,QCheckBox
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from PyQt6.QtCore import Qt, QUrl,pyqtSignal,QDateTime
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from PyQt6.QtGui import QAction, QIcon,QIntValidator  ,QFont,QColor,QPixmap,QStandardItem, QStandardItemModel, QDesktopServices
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QTabWidget, \
    QTableWidget,QMenu, QTableWidgetItem, QHBoxLayout, QLabel, QLineEdit,QFrame,QDateTimeEdit, QGridLayout, QDialog, QGroupBox,\
    QRadioButton, QComboBox,QProgressBar,QFormLayout,QTextEdit,QAbstractItemView, QMessageBox, QButtonGroup, QDockWidget,QSpinBox, QSpacerItem, QSizePolicy
import numpy as np
import pandas as pd
import zipfile
import os
from PyQt6.QtWidgets import QDialog, QFileDialog,QScrollArea,QVBoxLayout, QFormLayout, QLabel, QLineEdit, QDialogButtonBox, QMessageBox, QApplication
import sys
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, InputLayer
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import Callback

from sklearn.metrics import mean_absolute_error, mean_squared_error
import subprocess
import seaborn as sns


os.environ['QT_API'] = 'pyqt6'
matplotlib.use('QtAgg')

from pmdarima import auto_arima
from statsmodels.tsa.seasonal import seasonal_decompose
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pandas.plotting import lag_plot
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class View(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


class View(QMainWindow):
    """
    The View component in the MVC architecture, responsible for displaying the user interface.
    This class extends QMainWindow and manages the UI components and their layout.
    Args:
        controller (Controller): An instance of the Controller class to handle user interactions.
    """
    subsetGenerated = pyqtSignal()
    scrolling = pyqtSignal(int, int)  # Signal to notify controller to load subset of data



    def __init__(self, controller):
        # Inside your View's __init__ method or a specific setup method

        """
        Initializes the View component.
        Args:
            controller (Controller): The controller instance for the view to communicate with.
        """



        super().__init__()
        self.best_params = {}  # Define global variable to store best parameters
        self.model_dataframe = None
        self.file_path = None
        self.df_model=None
        self.selected_column=None
        self.order=None
        self.seasonal_order=None
        self.columnSelector = None
        self.fitted_model=None
        self.subsetCreated = False  # Track whether a subset has been created
        self.savedSubsets = None  # Initialize the data_frame attribute
        self.thresholds_layout = QVBoxLayout()  # Initialize the layout
        self.getValuesthreshold={}
        self.comboBox2 = CheckableComboBox()
        self.controller = controller
        self.latest_subset_display_dialog = None
        self.copied_data_frame=None
        # Assuming this is done in the part of your code where UI components are initialized
        self.current_row = 0
        self.rows_per_page = 1000
        self.generated_subsets = []
        self.copy_data_frame=None
        self.actual_data=self.controller.model.data_frame

        self.train_data=None
        self.test_data=None
        self.validation_data = None

        # Initialize the plotting dialog
    
        self.lineplotting_dialog = PlottingDialog(controller=self.controller)
                # Initialize the seasonal decomposition dialog
        self.seasonal_decompose_dialog = SeasonalDecomposeDialog(controller=self.controller)
        #Initialize the LagAcfPacfDialog dialog
        self.lag_acf_pacf_dialog = LagAcfPacfDialog(controller=self.controller)
        # Inside the View class
        self.unit_root_test_dialog = UnitRootTestDialog(controller=self.controller)
        self.closeEvent = self.close_event

        self.init_ui()
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(700, 100, 200, 20)  # Adjust the size and position as needed
        self.progressBar.setMaximum(100)  # Set the maximum value of progress bar
        self.progressBar.hide()  # Initially hide the progress bar
        self.data_changed = False
        self.checked_columns=None
    def style_index_column(self,table_widget, index_column=0):

     for row in range(self.table_widget.rowCount()):
        item = self.table_widget.item(row, index_column)
        if not item:  # Create the item if it doesn't exist
            item = QTableWidgetItem()
            self.table_widget.setItem(row, index_column, item)

        # Example styling
        item.setBackground(QColor('#FFD700'))  # Gold background
        item.setTextColor(QColor('#000000'))  # Black text
        item.setFont(QFont('Arial', 10, QFont.Weight.Bold))

    def on_cell_changed(self, row, column):
        # Set the flag when a cell is changed
      self.data_changed = True
      return True
    def close_event(self, event):
        if self.data_changed:
            # Ask the user if they want to save changes
            reply = QMessageBox.question(self, 'Save Changes?', 'Do you want to save changes?',
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel)

            if reply == QMessageBox.StandardButton.Yes:
                # Save changes
                self.controller.save_as()
                event.accept()
            elif reply == QMessageBox.StandardButton.No:
                # Discard changes
                event.accept()
            elif reply == QMessageBox.StandardButton.Cancel:
             # Cancel close event
                event.ignore()
            else:
                # Cancel close event
                event.ignore()
        else:
            # No changes, close without asking
            event.accept()

    # ... (your existing methods)
    def set_data_loaded(self, is_loaded):
        """
        Enable or disable menu items based on whether data is loaded or not.
        """
        save_as_action = self.menuBar().findChild(QAction, "&Save As...")
        explore_menu = self.menuBar().findChild(QMenu, "&Explore")

        if save_as_action is not None and explore_menu is not None:
            save_as_action.setEnabled(is_loaded)
            explore_menu.setEnabled(is_loaded)
    def init_ui(self):
        """
        Initializes the user interface components of the application.
        """
        self.set_data_loaded(False)

        #self.update_status_bar(self.controller.)
        self.setWindowTitle("TSA")
        
        icon = QIcon('images/bulb_icon.png')
        self.setWindowIcon(icon) 
        self.setGeometry(100, 100, 800, 600)

        self.create_menus()
        self.create_status_bar()

        # Create the central widget which will hold the main content
        self.central_widget = QWidget(self)
        # Set sky blue background color
        self.central_widget.setStyleSheet("background-color: white;")
        self.central_layout = QVBoxLayout(self.central_widget)
        self.central_layout.setContentsMargins(20, 20, 20, 20)  # Set margins

        # Create a QLabel with an initial message
        self.initial_message_label = QLabel(
            "Welcome! Load data to view it here.", self.central_widget)
        self.initial_message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.initial_message_label.setStyleSheet(
            "font-size: 16px; color: #1b4972;")  # Optional styling
        self.central_layout.addWidget(self.initial_message_label)

        # Create an initially empty QTableWidget
        self.table_widget = QTableWidget()
        self.table_widget.setStyleSheet("background-color: grey;")  # 333333
        self.style_index_column(self.table_widget, index_column=0)  # Style the first column
       # self.setup_scroll_handling()
        image_path = 'images/bulb.png'
        style_sheet = (
         f"border-image: url({image_path}) 0 0 0 0 stretch stretch;"
          "background-position: center;"
          "width: 500px; height: 320px;" 
          )


        self.table_widget.setStyleSheet(style_sheet)
       

        self.central_layout.addWidget(self.table_widget)

        self.setCentralWidget(self.central_widget)
        
        self.create_docked_widget()
        self.subsetGenerated.connect(self.onSubsetGenerated)  # Connect the custom signal to a slot

        # Set global stylesheet for buttons and comboboxes
        self.setStyleSheet("""
            QPushButton {
                background-color: #96b1c2; /* grey background */
                color: white;              /* White text */
                border-radius: 7px;       /* Rounded corners */
                padding: 6px;              /* Padding for text */
                font-weight: bold;         /* Bold font */
            }
            QPushButton:hover {
                background-color: #1b4972; /* Darker blue on hover */
            }
            QComboBox {
                border: 2px solid #edebe3; /* Blue border */
                border-radius: 7px;       /* Rounded corners */
                padding: 3px;              /* Padding inside the combobox */
                color: #0078D7;            /* Blue text */
                background-color: white;   /* White background */
            }
            QComboBox::drop-down {
                border: none;              /* No border for the dropdown button */

        """)

        self.table_widget.cellChanged.connect(self.on_cell_changed)

        
        self.setup_scroll_handling()
        if self.bool_test:
         self.table_widget.itemChanged.connect(self.handle_item_change)
    def bool_test(self):
     if self.data_changed:
        return True
     else: 
       return False
    def set_light_theme(self):
        # Placeholder implementation
        header_style = """
            QHeaderView::section {
                background-color: #B22222;
                color: white;
                font-weight: bold;
                border: 1px solid #B22222;
            }
        """
        self.table_widget.horizontalHeader().setStyleSheet(header_style)
        self.setStyleSheet("""
            QStatusBar {
                background-color: #B22222;
                color: white;
                border: 1px solid #0053A6;
                border-radius: 10px;
                padding: 2px;
                font-size: 10pt;
            }
            QPushButton {
                background-color: #96b1c2; /* grey background */
                color: white;              /* White text */
                border-radius: 7px;       /* Rounded corners */
                padding: 6px;              /* Padding for text */
                font-weight: bold;         /* Bold font */
            }
            QPushButton:hover {
                background-color: #1b4972; /* Darker blue on hover */
            }
            QComboBox {
                border: 2px solid #edebe3; /* Blue border */
                border-radius: 7px;       /* Rounded corners */
                padding: 3px;              /* Padding inside the combobox */
                color: #0078D7;            /* Blue text */
                background-color: white;   /* White background */
            }
            QComboBox::drop-down {
                border: none;              /* No border for the dropdown button */
              QTableWidget {
                alternate-background-color: #e8e8e8; /* Beige for alternating rows */
                color:black;
            }
        QHeaderView::section {
            background-color: #B22222; /* FireBrick red background */
            color: white;              /* White text color */
            font-weight: bold;         /* Bold font for the text */
            border: 1px solid #9B1B1B; /* Darker red border */
            padding: 3px;              /* Padding inside the header */
        }
            QStatusBar {
                background-color: #B22222;
                color: white;
                border: 1px solid #0053A6;
                border-radius: 10px;
                padding: 2px;
                font-size: 10pt;
            }  
        QTableWidget {
                alternate-background-color: #e8e8e8; /* Beige for alternating rows */
            }
        QScrollBar:vertical {
            border: 1px solid #c1c1c1;
            background: #f1f1f1;
            width: 10px;
            margin: 10px 0 10px 0;
            border-radius: 4px;
        }
        QScrollBar:horizontal {
            border: 1px solid #c1c1c1;
            background: #f1f1f1;
            height: 10px;
            margin: 0 10px 0 10px;
            border-radius: 4px;
        }
        QScrollBar::handle:vertical {
            background: #a0a0a0;
            min-height: 30px;
            border-radius: 4px;
        }
        QScrollBar::handle:horizontal {
            background: #a0a0a0;
            min-width: 30px;
            border-radius: 4px;
        }
        QScrollBar::add-line, QScrollBar::sub-line {
            background: none;
        }
        QScrollBar::up-arrow, QScrollBar::down-arrow, QScrollBar::left-arrow, QScrollBar::right-arrow {
            background: none;
        }
        QScrollBar::add-page, QScrollBar::sub-page {
            background: none;
        }            

        """)

    def set_dark_theme(self):
        header_style = """
            QHeaderView::section {
                background-color: #1A1A1A;
                color: white;
                font-weight: bold;
                border: 1px solid #1A1A1A;
                padding: 3px;
            }
        """
        self.table_widget.horizontalHeader().setStyleSheet(header_style)


        # Alternating row colors
        self.table_widget.setAlternatingRowColors(True)

        self.setStyleSheet(dark_stylesheet)
    def openSubsetDialogTable(self):
        if not self.generated_subsets:
            QMessageBox.warning(self, "No Subsets", "No subsets have been generated yet.")
            return
        # print(self.copy_data_frame)
        # print(self.checked_columns)
        # print(self.getValuesthreshold)
        #checked_columns = self.comboBox2.get_checked_items()
        column_ranges =self.checked_columns
          # Get the DataFrame from the controller
        dialog = LatestSubsetDialog(column_ranges, self.copy_data_frame,self.getValuesthreshold, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
           pass

# In your main window or wherever the subset button is defined
    def openSubsetDialog(self):
    # Check if data is loaded in the model
     if not self.comboBox2.get_checked_items():
        # Display a warning message if no columns are selected
        icon_path = os.path.abspath('images/subset_icon.ico')
        self.setWindowIcon(QIcon(icon_path))
        QMessageBox.warning(self, "No Columns Selected", "Please select at least one column before proceeding.")
        icon_path = os.path.abspath('images/bulb_icon.png')
        self.setWindowIcon(QIcon(icon_path))
        return
     if self.controller.model.data_frame is None:
        # Display a warning message if no data is loaded
        icon_path = os.path.abspath('images/subset_icon.ico')
        self.setWindowIcon(QIcon(icon_path))
        QMessageBox.warning(self, "Data Not Loaded", "Please load data first before accessing this feature.")
        # Optionally, set a specific icon to indicate the need for action or an error state
        icon_path = os.path.abspath('images/bulb_icon.png')
        self.setWindowIcon(QIcon(icon_path))
        return
     else:
        # Reset the window icon to the default or relevant icon when data is loaded
 
        
        # Proceed with operations if data is loaded
        checked_columns = self.comboBox2.get_checked_items()
        column_ranges = {}
        for column in checked_columns:
            column_ranges[column] = self.calculate_min_max_for_column(column)
        dataframe = self.controller.model.data_frame  # Get the DataFrame from the controller
        dialog = SubsetDialog(column_ranges, dataframe, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            values = dialog.getValues()
            # Handle the values as needed
         

    def calculate_min_max_for_column(self, column):
     try:
        if hasattr(self.controller.model, 'data_frame'):
            if column in self.controller.model.data_frame.columns:
                column_values = self.controller.model.data_frame[column]

                # Replace missing values with NaN
                column_values = column_values.replace('', np.nan).astype(float)

                # Filter out NaN values and calculate min and max
                valid_values = column_values.dropna()
                if not valid_values.empty:
                    return valid_values.min(), valid_values.max()
                else:
                    print("No numeric values found in the column:", column)
                    return None, None
            else:
                print("Column", column, "not found in the DataFrame.")
                return None, None
        else:
            print("DataFrame attribute is not present.")
            return None, None
     except AttributeError:
        print("Model attribute is not present.")
        return None, None



    def set_data_loaded(self, is_loaded):
        """
        Enable or disable menu items based on whether data is loaded or not.
        """
        save_as_action = self.menuBar().findChild(QAction, "&Save As...")
        explore_menu = self.menuBar().findChild(QMenu, "&Explore")

        if save_as_action is not None and explore_menu is not None:
            save_as_action.setEnabled(is_loaded)

            # Enable or disable all actions inside the Explore menu
            for action in explore_menu.actions():
                action.setEnabled(is_loaded)
    
   
    def handle_item_change(self, item):
        """
        Handles changes made to items in the QTableWidget and updates the corresponding DataFrame cell.
        """
        pass
    def create_menus(self):
        """
        Creates the menu bar and adds menus to it.
        """
        menu_bar = self.menuBar()  # Use the existing menu bar of QMainWindow
            


        # File menu
        file_menu = menu_bar.addMenu("&File")

        # Define Pixmaps for each icon
        set_directory_pixmap = QPixmap('images/set_directory_icon.svg')
        load_data_pixmap = QPixmap('images/load_data_icon.svg')
        save_as_pixmap = QPixmap('images/save_as_icon.svg')
       # change_theme_pixmap = QPixmap('images/change_theme_icon.svg')
        exit_pixmap = QPixmap('images/exit_icon.svg')

        # Actions for the file menu
        set_directory_action = QAction(QIcon(set_directory_pixmap), "&Set Directory", self, triggered=self.controller.set_directory)
        load_data_action = QAction(QIcon(load_data_pixmap), "&Load Data", self, triggered=self.controller.load_data)
        save_as_action = QAction(QIcon(save_as_pixmap), "&Save As...", self, triggered=self.controller.save_as)
       # change_theme_action = QAction(QIcon(change_theme_pixmap), "&Themes", self, triggered=self.controller.change_theme)
        exit_action = QAction(QIcon(exit_pixmap), "&Exit", self, triggered=self.close_event)
# Inside the View class
        save_as_action.setShortcut("Ctrl+S")  # Set a keyboard shortcut if desired

        # Set icons for each action using QPixmap
        set_directory_action.setIcon(QIcon(set_directory_pixmap))
        load_data_action.setIcon(QIcon(load_data_pixmap))
        save_as_action.setIcon(QIcon(save_as_pixmap))
      #  change_theme_action.setIcon(QIcon(change_theme_pixmap))
        exit_action.setIcon(QIcon(exit_pixmap))

        # Add actions to the file menu
        file_menu.addAction(set_directory_action)
        file_menu.addAction(load_data_action)
        file_menu.addAction(save_as_action)

       # file_menu.addAction(change_theme_action)
        change_theme_submenu = file_menu.addMenu(QIcon('images/change_theme_icon.svg'), "&Change Theme")

        change_theme_submenu.icon='change_theme_icon.svg'
        file_menu.addAction(exit_action)

##########################################################################################################
############################### Explore menu #############################################################
        # Create 'Explore' menu

        explore_menu = self.menuBar().addMenu("&Explore")
  # Light Theme action with icon
        light_theme_pixmap = QPixmap('images/light_theme_icon.svg')
        light_theme_icon = QIcon(light_theme_pixmap)
        light_theme_action = QAction(light_theme_icon, "&Light Theme", self)
        light_theme_action.triggered.connect(self.set_light_theme)
        change_theme_submenu.addAction(light_theme_action)

        # Dark Theme action with icon
        dark_theme_pixmap = QPixmap('images/dark_theme_icon.svg')
        dark_theme_icon = QIcon(dark_theme_pixmap)
        dark_theme_action = QAction(dark_theme_icon, "&Dark Theme", self)
        dark_theme_action.triggered.connect(self.set_dark_theme)
        change_theme_submenu.addAction(dark_theme_action)
        # Data Info action
        data_info_pixmap = QPixmap('images/data_info_icon.svg')
        data_info_icon = QIcon(data_info_pixmap)
        data_info_action = QAction(data_info_icon, "&Data Info", self)
        data_info_action.triggered.connect(self.controller.open_data_info)
        explore_menu.addAction(data_info_action)

        # Set Index action
        set_index_pixmap = QPixmap('images/set_index_icon.svg')
        set_index_icon = QIcon(set_index_pixmap)
        set_index_action = QAction(set_index_icon, "&Set Index", self)
        set_index_action.triggered.connect(self.controller.set_index)
        explore_menu.addAction(set_index_action)

        # Set Frequency action
        set_frequency_pixmap = QPixmap('images/set_frequency_icon.svg')
        set_frequency_icon = QIcon(set_frequency_pixmap)
        set_frequency_action = QAction(set_frequency_icon, "&Set Frequency", self)
        set_frequency_action.triggered.connect(self.controller.set_frequency)
        explore_menu.addAction(set_frequency_action)

        # Time Series Plots submenu
        #time_series_plots_menu = explore_menu.addMenu("&Time Series Plots")
        time_series_plots_menu = explore_menu.addMenu(QIcon('images/time_series_plots_icon.svg'), "&Time Series Plots")

        # Line Plot action
        line_plot_pixmap = QPixmap('images/line_plot_icon.svg')
        line_plot_icon = QIcon(line_plot_pixmap)
        line_plot_action = QAction(line_plot_icon, "&Line Plot", self)
        line_plot_action.triggered.connect(self.controller.open_line_plot_dialog)
        time_series_plots_menu.addAction(line_plot_action)

        # Seasonal Decompose action
        seasonal_decompose_pixmap = QPixmap('images/seasonal_decompose_icon.svg')
        seasonal_decompose_icon = QIcon(seasonal_decompose_pixmap)
        seasonal_decompose_action = QAction(seasonal_decompose_icon, "&Seasonal Decomposition", self)
        seasonal_decompose_action.triggered.connect(self.controller.open_seasonal_decompose_dialog)
        time_series_plots_menu.addAction(seasonal_decompose_action)

        # Lag, ACF and PACF action
        lag_acf_pacf_pixmap = QPixmap('images/acf_icon.svg')
        lag_acf_pacf_icon = QIcon(lag_acf_pacf_pixmap)
        lag_acf_pacf_action = QAction(lag_acf_pacf_icon, "&Lag | ACF | PACF", self)
        lag_acf_pacf_action.triggered.connect(self.controller.open_lag_acf_pacf_dialog)
        time_series_plots_menu.addAction(lag_acf_pacf_action)

        # Stationarity Test menu
        #stationarity_menu = explore_menu.addMenu("&Stationarity Test")
        stationarity_menu = explore_menu.addMenu(QIcon('images/stationarity_menu_icon.svg'), "&Stationarity Test")

        # Unit Root Test action
        unit_root_test_pixmap = QPixmap('images/unit_root.svg')
        unit_root_test_icon = QIcon(unit_root_test_pixmap)
        unit_root_test_action = QAction(unit_root_test_icon, "&Unit Root Test", self)
        unit_root_test_action.triggered.connect(self.controller.open_unit_root_test_dialog)
        stationarity_menu.addAction(unit_root_test_action)

        # Connect the load_data_action to enable/disable Explore menu items
        load_data_action.triggered.connect(lambda: self.set_data_loaded(True))
        exit_action.triggered.connect(lambda: self.set_data_loaded(False))


    #  Create Preprocess menu
        preprocess_menu = menu_bar.addMenu("&Preprocess")
    
    # Create Subset action with an icon and add it to the Preprocess menu
        subset_icon = QIcon('images/subset_icon.ico')  # Ensure the icon path is correct
        subset_action = QAction(subset_icon, "&Subset", self)
        subset_action.triggered.connect(self.openSubsetDialog)  # Connect the action to the method
        preprocess_menu.addAction(subset_action)

       # Create Resample action with an icon and add it to the Preprocess menu
        resample_icon = QIcon('images/resample_icon.ico')  # Ensure the icon path is correct
        resample_action = QAction(resample_icon, "&Resample", self)
        resample_action.triggered.connect(self.controller.open_resample_dialog)
        preprocess_menu.addAction(resample_action)
# Create Model menu
               # Create Model menu
        model_menu = self.menuBar().addMenu("&Model")
# Add Split Dataset action with an icon to the Model menu

        # Submenu ARIMA
        arima_submenu = model_menu.addMenu(QIcon('images/arima_icon.svg'), "&ARIMA")
        split_dataset_icon = QIcon('images/split_dataset.ico')  # Update the icon path as necessary
        split_dataset_action = QAction(split_dataset_icon, "&Split Dataset", self)
        split_dataset_action.triggered.connect(self.split_dataset_function)
        arima_submenu.addAction(split_dataset_action)
        # Submenu Grid Search Parameters
        grid_search_action = QAction("&Grid Search", self)
        grid_search_action.setIcon(QIcon('images/grid_search_icon.ico'))  # Replace 'images/grid_search_icon.png' with your icon path
        grid_search_action.triggered.connect(self.grid_search_parameters)
        arima_submenu.addAction(grid_search_action)

        # Submenu Model with Parameters
        model_with_parameters_action = QAction("&Model with Parameters", self)
        model_with_parameters_action.setIcon(QIcon('images/model_parameters_icon.ico'))  # Replace 'images/model_parameters_icon.png' with your icon path
        model_with_parameters_action.triggered.connect(self.model_with_parameters)
        arima_submenu.addAction(model_with_parameters_action)



        # Optionally, add submenu or additional options related to RNN
        rnn_submenu = model_menu.addMenu(QIcon('images/nueral_net.ico'), "&Nueral Network")

        # Add configurations or settings specific to RNN model
        configure_rnn_action = QAction("&Univariate RNN", self)
        configure_rnn_action.setIcon(QIcon('images/configure_icon.ico'))  # Replace with your icon path
        configure_rnn_action.triggered.connect(self.configure_rnn)
        multi_rnn_action = QAction("&Multivariate RNN", self)
        multi_rnn_action.setIcon(QIcon('images/configure_icon.ico'))  # Replace with your icon path
        multi_rnn_action.triggered.connect(self.multi_rnn)
        split_dataset_icon = QIcon('images/split_dataset.ico')  # Update the icon path as necessary
        split_dataset_rnn= QAction(split_dataset_icon, "&Split Dataset", self)
        split_dataset_rnn.triggered.connect(self.split_dataset_rnn)
        rnn_submenu.addAction(split_dataset_rnn)
        rnn_submenu.addAction(configure_rnn_action)
        rnn_submenu.addAction(multi_rnn_action)
       

        # Add Forecast menu
        forecast_menu = menu_bar.addMenu("&Forecast")
        arima_based = QAction("&ARIMA Based", self)
        arima_based.setIcon(QIcon('images/forecast_icon.ico'))  # Replace 'images/facebook_prophet_icon.png' with your icon path
        arima_based.triggered.connect(self.forecast_dialogue)
        forecast_menu.addAction(arima_based)
    def multi_rnn(self):
        if self.controller.model.data_frame is  None:
         icon_path = os.path.abspath('images/configure_icon.ico')
         self.setWindowIcon(QIcon(icon_path))
         QMessageBox.warning(self, "Warning", "Please load a DataFrame first!")
         icon_path = os.path.abspath('images/bulb_icon.png')
         self.setWindowIcon(QIcon(icon_path))
         return
        
        if not isinstance(self.controller.model.data_frame.index, pd.DatetimeIndex):
         icon_path = os.path.abspath('images/configure_icon.ico')
         self.setWindowIcon(QIcon(icon_path))
         QMessageBox.warning(self, "Warning", "The DataFrame index is not set as DateTime. Please set the index as DateTime for accurate splitting.")
         icon_path = os.path.abspath('images/bulb_icon.png')
         self.setWindowIcon(QIcon(icon_path))
         return


        if self.validation_data is None:
            QMessageBox.warning(self, "Data is empty", "Please split the data first to get Train and Validation Data.")
            return
       # rnn_configuration_dialog = MultiRNN(self)
       # rnn_configuration_dialog.show()

    def configure_rnn(self):
        if self.controller.model.data_frame is  None:
         icon_path = os.path.abspath('images/configure_icon.ico')
         self.setWindowIcon(QIcon(icon_path))
         QMessageBox.warning(self, "Warning", "Please load a DataFrame first!")
         icon_path = os.path.abspath('images/bulb_icon.png')
         self.setWindowIcon(QIcon(icon_path))
         return
        
        if not isinstance(self.controller.model.data_frame.index, pd.DatetimeIndex):
         icon_path = os.path.abspath('images/configure_icon.ico')
         self.setWindowIcon(QIcon(icon_path))
         QMessageBox.warning(self, "Warning", "The DataFrame index is not set as DateTime. Please set the index as DateTime for accurate splitting.")
         icon_path = os.path.abspath('images/bulb_icon.png')
         self.setWindowIcon(QIcon(icon_path))
         return


        if self.validation_data is None:
            QMessageBox.warning(self, "Data is empty", "Please split the data first to get Train and Validation Data.")
            return
        rnn_configuration_dialog = ConfigureRNN(self)
        rnn_configuration_dialog.show()

        # Add other actions to forecast_menu if needed

    def forecast_dialogue(self):
        if self.controller.model.data_frame is  None:
         icon_path = os.path.abspath('images/forecast_icon.ico')
         self.setWindowIcon(QIcon(icon_path))
         QMessageBox.warning(self, "Warning", "Please load a DataFrame first!")
         icon_path = os.path.abspath('images/bulb_icon.png')
         self.setWindowIcon(QIcon(icon_path))
         return
        
        if not isinstance(self.controller.model.data_frame.index, pd.DatetimeIndex):
         icon_path = os.path.abspath('images/forecast_icon.ico')
         self.setWindowIcon(QIcon(icon_path))
         QMessageBox.warning(self, "Warning", "The DataFrame index is not set as DateTime. Please set the index as DateTime for accurate splitting.")
         icon_path = os.path.abspath('images/bulb_icon.png')
         self.setWindowIcon(QIcon(icon_path))
         return
        if self.order is None or self.seasonal_order is None:
         icon_path = os.path.abspath('images/forecast_icon.ico')
         self.setWindowIcon(QIcon(icon_path))
         QMessageBox.warning(self, "Warning", "Please perform modeling for future forecasting. Navigate to menu Model > ARIMA > Model with Parameters.")
         icon_path = os.path.abspath('images/bulb_icon.png')
         self.setWindowIcon(QIcon(icon_path))
         return

        dialog = ForecastResult(self)
        dialog.exec() 
    def model_with_parameters(self):
        if self.controller.model.data_frame is  None:
         icon_path = os.path.abspath('images/model_parameters_icon.ico')
         self.setWindowIcon(QIcon(icon_path))
         QMessageBox.warning(self, "Warning", "Please load a DataFrame first!")
         icon_path = os.path.abspath('images/bulb_icon.png')
         self.setWindowIcon(QIcon(icon_path))
         return
        
        if not isinstance(self.controller.model.data_frame.index, pd.DatetimeIndex):
         icon_path = os.path.abspath('images/model_parameters_icon.ico')
         self.setWindowIcon(QIcon(icon_path))
         QMessageBox.warning(self, "Warning", "The DataFrame index is not set as DateTime. Please set the index as DateTime for accurate splitting.")
         icon_path = os.path.abspath('images/bulb_icon.png')
         self.setWindowIcon(QIcon(icon_path))
         return


        dialog = ModelWithParameter(self.controller.model.data_frame,self)
        dialog.exec()  #

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def split_dataset_function(self):
        if self.controller.model.data_frame is None:
            icon_path = os.path.abspath('images/split_dataset.ico')
            self.setWindowIcon(QIcon(icon_path))
            QMessageBox.warning(self, "Warning", "Please load a DataFrame first!")
            icon_path = os.path.abspath('images/bulb_icon.png')
            self.setWindowIcon(QIcon(icon_path))
            return

        if not isinstance(self.controller.model.data_frame.index, pd.DatetimeIndex):
            icon_path = os.path.abspath('images/split_dataset.ico')
            self.setWindowIcon(QIcon(icon_path))
            QMessageBox.warning(self, "Warning", "The DataFrame index is not set as DateTime. Please set the index as DateTime for accurate splitting.")
            icon_path = os.path.abspath('images/bulb_icon.png')
            self.setWindowIcon(QIcon(icon_path))
            return

        dialog = SplitDatasetDialog(self.controller.model.data_frame, self)
        dialog.exec()
    def split_dataset_rnn(self):
        if self.controller.model.data_frame is None:
            icon_path = os.path.abspath('images/split_dataset.ico')
            self.setWindowIcon(QIcon(icon_path))
            QMessageBox.warning(self, "Warning", "Please load a DataFrame first!")
            icon_path = os.path.abspath('images/bulb_icon.png')
            self.setWindowIcon(QIcon(icon_path))
            return

        if not isinstance(self.controller.model.data_frame.index, pd.DatetimeIndex):
            icon_path = os.path.abspath('images/split_dataset.ico')
            self.setWindowIcon(QIcon(icon_path))
            QMessageBox.warning(self, "Warning", "The DataFrame index is not set as DateTime. Please set the index as DateTime for accurate splitting.")
            icon_path = os.path.abspath('images/bulb_icon.png')
            self.setWindowIcon(QIcon(icon_path))
            return

        dialog = SplitDatasetDialogRNN(self.controller.model.data_frame, self)
        dialog.exec()
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

    def show_message(self, title, message):
        """
        Displays a message box with the given message.
        """
        # QMessageBox.information(self, "Information", message)
        QMessageBox.information(self, title, message)
# Assume `self.table_widget` is your QTableWidget and `self.model.data_frame` is your pandas DataFrame
    def display_latest_subset(self):
     if hasattr(self, 'Latest_subset_dialog'):
        self.latest_subset_dialog.close()  # Close previous dialog if open

    # Here, you need to fetch the latest subset DataFrame from wherever you're storing it
     latest_subset_dataframe = ...  # Fetch the latest subset DataFrame

    # Create and display the dialog to show the latest subset
     self.latest_subset_dialog = SubsetDisplayDialog(latest_subset_dataframe)
     self.latest_subset_dialog.exec()

    def display_data(self, data_frame):
     """
    Displays the given DataFrame in a QTableWidget, replacing any existing data.
    Args:
        data_frame (pd.DataFrame): The data to display.
     """

     if not hasattr(self, 'table_widget'):
        self.table_widget = QTableWidget()
        self.central_layout.addWidget(self.table_widget)
     self.table_widget.setUpdatesEnabled(False)  # Disable updates for batch processing
     self.table_widget.clear()
     self.table_widget.setRowCount(min(self.rows_per_page, data_frame.shape[0]))
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

    # Populate table with initial subset of rows
     for row in range(self.current_row, min(self.current_row + self.rows_per_page, data_frame.shape[0])):
        for col in range(data_frame.shape[1]):
            item = QTableWidgetItem(str(data_frame.iloc[row, col]))
            self.table_widget.setItem(row - self.current_row, col, item)

     self.table_widget.setUpdatesEnabled(True)  # Re-enable updates after batch processing
    # Connect signals for scrolling behavior
        # Populate table with initial subset of rows
     self.update_table(data_frame.iloc[:self.rows_per_page])
     self.initial_message_label.hide()
    def setup_scroll_handling(self):
        # Connect signal for vertical scroll bar value change
        self.table_widget.verticalScrollBar().valueChanged.connect(self.scroll_handler)

    def scroll_handler(self, value):
        max_value = self.table_widget.verticalScrollBar().maximum()
        visible_rows = self.table_widget.rowCount()
        total_rows = self.controller.model.data_frame.shape[0]

        if value == max_value and self.current_row + visible_rows < total_rows:
            # Reached the bottom, load next set of rows
            self.current_row += self.rows_per_page
            self.update_table(self.controller.model.data_frame.iloc[self.current_row:self.current_row+self.rows_per_page])
         
        elif value == 0 and self.current_row > 0:
            # Reached the top, load previous set of rows
            self.current_row -= self.rows_per_page
            self.update_table(self.controller.model.data_frame.iloc[self.current_row:self.current_row+self.rows_per_page])
    def update_table(self, data_frame):
     num_rows = min(self.rows_per_page, data_frame.shape[0])
     self.table_widget.setRowCount(num_rows)

     for row in range(num_rows):
        for col in range(data_frame.shape[1]):
            item = QTableWidgetItem(str(data_frame.iloc[row, col]))
            self.table_widget.setItem(row, col, item)

        # Set the row number as the first column
        row_number_item = QTableWidgetItem(str(row + self.current_row + 1))
        self.table_widget.setVerticalHeaderItem(row, row_number_item)

    # Check if there are more rows to load beyond the current subset
     total_rows = self.controller.model.data_frame.shape[0]
     if self.current_row + self.rows_per_page < total_rows:
        # Show a loading animation or "Show More" button here
        # For now, I'll just print a message
        print("Loading more rows...")

    # Check if the user has reached the top or bottom of the currently loaded subset
     if self.current_row == 0:
        # User has reached the top, disable loading more rows in the upward direction
        self.table_widget.verticalScrollBar().setValue(0)
     elif self.current_row + num_rows >= total_rows:
        # User has reached the bottom, load the next 1000 rows
        self.current_row = max(0, total_rows - self.rows_per_page)
        # Scroll to the bottom
        self.table_widget.verticalScrollBar().setValue(self.table_widget.verticalScrollBar().maximum())

    def open_data_info_dialog(self, data_frame_info):
        '''Opens the Data Information dialog window to display DataFrame details.
        Args:data_frame_info (dict): Information about the DataFrame to be displayed.'''

        dialog = DataInfoDialog()
        dialog.refresh_dialog()  # Update the dialog with the latest data

        dialog.populate_data_info(data_frame_info)
        dialog.exec()

    def update_plotting_dialog_columns(self, columns):
        if self.plotting_dialog is not None:
            self.plotting_dialog.update_combobox_items(columns)
  

    def grid_search_parameters(self):
        if self.controller.model.data_frame is  None:
         icon_path = os.path.abspath('images/grid_search_icon.ico')
         self.setWindowIcon(QIcon(icon_path))
         QMessageBox.warning(self, "Warning", "Please load a DataFrame first!")
         icon_path = os.path.abspath('images/bulb_icon.png')
         self.setWindowIcon(QIcon(icon_path))
         return
        
        if not isinstance(self.controller.model.data_frame.index, pd.DatetimeIndex):
         icon_path = os.path.abspath('images/grid_search_icon.ico')
         self.setWindowIcon(QIcon(icon_path))

         QMessageBox.warning(self, "Warning", "The DataFrame index is not set as DateTime. Please set the index as DateTime for accurate splitting.")
            

         icon_path = os.path.abspath('images/bulb_icon.png')
         self.setWindowIcon(QIcon(icon_path))
         return
        dialog = ArimaConfigDialog(self.controller.model.data_frame, self)
        dialog.exec()  # Make sure this is .exec() to display the dialog window
    
    def update_column_combobox(self, logical_index):
     if self.controller.model.data_frame is None:
        return

     column_name = self.controller.model.data_frame.columns[logical_index]
     self.comboBox.clear()
     self.comboBox.addItem(column_name)


     # Clear previous items from comboBox2
    
##################################################################################################################
    def is_column_numeric(self, column_name):
     try:
        if column_name and hasattr(self.controller.model, 'data_frame'):
            if column_name in self.controller.model.data_frame.columns:
                column_data = self.controller.model.data_frame[column_name]
                # Check if all values in the column are numeric
                if column_data.apply(lambda x: isinstance(x, (int, float))).all():
                    return True
     except Exception as e:
        print("An error occurred:", e)
     return False


    def onItemCheckStateChanged(self, item_text, is_checked):
    # Handle UI update here
     if is_checked:
        print(f"Show input fields for {item_text}")
        # Logic to show min/max input fields for item_text
     else:
        print(f"Hide input fields for {item_text}")
        # Logic to hide min/max input fields for item_text

    def create_docked_widget(self):
        """
        Creates a docked widget with a red background central widget and three container widgets.
        The 'column_selection_wshapeidget' contains a label, a combobox, and a button arranged horizontally.
        The 'buttons_widget' contains a grid of six buttons.
        The 'results_widget' contains a QTextEdit for displaying output.
        """

        docked_widget = QDockWidget("Property", self)
        central_widget = QWidget()
        central_widget.setObjectName("centralWidget")
        central_widget.setStyleSheet("QWidget#centralWidget { background-color: #B22222; }")
        central_layout = QVBoxLayout(central_widget)

      # Create and setup the column_selection_widget
        column_selection_widget = QWidget(central_widget)
        column_selection_widget.setStyleSheet("QWidget { border: 1px solid white; margin: 3px; padding: 3px; }")
        column_selection_layout = QVBoxLayout(column_selection_widget)

# First row layout for label, combobox, and refresh button
        first_row_layout = QHBoxLayout()
        label = QLabel("Header", column_selection_widget)
        label.setStyleSheet("color: white; font-weight: bold;")
        label.setFixedHeight(30)

        self.comboBox = QComboBox(column_selection_widget)
        self.comboBox.setObjectName("columnComboBox")
        self.comboBox.setFixedHeight(30)
        self.table_widget.horizontalHeader().sectionClicked.connect(self.update_column_combobox)

        refresh_button = QPushButton("Refresh", column_selection_widget)
        refresh_button.setObjectName("refreshButton")
        refresh_button.setToolTip("Refresh the data and update column names.")
        refresh_button.setFixedHeight(30)
  
        first_row_layout.addWidget(label, 1)
        self.subsetTableButton = QPushButton("Latest Subset Table", column_selection_widget)
        self.subsetTableButton.setObjectName("subsetTableButton")
        self.subsetTableButton.setToolTip("View generated subset table.")
        self.subsetTableButton.setFixedHeight(30)
        self.subsetTableButton.clicked.connect(self.openSubsetDialogTable)

        self.subsetTableButton.setVisible(False)  # Initially hidden
        first_row_layout.addWidget(self.comboBox, 5)
        first_row_layout.addWidget(refresh_button, 2)

# Second row layout for the second ComboBox and its label


# Add first and second row layouts to the column_selection_layout
        column_selection_layout.addLayout(first_row_layout)
        #column_selection_layout.addLayout(second_row_layout)
       # Add checkboxes and input fields for thresholds
       # Iterate over the columns of comboBox2 and add checkboxes and input fields for numerical columns
       # Add checkboxes and input fields for each numerical column in comboBox2


        # Create and setup the buttons_widget
        buttons_widget = QWidget(central_widget)
        buttons_widget.setStyleSheet("QWidget { border: 1px solid white; margin: 3px; padding: 3px; }")#setStyleSheet("QWidget { border: 2px solid black; margin: 5px; padding: 5px; }")
        buttons_layout = QGridLayout(buttons_widget)
        self.buttons = {}
        button_info = {
    "Size": "Calculate the size of the data.",
   
    "Type": "Calculate data types of columns.",
    "Missing": "Calculate the number of missing values.",
    "Statistics": "Calculate basic statistics of the data.",
   
}

        button_labels = ["Size", "Type", "Missing", "Statistics"]


#self.buttons[label].clicked.connect(getattr(self.controller, f"calculate_{label.lower()}"))
        for i, label in enumerate(button_labels):
            button = QPushButton(label, buttons_widget)
            button.setObjectName(f"{label.lower()}Button")
            self.buttons[label] = button
            self.buttons[label].setToolTip(button_info[label])
            row, col = divmod(i, 2)
            buttons_layout.addWidget(button, row, col)
       # buttons_layout.addWidget(self.subsetTableButton)
                # Subset controls setup
        subset_controls_layout = QHBoxLayout()
        self.label2 = QLabel("Subsets", buttons_widget)
        self.label2.setStyleSheet("color: white; font-weight: bold;")
        self.label2.setFixedHeight(30)

        self.comboBox2 = CheckableComboBox()
        self.comboBox2.setObjectName("columnComboBox2")
        self.comboBox2.setFixedHeight(30)

        self.unselect_button = QPushButton("Clear", column_selection_widget)
        self.unselect_button.setObjectName("unselectButton")
        self.unselect_button.setToolTip("Unselect all columns.")
        self.unselect_button.setFixedHeight(30)
        self.unselect_button.clicked.connect(self.comboBox2.unselect_all)

        subset_controls_layout.addWidget(self.label2,1)
        subset_controls_layout.addWidget(self.comboBox2,4)
        subset_controls_layout.addWidget(self.unselect_button,2)

        # Instead of buttons_layout.addLayout(subset_controls_layout)
        self.subset_controls_widget = QWidget()
        self.subset_controls_widget.setLayout(subset_controls_layout)
        buttons_layout.addWidget(self.subset_controls_widget, 2, 0, 1, -1)  # Span across all columns

        self.subset_button = QPushButton("Subset",buttons_widget)
        self.subset_button.setObjectName("subsetButton")
        self.subset_button.setFixedHeight(30)
       
# Add a stretch to push the button to the center
        buttons_layout.addWidget(self.subset_button, len(button_labels) // 2 + 2, 0, 1, 2)
        buttons_layout.addWidget(self.subsetTableButton, len(button_labels) // 2 + 3, 0, 1, 2)  # Change the row index
        buttons_layout.setVerticalSpacing(1)  # Set vertical spacing only once
        buttons_widget.setLayout(buttons_layout)
        central_layout.addWidget(buttons_widget,3)
        #$buttons_layout.addWidget(second_row_layout)
        # Create and setup the display_results_widget
        display_results_widget = QWidget(central_widget)
        display_results_layout = QVBoxLayout(display_results_widget)
        self.output_display = QTextEdit(display_results_widget)
        self.output_display.setReadOnly(True)
        display_results_layout.addWidget(self.output_display)

        # Add the container widgets to the central_layout
        central_layout.addWidget(column_selection_widget, 1)
        central_layout.addWidget(buttons_widget, 4)
        central_layout.addWidget(display_results_widget, 5)

        # Set the central widget as the docked widget's content
        docked_widget.setWidget(central_widget)

        # Add the docked widget to the main window
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, docked_widget)

######################################################## trying Functionalities for docked widget#####################################################
        refresh_button.clicked.connect(self.controller.update_column_names)
        self.subset_button.clicked.connect(self.openSubsetDialog)

        self.buttons["Size"].clicked.connect(self.controller.calculate_shape)
        # Connect the "Type" button
        self.buttons["Type"].clicked.connect(self.controller.calculate_dtype)
        # Connect the "Statistics" button
        self.buttons["Statistics"].clicked.connect(self.controller.calculate_statistics)
        # Connecting the 'Unique' button
      #  self.buttons["Unique"].clicked.connect(self.controller.calculate_unique)
        # Connect the "Missing"
        self.buttons["Missing"].clicked.connect(self.controller.calculate_missing)
        # Connect the"NaNs" buttons
       # self.buttons["NaNs"].clicked.connect(self.controller.calculate_nans)
# Function to update column widgets based on selected column

# In View class
    def viewSubsetTable(self):
     if self.savedSubsets is not None:

        # For simplicity, we assume savedSubsets is a list of DataFrames. Adapt as necessary.
        dialog = SubsetDisplayDialog(self.savedSubsets, self)  # Display the first subset for this example
        dialog.exec()
     else:
        QMessageBox.information(self, "Subset", "No subsets have been generated.")

    def onSubsetGenerated(self):
        self.copied_data_frame = self.controller.model.data_frame.copy()

        self.subsetTableButton.setVisible(True)
        # self.subset_button.setVisible(False)
        # self.subset_controls_widget.setVisible(False)
        # self.comboBox2.setVisible(False)
        # self.label2.setVisible(False)
        # self.unselect_button.setVisible(False)
        # self.subsetCreated = True
        QMessageBox.information(self, "Subset Created", "Your subset has been generated. You can view it using the 'Latest Subset Table' button.")
        
    def resetLayout(self):
    # Reset visibility of widgets
     self.subsetTableButton.setVisible(False)
    #  self.subset_button.setVisible(True)
    #  self.subset_controls_widget.setVisible(True)
    #  self.comboBox2.setVisible(True)
    #  self.label2.setVisible(True)
    #  self.unselect_button.setVisible(True)
    #  self.subsetCreated = False

###########################################################################################################################################
""" The lines below are specifically creating the UI elemnents for the Explore Menu: starting with DataInfo dialog, Setindex dialog """

###########################################################################################################################################

# No.1 DataInfo dialog
    

class DataInfoDialog(QDialog):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowTitle("Data Information")
        icon = QIcon('images/data_info_icon.svg')
        self.setWindowIcon(icon) 
        self.setGeometry(300, 300, 600, 400)  # Adjust size and position as needed

        # Create the tab widget
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.tabs.addTab(self.tab1, "DataFrame Info")
        self.tabs.addTab(self.tab2, "Data Conversion")

        # Layout for the dialog
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)
        # Setup Tab 1 (DataFrame Info)
        self.setup_tab1()

        # Setup Tab 2 (Data Conversion)
        self.setup_tab2()

        # Add buttons at the bottom
        self.add_buttons()

    def setup_tab1(self):
        layout = QVBoxLayout()
        self.table_widget = QTableWidget()
  
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(['Column', 'DataType', 'Missing Values'])

        # Styling the table header and rows
        header_style = """
        QHeaderView::section {
            background-color: #4a69bd; /* Blue background for headers */
            color: white;              /* White text color */
            font-weight: bold;         /* Bold font for the text */
            border: none;              /* No border */
            padding: 4px;              /* Padding inside the header */
        }"""
        self.table_widget.horizontalHeader().setStyleSheet(header_style)

        # Zebra stripes in the table rows
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setStyleSheet("""
        QTableWidget {
            alternate-background-color: #f1f1f1; /* Light grey for alternating rows */
            background-color: white;             /* White for other rows */
        }
        QTableWidget::item {
            padding: 4px;                        /* Padding for table cells */
        }""")

        layout.addWidget(self.table_widget)
        self.tab1.setLayout(layout)

    def setup_tab2(self):
        layout = QVBoxLayout()

        # GroupBox for Column Selection with a CheckableComboBox
        column_group = QGroupBox("Select Column(s)")
        column_layout = QVBoxLayout()
        self.column_combo = CheckableComboBox()  # A custom CheckableComboBox
        column_layout.addWidget(QLabel("Columns:"))
        column_layout.addWidget(self.column_combo)
        column_group.setLayout(column_layout)
        
        # GroupBox for Data Type Selection
        datatype_group = QGroupBox("Choose New Data Type")
        datatype_layout = QVBoxLayout()
        self.datatype_combo = QComboBox()
        datatypes = ['Choose Data Type...', 'Date Time', 'Float', 'Integer', 'Boolean', 'String']
        self.datatype_combo.addItems(datatypes)
        self.datatype_combo.model().item(0).setEnabled(False)
        datatype_layout.addWidget(self.datatype_combo)
        datatype_group.setLayout(datatype_layout)

        # Convert Button
        convert_button = QPushButton("Convert")
        convert_button.clicked.connect(self.initiate_conversion)
        

        # Adding widgets to the layout
        layout.addWidget(column_group)
        layout.addWidget(datatype_group)
        layout.addWidget(convert_button)
        self.tab2.setLayout(layout)

    def initiate_conversion(self):
        selected_columns = self.column_combo.get_checked_items()
        new_dtype = self.datatype_combo.currentText()
        if new_dtype != 'Choose Data Type...' and selected_columns:
            self.controller.convert_columns_data(selected_columns, new_dtype)
            self.refresh_data_info_tab()  # Refresh data info tab after conversion

        else:
            QMessageBox.warning(self, "Warning", "Please select columns and a data type.")

    def add_buttons(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: #96b1c2; /* grey background */
                color: white;              /* White text */
                border-radius: 7px;       /* Rounded corners */
                padding: 6px;              /* Padding for text */
                font-weight: bold;         /* Bold font */
            }
            QPushButton:hover {
                background-color: #1b4972; /* Darker blue on hover */
            }""")
        # Buttons for dialog actions
        button_layout = QHBoxLayout()

        self.confirm_exit_button = QPushButton("Confirm and Exit", self)
        self.confirm_exit_button.clicked.connect(self.confirm_and_exit)
        self.confirm_button = QPushButton("Confirm", self)
        self.confirm_button.clicked.connect(self.confirm)
        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(self.confirm_exit_button)
        button_layout.addWidget(self.confirm_button)
        button_layout.addWidget(self.cancel_button)

        self.layout().addLayout(button_layout)

    def refresh_data_info_tab(self):
        # Refresh the table with updated DataFrame info
        data_info = {
            'columns': self.controller.model.data_frame.columns.tolist(),
            'data_types': [str(dtype) for dtype in self.controller.model.data_frame.dtypes],
            'missing_values': self.controller.model.data_frame.isnull().sum().tolist()
        }
        
        self.populate_data_info(data_info)
        # Display a message box

    def confirm(self):
        # Display a message box for confirmation
        QMessageBox.information(self, "Confirm", "Changes have been confirmed.")
        self.refresh_data_info_tab()
    def showEvent(self, event):
        super(DataInfoDialog, self).showEvent(event)
        self.refresh_data_info_tab()

    def confirm_and_exit(self):
        QMessageBox.information(self, "Confirm and Exit", "Changes confirmed. Exiting now.")
        self.refresh_data_info_tab()  # Refresh the DataFrame info tab
        self.accept()  # Closes the dialog

    def populate_data_info(self, data_info):
        self.table_widget.clearContents()  # Clear existing contents
        self.table_widget.setRowCount(0)   # Reset the row count
        self.table_widget.setRowCount(len(data_info['columns']))  # Set new row count
    # The rest of the code for populating data remains the same

        self.table_widget.setColumnCount(3)
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
        self.table_widget.setHorizontalHeaderLabels(['Column', 'DataType', 'Missing Values'])
        self.table_widget.setRowCount(len(data_info['columns']))

        for row, column_name in enumerate(data_info['columns']):
            self.table_widget.setItem(row, 0, QTableWidgetItem(column_name))
            self.table_widget.setItem(row, 1, QTableWidgetItem(data_info['data_types'][row]))
            self.table_widget.setItem(row, 2, QTableWidgetItem(
                str(data_info['missing_values'][row])))
       # New code to populate the checkable combobox
        self.column_combo.clear()
        for column in data_info['columns']:
            column_data = self.controller.model.data_frame[column]
            self.column_combo.addItem(column,True,column_data.dtype) 
           # self.refresh_data_info_tab()  # Refresh data info tab after conversion

        self.column_combo.check_first_item_only()
       # Refresh the DataFrame info tab


class CheckableComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.view().pressed.connect(self.handleItemPressed)
        self.setModel(QStandardItemModel(self))

    def check_first_item_only(self):
        """Ensure only the first item is checked by default."""
        for index in range(self.model().rowCount()):
            item = self.model().item(index)
            if index == 0:
                item.setCheckState(Qt.CheckState.Checked)  # Check the first item
            else:
                item.setCheckState(Qt.CheckState.Unchecked)  # Uncheck all other items
    def addItem(self, text, is_numeric, dtype=None):
  
     if dtype is not None:
        item_text = f"{text} [{dtype}]"  # Concatenate column name and dtype
     else:
        item_text = f"{text}"  # Use only the column name
     item = QStandardItem(item_text)
     if is_numeric:
        item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
        # Set numeric items to be checked by default
        item.setData(Qt.CheckState.Checked, Qt.ItemDataRole.CheckStateRole)
     else:
        # Non-numeric columns are not user-checkable but are still enabled.
        item.setFlags(Qt.ItemFlag.ItemIsEnabled)
        item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)  # Ensure consistent data role
     self.model().appendRow(item)

    def unselect_all(self):
        for index in range(self.model().rowCount()):
            item = self.model().item(index)
            if item.flags() & Qt.ItemFlag.ItemIsUserCheckable:
                item.setCheckState(Qt.CheckState.Unchecked)

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        # Ensure action only for items that are user-checkable (numeric columns)
        if item.flags() & Qt.ItemFlag.ItemIsUserCheckable:
            newState = Qt.CheckState.Unchecked if item.checkState() == Qt.CheckState.Checked else Qt.CheckState.Checked
            item.setCheckState(newState)
            # print(f"Item pressed: {item.text()}, new state: {newState}")  # Debug print

    def checkedItems(self):
        checked_items = []
        for i in range(self.model().rowCount()):
            item = self.model().item(i)
            if item.flags() & Qt.ItemFlag.ItemIsUserCheckable and item.checkState() == Qt.CheckState.Checked:
                checked_items.append(item.text())
        return checked_items
    def get_checked_items(self):
        checked_items = []
        for index in range(self.model().rowCount()):
            item = self.model().item(index)
            if item.flags() & Qt.ItemFlag.ItemIsUserCheckable and item.checkState() == Qt.CheckState.Checked:
                # If the text contains '[', split to extract only the column name
                if '[' in item.text():
                    column_name = item.text().split(' [')[0]
                else:
                    column_name = item.text()  # Otherwise, use the whole text as the column name
                checked_items.append(column_name)
        return checked_items

class SetIndexDialog(QDialog):
    def __init__(self, columns, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Set Index")
        icon = QIcon('images/set_index_icon.svg')
        self.setWindowIcon(icon) 
        self.setGeometry(300, 300, 400, 150)

        # Main layout
        layout = QVBoxLayout()

        # Create a combo box for column selection
        self.column_combo = QComboBox()
        self.column_combo.addItems(columns)

        # Label
        label = QLabel("Select a column to set as index")

        # Buttons
        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)

        # Layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        # Adding widgets to the main layout
        layout.addWidget(label)
        layout.addWidget(self.column_combo)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def get_selected_column(self):
        return self.column_combo.currentText()

# No.3 Set frequency for the index


class SetFrequencyDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Set Frequency")
        icon = QIcon('images/set_frequency_icon.svg')
        self.setWindowIcon(icon) 
        self.setMinimumSize(500, 250)  # Adjust the size as needed
        layout = QVBoxLayout(self)

        self.check_freq_button = QPushButton("Check Current Frequency")
        self.check_freq_button.clicked.connect(self.on_check_frequency)
        layout.addWidget(self.check_freq_button)

        # Radio buttons to select frequency type
        self.common_freq_radio = QRadioButton("Common Frequency")
        self.custom_freq_radio = QRadioButton("Custom Frequency")
        self.help_button = QPushButton()
        help_icon_path = 'images/help_icon.svg'  # Replace 'path/to/your/help_icon.svg' with the actual path
       #self.help_button = QPushButton()
        #help_icon_path = 'path/to/your/help_icon.svg'  # Replace 'path/to/your/help_icon.svg' with the actual path
        help_icon = QIcon(QPixmap(help_icon_path).scaledToHeight(30))
        self.help_button.setIcon(help_icon)
        self.help_button.setToolTip("Help")
        self.help_button.clicked.connect(self.open_pandas_docs)
        # Load the SVG file and set its color
          # ComboBox for aggregation methods
        # self.aggregation_combo = QComboBox()
        # aggregation_methods = ['mean', 'sum', 'std', 'mode', 'max', 'min', 'count']
        # self.aggregation_combo.addItems(aggregation_methods)
        # self.aggregation_combo.insertItem(0, "Select Aggregation Method", None)
        # self.aggregation_combo.setCurrentIndex(0)

        #layout.addWidget(self.help_button)

        # Combo box for common frequency options
        self.common_freq_combo = QComboBox()
        common_frequencies = ["B", "C", "D", "W", "M", "SM",
                              "BM", "CBM", "MS", "SMS", "BMS", "CBMS", "Q"]
        self.common_freq_combo.addItems(common_frequencies)

        # Line edit for custom frequency
        self.custom_freq_lineedit = QLineEdit()
        self.custom_freq_lineedit.setPlaceholderText(
            "Enter custom frequency (e.g., '15T' for 15 minutes)")
       
        # Add radio buttons and combo box to the layout
        layout.addWidget(self.common_freq_radio)
        layout.addWidget(self.common_freq_combo)
        layout.addWidget(self.custom_freq_radio)
        layout.addWidget(self.custom_freq_lineedit)
        # layout.addWidget(QLabel("Aggregation Method:"))
        # layout.addWidget(self.aggregation_combo)
        # Set the default state and connect signals
        self.common_freq_radio.setChecked(True)
        self.common_freq_combo.setEnabled(True)
        self.custom_freq_lineedit.setEnabled(False)
        self.common_freq_radio.toggled.connect(self.toggle_freq_input)
        self.custom_freq_radio.toggled.connect(self.toggle_freq_input)

        # Buttons at the bottom
        buttons_layout = QHBoxLayout()



        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.confirm_frequency)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        

        # Add buttons to the layout with equal spacing
      
        buttons_layout.addWidget(self.confirm_button)
        buttons_layout.addWidget(self.cancel_button)
        buttons_layout.addWidget(self.help_button)

        # Add buttons layout to the main layout
        self.layout().addLayout(buttons_layout)

    def toggle_freq_input(self):
        # Enable or disable inputs based on the selected radio button
        is_common_freq = self.common_freq_radio.isChecked()
        self.common_freq_combo.setEnabled(is_common_freq)
        self.custom_freq_lineedit.setEnabled(not is_common_freq)

    def open_pandas_docs(self):
        # Open the pandas documentation in the user's default web browser
        QDesktopServices.openUrl(
            QUrl("https://pandas.pydata.org/docs/user_guide/timeseries.html#offset-aliases"))

    def confirm_frequency(self):
        if self.common_freq_radio.isChecked():
            frequency = self.common_freq_combo.currentText()
        else:
            frequency = self.custom_freq_lineedit.text()

        
        
        QMessageBox.information(self, "Frequency Set", f"Frequency set to: {frequency}")
        self.accept()
    # def get_aggregation(self):
    #     """
    #     Retrieves the aggregation method set in the dialog.

    #     Returns:
    #         callable: The aggregation function.
    #     """
    #     aggregation = self.aggregation_combo.currentText()
    #     if aggregation == 'mode':
    #         # For 'mode', you need a custom function because pandas' mode method returns a DataFrame
    #         return lambda x: x.mode().iloc[0] if not x.empty else None
    #     return aggregation
    def get_frequency(self):
        """
        Retrieves the frequency set in the dialog.

        Returns:
            str: The frequency string.
        """
        if self.common_freq_radio.isChecked():
            return self.common_freq_combo.currentText()
        else:
            return self.custom_freq_lineedit.text()
    def on_check_frequency(self):
        # This method will be called when the 'Check Current Frequency' button is clicked
        self.parent().controller.check_frequency()  # 
#####################################################################################################################################


class MultiSelectComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.view().pressed.connect(self.handleItemPressed)
        self.setModel(QStandardItemModel(self))

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == Qt.CheckState.Checked:
            item.setCheckState(Qt.CheckState.Unchecked)
        else:
            item.setCheckState(Qt.CheckState.Checked)

    def addItem(self, text):
        item = QStandardItem(text)
        item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
        item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
        self.model().appendRow(item)

    def get_checked_items(self):
        checked_items = []
        for index in range(self.model().rowCount()):
            item = self.model().item(index)
            if item.checkState() == Qt.CheckState.Checked:
                checked_items.append(item.text())
        return checked_items


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=10, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class PlottingDialog(QMainWindow):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.setWindowTitle("Line Plot")
        icon = QIcon('images/line_plot_icon.svg')
        self.setWindowIcon(icon) 
        self.setGeometry(100, 100, 1000, 800)  

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Instruction label
        self.instruction_label = QLabel(
            "select one or multiple series for the line plot")
        main_layout.addWidget(self.instruction_label)

        # Create a horizontal layout for the combobox and plot button
        selection_layout = QHBoxLayout()

        # Multi-select combobox for selecting columns
        self.column_selector = MultiSelectComboBox()
        self.column_selector.setFixedHeight(30)  # Set the fixed height for the combobox
        selection_layout.addWidget(self.column_selector)

        # Plot button
        self.plot_button = QPushButton("Plot")
        self.plot_button.setFixedHeight(30)  # Set the fixed height for the button
        selection_layout.addWidget(self.plot_button)
        self.plot_button.clicked.connect(self.on_plot_button_clicked)

        # Add the selection layout to the main layout
        main_layout.addLayout(selection_layout)

        # Canvas for plotting, increase proportion of space it takes
        self.canvas = MplCanvas(self, width=12, height=6, dpi=100)
        # The second parameter '1' gives it a higher stretch factor
        main_layout.addWidget(self.canvas, 1)

        # Navigation toolbar for the canvas
        self.toolbar = NavigationToolbar(self.canvas, self)
        main_layout.addWidget(self.toolbar)  # Add the toolbar to the layout

    def populate_columns(self, columns):
        """Populate the combobox with column names."""
        self.column_selector.clear()
        for column in columns:
            self.column_selector.addItem(column)

    def get_selected_columns(self):
        """Return the list of selected columns."""
        return self.column_selector.get_checked_items()

    def on_plot_button_clicked(self):
        """Handle the plot button click event."""
        selected_columns = self.get_selected_columns()
        if not selected_columns:
            QMessageBox.warning(self, "Warning", "Please select at least one column to plot.")
        else:
            # Call the method on the controller
            self.controller.plot_selected_columns(selected_columns)

    def plot_data(self, data):
        """Plot the data on the canvas."""
        self.canvas.axes.clear()
        for column in data:
            self.canvas.axes.plot(data[column], label=column)
        self.canvas.axes.figure.tight_layout()  # Adjust layout to fit
        self.canvas.axes.legend()
        self.canvas.draw()

    def update_combobox_items(self, items):
        """Updates the items in the combobox."""
        self.column_selector.clear()  # Clear any existing items
        for item in items:
            self.column_selector.addItem(item)  

           

######################################################### 
""" Decomposition plot funtionalities below"""
#########################################################

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

class SeasonalDecomposeDialog(QMainWindow):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.setWindowTitle("Seasonal Decomposition")
        icon = QIcon('images/seasonal_decompose_icon.svg')
        self.setWindowIcon(icon) 
        self.setGeometry(100, 100, 1000, 800)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Parameters layout for series, period, and model
        parameters_layout = QHBoxLayout()

        # Series selection combobox and label
        self.series_label = QLabel("Select Series:")
        self.series_combobox = QComboBox()
        self.series_combobox.setFixedHeight(30)
        parameters_layout.addWidget(self.series_label)
        parameters_layout.addWidget(self.series_combobox,2)

        # Period selection spinbox and label
        self.period_label = QLabel("Period:")
        self.period_spin_box = QSpinBox()
        self.period_spin_box.setFixedHeight(30)
        self.period_spin_box.setMinimum(1)
        self.period_spin_box.setMaximum(365)
        self.help_button = QPushButton()
        self.help_button.setToolTip("Help")

        help_icon = QPixmap('images/help_icon.svg')  # Replace 'path/to/your/help_icon.png' with the actual path
        self.help_button.setIcon(QIcon(help_icon))
        self.help_button.clicked.connect(self.open_pandas_docs)
        self.help_button.setFixedHeight(30)
        self.help_button.setMinimumWidth(100)  # Set minimum width for the button
        # Future implementation: self.help_button.clicked.connect(self.on_help_clicked)
       
        parameters_layout.addWidget(self.period_label)
        parameters_layout.addWidget(self.period_spin_box,1)

        # Model selection radio buttons and label
        self.model_label = QLabel("Model:")
        self.additive_radio = QRadioButton("Additive")
        self.multiplicative_radio = QRadioButton("Multiplicative")
        self.additive_radio.setChecked(True)
        self.model_group = QButtonGroup()
        self.model_group.addButton(self.additive_radio)
        self.model_group.addButton(self.multiplicative_radio)
        parameters_layout.addWidget(self.model_label)
        parameters_layout.addWidget(self.additive_radio,1)
        parameters_layout.addWidget(self.multiplicative_radio,1)
        parameters_layout.addWidget(self.help_button)

        # Add parameters layout to the main layout
        main_layout.addLayout(parameters_layout)


        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch(1)  # Add stretch to push buttons to the middle
        
       

        # Create a horizontal spacer item that will go between the buttons
        spacer_item = QSpacerItem(200, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        buttons_layout.addSpacerItem(spacer_item)

        self.decompose_button = QPushButton("Decompose")
        self.decompose_button.setFixedHeight(30)
        self.decompose_button.setMinimumWidth(100)  # Set minimum width for the button
        self.decompose_button.clicked.connect(self.on_decompose_clicked)
        buttons_layout.addWidget(self.decompose_button)

        buttons_layout.addStretch(1)  # Add stretch to push buttons to the middle
        main_layout.addLayout(buttons_layout)

        # Canvas for plotting
        self.canvas = MplCanvas(self, width=12, height=8, dpi=100)
        main_layout.addWidget(self.canvas)

        # Navigation toolbar for the canvas
        self.toolbar = NavigationToolbar(self.canvas, self)
        main_layout.addWidget(self.toolbar)

        # Set the main layout stretch factors to give more space to the canvas
        main_layout.setStretchFactor(self.canvas, 3)

    def open_pandas_docs(self):
        # Open the pandas documentation in the user's default web browser
        QDesktopServices.openUrl(
            QUrl("https://pandas.pydata.org/docs/user_guide/timeseries.html#offset-aliases"))
    
    def populate_series(self, series_list):
        """Populate the combobox with series names."""
        self.series_combobox.clear()
        for series in series_list:
            self.series_combobox.addItem(series)

    def on_decompose_clicked(self):
        """Handle the decompose button click event."""
        selected_series = self.series_combobox.currentText()
        if not selected_series:
            QMessageBox.warning(self, "Warning", "Please select a series to decompose.")
            return

        period = self.period_spin_box.value()
        model_type = 'additive' if self.additive_radio.isChecked() else 'multiplicative'

        # Call the controller's method to perform decomposition.
        if self.controller:
            self.controller.perform_seasonal_decomposition(selected_series, period, model_type)



    def plot_decomposition(self, decomposition_result):
        """Plot the decomposition result on the canvas."""
        self.canvas.figure.clf()  # Clear the figure to create a fresh plot area

        # Create subplots
        ax_observed = self.canvas.figure.add_subplot(411)
        ax_trend = self.canvas.figure.add_subplot(412)
        ax_seasonal = self.canvas.figure.add_subplot(413)
        ax_resid = self.canvas.figure.add_subplot(414)

        # Plot the components
        ax_observed.plot(decomposition_result.observed)
        ax_observed.set_ylabel('Observed')

        ax_trend.plot(decomposition_result.trend)
        ax_trend.set_ylabel('Trend')

        ax_seasonal.plot(decomposition_result.seasonal)
        ax_seasonal.set_ylabel('Seasonal')

        ax_resid.plot(decomposition_result.resid)
        ax_resid.set_ylabel('Residual')

        # Adjust layout
        self.canvas.figure.tight_layout()
        self.canvas.draw()
#################################################################
"""End of Decomposition plot"""


#################################################################
"""Lag, ACF, PACF plots starts here"""
#################################################################
from PyQt6.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QComboBox, QSpinBox, QPushButton)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pandas.plotting import lag_plot

class LagAcfPacfDialog(QMainWindow):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Lag, ACF, and PACF Analysis")
        icon = QIcon('images/acf_icon.svg')
        self.setWindowIcon(icon) 
        self.setGeometry(100, 100, 800, 600)
        
        # Main layout
        main_layout = QVBoxLayout()
        
        # Parameters layout
        parameters_layout = self.create_parameters_layout()
        main_layout.addLayout(parameters_layout)
        
        # Matplotlib canvas
        self.canvas = FigureCanvasQTAgg(Figure(figsize=(10, 8)))
        self.add_plots_to_canvas()
        main_layout.addWidget(self.canvas)
        
        # Matplotlib navigation toolbar
        self.toolbar = NavigationToolbar(self.canvas, self)
        main_layout.addWidget(self.toolbar)
        
        # Set the layout to the central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        

    def create_parameters_layout(self):
        parameters_layout = QHBoxLayout()
        self.series_combobox = QComboBox()
        parameters_layout.addWidget(QLabel("Select Series:"))
        parameters_layout.addWidget(self.series_combobox)
        self.lags_spin_box = QSpinBox()
        self.lags_spin_box.setRange(1, 100)  # Assuming 100 is a sensible maximum
        parameters_layout.addWidget(QLabel("Number of Lags:"))
        parameters_layout.addWidget(self.lags_spin_box)
        plot_button = QPushButton("Plot")
        plot_button.clicked.connect(self.on_plot_button_clicked)
        parameters_layout.addWidget(plot_button)
        return parameters_layout

    def add_plots_to_canvas(self):
        grid_spec = self.canvas.figure.add_gridspec(2, 2)
        self.lag_axes = self.canvas.figure.add_subplot(grid_spec[0, :])  # Span all columns
        self.acf_axes = self.canvas.figure.add_subplot(grid_spec[1, 0])
        self.pacf_axes = self.canvas.figure.add_subplot(grid_spec[1, 1])

    def on_plot_button_clicked(self):
        series_name = self.series_combobox.currentText()
        number_of_lags = self.lags_spin_box.value()
        self.controller.perform_lag_acf_pacf_analysis(series_name, number_of_lags)

    # Plotting methods are called by the controller
 
    def plot_lag(self, series, lag=1):
        """
        Plots a lag plot of the specified series with the given lag.

        Args:
            series (pd.Series): The series to plot.
            lag (int): The lag interval. Defaults to 1 if not specified.
        """
        self.lag_axes.clear()
        lag_plot(series, lag=lag, ax=self.lag_axes)  # Pass the user-defined lag here
        self.lag_axes.set_title(f'Lag Plot (Lag = {lag})')
        self.canvas.draw_idle()
    def plot_acf(self, series, lags):
        self.acf_axes.clear()
        plot_acf(series, lags=lags, ax=self.acf_axes)
        self.acf_axes.set_title('Autocorrelation Function (ACF)')
        self.canvas.draw_idle()

    def plot_pacf(self, series, lags):
        self.pacf_axes.clear()
        plot_pacf(series, lags=lags, ax=self.pacf_axes)
        self.pacf_axes.set_title('Partial Autocorrelation Function (PACF)')
        self.canvas.draw_idle()

    def clear_plots(self):
        """Clears all the plots from the canvas."""
        self.lag_axes.clear()
        self.acf_axes.clear()
        self.pacf_axes.clear()
        self.canvas.draw_idle()

    def populate_series(self, series_list):
        """Populates the combobox with a list of series names."""
        self.series_combobox.clear()
        self.series_combobox.addItems(series_list)

    def update_status_bar(self, message):
        """Updates the status bar with a message."""
        self.statusBar().showMessage(message)



# ##################################################################################################
# """The code below is for unit root test: ADF and KPSS"""
# ##################################################################################################
# class ADFTestDialog(QMainWindow):
#     def __init__(self, controller, parent=None):
#         super().__init__(parent)
#         print("Initializing ADF Test Dialog")  # Debug print
#         self.controller = controller
#         self.init_ui()

#     def init_ui(self):
#         self.setWindowTitle("ADF Test")
#         icon = QIcon('images/adf_icon.png')  # Replace with your ADF icon
#         self.setWindowIcon(icon)
#         self.setGeometry(100, 100, 600, 400)  # Adjust size and position as needed

#         # Main layout
#         main_layout = QVBoxLayout()

#         # Parameters layout
#         parameters_layout = self.create_parameters_layout()
#         main_layout.addLayout(parameters_layout)

#         # TextEdit to display results
#         self.results_text_edit = QTextEdit(self)
#         self.results_text_edit.setReadOnly(True)  # Make the text edit read-only
#         main_layout.addWidget(self.results_text_edit)

#         # Set the layout to the central widget
#         central_widget = QWidget()
#         central_widget.setLayout(main_layout)
#         self.setCentralWidget(central_widget)

#     def create_parameters_layout(self):
#         parameters_layout = QHBoxLayout()
#         self.column_combobox = QComboBox()
#         parameters_layout.addWidget(QLabel("Select Column:"))
#         parameters_layout.addWidget(self.column_combobox)
#         adf_test_button = QPushButton("Perform ADF Test")
#         adf_test_button.clicked.connect(self.on_adf_test_button_clicked)
#         parameters_layout.addWidget(adf_test_button)
#         return parameters_layout

#     def on_adf_test_button_clicked(self):
#         column_name = self.column_combobox.currentText()
#         self.controller.perform_adf_test(column_name)

#     def populate_columns(self, column_list):
#         """Populates the combobox with a list of column names."""
#         self.column_combobox.clear()
#         self.column_combobox.addItems(column_list)

#     def display_adf_result(self, result):
#         """Displays the ADF test result in the QTextEdit."""
#         self.results_text_edit.setText(result)

#     def update_status_bar(self, message):
#         """Updates the status bar with a message."""
#         self.statusBar().showMessage(message)

# ##################################################################################################
# """The code below is for unit root test: ADF and KPSS"""
# ##################################################################################################
class UnitRootTestDialog(QMainWindow):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.init_ui()
    def open_pandas_docs(self):
        # Open the pandas documentation in the user's default web browser
        QDesktopServices.openUrl(
            QUrl("https://pandas.pydata.org/docs/user_guide/timeseries.html#offset-aliases"))

    def init_ui(self):
        self.setWindowTitle("Unit Root Test")
        icon = QIcon('images/unit_root.svg')  # Update with a suitable icon
        self.setWindowIcon(icon)
        self.setFixedSize(600, 400)


        # Main vertical layout
        main_layout = QVBoxLayout()

        # Top parameters layout
        top_layout = self.create_parameters_layout()
        main_layout.addLayout(top_layout)
       
        # TextEdit for results
        self.results_text_edit = QTextEdit(self)
        self.results_text_edit.setReadOnly(True)
        main_layout.addWidget(self.results_text_edit)
    
        # Bottom buttons layout
        bottom_layout = QHBoxLayout()
        
        test_button = QPushButton("Test")
        test_button.setFixedHeight(30)
        test_button.clicked.connect(self.on_test_button_clicked)
        ok_button = QPushButton("OK")
        ok_button.setFixedHeight(30)
        ok_button.clicked.connect(self.close)  # Assuming you want 'OK' to close the dialog
       
        bottom_layout.addWidget(test_button)
        bottom_layout.addWidget(ok_button)
        
        # Add bottom_layout to main_layout
        main_layout.addLayout(bottom_layout)

        # Central widget setup
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def create_parameters_layout(self):
        parameters_layout = QHBoxLayout()
        help_button = QPushButton()
        help_button.setToolTip("Help")

        help_icon = QPixmap('images/help_icon.svg')  # Replace 'path/to/your/help_icon.png' with the actual path
        help_button.setIcon(QIcon(help_icon))
        help_button.clicked.connect(self.open_pandas_docs)
        help_button.setFixedHeight(30)

        # Column selection label
        label_select_column = QLabel("Select Column:")
        parameters_layout.addWidget(label_select_column)

        # Column selection combobox
        self.column_combobox = QComboBox()
        self.column_combobox.setFixedHeight(30)
        parameters_layout.addWidget(self.column_combobox)
        parameters_layout.setStretchFactor(self.column_combobox, 2)  # Give more stretch to combobox
     
        # Test type selection label
        label_select_test = QLabel("Select Test:")
        parameters_layout.addWidget(label_select_test)

        # Test type selection combobox
        self.test_type_combobox = QComboBox()
        self.test_type_combobox.addItems(["ADF Test", "KPSS Test"])
        self.test_type_combobox.setFixedHeight(30)
        parameters_layout.addWidget(self.test_type_combobox)
        parameters_layout.setStretchFactor(self.test_type_combobox, 2)  # Give more stretch to combobox
        parameters_layout.addWidget(help_button)
        return parameters_layout


    def on_test_button_clicked(self):
        column_name = self.column_combobox.currentText()
        test_type = self.test_type_combobox.currentText()
        if test_type == "ADF Test":
            self.controller.perform_adf_test(column_name)
        elif test_type == "KPSS Test":
            self.controller.perform_kpss_test(column_name)


    def populate_columns(self, column_list):
        self.column_combobox.clear()
        self.column_combobox.addItems(column_list)

    def display_test_result(self, result):
        self.results_text_edit.setText(result)

    def update_status_bar(self, message):
        self.statusBar().showMessage(message)



class ResampleDialog(QDialog):
    def __init__(self, parent=None):
        super(ResampleDialog, self).__init__(parent)
        self.setWindowTitle("Resample Data")
        self.setWindowIcon(QIcon('images/resample_icon.ico'))  # Adjust icon path as necessary
        self.setMinimumSize(500, 350)  # Adjusted size to accommodate new controls

        layout = QVBoxLayout(self)

        # Frequency selection
        self.common_freq_radio = QRadioButton("Common Frequency")
        self.custom_freq_radio = QRadioButton("Custom Frequency")
        self.common_freq_radio.setChecked(True)

        self.common_freq_combo = QComboBox()
        self.common_freq_combo.addItems(["1h", "2h", "5h", "10h", "1d", "1w"])



        self.custom_freq_lineedit = QLineEdit()
        self.custom_freq_lineedit.setPlaceholderText("Enter custom frequency (e.g., '15T')")
        self.custom_freq_lineedit.setEnabled(False)

        # Aggregation method selection
        self.aggregation_label = QLabel("Aggregation Method:")
        self.aggregation_combo = QComboBox()
        self.aggregation_combo.addItems(["mean", "sum", "max", "min", "median", "first", "last"])
        
        # Help Button
        self.help_button = QPushButton("Help")
        self.help_button.clicked.connect(self.open_help)

        # Confirm and Cancel buttons
        self.confirm_button = QPushButton("Confirm")
        self.cancel_button = QPushButton("Cancel")
        self.confirm_button.clicked.connect(self.on_confirm)
        self.cancel_button.clicked.connect(self.on_cancel)

        # Layout setup
        layout.addWidget(self.common_freq_radio)
        layout.addWidget(self.common_freq_combo)
        layout.addWidget(self.custom_freq_radio)
        layout.addWidget(self.custom_freq_lineedit)
        layout.addWidget(self.aggregation_label)
        layout.addWidget(self.aggregation_combo)
        layout.addWidget(self.help_button)
        self.error_message = QLabel('')
        layout.addWidget(self.error_message)
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.confirm_button)
        buttons_layout.addWidget(self.cancel_button)
        layout.addLayout(buttons_layout)

        # Signals
        self.common_freq_radio.toggled.connect(self.on_toggle_frequency_type)

    def on_toggle_frequency_type(self, checked):
        self.common_freq_combo.setEnabled(checked)
        self.custom_freq_lineedit.setEnabled(not checked)

    def open_help(self):
        QDesktopServices.openUrl(QUrl("https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects"))

    def get_frequency(self):
        if self.common_freq_radio.isChecked():
            return self.common_freq_combo.currentText()
        else:
            return self.custom_freq_lineedit.text()

    def get_aggregation_method(self):
        return self.aggregation_combo.currentText().lower()

    def on_confirm(self):
     if( self.common_freq_radio.isChecked):
      freq = self.common_freq_combo.currentText()
     else:
      freq = self.custom_freq_lineedit.text().strip()
     if not freq:
        self.error_message.setText("Please enter a valid frequency.")
        return
    
    # Validate the aggregation method selection
     agg_method = self.aggregation_combo.currentText()
    
        # Show a confirmation dialog before proceeding
     reply = QMessageBox.question(self, 'Confirm Resample',
                                     "Resampling will modify the current data. Do you want to continue?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

     if reply == QMessageBox.StandardButton.Yes:
            # User confirmed the action, proceed with resampling
            # This is where you might call a resampling method or emit a signal
            print("Proceed with resampling")  # Placeholder for actual resampling logic
            self.accept()  # Close the dialog if the user confirms
     else:
            # User canceled the action
            self.error_message.setText("Resampling cancelled by the user.")
            # Optionally, keep the dialog open for further adjustments by the user
            # self.reject()  # Use this if you want to close the dialog on cancel

    def on_cancel(self):
        # Close the dialog when the 'Cancel' button is clicked
        self.reject()  # Use reject to signal cancellation


# SubsetDisplayDialog implementation
class SubsetDisplayDialog(QDialog):
    def __init__(self, subsetDataFrame, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.tableWidget = QTableWidget()
        self.parent().savedSubsets = self.tableWidget # Assume subsets is a list of DataFrame objects or similar

        self.setWindowTitle("Subsets Latest Table")
        icon = QIcon('images/subset_icon.ico')
        self.setWindowIcon(icon)
        self.setGeometry(100, 100, 400, 300)
        self.populateTable(subsetDataFrame)
        self.layout.addWidget(self.tableWidget)

    def populateTable(self, df):
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns.tolist())
        for i, row in df.iterrows():
            for j, val in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

class SubsetDialog(QDialog):
    def __init__(self, column_ranges, dataframe, parent=None):
        super().__init__(parent)
        self.column_ranges = column_ranges  # Dictionary with column names as keys and (min, max) tuples as values
        self.setWindowTitle("Subsets - Define Column Ranges")
        icon = QIcon('images/subset_icon.ico')
        self.setWindowIcon(icon)
        self.setGeometry(100, 100, 400, 300)
        self.dataframe = dataframe  # The pandas DataFrame
        self.parent().copy_data_frame=self.dataframe

        self.initUI()
        
    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.formLayout = QFormLayout()
        self.inputs = {}

        for column, (min_val, max_val) in self.column_ranges.items():
            min_input = QLineEdit(str(min_val))
            max_input = QLineEdit(str(max_val))
            self.inputs[column] = (min_input, max_input)
            self.formLayout.addRow(QLabel(f"{column} (Min)"), min_input)
            self.formLayout.addRow(QLabel(f"{column} (Max)"), max_input)

        self.layout.addLayout(self.formLayout)
         
        # Create individual buttons
        self.generate_subsets_button = QPushButton("Generate Subsets")
        self.download_zip_button = QPushButton("Download Zip")
        self.cancel_button = QPushButton("Cancel")
        
        # Connect buttons to their respective slots
        self.generate_subsets_button.clicked.connect(self.on_generate_subsets)
        self.download_zip_button.clicked.connect(self.on_accept)
        self.cancel_button.clicked.connect(self.reject)
        
        # Create a horizontal layout for the buttons
        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.generate_subsets_button)
        self.buttons_layout.addWidget(self.download_zip_button)
        self.buttons_layout.addWidget(self.cancel_button)
        
        # Add the buttons layout to the main layout
        self.layout.addLayout(self.buttons_layout)

    def on_generate_subsets(self):
        thresholds = self.getValues()  # Get current input values
        self.parent().getValuesthreshold=thresholds
        self.subsets = self.split_into_subsets(thresholds)  # Generate subsets
    # Ensure the subset dialog and table are correctly setup and displayed
        self.subsetDialog = QDialog(self)  # Create a new dialog as a child of the main dialog
        self.subsetDialog.setWindowTitle("Subset Table")
        self.subsetDialog.setGeometry(200, 200, 600, 400)

    # Create the subset table within the new dialog
        self.createSubsetTable()
        self.populateTable()  # Populate the table with subset data
        if  self.subsets:
         self.parent().generated_subsets = self.tableWidget
         self.parent().checked_columns=self.column_ranges
        
            # Directly update the main UI with the selected subset
        # self.latest_subset_dialog = LatestSubsetDialog(selected_subset, parent=self)
        # self.latest_subset_dialog.show()
    # Show the subset dialog modally
         self.subsetDialog.exec()
         self.parent().subsetGenerated.emit()
        # In SubsetDialog, after generating subsets

         self.accept()
         self.generate_subsets_button.setEnabled(False)  # Disable the generation button
         self.download_zip_button.setEnabled(False) 


    def populateTable(self):
         # Check if subsets are populated
     if not self.subsets:
        print("No subsets to display.")  # Debug print
        QMessageBox.information(self, "No Subsets", "No subsets were created based on the given thresholds.")
        return
     print("Populating table with subsets...")  # Debug print


     self.tableWidget.setRowCount(len(self.subsets))
     for i, subset_indices in enumerate(self.subsets):
      #  print(f"Processing subset {i+1}")  # Debug print
        try:
            # Fetch the actual subset DataFrame using indices
            subset_df = self.dataframe.iloc[subset_indices]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(f"Subset {i+1}"))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(len(subset_df))))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(len(subset_df.columns))))
          
            # Create and add a radio button for the subset selection
            radioBtn = QRadioButton()
            self.tableWidget.setCellWidget(i, 3, radioBtn)
            #print(subset_df)
        except Exception as e:
            print(f"Error populating table for subset {i+1}: {e}")  # Log any error
        #self.parent().subsetGenerated.emit(self.parent().generatedSubsets)  # Emit signal with generated subsets

     print("Table populated.")  # Debug print

    def createSubsetTable(self):
    # Create and configure the table widget
     self.tableWidget = QTableWidget()
     self.tableWidget.setColumnCount(4)
     self.tableWidget.setHorizontalHeaderLabels(['Subset Name', 'Rows', 'Columns', 'Select'])

    # Create selection and cancel buttons
     selectButton = QPushButton("Select Subset")
     cancelButton = QPushButton("Cancel")
     selectButton.clicked.connect(self.on_subset_selected)
     cancelButton.clicked.connect(self.reject)
     layout = QVBoxLayout()
     layout.addWidget(self.tableWidget)
     layout.addWidget(selectButton)
     layout.addWidget(cancelButton)

    # Set the new layout to the subset dialog
     self.subsetDialog.setLayout(layout)

    def on_subset_selected(self):
     selected_subset = self.getSelectedSubset()
     if selected_subset is not None:
        reply = QMessageBox.question(self, 'Confirm Subset Process',
                                     "Subsetting Process will modify the current data. Do you want to continue?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
      
            subset_dataframe = self.dataframe.iloc[selected_subset]
            self.parent().controller.model.data_frame=subset_dataframe

            # Directly update the main UI with the selected subset DataFrame
            self.parent().display_data(subset_dataframe)
            QMessageBox.information(self, "Subset Selected", "The dataset has been updated.")
            self.accept()  # Close the dialog


    def getSelectedSubset(self):
        selected_indices = []
        for i in range(self.tableWidget.rowCount()):
            cellWidget = self.tableWidget.cellWidget(i, 3)
            if cellWidget and cellWidget.isChecked():
                subset_indices = self.subsets[i]
                selected_indices.extend(subset_indices)
        if selected_indices:
            return selected_indices
        return None
    def getValues(self):
        values = {}
        for column, (min_input, max_input) in self.inputs.items():
            min_val = min_input.text()
            max_val = max_input.text()
            values[column] = (float(min_val), float(max_val))
        return values
   
    def on_accept(self):
        try:
            thresholds = self.getValues()
            subsets = self.split_into_subsets(thresholds)
            if subsets:
                self.show_result_message(len(subsets), [len(subset) for subset in subsets])
                self.save_subsets(subsets)
                self.accept()
            else:
                QMessageBox.information(self, "No Subsets", "No subsets were created based on the given thresholds.")
        except ValueError:
                pass
    def split_into_subsets(self, thresholds):
     df = self.dataframe.copy()  # Work on a copy to avoid modifying the original DataFrame
     subsets = []
     continuous_subset = []
     for i in range(len(df)):
        valid_subset = True
        for col in thresholds:
            threshold_min = float(thresholds[col][0])
            threshold_max = float(thresholds[col][1])
            value = df.iloc[i][col]
            try:
                value = float(value)
            except ValueError:
                valid_subset = False
                break
            if not (threshold_min <= value <= threshold_max):
                valid_subset = False
                break
        if valid_subset:
            continuous_subset.append(i)
        else:
            if continuous_subset:
                subsets.append(continuous_subset)
                continuous_subset = []
     if continuous_subset:
        subsets.append(continuous_subset)
     return subsets

    def show_result_message(self, num_subsets, subset_lengths):
        message = f"Number of subsets created: {num_subsets}\n"
        message += "Number of rows in each subset: " + ", ".join(map(str, subset_lengths)) + "\n"
        if subset_lengths:
            best_subset = subset_lengths.index(max(subset_lengths)) + 1
            message += f"Recommendation: {best_subset} Subset is recommended for analysis."
        QMessageBox.information(self, "Subset Information", message)

   
    def save_subsets(self, subsets):
        zip_filename = "subsets.zip"
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for i, subset_indices in enumerate(subsets):
                subset_df = self.dataframe.iloc[subset_indices]
                subset_filename = f"subset_{i+1}.csv"
                subset_df.to_csv(subset_filename, index=False)
                zipf.write(subset_filename)
                os.remove(subset_filename)
        # Update the message to include the full path where the file is saved
        save_path = os.path.abspath(zip_filename)
        QMessageBox.information(self, "Success", f"Subsets saved to {save_path}")
class LatestSubsetDialog(QDialog):
    def __init__(self, column_ranges, dataframe, threshold, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Subset Table")
        self.setGeometry(200, 200, 600, 400)
        icon_path = os.path.abspath('images/subset_icon.ico')
        self.setWindowIcon(QIcon(icon_path))
        self.threshold = threshold
        self.column_ranges = column_ranges
        self.dataframe = dataframe

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Subset Name', 'Rows', 'Columns', 'Select'])
        selectButton = QPushButton("Select Subset")
        cancelButton = QPushButton("Cancel")
        selectButton.clicked.connect(self.on_subset_selected)
        cancelButton.clicked.connect(self.reject)

        button_layout = QHBoxLayout()
        button_layout.addWidget(selectButton)
        button_layout.addWidget(cancelButton)


        layout = QVBoxLayout(self)
        layout.addWidget(self.tableWidget)
        layout.addLayout(button_layout)
        self.setLayout(layout)
        self.populateTable()  # Populate the table with subset data

    def populateTable(self):

        print("Populating table with subsets...")  # Debug print

        # Generate subsets using the provided threshold
        subsets = self.split_into_subsets(self.threshold)

        # Check if subsets are populated
        if not subsets:
            print("No subsets to display.")  # Debug print
            return

        self.tableWidget.setRowCount(len(subsets))
        for i, subset_indices in enumerate(subsets):
            print(f"Processing subset {i+1}")  # Debug print
            try:
                # Fetch the actual subset DataFrame using indices
                subset_df = self.dataframe.iloc[subset_indices]
                self.tableWidget.setItem(i, 0, QTableWidgetItem(f"Subset {i+1}"))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(len(subset_df))))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(len(subset_df.columns))))

                # Create and add a radio button for the subset selection
                radioBtn = QRadioButton()
                self.tableWidget.setCellWidget(i, 3, radioBtn)
                #print(subset_df)
            except Exception as e:
                print(f"Error populating table for subset {i+1}: {e}")  # Log any error

        print("Table populated.")  # Debug print


    def getSelectedSubset(self):
        selected_indices = []
        self.subsets = self.split_into_subsets(self.threshold)  # Generate subsets

        for i in range(self.tableWidget.rowCount()):
            cellWidget = self.tableWidget.cellWidget(i, 3)
            if cellWidget and cellWidget.isChecked():
                subset_indices = self.subsets[i]
                selected_indices.extend(subset_indices)
        if selected_indices:
            return selected_indices
        return None

    def split_into_subsets(self, thresholds):
        df = self.dataframe.copy()  # Work on a copy to avoid modifying the original DataFrame
        subsets = []
        continuous_subset = []
        for i in range(len(df)):
            valid_subset = True
            for col in thresholds:
                threshold_min = float(thresholds[col][0])
                threshold_max = float(thresholds[col][1])
                value = df.iloc[i][col]
                try:
                    value = float(value)
                except ValueError:
                    valid_subset = False
                    break
                if not (threshold_min <= value <= threshold_max):
                    valid_subset = False
                    break
            if valid_subset:
                continuous_subset.append(i)
            else:
                if continuous_subset:
                    subsets.append(continuous_subset)
                    continuous_subset = []
        if continuous_subset:
            subsets.append(continuous_subset)
        return subsets

    def on_subset_selected(self):
        selected_subset = self.getSelectedSubset()
        if selected_subset is not None:
            reply = QMessageBox.question(self, 'Confirm Subset Process',
                                         "Subsetting Process will modify the current data. Do you want to continue?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                            # Directly update the main UI with the selected subset
             subset_dataframe = self.dataframe.iloc[selected_subset]
             self.parent().controller.model.data_frame=subset_dataframe

            # Directly update the main UI with the selected subset DataFrame
             self.parent().display_data(subset_dataframe)
             QMessageBox.information(self, "Subset Selected", "The dataset has been updated.")
             self.accept()  # Close the dialog


class ArimaConfigDialog(QDialog):
    def __init__(self, dataframe, parent=None):
        super().__init__(parent)
        self.dataframe = dataframe
        self.setWindowTitle("Grid Search")
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowMinMaxButtonsHint |
                            Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowMaximizeButtonHint |
                            Qt.WindowType.CustomizeWindowHint)  # Add min/max window option

        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)  # Add padding around the main layout

        icon_path = os.path.abspath('images/grid_search_icon.ico')
        self.setWindowIcon(QIcon(icon_path))

        self.columnSelectorLabel = QLabel("Select Time Series Column:")
        self.columnSelector = QComboBox()
        if self.dataframe is not None:
            self.columnSelector.addItems(self.dataframe.columns)
        elif self.parent().train_data is not None:
            self.columnSelector.addItems(self.parent().train_data.columns)
        elif self.parent().test_data is not None:
            self.columnSelector.addItems(self.parent().test_data.columns)
     

        self.datasetSelectorLabel = QLabel("Select Dataset:")
        self.datasetSelector = QComboBox()
        if self.dataframe is not None:
            self.datasetSelector.addItem("Actual Set")
        if self.parent().train_data is not None:
            self.datasetSelector.addItem("Train Set")
        if self.parent().test_data is not None:
            self.datasetSelector.addItem("Test Set")



        self.non_seasonal_group = self.create_non_seasonal_group()
        self.seasonal_group = self.create_seasonal_group()

        self.non_seasonal_collapsible = CollapsibleSection("Non-Seasonal")
        self.non_seasonal_collapsible.content_layout.addWidget(self.non_seasonal_group)

        self.seasonal_collapsible = CollapsibleSection("Seasonal")
        self.seasonal_collapsible.content_layout.addWidget(self.seasonal_group)
        self.seasonal_collapsible.setChecked(False)

        self.additional_options_group = self.create_additional_options_group()
        self.additional_options_collapsible = CollapsibleSection("Additional Options")
        self.additional_options_collapsible.content_layout.addWidget(self.additional_options_group)
        self.additional_options_collapsible.setChecked(False)
      
  

        self.iterationLogTextEdit = QTextEdit()
        self.iterationLogTextEdit.setReadOnly(True)
        self.iterationLogTextEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.iterationLogTextEdit.setMinimumHeight(400)  # Set minimum height

        self.runButton = QPushButton("Find Best Parameters")
        self.runButton.clicked.connect(self.findBestArimaParameters)

        # Add widgets to the layout
        self.main_layout.addWidget(self.columnSelectorLabel)
        self.main_layout.addWidget(self.columnSelector)
        self.main_layout.addWidget(self.datasetSelectorLabel)
        self.main_layout.addWidget(self.datasetSelector)
        self.main_layout.addWidget(self.non_seasonal_collapsible)
        self.main_layout.addWidget(self.seasonal_collapsible)
        self.main_layout.addWidget(self.additional_options_collapsible)
        self.main_layout.addWidget(self.iterationLogTextEdit)
        self.main_layout.addWidget(self.runButton)

        # Set main layout to a scrollable area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        content_widget = QWidget()
        content_widget.setLayout(self.main_layout)
        scroll_area.setWidget(content_widget)

        self.setLayout(QVBoxLayout())

        self.layout().addWidget(scroll_area)
        # Adjust window size
        self.resize(800, 600)  # Set initial size
        self.setMinimumWidth(600)  # Set minimum width
        self.setMinimumHeight(400)  # Set minimum height
        self.traceCheckBox = QCheckBox("Trace")
        self.traceCheckBox.setChecked(True)
        self.layout().addWidget(self.traceCheckBox)
        self.suppress_warnings_checkbox = self.create_checkbox("Suppress Warnings", True)
        self.layout().addWidget(self.suppress_warnings_checkbox)
    def findBestArimaParameters(self):
        self.iterationLogTextEdit.clear()
        if self.stepwise_radio.isChecked():
            self.stepwise = True
            self.random_search = False
        elif self.random_search_radio.isChecked():
            self.stepwise = False
            self.random_search = True

       
        selected_column = self.columnSelector.currentText()
        series = None

        if self.datasetSelector.currentText() == "Actual Set":
         series = self.dataframe[selected_column]
        elif self.datasetSelector.currentText() == "Train Set":
         series = self.parent().train_data[selected_column]
        elif self.datasetSelector.currentText() == "Test Set":
         series = self.parent().test_data[selected_column]

    # Handle missing values
        series.dropna(inplace=True)  # Drop rows with missing values

    # Check if there are missing values after dropping
        if series.isnull().any():
         QMessageBox.critical(self, "Error", "Missing values still exist in the time series data after preprocessing.")
         return

    # Ensure the series is in datetime format
        if not np.issubdtype(series.index.dtype, np.datetime64):
         QMessageBox.critical(self, "Error", "The index of the time series data must be in datetime format.")
         return

        original_stdout = sys.stdout
        sys.stdout = EmittingStream(self.iterationLogTextEdit)

        try:
            self.prepareAndRunAutoArima(series)
        finally:
            sys.stdout = original_stdout

    def create_non_seasonal_group(self):
        self.startPLineEdit = self.create_combobox_with_range(1, 5)
        self.maxPLineEdit = self.create_combobox_with_range(1, 5)
        self.dLineEdit = self.create_combobox_with_range(1, 5)
        self.maxdLineEdit = self.create_combobox_with_range(1, 5)
        self.startQLineEdit = self.create_combobox_with_range(1, 5)
        self.maxQLineEdit = self.create_combobox_with_range(1, 5)

        # Set default values
        self.startPLineEdit.setCurrentText("2")
        self.maxPLineEdit.setCurrentText("5")
        self.dLineEdit.setCurrentText('None')  # None
        self.maxdLineEdit.setCurrentText("2")
        self.startQLineEdit.setCurrentText("2")
        self.maxQLineEdit.setCurrentText("5")

        group = QGroupBox("Non-Seasonal Parameters")
        layout = QGridLayout()

        layout.addWidget(QLabel("Start p:"), 0, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.startPLineEdit, 0, 1)
        layout.addWidget(QLabel("Max p:"), 0, 2, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.maxPLineEdit, 0, 3)

        layout.addWidget(QLabel("d:"), 1, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.dLineEdit, 1, 1)
        layout.addWidget(QLabel("Max d:"), 1, 2, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.maxdLineEdit, 1, 3)

        layout.addWidget(QLabel("Start q:"), 2, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.startQLineEdit, 2, 1)
        layout.addWidget(QLabel("Max q:"), 2, 2, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.maxQLineEdit, 2, 3)

        group.setLayout(layout)
        return group
    def create_seasonal_group(self):
        # Create comboboxes
        self.startPSeasonalLineEdit = self.create_combobox_with_range(1, 5)
        self.maxPSeasonalLineEdit = self.create_combobox_with_range(1, 5)
        self.dSeasonalLineEdit = self.create_combobox_with_range(1, 5)
        self.maxDSeasonalLineEdit = self.create_combobox_with_range(1, 5)
        self.startQSeasonalLineEdit = self.create_combobox_with_range(1, 5)
        self.maxQSeasonalLineEdit = self.create_combobox_with_range(1, 5)

        # Set default values
        self.startPSeasonalLineEdit.setCurrentText("1")
        self.maxPSeasonalLineEdit.setCurrentText("2")
        self.dSeasonalLineEdit.setCurrentText('None')  # None
        self.maxDSeasonalLineEdit.setCurrentText("2")
        self.startQSeasonalLineEdit.setCurrentText("1")
        self.maxQSeasonalLineEdit.setCurrentText("2")

        # Create combobox with range 1 to 365
        self.mLineEdit = QComboBox()
        self.mLineEdit.setEditable(True)

        # Set default value to 1
        self.mLineEdit.setCurrentText("1")

        # Define the list of additional values for the dropdown
        other_values = [1, 4,6,7,12,24,52,365]

        # Add other values to the combobox
        for value in other_values:
            self.mLineEdit.addItem(str(value))

        # Create the group and layout
        group = QGroupBox("Seasonal Parameters")
        layout = QGridLayout()

        layout.addWidget(QLabel("Start P:"), 0, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.startPSeasonalLineEdit, 0, 1)
        layout.addWidget(QLabel("Max P:"), 0, 2, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.maxPSeasonalLineEdit, 0, 3)

        layout.addWidget(QLabel("D:"), 1, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.dSeasonalLineEdit, 1, 1)
        layout.addWidget(QLabel("Max D:"), 1, 2, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.maxDSeasonalLineEdit, 1, 3)

        layout.addWidget(QLabel("Start Q:"), 2, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.startQSeasonalLineEdit, 2, 1)
        layout.addWidget(QLabel("Max Q:"), 2, 2, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.maxQSeasonalLineEdit, 2, 3)

        layout.addWidget(QLabel("Seasonal Period (m):"), 3, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.mLineEdit, 3, 1)

        group.setLayout(layout)
        return group


    def create_additional_options_group(self):
        group = QGroupBox("Additional Parameters")
        layout = QVBoxLayout()

        checkboxes_layout = QHBoxLayout()

        # Replace the checkboxes for Stepwise and Random Search with radio buttons
        self.stepwise_radio = QRadioButton("Stepwise")
        self.random_search_radio = QRadioButton("Random Search")
       

        self.stepwise_radio.setChecked(True)

        self.stepwise_radio.toggled.connect(self.on_radio_toggled)
        self.random_search_radio.toggled.connect(self.on_radio_toggled)
        # Modify the create_additional_options_group method to use radio buttons
        checkboxes_layout.addWidget(self.stepwise_radio)
        checkboxes_layout.addWidget(self.random_search_radio)
  # Default selection
        layout.addLayout(checkboxes_layout)
        layout.addSpacing(5)  # Adjusted margin

        grid_layout = QGridLayout()

        parameters = [
            ("Max Order:", self.create_combobox_with_range(1, 10)),
            ("Information Criterion:", self.create_dropdown(['aic', 'bic', 'hqic', 'oob'])),
            ("Alpha:", QLineEdit("0.05")),
            ("Test:", self.create_dropdown(['kpss', 'adf', 'pp'])),
            ("Seasonal Test:", self.create_dropdown(['ocsb', 'ch'])),
            ("N Jobs:", self.create_dropdown([str(i) for i in range(1, 5)])),
            ("Method:", self.create_dropdown(['lbfgs', 'newton', 'nm', 'bfgs', 'cg', 'ncg', 'powell', 'basinhopping'])),
            ("Max Iter:", self.create_combobox_with_range(50, 500)),
            ("Error Action:", self.create_dropdown(['warn', 'raise', 'ignore', 'trace'])),
            ("Random State:", QLineEdit("None")),
            ("N Fits:", self.create_combobox_with_range(10, 100)),
            ("Out of Sample Size:", QLineEdit("0")),
            ("Scoring:", self.create_dropdown(['mse', 'mae'])),
            ("With Intercept:", self.create_dropdown(['auto', 'True', 'False'])),
            
            ("Random:", self.create_dropdown(['auto', 'True', 'False'])),
        ]
        self.max_order = int(parameters[0][1].currentText())
        self.info_criterion = parameters[1][1].currentText()
        self.alpha = float(parameters[2][1].text())
        self.test = parameters[3][1].currentText()
        self.seasonal_test = parameters[4][1].currentText()
        self.n_jobs = int(parameters[5][1].currentText())
        self.method = parameters[6][1].currentText()
        self.max_iter = int(parameters[7][1].currentText())
        self.error_action = parameters[8][1].currentText()
        self.random_state = parameters[9][1].text()
        self.n_fits = int(parameters[10][1].currentText())
        self.oos_size = int(parameters[11][1].text())
        self.scoring = parameters[12][1].currentText()
        self.with_intercept = parameters[13][1].currentText()

        self.random = parameters[14][1].currentText()
        for idx, (label, widget) in enumerate(parameters):
            if idx < 7:  # First column for non-seasonal parameters
                grid_layout.addWidget(QLabel(label), idx, 0, 1, 1, Qt.AlignmentFlag.AlignRight)
                grid_layout.addWidget(widget, idx, 1, 1, 1)
            else:  # Second column for seasonal parameters
                grid_layout.addWidget(QLabel(label), idx - 7, 2, 1, 1, Qt.AlignmentFlag.AlignLeft)
                grid_layout.addWidget(widget, idx - 7, 3, 1, 1)

        layout.addLayout(grid_layout)
        group.setLayout(layout)
        self.parameter_widgets = {label: widget for label, widget in parameters}  # Store parameter widgets in a dictionary
        #self.findBestArimaParameters()  # Call the method to initialize parameters
        if self.stepwise_radio.isChecked():
            self.parameter_widgets["Max Order:"].setEnabled(False)
            self.parameter_widgets["Random State:"].setEnabled(False)
            self.parameter_widgets["N Fits:"].setEnabled(False)
            self.parameter_widgets["Random:"].setEnabled(False)
        return group

    def on_radio_toggled(self):
        # Enable or disable parameters based on the selected radio button
        if self.stepwise_radio.isChecked():
            self.parameter_widgets["Max Order:"].setEnabled(False)
            self.parameter_widgets["Random State:"].setEnabled(False)
            self.parameter_widgets["N Fits:"].setEnabled(False)
            self.parameter_widgets["Random:"].setEnabled(False)
        elif self.random_search_radio.isChecked():
            self.parameter_widgets["Max Order:"].setEnabled(True)
            self.parameter_widgets["Random State:"].setEnabled(True)
            self.parameter_widgets["N Fits:"].setEnabled(True)
            self.parameter_widgets["Random:"].setEnabled(True)

    def create_combobox_with_range(self, start, end):
        combobox = QComboBox()
        combobox.setEditable(True)
        for i in range(start, end + 1):
            combobox.addItem(str(i))

        # Connect the currentTextChanged signal to the custom slot
        combobox.currentTextChanged.connect(self.check_numeric_input)

        # Set size policy to expand horizontally and have a fixed vertical size
        combobox.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        combobox.setMinimumWidth(100)  # Set minimum width

        return combobox
    def check_numeric_input(self, text):
     if text.strip() == "":
        # If the entered text is empty, do nothing
        return

     try:
        # Attempt to convert the entered text to a numeric value
        float(text)  # Try to convert to float

     except ValueError:
        # If conversion fails, display an error message
        pass
    def create_dropdown(self, options):
        dropdown = QComboBox()
        dropdown.addItems(options)

        # Set size policy to expand horizontally and have a fixed vertical size
        dropdown.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        dropdown.setMinimumWidth(100)  # Set minimum width

        return dropdown

    def create_checkbox(self, text, checked=False):
        checkbox = QCheckBox(text)
        checkbox.setChecked(checked)

        # Set size policy to expand horizontally and have a fixed vertical size
        checkbox.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        return checkbox



    def prepareAndRunAutoArima(self, series):
        trace = self.traceCheckBox.isChecked()
        if self.non_seasonal_collapsible.isChecked():
         start_p = int(self.startPLineEdit.currentText())
         start_q = int(self.startQLineEdit.currentText())
         max_p = min(int(self.maxPLineEdit.currentText()), 3)  # Limit maximum p to 3
         max_q = min(int(self.maxQLineEdit.currentText()), 3)  # Limit maximum q to 3
         d_text =self.dLineEdit.currentText()
         max_d=int(self.maxdLineEdit.currentText())
         
         error_action ='warn'


         d = None if d_text.lower() == None  or d_text=='None' else int(d_text)
         
        if self.non_seasonal_collapsible.isChecked()==False:
         start_p = 2
         start_q = 2
         d=None
         max_p =5
         max_d=2
         max_q=5
         error_action ='warn'
        elif self.seasonal_collapsible.isChecked and self.non_seasonal_collapsible.isChecked:
            start_p = int(self.startPLineEdit.currentText())
            start_q = int(self.startQLineEdit.currentText())
            max_p = min(int(self.maxPLineEdit.currentText()), 3)  # Limit maximum p to 3
            max_q = min(int(self.maxQLineEdit.currentText()), 3)  # Limit maximum q to 3
            d_text = self.dLineEdit.currentText()
            # Convert current text to integer, handling empty string case

            d = None if d_text.lower() == None  or d_text=='None' else int(d_text)            # Convert current text to integer, handling empty string case
            max_d=int(self.maxdLineEdit.currentText())
            start_P = int(self.startPSeasonalLineEdit.currentText())
            start_Q = int(self.startQSeasonalLineEdit.currentText())
            max_P = min(int(self.maxPSeasonalLineEdit.currentText()), 2)  # Limit maximum P to 2
            max_D=int(self.maxDSeasonalLineEdit.currentText())
            max_Q = min(int(self.maxQSeasonalLineEdit.currentText()), 2)  # Limit maximum Q to 2
            D_text=self.dSeasonalLineEdit.currentText()
            D = None if self.dSeasonalLineEdit == None  or D_text=='None' else int(D_text)
            m = int(self.mLineEdit.currentText())
            error_action ='warn'

        elif self.non_seasonal_collapsible.isChecked() and self.seasonal_collapsible.isChecked()==False:
            start_p = int(self.startPLineEdit.currentText())
            start_q = int(self.startQLineEdit.currentText())
            max_p = min(int(self.maxPLineEdit.currentText()), 3)  # Limit maximum p to 3
            max_q = min(int(self.maxQLineEdit.currentText()), 3)  # Limit maximum q to 3
            d_text = self.dLineEdit.currentText()
            max_d=int(self.maxdLineEdit.currentText())
            start_P =1
            start_Q =1
            max_P =2
            max_Q = 2
            max_D = 1
            D=None
            m = 1
            error_action ='warn'
        if self.additional_options_collapsible.isChecked():
            # Assign values from additional options collapsible
            max_order = self.max_order
            info_criterion = self.info_criterion
            alpha = self.alpha
            test = self.test
            seasonal_test = self.seasonal_test
            n_jobs = self.n_jobs
            method = self.method
            max_iter = self.max_iter
            error_action = self.error_action
            random_state = self.random_state
            n_fits = self.n_fits
            oos_size = self.oos_size
            scoring = self.scoring
            with_intercept = self.with_intercept
            random=self.random
        if self.additional_options_collapsible.isChecked()==False:
            # Set default values if additional options collapsible is unchecked
            max_order = None
            info_criterion = 'aic'
            alpha = 0.05
            test = 'kpss'
            seasonal_test = 'ocsb'
            n_jobs = 1
            method = 'lbfgs'
            max_iter = 50
            error_action = 'warn'
            random_state = None
            n_fits = 10
            oos_size = 0
            scoring = 'mse'
            with_intercept = 'auto'
            random=False
        try:
            # Fit auto ARIMA model based on the combinations of parameter checkboxes
            model = auto_arima(series, start_p=start_p, start_q=start_q, max_p=max_p, max_q=max_q, d=d,
                           start_P=start_P, start_Q=start_Q, max_Q=max_Q, max_P=max_P, m=m,
                           seasonal=self.seasonal_collapsible.isChecked(), D=D, trace=trace,
                           error_action=error_action, suppress_warnings=self.suppress_warnings_checkbox.isChecked(),
                           random_search=self.random_search_radio.isChecked(),
                           stepwise=self.stepwise_radio.isChecked(),
                           information_criterion=info_criterion, alpha=alpha, test=test,
                           seasonal_test=seasonal_test,max_D=max_D,
                           n_jobs=n_jobs, method=method, max_iter=max_iter, max_order=max_order,
                           random_state=random_state, max_d=max_d,n_fits=n_fits,
                           out_of_sample_size=oos_size, scoring=scoring, with_intercept=with_intercept,random=random)
            #print(type(model))
            self.parent().best_params = {
                'p': model.order[0],
                'd': model.order[1],
                'q': model.order[2],
                'P': model.seasonal_order[0],
                'D': model.seasonal_order[1],
                'Q': model.seasonal_order[2],
                'm': model.seasonal_order[3]
            }


            # Evaluate model
            forecast = model.predict(len(series))
            mse = mean_squared_error(series, forecast)
            self.iterationLogTextEdit.append(f"\nMean Squared Error (MSE): {mse}")
            if not self.traceCheckBox.isChecked():
                self.iterationLogTextEdit.append("\nPlease check the trace to get the best model parameters.")
           

        except Exception as e:
            self.iterationLogTextEdit.append(f"\n\nFailed to find optimal parameters due to an error:\n{e}")
            return
class EmittingStream(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        QApplication.processEvents()
        self.text_widget.append(text)

    def flush(self):
        pass


class CollapsibleSection(QGroupBox):
    def __init__(self, title="", parent=None):
        super().__init__(title, parent)
        
        self.setCheckable(True)
        self.setChecked(True)  # Default state: expanded
        self.setStyleSheet("QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top left; padding: 5px; }")
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(5, 5, 5, 5)  # Adjust margin for better spacing
        self.content_layout.addStretch()
        self.setLayout(self.content_layout)
        self.toggled.connect(self.on_toggled)


    def on_toggled(self, checked):
        for i in range(1, self.content_layout.count()):
            widget = self.content_layout.itemAt(i).widget()
            widget.setVisible(checked)
            if not checked:
                widget.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred))
            else:
                widget.setSizePolicy(QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred))
        # Adjust layout spacing when collapsible section is collapsed
        if not checked:
            self.layout().setSpacing(5)
        else:
            self.layout().setSpacing(20)



class ForecastResult(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Future Forecasting")
        self.setWindowIcon(QIcon('images/forecast_icon.ico'))  # Setting window icon
        self.dataframe = self.parent().df_model
        self.selected_column = self.parent().selected_column
        self.order = self.parent().order
        self.seasonal_order = self.parent().seasonal_order

        self.initUI()

    def initUI(self):
        # Creating a scroll area to make the dialog scrollable
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.layout = QVBoxLayout(self)
        self.setContentsMargins(20, 20, 20, 20)
        self.layout.addWidget(scroll_area)

        # Creating the content widget for the scroll area
        content_widget = QWidget()
        scroll_area.setWidget(content_widget)

        # Using a QVBoxLayout for the content widget
        content_layout = QVBoxLayout(content_widget)

        self.resize(800, 600)  # Set initial size
        self.setMinimumWidth(600)  # Set minimum width
        self.setMinimumHeight(400)  # Set minimum height

        # Forecasting and plotting
        steps_to_forecast = 12  # Or any other number of steps you wish to forecast
        forecasted_values = self.forecast_into_future(self.dataframe, self.selected_column, self.order,
                                                      self.seasonal_order, steps=steps_to_forecast)
        self.plot_historical_and_forecast(content_layout, self.dataframe, forecasted_values, self.selected_column)

        # Add button to save PDF
        save_button = QPushButton("Save as PDF", self)
        save_button.clicked.connect(self.save_as_pdf)
        content_layout.addWidget(save_button)

    def forecast_into_future(self, df, column_name, order, seasonal_order=None, steps=12):
        """
        Retrains the ARIMA model on the entire dataset including potential seasonal components and
        forecasts the specified number of steps into the future.
        """
        # Fit the ARIMA model to the entire dataset
        if seasonal_order:
            model = SARIMAX(df[column_name], order=order, seasonal_order=seasonal_order)
        else:
            model = SARIMAX(df[column_name], order=order)
        fitted_model =self.parent().fitted_model

        # The start point is the length of the dataset
        start = len(df)
        # The end point is the start point plus the number of steps
        end = start + steps - 1

        # Generating forecasts
        future_forecast = fitted_model.predict(start=start, end=end, typ='levels')

        return future_forecast

    def plot_historical_and_forecast(self, layout, df, future_forecast, column_name):
        """
        Plots the historical data alongside the future forecasted values.
        """
        # Clear layout before adding the plot
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

        fig, ax = plt.subplots(figsize=(12, 5))

        # Plotting the historical data
        ax.plot(df.index, df[column_name], label='Historical Data', marker='o', color='blue')

        # Creating a continuation of the index for the forecasted values
        last_date = df.index[-1]
        periods = len(future_forecast)
        freq = pd.infer_freq(df.index)  # Attempt to infer the frequency of the index
        future_index = pd.date_range(start=last_date, periods=periods + 1, freq=freq)[1:]  # Offset to start after last_date

        # Plotting the forecasted data
        ax.plot(future_index, future_forecast, label='Future Forecast', marker='x', linestyle='--', color='red')

        ax.set_title(f'Historical and Future Forecast of {column_name}')
        ax.set_xlabel('Date')
        ax.set_ylabel(column_name)
        ax.legend()
        ax.grid(True)

        # Embedding the matplotlib plot into PyQt
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

    def save_as_pdf(self):
        # Open file dialog to select save location
        filename = f"TSA_{os.path.basename(self.parent().file_path).split('.')[0]}_SARIMA_Forecast_Result_Report.pdf"
        file_path, _ = QFileDialog.getSaveFileName(self, "Save as PDF", filename, "PDF Files (*.pdf)")

        if file_path:
            # Create a PDF file
            with PdfPages(file_path) as pdf:
                # Get the current matplotlib figure
                fig = plt.gcf()
                # Save the figure to PDF
                pdf.savefig(fig)
                plt.close()

            # Open the saved PDF file
            try:
                subprocess.Popen(["xdg-open", file_path])  # Linux
            except:
                try:
                    subprocess.Popen(["open", file_path])  # macOS
                except:
                    subprocess.Popen(["start", "", file_path], shell=True)  # Windows
class ModelWithParameter(QDialog):
    def __init__(self, dataframe, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Model With Parameters")
        self.setWindowIcon(QIcon('images/model_parameters_icon.ico'))  # Setting window icon
        self.dataframe = dataframe
        self.initUI()

    def initUI(self):
        # Creating a scroll area to make the dialog scrollable
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        self.layout = QVBoxLayout(self)
        self.setContentsMargins(20,20,20,20)
        self.layout.addWidget(scroll_area)
        self.columnSelector = QComboBox()
        self.columnSelector.addItems(self.dataframe.columns)
        # Creating the content widget for the scroll area
        content_widget = QWidget()
        scroll_area.setWidget(content_widget)

        # Using a QVBoxLayout for the content widget
        content_layout = QVBoxLayout(content_widget)

        # Create tabs for manual input and import
        self.tabWidget = QTabWidget()
        self.manualTab = QWidget()
        self.reportTab = QWidget()
        self.plotTab = QWidget()
        self.tabWidget.addTab(self.manualTab, "Model With Parameters")
        self.tabWidget.addTab(self.reportTab, "Report")
        self.tabWidget.addTab(self.plotTab, "Plots")
        content_layout.addWidget(self.tabWidget)

        # Create widgets for manual input tab
        self.createManualInputGroup()

        # Initialize QTextEdit for displaying iteration logs and ARIMA model summary
        self.iterationLogTextEdit = QTextEdit()
        self.iterationLogTextEdit.setReadOnly(True)
        self.iterationLogTextEdit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.iterationLogTextEdit.setMinimumHeight(400)  # Set minimum height
        content_layout.addWidget(self.iterationLogTextEdit)
            # Call a function when the "Plots" tab is selected



        # Generate ARIMA Model Button
        self.generateModelButton = QPushButton("Generate ARIMA Model")
        self.generateModelButton.clicked.connect(self.findBestArimaParameters)

        self.generateModelButton.clicked.connect(self.generateArimaModel)
        content_layout.addWidget(self.generateModelButton)



        # Set initial tab states
        self.tabWidget.setTabEnabled(1, False)  # Report tab initially disabled
        self.tabWidget.setTabEnabled(2, False)  # Plots tab initially disabled

        self.resize(800, 600)  # Set initial size
        self.setMinimumWidth(600)  # Set minimum width
        self.setMinimumHeight(400)  # Set minimum height
        self.tabWidget.currentChanged.connect(self.handleTabChange)

    def handleTabChange(self, index):
        if index == 1:
            self.iterationLogTextEdit.setEnabled(False)
            self.iterationLogTextEdit.setVisible(False)
            self.generateModelButton.setVisible(False)

            # Call a function when the "Report" tab is selected
            self.addReportTab()
        if index == 0:
            self.iterationLogTextEdit.setEnabled(True)
            self.iterationLogTextEdit.setVisible(True)
            self.generateModelButton.setVisible(True)
        if index == 2:

            self.iterationLogTextEdit.setEnabled(False)
            self.iterationLogTextEdit.setVisible(False)
            self.generateModelButton.setVisible(False)
            self.addPlotsTab()
    def addReportTab(self):

        self.report_tab()
    def report_tab(self):
        self.iterationLogTextEdit.setEnabled(True)
        self.iterationLogTextEdit.setVisible(True)
        self.generateModelButton.setVisible(False)
        selected_column = self.columnSelector.currentText()
        if self.datasetSelector.currentText() == "Actual Set":
            series = self.dataframe[selected_column].astype(float)
        elif self.datasetSelector.currentText() == "Train Set":
            series = self.parent().train_data[selected_column].astype(float)
        elif self.datasetSelector.currentText() == "Test Set":
            series = self.parent().test_data[selected_column].astype(float)
        # Ensure train_data contains only numeric values

        # Initialize the layout for the report tab
        layout = QVBoxLayout()

        # Add the iteration log text edit widget to the layout
        layout.addWidget(self.iterationLogTextEdit)

        # Create a button to save the report as PDF
        self.reportSavePDFButton = QPushButton("Save PDF")
        self.reportSavePDFButton.clicked.connect(self.saveReportAsPDF)

        # Add the save PDF button to the layout
        layout.addWidget(self.reportSavePDFButton)

        # Set the layout for the report tab
        self.reportTab.setLayout(layout)

    def saveReportAsPDF(self):
        filename = f"TSA_{os.path.basename(self.parent().file_path).split('.')[0]}_SARIMA_Report.pdf"
        file_path = os.path.join(os.getcwd(), filename)

        # Create a PDF file
        with PdfPages(file_path) as pdf:
            # Create a figure and plot summary text
            fig, ax = plt.subplots(figsize=(8.27, 11.69))  # A4 size
            ax.axis('off')
            ax.text(0.5, 0.5, self.summary_text, fontsize=10, va='center', ha='center', wrap=True)  
            pdf.savefig(fig)
            plt.close()

        # Open the saved PDF file
        try:
            subprocess.Popen(["xdg-open", file_path])  # Linux
        except:
            try:
                subprocess.Popen(["open", file_path])  # macOS
            except:
                subprocess.Popen(["start", "", file_path], shell=True)  # Windows
    def addPlotsTab(self):
        selected_column = self.columnSelector.currentText()
        if self.datasetSelector.currentText() == "Actual Set":
            series = self.dataframe[selected_column].astype(float)
        elif self.datasetSelector.currentText() == "Train Set":
            series = self.parent().train_data[selected_column].astype(float)
        elif self.datasetSelector.currentText() == "Test Set":
            series = self.parent().test_data[selected_column].astype(float)
        
        # Ensure train_data contains only numeric values
            # Get the selected column
        column_name= self.columnSelector.currentText()
    
    # Get the selected dataset
        selected_dataset = self.datasetSelector.currentText()
    
    # Determine the dataset based on the selected option
        if selected_dataset == "Actual Set":
         train = self.dataframe[selected_column].values
        elif selected_dataset == "Train Set":
         train = self.parent().train_data[selected_column].values
        elif selected_dataset == "Test Set":
         train = self.parent().test_data[selected_column].values
        else:
         QMessageBox.warning(self, "Input Error", "Please select a dataset.")
         return
        # Fit ARIMA model
        order=(self.p, self.d, self.q)


        seasonal_order=(self.P,self.D,self.Q,self.m)

        fitted_model = self.fit_arima_model(train, column_name, order, seasonal_order)
        # Plot training predictions
        self.plot_train_predictions(series, fitted_model,selected_column=column_name)
        train_pred_plot = plt.gcf().canvas
        train_pred_plot.setMinimumSize(600, 400)  # Set minimum size for the plot canvas
        blank_widget = QWidget()
        blank_widget.setFixedHeight(50)  # Adjust the height as needed

        # Plot model diagnostics
        self.plot_model_diagnostics(fitted_model)
        diagnostics_plot = plt.gcf().canvas
        diagnostics_plot.setMinimumSize(600, 700)  # Set minimum size for the plot canvas
            
        # Check if Test Set is selected for prediction


        # Create buttons
        self.plotPredictButton = QPushButton("Predict")
        self.plotPredictButton.clicked.connect(lambda: self.generate_test_prediction_report(fitted_model, selected_column))

        self.plotSavePDFButton = QPushButton("Save PDF")
        self.plotSavePDFButton.clicked.connect(lambda: self.savePlotAsPDF(fitted_model, series, selected_column))
        
        # Create button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.plotPredictButton)
        button_layout.addWidget(self.plotSavePDFButton)

        # Set up the main layout for the plot tab
        layout = QVBoxLayout()
        layout.addWidget(train_pred_plot)
        layout.addWidget(blank_widget)
        layout.addWidget(diagnostics_plot)
        layout.addLayout(button_layout)  # Add button layout
        self.plotTab.setLayout(layout)


    def generateArimaModel(self):
        self.iterationLogTextEdit.clear()

        trend=None
        trend_offset=1
        measurement_error = False
        time_varying_regression = False
        mle_regression = True
        simple_differencing = False
        enforce_stationarity = True
        enforce_invertibility = True
        hamilton_representation = False
        concentrate_scale = False
        trend_offset = 1
        use_exact_diffuse = False

    # Get the selected column
        selected_column = self.columnSelector.currentText()
    
    # Get the selected dataset
        selected_dataset = self.datasetSelector.currentText()
    
    # Determine the dataset based on the selected option
        if selected_dataset == "Actual Set":
         dataset = self.dataframe[selected_column].values
         self.parent().df_model=self.dataframe


        elif selected_dataset == "Train Set":
         dataset = self.parent().train_data[selected_column].values
         self.parent().df_model=self.parent().train_data

        elif selected_dataset == "Test Set":
         dataset = self.parent().test_data[selected_column].values
         self.parent().df_model=self.parent().test_data

        else:
         QMessageBox.warning(self, "Input Error", "Please select a dataset.")
         return
        try:
            

            endog = dataset
            self.parent().selected_column=selected_column
            if self.seasonal_collapsible.isChecked() and self.non_seasonal_collapsible.isChecked():
             model = SARIMAX(endog=endog, order=(self.p, self.d, self.q),seasonal_order=(self.P,self.D,self.Q,self.m),trend=trend,
                            trend_offset=trend_offset, measurement_error=measurement_error,
                        time_varying_regression=time_varying_regression, mle_regression=mle_regression,
                        simple_differencing=simple_differencing, enforce_stationarity=enforce_stationarity,
                        enforce_invertibility=enforce_invertibility, hamilton_representation=hamilton_representation,
                        concentrate_scale=concentrate_scale, use_exact_diffuse=use_exact_diffuse)
             
            else:

             model = SARIMAX(endog=endog, order=(self.p, self.d, self.q),trend=trend,
                            trend_offset=trend_offset, measurement_error=measurement_error,
                        time_varying_regression=time_varying_regression, mle_regression=mle_regression,
                        simple_differencing=simple_differencing, enforce_stationarity=enforce_stationarity,
                        enforce_invertibility=enforce_invertibility, hamilton_representation=hamilton_representation,
                        concentrate_scale=concentrate_scale, use_exact_diffuse=use_exact_diffuse)
            
            p = self.p
            d = self.d
            q = self.q
            P = self.P
            D = self.D
            Q = self.Q
            m = self.m
            
            fitted_model = model.fit()
            self.parent().fitted_model=fitted_model
            self.order=(p, d, q)
            self.seasonal_order=(P,D,Q,m)
            self.parent().order=self.order
            self.parent().seasonal_order=self.seasonal_order
            self.differencing_order=d
# Display model summary
            summary_text = fitted_model.summary().as_text()
            self.summary_text=summary_text
            self.iterationLogTextEdit.append("\n\nSARIMA Model Summary:\n")
            self.iterationLogTextEdit.append(summary_text)
            self.tabWidget.setTabEnabled(1, True)  # Report tab initially disabled
            self.tabWidget.setTabEnabled(2, True)  


# Print residuals

        except Exception as e:
            self.iterationLogTextEdit.append(f"\n\nFailed to find SARIMA due to an error:\n{e}")
            return

        # Once the model is generated, enable the report and plots tabs
        self.tabWidget.setTabEnabled(1, True)  # Enable report tab
        self.tabWidget.setTabEnabled(2, True)  # Enable plots tab

        # Switch to the report tab
        self.tabWidget.setCurrentIndex(1)

    def fit_arima_model(self, train, column_name, order,seasonal_order):
        """
        Fits an ARIMA model to the specified column of the training dataset and prints the model summary.

        This function is tailored for training the model on a specific column of a pandas DataFrame or Series.
        It prints out the summary of the fitted model, providing insights into the performance and characteristics 
        of the model.

        Parameters:
        - train: The training dataset (pandas DataFrame or Series).
        - column_name: The name of the column to be modeled (string).
        - order: A tuple specifying the (p,d,q) order of the model.

        Returns:
        - results: The results of the fitted model, which include the model summary and coefficients.
        """
        self.iterationLogTextEdit.clear()

        trend=None
        trend_offset=1
        measurement_error = False
        time_varying_regression = False
        mle_regression = True
        simple_differencing = False
        enforce_stationarity = True
        enforce_invertibility = True
        hamilton_representation = False
        concentrate_scale = False
        trend_offset = 1
        use_exact_diffuse = False

    # Get the selected column
        selected_column = self.columnSelector.currentText()
    
    # Get the selected dataset
        selected_dataset = self.datasetSelector.currentText()
    
    # Determine the dataset based on the selected option
        if selected_dataset == "Actual Set":
         dataset = self.dataframe[selected_column].values
        elif selected_dataset == "Train Set":
         dataset = self.parent().train_data[selected_column].values
        elif selected_dataset == "Test Set":
         dataset = self.parent().test_data[selected_column].values
        else:
         QMessageBox.warning(self, "Input Error", "Please select a dataset.")
         return
        try:
            
            endog = dataset
            if self.seasonal_collapsible.isChecked() and self.non_seasonal_collapsible.isChecked():
             model = SARIMAX(endog=endog, order=(self.p, self.d, self.q),seasonal_order=(self.P,self.D,self.Q,self.m),trend=trend,
                            trend_offset=trend_offset, measurement_error=measurement_error,
                        time_varying_regression=time_varying_regression, mle_regression=mle_regression,
                        simple_differencing=simple_differencing, enforce_stationarity=enforce_stationarity,
                        enforce_invertibility=enforce_invertibility, hamilton_representation=hamilton_representation,
                        concentrate_scale=concentrate_scale, use_exact_diffuse=use_exact_diffuse)
             
            else:

             model = SARIMAX(endog=endog, order=(self.p, self.d, self.q),trend=trend,
                            trend_offset=trend_offset, measurement_error=measurement_error,
                        time_varying_regression=time_varying_regression, mle_regression=mle_regression,
                        simple_differencing=simple_differencing, enforce_stationarity=enforce_stationarity,
                        enforce_invertibility=enforce_invertibility, hamilton_representation=hamilton_representation,
                        concentrate_scale=concentrate_scale, use_exact_diffuse=use_exact_diffuse)

            p = self.p
            d = self.d
            q = self.q
            P = self.P
            D = self.D
            Q = self.Q
            m = self.m
            
            fitted_model = model.fit()
            self.order=(p, d, q)
            self.seasonal_order=(P,D,Q,m)
            self.differencing_order=d
# Display model summary
            summary_text = fitted_model.summary().as_text()
            self.summary_text=summary_text
            self.iterationLogTextEdit.clear()

            self.iterationLogTextEdit.append("\n\nSARIMA Model Summary:\n")
            self.iterationLogTextEdit.append(summary_text)
            self.tabWidget.setTabEnabled(1, True)  # Report tab initially disabled
            self.tabWidget.setTabEnabled(2, True)  



# Print residuals


# Print diagnostic plots (example: ACF and PACF)

        except Exception as e:
            self.iterationLogTextEdit.append(f"\n\nFailed to find SARIMA due to an error:\n{e}")
            return
        results = model.fit()
        print(results.summary())
        return results
    def plot_train_predictions(self, series, fitted_model,selected_column):
        # Plot training predictions vs actual data
        train_predictions = fitted_model.predict(start=0, end=len(series)-1)
        plt.figure(figsize=(10, 5))
        plt.plot(series.index, series.values, label='Actual Training Data', color='blue')
        plt.plot(series.index, train_predictions, label='Training Model Predictions', color='red', linestyle='--')
        plt.title(f'Train Data vs Model Predictions for {selected_column}')
        plt.xlabel('Time')
        plt.ylabel(f'{selected_column}')
        plt.legend()
        plt.grid()

    def plot_model_diagnostics(self, fitted_model):
        # Plot diagnostics from Statsmodels
        diag = fitted_model.plot_diagnostics(figsize=(10, 8))
        plt.grid(True, which='major', axis='y', color='green', alpha=0.75, linestyle='--')
        plt.grid(True, which='major', axis='x', color='blue', alpha=0.5, linestyle=':')
        plt.suptitle('Training Model Diagnostics: Residual Checks')
        diag.tight_layout()

    def savePlotAsPDF(self, fitted_model, train_data, selected_column):
        # Get the file path for saving
        filename = f"TSA_{os.path.basename(self.parent().file_path).split('.')[0]}_SARIMA_Plot_Report.pdf"
        file_path = os.path.join(os.getcwd(), filename)

        # Create a PDF canvas
        with PdfPages(file_path) as pdf:
            # Plot training predictions
            self.plot_train_predictions(train_data, fitted_model,selected_column)
            pdf.savefig()
            plt.close()  # Close the figure after saving

            # Plot model diagnostics
            self.plot_model_diagnostics(fitted_model)
            pdf.savefig()
            plt.close()  # Close the figure after saving

        # Show notification
        QMessageBox.information(self, "PDF Saved Successfully", f"PDF saved successfully at: {file_path}")

        # Open the saved PDF file
        try:
            subprocess.Popen(["xdg-open", file_path])  # Linux
        except:
            try:
                subprocess.Popen(["open", file_path])  # macOS
            except:
                subprocess.Popen(["start", "", file_path], shell=True)  # Windows
 
    def generate_test_predictions(self,test_data, fitted_model,train_data):
        """
        Generates predictions for the test set using the fitted ARIMA model.
        
        Parameters:
        - test_data: The test dataset (pandas DataFrame or Series).
        - fitted_model: The trained ARIMA model.
        
        Returns:
        - test_predictions: Predictions made on the test set.
        """
        test_predictions = fitted_model.predict(start=len(train_data), end=len(train_data) + len(test_data) - 1)
        return test_predictions


    def plot_test_predictions(self,test_data,selected_column, test_predictions):
        """
        Plots the actual test data against the test predictions.
        
        Parameters:
        - test_data: The test dataset, including actual values.
        - test_predictions: Predictions made on the test set.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(test_data.index, test_data.values, label='Actual Test Data', marker='o')
        plt.plot(test_data.index, test_predictions, label='Test APredictions', marker='x', linestyle='--', alpha=0.7)
        plt.title(f'Test Set Predictions vs Actual Test Data for {selected_column}')        
        plt.legend()
        plt.grid(True)
        plt.xlabel('Date-Time')
        plt.ylabel(f'{selected_column}')
        

    def plot_test_predictions_errors(self,test_data, test_predictions):
        """
        Plots a histogram of the test prediction errors.
        
        Parameters:
        - test_data: The test dataset, including actual values.
        - test_predictions: Predictions made on the test set.
        """
        prediction_errors = test_data - test_predictions
        plt.figure(figsize=(8, 5))
        sns.histplot(prediction_errors, kde=True, color='blue')
        plt.title('Histogram of Test Prediction Errors')
        plt.xlabel('Prediction Errors')
        plt.ylabel('Density')

    def plot_magnitude_residual_relationship(self,test_data, test_predictions):
        """
        Plots the relationship between the magnitude of actual test values and the squared prediction errors.
        
        Parameters:
        - test_data: The test dataset with actual values.
        - test_predictions: Predictions made on the test set.
        """
        prediction_errors = test_data - test_predictions
        plt.figure(figsize=(8, 5))
        plt.scatter(test_data, prediction_errors**2)
        plt.title('Magnitude-Residual Relationship')
        plt.xlabel('Actual Test Values')
        plt.ylabel('Squared Prediction Errors')
        plt.grid(True)
    

    # def display_test_evaluation_metrics(self,test_data, test_predictions):
    #     """
    #     Displays evaluation metrics for the test predictions.
        
    #     Parameters:
    #     - test_data: The test dataset with actual values.
    #     - test_predictions: Predictions made on the test set.
    #     """
    #     mae = mean_absolute_error(test_data, test_predictions)
    #     mse = mean_squared_error(test_data, test_predictions)
    #     rmse = np.sqrt(mse)
    #     mape = np.mean(np.abs((test_data - test_predictions) / test_data)) * 100

    #     print("MAE (Mean Absolute Error):", mae)
    #     print("MSE (Mean Squared Error):", mse)
    #     print("RMSE (Root Mean Squared Error):", rmse)
    #     print("MAPE (Mean Absolute Percentage Error):", mape)
    # 
    def display_metrics_matrix(self,mae, mse, rmse, mape):
        """
        Formats the evaluation metrics into a matrix-like format for display.

        Parameters:
        - mae: Mean Absolute Error
        - mse: Mean Squared Error
        - rmse: Root Mean Squared Error
        - mape: Mean Absolute Percentage Error

        Returns:
        - formatted_metrics: Formatted string containing the evaluation metrics.
        """
        formatted_metrics = f"{'Metric':<30}{'Value':<15}\n"
        formatted_metrics += "-" * 45 + "\n"
        formatted_metrics += f"{'MAE (Mean Absolute Error)':<30}{mae:<15.4f}\n"
        formatted_metrics += f"{'MSE (Mean Squared Error)':<30}{mse:<15.4f}\n"
        formatted_metrics += f"{'RMSE (Root Mean Squared Error)':<30}{rmse:<15.4f}\n"
        formatted_metrics += f"{'MAPE (Mean Absolute Percentage Error)':<30}{mape:<15.4f}\n"
        return formatted_metrics

    # def display_evaluation_metrics(self,test_data, test_predictions):
    #     from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
    #     mse = mean_squared_error(test_data, test_predictions)
    #     mae = mean_absolute_error(test_data, test_predictions)

    #     r2 = r2_score(test_data, test_predictions)
    #     rmse = np.sqrt(mse)
    #     mape = np.mean(np.abs((test_data - test_predictions) / test_data)) * 100

    #     print(f'Mean Squared Error (MSE): {mse}')
    #     print(f'Mean Absolute Error (MAE): {mae}')
    #     print(f'R-squared (R2): {r2}')
    #     print("RMSE (Root Mean Squared Error):", rmse)
    #     print("MAPE (Mean Absolute Percentage Error):", mape)
    # # def display_test_evaluation_metrics(self,test_data, test_predictions):
    # #     """
    #     Displays evaluation metrics for the test predictions.
        
    #     Parameters:
    #     - test_data: The test dataset with actual values.
    #     - test_predictions: Predictions made on the test set.
    #     """
    #     mae = mean_absolute_error(test_data, test_predictions)
    #     mse = mean_squared_error(test_data, test_predictions)
    #     rmse = np.sqrt(mse)
    #     mape = np.mean(np.abs((test_data - test_predictions) / test_data)) * 100

    #     print("MAE (Mean Absolute Error):", mae)
    #     print("MSE (Mean Squared Error):", mse)
    #     print("RMSE (Root Mean Squared Error):", rmse)
    #     print("MAPE (Mean Absolute Percentage Error):", mape)
    # def display_metrics_matrix(self,mae, mse, rmse, mape):
    #     """
    #     Formats the evaluation metrics into a matrix-like format for display.

    #     Parameters:
    #     - mae: Mean Absolute Error
    #     - mse: Mean Squared Error
    #     - rmse: Root Mean Squared Error
    #     - mape: Mean Absolute Percentage Error

    #     Returns:
    #     - formatted_metrics: Formatted string containing the evaluation metrics.
    #     """
    #     formatted_metrics = f"{'Metric':<30}{'Value':<15}\n"
    #     formatted_metrics += "-" * 45 + "\n"
    #     formatted_metrics += f"{'MAE (Mean Absolute Error)':<30}{mae:<15.4f}\n"
    #     formatted_metrics += f"{'MSE (Mean Squared Error)':<30}{mse:<15.4f}\n"
    #     formatted_metrics += f"{'RMSE (Root Mean Squared Error)':<30}{rmse:<15.4f}\n"
    #     formatted_metrics += f"{'MAPE (Mean Absolute Percentage Error)':<30}{mape:<15.4f}\n"
    #     return formatted_metrics
 
    def generate_test_prediction_report(self, fitted_model, selected_column):
        # Create a new window for the test prediction report
        test_report_window = QDialog(self)
        test_report_window.setWindowTitle("Test Prediction Report")
        if self.parent().test_data is None:
            QMessageBox.warning(self, "Test data is empty", "Please split the data first.")
            return
        selected_column = self.columnSelector.currentText()
    
        # Get test data
        test_data = self.parent().test_data[selected_column].astype(float)
        train_data = self.parent().train_data[selected_column].astype(float)
        test_predictions = self.generate_test_predictions(test_data, fitted_model,train_data)

        # Set a fixed size for the window
        test_report_window.setFixedSize(800, 600)

        # Create a layout for the test prediction report window
        test_report_layout = QVBoxLayout(test_report_window)

        # Add heading to the report
        heading_label = QLabel("======== Test Prediction Report ===========")
        heading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        test_report_layout.addWidget(heading_label)

        # Create a scroll area for the report content
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        test_report_layout.addWidget(scroll_area)

        # Create a widget to hold the contents of the scroll area
        scroll_contents = QWidget()
        scroll_layout = QVBoxLayout(scroll_contents)
        scroll_area.setWidget(scroll_contents)

        # Generate predictions for the test set
        test_predictions = self.generate_test_predictions(test_data, fitted_model,train_data)

        # Plot test predictions
        self.plot_test_predictions(test_data, selected_column, test_predictions)
        test_pred_plot = plt.gcf().canvas
        test_pred_plot.setMinimumSize(600, 400)  # Set minimum size for the plot canvas
        scroll_layout.addWidget(test_pred_plot)

        # Plot test prediction errors
        self.plot_test_predictions_errors(test_data, test_predictions)
        error_plot = plt.gcf().canvas
        error_plot.setMinimumSize(600, 400)  # Set minimum size for the plot canvas
        scroll_layout.addWidget(error_plot)

        # Plot magnitude-residual relationship
        self.plot_magnitude_residual_relationship(test_data, test_predictions)
        mag_residual_plot = plt.gcf().canvas
        mag_residual_plot.setMinimumSize(600, 400)  # Set minimum size for the plot canvas
        scroll_layout.addWidget(mag_residual_plot)

        # Display evaluation metrics
        evaluation_metrics_label = QLabel("Evaluation Metrics:")
        scroll_layout.addWidget(evaluation_metrics_label)

        mae, mse, rmse, mape = self.calculate_evaluation_metrics(test_data, test_predictions)
        metrics_text = QTextEdit()
        metrics_text.setReadOnly(True)
        metrics_text.setMinimumSize(600, 100)
        metrics_text.setText(self.display_metrics_matrix(mae, mse, rmse, mape))
        scroll_layout.addWidget(metrics_text)

        # Create a button to save report as PDF
        save_pdf_button = QPushButton("Save Report as PDF")
        save_pdf_button.clicked.connect(lambda: self.saveTestPredictionReportAsPDF(test_report_window, fitted_model, test_data, selected_column))
        test_report_layout.addWidget(save_pdf_button)

        # Ensure the scroll area scrolls down to the bottom
        scroll_area.verticalScrollBar().setValue(scroll_area.verticalScrollBar().maximum())

        # Show the test prediction report window
        test_report_window.exec()

    def calculate_evaluation_metrics(self, test_data, test_predictions):
        """
        Calculates evaluation metrics for the test predictions.

        Parameters:
        - test_data: The test dataset with actual values.
        - test_predictions: Predictions made on the test set.

        Returns:
        - mae: Mean Absolute Error
        - mse: Mean Squared Error
        - rmse: Root Mean Squared Error
        - mape: Mean Absolute Percentage Error
        """
        mae = mean_absolute_error(test_data, test_predictions)
        mse = mean_squared_error(test_data, test_predictions)
        rmse = np.sqrt(mse)
        mape = np.mean(np.abs((test_data - test_predictions) / test_data)) * 100
        return mae, mse, rmse, mape

    def saveTestPredictionReportAsPDF(self, test_report_window, fitted_model, test_data, selected_column):
        # Get the file path for saving
        filename = f"TSA_{os.path.basename(self.parent().file_path).split('.')[0]}_Test_Prediction_Report.pdf"
        file_path = os.path.join(os.getcwd(), filename)
        train_data = self.parent().train_data[selected_column].astype(float)
        test_predictions = self.generate_test_predictions(test_data,fitted_model,train_data)

        # Create a PDF canvas
        with PdfPages(file_path) as pdf:
            # Add heading to the PDF
            heading_text = "======== Test Prediction Report ==========="
            pdf.savefig()
            plt.clf()  # Clear the current figure

            # Add heading to the PDF
            plt.text(0.5, 0.9, heading_text, ha='center', va='center', fontsize=16)
            pdf.savefig()
            plt.clf()  # Clear the current figure

            # Plot test predictions
            self.plot_test_predictions(test_data, test_predictions)
            pdf.savefig()
            plt.close()  # Close the figure after saving

            # Plot test prediction errors
            self.plot_test_predictions_errors(test_data, test_predictions)
            pdf.savefig()
            plt.close()  # Close the figure after saving

            # Plot magnitude-residual relationship
            self.plot_magnitude_residual_relationship(test_data, test_predictions)
            pdf.savefig()
            plt.close()  # Close the figure after saving

            # Display evaluation metrics matrix
            mae, mse, rmse, mape = self.calculate_evaluation_metrics(test_data, test_predictions)
            metrics_matrix = self.display_metrics_matrix(mae, mse, rmse, mape)
            plt.text(0.1, 0.5, metrics_matrix, ha='left', va='center')
            pdf.savefig()
            plt.close()  # Close the figure after saving

        # Show notification
        QMessageBox.information(test_report_window, "PDF Saved Successfully", f"PDF saved successfully at: {file_path}")

        # Open the saved PDF file
        try:
            subprocess.Popen(["xdg-open", file_path])  # Linux
        except:
            try:
                subprocess.Popen(["open", file_path])  # macOS
            except:
                subprocess.Popen(["start", "", file_path], shell=True)  # Windows

    def createManualInputGroup(self):
        layout = QVBoxLayout(self.manualTab)
  

        self.non_seasonal_group = self.create_non_seasonal_group()
        self.seasonal_group = self.create_seasonal_group()
        self.non_seasonal_collapsible = CollapsibleSection("Non-Seasonal")
        self.non_seasonal_collapsible.content_layout.addWidget(self.non_seasonal_group)
        self.non_seasonal_collapsible.setChecked(True)
        self.seasonal_collapsible = CollapsibleSection("Seasonal")
        self.seasonal_collapsible.content_layout.addWidget(self.seasonal_group)
        self.seasonal_collapsible.setChecked(False)

        self.additional_options_group = self.create_additional_options_group()
        self.additional_options_collapsible = CollapsibleSection("Additional Options")
        self.additional_options_collapsible.content_layout.addWidget(self.additional_options_group)
        self.additional_options_collapsible.setChecked(False)
        self.columnSelectorLabel = QLabel("Select Time Series Column:")
        self.columnSelector = QComboBox()
        if self.dataframe is not None:
            self.columnSelector.addItems(self.dataframe.columns)
        elif self.parent().train_data is not None:
            self.columnSelector.addItems(self.parent().train_data.columns)
        elif self.parent().test_data is not None:
            self.columnSelector.addItems(self.parent().test_data.columns)
     


        self.datasetSelectorLabel = QLabel("Select Dataset:")
        self.datasetSelector = QComboBox()
        if self.dataframe is not None:
            self.datasetSelector.addItem("Actual Set")
        if self.parent().train_data is not None:
            self.datasetSelector.addItem("Train Set")
        if self.parent().test_data is not None:
            self.datasetSelector.addItem("Test Set")

        self.importBestParamsButton = QPushButton("Import Recommended Parameters")
        self.importBestParamsButton.setIcon(QIcon('images/import.ico'))  # Setting button icon
        self.importBestParamsButton.setToolTip(
            "Click to import best parameters from ARIMA model")  # Tooltip for button
        self.importBestParamsButton.clicked.connect(self.importBestParameters)
        layout.addWidget(self.importBestParamsButton)  
        layout.addWidget(self.columnSelectorLabel)  
        layout.addWidget(self.columnSelector)  
        layout.addWidget(self.datasetSelectorLabel)
        layout.addWidget(self.datasetSelector)
        layout.addWidget(self.non_seasonal_collapsible)
        layout.addWidget(self.seasonal_collapsible)
        layout.addWidget(self.additional_options_collapsible)

    def create_non_seasonal_group(self):
        group = QGroupBox("Non-Seasonal Parame0ters")
        layout = QGridLayout(group)

        self.pLineEdiM = self.create_combobox_with_range(0, 5)
        self.dLineEditM = self.create_combobox_with_range(0, 2)
        self.qLineEditM = self.create_combobox_with_range(0, 5)
        layout.addWidget(QLabel("p:"), 0, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.pLineEdiM,0,1)
        layout.addWidget(QLabel("d:") ,1, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.dLineEditM,1, 1)
        layout.addWidget(QLabel("q:"), 2, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.qLineEditM,2,1)

        group.setLayout(layout)
        return group
    def print_test_dataset_columns(self):
        """
        Prints out the columns of the test dataset.
        """
        if self.parent().test_data is None:
            print("Test dataset is not available.")
        else:
            print("Columns of the test dataset:")
            print(self.parent().test_data.columns)
    def create_seasonal_group(self):
        self.startPSeasonalLineEdit = self.create_combobox_with_range(0, 2,default_value=0)
        self.dSeasonalLineEdit = self.create_combobox_with_range(0, 1,default_value=0)
        self.startQSeasonalLineEdit = self.create_combobox_with_range(0, 1,default_value=0)
        self.mLineEdit = self.create_combobox_with_range(3, 12,default_value=3)

        group = QGroupBox("Seasonal Parameters")
        layout = QGridLayout()

        layout.addWidget(QLabel("P:"), 0, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.startPSeasonalLineEdit, 0, 1)

        layout.addWidget(QLabel("D:"), 1, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.dSeasonalLineEdit, 1, 1)
  

        layout.addWidget(QLabel("Q:"), 2, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.startQSeasonalLineEdit, 2, 1)


        layout.addWidget(QLabel("Seasonal Period (m):"), 3, 0, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.mLineEdit, 3, 1)

        group.setLayout(layout)
        return group
 
        
    def create_additional_options_group(self):
        group = QGroupBox("Additional Options")
        layout = QFormLayout(group)

        # Create widgets for additional options
        checkbox_labels = ["Measurement Error", "Time-Varying Regression", "MLE Regression",
                   "Simple Differencing", "Enforce Stationarity", "Enforce Invertibility",
                   "Hamilton Representation", "Concentrate Scale", "Use Exact Diffuse"]

        checkboxes = [QCheckBox(label) for label in checkbox_labels]
        for checkbox in checkboxes:
          layout.addRow(checkbox)
        self.measurement_error = checkboxes[0].isChecked()
        self.time_varying_regression = checkboxes[1].isChecked()
        self.mle_regression = checkboxes[2].isChecked()
        self.simple_differencing = checkboxes[3].isChecked()
        self.enforce_stationarity = checkboxes[4].isChecked()
        self.enforce_invertibility = checkboxes[5].isChecked()
        self.hamilton_representation = checkboxes[6].isChecked()
        self.concentrate_scale = checkboxes[7].isChecked()
        self.use_exact_diffuse = checkboxes[8].isChecked()
            # Trend options as QComboBox
        self.trendComboBox = QComboBox()
        self.trendComboBox.addItems(['n', 'c', 't', 'ct'])
        layout.addRow("Trend:", self.trendComboBox)
        self.trendOffsetLineEdit = QLineEdit("1")
        layout.addRow("Trend Offset:", self.trendOffsetLineEdit)

    # # Dates, Frequency, and Missing
    #     selected_column_name = self.columnSelector.currentText()
    #     selected_column = self.dataframe[selected_column_name]
    #     if isinstance(selected_column.index, pd.DatetimeIndex):
    #      layout.addWidget(QLabel("Dates:"), 2, 0)
    #      self.datesLineEdit = QLineEdit(selected_column.index[0].strftime('%Y-%m-%d'))
    #      layout.addWidget(self.datesLineEdit, 2, 1)

    #     # Infer frequency
    #      freq = selected_column.index.inferred_freq
    #      if freq:
    #         layout.addWidget(QLabel("Frequency:"), 2, 2)
    #         self.freqLineEdit = QLineEdit(freq)
    #         layout.addWidget(self.freqLineEdit, 2, 3)
    #     else:
    #      layout.addWidget(QLabel("No Dates Available"), 2, 0)

    #     layout.addWidget(QLabel("Missing:"), 2, 4)
    #     self.missingLineEdit = QLineEdit(str(selected_column.isna().sum()))  # Convert to str to display
    #     layout.addWidget(self.missingLineEdit, 2, 5)


        group.setLayout(layout)
        return group

    def importBestParameters(self):
        if not self.parent().best_params:
            QMessageBox.information(self, "Import Recommended Parameters",
                                    'No Recommended parameters available. Please go to the ARIMA -> "Grid Search" menu to generate recommended parameters.')
            return


        self.pLineEdiM.setCurrentText(str(self.parent().best_params.get('p', '')))
        self.dLineEditM.setCurrentText(str(self.parent().best_params.get('d', '')))
        self.qLineEditM.setCurrentText(str(self.parent().best_params.get('q', '')))
        self.startPSeasonalLineEdit.setCurrentText(str(self.parent().best_params.get('P', '')))
        self.dSeasonalLineEdit.setCurrentText(str(self.parent().best_params.get('D', '')))
        self.startQSeasonalLineEdit.setCurrentText(str(self.parent().best_params.get('Q', '')))
        self.mLineEdit.setCurrentText(str(self.parent().best_params.get('m', '')))      
    def create_combobox_with_range(self, start, end,default_value=0):
        combobox = QComboBox()
        combobox.setEditable(True)
        for i in range(start, end + 1):
            combobox.addItem(str(i))
        combobox.setCurrentText(str(default_value))  # Set default value

        # Connect the currentTextChanged signal to the custom slot
        combobox.currentTextChanged.connect(self.check_numeric_input)

        # Set size policy to expand horizontally and have a fixed vertical size
        combobox.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        combobox.setMinimumWidth(100)  # Set minimum width

        return combobox

    def check_numeric_input(self, text):
        if text.strip() == "":
            # If the entered text is empty, do nothing
            return

        try:
            # Attempt to convert the entered text to a numeric value
            float(text)  # Try to convert to float

        except ValueError:
            # If conversion fails, display an error message
            QMessageBox.critical(self, "Error", "Please enter a valid numeric value.")

    def findBestArimaParameters(self):
        
        self.iterationLogTextEdit.clear()
        selected_column = self.columnSelector.currentText()
        series = None

        if self.datasetSelector.currentText() == "Actual Set":
         series = self.dataframe[selected_column]
        elif self.datasetSelector.currentText() == "Train Set":
         series = self.parent().train_data[selected_column]
        elif self.datasetSelector.currentText() == "Test Set":
         series = self.parent().test_data[selected_column]

    # Handle missing values
        series.dropna(inplace=True)  # Drop rows with missing values

    # Check if there are missing values after dropping
        if series.isnull().any():
         QMessageBox.critical(self, "Error", "Missing values still exist in the time series data after preprocessing.")
         return

    # Ensure the series is in datetime format
        if not np.issubdtype(series.index.dtype, np.datetime64):
         QMessageBox.critical(self, "Error", "The index of the time series data must be in datetime format.")
         return

        sys.stdout = EmittingStream(self.iterationLogTextEdit)

        self.iterationLogTextEdit.clear()
        p_text = self.pLineEdiM.currentText()
        d_text = self.dLineEditM.currentText()
        q_text = self.qLineEditM.currentText()
        P_text = self.startPSeasonalLineEdit.currentText()
        D_text = self.dSeasonalLineEdit.currentText()
        Q_text = self.startQSeasonalLineEdit.currentText()
        m_text = self.mLineEdit.currentText()
        if not p_text or not d_text or not q_text or not P_text or not Q_text or not m_text:
            QMessageBox.warning(self, "Input Error", "Please fill in all manual input parameters.")
            return

        p = int(p_text)
        d = int(d_text)
        q = int(q_text)
        P = int(P_text)
        D = int(D_text)
        Q = int(Q_text)
        m = int(m_text)
        if self.non_seasonal_collapsible.isChecked():
            p_text = self.pLineEdiM.currentText()
            d_text = self.dLineEditM.currentText()
            q_text = self.qLineEditM.currentText()

            if not p_text or not d_text or not q_text:
                QMessageBox.warning(self, "Input Error", "Please fill in all manual input parameters.")
                return
            p = int(p_text)
            d = int(d_text)
            q = int(q_text)
            results_text = f"Selected SARIMA parameters are:\n(p={p}, d={d}, q={q})."

        if self.seasonal_collapsible.isChecked():
            p_text = self.pLineEdiM.currentText()
            d_text = self.dLineEditM.currentText()
            q_text = self.qLineEditM.currentText()
            P_text = self.startPSeasonalLineEdit.currentText()
            D_text = self.dSeasonalLineEdit.currentText()
            Q_text = self.startQSeasonalLineEdit.currentText()
            m_text = self.mLineEdit.currentText()
            if not p_text or not d_text or not q_text or not P_text or not Q_text or not m_text:
                QMessageBox.warning(self, "Input Error", "Please fill in all manual input parameters.")
                return

            p = int(p_text)
            d = int(d_text)
            q = int(q_text)
            P = int(P_text)
            D = int(D_text)
            Q = int(Q_text)
            m = int(m_text)
            results_text = f"Selected SARIMA parameters from (Grid Search) are:\n(p={p}, d={d}, q={q})(P={P}, D={D}, Q={Q})[m={m}]."

        if self.seasonal_collapsible.isChecked() and self.non_seasonal_collapsible.isChecked():
            p_text = self.pLineEdiM.currentText()
            d_text = self.dLineEditM.currentText()
            q_text = self.qLineEditM.currentText()
            P_text = self.startPSeasonalLineEdit.currentText()
            D_text = self.dSeasonalLineEdit.currentText()
            Q_text = self.startQSeasonalLineEdit.currentText()
            m_text = self.mLineEdit.currentText()
            if not p_text or not d_text or not q_text or not P_text or not Q_text or not m_text:
                QMessageBox.warning(self, "Input Error", "Please fill in all manual input parameters.")
                return

            p = int(p_text)
            d = int(d_text)
            q = int(q_text)
            P = int(P_text)
            D = int(D_text)
            Q = int(Q_text)
            m = int(m_text)
            results_text = f"Selected SARIMA parameters from (Grid Search) are:\n(p={p}, d={d}, q={q})(P={P}, D={D}, Q={Q})[m={m}]."
        self.iterationLogTextEdit.clear()
        self.iterationLogTextEdit.append("\n" + results_text) 
     
        self.p = p
        self.d = d
        self.q = q
        self.P = P
        self.D = D
        self.Q = Q
        self.m = m  
        
    def create_dropdown(self, options):
        dropdown = QComboBox()
        dropdown.addItems(options)

        # Set size policy to expand horizontally and have a fixed vertical size
        dropdown.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        dropdown.setMinimumWidth(100)  # Set minimum width

        return dropdown

    def create_checkbox(self, text, checked=False):
        checkbox = QCheckBox(text)
        checkbox.setChecked(checked)

        # Set size policy to expand horizontally and have a fixed vertical size
        checkbox.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        return checkbox

class SplitDatasetDialog(QDialog):
    def __init__(self, dataframe, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Split Dataset")
        self.setWindowIcon(QIcon('images/split_dataset.ico'))
        self.setWindowFlag(Qt.WindowType.WindowContextHelpButtonHint, False)
        self.resize(500, 300)
        self.dataframe = dataframe

        layout = QVBoxLayout()

        # Tab widget for selecting splitting method
        self.tab_widget = QTabWidget()

        # Add tabs
        self.tab_percentage = QWidget()
        self.tab_date = QWidget()
        self.tab_data_points = QWidget()

        self.tab_widget.addTab(self.tab_percentage, "Split by Percentage")
        self.tab_widget.addTab(self.tab_date, "Split by Date")
        self.tab_widget.addTab(self.tab_data_points, "Split by Number of Data Points")

        layout.addWidget(self.tab_widget)

        # Input widgets for each tab
        self.setup_percentage_tab()
        self.setup_date_tab()
        self.setup_data_points_tab()

        # Buttons
        self.split_button = QPushButton("Split Dataset")
        self.split_button.clicked.connect(self.split_dataset)
        layout.addWidget(self.split_button)

        self.setLayout(layout)

        # Variables to store split datasets
        self.train_data = None
        self.test_data = None


        # Stylesheet for QDateEdit and QLineEdit
        self.setStyleSheet("""
                           
           QDateTime,QDateTimeEdit,QDate {
                border: 2px solid #edebe3; /* Blue border */
                border-radius: 7px;       /* Rounded corners */
                padding: 3px;              /* Padding inside the combobox */
                color: #0078D7;            /* Blue text */
                background-color: white;   /* White background */
            }

            QLineEdit {
                border: 2px solid #edebe3; /* Blue border */
                border-radius: 7px;       /* Rounded corners */
                padding: 3px;              /* Padding inside the combobox */
                color: #0078D7;            /* Blue text */
                background-color: white;   /* White background */
            }
        """)

    def setup_percentage_tab(self):
        layout = QVBoxLayout()

        self.training_set_label = QLabel("Train Set Size(%):")
        layout.addWidget(self.training_set_label)

        self.training_set_combobox = self.create_combobox_with_range(25, 100, 25)
        layout.addWidget(self.training_set_combobox)
        self.testing_set_label = QLabel("Test Set Size(%):")
        layout.addWidget(self.testing_set_label)
        # Combo box for test set size (read-only)
        self.test_set_combobox = self.create_combobox_with_range(75, 100, 25)
        self.test_set_combobox.setEnabled(False)
        layout.addWidget(self.test_set_combobox)

        self.training_set_combobox.currentTextChanged.connect(self.update_test_set_combobox)

        self.tab_percentage.setLayout(layout)

    def setup_date_tab(self):
        layout = QVBoxLayout()

        self.date_label = QLabel("Split Date:")
        layout.addWidget(self.date_label)

        # Find the minimum and maximum dates in the DataFrame
        min_date = self.dataframe.index.min()
        max_date = self.dataframe.index.max()

        # Check if min_date is not None
        if min_date is not None:
            # Set the minimum and maximum dates in the QDateTimeEdit widget
            min_datetime = QDateTime(datetime.datetime.combine(min_date, datetime.datetime.min.time()))
            max_datetime = QDateTime(datetime.datetime.combine(max_date, datetime.datetime.max.time()))

            self.date_edit = QDateTimeEdit()
            self.date_edit.setDisplayFormat("dd/MM/yyyy HH:mm:ss")
            self.date_edit.setCalendarPopup(True)
            self.date_edit.setMinimumDateTime(min_datetime)
            self.date_edit.setMaximumDateTime(max_datetime)
            self.date_edit.setDateTime(QDateTime.currentDateTime())  # Set default to current date-time
            layout.addWidget(self.date_edit)
        else:
            layout.addWidget(QLabel("No dates available in the DataFrame"))

        self.tab_date.setLayout(layout)




        self.tab_date.setLayout(layout)

    def setup_data_points_tab(self):
        layout = QVBoxLayout()

        self.data_points_label = QLabel("Number of Data Points(Train):")
        layout.addWidget(self.data_points_label)

        self.data_points_combobox = self.create_combobox_with_range(1, len(self.dataframe), 1)

        layout.addWidget(self.data_points_combobox)

        # Combo box for test set size (read-only)
        self.data__points_label_test = QLabel("Number of Data Points(Test):")
        layout.addWidget(self.data__points_label_test)
        self.test_set_combobox_points = self.create_combobox_with_range(len(self.dataframe)-1, len(self.dataframe), 1)
        self.test_set_combobox_points.setEnabled(False)
        layout.addWidget(self.test_set_combobox_points)
        self.data_points_combobox.currentTextChanged.connect(self.update_test_set_combobox)


        self.tab_data_points.setLayout(layout)

    def create_combobox_with_range(self, start, end, step):
        combobox = QComboBox()
        combobox.setEditable(True)
        for i in range(start, end + 1, step):
            combobox.addItem(str(i))

        # Set size policy to expand horizontally and have a fixed vertical size
        combobox.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        combobox.setMinimumWidth(100)  # Set minimum width

        return combobox

    def split_dataset(self):
        if self.tab_widget.currentIndex() == 0:  # Split by Percentage tab
            training_set_size = int(self.training_set_combobox.currentText())
            self.split_by_percentage(training_set_size)
        elif self.tab_widget.currentIndex() == 1:  # Split by Date tab
            split_date = self.date_edit.dateTime().toPyDateTime()
            self.split_by_date(split_date)
        elif self.tab_widget.currentIndex() == 2:  # Split by Data Points tab
            data_points = int(self.data_points_combobox.currentText())
            self.split_by_data_points(data_points)

    def split_by_percentage(self, training_set_size):
        num_rows = int(len(self.dataframe) * (training_set_size / 100))
        train_data = self.dataframe.head(num_rows)
        test_data = self.dataframe.tail(len(self.dataframe) - num_rows)
        self.set_split_data(train_data, test_data)

    def split_by_date(self, split_date):
        train_data = self.dataframe[self.dataframe.index < split_date]
        test_data = self.dataframe[self.dataframe.index >= split_date]
        self.set_split_data(train_data, test_data)

    def split_by_data_points(self, data_points):
        train_data = self.dataframe.head(data_points)
        test_data = self.dataframe.tail(len(self.dataframe) - data_points)
        self.set_split_data(train_data, test_data)

    def update_test_set_combobox(self):
        if self.tab_widget.currentIndex() == 0:  # Split by Percentage tab
            training_set_text = self.training_set_combobox.currentText()
            test_set_size = 100 - int(training_set_text)
            self.test_set_combobox.setCurrentText(str(test_set_size))
        elif self.tab_widget.currentIndex() == 2:  # Split by Data Points tab
            training_set_text = self.data_points_combobox.currentText()
            test_set_size = len(self.dataframe) - int(training_set_text)
            self.test_set_combobox_points.setCurrentText(str(test_set_size))

    def set_split_data(self, train_data, test_data):
        self.train_data = train_data
        self.test_data = test_data
        self.parent().train_data = self.train_data
        self.parent().test_data = self.test_data
        self.parent().actual_data = self.dataframe
        QMessageBox.information(self, "Success", f"Dataset split successful!\nTrain Data: {len(self.train_data)} rows\nTest Data: {len(self.test_data)} rows")
        self.accept()
class SplitDatasetDialogRNN(QDialog):
    def __init__(self, dataframe, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Split Dataset")
        self.setWindowIcon(QIcon('images/split_dataset.ico'))
        self.setWindowFlag(Qt.WindowType.WindowContextHelpButtonHint, False)
        self.resize(500, 300)
        self.dataframe = dataframe

        layout = QVBoxLayout()
        self.tab_widget = QTabWidget()
        self.tab_percentage = QWidget()
        self.tab_date = QWidget()
        self.tab_data_points = QWidget()

        self.tab_widget.addTab(self.tab_percentage, "Split by Percentage")
        self.tab_widget.addTab(self.tab_date, "Split by Date")
        self.tab_widget.addTab(self.tab_data_points, "Split by Number of Data Points")

        layout.addWidget(self.tab_widget)

        self.setup_percentage_tab()
        self.setup_date_tab()
        self.setup_data_points_tab()

        self.split_button = QPushButton("Split Dataset")
        self.split_button.clicked.connect(self.split_dataset)
        layout.addWidget(self.split_button)
        self.setLayout(layout)

        self.train_data = None
        self.validation_data = None
        self.test_data = None
        self.actual_data = self.dataframe  # Store the original dataframe
        
        # Stylesheet for QDateEdit and QLineEdit
        self.setStyleSheet("""
                            # Set global stylesheet for buttons and comboboxes
            QPushButton {
                background-color: #96b1c2; /* grey background */
                color: white;              /* White text */
                border-radius: 7px;       /* Rounded corners */
                padding: 6px;              /* Padding for text */
                font-weight: bold;         /* Bold font */
            }
            QPushButton:hover {
                background-color: #1b4972; /* Darker blue on hover */
            }
            QComboBox {
                border: 2px solid #edebe3; /* Blue border */
                border-radius: 7px;       /* Rounded corners */
                padding: 3px;              /* Padding inside the combobox */
                color: #0078D7;            /* Blue text */
                background-color: white;   /* White background */
            }
            QComboBox::drop-down {
                border: none;              /* No border for the dropdown button */


           QDateTime,QDateTimeEdit,QDate {
                border: 2px solid #edebe3; /* Blue border */
                border-radius: 7px;       /* Rounded corners */
                padding: 3px;              /* Padding inside the combobox */
                color: #0078D7;            /* Blue text */
                background-color: white;   /* White background */
            }

            QLineEdit {
                border: 2px solid #edebe3; /* Blue border */
                border-radius: 7px;       /* Rounded corners */
                padding: 3px;              /* Padding inside the combobox */
                color: #0078D7;            /* Blue text */
                background-color: white;   /* White background */
            }
        """)

    def setup_date_tab(self):
        layout = QVBoxLayout()
        self.date_label = QLabel("Select Split Date:")
        layout.addWidget(self.date_label)

        # Create a date picker for selecting the split date
        self.date_edit = QDateTimeEdit()
        self.date_edit.setDisplayFormat("dd/MM/yyyy")
        self.date_edit.setCalendarPopup(True)
        
        # Ensure the date range is valid based on the DataFrame's index
        if isinstance(self.dataframe.index, pd.DatetimeIndex):
            min_date = self.dataframe.index.min().to_pydatetime()
            max_date = self.dataframe.index.max().to_pydatetime()
            self.date_edit.setMinimumDate(min_date)
            self.date_edit.setMaximumDate(max_date)
        else:
            self.date_edit.setEnabled(False)  # Disable if not datetime index
        
        layout.addWidget(self.date_edit)
        self.tab_date.setLayout(layout)
    def setup_data_points_tab(self):
        layout = QVBoxLayout()
        self.data_points_label = QLabel("Enter Number of Data Points for Training:")
        layout.addWidget(self.data_points_label)
        
        # Combo box to select the number of data points for training
        self.data_points_combobox = QComboBox()
        self.data_points_combobox.setEditable(True)
        
        max_points = len(self.dataframe)
        for i in range(1, max_points, 100):  # Adjust step size based on your dataset size
            self.data_points_combobox.addItem(str(i))
        
        layout.addWidget(self.data_points_combobox)
        
        # Validation data points label and combo box
        self.validation_points_label = QLabel("Enter Number of Data Points for Validation (15% of Train):")
        layout.addWidget(self.validation_points_label)
        self.validation_points_combobox = QComboBox()
        self.validation_points_combobox.setEditable(True)
        
        layout.addWidget(self.validation_points_combobox)
        
        # Test data points label and combo box
        self.test_points_label = QLabel("Enter Number of Data Points for Test (Remaining after Train and Validation):")
        layout.addWidget(self.test_points_label)
        self.test_points_combobox = QComboBox()
        self.test_points_combobox.setEditable(True)
        
        layout.addWidget(self.test_points_combobox)
        
        self.tab_data_points.setLayout(layout)

        # Connect change signal of training data points combo box to a custom slot to update validation and test combo boxes
        self.data_points_combobox.currentTextChanged.connect(self.update_validation_and_test_comboboxes)

    def update_validation_and_test_comboboxes(self):
        train_points = int(self.data_points_combobox.currentText())
        max_points = len(self.dataframe)
        validation_points = int(0.15 * train_points)  # 15% of training data
        remaining_points = max_points - train_points
        test_points = remaining_points   # Remaining data after allocating for validation

        # Clear existing items and update validation points combo box
        self.validation_points_combobox.clear()
        self.validation_points_combobox.addItem(str(validation_points))

        # Clear existing items and update test points combo box
        self.test_points_combobox.clear()
        self.test_points_combobox.addItem(str(test_points))

    def setup_percentage_tab(self):
        layout = QVBoxLayout()

        # Train set size
        train_layout = QHBoxLayout()
        self.training_set_label = QLabel("Train Set Size (%):")
        self.training_set_combobox = self.create_combobox_with_range(70, 80, 5)
        train_layout.addWidget(self.training_set_label)
        train_layout.addWidget(self.training_set_combobox)
        layout.addLayout(train_layout)

        # Validation set size
        validation_layout = QHBoxLayout()
        self.validation_set_label = QLabel("Validation Set Size (%):")
        self.validation_set_combobox = self.create_combobox_with_range(15, 25, 5)
        validation_layout.addWidget(self.validation_set_label)
        validation_layout.addWidget(self.validation_set_combobox)
        layout.addLayout(validation_layout)

        # Test set size (automatically calculated, not editable)
        test_layout = QHBoxLayout()
        self.test_set_label = QLabel("Test Set Size (%):")
        self.test_set_combobox = QComboBox()
        self.test_set_combobox.setEditable(True)
        test_layout.addWidget(self.test_set_label)
        test_layout.addWidget(self.test_set_combobox)
        layout.addLayout(test_layout)

        self.tab_percentage.setLayout(layout)

        self.training_set_combobox.currentIndexChanged.connect(self.update_test_set_size)
        self.validation_set_combobox.currentIndexChanged.connect(self.update_test_set_size)
        self.update_test_set_size()

    def create_combobox_with_range(self, start, end, step):
        combobox = QComboBox()
        combobox.setEditable(True)
        for i in range(start, end + 1, step):
            combobox.addItem(str(i))
        return combobox

    def update_test_set_size(self):
        try:
            train_size = int(self.training_set_combobox.currentText())
            validation_size = int(self.validation_set_combobox.currentText())
            test_size = 100 - train_size 
            self.test_set_combobox.clear()
            self.test_set_combobox.addItem(str(test_size))
        except Exception as e:
            print(f"Error updating test set size: {e}")
    def split_by_percentage(self, train_percent, val_percent_of_train):
        total_samples = len(self.dataframe)
        train_size = int(total_samples * train_percent / 100)  # Convert percentage to fraction
        val_size = int(train_size * val_percent_of_train / 100)  # Convert percentage to fraction

        # Recompute train_size to exclude the validation set from the original train set
        train_size -= val_size

        # Slice the dataframe to create training, validation, and testing sets
        self.train_data = self.dataframe.iloc[:train_size]
        self.validation_data = self.dataframe.iloc[train_size:train_size + val_size]
        self.test_data = self.dataframe.iloc[train_size + val_size:]

        self.show_split_results()
    def split_dataset(self):
        if self.tab_widget.currentIndex() == 0:
            train_percent = int(self.training_set_combobox.currentText())
            val_percent_of_train = int(self.validation_set_combobox.currentText())
            self.split_by_percentage(train_percent, val_percent_of_train)
        elif self.tab_widget.currentIndex() == 1:
            # Pass the QDateTime object directly
            self.split_by_date(self.date_edit.dateTime())
        elif self.tab_widget.currentIndex() == 2:
            train_points = int(self.data_points_combobox.currentText())
            validation_points = int(self.validation_points_combobox.currentText())
            self.split_by_data_points(train_points, validation_points)
        if self.parent() is not None:
            self.parent().train_data = self.train_data
            self.parent().validation_data = self.validation_data
            self.parent().test_data = self.test_data
            self.parent().actual_data = self.dataframe

    def show_split_results(self):
        QMessageBox.information(self, "Success", f"Dataset split successful!\nTrain Data: {len(self.train_data)} rows\nValidation Data: {len(self.validation_data)} rows\nTest Data: {len(self.test_data)} rows")
        self.accept()
    
    def split_by_date(self, qdatetime):
        # Convert QDateTime to a pandas-compatible datetime (numpy datetime64)
        # Here, we include the time in the conversion process
        split_datetime = pd.to_datetime(qdatetime.toString("yyyy-MM-dd hh:mm:ss"))

        # Ensure the index is in datetime format if it's not already
        if not isinstance(self.dataframe.index, pd.DatetimeIndex):
            self.dataframe.index = pd.to_datetime(self.dataframe.index)

        # Filter the dataset based on the datetime
        mask = self.dataframe.index < split_datetime
        train_data = self.dataframe.loc[mask]
        remaining_data = self.dataframe.loc[~mask]

        # Split the remaining data equally for validation and testing
        split_index = len(remaining_data) // 2
        self.validation_data = remaining_data.iloc[:split_index]
        self.test_data = remaining_data.iloc[split_index:]

        self.train_data = train_data
        self.show_split_results()

    def split_by_data_points(self, train_points, validation_points):
        if train_points + validation_points > len(self.dataframe):
            QMessageBox.warning(self, "Error", "Sum of training and validation points exceeds total data points.")
            return

        self.train_data = self.dataframe.iloc[:train_points]
        self.validation_data = self.dataframe.iloc[train_points:train_points + validation_points]
        self.test_data = self.dataframe.iloc[train_points + validation_points:]

        self.show_split_results()



class ConfigureRNN(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Univariate RNN")
        icon_path = os.path.abspath('images/configure_icon.ico')
        self.setWindowIcon(QIcon(icon_path))
        self.setup_ui()
        self.setStyleSheet("""
            QPushButton {
                background-color: #96b1c2; /* grey background */
                color: white;              /* White text */
                border-radius: 7px;       /* Rounded corners */
                padding: 6px;              /* Padding for text */
                font-weight: bold;         /* Bold font */
            }
            QPushButton:hover {
                background-color: #1b4972; /* Darker blue on hover */
            }
            QLineEdit {
                border: 2px solid #edebe3;
                border-radius: 7px;
                padding: 3px;
                color: #0078D7;
                background-color: white;
            }""")

    def setup_ui(self):
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(10)
        self.resize(400, 300)

        self.window_size_input = QLineEdit()
        self.window_size_input.setValidator(QIntValidator(1, 100))
        self.window_size_input.setText("2")
        self.layout.addWidget(QLabel("Window Size:"))
        self.layout.addWidget(self.window_size_input)

        self.column_selection = QComboBox()
        self.column_selection.addItems([str(col) for col in self.parent().train_data.columns if self.parent().train_data[col].dtype in [np.float64, np.int64]])
        self.layout.addWidget(QLabel("Select Numeric Column:"))
        self.layout.addWidget(self.column_selection)

        self.num_units_input = QLineEdit()
        self.num_units_input.setValidator(QIntValidator(1, 512))
        self.num_units_input.setText("64")
        self.layout.addWidget(QLabel("Number of LSTM Units:"))
        self.layout.addWidget(self.num_units_input)

        self.lstm_activation = QComboBox()
        self.lstm_activation.addItems(['tanh', 'relu', 'sigmoid', 'linear'])
        self.layout.addWidget(QLabel("LSTM Activation Function:"))
        self.layout.addWidget(self.lstm_activation)

        self.dense_activation = QComboBox()
        self.dense_activation.addItems(['relu', 'sigmoid', 'tanh', 'linear'])
        self.layout.addWidget(QLabel("Dense Layer Activation Function:"))
        self.layout.addWidget(self.dense_activation)

        self.train_button = QPushButton("Train Model")
        self.train_button.clicked.connect(self.train_model)
        self.layout.addWidget(self.train_button)

        self.progress_bar = QProgressBar()
        self.layout.addWidget(self.progress_bar)
    
    def train_model(self):
        if not self.validate_data():
            return
        window_size = int(self.window_size_input.text())
        num_units = int(self.num_units_input.text())
        lstm_activation = self.lstm_activation.currentText()
        dense_activation = self.dense_activation.currentText()
        selected_column = self.column_selection.currentText()

        X_train, y_train = self.df_to_X_y(self.parent().train_data, window_size, selected_column)
        X_val, y_val = self.df_to_X_y(self.parent().validation_data, window_size, selected_column)
        X_test, y_test = self.df_to_X_y(self.parent().test_data, window_size, selected_column)

        self.model = self.build_model(window_size, num_units, lstm_activation, dense_activation)
        
        # Normalize training data
        X_train_norm, mids, hrange = self.normalize(X_train)

        # Apply the same normalization to the validation and test sets using the training parameters
        X_val_norm = (X_val - mids) / hrange
        X_test_norm = (X_test - mids) / hrange
        ######################################################################################################
        y_train_norm, y_mids, y_hrange = self.normalize(y_train)
        y_val_norm = (y_val - y_mids) / y_hrange
        y_test_norm = (y_test - y_mids) / y_hrange

        # Create a ProgressCallback instance
        progress_callback = ProgressCallback(self.progress_bar)
        progress_callback.on_epoch_end(0)  # Initialize progress bar to 0%

        # Pass the ProgressCallback instance as a callback during model training
        history = self.model.fit(X_train_norm, y_train_norm, validation_data=(X_val_norm, y_val_norm), epochs=10, callbacks=[progress_callback])

        test_predictions = self.model.predict(X_test_norm).flatten()
        self.generate_plots(y_test_norm, test_predictions)
        QMessageBox.information(self, "Training Complete", "Model training has completed successfully.")

    def build_model(self, window_size, num_units, lstm_activation, dense_activation):
        model = Sequential([
            InputLayer(input_shape=(window_size, 1)),
            LSTM(num_units, activation=lstm_activation),
            Dense(1, activation=dense_activation)
        ])
        model.compile(optimizer=Adam(), loss='mean_squared_error')
        return model
    def generate_plots(self, y_test, test_predictions):
        test_results = pd.DataFrame({
            'Test Predictions': test_predictions,
            'Actuals': y_test
        })
        test_results['Residuals'] = test_results['Actuals'] - test_results['Test Predictions']
        test_mae = mean_absolute_error(test_results['Actuals'], test_results['Test Predictions'])
        test_mse = mean_squared_error(test_results['Actuals'], test_predictions)
        test_rmse = np.sqrt(test_mse)

        dialog = QDialog(self)
        dialog.setWindowTitle("Univariate RNN Test Results")
        dialog.setMaximumSize(800, 800)  # Increased height to accommodate larger graphs
        dialog_layout = QVBoxLayout(dialog)

        # Create a frame for selected attributes
        attributes_frame = QFrame()
        attributes_layout = QGridLayout()
        attributes_frame.setLayout(attributes_layout)

        attributes = {
            "Window Size": self.window_size_input.text(),
            "Numeric Column": self.column_selection.currentText(),
            "Number of LSTM Units": self.num_units_input.text(),
            "LSTM Activation Function": self.lstm_activation.currentText(),
            "Dense Layer Activation Function": self.dense_activation.currentText()
        }

        for i, (label, value) in enumerate(attributes.items()):
            label_widget = QLabel(label + ":")
            value_widget = QLabel(value)
            attributes_layout.addWidget(label_widget, i, 0)
            attributes_layout.addWidget(value_widget, i, 1)

        dialog_layout.addWidget(attributes_frame)

        # Add spacer for separation
        dialog_layout.addSpacing(20)

        # Add heading for test results report
        heading_label = QLabel("======== Univariate RNN Test Results Report ===========")
        heading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dialog_layout.addWidget(heading_label)

        # Add scroll area for plots
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        dialog_layout.addWidget(scroll_area)

        # Add scroll contents
        scroll_contents = QWidget()
        scroll_layout = QVBoxLayout(scroll_contents)
        scroll_area.setWidget(scroll_contents)

        # Plot test predictions vs actuals
        self.plot_train_predictions_vs_actuals(test_results, percentage=98, test_predictions=test_predictions)
        plot_train_predictions = plt.gcf().canvas
        plot_train_predictions.setMinimumSize(600, 400)
        scroll_layout.addWidget(plot_train_predictions)

        # Plot residual relationships
        self.plot_train_residuals_relationship(test_results)
        plot_train_residuals = plt.gcf().canvas
        plot_train_residuals.setMinimumSize(600, 400)
        scroll_layout.addWidget(plot_train_residuals)

        # Plot residual histogram
        self.plot_train_residuals_histogram(test_results)
        plot_train_histogram = plt.gcf().canvas
        plot_train_histogram.setMinimumSize(600, 400)
        scroll_layout.addWidget(plot_train_histogram)

        # Add buttons for interaction
        dialog_layout.addWidget(scroll_area)
        test_button = QPushButton("Test Prediction", dialog)
        dialog_layout.addWidget(test_button)
        save_pdf_button = QPushButton("Save PDF", dialog)
        save_pdf_button.clicked.connect(lambda: self.save_plots_as_pdf(dialog, test_results, test_predictions=test_predictions))
        dialog_layout.addWidget(save_pdf_button)

        dialog.exec()


    def plot_train_residuals_relationship(self, train_results, figsize=(8, 6)):
        # Calculate squared residuals
        train_results['Residuals'] = (train_results['Actuals'] - train_results['Test Predictions'])
        train_results['Squared Residuals'] = (train_results['Actuals'] - train_results['Test Predictions'])**2
        mae = mean_absolute_error(train_results['Actuals'], train_results['Test Predictions'])
        mse = mean_squared_error(train_results['Actuals'], train_results['Test Predictions'])
        rmse = np.sqrt(mse)
        metrics_text = f"MAE: {mae:.2f}\nMSE: {mse:.2f}\nRMSE: {rmse:.2f}"

        plt.figure(figsize=figsize)
        sns.scatterplot(x=train_results['Actuals'], y=train_results['Squared Residuals'], alpha=0.5)
        plt.title('Magnitude-Residual Relationship')
        plt.xlabel('Actual Values')
        plt.ylabel('Squared Residuals')
        plt.grid(True)
        # Positioning the text, might need adjustment based on actual data range
        plt.text(0.01, 0.99, metrics_text, verticalalignment='top', horizontalalignment='left', transform=plt.gca().transAxes, fontsize=10, bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white', alpha=0.8))

    def plot_train_residuals_histogram(self, train_results, bins=20, figsize=(8, 6), include_kde=True):
        mae = mean_absolute_error(train_results['Actuals'], train_results['Test Predictions'])
        mse = mean_squared_error(train_results['Actuals'], train_results['Test Predictions'])
        rmse = np.sqrt(mse)
        metrics_text = f"MAE: {mae:.2f}\nMSE: {mse:.2f}\nRMSE: {rmse:.2f}"

        plt.figure(figsize=figsize)
        # Using 'kde' parameter from sns.histplot to include/exclude KDE
        sns.histplot(train_results['Residuals'], bins=bins, kde=include_kde, edgecolor='black', color='g', alpha=0.7)
        plt.title('Residuals')
        plt.xlabel('Residuals')
        plt.ylabel('Frequency')
        plt.text(0.99, 0.99, metrics_text, verticalalignment='top', horizontalalignment='right', transform=plt.gca().transAxes, fontsize=10, bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white', alpha=0.8))

    def plot_train_predictions_vs_actuals(self, train_results, percentage=10, figsize=(12, 6), test_predictions=None):
        num_entries = int(len(train_results) * (percentage / 100))
        start_index = max(0, len(train_results) - num_entries)
        
        # Calculate error metrics
        mae = mean_absolute_error(train_results['Actuals'][start_index:], test_predictions[start_index:])
        mse = mean_squared_error(train_results['Actuals'][start_index:], test_predictions[start_index:])
        rmse = np.sqrt(mse)
        metrics_text = f"MAE: {mae:.2f}\nMSE: {mse:.2f}\nRMSE: {rmse:.2f}"
        
        # Prepare a slice of the DataFrame for plotting
        plot_data = train_results.iloc[start_index:].reset_index()
        melted_data = pd.melt(plot_data, id_vars=['index'], value_vars=['Test Predictions', 'Actuals'])
        
        plt.figure(figsize=figsize)
        sns.lineplot(data=melted_data, x='index', y='value', hue='variable')
        plt.title(f'Predicted vs. Actual Values - Last {percentage}% of Data')
        plt.ylabel('Values')
        plt.xlabel('')
        plt.legend(title='Legend')
        plt.text(0.01, 0.99, metrics_text, verticalalignment='top', horizontalalignment='left', transform=plt.gca().transAxes, fontsize=10, bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='white', alpha=0.8))
    


    def normalize(self,data):
        """
        Normalizes the data to the range [-1, 1] based on the mid-range and half-range of maximum and minimum values.

        Parameters:
            data (np.array or pd.DataFrame): Input data to normalize.

        Returns:
            tuple: normalized data, mid-range values, half-range values.
        """
        if isinstance(data, pd.DataFrame):
            data = data.values

        if data.ndim == 1:
            data = data.reshape(-1, 1)
        
        normalized = np.zeros(data.shape)
        maxes = np.amax(data, axis=0)
        mins = np.amin(data, axis=0)
        mids = (maxes + mins) / 2
        hrange = (maxes - mins) / 2

        hrange[hrange == 0] = 1
        normalized = (data - mids) / hrange

        if data.shape[1] == 1:
            normalized = normalized.flatten()

        return normalized, mids, hrange

    def convert_to_list(self,vec):
        """
        Converts a DataFrame, ndarray, or an iterable to a list.

        Parameters:
            vec (iterable): Data to convert to a list.

        Returns:
            list: List representation of the input data.
        """
        try:
            if isinstance(vec, pd.DataFrame):
                return vec.iloc[:, 0].tolist()
            elif isinstance(vec, np.ndarray):
                return vec.flatten().tolist()
            else:
                return list(vec)
        except Exception as e:
            print('Error in function convert_to_list')
            print('Exception:', str(e))
            print('Argument type:', type(vec))
            print('End of error message')
    ######################################################################################################
    #Normalize the various splits

    def save_plots_as_pdf(self,dialog,test_results, test_predictions):
        filename = f"TSA_{os.path.basename(self.parent().file_path).split('.')[0]}_Test_Prediction_Report.pdf"
        file_path = os.path.join(os.getcwd(), filename)

        # Create a PDF canvas
        with PdfPages(file_path) as pdf:
            # Add heading to the PDF
            heading_text = "======== Test Prediction Report ==========="
            pdf.savefig()
            plt.clf()  # Clear the current figure

            # Add heading to the PDF
            plt.text(0.5, 0.9, heading_text, ha='center', va='center', fontsize=16)
            pdf.savefig()
            plt.clf()  # Clear the current figure

            # Plot test predictions
            self.plot_train_predictions_vs_actuals(test_results, percentage=98, test_predictions=test_predictions)
            pdf.savefig()
            plt.close()  # Close the figure after saving

            # Plot test prediction errors
            self.plot_train_residuals_relationship(test_results)
            pdf.savefig()
            plt.close()  # Close the figure after saving

            # Plot magnitude-residual relationship
            self.plot_train_residuals_histogram(test_results)
            pdf.savefig()
            plt.close()  # Close the figure after saving


        # Show notification
        QMessageBox.information(dialog, "PDF Saved Successfully", f"PDF saved successfully at: {file_path}")

        # Open the saved PDF file
        try:
            subprocess.Popen(["xdg-open", file_path])  # Linux
        except:
            try:
                subprocess.Popen(["open", file_path])  # macOS
            except:
                subprocess.Popen(["start", "", file_path], shell=True)  # Windows
 
    def df_to_X_y(self, df, window_size=1, column_name=None):
       
        try:
            df_as_np = df[column_name].to_numpy()
            X = []
            y = []
            for i in range(len(df_as_np) - window_size):
                #row = [[a] for a in df_as_np[i:i + window_size]]
                row = [a for a in df_as_np[i:i + window_size]]
                X.append(row)
                target = df_as_np[i + window_size]
                y.append(target)
            return np.array(X), np.array(y)
        except Exception as e:
            print("An error occurred:", e)
            return None,None

    def update_progress(self, epoch, logs=None):
        if logs is not None:
            progress = int((epoch / 10) * 100)
            self.progress_bar.setValue(progress)

    def validate_data(self):
        if self.parent().train_data is None or self.parent().validation_data is None:
            QMessageBox.warning(self, "Data Error", "Training or validation data not set.")
            return False
        return True


class ProgressCallback(Callback):
    def __init__(self, progress_bar):
        super().__init__()
        self.progress_bar = progress_bar

    def on_epoch_end(self, epoch, logs=None):
        # Update the progress bar based on the number of epochs
        if logs is not None:
            progress = int((epoch + 1) / 10 * 100)  # Assuming 10 epochs
            self.progress_bar.setValue(progress)