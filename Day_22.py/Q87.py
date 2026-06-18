# Character frequency
s = input("Enter a string: ")

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1   # count each character

print("Character frequencies:")
for ch, count in freq.items():
    print(ch, ":", count)
