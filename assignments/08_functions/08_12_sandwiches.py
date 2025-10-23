def make_sandwich(*items):
    """Print a summary of the sandwich being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('ham', 'cheese', 'tomato')
make_sandwich('turkey', 'lettuce', 'mayo')
make_sandwich('peanut butter', 'jelly')