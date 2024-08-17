numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def doubler(number):
    return number * 2

def even_giver(number):
    return number % 2 == 0

doubled_number = map(doubler, numbers)
print(list(doubled_number))

even_numbers = filter(even_giver, numbers)
print(list(even_numbers))

