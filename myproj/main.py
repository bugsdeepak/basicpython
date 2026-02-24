# Python is a high-level, interpreted programming language that emphasizes code readability and simplicity. supports multiple programming paradigms, including procedural, object-oriented, and functional programming. It has a large standard library and a vibrant ecosystem of third-party packages, making it a popular choice for various applications such as web development, data analysis, machine learning, automation, and more.
# This is the main file of the project. It contains the main function and the main logic of the program.
# Python 3.10+ supports type hints, which allow you to specify the expected data types of variables, function parameters, and return values. This can help improve code readability and catch potential type-related errors during development.
# Python is a dynamically typed language, which means that you don't have to declare the type of variable when you create it. However, using type hints can provide additional information about the expected types and can be helpful for code editors and static analysis tools.
# Python uses indentation to define code blocks, which is a key feature of the language. Proper indentation is crucial for the correct execution of Python code.

print("Hello World")

# Variables - Date type is optional and inferred: Data Types - int, float, str, bool, list, set, tuple, dict
# END OF STATEMENT - NEW LINE - NO SEMICOLON NEEDED
positive_integer = 10
negative_integer = -5
number: int = 22
decimal : float = 5.012345678901234567890123456789
print("Decimal:",  decimal) # Truncates to 15 decimal places by default when printed, but retains full precision internally.
name1: str = "hello world" # Double quotes
name2: str = 'hello world' # or single quotes
active : bool = True # or False

# Data Structures
names: list[str] = ["Alice", "Bob", "Charlie"] # Mutable ordered collection of items
unique : set[int] = { 2, 3, 5, 1, 89, 3, 5, 1, "antony" }  # Set will automatically remove duplicates.
# Data types can be mixed, but it's generally recommended to use a single data type for sets to avoid confusion. Sets are mutable and unordered collections of unique items.
print(unique)
coordinates : tuple[float, float] = (1.5, 3.5) # Immutable ordered collection of items
coordinates2 : tuple = (3, 3.5)
# Dictionary database
ages: dict[str, int] = {"Alice": 30, "Bob": 25, "Charlie": 35} # Dictionary is a collection of key-value pairs, where each key is unique and maps to a value. It is mutable and unordered.

# Function definition
def greet(name: str) -> None: # Function that takes a string argument and returns nothing (void)
    # F String - Formatted string literals, allow to embed expressions inside string literals, using curly braces {}. They provide a convenient and readable way to format strings.
    print(f"Hello {name}! How are you")


# Function Invocation
greet("Deepak")