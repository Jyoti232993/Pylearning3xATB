# Avinash - Multiple Condition

# Problem  Find the Max between 3 numbers

# num1, num2 , num3

# num1 > num2 and num1 > num3 ->  num1

# num2 > num1 and num2 > num3 -> num2

# num3

num_1 = int(input("Enter the first number:"))
num_2 = int(input("Enter the second number:"))
num_3 = int(input("Enter the third number:"))

if num_1 >= num_2 and num_1 >= num_3:
    print(num_1)
elif num_2 >= num_1 and num_2 >= num_3:
    print(num_2)
else:
    print(num_3)

# max()
# outTrue if conditin else outfalse
# result = print(max(num_1, num_2, num_3))

