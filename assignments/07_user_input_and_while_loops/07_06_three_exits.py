active = True

# Ask the user what kind of rental car they would like
while active:
    car_type = input("What kind of rental car would you like? (Type 'quit' to finish) ")
    if car_type.lower() == 'quit':
        active = False
    else:
        print(f"Let me see if I can find you a {car_type}.")