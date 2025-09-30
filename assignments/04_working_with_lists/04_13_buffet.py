# Tuple of five basic foods
menu = ('pizza', 'pasta', 'salad', 'soup', 'breadsticks')

# Use a for loop to print each food the restaurant offers
print("original menu:")
for food in menu:
    print("- " + food)

# Try to modify one of the items (this will raise an error)
try:
    menu[0] = 'sushi'
except TypeError as e:
    print("\nAttempt to modify the tuple:")
    print(e)
# The restaurant changes its menu, replace two items
menu = ('sushi', 'ramen', 'salad', 'soup', 'breadsticks')

# use a for loop to print each food the restaurant now offers
print("\nUpdated menu:")
for food in menu:
    print("- " + food)
    print("- " + food)