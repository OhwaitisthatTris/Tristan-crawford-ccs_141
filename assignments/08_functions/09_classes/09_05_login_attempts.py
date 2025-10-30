class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize the user profile attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0  # Initialize login attempts to 0

    def describe_user(self):
        """Print a summary of the user’s information."""
        print(f"User Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0

user = User("Alice", "Smith", 30, "New York", "Engineer")

# Call increment_login_attempts() several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"Login attempts after incrementing: {user.login_attempts}")

user.reset_login_attempts()

print(f"Login attempts after resetting: {user.login_attempts}")