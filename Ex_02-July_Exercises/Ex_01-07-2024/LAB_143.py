# Polymorphism
# Polymorphism allows objects of
# different classes to be treated as
# objects of a common superclass.

# Pramod -> Mentor, Husband, Brother.
# Object -Method -> Mother, Matenal She is, sister, parent -

# Method overriding

class Shape:
    def area(self):
        print("Area of the Shape")

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shape_1 = Rectangle(3,4)
print(shape_1.area())

shape_2 = Circle(10)
print(shape_2.area())

shape_3 = Shape()
shape_3.area()