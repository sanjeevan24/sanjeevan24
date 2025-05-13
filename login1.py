import os
import random

customer_file = "customers.txt"
account_file = "accounts.txt"
transaction_file = "transactions.txt"
account_number_file = "account_numbers.txt"

# Load customer credentials
def bank_customers():
    customers = {}
    if os.path.exists(customer_file):
        with open(customer_file, "r") as file:
            for files in file:
                files = files.strip()
                if files:
                    try:
                        username, password = files.split(",")
                        customers[username] = password
                    except ValueError:
                        print(f"Skipping malformed files in {customer_file}: {files}")
    return customers

# Load account balances
def bank_accounts():
    accounts = {}
    if os.path.exists(account_file):
        with open(account_file, "r") as file:
            for files in file:
                files = files.strip()
                if files:
                    try:
                        username, balance = files.split(",")
                        accounts[username] = float(balance)
                    except ValueError:
                        print(f"Skipping malformed files in {account_file}: {files}")
    return accounts

# Load transactions
def bank_transactions():
    transactions = {}
    if os.path.exists(transaction_file):
        with open(transaction_file, "r") as file:
            for files in file:
                files = files.strip()
                if files:
                    try:
                        username, detail = files.split(",")
                        transactions.setdefault(username, []).append(detail)
                    except ValueError:
                        print(f"Skipping malformed files in {transaction_file}: {files}")
    return transactions

# Load account numbers
def load_account_numbers():
    account_numbers = {}
    if os.path.exists(account_number_file):
        with open(account_number_file, "r") as file:
            for files in file:
                files = files.strip()
                if files:
                    try:
                        username, acc_num = files.split(",")
                        account_numbers[username] = acc_num
                    except ValueError:
                        print(f"Skipping malformed files in {account_number_file}: {files}")
    return account_numbers

# Save functions
def save_account_numbers(account_numbers):
    with open(account_number_file, "w") as file:
        for username, acc_num in account_numbers.items():
            file.write(f"{username},{acc_num}\n")

def save_customers(customers):
    with open(customer_file, "w") as file:
        for username, password in customers.items():
            file.write(f"{username},{password}\n")

def save_accounts(accounts):
    with open(account_file, "w") as file:
        for username, balance in accounts.items():
            file.write(f"{username},{balance}\n")

def append_transaction(username, detail):
    with open(transaction_file, "a") as file:
        file.write(f"{username},{detail}\n")

#  account number
def generate_account_number(existing_numbers):
    while True:
        acc_num = str(random.randint(0000,9999))
        if acc_num not in existing_numbers.values():
            return acc_num

# Admin creates a customer account
def admin_create_account(customers, accounts):
    account_numbers = load_account_numbers()
    print("\nCreate Customer Account")
    username = input("Enter customer username: ")
    if username in customers:
        print("Account already exists.")
        return
    password = input("Enter customer password: ")
    acc_num = generate_account_number(account_numbers)

    customers[username] = password
    accounts[username] = 100.0
    account_numbers[username] = acc_num

    save_customers(customers)
    save_accounts(accounts)
    save_account_numbers(account_numbers)

    print(f"Customer account for '{username}' created successfully.")
    print(f"Assigned Account Number: {acc_num}")

# Customer login
def login(customers):
    account_numbers = load_account_numbers()
    print("\n == Customer Login ==")
    username = input("Enter your username: ")
    if username not in customers:
        print("Account not found!")
        return None
    password = input("Enter your password: ")
    if customers[username] != password:
        print("Incorrect password.")
        return None
    print(f"Welcome, {username}!")
    if username in account_numbers:
        print(f"Your Account Number: {account_numbers[username]}")
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
        append_transaction(username, f"Deposited: {amount}")
        print(f"Deposited {amount}. New balance: {accounts[username]}")
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
        append_transaction(username, f"Withdrew: {amount}")
        print(f"Withdrew {amount}. New balance: {accounts[username]}")
    except ValueError:
        print("Invalid amount entered.")

# View balance
def view_balance(username, accounts):
    print(f"Current balance: {accounts[username]}")

# View transaction history
def view_transactions(username, transactions):
    print("\nTransaction History")
    if username in transactions and transactions[username]:
        for t in transactions[username]:
            print(t)
    else:
        print("No transactions found.")


# Customer banking menu
def account_operations(username, accounts, transactions):
    while True:
        print("\n----- Banking Menu -----")
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
            transactions = bank_transactions()
            view_transactions(username, transactions)
        elif choice == "5":
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice.")

# Main program
def main():
    adminpassword = "admin123"

    print("\n===== Admin Login =====")
    for _ in range(3):
        pwd = input("Enter admin password: ")
        if pwd == adminpassword:
            print("Admin access granted.")
            while True:
                customers = bank_customers()
                accounts = bank_accounts()
                account_numbers = load_account_numbers()
                print("\n===== Admin Menu =====")
                print("1. Create Customer Account")
                
                print("2. Continue to Customer Login")
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

    while True:
        customers = bank_customers()
        accounts = bank_accounts()
        transactions = bank_transactions()
        print("\n----- Customer Menu -----")
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
