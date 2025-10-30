class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name, cuisine type, and number served attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value for number of customers served

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


if __name__ == "__main__":
    # Create an instance of the Restaurant class
    restaurant = Restaurant("Tasty Bites", "Italian")

    # Call one of the Restaurant’s methods to show that the class works
    restaurant.describe_restaurant()

