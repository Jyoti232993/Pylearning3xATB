class Dog:
    # Attributes
    name = None
    id = None

    # Constuctor ?
    # Use to initialize the values
    # of the instance variables (Attributes)

    #Behaviours
    def sleep(self):
        print("Sleeping")


# Create object of a "Dog" class
# objectRef = Object ->  ClassName()

dog1 = Dog()
print(dog1.name) #Using of attributes on the object reference.
dog1.name = "Chow"
print(dog1.name)
dog1.sleep() #Using Behaviours on the object reference.

print(" ---- -----------------")

dog2 = Dog()
print(dog2.name)
dog2.name = "Mow"
print(dog2.name)



