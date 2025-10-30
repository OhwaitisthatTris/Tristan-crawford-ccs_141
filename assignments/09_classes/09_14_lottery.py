import random

numbers_and_letters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

winning_items = random.sample(numbers_and_letters, 4)

print("Winning items: ", winning_items)
print("Any ticket matching these 4 numbers or letters wins a prize!")