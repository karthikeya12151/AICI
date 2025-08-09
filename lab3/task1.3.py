import math

try:
    num = int(input("Enter a non-negative integer: "))
    if num < 0:
        print("Please enter a non-negative integer.")
    else:
        print(f"Factorial of {num} is {math.factorial(num)}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
