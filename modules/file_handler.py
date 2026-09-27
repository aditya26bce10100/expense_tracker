"""
file_handler.py

Handles reading and writing expense data to a CSV file.
"""

import csv
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "expenses.csv")
FIELDNAMES = ["id", "date", "category", "amount", "description"]


def load_expenses():
    """Read all expenses from the CSV file into a list of dictionaries."""
    expenses = []
    if not os.path.exists(DATA_FILE):
        return expenses

    try:
        with open(DATA_FILE, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["amount"] = float(row["amount"])
                row["id"] = int(row["id"])
                expenses.append(row)
    except (IOError, ValueError) as e:
        print(f"Warning: could not fully read data file ({e}). Starting fresh.")
    return expenses


def save_expenses(expenses):
    """Write the full list of expenses back to the CSV file. Returns True on success."""
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(expenses)
        return True
    except IOError as e:
        print(f"Error: could not save data ({e}).")
        return False
