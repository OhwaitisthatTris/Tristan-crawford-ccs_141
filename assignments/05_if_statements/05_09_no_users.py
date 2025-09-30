usernames = ['admin', 'Tristan', 'owl', 'Niomi', 'Mila']

# Check if the list is empty
if usernames:
    # Loop through the list and print a greeting to each user
    for username in usernames:
        if username == 'admin':
            print(f"Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")