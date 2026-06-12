# Find missing number in array
def find_missing(arr, n):
    total = n * (n + 1) // 2   # sum of 1..n
    return total - sum(arr)

# Example
arr = [1, 2, 4, 5, 6]
n = 6
print("Missing number:", find_missing(arr, n))
