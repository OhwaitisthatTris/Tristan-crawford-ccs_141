def read_file_and_print(filename):
    try:
        with open(filename) as file:
            contents = file.read()
            print(contents.lower().count('at'))
    except FileNotFoundError:
        pass

filenames = ['assignments/10_files_and_exceptions/frankenstine.txt']

for filename in filenames:
    read_file_and_print(filename)