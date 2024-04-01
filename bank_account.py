class BankAccount:
    def __init__(self, account_number, owner, balance=0, password=None):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.password = password

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited £{amount} into account {self.account_number}.")
            print(f"New balance: £{self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew £{amount} from account {self.account_number}.")
            print(f"New balance: £{self.balance}")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def check_balance(self):
        print(f"Account {self.account_number} balance: £{self.balance}")


if __name__ == "__main__":
    accounts = {}  # Dictionary to store bank accounts
    current_account = None  # Variable to store the currently signed-in account

    while True:
        print("\nBank App Options:")
        if current_account:
            print("1. Sign out")
        else:
            print("1. Sign in to existing account")
        print("2. Create a new account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            if current_account:
                current_account = None
                print("Signed out successfully.")
            else:
                account_number = input("Enter account number: ")
                password = input("Enter password: ")
                if account_number in accounts:
                    if accounts[account_number].password == password:
                        current_account = accounts[account_number]
                        print("Signed in successfully.")
                    else:
                        print("Incorrect password.")
                else:
                    print("Account not found.")

        elif choice == '2':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                print("Account already exists.")
            else:
                owner = input("Enter account owner's name: ")
                password = input("Enter password: ")
                initial_balance = float(input("Enter initial balance: "))
                account = BankAccount(account_number, owner, initial_balance, password)
                accounts[account_number] = account
                print("Account created successfully.")

        elif choice == '3':
            if current_account:
                deposit_amount = float(input("Enter amount to deposit: "))
                current_account.deposit(deposit_amount)
            else:
                print("Please sign in or create a new account first.")

        elif choice == '4':
            if current_account:
                withdraw_amount = float(input("Enter amount to withdraw: "))
                current_account.withdraw(withdraw_amount)
            else:
                print("Please sign in or create a new account first.")

        elif choice == '5':
            if current_account:
                current_account.check_balance()
            else:
                print("Please sign in or create a new account first.")

        elif choice == '6':
            print("Exiting the bank app.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
