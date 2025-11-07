# Level 3: Basic Math Operations

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.sql` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Master arithmetic operations and use the language as your calculator.

---

### Learning Goals

- Learn all basic arithmetic operators (+, -, *, /, %)
- Understand operator precedence (order of operations)
- Practice mathematical expressions
- Work with both integers and floating-point numbers

---

### Your Task

**Copy the following code EXACTLY as shown below into `main.sql`**

```
-- Math Operations in SQL
SELECT
    15 + 4 AS addition,
    15 - 4 AS subtraction,
    15 * 4 AS multiplication,
    15 / 4 AS division,
    15 % 4 AS remainder,
    15.0 / 4.0 AS precise_division;
```

---

### Success Checklist

- [ ] Created a file named `main.sql`
- [ ] Copied the code exactly as shown
- [ ] Ran the program successfully
- [ ] Understood the basic concepts
- [ ] Experimented with small modifications

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (Study after attempting!)

### The Complete Code

```
-- Math Operations in SQL
SELECT
    15 + 4 AS addition,
    15 - 4 AS subtraction,
    15 * 4 AS multiplication,
    15 / 4 AS division,
    15 % 4 AS remainder,
    15.0 / 4.0 AS precise_division;
```

### What This Code Does

This program demonstrates basic math operations in SQL.

### Key Concepts

- **Arithmetic Operators**: `+`, `-`, `*`, `/`, `%`
- **Integer Division**: Division with whole numbers
- **Floating-Point Division**: Division with decimals for precise results
- **Operator Precedence**: Order of operations (PEMDAS)

### Line-by-Line Breakdown

The code performs basic mathematical operations:

1. **Variable Declaration**: Store two numbers to work with
2. **Addition**: Adding two numbers together
3. **Subtraction**: Finding the difference between numbers
4. **Multiplication**: Multiplying numbers
5. **Division**: Dividing numbers (integer division)
6. **Remainder/Modulus**: Finding the remainder after division
7. **Precise Division**: Using decimals for accurate results

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Syntax error | Typo in code | Double-check spelling and punctuation |
| Type error | Wrong data type | Ensure variables are correct type |
| Runtime error | Code runs but crashes | Check your logic and data flow |

### Bonus Knowledge

- The modulus operator (%) is useful for checking if numbers are even or odd
- Integer division truncates (removes) decimal places
- Always use floating-point numbers when precision matters
- Order of operations: Parentheses → Multiply/Divide → Add/Subtract

---

**Excellent work! You've mastered basic math operations!**

*Continue to the next level to keep building your skills!*
