
def get_gardening_advice(season, plant_type):
    """Give gardening advice based on the season and plant type."""

    # Start an empty list to store the advice.
    advice = []

    # Give advice based on the current season.
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

    # Add advice based on the type of plant.
    if plant_type == "flower":
        advice.append("Use fertiliser to help your flowers grow and bloom.")
    elif plant_type == "vegetable":
        advice.append("Keep an eye out for pests and check your vegetables regularly.")
    else:
        advice.append("I don't have specific advice for that type of plant yet.")

    # Return all advice as one string.
    return "\n".join(advice)


def main():
    """Ask the user questions and print gardening advice."""

    # Welcome the user to the program.
    print("Welcome to the Garden Advice Program!")

    # Get the user's answers and remove extra spaces.
    season = input("What season is it? ").lower().strip()
    plant_type = input("What type of plant do you have (flower or vegetable)? ").lower().strip()

    # Generate and display the gardening advice.
    advice = get_gardening_advice(season, plant_type)

    print("\nHere is your gardening advice:")
    print(advice)


# Run the program when this file is opened directly.
if __name__ == "__main__":
    main()
