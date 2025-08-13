def read_txt_file_from_console():
    filename = input("Enter the path to the .txt file: ")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    read_txt_file_from_console()