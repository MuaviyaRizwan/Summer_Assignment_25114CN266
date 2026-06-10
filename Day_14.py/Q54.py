# Write a program to Frequency of an element
# Program to find frequency of elements in a list

# Input list from user
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Dictionary to store frequency
freq = {}

for item in arr:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

# Display frequency
print("\nFrequency of elements:")
for key, value in freq.items():
    print(f"{key} occurs {value} times")
