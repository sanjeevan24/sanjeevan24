# mini Banking Application

print("/n welcome to uor bank.\n")
admin_name=input("enter the name :")
admin_id=input("enter admin id :")
admin_password=input("enter the admin password :")


with open("admin.txt",'w') as file:
 file.write(f"{admin_name}\t{admin_id}\t{admin_password}")

print("admin account created succesfully...\n ")





#create==============================
accounts = {}

def create_account():
    name = input("Enter account holder's name: ")
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        print("Account already exists!")
    else:
        accounts[acc_num] = {"name": name, "balance": 0}
        print(f"Account created for {name} with account number {acc_num}.")
#balance==================
def view_balance():
    acc_num = input("Enter your account number: ")
    if acc_num in accounts:
        print(f"Account holder: {accounts[acc_num]['name']}")
        print(f"Current balance: ${accounts[acc_num]['balance']}")
    else:
        print("Account not found!")
#deposit==============================
def deposit():
    acc_num = input("Enter your account number: ")
    if acc_num in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[acc_num]["balance"] += amount
        print(f"${amount} deposited successfully.")
    else:
        print("Account not found!")
# withdraw=============================
def withdraw():
    acc_num = input("Enter your account number: ")
    if acc_num in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= accounts[acc_num]["balance"]:
            accounts[acc_num]["balance"] -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Inbalance.")
    else:
        print("Account not found!")

def main():
    while True:
        print("\n--- Mini Banking System ---")
        print("1. Create Account")
        print("2. View Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            view_balance()
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()





















import os
import json

# Define the file path for storing account data
account_file = "accounts.json"

def load_accounts():
    
    if os.path.exists(account_file):
        with open(account_file, 'r') as file:
            return json.load(file)
    return {}

def save_accounts():
    
    with open(account_file, 'w') as file:
        json.dump(accounts, file)

# Load accounts from the file when the application starts
accounts = load_accounts()
#menu---------------------------------------------------------------
def display_menu():
    print("\n--- Mini Bank Application ---")
    print("1. Create a new account")
    print("2. Login to existing account")
    print("3.exit")


 #create-------------------------------------------------------------

def create_account():
    print("\n--- Create account ---")
    username = input("enter your username: ")

    if username in accounts:
        print("account already exists! Please login or choose a different username.")
        return

    password = input(" enteryour password: ")
    accounts[username] = {'password': password,'balance': 100,'transactions': []}

    save_accounts()  # Save updated accounts to the file
    print(f"account created successfully for {username}.")
#login------------------------------------
def login():
    print("\n--- Login ---")
    username = input("enter your username: ")

    if username not in accounts:
        print("account not found!")
        return None

    password = input("enter your password: ")

    if accounts[username]['password'] != password:
        print("Incorrect password!")
        return None
    print(f"Welcome back, {username}!")
    return username


#deposit amount------------------------------------------

def deposit(username):
    amount = float(input("enter deposit amount: "))
    accounts[username]['balance'] += amount
    accounts[username]['transactions'].append(f"Deposited: ${amount}")
    save_accounts()  # Save updated accounts to the file
    print(f"Successfully deposited ${amount}. Current balance: ${accounts[username]['balance']}.")

#withdraw amount----------------------------------

def withdraw(username):
    amount = float(input("enter withdrawal amount: "))
    if amount > accounts[username]['balance']:
        print("Insufficient balance!")
        return
    accounts[username]['balance'] -= amount
    accounts[username]['transactions'].append(f"Withdrew: ${amount}")
    save_accounts()  # Save updated accounts to the file
    print(f"Successfully withdrew ${amount}. Current balance: ${accounts[username]['balance']}.")



#balance-------------------------------------------------

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
        print("\n--- account Operations ---")
        print("1. View balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View transaction history")
        print("5. backt")
        
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
            print("back")
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

















def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            username = input("Enter admin username to create a new account: ")
            password = input("Enter admin password: ")
            if username == 'admin' and username in accounts and accounts[username]['password'] == password:
                create_account()
            else:
                print("Only admin can create new accounts. Invalid credentials.")
        elif choice == '2':
            username = login()
            if username:
                account_operations(username)
        elif choice == '3':
            print("Thank you for using Mini Bank. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
