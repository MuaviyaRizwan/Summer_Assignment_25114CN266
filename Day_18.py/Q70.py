# Selection Sort Program
A = []
n = int(input("Enter number of elements: "))
for i in range(n):
    A.append(int(input()))

print("Original array:", A)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if A[j] < A[min_index]:
            min_index = j
    A[i], A[min_index] = A[min_index], A[i]

print("Sorted array (Ascending):", A)
