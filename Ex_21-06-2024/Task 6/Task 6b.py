# Program to check whether the string is palindrome or not
# A string is said to be a palindrome if the reverse of the string is the same as the string.
# For example, “radar” is a palindrome, but “radix” is not a palindrome.

string_input = input ("Enter a string: ")

reverse_string = string_input[::-1]

if string_input == reverse_string:
   print("The string is a palindrome.")

else:
   print("The string is not a palindrome.")
