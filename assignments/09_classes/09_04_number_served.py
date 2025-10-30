class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name, cuisine type, and number served attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  
    def describe_restaurant(self):
        """Print a summary of the restaurant."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        if additional_served >= 0:
            self.number_served += additional_served
        else:
            print("You can't serve a negative number of customers.")

restaurant = Restaurant("Tasty Bites", "Italian")

print(f"Number of customers served: {restaurant.number_served}")

restaurant.number_served = 10
print(f"Updated number of customers served: {restaurant.number_served}")

restaurant.set_number_served(20)
print(f"Number of customers served after using set_number_served: {restaurant.number_served}")

restaurant.increment_number_served(5)
print(f"Number of customers served after incrementing: {restaurant.number_served}")