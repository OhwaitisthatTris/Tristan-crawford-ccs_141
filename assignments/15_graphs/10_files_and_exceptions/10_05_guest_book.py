names = []

while True:
    name = input("Please enter your name (or type 'quit' to finish): ")
    if name.lower() == 'quit':
        break
    names.append(name)

with open('guest_book.txt', 'w') as file_object:
    for name in names:
        file_object.write(name + '\n')

print("Thank you! All names have been written to guest_book.txt.")