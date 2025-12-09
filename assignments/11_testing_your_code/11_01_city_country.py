import os

def read_file_and_print(filename):
    try:
        with open(filename) as file:
            contents = file.read()
            print(contents.lower().count('at'))
    except FileNotFoundError:
        pass
    except IsADirectoryError:
        # skip directories if accidentally passed here
        pass

filenames = ['assignments/11_testing_your_code/city_country_project/']

for filename in filenames:
    if os.path.isdir(filename):
        for entry in os.listdir(filename):
            path = os.path.join(filename, entry)
            if os.path.isfile(path):
                read_file_and_print(path)
    else:
        read_file_and_print(filename)