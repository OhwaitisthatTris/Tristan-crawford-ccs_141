import matplotlib.pyplot as plt
import random

class RandomWalk:
	"""A simple class to generate random walks."""
	def __init__(self, num_points=5000):
		self.num_points = num_points
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		"""Calculate all the points in the walk."""
		while len(self.x_values) < self.num_points:
			x_direction = random.choice([1, -1])
			x_distance = random.choice([0, 1, 2, 3, 4])
			x_step = x_direction * x_distance

			y_direction = random.choice([1, -1])
			y_distance = random.choice([0, 1, 2, 3, 4])
			y_step = y_direction * y_distance

			if x_step == 0 and y_step == 0:
				continue

			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)

# Make a random walk.
rw = RandomWalk(5000)
rw.fill_walk()

# Plot the points in the walk.
plt.figure(figsize=(10, 6))
plt.scatter(rw.x_values, rw.y_values, c=range(rw.num_points), cmap=plt.cm.Blues, s=15)
plt.title("Random Walk with 5,000 Points", fontsize=24)
plt.xlabel("X", fontsize=15)
plt.ylabel("Y", fontsize=15)
plt.show()

# Modify to use ax.plot()
plt.figure(figsize=(10, 6))
ax = plt.gca()
ax.plot(rw.x_values, rw.y_values, linewidth=0.5, color='blue')
ax.set_title("Random Walk with 5,000 Points", fontsize=24)
ax.set_xlabel("X", fontsize=15)
ax.set_ylabel("Y", fontsize=15)
plt.show()