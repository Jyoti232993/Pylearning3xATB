# Program to print the Right Triangle Star Pattern

rows = int(input("Enter the number of rows: "))

for row_numbers in range(1, rows + 1):
    for columns in range(1, row_numbers + 1):
        print("*", end= " ")
    print()


