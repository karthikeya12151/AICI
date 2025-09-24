def read_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        return "Error: File not found."
    except PermissionError:
        return "Error: Permission denied."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


if __name__ == "__main__":
    filename = input("Enter filename to read: ")
    content = read_file(filename)
    print("\n--- File Content ---")
    print(content)
