# Write a program to Write function for palindrome.
def palindrome(n):
    reverse = 0
    while(n>=1):
     r = n%10
     reverse = reverse*10 + r
     n = n//10
    return reverse
    
num  = int(input("Enter number:"))

Reverse =  palindrome(num)
if (Reverse==num):
    print(num, "is palindrome")
else:
    print(num,"is not palindrome")
        
