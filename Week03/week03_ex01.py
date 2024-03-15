# This script takes a word and prints each letter in squares.

word = "gżegżółka"
line = "+---"
word_len = len(word)

print(line * word_len + "+")

for x in word:
    print(f"| {x} ", end = "")

print("|")
print(line * word_len + "+")