# Matrix Multiplication
rows_a = int(input("Enter rows of first matrix: "))
cols_a = int(input("Enter cols of first matrix: "))
rows_b = int(input("Enter rows of second matrix: "))
cols_b = int(input("Enter cols of second matrix: "))

if cols_a != rows_b:
    print("Matrix multiplication not possible!")
else:
    print("Enter first matrix:")
    a = [[int(input()) for j in range(cols_a)] for i in range(rows_a)]

    print("Enter second matrix:")
    b = [[int(input()) for j in range(cols_b)] for i in range(rows_b)]

    # Resultant matrix
    result = [[0 for j in range(cols_b)] for i in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    print("Resultant Matrix (Multiplication):")
    for row in result:
        print(row)
