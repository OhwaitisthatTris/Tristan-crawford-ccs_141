# Dictionary of cities with nested dictionaries for details
cities = {
    "Tokyo": {
        "country": "Japan",
        "population": "37 million",
        "fact": "It is the largest metropolitan area in the world."
    },
    "Paris": {
        "country": "France",
        "population": "11 million",
        "fact": "Known as the 'City of Light' and famous for the Eiffel Tower."
    },
    "Cairo": {
        "country": "Egypt",
        "population": "20 million",
        "fact": "Home to the Great Pyramid of Giza, one of the Seven Wonders of the Ancient World."
    }
}

# Loop through cities and print info
for city, info in cities.items():
    print(f"City: {city}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")
