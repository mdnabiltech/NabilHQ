from collections import Counter

a = input("Give me a word: ").upper
b = input("Give me a word: ").upper

ax = Counter(a)
bx = Counter(b)

print(f"Output: {ax == bx}")
