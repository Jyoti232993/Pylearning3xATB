# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides.
# determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

#Enter the length of three sides
side_1 = float(input("Enter the length of the first side of triangle:"))
side_2 = float(input("Enter the length of the second side of triangle:"))
side_3 = float(input("Enter the length of the third side of triangle:"))

# If all sides are equal, display that it's an equilateral triangle
if side_1 == side_2 == side_3:
    print("The triangle is equilateral.")

# If at least two sides are equal, display that it's an isosceles triangle
elif side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
    print("The triangle is isosceles.")

# If all sides have different lengths, display that it's a scalene triangle
else:
    print("The triangle is scalene.")





