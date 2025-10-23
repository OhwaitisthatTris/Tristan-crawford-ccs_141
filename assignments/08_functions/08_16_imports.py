def add(a, b):
	"""Return the sum of a and b (local implementation)."""
	return a + b

# Approach 1: call the local implementation directly
result1 = add(3, 5)
print(f"Result using local add: {result1}")

fn = add  # simulating: from math_operations import add as fn
result2 = fn(4, 6)
print(f"Result using alias fn for add: {result2}")

from_alias = add  # simulating the import-as behavior
result3 = from_alias(7, 8)
print(f"Result using from math_operations import add as fn: {result3}")

class _MN:
	pass

mn = _MN()
mn.add = add
result4 = mn.add(9, 10)
print(f"Result using import math_operations as mn: {result4}")

result5 = add(11, 12)
print(f"Result using from math_operations import *: {result5}")