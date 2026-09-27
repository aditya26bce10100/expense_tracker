"""
report_generator.py

Tells:
- total spending
- category-wise breakdown
- monthly summary
- highest spending category
"""


def total_spent(expenses):
    """Return the sum of all expense amounts."""
    return sum(e["amount"] for e in expenses)


def category_wise_summary(expenses):
    """
    Return a dictionary of {category: total_amount}, sorted by
    amount spent in descending order (highest spending first).
    """
    summary = {}
    for e in expenses:
        cat = e["category"]
        summary[cat] = summary.get(cat, 0) + e["amount"]

    sorted_summary = dict(sorted(summary.items(), key=lambda item: item[1], reverse=True))
    return sorted_summary


def monthly_summary(expenses):
    summary = {}
    for e in expenses:
        parts = e["date"].split("-")
        if len(parts) == 3:
            month_year = f"{parts[1]}-{parts[2]}"
            summary[month_year] = summary.get(month_year, 0) + e["amount"]
    return summary


def print_summary_report(expenses):
    if not expenses:
        print("\nNo data available to generate a report.")
        return

    print("\n========== EXPENSE SUMMARY REPORT ==========")
    print(f"Total Expenses Recorded : {len(expenses)}")
    print(f"Total Amount Spent      : Rs.{total_spent(expenses):.2f}")

    print("\n--- Category-wise Breakdown ---")
    cat_summary = category_wise_summary(expenses)
    for cat, amt in cat_summary.items():
        print(f"  {cat:<15}: Rs.{amt:.2f}")

    if cat_summary:
        top_category = next(iter(cat_summary))
        print(f"\nHighest Spending Category: {top_category} (Rs.{cat_summary[top_category]:.2f})")

    print("\n--- Month-wise Breakdown ---")
    month_summary = monthly_summary(expenses)
    for month, amt in sorted(month_summary.items()):
        print(f"  {month:<10}: Rs.{amt:.2f}")
    print("==============================================")
