# Web Automation - Selenium
# Page - You are going automate

class VWOLoginpage:

    def __init__(self, email,password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.email == "pramod@gmail.com" and self.password == "Pass123":
            print("Allowed to enter")
        else:
           print("Not allowed")
# This is the end of the class

email = input("Enter the E-mail: \n")
password = input("Enter the password: \n")
amit = VWOLoginpage(email, password)
amit.login_confirm()


email = input("Enter the E-mail: \n")
password = input("Enter the password: \n")
pramod = VWOLoginpage(email, password)
pramod.login_confirm()


