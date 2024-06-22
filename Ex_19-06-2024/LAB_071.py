# Function Scope

def my_function():
    a =10
    local_variable = 34
    print("Hello")
    print(a)

# print(a), Outside the function it will not allow to print.
my_function()