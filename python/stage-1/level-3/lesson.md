# Level 3: Basic Math Operations

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Time to do some math with Python! Programming is great for calculations. Python supports all the basic arithmetic operations you learned in school, plus some extras. Let's see how to perform calculations and display results.

---

### Learning Goals

- Learn Python's arithmetic operators
- Understand operator precedence
- Practice mathematical expressions
- See how to display calculation results

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `math.py`**

```python
# Some numbers to work with
a = 10
b = 3

# Basic arithmetic operations
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Integer Division: {a} // {b} = {a // b}")
print(f"Modulus (Remainder): {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
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
    python3 math.py
    ```

**Expected output:**
```
Addition: 10 + 3 = 13
Subtraction: 10 - 3 = 7
Multiplication: 10 * 3 = 30
Division: 10 / 3 = 3.3333333333333335
Integer Division: 10 // 3 = 3
Modulus (Remainder): 10 % 3 = 1
Exponentiation: 10 ** 3 = 1000
```

---

### Success Checklist

- [ ] Created a file named `math.py`
- [ ] Copied the code exactly as shown
- [ ] Ran the program successfully
- [ ] Saw all seven mathematical operations with their results

---

### What Happened?

You just performed mathematical calculations in Python! Here's what each operation does:

- `+` - Addition
- `-` - Subtraction
- `*` - Multiplication
- `/` - Division (always produces float)
- `//` - Integer division (whole number result)
- `%` - Modulus (remainder after division)
- `**` - Exponentiation (power)

---

### Try This (Optional Challenges)

If you're feeling brave, try these modifications:

1. Change the values of `a` and `b` to different numbers
2. Add more complex expressions like `a * b + 5`
3. Try negative numbers in calculations

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```python
# Some numbers to work with
a = 10
b = 3
```

- **`a = 10`** = Store 10 in variable `a`
- **`b = 3`** = Store 3 in variable `b`

```python
# Basic arithmetic operations
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Integer Division: {a} // {b} = {a // b}")
print(f"Modulus (Remainder): {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
```

- **Each line** = Calculates and displays one operation
- **`{a + b}`** = Performs calculation and inserts result
- **F-string formatting** = Combines text and calculations

### Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` |
| `//` | Integer Division | `10 // 3` | `3` |
| `%` | Modulus | `10 % 3` | `1` |
| `**` | Exponentiation | `10 ** 3` | `1000` |

### Operator Precedence

Python follows mathematical order:
1. `**` (exponentiation)
2. `*`, `/`, `//`, `%` (multiplication/division)
3. `+`, `-` (addition/subtraction)

Use parentheses `()` to change order: `(2 + 3) * 4 = 20`

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `ZeroDivisionError` | Dividing by zero | Use non-zero divisor |
| `TypeError` | Wrong types in operation | Ensure numeric types |

### Bonus Knowledge

- **Float Division**: `/` always gives float result
- **Integer Division**: `//` truncates toward negative infinity
- **Modulus**: Sign follows divisor (useful for programming)
- **Complex Expressions**: Combine operations with parentheses

---

 **Excellent! You can now do math with Python!** 

*Keep moving forward - next up: User Input!*
