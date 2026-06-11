# Write a program to Rotate array right. 
A=[]
n = int(input("Enter the number of elements to be entered in the array:"))
for i in range(n):
 A.append(int(input()))   #    0 1 2 3 4
print("Original array:",A)  # [2,4,3,7,5]
shift = int(input("Enter the number by the array should rotate:"))
shift = shift % n
for j in range(shift):   
 last = A[n-1]
 for k in range(n-1,0,-1):
     A[k]=A[k-1]
 A[0]=last
     
print("Rotated array to right by",shift,"position:",A)