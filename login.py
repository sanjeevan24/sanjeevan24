import os

CUSTOMER_FILE = "customers.txt"
ACCOUNT_FILE = "accounts.txt"
TRANSACTION_FILE = "transactions.txt"

# Load customer credentials
def load_customers():
    customers = {}
    if os.path.exists(CUSTOMER_FILE):
        with open(CUSTOMER_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        username, password = line.split(",")
                        customers[username] = password
                    except ValueError:
                        print(f"Skipping malformed line in {CUSTOMER_FILE}: {line}")
    return customers

# Load account balances
def load_accounts():
    accounts = {}
    if os.path.exists(ACCOUNT_FILE):
        with open(ACCOUNT_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        username, balance = line.split(",")
                        accounts[username] = float(balance)
                    except ValueError:
                        print(f"Skipping malformed line in {ACCOUNT_FILE}: {line}")
    return accounts

# Load transactions (no timestamp)
def load_transactions():
    transactions = {}
    if os.path.exists(TRANSACTION_FILE):
        with open(TRANSACTION_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        username, detail = line.split(",", 1)
                        transactions.setdefault(username, []).append(detail)
                    except ValueError:
                        print(f"Skipping malformed line in {TRANSACTION_FILE}: {line}")
    return transactions

# Save all data
def save_customers(customers):
    with open(CUSTOMER_FILE, "w") as file:
        for username, password in customers.items():
            file.write(f"{username},{password}\n")

def save_accounts(accounts):
    with open(ACCOUNT_FILE, "w") as file:
        for username, balance in accounts.items():
            file.write(f"{username},{balance}\n")

def append_transaction(username, detail):
    with open(TRANSACTION_FILE, "a") as file:
        file.write(f"{username},{detail}\n")

# Admin creates a customer account
def admin_create_account(customers, accounts):
    print("\n--- Create Customer Account ---")
    username = input("Enter customer username: ")
    if username in customers:
        print("Account already exists.")
        return
    password = input("Enter customer password: ")
    customers[username] = password
    accounts[username] = 100.0
    save_customers(customers)
    save_accounts(accounts)
    print(f"Customer account for '{username}' created successfully.")

# Customer login
def login(customers):
    print("\n--- Customer Login ---")
    username = input("Enter your username: ")
    if username not in customers:
        print("Account not found!")
        return None
    password = input("Enter your password: ")
    if customers[username] != password:
        print("Incorrect password.")
        return None
    print(f"Welcome, {username}!")
    return username

# Deposit
def deposit(username, accounts):
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        accounts[username] += amount
        save_accounts(accounts)
        append_transaction(username, f"Deposited: ${amount}")
        print(f"Deposited ${amount}. New balance: ${accounts[username]}")
    except ValueError:
        print("Invalid amount entered.")

# Withdraw
def withdraw(username, accounts):
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > accounts[username]:
            print("Insufficient funds.")
            return
        accounts[username] -= amount
        save_accounts(accounts)
        append_transaction(username, f"Withdrew: ${amount}")
        print(f"Withdrew ${amount}. New balance: ${accounts[username]}")
    except ValueError:
        print("Invalid amount entered.")

# View balance
def view_balance(username, accounts):
    print(f"Current balance: ${accounts[username]}")

# View transaction history
def view_transactions(username, transactions):
    print("\n--- Transaction History ---")
    if username in transactions and transactions[username]:
        for t in transactions[username]:
            print(t)
    else:
        print(f"No transactions found for {username}.")

# Banking menu
def account_operations(username, accounts, transactions):
    while True:
        print("\n--- Banking Menu ---")
        print("1. View Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transaction History")
        print("5. Back")
        choice = input("Select option: ")
        if choice == "1":
            view_balance(username, accounts)
        elif choice == "2":
            deposit(username, accounts)
        elif choice == "3":
            withdraw(username, accounts)
        elif choice == "4":
            transactions = load_transactions()  # Reload latest
            view_transactions(username, transactions)
        elif choice == "5":
            print("Back to menu.")
            break
        else:
            print("Invalid choice.")

# Main program
def main():
    adminpassword = "admin123"

    customers = load_customers()
    accounts = load_accounts()
    transactions = load_transactions()

    # Admin section
    print("--- Admin Login ---")
    for _ in range(3):
        pwd = input("Enter admin password : ")
       
        if pwd == adminpassword:
            print("Admin access granted.")
            while True:
                print("\n--- Admin Menu ---")
                print("1. Create Customer Account")
                print("2. login customer")
                admin_choice = input("Choose option: ")

                if admin_choice == "1":
                    admin_create_account(customers, accounts)
                elif admin_choice == "2":
                    break
                else:
                    print("Invalid choice.")
            break
        else:
            print("Incorrect password.")


    
       
    # Customer section
    while True:
        print("\n--- Customer Menu ---")
        print("1. Login")
        print("2. Exit")
        choice = input("Select option: ")
        if choice == "1":
            username = login(customers)
            if username:
                account_operations(username, accounts, transactions)
        elif choice == "2":
            print("Exiting system.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
