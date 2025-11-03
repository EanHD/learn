# Level 6: Loop Pseudocode (For Loops)

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
```

**Translate to Python. Hints:**

- Use `for i in range(1, 6):` (note: range goes UP TO but not including 6)
- Indent code inside the loop
- `range(1, 6)` produces: 1, 2, 3, 4, 5

---

### How to Run

Expected output:

```
1
2
3
4
5
```

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
```

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

```
range(1, 6) = [1, 2, 3, 4, 5]
              ↑           ↑
            start      stop (exclusive)
```

---

**Loops are where programming gets really powerful!**

*Next up: Functions - writing reusable code!*
