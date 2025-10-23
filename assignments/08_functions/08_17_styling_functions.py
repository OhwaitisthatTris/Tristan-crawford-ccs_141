def print_model(unprinted_designs, printed_models):
    """Simulate printing each design, until none are left."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        printed_models.append(current_design)

def show_completed_models(printed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for printed_model in printed_models:
        print(printed_model)

        # Import the functions from printing_functions.py
from printing_functions import print_model, show_completed_models

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design.
print_model(unprinted_designs, completed_models)

# Display all completed models.
show_completed_models(completed_models)

# Import the build_profile function from user_profile.py
from user_profile import build_profile

# Build a profile for a user
user_profile = build_profile(
    'Alice',  # First name
    'Smith',  # Last name
    location='New York',  # Additional key-value pair
    field='Data Science',  # Additional key-value pair
    hobby='Hiking'  # Additional key-value pair
)

# Print the profile
print(user_profile)