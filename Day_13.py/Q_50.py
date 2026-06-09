#Write a program to Find sum and average of array.
A= []# empty array
n = int(input("Enter number of elements to be entered in array:"))
sum = 0
for i in range(n):
    A.append(int(input()))
    sum+=A[i]
    
print("The array is:",A)
print("Sum of elements in array:",sum)
print("Average of elemnts present in array:",sum/n)

    

