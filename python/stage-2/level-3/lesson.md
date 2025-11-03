# Level 3: Mathematical Pseudocode

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
```

**Your mission**: Translate this into Python code.

---

### How to Run

1. Navigate to workspace:

    ```bash
    cd ~/.local/share/learn/workspaces/python/stage-2/level-3
    ```

2. Edit and run main.py

**Expected output:**

```
15
5
50
2.0
```

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
```

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
```

**Why 2.0 not 2?**
In Python 3, division with `/` always returns a float (decimal number).

---

**Great! You're now a calculator programmer!**

*Next up: Getting input from users!*
