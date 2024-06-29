t = ("TheTestingAcademy", "for", "TheTestingAcademy")
print(set(t))

set_1 = {1, 2, 3}
set_2 = {4, 5, 6}
my_set = set_1.union(set_2)
print(my_set)

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}
my_set = set_1.intersection(set_2)
print(my_set)

my_set = set_1.difference(set_2)
print(my_set)

my_set = set_2.difference(set_1)
print(my_set)
