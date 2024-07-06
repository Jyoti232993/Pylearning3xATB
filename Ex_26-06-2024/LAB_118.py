class calc:

    # Define constructor
    def __init__(self):
        print("Hello DC")

    def sum(self, a,b):
        return a + b

    def sub(self,a,b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        return a/b

# Create object of a "Calc" class
# objectRef = Object ->  ClassName()

object_ref = calc()
output = object_ref.sum(3,4)
print(output)




