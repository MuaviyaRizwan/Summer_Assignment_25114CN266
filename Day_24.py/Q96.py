# Program to find longest word

sentence = input("Enter a sentence: ")
words = sentence.split()

longest = max(words, key=len)

print("Longest word =", longest)
print("Length =", len(longest))
