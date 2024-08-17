# Python program to find the factorial of a number provided by the user.
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24

num = int(input("Enter any number:"))
factorial = 1

# check if the number is negative, positive or zero

if(num <0):
    print("Sorry, factorial does not exist for negative numbers")

elif(num == 0):
    print("The factorial of 0 is 1")

else:
    for i in range(1, num+1):
        factorial = factorial * i

    print(f"The factorial of {num} is {factorial}")
