for i in range(1, 10):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#fizzBuzz using funtions
result=[]
def fizzBuzz(n):
    for i in range(1, n + 1):
        # Check if i is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        # Check if i is divisible by 3
        elif i % 3 == 0:
            result.append("Fizz")
        # Check if i is divisible by 5
        elif i % 5 == 0:
            result.append("Buzz")
        # Otherwise, add the current number as a string
        else:
            result.append(str(i))

    return result
result=fizzBuzz(15)
#print(result)