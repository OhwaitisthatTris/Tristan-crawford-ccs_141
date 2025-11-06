import matplotlib.pyplot as plt
from random import randint

def roll_dice(num_rolls, sides=8):
    """Simulate rolling two dice with a given number of sides using list comprehension."""
    results = [randint(1, sides) + randint(1, sides) for _ in range(num_rolls)]
    return results

def plot_results(results, num_rolls, sides=8):
    """Plot the results of rolling two dice."""
    plt.figure(figsize=(10, 6))
    plt.hist(results, bins=range(2, 17), edgecolor='black', align='left')
    plt.title(f'Results of Rolling Two {sides}-sided Dice {num_rolls} Times', fontsize=24)
    plt.xlabel('Sum of Two Dice', fontsize=14)
    plt.ylabel('Frequency of Result', fontsize=14)
    plt.xticks(range(2, 17))
    plt.show()

# Simulate rolling two eight-sided dice 1,000 times
num_rolls = 1000
sides = 8
results = roll_dice(num_rolls, sides)

# Plot the results
plot_results(results, num_rolls, sides)