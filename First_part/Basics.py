INPUT 

user_input = input("Enter something: ")
user_input = int(input("Enter something: "))


OUTPUT
# Basic print statement
print("Hello, World!")

# Print variables
name = "Ananya"
age = 20
print("Name:", name)
print("Age:", age)

# Print multiple values
height = 5.5
is_active = True
print("Height:", height, "Active:", is_active)

# Print with string concatenation
greeting = "Hello"
message = "Welcome to Python!"
print(greeting + " " + message)

# Print with escape characters
print("This is a line\nThis is a new line")  # \n creates a new line
print("Tab space:\tIndented")  # \t adds a tab space

# Print with separators
print("Apple", "Banana", "Cherry", sep=", ")  # Using a comma as separator





DATATYPES

# Integer type
x = 10  # int
print(f"Integer: {x}, Type: {type(x)}")

# Floating-point type
y = 10.5  # float
print(f"Float: {y}, Type: {type(y)}")

# String type (for characters)
z = "Hello"  # str
print(f"String: {z}, Type: {type(z)}")

# Boolean type
is_true = True  # bool
print(f"Boolean: {is_true}, Type: {type(is_true)}")

# None type
nothing = None  # NoneType
print(f"None: {nothing}, Type: {type(nothing)}")

FSTRING 
# Variables
name = "Kruthi"
age = 40

# Using f-string to format the string
message = f"My name is {name}, I am {age} years old."

# Printing the result
print(message)





LISTS, TUPLES, DICTS, SETS

# List: Ordered, mutable collection
my_list = [1, 2, 3, 4]  # List of integers
my_list.append(5)  # Add an item to the list
print(f"List: {my_list}, Type: {type(my_list)}")

# Example of Slicing
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Syntax: list[start:end:step]
print(my_list[2:7])        # Output: [2, 3, 4, 5, 6]
print(my_list[:5])         # Output: [0, 1, 2, 3, 4] (from start to index 4)
print(my_list[5:])         # Output: [5, 6, 7, 8, 9] (from index 5 to the end)
print(my_list[::2])        # Output: [0, 2, 4, 6, 8] (every second element)
print(my_list[::-1])       # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed list)

# Example of Splicing
my_list[2:5] = [20, 30, 40]   # Replacing elements from index 2 to 4
print(my_list)                # Output: [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

# Inserting new elements using slicing
my_list[5:5] = [100, 200]     # Insert at index 5
print(my_list)                # Output: [0, 1, 20, 30, 40, 100, 200, 5, 6, 7, 8, 9]

# Deleting elements using slicing
my_list[2:4] = []             # Remove elements at index 2 and 3
print(my_list)                # Output: [0, 1, 40, 100, 200, 5, 6, 7, 8, 9]


# Tuple: Ordered, immutable collection
my_tuple = (10, 20, 30, 40)  # Tuple of integers
print(f"Tuple: {my_tuple}, Type: {type(my_tuple)}")

# Dictionary: Key-value pairs, unordered collection
my_dict = {"name": "Alice", "age": 25}  # Dictionary with keys and values
my_dict["city"] = "New York"  # Add a new key-value pair
print(f"Dictionary: {my_dict}, Type: {type(my_dict)}")

# Set: Unordered collection of unique items
my_set = {1, 2, 3, 4, 5}  # Set of integers
my_set.add(6)  # Add an item to the set
my_set.add(2)  # Trying to add a duplicate item (won't be added)
print(f"Set: {my_set}, Type: {type(my_set)}")


OPERATORS
1. ARITHMETIC
a = 10
b = 3

print("Addition:", a + b)        # Output: 13
print("Subtraction:", a - b)     # Output: 7
print("Multiplication:", a * b)  # Output: 30
print("Division:", a / b)        # Output: 3.3333
print("Floor Division:", a // b) # Output: 3 (quotient without remainder)
print("Modulus:", a % b)         # Output: 1 (remainder)
print("Exponent:", a ** b)       # Output: 1000 (10^3)

2. COMPARISION
x = 5
y = 10

print("Equal:", x == y)          # Output: False
print("Not Equal:", x != y)      # Output: True
print("Greater Than:", x > y)    # Output: False
print("Less Than:", x < y)       # Output: True
print("Greater or Equal:", x >= y) # Output: False
print("Less or Equal:", x <= y)  # Output: True

3. LOGICAL
a = True
b = False

print("AND:", a and b)           # Output: False
print("OR:", a or b)             # Output: True
print("NOT:", not a)             # Output: False



STATEMENTS AND EXPRESSIONS


# Expression to input age
age = int(input("Enter your age: "))  # Expression


# Statement to check if the person is eligible to vote
if age >= 18:  # Statement
    print("You are eligible to vote.")  # Statement
else:
    print("You are not eligible to vote.")  # Statement

