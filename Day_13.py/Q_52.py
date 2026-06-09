#Write a program to Count even and odd elements.
A=[]
n = int(input("Enter the number of elements in the array:"))
countE = 0
countO = 0
for i in range(n):
    A.append(int(input()))
print("Array:",A)
for i in range(n):
    if(A[i]%2==0):
        countE+=1  
    else:
        countO+=1
          
print("Number of even elements is/are:",countE)
print("Number of odd elements is/are:",countO)
    

