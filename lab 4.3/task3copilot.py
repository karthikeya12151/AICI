def format_full_name():
    full_name = input("Enter full name (First Last): ").strip()
    parts = full_name.split()
    if len(parts) >= 2:
        first = parts[0]
        last = " ".join(parts[1:])
        formatted = f"{last}, {first}"
        print(formatted)
    else:
        print("Invalid input. Please enter both first and last name.")

# Example usage
format_full_name()