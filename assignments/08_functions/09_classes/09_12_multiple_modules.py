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
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0

class Privileges:
    def __init__(self, privileges):
        """Initialize the privileges attribute."""
        self.privileges = privileges

    def show_privileges(self):
        """Print the list of privileges."""
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize attributes of the parent class. Then initialize attributes specific to an admin."""
        super().__init__(first_name, last_name, age, location, occupation)
        self.privileges = Privileges(["can add post", "can delete post", "can ban user", "can manage users"])

if __name__ == "__main__":
    admin = Admin("Tristan", "Crawford", 18, "pennsylvania", "Administrator")

    # Call the show_privileges method to show that everything is working correctly
    admin.privileges.show_privileges()