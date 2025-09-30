favorite_places = {
    "Tristan": ["Hawaii", "Paris", "Tokyo"],
    "Niomi": ["New York"],
    "Ethan": ["Sydney", "Barcelona"]
}

# Loop through the dictionary and print each person's favorite places
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f" - {place}")
    print()  # Blank line for better readability