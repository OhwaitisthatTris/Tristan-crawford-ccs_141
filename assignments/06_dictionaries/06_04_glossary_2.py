glossary = {
    "variable": "A storage location paired with a name that holds data which can change during program execution.",
    "function": "A block of organized, reusable code that performs a specific task when called.",
    "loop": "A control structure that repeats a block of code as long as a specified condition is true.",
    "dictionary": "A collection of key-value pairs where each key is unique and used to access its corresponding value.",
    "list": "An ordered collection of items which can be of different data types and can be changed after creation.",
    "tuple": "An ordered, immutable collection of items, meaning its contents cannot be changed after creation.",
    "set": "An unordered collection of unique elements, often used to test membership or remove duplicates.",
    "class": "A blueprint for creating objects, encapsulating data and behavior in object-oriented programming.",
    "module": "A file containing Python definitions and statements intended for use in other Python programs.",
    "exception": "An event that occurs during execution that disrupts the normal flow of instructions, often handled with try-except blocks."}
    # Use a loop to print all terms and their meanings
for term, definition in glossary.items():
    print(f"{term.capitalize()}:\n  {definition}\n")