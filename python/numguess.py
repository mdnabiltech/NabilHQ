import random

rand = random.randint(1, 100)
tries = 0

while True: 
    guess = int(input("What's your guess: "))
    tries += 1

    if guess == rand:
        print(f"You got it! Took you {tries} tries")
        break
    elif guess > rand:
        print("Try again, you're too high")
    elif guess < rand:
        print("Try again, you're too low")



