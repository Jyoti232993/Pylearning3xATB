# *args - any number of arguments
# print("Pramod", "Amit", "SB")

def sum_three(a=1, b=1, c=1):
    return a + b +c

# result = sum_three()
result_1 = sum_three()
result_2 = sum_three(1,2)
result_3 = sum_three(1,2,3)
result_4 = sum_three(10, 67, 45)
result_5 = sum_three(67,10,45)
print(result_1, result_2, result_3, result_4, result_5)