# Symmetric Matrix Check
n = int(input("Enter size of square matrix: "))

print("Enter matrix:")
a = [[int(input()) for j in range(n)] for i in range(n)]

symmetric = True
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            symmetric = False
            break

if symmetric:
    print("Matrix is Symmetric")
else:
    print("Matrix is NOT Symmetric")
