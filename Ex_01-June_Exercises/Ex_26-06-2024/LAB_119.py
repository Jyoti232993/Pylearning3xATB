class calc:

    # Define the constructor
    def __init__(self, a, b):
        self. a = a
        self. b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

object_ref = calc(5,4)
output = object_ref.sum()
print(output)