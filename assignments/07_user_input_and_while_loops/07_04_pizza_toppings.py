# Initialize an empty list to store pizza toppings
pizza_toppings = []

# Simulate user input
user_inputs = ["cheese", "toppings", "quit"]

# Prompt the user to enter pizza toppings
for topping in user_inputs:
    if topping.lower() == 'quit':
        break

    pizza_toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

# Print a summary of the pizza toppings
print("\nYour pizza will have the following toppings:")
for topping in pizza_toppings:
    print(f"- {topping}")