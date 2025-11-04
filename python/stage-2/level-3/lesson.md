# Level 3: Mathematical Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 2: Pseudocode to Code

### Today's Mission

Math is at the heart of programming! Today, you'll translate pseudocode that performs calculations into Python code. Learn how to make your programs do arithmetic!

---

### Learning Goals

- Understand mathematical operations in pseudocode
- Learn Python operators: +, -, *, /
- Translate math pseudocode to Python
- Practice calculating and storing results

---

### Your Task

Here's pseudocode for a simple calculator:

```text
START
    x = 10
    y = 5
    sum = x + y
    difference = x - y
    product = x * y
    quotient = x / y
    print sum
    print difference
    print product
    print quotient
END
```python

**Your mission**: Translate this into Python code.

---

### How to Run

1. Navigate to workspace:

    ```bash
    cd ~/.local/share/learn/workspaces/python/stage-2/level-3
    ```bash

2. Edit and run main.py

**Expected output:**

```python
15
5
50
2.0
```python

---

### Success Checklist

- [ ] Assigned x=10 and y=5
- [ ] Calculated sum, difference, product, quotient
- [ ] Each result printed on separate line
- [ ] Output matches expected exactly

---

## ANSWER KEY

### Solution

```python
x = 10
y = 5
sum = x + y
difference = x - y
product = x * y
quotient = x / y
print(sum)
print(difference)
print(product)
print(quotient)
```python

### Key Concepts

**Arithmetic Operators:**

- `+` Addition: `10 + 5 = 15`
- `-` Subtraction: `10 - 5 = 5`
- `*` Multiplication: `10 * 5 = 50`
- `/` Division: `10 / 5 = 2.0` (always returns float)

**Expression Evaluation:**

```python
sum = x + y
      ↑    ↑
    variable values are looked up, added, result stored
```python

**Why 2.0 not 2?**
In Python 3, division with `/` always returns a float (decimal number).

---

**Great! You're now a calculator programmer!**

*Next up: Getting input from users!*


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic


<div style="page-break-after: always;"></div>

## Answer Key

### Complete Solution

```py
print("Hello, World!")

```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard python conventions with proper imports and main function
2. **Variables**: Data types are correctly declared and initialized
3. **Logic**: The program implements the required functionality
4. **Output**: Results are displayed clearly to the user
5. **Best Practices**: Code is readable and follows naming conventions

### Testing Your Solution

Try these test cases to verify your code works correctly:

1. **Basic Test**: Run the program with standard inputs
2. **Edge Cases**: Test with boundary values (0, -1, very large numbers)
3. **Error Handling**: Verify the program handles invalid inputs gracefully

### Tips for Understanding

- Review each section carefully
- Try modifying values to see how output changes
- Add your own printf/print statements to trace execution
- Experiment with different inputs
