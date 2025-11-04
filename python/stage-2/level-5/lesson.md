# Level 5: Decision Pseudocode (If Statements)

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 2: Pseudocode to Code

### Today's Mission

Programs that make decisions are powerful! Today, you'll translate pseudocode with conditionals (if statements) into Python. Learn to make your programs respond differently based on input!

---

### Learning Goals

- Understand conditional logic in pseudocode
- Learn Python `if` and `else` statements
- Translate decision pseudocode to Python
- Create programs that respond intelligently

---

### Your Task

Here's pseudocode for a program that checks age:

```text
START
    print "How old are you?"
    age = get input from user
    if age >= 18
        print "You are an adult"
    else
        print "You are a minor"
END
```

**Translate to Python. Hints:**

- `age = input()` gets the input but returns a STRING
- Convert to number: `age = int(input())`
- `>=` means "greater than or equal to"
- Indentation matters in Python!

---

### How to Run

If you enter 20:

```python
How old are you?
20
You are an adult
```

If you enter 15:

```python
How old are you?
15
You are a minor
```

---

### Success Checklist

- [ ] Prompt for age
- [ ] Convert input to integer with `int()`
- [ ] Check if age >= 18
- [ ] Print appropriate message
- [ ] Proper indentation under `if` and `else`

---

## ANSWER KEY

### Solution

```python
print("How old are you?")
age = int(input())
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### Key Concepts

**`int()` Conversion:**

- `input()` returns string: "20"
- `int("20")` converts to number: 20
- Compare numbers with `>=`, `<=`, `==`, `!=`

**If/Else Structure:**

```python
if condition:
    code if true
else:
    code if false
```

**Indentation:**

- Python uses indentation (spaces) to show code blocks
- Indent code inside `if` and `else` with 4 spaces

---

**Congratulations! Your program makes decisions!**

*Next up: Loops - doing things repeatedly!*
