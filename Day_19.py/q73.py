# Matrix Addition
rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

print("Enter first matrix:")
a = [[int(input()) for j in range(cols)] for i in range(rows)]

print("Enter second matrix:")
b = [[int(input()) for j in range(cols)] for i in range(rows)]

# Add matrices
sum_matrix = [[a[i][j] + b[i][j] for j in range(cols)] for i in range(rows)]

print("Resultant Matrix (Addition):")
for row in sum_matrix:
    print(row)
