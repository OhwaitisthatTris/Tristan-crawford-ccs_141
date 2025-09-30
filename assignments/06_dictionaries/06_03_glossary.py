glossary = {
    "variable": "A storage location paired with a name that holds data which can change during program execution.",
    "function": "A block of organized, reusable code that performs a specific task when called.",
    "loop": "A control structure that repeats a block of code as long as a specified condition is true.",
    "dictionary": "A collection of key-value pairs where each key is unique and used to access its corresponding value.",
    "list": "An ordered collection of items which can be of different data types and can be changed after creation."
}

# Print each word and its meaning with formatting
for word, meaning in glossary.items():
    print(f"{word.capitalize()}:\n  {meaning}\n")
