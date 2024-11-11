# String traversal using for loop
text = "Hello, World!"

# Simple iteration over characters
for char in text:
    print(char)

# Iterating with index using range()
for i in range(len(text)):
    print(f"Index {i}: {text[i]}")

# String traversal using while loop
index = 0
while index < len(text):
    print(text[index])
    index += 1

# Examples of range() function
# 1. Basic usage:
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# 2. Specifying start and end:
for i in range(2, 7):
    print(i)  # Output: 2 3 4 5 6

# 3. Specifying step size:
for i in range(0, 10, 2):
    print(i)  # Output: 0 2 4 6 8

#Same output with for and while loop

# Example: Printing numbers from 1 to 5

# Using a for loop
for i in range(1, 6):
    print(i)

# Using a while loop
i = 1
while i <= 5:
    print(i)
    i += 1
