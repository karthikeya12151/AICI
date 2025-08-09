def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    num = int(input("Enter a non-negative integer: "))
    if num < 0:
        print("Please enter a non-negative integer.")
    else:
        print(f"Factorial of {num} is {factorial(num)}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
