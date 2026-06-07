def prime(n):
   count= 0
   for i in range(1,n+1):
       if(n%i==0):
           count+=1
       else:
           count=count 
       
   if(count>2):
        print(n,"is not a prime number")
        
   else:
       print(n,"is a prime number")               

       
       
       
n = int(input("Enter number:"))
prime(n)    