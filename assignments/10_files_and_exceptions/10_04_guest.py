username = input("Please enter your name: ")

with open('assignments/10_files_and_exceptions/guest.txt', 'w') as file_object:
    file_object.write(username)

print(f"Thank you, {username}! Your name has been written to guest.txt.")