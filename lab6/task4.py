def sum_to_n(n):
    return sum(range(1, n + 1))

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    total = sum_to_n(n)
    print(f"Sum of first {n} numbers is {total}")