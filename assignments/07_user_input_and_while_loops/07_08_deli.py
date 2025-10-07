sandwich_orders = ['tuna', 'turkey', 'club', 'BLT', 'pastrami', 'grilled cheese', 'pastrami']

# List to keep track of finished sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\nThe following sandwiches have been made by Tristan:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")