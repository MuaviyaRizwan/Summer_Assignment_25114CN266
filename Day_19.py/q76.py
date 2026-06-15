# Diagonal Sum of Square Matrix
n = int(input("Enter size of square matrix: "))

print("Enter matrix:")
a = [[int(input()) for j in range(n)] for i in range(n)]

# Main diagonal sum
main_sum = sum(a[i][i] for i in range(n))

# Secondary diagonal sum (optional)
sec_sum = sum(a[i][n-1-i] for i in range(n))

print("Main diagonal sum =", main_sum)
print("Secondary diagonal sum =", sec_sum)
