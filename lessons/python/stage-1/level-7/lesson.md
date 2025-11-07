# Level 7: Functions - Code Organization

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Functions let you organize code into reusable blocks! Instead of repeating the same code, you write it once as a function and call it whenever needed. This makes programs cleaner, easier to understand, and easier to maintain.

---

### Learning Goals

- Learn function definition with `def`
- Understand parameters and return values
- Practice calling functions
- See how functions organize code

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `functions.py`**

```
# Function definitions
def greet(name):
    """Return a personalized greeting."""
    return f"Hello, {name}!"

def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def display_info(name, age, city):
    """Display formatted information about a person."""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print("-" * 20)

# Using the functions
print(greet("Alice"))
print(greet("Bob"))
print()

area = calculate_area(5, 3)
print(f"Area of 5×3 rectangle: {area}")
print()

print("Even numbers check:")
for num in [1, 2, 3, 4, 5]:
    result = is_even(num)
    print(f"{num} is even: {result}")
print()

print("Person information:")
display_info("Alice", 25, "New York")
display_info("Bob", 30, "London")
```

---

### How to Run

1. **Open your terminal** (or command prompt)
2. **Navigate to where you saved your file**:
    ```
    cd /path/to/your/folder
    ```
3. **Run the code**:
    ```
    python3 functions.py
    ```

**Expected output:**
```
Hello, Alice!
Hello, Bob!

Area of 5×3 rectangle: 15

Even numbers check:
1 is even: False
2 is even: True
3 is even: False
4 is even: True
5 is even: False

Person information:
Name: Alice
Age: 25
City: New York
--------------------
Name: Bob
Age: 30
City: London
--------------------
```

---

### Success Checklist

- [ ] Created a file named `functions.py`
- [ ] Copied the code exactly as shown
- [ ] Ran the program successfully
- [ ] Saw all function examples work correctly

---

### What Happened?

You just organized code into reusable functions! Here's what each part does:

- `def function_name(parameters):` - Defines a new function
- `return value` - Sends result back to caller
- `function_name(arguments)` - Calls the function with values
- Functions group related code and can be reused

---

### Try This (Optional Challenges)

If you're feeling brave, try these modifications:

1. Add a new function for calculating circle area
2. Modify display_info to include more details
3. Create a function that converts Celsius to Fahrenheit

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```
def greet(name):
    """Return a personalized greeting."""
    return f"Hello, {name}!"
```

- **`def greet(name):`** = Define function named `greet` with parameter `name`
- **`"""Return a personalized greeting."""`** = Docstring (documentation)
- **`return f"Hello, {name}!"`** = Return formatted greeting string

```
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width
```

- **Two parameters** = `length` and `width`
- **Returns calculation** = Result of multiplication
- **Called as** = `calculate_area(5, 3)`

```
def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0
```

- **Boolean return** = Returns `True` or `False`
- **`number % 2 == 0`** = Even if remainder when divided by 2 is 0

```
def display_info(name, age, city):
    """Display formatted information about a person."""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print("-" * 20)
```

- **No return value** = Function prints directly (returns `None`)
- **Multiple statements** = Can contain many lines of code
- **Side effects** = Changes outside world (prints to screen)

### Function Components

| Component | Purpose | Example |
|-----------|---------|---------|
| `def` | Keyword to define function | `def my_function():` |
| Function name | Identifier for calling | `calculate_area` |
| Parameters | Input values | `(length, width)` |
| Docstring | Documentation | `"""Calculate area."""` |
| Body | Code to execute | Indented statements |
| `return` | Send result back | `return result` |

### Function Types

| Type | Returns | Example |
|------|---------|---------|
| Fruitful | Value | `return x + y` |
| Void | `None` | Just `print()` statements |
| Predicate | Boolean | `return x > 0` |

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `IndentationError` | Wrong indentation | Indent function body |
| `TypeError` | Wrong arguments | Match parameter count |
| `NameError` | Function not defined | Define before calling |

### Bonus Knowledge

- **Scope** = Variables inside functions are local
- **Default parameters** = `def func(x=5):`
- **Keyword arguments** = `func(x=10, y=20)`
- **Variable arguments** = `def func(*args):`
- **Lambda functions** = Anonymous functions

---

 **Congratulations! You've mastered Python functions!**

*You've completed Stage 1: Copying Code! Time to move to Stage 2: Pseudocode to Code!*


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic
