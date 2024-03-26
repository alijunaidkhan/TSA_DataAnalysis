# main.py
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
from controller import Controller
def main():
    app = QApplication(sys.argv)
    app.setFont(QFont("Roboto", 10))
    controller = Controller()
    controller.run()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
