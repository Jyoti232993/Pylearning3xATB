class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def __withdraw(self, amount):
        self.balance -= amount


    def __show_balance(self):
        print("Your balance is", self.balance)

    def if_you_are_auth(self, flag):    # If user is authenticated to show the balance
        if flag:
            self.__show_balance()
        else:
            print("Not Allowed")

    def if_you_are_auth_user(self, auth, balance):
        if auth:
            self.__withdraw(balance=balance)
        else:
            print("Not Allowed")

jp_chase = BankAccount()
jp_chase.deposit(100)


# When user wants to see the balance
secret_pass = input("Enter your PIN to see the balance:")
if secret_pass == "1234":
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth(False)



# When user wants to withdraw the money

secret_pass = input("Enter your PIN to withdraw the money:")
your_amount = int(input("Enter your amount to Withdraw"))

if secret_pass == "1234":
    jp_chase.if_you_are_auth_user(True, balance=your_amount)
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth_user(False)









