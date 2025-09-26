# original list of pizza
pizzas = ['pepperoni', 'margherita', 'bbq chicken']

# making a copy of the list of pizza
friend_pizzas = pizzas[:]

# adding a new pizza to the original list
pizzas.append('hawaiian')

#Add a different pizza to the friend_pizzas list
friend_pizzas.append('veggie')

# Prove that you have two separate lists
print("My favorite pizzas are:")
for pizza in pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)