# Program to check if two strings are anagrams

str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
