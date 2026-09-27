from modules import expense_manager, report_generator, file_handler


def print_menu():
    print("\n========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Expenses by Category")
    print("4. Delete an Expense")
    print("5. View Summary Report")
    print("6. Save & Exit")
    print("================================================")


def get_menu_choice():
    while True:
        choice = input("Enter your choice (1-6): ").strip()
        if choice in {"1", "2", "3", "4", "5", "6"}:
            return int(choice)
        print("Invalid choice. Please enter a number from 1 to 6.")


def main():
    expenses = file_handler.load_expenses()
    print("Welcome to your Personal Expense Tracker!")
    print(f"Loaded {len(expenses)} existing expense record(s).")

    while True:
        print_menu()
        choice = get_menu_choice()

        if choice == 1:
            expense_manager.add_expense(expenses)
            file_handler.save_expenses(expenses)  # auto-save after every change

        elif choice == 2:
            expense_manager.view_all_expenses(expenses)

        elif choice == 3:
            category = input("Enter category to filter by: ").strip().title()
            expense_manager.view_by_category(expenses, category)

        elif choice == 4:
            try:
                expense_id = int(input("Enter the ID of the expense to delete: ").strip())
                expense_manager.delete_expense(expenses, expense_id)
                file_handler.save_expenses(expenses)
            except ValueError:
                print("Please enter a valid numeric ID.")

        elif choice == 5:
            report_generator.print_summary_report(expenses)

        elif choice == 6:
            file_handler.save_expenses(expenses)
            print("Data saved. Goodbye!")
            break


if __name__ == "__main__":
    main()
