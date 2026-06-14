# Sort Array in Descending Order
A = []
n = int(input("Enter number of elements: "))
for i in range(n):
    A.append(int(input()))

print("Original array:", A)

A.sort(reverse=True)

print("Sorted array (Descending):", A)
