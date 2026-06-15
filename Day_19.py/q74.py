# Matrix Subtraction
rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

print("Enter first matrix:")
a = [[int(input()) for j in range(cols)] for i in range(rows)]

print("Enter second matrix:")
b = [[int(input()) for j in range(cols)] for i in range(rows)]

# Subtract matrices
diff_matrix = [[a[i][j] - b[i][j] for j in range(cols)] for i in range(rows)]

print("Resultant Matrix (Subtraction):")
for row in diff_matrix:
    print(row)
