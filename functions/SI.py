# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time=1):
    """
    Calculate simple interest given principal, rate, and time.
    Default time is set to 1 year if not provided.
    """
    interest = (principal * rate * time) / 100
    return interest

# Calling the function with all three parameters
interest1 = calculate_simple_interest(1000, 5, 2)  # principal = 1000, rate = 5%, time = 2 years
print("Simple Interest (2 years):", interest1)

# Calling the function with default time parameter
interest2 = calculate_simple_interest(1000, 5)  # principal = 1000, rate = 5%, time defaults to 1 year
print("Simple Interest (1 year):", interest2)
