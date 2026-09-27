import unittest
from modules import report_generator


class TestReportGenerator(unittest.TestCase):

    def setUp(self):
        """Sample data used across multiple tests."""
        self.sample_expenses = [
            {"id": 1, "date": "01-09-2026", "category": "Food", "amount": 200.0, "description": "Lunch"},
            {"id": 2, "date": "05-09-2026", "category": "Travel", "amount": 100.0, "description": "Bus"},
            {"id": 3, "date": "10-09-2026", "category": "Food", "amount": 150.0, "description": "Dinner"},
            {"id": 4, "date": "02-10-2026", "category": "Bills", "amount": 500.0, "description": "Electricity"},
        ]

    def test_total_spent_with_expenses(self):
        self.assertEqual(report_generator.total_spent(self.sample_expenses), 950.0)

    def test_total_spent_empty_list(self):
        self.assertEqual(report_generator.total_spent([]), 0)

    def test_category_wise_summary_totals(self):
        summary = report_generator.category_wise_summary(self.sample_expenses)
        self.assertEqual(summary["Food"], 350.0)
        self.assertEqual(summary["Travel"], 100.0)
        self.assertEqual(summary["Bills"], 500.0)

    def test_category_wise_summary_sorted_descending(self):
        summary = report_generator.category_wise_summary(self.sample_expenses)
        # Highest spending category should appear first
        top_category = next(iter(summary))
        self.assertEqual(top_category, "Bills")

    def test_monthly_summary_groups_by_month(self):
        summary = report_generator.monthly_summary(self.sample_expenses)
        self.assertEqual(summary["09-2026"], 450.0)  # Sept expenses: 200 + 100 + 150
        self.assertEqual(summary["10-2026"], 500.0)  # Oct expenses: 500

    def test_empty_expenses_returns_empty_summaries(self):
        self.assertEqual(report_generator.category_wise_summary([]), {})
        self.assertEqual(report_generator.monthly_summary([]), {})


if __name__ == "__main__":
    unittest.main()
