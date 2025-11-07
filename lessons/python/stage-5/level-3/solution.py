import random

secret = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number 1-100")
while True:
    guess = int(input("Guess: "))
    attempts = attempts + 1

    if guess == secret:
        print("Correct! You got it in " + str(attempts) + " attempts")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
