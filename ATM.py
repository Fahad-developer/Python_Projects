# ATM machine program

# Initialize user account information in a dictionary
accounts = {
    'user1': {'password': '1234', 'balance': 1000},
    'user2': {'password': '4321', 'balance': 500},
    'user3': {'password': '1111', 'balance': 2000},
    'user4': {'password': '0000', 'balance': 5000}
}

# Function to check if user is valid
def check_user(username):
    if username in accounts:
        return True
    else:
        return False

# Function to check if password is correct
def check_password(username, password):
    if accounts[username]['password'] == password:
        return True
    else:
        return False

# Function to check if amount entered is valid
def check_amount(username, amount):
    if amount > 0 and amount <= accounts[username]['balance']:
        return True
    else:
        return False

# Function to withdraw money
def withdraw_money(username, amount):
    accounts[username]['balance'] -= amount
    return amount

# Function to deposit money
def deposit_money(username, amount):
    accounts[username]['balance'] += amount

# Main program
while True:
    # Get user input for username
    username = input("Enter your username: ")
    if check_user(username):
        # Get user input for password
        password = input("Enter your password: ")
        if check_password(username, password):
            while True:
                # Print options for user
                print("1. Check Balance")
                print("2. Withdraw Money")
                print("3. Deposit Money")
                print("4. Exit")
                # Taking input from the user
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    # Print current balance
                    print("Your current balance is:", accounts[username]['balance'])
                elif choice == 2:
                    # Get user input for amount to withdraw
                    amount = int(input("Enter the amount to withdraw: "))
                    if check_amount(username, amount):
                        # Withdraw money
                        print("Please take your cash: ", withdraw_money(username, amount))
                    else:
                        print("Invalid amount. Please enter a valid amount.")
                elif choice == 3:
                    # Get user input for amount to deposit
                    amount = int(input("Enter the amount to deposit: "))
                    if check_amount(username, amount):
                        # Deposit money
                        deposit_money(username, amount)
                        print("Your account has been credited with: ", amount)
                    else:
                        print("Invalid amount. Please enter a valid amount.")
                elif choice == 4:
                    # Exit program
                    print("Thank you for using our ATM. Have a nice day!")
                    break
                else:
                    print("Invalid choice. Please enter a valid choice.")
        else:
            print("Invalid password. Please enter a valid password.")
    else:
        print("Invalid username. Please enter a valid username.")

