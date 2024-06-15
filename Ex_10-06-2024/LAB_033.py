# Program - Calculate the area of circle.
# input -> radius
# output -> area

import math
# data types
# input -> int or float -> float
# output -> float

# Core Logic -> pi*r*r = 3.14

radius = float(input("Enter the value of the radius:"))
print(math.pi)
area = math.pi*(radius ** 2)
print(area)
area_2 = math.pi*(math.pow(radius, 2))
print(area_2)


