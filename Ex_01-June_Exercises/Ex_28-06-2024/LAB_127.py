class car:
    name = None

    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected123"
        self.__private_var = "pass@123"

    def __private_method(self):    # private function
        print("Protected!")

    def printname(self):    # Public function which can access private function within the class.
        self.__private_method()
        if self.__private_var == "123":
            print("Hi, 123")
        print("I am allowed public")

alto = car()
alto.printname()
