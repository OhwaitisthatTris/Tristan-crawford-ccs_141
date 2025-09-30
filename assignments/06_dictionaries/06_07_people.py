person1 = {
    "first_name": "Tristan",
    "last_name": "Crawford",
    "age": 18,
    "city": "Harrisburg"
}

# Dictionary for person 2
person2 = {
    "first_name": "Maya",
    "last_name": "Lopez",
    "age": 24,
    "city": "Seattle"
}

# Dictionary for person 3
person3 = {
    "first_name": "Ethan",
    "last_name": "Brown",
    "age": 30,
    "city": "Denver"
}

# List containing all three dictionaries
people = [person1, person2, person3]

# Loop through the list and print information about each person
for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")