A simple implementation of a bank account

1. BankAccount Class:
    - This class represents a bank account. It has the following attributes:
        - `account_number`: Account number of the bank account.
        - `owner`: Owner's name of the bank account.
        - `balance`: Current balance of the bank account.
    - It provides the following methods:
        - `deposit(amount)`: Deposits the specified amount into the bank account.
        - `withdraw(amount)`: Withdraws the specified amount from the bank account.
        - `check_balance()`: Displays the current balance of the bank account.

2. Main Block (`if __name__ == "__main__":`):
    - It sets up the main functionality of the bank app.
    - It initializes an empty dictionary named `accounts` to store bank accounts and a variable `current_account` to keep track of the currently signed-in account.
    - It enters a loop that displays the available bank app options and prompts the user for input.
    - The available options are:
        - **Sign in to existing account** (`1`): Allows the user to sign in to an existing account by providing the account number.
        - **Create a new account** (`2`): Prompts the user to create a new bank account by providing details such as account number, owner's name, and initial balance.
        - **Deposit** (`3`): If a user is signed in, allows the user to deposit money into their account.
        - **Withdraw** (`4`): If a user is signed in, allows the user to withdraw money from their account.
        - **Check Balance** (`5`): If a user is signed in, displays the current balance of their account.
        - **Exit** (`6`): Exits the bank app and ends the loop.
    - Depending on the user's choice, the corresponding actions are performed. If the choice is invalid, an appropriate message is displayed.
    
3. Account Management:
    - The code maintains a dictionary `accounts` to store instances of `BankAccount` class, where account numbers serve as keys.
    - It keeps track of the currently signed-in account using the `current_account` variable.

Overall, this code provides a simple command-line interface for managing bank accounts, allowing users to sign in, create accounts, deposit/withdraw money, check balances, and exit the application.

