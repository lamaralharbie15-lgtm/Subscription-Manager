# ============================================================
# ui.py - User Interface (member 1)
# Handles all printing and input() for the Subscription Manager
# ============================================================

from datetime import datetime, date

CURRENCY = "SAR"


def show_menu():
    """Print the main menu and return the user's choice as a string."""
    print("\n========== Subscription Manager ==========")
    print("1. Add subscription")
    print("2. Show all subscriptions")
    print("3. Show totals (monthly / yearly)")
    print("4. Upcoming renewals")
    print("5. Delete subscription")
    print("0. Exit")
    choice = input("Choose an option: ").strip()
    return choice


def get_new_subscription():
    """Ask the user for a new subscription, validate it, and return it as a dict."""
    print("\n--- Add a new subscription ---")

    # name: must not be empty
    while True:
        name = input("Subscription name (e.g. Netflix): ").strip()
        if name != "":
            break
        print("Name cannot be empty. Try again.")

    # price: must be a number greater than 0
    while True:
        text = input("Price (" + CURRENCY + "): ").strip()
        try:
            price = float(text)
            if price > 0:
                break
            print("Price must be greater than 0.")
        except ValueError:
            print("Please enter a valid number (e.g. 45 or 45.5).")

    # cycle: only monthly or yearly
    while True:
        cycle = input("Billing cycle (monthly / yearly): ").strip().lower()
        if cycle == "monthly" or cycle == "yearly":
            break
        print("Please type exactly: monthly or yearly.")

    # renewal date: YYYY-MM-DD
    while True:
        text = input("Next renewal date (YYYY-MM-DD): ").strip()
        try:
            renewal = datetime.strptime(text, "%Y-%m-%d")
            renewal_date = renewal.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Use the format YYYY-MM-DD (e.g. 2026-12-01).")

    return {
        "name": name,
        "price": price,
        "cycle": cycle,
        "renewal_date": renewal_date,
    }


def display_subscriptions(subscriptions):
    """Print all subscriptions in a table (or a message if the list is empty)."""
    if len(subscriptions) == 0:
        print("\nNo subscriptions yet.")
        return

    print("\n#   Name                Price      Cycle     Renewal date")
    print("-" * 58)
    number = 1
    for sub in subscriptions:
        print(f"{number:<4}{sub['name']:<20}{sub['price']:<11.2f}{sub['cycle']:<10}{sub['renewal_date']}")
        number += 1


def display_totals(monthly_total, yearly_total):
    """Print the monthly and yearly spending summary."""
    print("\n--- Spending summary ---")
    print(f"Total per month : {monthly_total:.2f} {CURRENCY}")
    print(f"Total per year  : {yearly_total:.2f} {CURRENCY}")


def display_upcoming(upcoming):
    """Print the subscriptions that are about to renew."""
    if len(upcoming) == 0:
        print("\nNo upcoming renewals.")
        return

    print("\n--- Upcoming renewals ---")
    for sub in upcoming:
        renewal = datetime.strptime(sub["renewal_date"], "%Y-%m-%d").date()
        days_left = (renewal - date.today()).days
        if days_left == 0:
            when = "TODAY"
        elif days_left < 0:
            when = str(-days_left) + " day(s) ago"
        else:
            when = "in " + str(days_left) + " day(s)"
        print(f"!! {sub['name']} renews {when} ({sub['renewal_date']}) - {sub['price']:.2f} {CURRENCY}")


def get_delete_index(subscriptions):
    """Show numbered subscriptions and return the index (from 0) to delete, or None."""
    if len(subscriptions) == 0:
        print("\nNo subscriptions to delete.")
        return None

    print("\n--- Delete a subscription ---")
    number = 1
    for sub in subscriptions:
        print(str(number) + ". " + sub["name"] + " (" + f"{sub['price']:.2f} " + CURRENCY + ", " + sub["cycle"] + ")")
        number += 1

    text = input("Enter the number to delete (0 to cancel): ").strip()
    try:
        choice = int(text)
    except ValueError:
        print("That is not a valid number.")
        return None

    if choice == 0:
        print("Cancelled.")
        return None
    if 1 <= choice <= len(subscriptions):
        return choice - 1

    print("Number out of range.")
    return None


def show_message(msg):
    """Print any message sent by main.py."""
    print(msg)
