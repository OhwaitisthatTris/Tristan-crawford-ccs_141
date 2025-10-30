class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a summary of the restaurant."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant1 = Restaurant("Tasty Bites", "Italian")
restaurant2 = Restaurant("Spicy tacos", "Mexican")
restaurant3 = Restaurant("Fresh Greens", "Vegan")

restaurant1.describe_restaurant()
print()  
restaurant2.describe_restaurant()
print()  
restaurant3.describe_restaurant()