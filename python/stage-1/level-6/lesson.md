# Level 6: Loops and Repetition

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Loops let your program do the same thing multiple times automatically! This is perfect for repetitive tasks. Python has `for` loops (when you know how many times) and `while` loops (when you don't). Let's automate some counting and patterns!

---

### Learning Goals

- Learn `for` and `while` loop syntax
- Understand loop control with `range()`
- Practice repetitive operations
- Create programs that automate tasks

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `loops.py`**

```python
# While loop example - countdown
print("While loop countdown:")
count = 5
while count > 0:
    print(f"Count: {count}")
    count = count - 1
print("Blast off!\n")

# For loop with range - counting up
print("For loop counting:")
for i in range(1, 6):
    print(f"Number: {i}")
print()

# For loop - iterating through a list
print("Favorite fruits:")
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"I like {fruit}s")
print()

# Nested loops - multiplication table
print("Multiplication table (3x):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} × {j} = {result}")
    print()  # Empty line between rows
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
    python3 loops.py
    ```

**Expected output:**
```
While loop countdown:
Count: 5
Count: 4
Count: 3
Count: 2
Count: 1
Blast off!

For loop counting:
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5

Favorite fruits:
I like apples
I like bananas
I like oranges
I like grapes

Multiplication table (3x):
1 × 1 = 1
1 × 2 = 2
1 × 3 = 3

2 × 1 = 2
2 × 2 = 4
2 × 3 = 6

3 × 1 = 3
3 × 2 = 6
3 × 3 = 9
```

---

### Success Checklist

- [ ] Created a file named `loops.py`
- [ ] Copied the code exactly as shown
- [ ] Ran the program successfully
- [ ] Saw all four different loop examples execute

---

### What Happened?

You just automated repetitive tasks with loops! Here's what each loop does:

- `while condition:` - Repeats while condition is true
- `for item in sequence:` - Repeats for each item in a sequence
- `range(start, end)` - Creates sequence of numbers
- Nested loops - loops inside loops for complex patterns

---

### Try This (Optional Challenges)

If you're feeling brave, try these modifications:

1. Change the countdown starting number
2. Add more fruits to the list
3. Make a bigger multiplication table

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```python
# While loop example - countdown
count = 5
while count > 0:
    print(f"Count: {count}")
    count = count - 1
```

- **`while count > 0:`** = Loop while count is greater than 0
- **`count = count - 1`** = Decrement counter each iteration
- **Must change condition** = Or loop runs forever!

```python
# For loop with range - counting up
for i in range(1, 6):
    print(f"Number: {i}")
```

- **`range(1, 6)`** = Numbers 1, 2, 3, 4, 5 (up to but not including 6)
- **`for i in ...:`** = `i` takes each value in sequence
- **Automatic counting** = No manual counter needed

```python
# For loop - iterating through a list
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"I like {fruit}s")
```

- **List** = Collection of items in square brackets `[]`
- **`for fruit in fruits:`** = `fruit` becomes each item in list
- **Works with any sequence** = Lists, strings, ranges, etc.

### Loop Control

| Keyword | Purpose | Example |
|---------|---------|---------|
| `break` | Exit loop immediately | `if x == 5: break` |
| `continue` | Skip to next iteration | `if x == 3: continue` |
| `else` | Run after loop completes | `while condition: ... else: ...` |

### Range Function

| Usage | Produces | Example |
|-------|----------|---------|
| `range(5)` | 0, 1, 2, 3, 4 | `for i in range(5)` |
| `range(1, 6)` | 1, 2, 3, 4, 5 | `for i in range(1, 6)` |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 | `for i in range(0, 10, 2)` |

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `IndentationError` | Wrong indentation | Use consistent indentation |
| Infinite loop | Condition never false | Ensure condition changes |

### Bonus Knowledge

- **Iterables** = Anything you can loop through (lists, strings, files)
- **List comprehensions** = Compact way to create lists
- **Generator expressions** = Memory-efficient sequences
- **Loop else clause** = Code that runs if loop wasn't broken

---

 **Excellent! Your programs can now repeat tasks automatically!** 

*Keep moving forward - next up: Functions - Code Organization!*