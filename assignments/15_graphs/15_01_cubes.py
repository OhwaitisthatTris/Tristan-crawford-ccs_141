import matplotlib.pyplot as plt

# Generate the first 5,000 cubic numbers
n = 5000
cubic_numbers = [i**3 for i in range(1, n + 1)]

# Plotting the first 5 cubic numbers
plt.figure(figsize=(10, 5))
plt.plot(cubic_numbers[:5], 'ro-', label='First 5 Cubic Numbers')
plt.title('First 5 Cubic Numbers')
plt.xlabel('Index')
plt.ylabel('Cubic Number')
plt.legend()
plt.show()

# Plotting the first 5,000 cubic numbers
plt.figure(figsize=(12, 6))
plt.plot(cubic_numbers, 'b-', label='First 5,000 Cubic Numbers')
plt.title('First 5,000 Cubic Numbers')
plt.xlabel('Index')
plt.ylabel('Cubic Number')
plt.legend()
plt.show()