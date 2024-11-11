# Defining a basic function that greets the user
def greet():
    print("Hello! Welcome to learning functions in Python.")

# Calling the function
greet()


# Defining a function that takes a parameter
def greet_user(name):
    print(f"Hello, {name}! Nice to meet you.")

# Calling the function with an argument
greet_user("Alice")

# Defining a function that adds two numbers and returns the result
def add_numbers(a, b):
    result = a + b
    return result

# Using the return value
sum_result = add_numbers(5, 3)
print("The sum is:", sum_result)