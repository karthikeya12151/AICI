def sum_of_squares():
    n = int(input("Enter a number: "))
    total = 0
    for i in range(1, n+1):
        total += i*i
    print("Sum of squares from 1 to", n, "is", total)

sum_of_squares()
