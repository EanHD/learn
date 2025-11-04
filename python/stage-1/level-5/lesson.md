# Level 5: Conditionals and Decision Making

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Programs that can make decisions are much more powerful! Python's `if`, `elif`, and `else` statements let your program choose different actions based on conditions. This is how programs become smart and responsive.

---

### Learning Goals

- Learn conditional statements (`if`, `elif`, `else`)
- Understand comparison operators
- Practice decision-making logic
- Create programs that respond differently to different inputs

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `conditionals.py`**

```python
# Get user input
age = int(input("How old are you? "))
temperature = float(input("What is the temperature in Celsius? "))

# Age-based decisions
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Temperature-based decisions
if temperature < 0:
    print("It's freezing! Wear a heavy coat.")
elif temperature < 15:
    print("It's cold. Bring a jacket.")
elif temperature < 25:
    print("It's mild weather.")
else:
    print("It's hot! Stay cool.")
```

---

### How to Run

1. **Open your terminal** (or command prompt)
2. **Navigate to where you saved your file**:
    ```bash
    cd /path/to/your/folder
    ```
3. **Run the code**:
    ```bash
    python3 conditionals.py
    ```
4. **Provide input** when prompted!

**Example interaction:**
```python
How old are you? 25
What is the temperature in Celsius? 22

You are an adult.
It's mild weather.
```

---

### Success Checklist

- [ ] Created a file named `conditionals.py`
- [ ] Copied the code exactly as shown
- [ ] Ran the program with different inputs
- [ ] Saw different outputs based on your input values

---

### What Happened?

You just created a program that makes decisions! Here's how it works:

- `if condition:` - Checks if condition is true, runs indented code if so
- `elif condition:` - Checks alternative condition if previous were false
- `else:` - Runs if no previous conditions were true
- Indentation matters - the code under each condition must be indented

---

### Try This (Optional Challenges)

If you're feeling brave, try these modifications:

1. Add more age categories or temperature ranges
2. Create a grading system (90-100 = A, etc.)
3. Combine conditions with `and`/`or`

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```python
# Get user input
age = int(input("How old are you? "))
temperature = float(input("What is the temperature in Celsius? "))
```

- **Gets numeric input** = Age as integer, temperature as float

```python
# Age-based decisions
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

- **`if age < 13:`** = Checks if age is less than 13
- **`elif age < 20:`** = If not child, checks if less than 20
- **`else:`** = If none above, must be 65 or older
- **Only one block executes** = First true condition wins

### Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `age == 25` |
| `!=` | Not equal to | `age != 25` |
| `<` | Less than | `age < 25` |
| `<=` | Less than or equal | `age <= 25` |
| `>` | Greater than | `age > 25` |
| `>=` | Greater than or equal | `age >= 25` |

### Logical Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both true | `age > 18 and age < 65` |
| `or` | Either true | `temperature < 0 or temperature > 30` |
| `not` | Negates | `not (age < 18)` |

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `IndentationError` | Wrong indentation | Use consistent 4 spaces |
| `SyntaxError` | Missing colon | Add `:` after conditions |

### Bonus Knowledge

- **Truthy/Falsy values** = Non-zero numbers, non-empty strings are "truthy"
- **Short-circuit evaluation** = `and`/`or` stop early when possible
- **Nested conditions** = `if` statements inside other `if` statements
- **Decision trees** = Complex logic with multiple branches

---

 **Awesome! Your programs can now make decisions!** 

*Keep moving forward - next up: Loops and Repetition!*
