class Person:
    # Class Variables / instance variables / Attributes
    name = "John"
    age = None

    def walk(self):
        a = 10 # local variable
        print("I am am Method")
        print("Hi", self.age)

amit = Person()
amit.walk()