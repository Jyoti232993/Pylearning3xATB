# Create a program that takes two numbers as input and prints
# whether the first number is greater than, less than, or equal to the second number.

num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))

if num_1 > num_2:
    print("The first number is greater than second number.")

elif num_1 < num_2:
    print("The first number is less than second number.")

else:
    print("Both the numbers are equal")