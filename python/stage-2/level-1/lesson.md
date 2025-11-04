# Level 1: Basic Pseudocode Translation

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 2: Pseudocode to Code

### Today's Mission

Now that you know the basics, it's time to think like a programmer! You'll take pseudocode (plain English instructions) and translate it into real Python code. This is where programming logic comes to life.

---

### Learning Goals

- Understand how pseudocode maps to real code
- Learn to translate plain English into Python syntax
- Practice reading and implementing logic from specifications
- Build confidence in independent coding

---

### Your Task

Here's some pseudocode that describes a simple program:

```
START
    print "Welcome to the program!"
    print "This is my first real program"
    print "I'm learning to code!"
END
```

**Your mission**: Translate this pseudocode into Python code.

Hints:

- Each `print` instruction becomes a `print()` function call
- Text to print goes inside quotation marks
- Each statement should be on its own line

---

### How to Compile and Run

1. **Open your terminal**
2. **Navigate to your workspace folder**:

    ```bash
    cd ~/.local/share/learn/workspaces/python/stage-2/level-1
    ```

3. **Edit main.py** with your translated code
4. **Run your program**:

    ```bash
    python3 main.py
    ```

**Expected output:**

```
Welcome to the program!
This is my first real program
I'm learning to code!
```

---

### Success Checklist

- [ ] Created three `print()` statements
- [ ] Each print statement has the correct message
- [ ] Program runs without errors
- [ ] Output matches expected output exactly
- [ ] All text is in quotation marks

---

### What's Different About Stage 2?

**Stage 1 (Copying):** Code was provided, you typed it
**Stage 2 (Pseudocode):** Logic is described, you write the code

This teaches you to:

- Read specifications
- Understand requirements
- Make decisions about syntax
- Build code from descriptions

---

### Pro Tips

1. **Read the pseudocode twice** - Once to understand, once to code
2. **Output matters** - Your output must match exactly
3. **Syntax is strict** - `Print` vs `print`, `"text"` vs `'text'` matters
4. **Test often** - Run after each change

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Solution

```python
print("Welcome to the program!")
print("This is my first real program")
print("I'm learning to code!")
```

### Explanation

Each line of pseudocode translates directly:

| Pseudocode | Python | Meaning |
|------------|--------|---------|
| `print "text"` | `print("text")` | Call print function with string argument |
| Text in instruction | Text in quotes | Strings must be quoted in Python |
| Each instruction | Each line | One statement per line |

### Key Concepts

**1. Functions in Python**

- `print()` is a **built-in function**
- Functions take **arguments** inside parentheses
- Arguments are the data passed to the function

**2. Strings**

- Text must be enclosed in quotes (single `'` or double `"`)
- Python treats them as string literals
- Both are equivalent: `"hello"` = `'hello'`

**3. Pseudocode to Code Mapping**

```
Pseudocode:  print "message"
Code:        print("message")
                   ↑        ↑
                Syntax to use in real Python
```

### Common Mistakes & Solutions

| Mistake | Problem | Solution |
|---------|---------|----------|
| `print"text"` | Missing parentheses | Add `()` - it's `print("text")` |
| `print(text)` | Missing quotes | Add quotes - it's `print("text")` |
| `Print("text")` | Capital P | Python is case-sensitive: use `print` |
| Output has extra symbols | Copy/paste issues | Type manually from the lesson |

### Next Steps

You've now:

- ✓ Understood pseudocode
- ✓ Translated to Python
- ✓ Run your code

**Pattern Recognition**: Notice how each pseudocode line became one Python line. This pattern holds for more complex programs too!

---

**Great job! You're thinking like a programmer now!**

*Next up: Variables - storing and using data!*
