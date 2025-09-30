favorite_numbers = {
    "Alice": [7, 42],
    "Bob": [3, 14, 27],
    "Charlie": [99],
    "Diana": [10, 20, 30],
    "Ethan": [1, 2]
}

# Loop through the dictionary and print each person's favorite numbers
for person, numbers in favorite_numbers.items():
    numbers_str = ", ".join(str(num) for num in numbers)
    print(f"{person}'s favorite numbers are: {numbers_str}")
