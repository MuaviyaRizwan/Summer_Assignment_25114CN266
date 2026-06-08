# Write a program to Write function for Armstrong.

def Armstrong(n):
    A = 0
    while(n>=1):
        r = n%10
        A += r**3
        n = n//10
    return A    
    
num = int(input("Enter number:"))

arm = Armstrong(num)
if(arm == num):
    print(num, "is armstrong number")
else:
    print(num, "is not a armstrong number")    

