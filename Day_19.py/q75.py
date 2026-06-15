# Transpose of Matrix
rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

print("Enter matrix:")
a = [[int(input()) for j in range(cols)] for i in range(rows)]

transpose = [[a[j][i] for j in range(rows)] for i in range(cols)]

print("Transpose of Matrix:")
for row in transpose:
    print(row)
