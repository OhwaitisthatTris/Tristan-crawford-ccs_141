def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('tesla', 'model 3', color='red', autopilot=True)

# Print the dictionary to verify the information
print(car)