import matplotlib.pyplot as plt
import random

def roll_die():
    """Simulate rolling a six-sided die."""
    return random.randint(1, 6)

def plot_die_rolls(num_rolls):
    """Plot the results of rolling a die multiple times."""
    rolls = [roll_die() for _ in range(num_rolls)]
    plt.figure(figsize=(10, 6))
    plt.hist(rolls, bins=range(1, 8), edgecolor='black', align='left')
    plt.title('Die Roll Simulation', fontsize=24)
    plt.xlabel('Die Face', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xticks(range(1, 7))
    plt.show()

# Simulate rolling a die 1,000 times
num_rolls = 1000
plot_die_rolls(num_rolls)