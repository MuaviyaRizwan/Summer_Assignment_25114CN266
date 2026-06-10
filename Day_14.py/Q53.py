# Write a program to Linear search.
# Linear Search Program in Python

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index if found
    return -1          # return -1 if not found

# Example usage
arr = [10, 25, 30, 45, 50]
target = int(input("Enter the number to search: "))

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")