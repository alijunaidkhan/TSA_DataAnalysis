# view.py
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
import os
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QAction, QIcon,QColor,QPainter,QPixmap,QStandardItem, QStandardItemModel, QDesktopServices
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QTabWidget, \
    QTableWidget,QMenu, QTableWidgetItem, QHBoxLayout, QLabel, QLineEdit, QGridLayout, QDialog, QGroupBox,\
    QRadioButton, QComboBox, QTextEdit, QMessageBox, QButtonGroup, QDockWidget,QSpinBox, QSpacerItem, QSizePolicy
os.environ['QT_API'] = 'pyqt6'
matplotlib.use('QtAgg')
from PyQt5.QtSvg import QSvgRenderer,QSvgWidget

from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pandas.plotting import lag_plot



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
        # Initialize the plotting dialog
    
        self.lineplotting_dialog = PlottingDialog(controller=self.controller)
                # Initialize the seasonal decomposition dialog
        self.seasonal_decompose_dialog = SeasonalDecomposeDialog(controller=self.controller)
        #Initialize the LagAcfPacfDialog dialog
        self.lag_acf_pacf_dialog = LagAcfPacfDialog(controller=self.controller)
        # Inside the View class
        self.unit_root_test_dialog = UnitRootTestDialog(controller=self.controller)

        self.init_ui()
        
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
        dark_stylesheet = """
            * {
                background-color: #0D0D0D;
                color: white;
                
            }
            QTableWidget {
                background-color: #1A1A1A;
                color:black;
            }
            QToolTip {
                background-color: #2F2F2F;
                color: white;
                border: 1px solid #1A1A1A;
                border-radius: 2px;
                padding: 2px;
            }

            QPushButton {
                background-color: #1A1A1A;
                border-radius: 7px;
                padding: 6px;
                font-weight: bold;

            }
            QPushButton:hover {
                background-color: #121212;
            }
            QComboBox {
                border: 2px solid #FF929292;
                border-radius: 7px;
                padding: 3px;
                background-color: #FF929292;
            }
            QComboBox::drop-down {
                border: none

            }

            QStatusBar {
                background-color: #1A1A1A;
                color: white;
                border: 1px solid #1A1A1A;
                border-radius: 10px;
                padding: 2px;
                font-size: 10pt;
            }
            QScrollBar:vertical {
                border: 1px solid #333333;
                background: #1A1A1A;
                width: 10px;
                margin: 10px 0 10px 0;
                border-radius: 4px;
            }
            QScrollBar:horizontal {
                border: 1px solid #121212;
                background: #121212;
                color: white;
                height: 10px;
                margin: 0 10px 0 10px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #121212;
                min-height: 30px;
                border-radius: 4px;
            }
            QScrollBar::handle:horizontal {
                background: #121212;
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
        """

        self.setStyleSheet(dark_stylesheet)
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
        exit_action = QAction(QIcon(exit_pixmap), "&Exit", self, triggered=self.close)
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

        # Hide the initial message label
        self.initial_message_label.hide()
####################################################################################################
        # Custom stylesheet for vertical and horizontal scroll bars
        scrollbar_style = """
        
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
        """

        # Apply the scrollbar style to the table widget
        self.table_widget.setStyleSheet(self.table_widget.styleSheet() + scrollbar_style)

    def open_data_info_dialog(self, data_frame_info):
        '''Opens the Data Information dialog window to display DataFrame details.
        Args:data_frame_info (dict): Information about the DataFrame to be displayed.'''

        dialog = DataInfoDialog()
        dialog.populate_data_info(data_frame_info)
        dialog.exec()

    def update_plotting_dialog_columns(self, columns):
        if self.plotting_dialog is not None:
            self.plotting_dialog.update_combobox_items(columns)
    def update_column_combobox(self, logical_index):
        """
        Updates the combobox with the selected column name.
        """
        column_name = self.table_widget.horizontalHeaderItem(logical_index).text()
        self.comboBox.clear()
        self.comboBox.addItem(column_name)
    

##################################################################################################################

    def create_docked_widget(self):
        """
        Creates a docked widget with a red background central widget and three container widgets.
        The 'column_selection_widget' contains a label, a combobox, and a button arranged horizontally.
        The 'buttons_widget' contains a grid of six buttons.
        The 'display_results_widget' contains a QTextEdit for displaying output.
        """
        docked_widget = QDockWidget("Exploratory Data Analysis", self)
        central_widget = QWidget()
        central_widget.setObjectName("centralWidget")
        central_widget.setStyleSheet("QWidget#centralWidget { background-color: #B22222; }")
        central_layout = QVBoxLayout(central_widget)

        # Create and setup the column_selection_widget
        column_selection_widget = QWidget(central_widget)
        column_selection_layout = QHBoxLayout(column_selection_widget)
        label = QLabel("Header", column_selection_widget)
        label.setStyleSheet("color: white; font-weight: bold;")
        label.setFixedHeight(30)

        self.comboBox = QComboBox(column_selection_widget)
        self.comboBox.setObjectName("columnComboBox")
        self.comboBox.setFixedHeight(30)
        self.table_widget.horizontalHeader().sectionClicked.connect(self.update_column_combobox)
        #self.table_widget.itemClicked.connect(self.update_column_combobox)


        refresh_button = QPushButton("Refresh", column_selection_widget)
        refresh_button.setObjectName("refreshButton")
        refresh_button.setToolTip("Refresh the data and update column names.")

        refresh_button.setFixedHeight(30)

        column_selection_layout.addWidget(label, 1)
        column_selection_layout.addWidget(self.comboBox, 5)
        column_selection_layout.addWidget(refresh_button, 2)


        # Create and setup the buttons_widget
        buttons_widget = QWidget(central_widget)
        buttons_layout = QGridLayout(buttons_widget)
        self.buttons = {}
        button_info = {
    "Shape": "Calculate the shape of the data.",
    "Unique": "Calculate unique values in the data.",
    "Type": "Calculate data types of columns.",
    "Missing": "Calculate the number of missing values.",
    "Statistics": "Calculate basic statistics of the data.",
    "NaNs": "Calculate the number of NaN values in the data."
}

        button_labels = ["Shape", "Unique", "Type", "Missing", "Statistics", "NaNs"]


#self.buttons[label].clicked.connect(getattr(self.controller, f"calculate_{label.lower()}"))
        for i, label in enumerate(button_labels):
            button = QPushButton(label, buttons_widget)
            button.setObjectName(f"{label.lower()}Button")
            self.buttons[label] = button
            self.buttons[label].setToolTip(button_info[label])
            row, col = divmod(i, 2)
            buttons_layout.addWidget(button, row, col)

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
        self.buttons["Shape"].clicked.connect(self.controller.calculate_shape)
        # Connect the "Type" button
        self.buttons["Type"].clicked.connect(self.controller.calculate_dtype)
        # Connect the "Statistics" button
        self.buttons["Statistics"].clicked.connect(self.controller.calculate_statistics)
        # Connecting the 'Unique' button
        self.buttons["Unique"].clicked.connect(self.controller.calculate_unique)
        # Connect the "Missing"
        self.buttons["Missing"].clicked.connect(self.controller.calculate_missing)
        # Connect the"NaNs" buttons
        self.buttons["NaNs"].clicked.connect(self.controller.calculate_nans)


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
        QMessageBox.information(self, "Confirm and Exit", "Changes confirmed.")

    def confirm(self):
        # Display a message box for confirmation
        QMessageBox.information(self, "Confirm", "Changes have been confirmed.")
        self.refresh_data_info_tab()

    def confirm_and_exit(self):
        QMessageBox.information(self, "Confirm and Exit", "Changes confirmed. Exiting now.")
        self.refresh_data_info_tab()  # Refresh the DataFrame info tab
        self.accept()  # Closes the dialog

    def populate_data_info(self, data_info):
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
            self.column_combo.addItem(column)  # Add column name as both text and data


class CheckableComboBox(QComboBox):
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

    def checkedItems(self):
        checked_items = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.CheckState.Checked:
                checked_items.append(self.model().item(i).text())
        return checked_items

    def get_checked_items(self):
        checked_items = []
        for index in range(self.model().rowCount()):
            item = self.model().item(index)
            if item.checkState() == Qt.CheckState.Checked:
                checked_items.append(item.text())
        return checked_items

# No.2 Index dialog


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
        ok_button = QPushButton("OK")
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
    def plot_lag(self, series):
        self.lag_axes.clear()
        lag_plot(series, ax=self.lag_axes)
        self.lag_axes.set_title('Lag Plot')
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
