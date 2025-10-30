class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range_miles = 150
        elif self.battery_size == 65:
            range_miles = 225
        else:
            range_miles = 0
        print(f"This car can go about {range_miles} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery if it isn't already at 65 kWh."""
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("The battery is already at its maximum capacity.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class. Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()

# Create an instance of the ElectricCar class
my_tesla = ElectricCar('tesla', 'model s', 2019)

# Call get_range() once
print("Range before upgrading the battery:")
my_tesla.battery.get_range()

# Upgrade the battery
my_tesla.battery.upgrade_battery()

# Call get_range() a second time after upgrading the battery
print("\nRange after upgrading the battery:")
my_tesla.battery.get_range()

