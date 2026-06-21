# Find common characters in two strings
def common_chars(str1, str2):
    return set(str1) & set(str2)

s1 = "microsoft"
s2 = "adobe"
print("Common characters:", common_chars(s1, s2))
