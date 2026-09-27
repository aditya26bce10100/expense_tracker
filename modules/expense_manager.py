"""
expense_manager.py

Use: adding, viewing, and deleting expenses.
"""

from modules import utils


def add_expense(expenses):
    """Prompt the user for details and add a new expense record."""
    print("\n--- Add New Expense ---")
    date = utils.get_valid_date()
    category = utils.get_valid_category()
    amount = utils.get_valid_amount()
    description = utils.get_non_empty_string("Enter description: ")

    new_id = (max((e["id"] for e in expenses), default=0)) + 1

    expense = {
        "id": new_id,
        "date": date,
        "category": category,
        "amount": amount,
        "description": description,
    }
    expenses.append(expense)
    print(f"Expense added successfully! (ID: {new_id})")
    return expenses


def view_all_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n{:<5}{:<12}{:<15}{:<10}{:<}".format("ID", "Date", "Category", "Amount", "Description"))
    print("-" * 65)
    for e in expenses:
        print("{:<5}{:<12}{:<15}{:<10}{:<}".format(
            e["id"], e["date"], e["category"], f"Rs.{e['amount']:.2f}", e["description"]
        ))


def view_by_category(expenses, category):
    """Filter and display expenses belonging to one category."""
    filtered = [e for e in expenses if e["category"].lower() == category.lower()]
    if not filtered:
        print(f"\nNo expenses found in category '{category}'.")
        return
    view_all_expenses(filtered)


def delete_expense(expenses, expense_id):
    """Remove an expense by its ID. Returns True if something was deleted."""
    for e in expenses:
        if e["id"] == expense_id:
            expenses.remove(e)
            print(f"Expense ID {expense_id} deleted.")
            return True
    print(f"No expense found with ID {expense_id}.")
    return False
