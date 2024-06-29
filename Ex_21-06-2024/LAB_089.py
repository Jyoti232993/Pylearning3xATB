# Unpacking of tuple
a, b, c = (12, 34, 56)

t = (12, 34, 56)
# t.append()  tuple are immutable in nature

new_t = t + (4,) # Modified the tuple by not operating on it , but creating a new tuple from the exisitng one

print(new_t)

my_list = list(t) # Created list from tupple
print(my_list)
my_list.append(5) # Appneded the list
new_t2 = tuple(my_list) # Create tuple back from the list
print(new_t2)