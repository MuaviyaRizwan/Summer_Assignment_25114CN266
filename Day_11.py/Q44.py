def factorial(n):
    
    if(n==0 or n==1):
     return 1
    else:
     fact=factorial(n-1) * n   
     return fact
n = int(input("Enter the number:"))
print("Factorial of",n,"is:",factorial(n))
