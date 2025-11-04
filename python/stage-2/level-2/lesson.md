# Level 2: Variables in Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 2: Pseudocode to Code

### Today's Mission

Variables are like labeled boxes where you store information. Today, you'll learn to translate pseudocode that uses variables into real Python code. This opens up possibilities for creating programs that remember and manipulate data!

---

### Learning Goals

- Understand variables and variable assignment
- Learn how to name variables properly
- Translate variable pseudocode to Python
- Practice storing and displaying data

---

### Your Task

Here's some pseudocode that uses variables:

```text
START
    name = "Alice"
    age = 25
    print name
    print age
END
```python

**Your mission**: Translate this pseudocode into Python code.

Hints:

- `name = "Alice"` creates a variable called `name` and stores the text "Alice" in it
- `age = 25` creates a variable called `age` and stores the number 25
- `print name` prints the VALUE stored in the variable (not the word "name")
- Use the exact same syntax as the pseudocode

---

### How to Run

1. **Open your terminal**
2. **Navigate to your workspace**:

    ```bash
    cd ~/.local/share/learn/workspaces/python/stage-2/level-2
    ```bash

3. **Edit main.py**
4. **Run it**:

    ```bash
    python3 main.py
    ```python

**Expected output:**

```python
Alice
25
```python

---

### Success Checklist

- [ ] Created two variable assignments
- [ ] First variable stores a name (string)
- [ ] Second variable stores an age (number)
- [ ] Two print statements display the values
- [ ] Output matches expected output

---

### Key Difference: Variables vs Strings

- `print("name")` - Prints the word "name" literally
- `print(name)` - Prints the VALUE stored in variable name

This is crucial! Remove quotes to access the variable.

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY

### Solution

```python
name = "Alice"
age = 25
print(name)
print(age)
```python

### Explanation

**Line 1 & 2: Variable Assignment**

```python
name = "Alice"      # Create variable 'name', store "Alice"
age = 25            # Create variable 'age', store 25
```python

The `=` operator assigns values to variables.

**Line 3 & 4: Using Variables**

```python
print(name)         # Print value IN variable name
print(age)          # Print value IN variable age
```python

Without quotes, Python looks up the variable and uses its value.

### Key Concepts

**Variables:**

- Named containers for storing data
- Can hold strings, numbers, or other types
- Created with assignment: `variable_name = value`

**Naming Rules:**

- Start with letter or underscore
- Can contain letters, numbers, underscores
- Are case-sensitive (`name` ≠ `Name`)
- Use lowercase with underscores: `first_name` (Python style)

**Data Types:**

- Strings: `"text"` (in quotes)
- Integers: `25` (no quotes)
- Floats: `3.14` (decimals)

### Common Mistakes & Solutions

| Mistake | Problem | Solution |
|---------|---------|----------|
| `print("name")` | Prints literal word | Remove quotes: `print(name)` |
| `name = Alice` | Missing quotes on string | Add quotes: `name = "Alice"` |
| `Name = "Alice"` then `print(name)` | Case mismatch | Variable names are case-sensitive |
| `age = "25"` | Storing number as string | Remove quotes: `age = 25` |

### How Variables Work

```python
Step 1: name = "Alice"
        Memory: [name] → "Alice"

Step 2: print(name)
        Python: Look up "name" → find "Alice" → print it
        Output: Alice
```python

---

**Excellent! Variables are the foundation of real programming!**

*Next up: Mathematical operations with variables!*


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
