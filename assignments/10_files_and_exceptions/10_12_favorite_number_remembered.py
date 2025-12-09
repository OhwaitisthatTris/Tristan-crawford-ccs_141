import json

def get_stored_favorite_number():

    filename = 'favorite_number.json'
    try:
        with open(filename) as file_object:
            favorite_number = json.load(file_object)
        return favorite_number
    except FileNotFoundError:
        return None

def get_new_favorite_number():
    try:
        favorite_number = int(input("What is your favorite number? "))
        filename = 'favorite_number.json'
        with open(filename, 'w') as file_object:
            json.dump(favorite_number, file_object)
        return favorite_number
    except ValueError:
        print("That's not a valid number. Please try again.")
        return None

def greet_user():
    favorite_number = get_stored_favorite_number()

    if favorite_number:
        print(f"I know your favorite number! It’s {favorite_number}.")
    else:
       
        while True:
            favorite_number = get_new_favorite_number()
            if favorite_number is not None:
                print(f"Your favorite number, {favorite_number}, has been saved!")
                break

greet_user()