# Merge two sorted arrays
def merge_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    # Add remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
print("Merged Array:", merge_sorted_arrays(A, B))
