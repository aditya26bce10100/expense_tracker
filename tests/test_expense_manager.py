import unittest
from unittest.mock import patch
from modules import expense_manager


class TestDeleteExpense(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            {"id": 1, "date": "01-09-2026", "category": "Food", "amount": 200.0, "description": "Lunch"},
            {"id": 2, "date": "05-09-2026", "category": "Travel", "amount": 100.0, "description": "Bus"},
        ]

    def test_delete_existing_expense(self):
        result = expense_manager.delete_expense(self.expenses, 1)
        self.assertTrue(result)
        self.assertEqual(len(self.expenses), 1)
        self.assertEqual(self.expenses[0]["id"], 2)

    def test_delete_nonexistent_expense(self):
        result = expense_manager.delete_expense(self.expenses, 999)
        self.assertFalse(result)
        self.assertEqual(len(self.expenses), 2)  # nothing removed


class TestViewByCategory(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            {"id": 1, "date": "01-09-2026", "category": "Food", "amount": 200.0, "description": "Lunch"},
            {"id": 2, "date": "05-09-2026", "category": "Travel", "amount": 100.0, "description": "Bus"},
        ]

    def test_view_by_category_matches_case_insensitive(self):
        # Should not raise an error, and should not crash on mixed case
        try:
            expense_manager.view_by_category(self.expenses, "food")
        except Exception as e:
            self.fail(f"view_by_category raised an unexpected exception: {e}")


class TestAddExpense(unittest.TestCase):

    @patch("builtins.input")
    def test_add_expense_creates_correct_record(self, mock_input):
        # Simulate the user's answers to each prompt, in order:
        # date -> category -> amount -> description
        mock_input.side_effect = ["01-09-2026", "Food", "150", "Groceries"]

        expenses = []
        expense_manager.add_expense(expenses)

        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]["id"], 1)
        self.assertEqual(expenses[0]["date"], "01-09-2026")
        self.assertEqual(expenses[0]["category"], "Food")
        self.assertEqual(expenses[0]["amount"], 150.0)
        self.assertEqual(expenses[0]["description"], "Groceries")

    @patch("builtins.input")
    def test_add_expense_assigns_incrementing_ids(self, mock_input):
        mock_input.side_effect = [
            "01-09-2026", "Food", "100", "First",
            "02-09-2026", "Travel", "50", "Second",
        ]

        expenses = []
        expense_manager.add_expense(expenses)
        expense_manager.add_expense(expenses)

        self.assertEqual(expenses[0]["id"], 1)
        self.assertEqual(expenses[1]["id"], 2)


if __name__ == "__main__":
    unittest.main()
