def check_number(num):
    if num > 0:
        print("The number is positive")
    elif num < 0:
        print("The number is negative")
    else:
        print("The number is zero")

# Test the function with different numbers
check_number(-5)  # Output: The number is negative
check_number(0)   # Output: The number is zero
check_number(7)   # Output: The number is positive
