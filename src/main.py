# main.py
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont,QIcon
from controller import Controller
def main():
    app = QApplication(sys.argv)
    app.setFont(QFont("Roboto", 10))
    icon = QIcon('images/bulb_icon.png')
    app.setWindowIcon(icon)
    controller = Controller()
    controller.run()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
