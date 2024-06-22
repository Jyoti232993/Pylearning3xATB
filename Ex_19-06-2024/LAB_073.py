def outer_function():
    var1 = 30
    def inner_function(): # Call the function first time.
        print(var1)
    inner_function()

    def inner_function_2():
        print(var1)
    inner_function_2()


outer_function()