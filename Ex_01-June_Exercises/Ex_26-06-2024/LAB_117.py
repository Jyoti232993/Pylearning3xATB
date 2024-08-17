class Dog:
    name = None
    id = None

    # Define the constructors
    def __init__(self):
        print("Default No Argument")

    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id

    # Behaviours
    def sleep(self):
        print("sleeping")


# Create object of a "Dog" class
# objectRef = Object ->  ClassName()
dog1 = Dog("Chow","1")
print(dog1.name)
print(dog1.id)

dog2 = Dog()
print(dog2.name)
print(dog2.id)




