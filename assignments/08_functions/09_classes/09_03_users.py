class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize the user profile attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation

    def describe_user(self):
        """Print a summary of the user’s information."""
        print(f"User Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back.")

# Create several instances representing different users
user1 = User("Niomi", "Milan", 18, "pennsylvania", "Nurse")
user2 = User("Tristan", "Crawford", 18, "Pennsylvania", "Millionare")
user3 = User("Charlie", "Williams", 35, "Chicago", "Teacher")


user1.describe_user()
print()  
user1.greet_user()
print() 

user2.describe_user()
print() 
user2.greet_user()
print() 

user3.describe_user()
print()  
user3.greet_user()