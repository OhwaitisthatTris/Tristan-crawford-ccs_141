pet1 = {
    "animal": "dog",
    "owner": "Tristan"
}

pet2 = {
    "animal": "cat",
    "owner": "Bob"
}

pet3 = {
    "animal": "parrot",
    "owner": "Charlie"
}

pet4 = {
    "animal": "hamster",
    "owner": "Diana"
}

# List of all pet dictionaries
pets = [pet1, pet2, pet3, pet4]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"Animal: {pet['animal'].capitalize()}")
    print(f"Owner: {pet['owner']}\n")