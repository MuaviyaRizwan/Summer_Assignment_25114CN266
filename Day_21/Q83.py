# Program to count vowels and consonants

string = input("Enter a string: ")
vowels = 0
consonants = 0

for ch in string:
    if ch.isalpha():  # check only letters
        ch = ch.lower()
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
