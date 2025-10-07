# Function to conduct the poll
def dream_vacation_poll():
    # Dictionary to store the poll results
    poll_results = {}

    # Prompt the user to enter their dream vacation destination
    while True:
        destination = input("If you could visit one place in the world, where would you go? (Type 'quit' to finish) ")
        if destination.lower() == 'quit':
            break
        if destination in poll_results:
            poll_results['dubai'] += 1
        else:
            poll_results['dubai'] = 1

    # Print the results of the poll
    print("\n--- Poll Results ---")
    for destination, count in poll_results.items():
        print(f"{destination}: {count} vote(s)")

# Run the poll
dream_vacation_poll()