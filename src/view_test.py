import unittest
from unittest.mock import MagicMock
from view import View

class TestView(unittest.TestCase):
    def setUp(self):
        # Create a mock controller
        self.mock_controller = MagicMock()

    def test_init_ui(self):
        # Create a View instance with the mock controller
        view = View(self.mock_controller)

        # Test whether the UI components are initialized correctly
        self.assertIsNotNone(view.central_widget)
        self.assertIsNotNone(view.initial_message_label)
        self.assertIsNotNone(view.table_widget)
        self.assertIsNotNone(view.progressBar)

        # Test whether signals are connected correctly
        self.assertTrue(view.subsetGenerated.hasConnections())
        self.assertTrue(view.table_widget.cellChanged.hasConnections())

    def test_bool_test(self):
        # Create a View instance with the mock controller
        view = View(self.mock_controller)

        # Test the bool_test method
        self.assertFalse(view.bool_test())  # Initially data_changed is False

        # Set data_changed to True
        view.data_changed = True
        self.assertTrue(view.bool_test())

    # You can add more test methods for other functionalities as needed

if __name__ == '__main__':
    unittest.main()
