# Row-wise Sum
rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

print("Enter matrix:")
a = [[int(input()) for j in range(cols)] for i in range(rows)]

for i in range(rows):
    row_sum = sum(a[i])
    print(f"Sum of row {i+1} =", row_sum)
