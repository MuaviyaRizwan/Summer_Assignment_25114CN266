# Write a program to Write function for Fibonacci.
def Fibonacci(n):
    a = 0
    b = 1
    print("Fibonacci series upto range",n,"is :",end=" ")
    print(a,b,end=" ")
    for i in range(n-2):
        c = a+b
        a = b
        b = c
        print(c,end=" ")
        
    
n = int(input("Enter range:"))
Fibonacci(n)

