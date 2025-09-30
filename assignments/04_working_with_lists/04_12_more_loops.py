# Lists of foods
foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = foods[:]

#Add a new food to each list
foods.append('cannoli')

#Add a different food to the friend_foods list
friend_foods.append('ice cream')

# Print each list of foods using for loop
print("My favorite foods are:")
for food in foods:
    print("- " + food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print("- " + food)