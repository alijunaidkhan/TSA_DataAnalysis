# main.py
import time
import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QToolButton, QMenu, \
    QCheckBox, QTableWidget, QTableWidgetItem, QMenuBar, QHBoxLayout, QWidgetAction, QScrollArea, QLabel, QLineEdit, \
    QStatusBar, QProgressDialog, QDialog, QGroupBox, QGroupBox, QComboBox, QListWidget, QListWidgetItem, QErrorMessage,\
    QMessageBox, QStylePainter, QStyleOptionComboBox, QStyle, QStyledItemDelegate, QStyleOptionComboBox, QAbstractItemView

from PyQt6.QtGui import QIcon, QAction, QFont, QPixmap, QColor, QStandardItem, QStandardItemModel, QPalette
from PyQt6.QtCore import Qt, QSize, QThread, pyqtSignal, QEvent, QTimer
from controller import Controller


def main():
    app = QApplication(sys.argv)
    controller = Controller()
    controller.run()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
