# Extended cities dictionary with new key 'area' (in square km) and population as integer
cities = {
    "Tokyo": {
        "country": "Japan",
        "population": 37000000,  # Approximate metro area population
        "area": 2191,  # in sq km
        "fact": "Largest metropolitan area in the world."
    },
    "Paris": {
        "country": "France",
        "population": 11000000,
        "area": 105,
        "fact": "Known as the 'City of Light' and famous for the Eiffel Tower."
    },
    "Cairo": {
        "country": "Egypt",
        "population": 20000000,
        "area": 3085,
        "fact": "Home to the Great Pyramid of Giza, one of the Seven Wonders of the Ancient World."
    }
}

# Loop through cities and print extended info with population density
for city, info in cities.items():
    population_density = info["population"] / info["area"]
    print(f"City: {city}")
    print(f"  Country:           {info['country']}")
    print(f"  Population:        {info['population']:,}")  # Format with commas
    print(f"  Area (sq km):      {info['area']}")
    print(f"  Population Density:{population_density:,.2f} people per sq km")
    print(f"  Fact:              {info['fact']}\n")
