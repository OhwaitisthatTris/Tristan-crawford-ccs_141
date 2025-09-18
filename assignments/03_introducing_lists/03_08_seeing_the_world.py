places= ["Tokyo", "New York", "Paris", "London", "Sydney"]

print("original list:", places)
print("sorted list:", places)
print ("original still:", places)

print ("reverse-sorted:", sorted(places, reverse=True))
print("original still:", places)

places.reverse()
print("reversed:", places)

places.reverse()
print("back to original order:", places)  

places.sort()
print("sorted permanetly:", places)

places.sort(reverse=True)
print("sorted permanetly in reverse:", places)