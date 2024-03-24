import unittest
from unittest.mock import MagicMock
from PyQt6.QtWidgets import QApplication
from main import main

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def tearDown(self):
        self.app.quit()

    def test_main(self):
        controller = MagicMock()
        main()
        # Add assertions here to check if the application behaves as expected


if __name__ == "__main__":
    unittest.main()
