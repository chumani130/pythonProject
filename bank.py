import os

bank_data_file = "Bank Data.txt"
transaction_log_file = "Transaction Log.txt"

def display_balance():
    with open(bank_data_file, "r") as file:
        balance = float(file.read())
        print("Current balance: $", balance)

def make_transaction():
    transaction_type = input("Would you like to make a deposit or withdrawal? (Yes or No): ").lower()
    if transaction_type == "yes":
        deposit_or_withdrawal = input("Would you like to make a deposit or withdrawal? (Deposit or Withdrawal): ").lower()
        if deposit_or_withdrawal == "deposit":
            amount = float(input("How much would you like to deposit? "))
            if amount > 0:
                with open(bank_data_file, "r") as file:
                    balance = float(file.read())
                balance += amount
                with open(bank_data_file, "w") as file:
                    file.write(str(balance))
                with open(transaction_log_file, "a") as file:
                    file.write(f"Deposit: +{amount}\n")
                display_balance()
            else:
                print("Invalid amount. Please enter a positive value.")
        elif deposit_or_withdrawal == "withdrawal":
            amount = float(input("How much would you like to withdraw? "))
            with open(bank_data_file, "r") as file:
                balance = float(file.read())
            if 0 < amount <= balance:
                balance -= amount
                with open(bank_data_file, "w") as file:
                    file.write(str(balance))
                with open(transaction_log_file, "a") as file:
                    file.write(f"Withdrawal: -{amount}\n")
                display_balance()
            else:
                print("Invalid amount. Please enter a valid value.")
        else:
            print("Invalid input. Please enter 'Deposit' or 'Withdrawal'.")
    elif transaction_type == "no":
        print("No transaction made.")
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

def initialize_files():
    if not os.path.isfile(bank_data_file):
        with open(bank_data_file, "w") as file:
            file.write("0.0")
    if not os.path.isfile(transaction_log_file):
        with open(transaction_log_file, "w"):
            pass

initialize_files()

while True:
    make_transaction()
    continue_option = input("Would you like to make another transaction? (Yes or No): ").lower()
    if continue_option != "yes":
        break

print("Thank you for using the banking application.")
