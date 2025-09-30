# Generate a list of the first 40 cubes using
cubes = [i**3 for i in range(1, 41)]

#print the list of cubes
print("The first 40 cubes:")
print(cubes)

# print the first three items in the list
print("\nThe first three cubes are:")
print(cubes[:3])

#print the middle three items in the list
middle_index = len(cubes) // 2
print("\nThe middle three cubes are:")
print(cubes[middle_index - 1: middle_index + 2])

# print the last three items in the list
print("\nThe last three cubes are:")
print(cubes[-3:])