"""Give gardening advice based on the month entered by the user."""

# Store each month's season and gardening advice in one dictionary.
GARDENING_ADVICE = {
    "december": ("Winter", "Protect plants from cold weather."),
    "january": ("Winter", "Protect plants from cold weather."),
    "february": ("Winter", "Protect plants from cold weather."),
    "march": ("Spring", "Start planting suitable flowers and vegetables."),
    "april": ("Spring", "Start planting suitable flowers and vegetables."),
    "may": ("Spring", "Start planting suitable flowers and vegetables."),
    "june": ("Summer", "Water plants regularly."),
    "july": ("Summer", "Water plants regularly."),
    "august": ("Summer", "Water plants regularly."),
    "september": ("Autumn", "Remove dead leaves and prepare plants for colder weather."),
    "october": ("Autumn", "Remove dead leaves and prepare plants for colder weather."),
    "november": ("Autumn", "Remove dead leaves and prepare plants for colder weather."),
}


def get_gardening_advice(month):
    """Return gardening advice for a valid month, or an error message."""
    if not isinstance(month, str):
        return "Invalid month. Please enter a valid month."

    month = month.strip().lower()
    if month not in GARDENING_ADVICE:
        return "Invalid month. Please enter a valid month."

    season, advice = GARDENING_ADVICE[month]
    return f"{season} gardening: {advice}"


def main():
    """Ask for a month and print the matching gardening advice."""
    month = input("Enter the current month: ")
    print(get_gardening_advice(month))


if __name__ == "__main__":
    main()
