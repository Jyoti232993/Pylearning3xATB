# Inheritance
# Acquire the Attributes and Behaviour
# Data members and Methods

# 3BHK House -F -> Inheritance - Son -
# concept in object-oriented programming (OOP)
# that allows a class (child class) to inherit attributes and methods
# from another class (parent class)

# Types of Inheritance

# Single - 80%  - # API, Web Automation - 80% -> Single
# Multiple
# Multi level
# Hybrid
# Hierarchical

# Single
class Grandparent: # Parent Class, Base Class
    key = "abc@123"
    def grandparent_method(self):
        return  "Grandparent's method"


class Father(Grandparent): # Child Class, Sub Class
    def parent_method(self):
        return "Parent's method"

grandfather = Grandparent()
grandfather.grandparent_method()


parent = Father()
print(parent.parent_method())
print(parent.grandparent_method())
print(parent.key)
