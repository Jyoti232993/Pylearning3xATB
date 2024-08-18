# Multiple Inheritance

class Father():

    def father_money(self):
        return "5"

    def home(self):
        return "This is from the Father"


class Mother():

    def mother_money(self):
        return "2"

    def home(self):
        return "This is from the Mother"


class Son(Father, Mother):
    pass

# Probelm - Diamond Problem - Java
# Python - Multiple Inheritance
# F,M -> S

son = Son()
print(son.father_money())
print(son.mother_money())
print(son.home()) # Method Resolution


