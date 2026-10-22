def get_gardening_advice(season, plant_type):
    """Give simple gardening advice based on the season and plant type."""

    advice = []

    if season == "summer":
        advice.append("Water your plants regularly and give them some shade.")
    elif season == "winter":
        advice.append("Protect your plants from frost with covers.")
    elif season == "spring":
        advice.append("Spring is a good time to plant new flowers and vegetables.")
    elif season == "autumn":
        advice.append("Clean up dead leaves and get your plants ready for colder weather.")
    else:
        advice.append("I don't have advice for that season yet.")

    if plant_type == "flower":
        advice.append("Use fertiliser to help your flowers grow and bloom.")
    elif plant_type == "vegetable":
        advice.append("Keep an eye out for pests and check your vegetables regularly.")
    else:
        advice.append("I don't have specific advice for that type of plant yet.")

    return "\n".join(advice)


def main():
    """Ask the user questions and print gardening advice."""

    print("Welcome to the Garden Advice Program!")

    season = input("What season is it? ").lower().strip()
    plant_type = input("What type of plant do you have (flower or vegetable)? ").lower().strip()

    advice = get_gardening_advice(season, plant_type)

    print("\nHere is your gardening advice:")
    print(advice)


if __name__ == "__main__":
    main()
