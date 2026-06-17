# Program to convert lowercase to uppercase

string = input("Enter a string: ")

upper_string = ""
for ch in string:
    if 'a' <= ch <= 'z':
        upper_string += chr(ord(ch) - 32)  # ASCII difference
    else:
        upper_string += ch

print("Uppercase string =", upper_string)
