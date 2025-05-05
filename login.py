ACCOUNT_FILE = "accounts.txt"

def load_accounts():
    accounts = {}
    try:
        with open(ACCOUNT_FILE, 'r') as file:
            for line in file:
                x = line.split('')
                if len(x) >= 3:
                    username = x[0]
                    password = x[1]
                    balance = float(x[2])
                    transactions = x[3:] if len(x) > 3 else []
                    accounts[username] = {
                        'password': password,
                        'balance': balance,
                        'transactions': transactions
                    }
    except FileNotFoundError:
        pass
    return accounts

def save_accounts():
    with open(ACCOUNT_FILE, 'w') as file:
        for username, data in accounts.items():
            line = '  '.join([username, data['password'], str(data['balance'])] + data['transactions'])
            file.write(line + '\n')

# Load accounts from file
accounts = load_accounts()

def display_menu():
    print("\n--- Mini Bank Application ---")
    print("1. Create a new account")
    print("2. Login to existing account")
    print("3. Exit")

def create_account():
    print("\n--- Create account ---")
    username = input("Enter your username: ")
    if username in accounts:
        print("Account already exists! Please login or choose a different username.")
        return
    password = input("Enter your password: ")
    accounts[username] = {'password': password, 'balance': 100, 'transactions': []}
    save_accounts()
    print(f"Account created successfully for {username}.")

def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    if username not in accounts:
        print("Account not found!")
        return None
    password = input("Enter your password: ")
    if accounts[username]['password'] != password:
        print("Incorrect password!")
        return None
    print(f"Welcome back, {username}!")
    return username

def deposit(username):
    try:
        amount = float(input("Enter deposit amount: "))
        accounts[username]['balance'] += amount
        accounts[username]['transactions'].append(f"Deposited: ${amount}")
        save_accounts()
        print(f"Successfully deposited ${amount}. Current balance: ${accounts[username]['balance']}.")
    except ValueError:
        print("Invalid amount!")

def withdraw(username):
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount > accounts[username]['balance']:
            print("Insufficient balance!")
            return
        accounts[username]['balance'] -= amount
        accounts[username]['transactions'].append(f"Withdrew: ${amount}")
        save_accounts()
        print(f"Successfully withdrew ${amount}. Current balance: ${accounts[username]['balance']}.")
    except ValueError:
        print("Invalid amount!")

def view_balance(username):
    print(f"Your current balance is: ${accounts[username]['balance']}.")

def view_transactions(username):
    print("\nTransaction History:")
    if not accounts[username]['transactions']:
        print("No transactions yet.")
    else:
        for transaction in accounts[username]['transactions']:
            print(transaction)

def account_operations(username):
    while True:
        print("\n--- Account Operations ---")
        print("1. View balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View transaction history")
        print("5. Back")
        choice = input("Choose an operation: ")
        if choice == '1':
            view_balance(username)
        elif choice == '2':
            deposit(username)
        elif choice == '3':
            withdraw(username)
        elif choice == '4':
            view_transactions(username)
        elif choice == '5':
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice! Please try again.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            username = login()
            if username:
                account_operations(username)
        elif choice == '3':
            print("Thank you for using Mini Bank. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
