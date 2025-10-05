import random

print("Welcome to the Math Multiplication Madness!")
print()

score = 0

for i in range(1, 6):
    x = random.randint(pow(2, i), pow(3, i)) 
    y = random.randint(pow(2, i), pow(3, i))

    ans = int(input(f"Question {i}: What is {x} times {y}: "))

    if ans == x * y:
        score += 1
        print("Correcto Mundo!")
    else:
        print(f"Frick! Better luck next time, it was actually {x * y}")
print(f"You answered {score} question{'s' if score != 1 else ''} correctly.")
