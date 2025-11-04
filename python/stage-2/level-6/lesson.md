# Level 6: Loop Pseudocode (For Loops)

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 2: Pseudocode to Code

### Today's Mission

Loops let you repeat code without rewriting it! Today, you'll translate pseudocode with loops into Python. Learn to make your programs efficient and powerful!

---

### Learning Goals

- Understand loops in pseudocode
- Learn Python `for` loops and `range()`
- Translate loop pseudocode to Python
- Create programs that repeat efficiently

---

### Your Task

Here's pseudocode that counts from 1 to 5:

```text
START
    for i = 1 to 5
        print i
END
```python

**Translate to Python. Hints:**

- Use `for i in range(1, 6):` (note: range goes UP TO but not including 6)
- Indent code inside the loop
- `range(1, 6)` produces: 1, 2, 3, 4, 5

---

### How to Run

Expected output:

```python
1
2
3
4
5
```python

---

### Success Checklist

- [ ] Use `for` loop with `range()`
- [ ] Loop variable `i` from 1 to 5
- [ ] Print `i` each iteration
- [ ] Output shows 1 through 5
- [ ] Proper indentation

---

## ANSWER KEY

### Solution

```python
for i in range(1, 6):
    print(i)
```python

### Key Concepts

**`for` Loops:**

- Repeat code a specific number of times
- `for variable in sequence:` is the syntax

**`range()` Function:**

- `range(1, 6)` produces: 1, 2, 3, 4, 5
- Start (inclusive), Stop (exclusive)
- `range(1, 6)` means "from 1 up to but not including 6"

**Loop Variable:**

- `i` gets each value from the range, one per iteration
- First iteration: i = 1, print 1
- Second iteration: i = 2, print 2
- And so on...

**Why range(1, 6) for "1 to 5"?**

```python
range(1, 6) = [1, 2, 3, 4, 5]
              ↑           ↑
            start      stop (exclusive)
```python

---

**Loops are where programming gets really powerful!**

*Next up: Functions - writing reusable code!*


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
