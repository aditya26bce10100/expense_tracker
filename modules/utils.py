from datetime import datetime

CATEGORIES = ["Food", "Travel", "Bills", "Shopping", "Entertainment", "Health", "Other"]


def get_valid_amount():
    """Keep asking until the user enters a positive number."""
    while True:
        raw = input("Enter amount (Rs.): ").strip()
        try:
            amount = float(raw)
            if amount <= 0:
                print("Amount must be greater than 0. Try again.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 250.50).")


def get_valid_date():
    """Accept a date in DD-MM-YYYY format, or default to today."""
    raw = input("Enter date (DD-MM-YYYY) or press Enter for today: ").strip()
    if raw == "":
        return datetime.now().strftime("%d-%m-%Y")
    try:
        parsed = datetime.strptime(raw, "%d-%m-%Y")
        return parsed.strftime("%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Using today's date instead.")
        return datetime.now().strftime("%d-%m-%Y")


def get_non_empty_string(prompt):
    """Keep asking until the user enters something (not blank)."""
    while True:
        value = input(prompt).strip()
        if value == "":
            print("This field cannot be empty. Try again.")
            continue
        return value


def get_valid_category():
    print("Categories:", ", ".join(CATEGORIES))
    while True:
        raw = input("Enter category: ").strip().title()
        if raw in CATEGORIES:
            return raw
        print(f"Please choose one of: {', '.join(CATEGORIES)}")
