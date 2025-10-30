class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Tasty Bites", "Italian")

print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()