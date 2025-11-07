# Level 7: Function Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 2: Pseudocode to Code

### Today's Mission

Functions let you write code once and use it many times! Today, you'll learn to translate pseudocode with functions into Python. This is one of the most important skills in programming!

---

### Learning Goals

- Understand functions in pseudocode
- Learn to define and call functions in Python
- Translate function pseudocode to Python
- Write reusable, organized code

---

### Your Task

Here's pseudocode for a program with a function:

```text
START
    FUNCTION greet(name)
        print "Hello, " + name + "!"
    END FUNCTION

    greet("Alice")
    greet("Bob")
END
```python

**Translate to Python. Hints:**

- `def` keyword defines a function
- Function name followed by `(parameters):`
- Indent code inside the function
- Call the function with `name(arguments)`

---

### How to Run

Expected output:

```python
Hello, Alice!
Hello, Bob!
```python

---

### Success Checklist

- [ ] Define `greet` function with `name` parameter
- [ ] Function prints greeting with name
- [ ] Call function twice with different names
- [ ] Output shows both greetings
- [ ] Proper indentation

---

## ANSWER KEY

### Solution

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Alice")
greet("Bob")
```python

### Key Concepts

**Defining Functions:**

```python
def function_name(parameters):
    # Code inside function
    # Indented
```python

**Function Components:**

- `def` - Keyword to define a function
- `greet` - Function name
- `(name)` - Parameters (inputs the function accepts)
- `:` - Colon indicates start of function body
- Indented code - The function body

**Calling Functions:**

```python
greet("Alice")  # Call greet with "Alice" as argument
                # name = "Alice" inside the function
```python

**Parameters vs Arguments:**

- **Parameter:** `name` in `def greet(name):`
- **Argument:** `"Alice"` in `greet("Alice")`

**How It Works:**

1. Define function `greet` - tells Python what it does
2. Call `greet("Alice")` - executes the function with name="Alice"
3. Prints: Hello, Alice!
4. Call `greet("Bob")` - executes again with name="Bob"
5. Prints: Hello, Bob!

---

**Excellent! You now understand functions - a fundamental building block!**

*Stage 2 complete! You've learned to translate logic into code!*


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
