def sort_numbers():
    try:
        nums = input("Enter numbers separated by spaces: ")
        num_list = [int(x) for x in nums.strip().split()]
        order = input("Enter 'asc' for ascending or 'desc' for descending order: ").strip().lower()
        match order:
            case 'asc':
                sorted_list = sorted(num_list)
                print("Sorted list (ascending):", sorted_list)
            case 'desc':
                sorted_list = sorted(num_list, reverse=True)
                print("Sorted list (descending):", sorted_list)
            case _:
                print("Invalid order. Please enter 'asc' or 'desc'.")
    except ValueError:
        print("Invalid input. Please enter only integers separated by spaces.")

sort_numbers()
