# Write a program to Move zeroes to end
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

print("Original array:", arr)


pos = 0   # index where next non-zero should go

for i in range(n):
    if arr[i] != 0:
        arr[pos] = arr[i]   #
        pos += 1


for i in range(pos, n):
    arr[i] = 0

print("Array after moving zeroes to end:", arr)      
        
        
        
    
            
            