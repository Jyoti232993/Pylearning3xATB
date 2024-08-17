# Program to count vowels and consonants in a given string

string_input = input("Enter a string: ")
count_vowels = 0
count_consonants = 0

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for i in string_input:
    if i in vowels:
        count_vowels = count_vowels + 1
    else:
        count_consonants = count_consonants + 1
print("The total number of vowels count: ", count_vowels)
print("The total number of consonants count: ", count_consonants)