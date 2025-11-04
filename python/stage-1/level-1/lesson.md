# Level 1: Hello World

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Welcome to your first step into programming with Python! Today, you'll learn how to create your very first Python program. Don't worry about understanding everything yet - just focus on getting the code typed correctly and watching it work!

---

### Learning Goals

- Understand the basic structure of a Python program
- Learn how to run Python code
- See your first program output "Hello, World!"
- Get comfortable with your text editor

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `hello.py`**

```python
print("Hello, World!")
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
    python3 hello.py
    ```

**Expected output:**
```
Hello, World!
```

---

### Success Checklist

- [ ] Created a file named `hello.py`
- [ ] Copied the code exactly as shown
- [ ] Ran the program successfully
- [ ] Saw "Hello, World!" printed on screen

---

### What Happened?

You just created a real computer program! Here's what each part does:

- `print(...)` - A function that prints text to the screen
- `"Hello, World!"` - The message to print
- The parentheses `()` - Contain the arguments passed to the function

---

### Try This (Optional Challenges)

If you're feeling brave, try these small changes:

1. Change the message to "Hello, Python Programming!"
2. Add another print() line with your name
3. Remove the quotes and see what happens

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```python
print("Hello, World!")
```

- **`print`** = Built-in function that displays text
- **`"`** = String literal start/end delimiters
- **`"Hello, World!"`** = String argument passed to print function
- **`(` and `)`** = Function call parentheses

### Execution Process

1. **Parsing**: Python reads and analyzes the code syntax
2. **Interpretation**: Code is executed line by line
3. **Output**: The print function displays the string
4. **Result**: "Hello, World!" appears on your screen!

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `SyntaxError: invalid syntax` | Missing quotes around string | Add quotes: `print("Hello")` |
| `NameError: name 'Print' is not defined` | Wrong capitalization | Use lowercase: `print()` |
| `python3: command not found` | Python not installed | Install with: `sudo apt-get install python3` |
| `ModuleNotFoundError` | Wrong filename | Ensure file ends with `.py` |

### Bonus Knowledge

- **Python History**: Created by Guido van Rossum in 1991
- **Why "Hello, World!"?**: Tradition started with Brian Kernighan in 1978
- **Python Philosophy**: Readable, simple, and powerful
- **File extensions**: `.py` for Python source files

---

 **Congratulations! You've written your first Python program!** 

*Keep moving forward - next up: Variables!*
