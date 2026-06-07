def max(a,b,c):
    if(a>b or a>c):
        return a
    elif(b>c):
        return b
    else:
        return c
    
a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))

print("Maximum is :",max(a,b,c))
    