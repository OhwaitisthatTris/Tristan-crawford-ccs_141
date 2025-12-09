import os
filename = 'learning_python.txt'

if not os.path.exists(filename):
    print(f"Error: file '{filename}' not found.")
else:
    with open(filename) as file_object:
        contents = file_object.read()
        print("\nReading the entire file:\n")
        print(contents)

    print("\nReading the file line by line:\n")
    with open(filename) as file_object:
        for line in file_object:
            print(line.rstrip())

    print("\nStoring the lines in a list and printing each line:\n")
    with open(filename) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())