# Problem Statement

## Problem Statement

Many students and young professionals struggle to keep track of their daily
expenses. Without a simple way to log and review spending, it becomes
difficult to understand where money is going each month, identify
overspending in specific categories, and plan a budget. Most solutions
either require internet access, complex apps, or paid software. There is a
need for a lightweight, offline tool that lets a user quickly record
expenses and instantly view meaningful summaries.

## Scope of the Project

This project is a command-line based Personal Expense Tracker built in
Python. It allows a single user to:
- Record expenses with a date, category, amount, and description
- View, filter, and delete recorded expenses
- Generate summary reports (total spend, category-wise breakdown, monthly
  breakdown, and highest spending category)

The scope is intentionally limited to a single-user, offline, file-based
system (no database, no GUI, no multi-user support), matching the level of
an Introduction to Problem Solving and Programming course project.

## Target Users

- College students managing a monthly allowance or pocket money
- Individuals who want a simple, no-frills way to track daily spending
  without installing a heavy finance app

## High-Level Features

1. **Add Expense** – log a new expense with date, category, amount, and
   description
2. **View Expenses** – view all expenses, or filter by category
3. **Delete Expense** – remove an incorrectly entered expense by its ID
4. **Summary Report** – view total spending, category-wise breakdown
   (sorted by amount), month-wise breakdown, and the highest spending
   category
5. **Persistent Storage** – all data is automatically saved to a CSV file
   and reloaded the next time the program runs
