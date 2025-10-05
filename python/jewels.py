jewels = "aA"
stones = "aAAbbbb"

count = 0

for c in stones:
    if c in jewels:
        count += 1

print(count)
