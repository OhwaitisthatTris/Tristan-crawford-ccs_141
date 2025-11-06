import matplotlib.pyplot as plt
import numpy as np

# Generate the first 5,000 cubic numbers
n = 5000
cubic_numbers = [i**3 for i in range(1, n + 1)]

# Create a scatter plot with a colormap
plt.figure(figsize=(12, 6))
sc = plt.scatter(range(1, n + 1), cubic_numbers, c=cubic_numbers, cmap='viridis', s=10, alpha=0.5)
plt.colorbar(sc, label='Cubic Number')
plt.title('First 5,000 Cubic Numbers with Colormap')
plt.xlabel('Index')
plt.ylabel('Cubic Number')
plt.show()