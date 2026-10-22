
"""Give gardening advice based on the month."""

MONTHLY_ADVICE = {
    "january": "Winter gardening: Protect plants from cold weather.",
    "february": "Winter gardening: Prepare for spring and protect plants from frost.",
    "march": "Spring gardening: Start planting seeds and prepare your soil.",
    "april": "Spring gardening: Water plants regularly and remove weeds.",
    "may": "Spring gardening: Plant flowers and vegetables.",
    "june": "Summer gardening: Water plants regularly in hot weather.",
    "july": "Summer gardening: Keep plants watered and watch for pests.",
    "august": "Summer gardening: Harvest ripe vegetables and keep soil moist.",
    "september": "Autumn gardening: Plant cool-season crops and collect seeds.",
    "october": "Autumn gardening: Remove dead plants and prepare for winter.",
    "november": "Autumn gardening: Protect plants from frost.",
    "december": "Winter gardening: Protect plants from cold weather.",
}


def get_gardening_advice(month):
    """Return gardening advice for the selected month."""
    if not isinstance(month, str):
        return "Invalid month. Please enter a valid month."

    month = month.strip().lower()

    if month not in MONTHLY_ADVICE:
        return "Invalid month. Please enter a valid month."

    return MONTHLY_ADVICE[month]


def main():
    """Ask for a month and display the gardening advice."""
    month = input("Enter the current month: ")
    advice = get_gardening_advice(month)
    print(advice)


if __name__ == "__main__":
    main()
