# Find pair with given sum
def find_pair(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return (num, target - num)
        seen.add(num)
    return None

# Example
arr = [1, 4, 7, 2, 5]
target = 9
print("Pair with sum:", find_pair(arr, target))
