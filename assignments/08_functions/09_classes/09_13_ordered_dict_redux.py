import random

class Die:
    def __init__(self, sides=6):
        """Initialize the die with a default of 6 sides."""
        self.sides = sides

    def roll_die(self):
        """Roll the die and print a random number between 1 and the number of sides."""
        print(random.randint(1, self.sides))

# Create an instance of the Die class with 6 sides
dice = Die()

# Roll the die 10 times
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    dice.roll_die()
    