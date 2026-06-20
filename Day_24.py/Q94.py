# Program to check string rotation

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    # Concatenate s1 with itself
    temp = s1 + s1
    return s2 in temp

# Example
s1 = "abcd"
s2 = "cdab"
if is_rotation(s1, s2):
    print("Yes, rotation")
else:
    print("Not rotation")
