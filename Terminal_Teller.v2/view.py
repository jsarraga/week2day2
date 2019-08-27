
def welcome_menu():
    print()
    print("Welcome to Terminal Teller!: ")
    print()
    print("1 - Create Account")
    print("2 - Log In")
    print("3 - Quit")


def get_acct():
    return input("Account Number: ")

def get_pin():
    return input("Enter PIN: ")

def show_menu(account):
    print()
    print("Woring on account {}".format(account))
    print()
    print("Options:")
    print("1 - Check Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Quit")

def get_input():
    print()
    print("Your Choice: ", end="")
    return input()

def get_amount_input():
    print()
    print("Amount: ", end="")
    return input()

def show_balance(balance):
    print("Your Account Balance is: {}".format(balance))

def bad_input():
    print()
    print("Bad Input")
    print()

def quit_input():
    print()
    print("Are you finished? y/n ")
    return input()

def create_account():
    print("Account Creation ")
    print()

def first_name():
    print()
    return input("First Name: ")

def last_name():
    print()
    return input(("Last Name: "))

def create_pin():
    print()
    input("PIN: ")
    return input("Confirm PIN: ")

def new_account(account):
    print()
    print("account created, your account number is {}".format(account))
    