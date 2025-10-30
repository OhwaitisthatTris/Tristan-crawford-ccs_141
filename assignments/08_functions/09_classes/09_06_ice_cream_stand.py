class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name, cuisine type, and number served attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        """Set the number of customers served to the given value."""
        if number_served >= 0:
            self.number_served = number_served
        else:
            print("Number served cannot be negative.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors=None):
        super().__init__(restaurant_name, cuisine_type)
        # Ensure flavors is always stored as a list; accept None, a single flavor string, or an iterable of flavors.
        if flavors is None:
            self.flavors = []
        elif isinstance(flavors, (list, tuple, set)):
            self.flavors = list(flavors)
        else:
            # single string or other single value -> wrap in list
            self.flavors = [flavors]

    def display_flavors(self):
        """Print the list of ice cream flavors."""
        print(f"Ice cream flavors available at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")