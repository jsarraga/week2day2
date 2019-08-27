import json
import os


DIR = os.path.dirname(__file__)
DATAFILENAME = "data.json"  # use your tteller filename
DATAPATH = os.path.join(DIR, DATAFILENAME)

class Account:
    data_path = DATAPATH

    def __init__(self, first_name='', last_name='', account_num="", pin="", balance=""):
        self.account_num = account_num
        self.pin = pin
        self.balance = balance
        self.first_name = first_name
        self.last_name = last_name

    def validate(self):
        with open(self.data_path, 'r') as file_object:
            data = json.load(file_object)
            if self.account_num in data:
                if data[self.account_num]["pin"] == self.pin:
                    return True
            return False

            

    def load(self):
        with open(self.data_path, 'r') as file_object:
            data = json.load(file_object)
            my_data = data[self.account_num]
            self.balance = my_data['balance']
        # load the account with this object's self.account_num
        # Sample CONTROLLER code
        # user = Account(account_num="0000000001", pin="1234")
        # if user.validate():
        #     user.load()
        # else:
        #     raise AuthenticationError

    def save(self):
        with open(self.data_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            pass

# Justin = Account(account_num= '1814', pin='1234',balance = 900)
# Justin.withdraw(50)
# print(Justin.balance)
# # print(Justin.validate('3l850', '1111'))
# Justin.load()
# print(Justin.balance)

steph = Account(account_num='4862', pin='1111',)
steph.load()
print(steph.balance)

