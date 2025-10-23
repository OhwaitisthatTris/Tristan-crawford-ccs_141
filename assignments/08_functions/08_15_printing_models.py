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

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'hanging pendant', 'dodecahedron']
completed_models = []

print_model(unprinted_designs, completed_models)

# Display all completed models.
show_completed_models(completed_models)