# Bubble Sort Program
A = []
n = int(input("Enter number of elements: "))
for i in range(n):
    A.append(int(input()))

print("Original array:", A)

for i in range(n-1):
    for j in range(n-1-i):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

print("Sorted array (Ascending):", A)
