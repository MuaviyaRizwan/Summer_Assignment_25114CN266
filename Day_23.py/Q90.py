# Program to find first non-repeating character

s = "programming"

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1
    if count == 1:
        print("First non-repeating character:", s[i])
        break
