# Program to check whether the two strings are Anagrams
# Two strings are said to be anagram if we can form one string by arranging the characters of another string.
# For example, Race and Care. Here, we can form Race by arranging the characters of Care.

string_input_1 = input("Enter the first string:")
string_input_2 = input("Enter the second string:")


# check if length is same

if len(string_input_1) == len(string_input_2):
        # sort the strings
        sorted_str_1 = sorted(string_input_1)
        sorted_str_2 = sorted(string_input_2)

        # if sorted char arrays are same
        if sorted_str_1 == sorted_str_2:
            print(f"{string_input_1} and {string_input_2} are anagram.")
        else:
            print(f"{string_input_1} and {string_input_2} are not anagram.")

else:
    print(f"{string_input_1} and {string_input_2} are not anagram.")
