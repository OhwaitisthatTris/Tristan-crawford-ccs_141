# Ask the user how many people are in their dinner group
num_people = int(input("How many people are in your dinner group? "))

# Check the number of people and print the appropriate message
if num_people > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")