# Program to remove duplicate characters

string = input("Enter a string: ")
result = ""

for ch in string:
    if ch not in result:
        result += ch

print("String without duplicates =", result)
