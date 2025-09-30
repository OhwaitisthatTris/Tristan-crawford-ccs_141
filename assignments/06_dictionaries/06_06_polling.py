# Existing dictionary of people who have taken the poll and their favorite languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# List of people who should take the poll (some are already in the dictionary, some are not)
people_to_poll = ['jen', 'mike', 'sarah', 'alex', 'phil', 'emma']

# Loop through each person in the list
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.capitalize()}, for taking the poll.")
    else:
        print(f"{person.capitalize()}, please take the favorite languages poll!")