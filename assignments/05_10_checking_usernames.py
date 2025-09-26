current_users = ['admin', 'Tristan', 'owl', 'Niomi', 'Mila']

# List of new usernames
new_users = ['john', 'Alice', 'owl', 'Bob', 'admin']

# Create a copy of current_users with all usernames in lowercase
current_users_lower = [user.lower() for user in current_users]

# Loop through the new_users list to check for unique usernames
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")