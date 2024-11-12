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






STATEMENTS AND EXPRESSIONS


# Expression to input age
age = int(input("Enter your age: "))  # Expression


# Statement to check if the person is eligible to vote
if age >= 18:  # Statement
    print("You are eligible to vote.")  # Statement
else:
    print("You are not eligible to vote.")  # Statement






BRANCHING AND DECISION MAKING 

# Get the student's score
score = int(input("Enter your score (0-100): "))

# Step 1: Using if statement

if score >= 90:
    print("Excellent! You've scored an A.")
    
# Step 2: Using if-else statement to check pass/fail

if score >= 50:
    print("You passed the exam.")
else:
    print("You failed the exam.")

    
# Step 3: Using if-elif-else statement for grade categorization

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Step 4: Nested if statement to check if the student needs improvement

if score < 50:
    print("You failed, but don't worry! You can improve with more practice.")
    if score < 30:
        print("Consider seeking extra help, your score is quite low.")
    else:
        print("You can pass with some effort, focus on areas of weakness.")
