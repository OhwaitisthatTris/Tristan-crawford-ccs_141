import matplotlib.pyplot as plt
from random import randint

def roll_and_multiply_dice(num_rolls, sides=6):
    """Simulate rolling two dice and multiplying the results."""
    results = []
    for _ in range(num_rolls):
        die1 = randint(1, sides)
        die2 = randint(1, sides)
        results.append(die1 * die2)
    return results

def plot_results(results, num_rolls, sides=6):
    """Plot the results of multiplying two dice rolls."""
    plt.figure(figsize=(10, 6))
    plt.hist(results, bins=range(1, 37), edgecolor='black', align='left')
    plt.title(f'Results of Multiplying Two {sides}-sided Dice {num_rolls} Times', fontsize=24)
    plt.xlabel('Product of Two Dice', fontsize=14)
    plt.ylabel('Frequency of Result', fontsize=14)
    plt.xticks(range(1, 37))
    plt.show()

# Simulate rolling two six-sided dice 1,000 times and multiplying the results
num_rolls = 1000
sides = 6
results = roll_and_multiply_dice(num_rolls, sides)

# Plot the results
plot_results(results, num_rolls, sides)