#Write a program to Find duplicates in array.
A=[]
n = int((input("Enter the number of elements to be entered in the  array:")))
for i in range(n):
    A.append(int(input()))
print("Array:",A)

for j in range(n):           #0 1 2
    for k in range(j+1,n):  #[1,2,1]
     if( A[j]==A[k]):
        print("Array  has duplicate of:",A[j])

        
        
        

            
    
        