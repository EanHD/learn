# Level 7: Function Pseudocode

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
```

**Translate to Python. Hints:**

- `def` keyword defines a function
- Function name followed by `(parameters):`
- Indent code inside the function
- Call the function with `name(arguments)`

---

### How to Run

Expected output:

```
Hello, Alice!
Hello, Bob!
```

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
```

### Key Concepts

**Defining Functions:**

```python
def function_name(parameters):
    # Code inside function
    # Indented
```

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
```

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
