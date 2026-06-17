# Program to find string length without using len()

string = input("Enter a string: ")
count = 0

for ch in string:
    count += 1

print("Length of string =", count)
