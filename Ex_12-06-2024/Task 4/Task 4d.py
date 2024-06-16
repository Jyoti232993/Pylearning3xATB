# Enter how many number of terms are required in the series?

n_terms = int(input("Enter the number of terms:"))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive integer.")

# if there is only one term, return n1
elif n_terms == 1:
    print("Fibonacci sequence upto", n_terms, ":")
    print(n1)

# generate fibonacci sequence
else:
    while(count < n_terms):
        print(n1)
        result = n1 + n2
        # update values
        n1 = n2
        n2 = result
        count += 1
