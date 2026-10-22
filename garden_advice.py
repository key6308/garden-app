# TODO 1: Create a function to organize the gardening advice.
# TODO 2: Add documentation to explain how the program works.
# TODO 3: Replace hardcoded advice with a dictionary.

month = input("Enter the current month: ").strip().lower()

if month in ["december", "january", "february"]:
    print("Winter gardening: Protect plants from cold weather.")

elif month in ["march", "april", "may"]:
    print("Spring gardening: Start planting suitable flowers and vegetables.")

elif month in ["june", "july", "august"]:
    print("Summer gardening: Water plants regularly.")

elif month in ["september", "october", "november"]:
    print("Autumn gardening: Remove dead leaves and prepare plants for colder weather.")

else:
    print("Please enter a valid month.")
