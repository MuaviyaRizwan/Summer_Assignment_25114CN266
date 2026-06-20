# Program to find maximum occurring character

s = "programming"

max_count = 0
max_char = None

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1
    if count > max_count:
        max_count = count
        max_char = s[i]

print("Maximum occurring character:", max_char)
print("Frequency:", max_count)
