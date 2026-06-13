# Common elements in three arrays
arr1 = [1, 2, 3, 4]
arr2 = [2, 3, 5, 6]
arr3 = [3, 7, 2, 8]

common = list(set(arr1) & set(arr2) & set(arr3))
print("Common Elements:", common)
