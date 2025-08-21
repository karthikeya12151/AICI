class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid or insufficient funds.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

def main():
    name = input("Enter account holder name: ")
    account = BankAccount(name)
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == '2':
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()