# Loop to ask users their age and tell them the cost of their movie ticket
while True:
    age = input("Please enter your age (or type 'quit' to finish): ")

    if age.lower() == 'quit':
        break

    try:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif 3 <= age <= 12:
            print("The cost of your movie ticket is $10.")
        else:
            print("The cost of your movie ticket is $15.")
    except ValueError:
        print("Please enter a valid age or 'quit' to finish.")

print("Thank you for using Tristan's movie ticket calculator!")