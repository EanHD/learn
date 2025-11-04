# Level 4: Input/Output Pseudocode

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 2: Pseudocode to Code

### Today's Mission

Programs that only print fixed data are boring! Today, you'll learn to take input from users and respond to it. This makes your programs interactive!

---

### Learning Goals

- Understand user input in pseudocode
- Learn the `input()` function in Python
- Translate I/O pseudocode to Python
- Create interactive programs

---

### Your Task

Here's pseudocode for an interactive program:

```text
START
    print "What is your name?"
    name = get input from user
    print "Hello, " + name + "!"
END
```

**Your mission**: Translate to Python. In Python, `input()` gets user input, and `+` concatenates strings.

---

### How to Run

1. Navigate to workspace
2. Run: `python3 main.py`
3. When prompted, type your name and press Enter

**If you type "Bob":**

```
What is your name?
Bob
Hello, Bob!
```

---

### Success Checklist

- [ ] Prompt user for name
- [ ] Store input in variable
- [ ] Greet user with their name
- [ ] Use string concatenation with +

---

## ANSWER KEY

### Solution

```python
print("What is your name?")
name = input()
print("Hello, " + name + "!")
```

### Key Concepts

**`input()` Function:**

- Stops program and waits for user to type
- Returns what user typed as a string
- Common pattern: `variable = input()`

**String Concatenation:**

- Join strings with `+` operator
- `"Hello, " + name + "!"` combines three strings

**Example:**

```python
name = input()        # User types: "Alice"
# Now name = "Alice" (a string)
print("Hi, " + name)  # Prints: Hi, Alice
```

---

**You've made an interactive program!**

*Next up: Making decisions with conditionals!*
