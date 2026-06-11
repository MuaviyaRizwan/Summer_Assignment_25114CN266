# Write a program to Reverse array.
A=[]
n = int(input("Enter number of elements to be entered in the arraya:"))
for i in range(n):
    A.append(int(input())) # 0 1 2 3 4
print("Original array:")   #[2,4,7,3,1]
revrese_A =[]
for j in range(n-1,-1,-1):
    revrese_A.append(A[j])
print("Reversed array:",revrese_A)
    
    