# Program to find first repeating character

s = "programming"

for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            print("First repeating character:", s[i])
            exit()
