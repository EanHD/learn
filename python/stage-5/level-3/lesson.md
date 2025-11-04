# Level 3: Number Guessing Game

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 5: Capstone Project

### Your Project

Build a game that:

1. Computer picks random number 1-100
2. Player guesses
3. Computer says higher/lower
4. Counts attempts
5. Declares winner with attempts

---

## ANSWER KEY

```python
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
```

---

**Random numbers and game loops!**
