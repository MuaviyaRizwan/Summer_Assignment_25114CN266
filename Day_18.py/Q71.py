# Binary Search Program
def binary_search(arr, x):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

A = []
n = int(input("Enter number of elements: "))
for i in range(n):
    A.append(int(input()))

A.sort()  # Binary search requires sorted array
print("Sorted array:", A)

x = int(input("Enter element to search: "))
result = binary_search(A, x)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
