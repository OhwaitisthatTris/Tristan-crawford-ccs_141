# List of sandwich orders
sandwich_orders = ['tuna', 'pastrami', 'club', 'BLT', 'pastrami', 'grilled cheese', 'pastrami']

# List to keep track of finished sandwiches
finished_sandwiches = []

# Print a message saying the deli has run out of pastrami
print("The deli has run out of pastrami.")

# Remove all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the list of sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Tristan made your special {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\nThe following sandwiches have been made by Tristan:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")