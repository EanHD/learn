# Level 2: Variables
## Stage 1: Copying Code

### Today's Mission

Now that you know how to run Python programs, let's learn about variables! Variables are like containers that store information. In Python, you don't need to declare types - Python figures it out automatically!

---

### Learning Goals

- Understand what variables are and why they're useful
- Learn Python's dynamic typing system
- Practice storing and displaying different types of data
- See how variables make code reusable

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `variables.py`**

```python
# Store some information in variables
name = "Alice"
age = 25
height = 5.6
is_student = True

# Display the information
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Your height is {height} feet.")
print(f"Student status: {is_student}")
```

---

### How to Run

1. **Open your terminal** (or command prompt)
2. **Navigate to where you saved your file**:
    ```bash
    cd /path/to/your/folder
    ```
3. **Run the code**:
    ```bash
    python3 variables.py
    ```

**Expected output:**
```
Hello, Alice!
You are 25 years old.
Your height is 5.6 feet.
Student status: True
```

---

### Success Checklist

- [ ] Created a file named `variables.py`
- [ ] Copied the code exactly as shown
- [ ] Ran the program successfully
- [ ] Saw all four lines of output with the stored values

---

### What Happened?

You just used variables to store and display different types of information! Here's what each part does:

- `name = "Alice"` - Stores text (string) in a variable
- `age = 25` - Stores a whole number (integer) in a variable
- `height = 5.6` - Stores a decimal number (float) in a variable
- `is_student = True` - Stores a true/false value (boolean) in a variable
- `print(f"...{variable}...")` - Displays text with variable values inserted

---

### Try This (Optional Challenges)

If you're feeling brave, try these modifications:

1. Change the name, age, height, and student status to your own information
2. Add a new variable for your favorite color and display it
3. Try changing a variable's value halfway through the program

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```python
# Store some information in variables
name = "Alice"
age = 25
height = 5.6
is_student = True
```

- **`name = "Alice"`** = Creates variable `name` and assigns string value
- **`age = 25`** = Creates variable `age` and assigns integer value
- **`height = 5.6`** = Creates variable `height` and assigns float value
- **`is_student = True`** = Creates variable `is_student` and assigns boolean value
- **`#`** = Comment - ignored by Python, for human readers

```python
# Display the information
print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Your height is {height} feet.")
print(f"Student status: {is_student}")
```

- **`f"Hello, {name}!"`** = F-string formatting - inserts variable values into strings
- **`{name}`** = Placeholder where variable value gets inserted
- **Each print()** = Displays one line of formatted text

### Variable Types in Python

| Type | Example | Description |
|------|---------|-------------|
| `str` | `"Alice"`, `'Bob'` | Text data |
| `int` | `25`, `-10`, `0` | Whole numbers |
| `float` | `5.6`, `3.14`, `-2.5` | Decimal numbers |
| `bool` | `True`, `False` | True/false values |

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `NameError: name 'Name' is not defined` | Wrong variable name | Use exact name: `name` not `Name` |
| `SyntaxError: invalid syntax` | Missing quotes on strings | Add quotes: `name = "Alice"` |
| `TypeError` | Wrong type in f-string | Ensure variable exists before using |

### Bonus Knowledge

- **Dynamic Typing**: Python figures out variable types automatically
- **Variable Names**: Can contain letters, numbers, underscores (can't start with number)
- **Case Sensitive**: `name` and `Name` are different variables
- **F-strings**: Modern way to format strings (Python 3.6+)

---

 **Great job! You now understand variables in Python!** 

*Keep moving forward - next up: Basic Math Operations!*