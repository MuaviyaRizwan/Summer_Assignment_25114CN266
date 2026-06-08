# Write a program to Write function for perfect
# number.
def perfect(n):
    temp = 0
    for i in range(1,n):
        if(n%i==0):
            temp+=i
    return temp    
num = int(input("Enter number:"))
P  =  perfect(num)
if(P == num):
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")
            
            
        
