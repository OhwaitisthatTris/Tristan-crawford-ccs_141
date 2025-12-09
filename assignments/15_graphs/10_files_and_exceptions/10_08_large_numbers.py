def read_file_and_print(filename):
    """Read the contents of a file and print it to the console."""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            print(f"--- Contents of {filename} ---")
            print(contents.strip())
    except FileNotFoundError:
        print(f"Sorry, the file {filename} was not found.")

filenames = ['assignments/10_files_and_exceptions/cats.txt', 'assignments/10_files_and_exceptions/dogs.txt']

for filename in filenames:
    read_file_and_print(filename)