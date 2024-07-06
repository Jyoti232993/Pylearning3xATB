class Person:
    # Attributes
    name = None
    id = None
    age = None
    phone_number = None

    # Behaviour
    def talk(self):  # No Arg -> No Return
         print("I can talk.")


    def sleep(self, name):  # Arg with No Return
        print("I am a Method!!")
        return ("Sleep", name)


    def sleep2(self, name):  # Arg with Return
        print("I am a Method!!")
        return None


    def walk(self):
        print("I am walking")


    def walk_return(self):  # No Arg with Return
        return "I am walking"


# Create object of a "Person" class
# objectRef = Object ->  ClassName()

surya = Person()
surya.name = "Surya Prakash"
surya.talk()


ritika = Person()
ritika.name = "Ritika Gupta"
ritika.walk()
