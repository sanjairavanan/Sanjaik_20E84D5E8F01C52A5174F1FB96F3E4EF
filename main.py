class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__account_balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.__account_balance:.2f}")
            else:
                print("Insufficient funds. Cannot withdraw.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance:.2f}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount("1234567890", "John Doe", 1000.0)

    # Display the initial balance
    account.display_balance()

    # Deposit $500
    account.deposit(500.0)

    # Withdraw $200
    account.withdraw(200.0)

    # Try to withdraw an amount greater than the balance
    account.withdraw(2000.0)

    # Display the final balance
    account.display_balance()
