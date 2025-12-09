def get_number(prompt):
    """Prompt the user for a number and handle ValueError."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Sorry, that's not a valid number. Please enter a whole number.")

num1 = get_number("Please enter the first number: ")

num2 = get_number("Please enter the second number: ")

result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}.")