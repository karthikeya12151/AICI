# The following code defines two linked functions for a simple user authentication system:
# 1. register_user(): Prompts the user to register by entering a username and password, and stores them in a dictionary.
# 2. login_user(): Prompts the user to log in by entering their username and password, and checks them against the registered users.
# The functions take input from the user and demonstrate basic registration and login logic.

def register_user(users):
    """
    Registers a new user by asking for a username and password.
    Stores the credentials in the provided users dictionary.
    """
    username = input("Enter a username to register: ")
    if username in users:
        print("Username already exists. Please choose a different username.")
        return
    password = input("Enter a password: ")
    users[username] = password
    print("Registration successful!")

def login_user(users):
    """
    Logs in a user by asking for a username and password.
    Checks the credentials against the users dictionary.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful! Welcome,", username)
    else:
        print("Invalid username or password.")

# Example usage:
users = {}
while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        register_user(users)
    elif choice == '2':
        login_user(users)
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
