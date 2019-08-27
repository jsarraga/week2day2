import view
import model
import random

def run():
    welcomemenu()
    model.load() 
    # account = view.get_acct()
    # pin = view.get_pin()
    # if pin == model.pin_check(account, pin):
    #     mainmenu(account)
    # else:
    #     view.bad_input()    

def welcomemenu():
    while True:
        view.welcome_menu()
        selection = view.get_input()
        if selection == '1':
            create_account()
        if selection == '2':
            login()
        if selection == '3':
            model.save()
            return

def login():
    model.load() 
    account = view.get_acct()
    pin = view.get_pin()
    if pin == model.pin_check(account, pin):
        mainmenu(account)
    else:
        view.bad_input()


def mainmenu(account):
    while True:
        view.show_menu(account)
        selection = view.get_input()
        if selection == '4':
            answer = view.quit_input()
            if answer =="y":
                model.save() 
                break
            if answer == "n":
                view.show_menu(account)
        elif selection == '1':
            balance = model.check_balance(account) 
            view.show_balance(balance)
        elif selection == '2':
            depbalance = float(view.get_amount_input())
            model.deposit(account, depbalance) 
            balance = model.check_balance(account)
            view.show_balance(balance)
        elif selection =='3':
            wdbalance = float(view.get_amount_input())
            model.withdraw(account, wdbalance) 
            balance = model.check_balance(account)
            view.show_balance(balance)
        else:
            view.bad_input()

def create_account():
    while True:
        model.load()
        view.create_account()
        account = random.randint(1,10000)
        first_name = view.first_name()
        last_name = view.last_name()
        create_pin = view.create_pin()
        model.create_acct(account, first_name, last_name, create_pin)
        view.new_account(account)
        model.save()
        return 

if __name__ == "__main__":
    run()
    # print("Current __name__: ", __name__)