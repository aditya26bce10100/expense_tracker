import unittest
import os
import tempfile
from modules import file_handler


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        """Point the module at a temporary file before each test."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_data_file = file_handler.DATA_FILE
        file_handler.DATA_FILE = os.path.join(self.temp_dir.name, "test_expenses.csv")

    def tearDown(self):
        """Restore the real data file path and clean up the temp directory."""
        file_handler.DATA_FILE = self.original_data_file
        self.temp_dir.cleanup()

    def test_load_expenses_when_file_missing_returns_empty_list(self):
        expenses = file_handler.load_expenses()
        self.assertEqual(expenses, [])

    def test_save_and_load_roundtrip(self):
        sample = [
            {"id": 1, "date": "01-09-2026", "category": "Food", "amount": 200.0, "description": "Lunch"},
            {"id": 2, "date": "05-09-2026", "category": "Travel", "amount": 100.0, "description": "Bus"},
        ]
        success = file_handler.save_expenses(sample)
        self.assertTrue(success)

        loaded = file_handler.load_expenses()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0]["category"], "Food")
        self.assertEqual(loaded[0]["amount"], 200.0)
        self.assertEqual(loaded[1]["id"], 2)


if __name__ == "__main__":
    unittest.main()
