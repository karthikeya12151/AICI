def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example test cases
if __name__ == "__main__":
    print("Factorial =", factorial(5))  # Output: Factorial = 120
    print("Factorial =", factorial(0))  # Output: Factorial = 1
