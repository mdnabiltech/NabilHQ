
s = input("Give me a word: ")

i = -1

for c in s:
    if s.count(c) == 1:
        i = s.index(c)
        break

print(f"Output: {i}")
