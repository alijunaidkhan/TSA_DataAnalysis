import sys
import unittest
from unittest.mock import patch, MagicMock
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
from main import main

class TestMain(unittest.TestCase):
    @patch('main.QFont', MagicMock())  # Mock QFont to avoid actual GUI initialization
    @patch('main.Controller', MagicMock())  # Mock Controller class
    @patch.object(sys, 'exit')  # Mock sys.exit to prevent program termination
    @patch.object(QApplication, 'exec')  # Mock QApplication.exec to prevent GUI event loop
    def test_main(self, mock_exec, mock_exit, mock_controller, mock_qfont):
        # Call the main function
        main()

        # Assert that QFont was initialized with the correct parameters
        mock_qfont.assert_called_once_with("Arial", 10)

        # Assert that Controller's run method was called
        mock_controller.return_value.run.assert_called_once()

        # Assert that sys.exit was called with the correct argument
        mock_exit.assert_called_once_with(mock_exec.return_value)

if __name__ == "__main__":
    unittest.main()
