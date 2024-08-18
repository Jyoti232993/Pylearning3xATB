# Ecap
# Inheritance
# Poly ( method overiding)
# Class
# Object
# Constructor
# Self, super, __init__
# public, _ , __ private

# Abstraction
# Abstraction - OOPs
# Hiding the details and showing the what is required

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


dog = Dog("Rancho")
print(dog.sound())

cat = Cat("Ed")
print(cat.sound())
