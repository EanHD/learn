# Level 4: User Input

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

So far, our programs have used fixed values. Now let's make programs that interact with users! Python's `input()` function lets users type information that our program can use. This makes programs much more useful and fun!

---

### Learning Goals

- Learn how to get input from users
- Understand type conversion (string to number)
- Practice combining input with output
- Create interactive programs

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `input.py`**

```
# Get user information
name = input("What is your name? ")
age = int(input("How old are you? "))
favorite_color = input("What is your favorite color? ")

# Display personalized message
print(f"\nHello, {name}!")
print(f"You are {age} years old.")
print(f"Your favorite color is {favorite_color}.")
print(f"Nice to meet you, {name}!")
```

---

### How to Run

1. **Open your terminal** (or command prompt)
2. **Navigate to where you saved your file**:
    ```
    cd /path/to/your/folder
    ```
3. **Run the code**:
    ```
    python3 input.py
    ```
4. **Follow the prompts** - type your answers when asked!

**Example interaction:**
```
What is your name? Alice
How old are you? 25
What is your favorite color? Blue

Hello, Alice!
You are 25 years old.
Your favorite color is Blue.
Nice to meet you, Alice!
```

---

### Success Checklist

- [ ] Created a file named `input.py`
- [ ] Copied the code exactly as shown
- [ ] Ran the program and provided input when prompted
- [ ] Saw personalized output using your input

---

### What Happened?

You just created an interactive program! Here's what each part does:

- `input("prompt")` - Displays prompt and waits for user typing
- `int(input("..."))` - Converts text input to integer
- The program pauses at each input() and waits for you to type
- Press Enter after typing each response

---

### Try This (Optional Challenges)

If you're feeling brave, try these modifications:

1. Add another input question (like favorite food)
2. Change the age to calculate next birthday
3. Try removing `int()` and see what happens

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```
# Get user information
name = input("What is your name? ")
age = int(input("How old are you? "))
favorite_color = input("What is your favorite color? ")
```

- **`input("What is your name? ")`** = Displays prompt, gets text input
- **`int(input("How old are you? "))`** = Gets input, converts to integer
- **`name = ...`** = Stores input in variable `name`

```
# Display personalized message
print(f"\nHello, {name}!")
print(f"You are {age} years old.")
print(f"Your favorite color is {favorite_color}.")
print(f"Nice to meet you, {name}!")
```

- **`f"\nHello, {name}!"`** = Newline then personalized greeting
- **Uses stored variables** = Program remembers what user typed

### Input Function Details

- **`input(prompt)`** = Returns string (text) always
- **Type conversion needed** = Use `int()` for numbers, `float()` for decimals
- **Program waits** = Execution pauses until user presses Enter
- **Includes newline** = Input includes the Enter key press

### Type Conversion Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `int()` | String to integer | `int("25")` → `25` |
| `float()` | String to float | `float("3.14")` → `3.14` |
| `str()` | Number to string | `str(25)` → `"25"` |

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `ValueError: invalid literal for int()` | Non-numeric input | Add error handling or use try/except |
| `TypeError` | Wrong type in operation | Convert input to correct type |

### Bonus Knowledge

- **Input always returns string** = Even numbers come as text
- **Whitespace included** = Input includes spaces and newlines
- **Empty input** = User can press Enter without typing
- **Interactive programs** = Input makes programs conversational

---

 **Fantastic! Your programs can now talk to users!**

*Keep moving forward - next up: Conditionals and Decision Making!*


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic
