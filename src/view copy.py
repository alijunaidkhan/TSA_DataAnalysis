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
import cProfile
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget,QCheckBox
import os
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from PyQt6.QtCore import Qt, QUrl,QThread, pyqtSignal

from PyQt6.QtGui import QAction, QIcon,QFont,QColor,QPixmap,QStandardItem, QStandardItemModel, QDesktopServices
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QTabWidget, \
    QTableWidget,QMenu, QTableWidgetItem, QHBoxLayout, QLabel, QLineEdit, QGridLayout, QDialog, QGroupBox,\
    QRadioButton, QComboBox,QDialogButtonBox, QProgressBar,QFormLayout,QTextEdit,QAbstractItemView, QMessageBox, QButtonGroup, QDockWidget,QSpinBox, QSpacerItem, QSizePolicy
import pandas as pd
import zipfile
import os
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QDialogButtonBox, QMessageBox, QApplication

os.environ['QT_API'] = 'pyqt6'
matplotlib.use('QtAgg')

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pandas.plotting import lag_plot

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


    def __init__(self, controller):
        # Inside your View's __init__ method or a specific setup method

        """
        Initializes the View component.
        Args:
            controller (Controller): The controller instance for the view to communicate with.
        """



        super().__init__()
        self.thresholds_layout = QVBoxLayout()  # Initialize the layout
        self.comboBox2 = CheckableComboBox()
        self.controller = controller
        # Assuming this is done in the part of your code where UI components are initialized


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
        self.progressBar.setGeometry(50, 140, 200, 25)  # Adjust the size and position as needed
        self.progressBar.setMaximum(100)  # Set the maximum value of progress bar
        self.progressBar.hide()  # Initially hide the progress bar
        self.data_changed = False

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



# In your main window or wherever the subset button is defined
    def openSubsetDialog(self):
    # Check if data is loaded in the model
     if not self.comboBox2.get_checked_items():
        # Display a warning message if no columns are selected
        icon_path = os.path.abspath('images/subset_icon.svg')
        self.setWindowIcon(QIcon(icon_path))
        QMessageBox.warning(self, "No Columns Selected", "Please select at least one column before proceeding.")
        icon_path = os.path.abspath('images/bulb_icon.png')
        self.setWindowIcon(QIcon(icon_path))
        return
     if self.controller.model.data_frame is None:
        # Display a warning message if no data is loaded
        icon_path = os.path.abspath('images/subset_icon.svg')
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
        dataframe = self.controller.get_dataframe()  # Get the DataFrame from the controller
        dialog = SubsetDialog(column_ranges, dataframe, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            values = dialog.getValues()
            # Handle the values as needed
            print(values)  # Example usage


    def calculate_min_max_for_column(self, column):
     column_index = self.table_widget.columnCount()
     for i in range(self.table_widget.columnCount()):
        if self.table_widget.horizontalHeaderItem(i).text() == column:
            column_index = i
            break

     values = []
     for row in range(self.table_widget.rowCount()):
        item = self.table_widget.item(row, column_index)
        if item:
            try:
                value = float(item.text())  # Use float to accommodate decimal values
                values.append(value)
            except ValueError:
                continue  # Skip non-numeric values

     if values:
        return min(values), max(values)
     return 0, 0  # Return default min and max if no numeric values found


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
        subset_icon = QIcon('images/subset_icon.svg')  # Ensure the icon path is correct
        subset_action = QAction(subset_icon, "&Subset", self)
        subset_action.triggered.connect(self.openSubsetDialog)  # Connect the action to the method
        preprocess_menu.addAction(subset_action)

       # Create Resample action with an icon and add it to the Preprocess menu
        resample_icon = QIcon('images/resample_icon.svg')  # Ensure the icon path is correct
        resample_action = QAction(resample_icon, "&Resample", self)
        resample_action.triggered.connect(self.controller.open_resample_dialog)
        preprocess_menu.addAction(resample_action)



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
        self.table_widget.setRowCount(data_frame.shape[0])
        self.table_widget.setColumnCount(data_frame.shape[1])
        self.table_widget.setHorizontalHeaderLabels(data_frame.columns)

        # Allow editing of items in the table
        #self.table_widget.setEditTriggers(QAbstractItemView.AllEditTriggers)

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
 


        for row in range(data_frame.shape[0]):
            for col in range(data_frame.shape[1]):
                item = QTableWidgetItem(str(data_frame.iloc[row, col]))
                self.table_widget.setItem(row, col, item)

        self.table_widget.setUpdatesEnabled(True)  # Re-enable updates after batch processing
        self.initial_message_label.hide()


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
  

     
    def update_column_combobox(self, logical_index):
    
     column_name = self.table_widget.horizontalHeaderItem(logical_index).text()
     self.comboBox.clear()
     self.comboBox.addItem(column_name)

     # Clear previous items from comboBox2
    
##################################################################################################################

    def is_column_numeric(self, column_name):
  
     try:
        if column_name and hasattr(self, 'table_widget'):
            logical_index = -1
            for i in range(self.table_widget.columnCount()):
                if self.table_widget.horizontalHeaderItem(i).text() == column_name:
                    logical_index = i
                    break

            if logical_index != -1:
                column_data = [self.table_widget.item(row, logical_index).text()
                               for row in range(self.table_widget.rowCount()) if self.table_widget.item(row, logical_index)]

                for dtype in [int, float]:
                    try:
                        [dtype(value) for value in column_data if value.strip()]
                        return True  # Column is numeric
                    except ValueError:
                        continue

                return False  # Column is not numeric
     except Exception as e:
        print(f"An exception occurred: {e}")  # Or handle the exception as needed
        return False
    def onItemCheckStateChanged(self, item_text, is_checked):
    # Handle UI update here
     if is_checked:
        print(f"Show input fields for {item_text}")
        # Logic to show min/max input fields for item_text
     else:
        print(f"Hide input fields for {item_text}")
        # Logic to hide min/max input fields for item_text


#     def create_docked_widget(self):
#         """
#         Creates a docked widget with a red background central widget and three container widgets.
#         The 'column_selection_widget' contains a label, a combobox, and a button arranged horizontally.
#         The 'buttons_widget' contains a grid of six buttons.
#         The 'display_results_widget' contains a QTextEdit for displaying output.
#         """
#         docked_widget = QDockWidget("Property", self)
#         central_widget = QWidget()
#         central_widget.setObjectName("centralWidget")
#         central_widget.setStyleSheet("QWidget#centralWidget { background-color: #B22222; }")
#         central_layout = QVBoxLayout(central_widget)

#       # Create and setup the column_selection_widget
#         column_selection_widget = QWidget(central_widget)
#         column_selection_layout = QVBoxLayout(column_selection_widget)

# # First row layout for label, combobox, and refresh button
#         first_row_layout = QHBoxLayout()
#         label = QLabel("Header", column_selection_widget)
#         label.setStyleSheet("color: white; font-weight: bold;")
#         label.setFixedHeight(30)

#         self.comboBox = QComboBox(column_selection_widget)
#         self.comboBox.setObjectName("columnComboBox")
#         self.comboBox.setFixedHeight(30)
#         self.table_widget.horizontalHeader().sectionClicked.connect(self.update_column_combobox)

#         refresh_button = QPushButton("Refresh", column_selection_widget)
#         refresh_button.setObjectName("refreshButton")
#         refresh_button.setToolTip("Refresh the data and update column names.")
#         refresh_button.setFixedHeight(30)
# ############################################################################################################        
#         first_row_layout.addWidget(label, 1)
#         first_row_layout.addWidget(self.comboBox, 4)
#         first_row_layout.addWidget(refresh_button, 2)


# # Second row layout for the second ComboBox and its label
#         second_row_layout = QHBoxLayout()
#         label2 = QLabel("Subsets", column_selection_widget)
#         label2.setStyleSheet("color: white; font-weight: bold;")
#         label2.setFixedHeight(30)
#         self.comboBox2 = CheckableComboBox()
        
#         self.comboBox2.setObjectName("columnComboBox2")
#         self.comboBox2.setFixedHeight(30)
#         self.table_widget.horizontalHeader().sectionClicked.connect(self.update_column_combobox)
# ###############################################################################################################
#         unselect_button = QPushButton("Unselect", column_selection_widget)
#         unselect_button.setObjectName("unselectButton")
#         unselect_button.setToolTip("Unselect all columns.")
#         unselect_button.setFixedHeight(30)
#         unselect_button.clicked.connect(self.comboBox2.unselect_all)       
# ################################################################################
#         subset_button = QPushButton("Subset", column_selection_widget)
#         subset_button.setObjectName("subsetButton")
#         subset_button.setToolTip("Filter data into subsets based on selected columns and thresholds.")
#         subset_button.setFixedHeight(30)

# ###############################################################
#         second_row_layout.addWidget(label2,1)
#         second_row_layout.addWidget(self.comboBox2,4)
#         second_row_layout.addWidget(unselect_button, 2)

# ###############################################################
#         third_row_layout = QHBoxLayout()
#         third_row_layout.addWidget(subset_button)

# # Add first and second row layouts to the column_selection_layout
#         column_selection_layout.addLayout(first_row_layout)
#         column_selection_layout.addLayout(second_row_layout)
#         column_selection_layout.addLayout(third_row_layout)
       
#         # Create and setup the buttons_widget
#         buttons_widget = QWidget(central_widget)
#         buttons_layout = QGridLayout(buttons_widget)
#         self.buttons = {}
#         button_info = {
#     "Size": "Number of rows the column.",
#     "Type": "Data type of the column.",
#     "Missing": "Number of rows with missing values.",
#     "Statistics": "Basic statistics of the column.",  
# }

#         button_labels = ["Size", "Type", "Missing", "Statistics"]

# #self.buttons[label].clicked.connect(getattr(self.controller, f"calculate_{label.lower()}"))
#         for i, label in enumerate(button_labels):
#             button = QPushButton(label, buttons_widget)
#             button.setObjectName(f"{label.lower()}Button")
#             self.buttons[label] = button
#             self.buttons[label].setToolTip(button_info[label])
#             row, col = divmod(i, 2)
#             buttons_layout.addWidget(button, row, col)

#         # Create and setup the display_results_widget
#         display_results_widget = QWidget(central_widget)
#         display_results_layout = QVBoxLayout(display_results_widget)
#         self.output_display = QTextEdit(display_results_widget)
#         self.output_display.setReadOnly(True)
#         display_results_layout.addWidget(self.output_display)

#         # Add the container widgets to the central_layout
#         central_layout.addWidget(column_selection_widget, 3)
#         central_layout.addWidget(buttons_widget, 3)
#         central_layout.addWidget(display_results_widget, 4)

#         # Set the central widget as the docked widget's content
#         docked_widget.setWidget(central_widget)

#         # Add the docked widget to the main window
#         self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, docked_widget)

# ######################################################## trying Functionalities for docked widget#####################################################
#         refresh_button.clicked.connect(self.controller.update_column_names)
#         subset_button.clicked.connect(self.openSubsetDialog)

#         self.buttons["Size"].clicked.connect(self.controller.calculate_shape)
#         # Connect the "Type" button
#         self.buttons["Type"].clicked.connect(self.controller.calculate_dtype)
#         # Connect the "Statistics" button
#         self.buttons["Statistics"].clicked.connect(self.controller.calculate_statistics)
#         # Connect the "Missing"
#         self.buttons["Missing"].clicked.connect(self.controller.calculate_missing)
# ################################################################################################################
    # def create_docked_widget(self):
    #     docked_widget = QDockWidget("Property", self)
    #     central_widget = QWidget()
    #     central_widget.setObjectName("centralWidget")
    #     central_widget.setStyleSheet("QWidget#centralWidget { background-color: #B22222; }")
    #     central_layout = QVBoxLayout(central_widget)

    #     # Create and setup the column_selection_widget
    #     column_selection_widget = QWidget()
    #     column_selection_layout = QVBoxLayout(column_selection_widget)

    #     # First row layout for label, combobox, and refresh button
    #     first_row_layout = QHBoxLayout()
    #     label = QLabel("Header", column_selection_widget)
    #     label.setStyleSheet("color: white; font-weight: bold;")
    #     label.setFixedHeight(30)

    #     self.comboBox = QComboBox()
    #     self.comboBox.setObjectName("columnComboBox")
    #     self.comboBox.setFixedHeight(30)

    #     refresh_button = QPushButton("Refresh", column_selection_widget)
    #     refresh_button.setObjectName("refreshButton")
    #     refresh_button.setFixedHeight(30)

    #     first_row_layout.addWidget(label)
    #     first_row_layout.addWidget(self.comboBox)
    #     first_row_layout.addWidget(refresh_button)

    #     # Grid buttons setup
    #     buttons_widget = QWidget()
    #     buttons_layout = QGridLayout(buttons_widget)
    #     self.buttons = {}
    #     button_info = {
    #         "Size": "Number of rows the column.",
    #         "Type": "Data type of the column.",
    #         "Missing": "Number of rows with missing values.",
    #         "Statistics": "Basic statistics of the column.",  
    #     }

    #     button_labels = ["Size", "Type", "Missing", "Statistics"]
    #     for i, label in enumerate(button_labels):
    #         button = QPushButton(label, buttons_widget)
    #         button.setObjectName(f"{label.lower()}Button")
    #         self.buttons[label] = button
    #         self.buttons[label].setToolTip(button_info[label])
    #         row, col = divmod(i, 2)
    #         buttons_layout.addWidget(button, row, col)

    #     # Second row layout for the second ComboBox and its label
    #     second_row_layout = QHBoxLayout()
    #     label2 = QLabel("Subsets", column_selection_widget)
    #     label2.setStyleSheet("color: white; font-weight: bold;")
    #     label2.setFixedHeight(30)

    #     self.comboBox2 = CheckableComboBox()  # Instantiate without passing column_selection_widget
    #     self.comboBox2.setObjectName("columnComboBox2")
    #     self.comboBox2.setFixedHeight(30)

    #     unselect_button = QPushButton("Unselect", column_selection_widget)
    #     unselect_button.setObjectName("unselectButton")
    #     unselect_button.setFixedHeight(30)
    #     unselect_button.clicked.connect(self.comboBox2.unselect_all)

    #     subset_button = QPushButton("Subset", column_selection_widget)
    #     subset_button.setObjectName("subsetButton")
    #     subset_button.setFixedHeight(30)
    #     subset_button.clicked.connect(self.openSubsetDialog)

    #     second_row_layout.addWidget(label2)
    #     second_row_layout.addWidget(self.comboBox2)
    #     second_row_layout.addWidget(unselect_button)

    #     # Add first row and grid buttons to column_selection_layout
    #     column_selection_layout.addLayout(first_row_layout)
    #     column_selection_layout.addWidget(buttons_widget)

    #     # Add second row to column_selection_layout
    #     column_selection_layout.addLayout(second_row_layout)

    #     # Add subset button to column_selection_layout
    #     column_selection_layout.addWidget(subset_button)

    #     # Set column_selection_layout as the layout for column_selection_widget
    #     column_selection_widget.setLayout(column_selection_layout)

    #     # Create and setup the display_results_widget
    #     display_results_widget = QWidget()
    #     display_results_layout = QVBoxLayout(display_results_widget)
    #     self.output_display = QTextEdit()
    #     self.output_display.setReadOnly(True)
    #     display_results_layout.addWidget(self.output_display)

    #     # Add all widgets to central_layout
    #     central_layout.addWidget(column_selection_widget)
    #     central_layout.addWidget(display_results_widget)

    #     # Set the central widget as the docked widget's content and add it to the main window
    #     docked_widget.setWidget(central_widget)
    #     self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, docked_widget)

    #     # Connect signals to slots
    #     refresh_button.clicked.connect(self.controller.update_column_names)
    #     self.buttons["Size"].clicked.connect(self.controller.calculate_shape)
    #     self.buttons["Type"].clicked.connect(self.controller.calculate_dtype)
    #     self.buttons["Missing"].clicked.connect(self.controller.calculate_missing)
    #     self.buttons["Statistics"].clicked.connect(self.controller.calculate_statistics)

    # def create_docked_widget(self):
    #     docked_widget = QDockWidget("Property", self)
    #     central_widget = QWidget()
    #     central_widget.setObjectName("centralWidget")
    #     central_widget.setStyleSheet("QWidget#centralWidget { background-color: #B22222; }")
    #     central_layout = QVBoxLayout(central_widget)

    #     # Create and setup the column_selection_widget with the first row layout
    #     column_selection_widget = QWidget()
    #     column_selection_layout = QVBoxLayout(column_selection_widget)

    #     first_row_layout = QHBoxLayout()
    #     label = QLabel("Header", column_selection_widget)
    #     label.setStyleSheet("color: white; font-weight: bold;")
    #     label.setFixedHeight(30)

    #     self.comboBox = QComboBox()
    #     self.comboBox.setObjectName("columnComboBox")
    #     self.comboBox.setFixedHeight(30)

    #     refresh_button = QPushButton("Refresh", column_selection_widget)
    #     refresh_button.setObjectName("refreshButton")
    #     refresh_button.setFixedHeight(30)

    #     first_row_layout.addWidget(label)
    #     first_row_layout.addWidget(self.comboBox)
    #     first_row_layout.addWidget(refresh_button)

    #     column_selection_layout.addLayout(first_row_layout)
    #     column_selection_widget.setLayout(column_selection_layout)
    #     central_layout.addWidget(column_selection_widget, 1)

    #     # Create and setup the buttons_widget with grid buttons and subset controls
    #     buttons_widget = QWidget()
    #     buttons_layout = QVBoxLayout(buttons_widget)  # Use QVBoxLayout to stack grid and subset controls

    #     # Grid buttons setup
    #     grid_buttons_layout = QGridLayout()
    #     self.buttons = {}
    #     button_labels = ["Size", "Type", "Missing", "Statistics"]
    #     for i, label in enumerate(button_labels):
    #         button = QPushButton(label, buttons_widget)
    #         button.setObjectName(f"{label.lower()}Button")
    #         self.buttons[label] = button
    #         row, col = divmod(i, 2)
    #         grid_buttons_layout.addWidget(button, row, col)
        
    #     # Add grid buttons layout to buttons_layout
    #     buttons_layout.addLayout(grid_buttons_layout)

    #     # Subset controls setup
    #     subset_controls_layout = QHBoxLayout()
    #     label2 = QLabel("Subsets", buttons_widget)
    #     label2.setStyleSheet("color: white; font-weight: bold;")
    #     label2.setFixedHeight(30)

    #     self.comboBox2 = CheckableComboBox()
    #     self.comboBox2.setObjectName("columnComboBox2")
    #     self.comboBox2.setFixedHeight(30)

    #     unselect_button = QPushButton("Unselect", buttons_widget)
    #     unselect_button.setObjectName("unselectButton")
    #     unselect_button.setFixedHeight(30)

    #     subset_button = QPushButton("Subset", buttons_widget)
    #     subset_button.setObjectName("subsetButton")
    #     subset_button.setFixedHeight(30)

    #     subset_controls_layout.addWidget(label2)
    #     subset_controls_layout.addWidget(self.comboBox2)
    #     subset_controls_layout.addWidget(unselect_button)
    #     subset_controls_layout.addWidget(subset_button)

    #     # Add subset controls layout to buttons_layout
    #     buttons_layout.addLayout(subset_controls_layout)

    #     buttons_widget.setLayout(buttons_layout)
    #     central_layout.addWidget(buttons_widget, 3)  # Larger stretch factor for buttons_widget

    #     # Create and setup the display_results_widget
    #     display_results_widget = QWidget()
    #     display_results_layout = QVBoxLayout(display_results_widget)
    #     self.output_display = QTextEdit()
    #     self.output_display.setObjectName("outputDisplay")
    #     self.output_display.setReadOnly(True)
    #     display_results_layout.addWidget(self.output_display)
    #     display_results_widget.setLayout(display_results_layout)
    #     central_layout.addWidget(display_results_widget, 4)

    #     docked_widget.setWidget(central_widget)
    #     self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, docked_widget)

    #     # Connection setup
    #     refresh_button.clicked.connect(self.controller.update_column_names)
    #     unselect_button.clicked.connect(self.comboBox2.unselect_all)
    #     subset_button.clicked.connect(self.openSubsetDialog)
    #     self.buttons["Size"].clicked.connect(self.controller.calculate_shape)
    #     self.buttons["Type"].clicked.connect(self.controller.calculate_dtype)
    #     self.buttons["Missing"].clicked.connect(self.controller.calculate_missing)
    #     self.buttons["Statistics"].clicked.connect(self.controller.calculate_statistics)

    # def create_docked_widget(self):
    #     docked_widget = QDockWidget("Property", self)
    #     central_widget = QWidget()
    #     central_widget.setObjectName("centralWidget")
    #     central_widget.setStyleSheet("QWidget#centralWidget { background-color: #B22222; }")
    #     central_layout = QVBoxLayout(central_widget)

    #     # Column selection setup remains the same
    #     column_selection_widget = QWidget()
    #     column_selection_layout = QVBoxLayout(column_selection_widget)
        
    #     first_row_layout = QHBoxLayout()
    #     label = QLabel("Header", column_selection_widget)
    #     label.setStyleSheet("color: white; font-weight: bold;")
    #     label.setFixedHeight(30)
    #     self.comboBox = QComboBox()
    #     self.comboBox.setObjectName("columnComboBox")
    #     self.comboBox.setFixedHeight(30)
    #     refresh_button = QPushButton("Refresh", column_selection_widget)
    #     refresh_button.setObjectName("refreshButton")
    #     refresh_button.setFixedHeight(30)
    #     first_row_layout.addWidget(label)
    #     first_row_layout.addWidget(self.comboBox)
    #     first_row_layout.addWidget(refresh_button)
    #     column_selection_layout.addLayout(first_row_layout)
    #     column_selection_widget.setLayout(column_selection_layout)
    #     central_layout.addWidget(column_selection_widget, 1)

    #     # Buttons widget setup with grid buttons and subset controls
    #     buttons_widget = QWidget()
    #     buttons_layout = QVBoxLayout(buttons_widget)
    #     grid_buttons_layout = QGridLayout()
    #     self.buttons = {}
    #     button_labels = ["Size", "Type", "Missing", "Statistics"]
    #     for i, label in enumerate(button_labels):
    #         button = QPushButton(label, buttons_widget)
    #         button.setObjectName(f"{label.lower()}Button")
    #         self.buttons[label] = button
    #         row, col = divmod(i, 2)
    #         grid_buttons_layout.addWidget(button, row, col)
    #     buttons_layout.addLayout(grid_buttons_layout)

    #     # Subset controls setup, excluding the Subset button
    #     subset_controls_layout = QHBoxLayout()
    #     label2 = QLabel("Subsets", buttons_widget)
    #     label2.setStyleSheet("color: white; font-weight: bold;")
    #     label2.setFixedHeight(30)
    #     self.comboBox2 = CheckableComboBox()
    #     self.comboBox2.setObjectName("columnComboBox2")
    #     self.comboBox2.setFixedHeight(30)
    #     unselect_button = QPushButton("Clear", buttons_widget)
    #     unselect_button.setObjectName("unselectButton")
    #     unselect_button.setFixedHeight(30)
    #     subset_controls_layout.addWidget(label2)
    #     subset_controls_layout.addWidget(self.comboBox2)
    #     subset_controls_layout.addWidget(unselect_button)

    #     # Add subset controls layout to buttons_layout
    #     buttons_layout.addLayout(subset_controls_layout)

    #     # Separate layout for Subset button
    #     subset_button_layout = QHBoxLayout()
    #     subset_button = QPushButton("Subset", buttons_widget)
    #     subset_button.setObjectName("subsetButton")
    #     subset_button.setFixedHeight(30)
    #     subset_button_layout.addWidget(subset_button)

    #     # Add Subset button layout to buttons_layout
    #     buttons_layout.addLayout(subset_button_layout)

    #     buttons_widget.setLayout(buttons_layout)
    #     central_layout.addWidget(buttons_widget, 3)

    #     # Display results widget setup remains the same
    #     display_results_widget = QWidget()
    #     display_results_layout = QVBoxLayout(display_results_widget)
    #     self.output_display = QTextEdit()
    #     self.output_display.setObjectName("outputDisplay")
    #     self.output_display.setReadOnly(True)
    #     display_results_layout.addWidget(self.output_display)
    #     display_results_widget.setLayout(display_results_layout)
    #     central_layout.addWidget(display_results_widget, 4)

    #     docked_widget.setWidget(central_widget)
    #     self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, docked_widget)

    #     # Connection setup remains the same
    #     refresh_button.clicked.connect(self.controller.update_column_names)
    #     unselect_button.clicked.connect(self.comboBox2.unselect_all)
    #     subset_button.clicked.connect(self.openSubsetDialog)
    #     self.buttons["Size"].clicked.connect(self.controller.calculate_shape)
    #     self.buttons["Type"].clicked.connect(self.controller.calculate_dtype)
    #     self.buttons["Missing"].clicked.connect(self.controller.calculate_missing)
    #     self.buttons["Statistics"].clicked.connect(self.controller.calculate_statistics)
    def create_docked_widget(self):
        docked_widget = QDockWidget("Property", self)
        central_widget = QWidget()
        central_widget.setObjectName("centralWidget")
        central_widget.setStyleSheet("QWidget#centralWidget { background-color: #B22222; }")
        central_layout = QVBoxLayout(central_widget)

        # Column selection widget setup
        column_selection_widget = QWidget()
        column_selection_widget.setStyleSheet("QWidget { border: 1px solid white; margin: 3px; padding: 3px; }")
        column_selection_layout = QVBoxLayout(column_selection_widget)
        
        first_row_layout = QHBoxLayout()
        label = QLabel("Header", column_selection_widget)
        label.setStyleSheet("color: white; font-weight: bold;")
        label.setFixedHeight(30)

        self.comboBox = QComboBox()
        self.comboBox.setObjectName("columnComboBox")
        self.comboBox.setFixedHeight(30)

        refresh_button = QPushButton("Refresh", column_selection_widget)
        refresh_button.setObjectName("refreshButton")
        refresh_button.setFixedHeight(30)

        first_row_layout.addWidget(label,1)
        first_row_layout.addWidget(self.comboBox,4)
        first_row_layout.addWidget(refresh_button,1)
        column_selection_layout.addLayout(first_row_layout)
        column_selection_widget.setLayout(column_selection_layout)
        central_layout.addWidget(column_selection_widget, 1)

        # Buttons widget setup
        buttons_widget = QWidget()
        buttons_widget.setStyleSheet("QWidget { border: 1px solid white; margin: 3px; padding: 3px; }")#setStyleSheet("QWidget { border: 2px solid black; margin: 5px; padding: 5px; }")
        buttons_layout = QVBoxLayout(buttons_widget)
        grid_buttons_layout = QGridLayout()
        self.buttons = {}

        button_labels = ["Size", "Type", "Missing", "Statistics"]
        for i, label in enumerate(button_labels):
            button = QPushButton(label, buttons_widget)
            button.setObjectName(f"{label.lower()}Button")
            self.buttons[label] = button
            row, col = divmod(i, 2)
            grid_buttons_layout.addWidget(button, row, col)

        buttons_layout.addLayout(grid_buttons_layout)

        # Subset controls setup
        subset_controls_layout = QHBoxLayout()
        label2 = QLabel("Subsets", buttons_widget)
        label2.setStyleSheet("color: white; font-weight: bold;")
        label2.setFixedHeight(30)

        self.comboBox2 = CheckableComboBox()
        self.comboBox2.setObjectName("columnComboBox2")
        self.comboBox2.setFixedHeight(30)

        unselect_button = QPushButton("Clear", buttons_widget)
        unselect_button.setObjectName("unselectButton")
        unselect_button.setFixedHeight(30)

        subset_controls_layout.addWidget(label2,1)
        subset_controls_layout.addWidget(self.comboBox2,4)
        subset_controls_layout.addWidget(unselect_button,2)

        buttons_layout.addLayout(subset_controls_layout)

        subset_button_layout = QHBoxLayout()
        subset_button = QPushButton("Subset", buttons_widget)
        subset_button.setObjectName("subsetButton")
        subset_button.setFixedHeight(30)
        subset_button_layout.addWidget(subset_button)

        buttons_layout.addLayout(subset_button_layout)

        buttons_widget.setLayout(buttons_layout)
        central_layout.addWidget(buttons_widget, 3)

        # Display results widget setup
        display_results_widget = QWidget()
        #display_results_widget.setStyleSheet("QWidget { border: 0.5px solid white; margin: 3px; padding: 3px; }")#setStyleSheet("QWidget { border: 2px solid black; margin: 5px; padding: 5px; }")
        display_results_layout = QVBoxLayout(display_results_widget)
        
        self.output_display = QTextEdit()
        self.output_display.setObjectName("outputDisplay")
        self.output_display.setReadOnly(True)
        display_results_layout.addWidget(self.output_display)
        display_results_widget.setLayout(display_results_layout)
        central_layout.addWidget(display_results_widget, 4)

        docked_widget.setWidget(central_widget)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, docked_widget)

        # Connection setup remains the same
        refresh_button.clicked.connect(self.controller.update_column_names)
        unselect_button.clicked.connect(self.comboBox2.unselect_all)
        subset_button.clicked.connect(self.openSubsetDialog)
        self.buttons["Size"].clicked.connect(self.controller.calculate_shape)
        self.buttons["Type"].clicked.connect(self.controller.calculate_dtype)
        self.buttons["Missing"].clicked.connect(self.controller.calculate_missing)
        self.buttons["Statistics"].clicked.connect(self.controller.calculate_statistics)
        # Subset controls setup
        subset_controls_layout = QHBoxLayout()
        label2 = QLabel("Subsets", buttons_widget)
        label2.setStyleSheet("color: white; font-weight: bold;")
        label2.setFixedHeight(30)

        self.comboBox2 = CheckableComboBox()
        self.comboBox2.setObjectName("columnComboBox2")
        self.comboBox2.setFixedHeight(30)

        unselect_button = QPushButton("Clear", buttons_widget)
        unselect_button.setObjectName("unselectButton")
        unselect_button.setFixedHeight(30)

        subset_controls_layout.addWidget(label2,1)
        subset_controls_layout.addWidget(self.comboBox2,4)
        subset_controls_layout.addWidget(unselect_button,2)

        buttons_layout.addLayout(subset_controls_layout)
###########################################################################################################################################
""" The lines below are specifically creating the UI elemnents for the Explore Menu: starting with DataInfo dialog, Setindex dialog """

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
            self.column_combo.addItem(column,True)  # Add column name as both text and data
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

    def addItem(self, text, is_numeric):
        """
        Adds an item to the combo box. If is_numeric is True, the item will be user-checkable and checked by default.
        
        :param text: The text of the item to add
        :param is_numeric: Boolean indicating whether the item is numeric
        """
        print(f"Adding item: {text}, Numeric: {is_numeric}")  # Debug print
        item = QStandardItem(text)
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
            print(f"Item pressed: {item.text()}, new state: {newState}")  # Debug print

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
                checked_items.append(item.text())
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
        self.setWindowIcon(QIcon('images/resample_icon.svg'))  # Adjust icon path as necessary
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



class SubsetDialog(QDialog):
    def __init__(self, column_ranges, dataframe, parent=None):
        super().__init__(parent)
        self.column_ranges = column_ranges  # Dictionary with column names as keys and (min, max) tuples as values
        self.setWindowTitle("Subsets - Define Column Ranges")
        icon = QIcon('images/subset_icon.svg')
        self.setWindowIcon(icon)
        self.setGeometry(100, 100, 400, 300)
        self.dataframe = dataframe  # The pandas DataFrame
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
        self.subsets = self.split_into_subsets(thresholds)  # Generate subsets
    # Ensure the subset dialog and table are correctly setup and displayed
        self.subsetDialog = QDialog(self)  # Create a new dialog as a child of the main dialog
        self.subsetDialog.setWindowTitle("Subset Table")
        self.subsetDialog.setGeometry(200, 200, 600, 400)

    # Create the subset table within the new dialog
        self.createSubsetTable()
        self.populateTable()  # Populate the table with subset data

    # Show the subset dialog modally
        self.subsetDialog.exec()
        

    def populateTable(self):
     print("Populating table with subsets...")  # Debug print

    # Check if self.subsets is populated
     if not hasattr(self, 'subsets') or not self.subsets:
        print("No subsets to display.")  # Debug print
        return  # Exit if there are no subsets

     self.tableWidget.setRowCount(len(self.subsets))
     for i, subset_indices in enumerate(self.subsets):
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
        except Exception as e:
            print(f"Error populating table for subset {i+1}: {e}")  # Log any error

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
            # Directly update the main UI with the selected subset
            self.parent().display_data(selected_subset)
            QMessageBox.information(self, "Subset Selected", "The dataset has been updated.")
            self.accept()  # Close the dialog

    # Method to get selected subset
    def getSelectedSubset(self):
     for i in range(self.tableWidget.rowCount()):
        cellWidget = self.tableWidget.cellWidget(i, 3)
        if cellWidget and cellWidget.isChecked():
            subset_indices = self.subsets[i]
            return self.dataframe.iloc[subset_indices]
     return None  # Handle the case where no subset is selected


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
            QMessageBox.warning(self, "Error", "Invalid input: Please ensure all threshold values are numeric.")

    def split_into_subsets(self, thresholds):
        df = self.dataframe.copy()  # Work on a copy to avoid modifying the original DataFrame
        subsets = []
        continuous_subset = []
        for i in range(len(df)):
            if all(thresholds[col][0] <= df.iloc[i][col] <= thresholds[col][1] for col in thresholds):
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



