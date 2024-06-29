# Decorators
# What is a Decorator?
# A decorator is essentially a function that takes another function as an argument
# returns a new function that usually extends the behavior


def my_decorator(say_hello): #Decorator function that takes say_hello function as an argument and returns the wrapper function.
        def wrapper(): # Wrapper function is used to give a proper appearnce.
            print("Starting.....")
            print("****************")
            say_hello() #Function is called here.
            print("****************")
            print("Ending")
        return wrapper()



@my_decorator
def say_hello(): #actual function block is written here.
    print("Hello, Hi Hope you are doing well?")

