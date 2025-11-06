import matplotlib.pyplot as plt
from random import randint

def roll_dice(num_rolls, sides=6, num_dice=3):

    results = []
    for _ in range(num_rolls):
        roll_sum = sum(randint(1, sides) for _ in range(num_dice))
        results.append(roll_sum)
    return results

def plot_results(results, num_rolls, sides=6, num_dice=3):
    """Plot the results of rolling multiple dice."""
    plt.figure(figsize=(10, 6))
    min_sum = num_dice
    max_sum = num_dice * sides

    plt.hist(results, bins=range(min_sum, max_sum + 2), edgecolor='black', align='left')
    plt.title(f'Results of Rolling {num_dice} {sides}-sided Dice {num_rolls} Times', fontsize=24)
    plt.xlabel(f'Sum of {num_dice} Dice', fontsize=14)
    plt.ylabel('Frequency of Result', fontsize=14)
    plt.xticks(range(min_sum, max_sum + 1))
    plt.show()