# Level 5: Decision Pseudocode (If Statements)

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



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

```
How old are you?
20
You are an adult
```

If you enter 15:

```
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

```
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

```
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
