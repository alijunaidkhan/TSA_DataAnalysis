from PyQt6.QtWidgets import (QApplication, QDialog, QVBoxLayout, QGridLayout,
                             QLabel, QComboBox, QLineEdit, QCheckBox, QPushButton,
                             QGroupBox, QHBoxLayout, QFormLayout, QSizePolicy)
from PyQt6.QtCore import QSize, Qt

class ArimaConfigDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ARIMA Orders Grid Search")
        self.setMinimumSize(QSize(900, 600))  # Set the window size
        
        # Main vertical layout
        main_layout = QVBoxLayout()

        # Add parameter groups
        self.non_seasonal_group = self.create_non_seasonal_group()
                
        self.seasonal_group = self.create_seasonal_group()
        
        self.additional_options_group = self.create_additional_options_group()
           
        
        
        self.additional_options_group = self.create_additional_options_group()

        # Add parameter groups to the main layout
        main_layout.addWidget(self.create_non_seasonal_group())
        main_layout.addWidget(self.create_seasonal_group())
        main_layout.addWidget(self.create_additional_options_group())
              



        # Add action buttons at the bottom
        self.create_action_buttons(main_layout)

        self.setLayout(main_layout)


    def create_non_seasonal_group(self):
        group = QGroupBox("Non-Seasonal Parameters")
        layout = QGridLayout()

        # Set the column stretch to control spacing
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(3, 1)

        # Create labels and comboboxes for non-seasonal parameters
        params = [
            ("Start p", "Max p", 0, 5),
            ("d", "Max d", 0, 2),
            ("Start q", "Max q", 0, 5),
        ]

        # Add widgets to the layout
        for i, (start_label, max_label, start, end) in enumerate(params):
            label = QLabel(f"{start_label}:")
            layout.addWidget(label, i, 0)

            combobox = self.create_combobox_with_range(start, end)
            layout.addWidget(combobox, i, 1)

            label_max = QLabel(f"{max_label}:")
            layout.addWidget(label_max, i, 2)

            combobox_max = self.create_combobox_with_range(start, end)
            layout.addWidget(combobox_max, i, 3)

        group.setLayout(layout)
        return group


    def create_seasonal_group(self):
        group = QGroupBox("Seasonal Parameters")
        layout = QGridLayout()

        # Set the column stretch to control spacing
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(3, 1)

        # Checkbox for enabling seasonal parameters
        self.seasonal = QCheckBox("Enable Seasonal")
        layout.addWidget(self.seasonal, 0, 0, 1, 4)  # Span 4 columns for alignment

        # Seasonal parameters and their comboboxes
        seasonal_params = [
            ("Start P", "Max P", 0, 2),
            ("D", "Max D", 0, 1),
            ("Start Q", "Max Q", 0, 2),
            # The Seasonal Period (m) will span to the end of the layout
            ("Seasonal Period (m)", None, 1, 12),
        ]

        # Starting from the second row, as the first row contains the checkbox
        for i, (label_text, max_label_text, start, end) in enumerate(seasonal_params, start=1):
            label = QLabel(f"{label_text}:")
            layout.addWidget(label, i, 0)

            combobox = self.create_combobox_with_range(start, end)
            layout.addWidget(combobox, i, 1)

            if max_label_text:  # Only add max labels and comboboxes if they exist
                max_label = QLabel(f"{max_label_text}:")
                layout.addWidget(max_label, i, 2)

                max_combobox = self.create_combobox_with_range(start, end)
                layout.addWidget(max_combobox, i, 3)
            else:
                # For the Seasonal Period (m), extend the combobox to the end
                layout.addWidget(combobox, i, 1, 1, 3)

        group.setLayout(layout)
        return group




    def create_param_row(self, layout, start_label_text, max_label_text, start, end):
        row_layout = QHBoxLayout()
        start_label = QLabel(start_label_text)
        start_combobox = self.create_combobox_with_range(start, end)
        max_label = QLabel(max_label_text)
        max_combobox = self.create_combobox_with_range(start, end)
        row_layout.addWidget(start_label)
        row_layout.addWidget(start_combobox)
        row_layout.addWidget(max_label)
        row_layout.addWidget(max_combobox)
        layout.addLayout(row_layout)

    def create_additional_options_group(self):
        group = QGroupBox("Additional Options")
        main_layout = QVBoxLayout()

        # Horizontal layout for checkboxes
        checkboxes_layout = QHBoxLayout()
        self.stepwise = QCheckBox("Stepwise")
        self.stepwise.setChecked(True)
        checkboxes_layout.addWidget(self.stepwise)

        self.suppress_warnings = QCheckBox("Suppress Warnings")
        self.suppress_warnings.setChecked(True)
        checkboxes_layout.addWidget(self.suppress_warnings)

        self.trace = QCheckBox("Trace")
        checkboxes_layout.addWidget(self.trace)

        self.random = QCheckBox("Random Search")
        checkboxes_layout.addWidget(self.random)

        self.return_valid_fits = QCheckBox("Return Valid Fits")
        checkboxes_layout.addWidget(self.return_valid_fits)

        # Grid layout for the rest of the options
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
        ]

        # Add parameters to grid layout
        for i, (label, widget) in enumerate(parameters):
            row = i // 2
            col = (i % 2) * 2
            grid_layout.addWidget(QLabel(label), row, col)
            grid_layout.addWidget(widget, row, col + 1)

        # Combine the checkbox and grid layouts
        main_layout.addLayout(checkboxes_layout)
        main_layout.addLayout(grid_layout)

        group.setLayout(main_layout)
        return group

    def create_dropdown(self, options):
        dropdown = QComboBox()
        dropdown.addItems(options)
        return dropdown

    # Helper method to create a combobox with a range of numbers
    def create_combobox_with_range(self, start, end):
        combobox = QComboBox()
        for i in range(start, end + 1):
            combobox.addItem(str(i))
        return combobox


    def create_action_buttons(self, layout):
        buttons_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)
        layout.addLayout(buttons_layout)

    # Helper method to create a combobox with range
    def create_combobox_with_range(self, start, end):
        combobox = QComboBox()
        for i in range(start, end + 1):
            combobox.addItem(str(i))
        return combobox

if __name__ == "__main__":
    app = QApplication([])
    dialog = ArimaConfigDialog()
    dialog.show()
    app.exec()

