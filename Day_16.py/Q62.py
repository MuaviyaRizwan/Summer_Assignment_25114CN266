# Find element with maximum frequency
def max_frequency(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return max(freq, key=freq.get)

# Example
arr = [2, 3, 2, 4, 3, 2]
print("Max frequency element:", max_frequency(arr))
