from datetime import datetime, timedelta


def calculate_totals(subscriptions: list[dict]) -> tuple[float, float]:
    if not subscriptions:
        return 0.0, 0.0

    monthly_total = 0.0
    yearly_total = 0.0

    for sub in subscriptions:
        price = float(sub["price"])
        cycle = sub["cycle"].strip().lower()

        if cycle == "monthly":
            monthly_total += price
            yearly_total += price * 12
        elif cycle == "yearly":
            monthly_total += price / 12
            yearly_total += price

    return round(monthly_total, 2), round(yearly_total, 2)


def get_upcoming_renewals(subscriptions: list[dict]) -> list[dict]:
    if not subscriptions:
        return []

    today = datetime.now().date()
    deadline = today + timedelta(days=7)
    upcoming = []

    for sub in subscriptions:
        try:
            renewal_date = datetime.strptime(sub["renewal_date"], "%Y-%m-%d").date()
            if today <= renewal_date <= deadline:
                upcoming.append(sub)
        except (ValueError, KeyError):
            continue

    return upcoming