# Write a program to Second largest element.
A=[]
n = int(input("Enter the number of elements to be entered in the array:"))
for i in range(n):
    A.append(int(input()))
    
print("Array:",A)
largest=A[0]
for j in range(1,n):
    if(A[i]>largest):
        largest=A[i]
print("Largest:",largest)
sec_large=A[0]                      #A=[1,2,3,4,5]              
for k in range(0,n-1):
    if(A[k]<A[k+1] and A[k+1]<largest ):
        sec_large=A[k+1]        
print("Second largest number is:",sec_large)    