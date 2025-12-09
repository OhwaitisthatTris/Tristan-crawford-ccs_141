def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Sorry, that's not a valid number. Please enter a whole number.")

def main():
    while True:
        num1 = get_number("Please enter the first number (or type 'quit' to finish): ")

        if num1 == 'quit':
            break

        num2 = get_number("Please enter the second number (or type 'quit' to finish): ")

        if num2 == 'quit':
            break

        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}.")

    print("Thank you for using the number adder!")

if __name__ == "__main__":
    main()