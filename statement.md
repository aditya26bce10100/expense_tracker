# Problem Statement

## Problem Statement

There is a problem among students and young people regarding keeping track
of their daily expenditure. The lack of a way to log and analyze their
spending makes it impossible to see where their money goes every month,
determine overspending in some categories, and plan a budget. All the
possible solutions require either internet connection or special applications
that cost money. Thus, there is a need for a light tool to log
expenses that does not require an internet connection and has an instant
visualization of spending.

## Scope of the Project

The current project is a command line Personal Expense Tracker in Python.
It enables one user to do the following:
- log expenses with date, category, amount, and description;
- view, filter, and delete logged expenses;
- generate report that shows total expenses, category-wise breakdown of the
  expenses, monthly breakdown of the expenses, and the most costly category.

The scope is deliberately narrow in order to be consistent with the scope
of a course project for Introduction to Problem Solving and Programming.

## Target Users

- college students tracking their monthly allowance or pocket money
- individuals who are interested in logging their daily expenses using a
  lightweight tool instead of installing a bulky finance application

## High-Level Features

1. **Add Expense** – logging a new expense with date, category, amount,
   and description
2. **View Expenses** – viewing all the expenses or filtering them by
   category
3. **Delete Expense** – deleting an incorrect expense by its ID
4. **Summary Report** – viewing total expenses, category-wise breakdown of
   the expenses (in descending order of the amounts), month-wise breakdown,
   and the most costly category
5. **Persistent Storage** – storing all the information to the CSV file and
   loading it in the next session