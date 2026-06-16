# Column-wise Sum
rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

print("Enter matrix:")
a = [[int(input()) for j in range(cols)] for i in range(rows)]

for j in range(cols):
    col_sum = sum(a[i][j] for i in range(rows))
    print(f"Sum of column {j+1} =", col_sum)
