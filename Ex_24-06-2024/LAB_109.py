# LeetCode - Sum of Digits

# number = 12345
# r1 = number % 10  # Gives reminder
# q1 = number //10   # Gives quotient
# print(r1, q1)
#
# r2 = q1 % 10
# q2 = q1 // 10
# print(r2, q2)
#
# r3 = q2 % 10
# q3 = q2 //10
# print(r3, q3)
#
# r4 = q3 % 10
# q4 = q3 // 10
# print(r4, q4)
#
# r5 = q4 % 10
# q5 = q4 // 10
# print(r5, q5)
#
# print(r1 + r2 + r3 + r4 + r5)

def sum_of_digits(n):
    # Base Case
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(12345))
