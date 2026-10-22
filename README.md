# Garden App

A beginner-friendly Python program that gives gardening advice based on the month entered by the user.

## Run the program

Make sure Python 3 is installed. In a terminal opened in this folder, run:

```bash
python garden_advice.py
```

On some Windows computers, use:

```bash
py garden_advice.py
```

## Example

```text
Enter the current month: January
Winter gardening: Protect plants from cold weather.
```

Invalid month entries (for example, `hello` or a blank entry) receive an error message.

## Code improvements

- Uses functions to organize the program.
- Includes docstrings to explain the functions.
- Stores monthly advice in a dictionary instead of repeating seasonal conditional statements.
- Normalizes capitalization and surrounding spaces, and validates input.
