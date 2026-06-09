#Write a program to Find largest and smallest  element in an array
A = []
n = int(input("Enter the number of elments to be entered in the array:"))
for i in range(n):
    A.append(int(input()))
print("Array:",A)
#for largest element: 
largest=A[0]
for j in range(1,n):
    if (A[j]>largest):
        largest=A[j]
print("The largest element in array is:",largest)
# for smallest
smallest=A[0]
for k in range(1,n):
    if(A[k]<smallest):
        smallest=A[k]
print("The smallest element in array is:",smallest)        
            
           

 
