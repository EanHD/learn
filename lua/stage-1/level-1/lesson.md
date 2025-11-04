# Level 1: Hello World

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Welcome to your first step into Lua programming! Today, you'll learn how to create your very first Lua program. Don't worry about understanding everything yet - just focus on getting the code typed correctly and watching it work!

---

### Learning Goals

- Understand the basic structure of a Lua program
- Learn how to execute Lua code
- See your first program output "Hello, World!"
- Get comfortable with your text editor
- Learn about Lua execution environment

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `hello.lua`**

```lua
print("Hello, World!")
```

---

### How to Execute

1. **Open your terminal** (or command prompt)
2. **Navigate to where you saved your file**:
   ```bash
   cd /path/to/your/folder
   ```
3. **Run your program**:
   ```bash
   lua hello.lua
   ```

**Expected output:**
```
Hello, World!
```

---

### Success Checklist

- [ ] Created a file named `hello.lua`
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw "Hello, World!" printed on screen
- [ ] Understood the basic console output

---

### What Happened?

You just created a real Lua program! Here's what each part does:

- `print()` - A function that prints text to the console
- `"Hello, World!"` - The string literal that we want to print
- `()` - Parentheses contain the argument passed to the function
- No statement terminator required in Lua (unlike other languages)

Lua is a lightweight, embeddable scripting language designed to be simple and efficient!

---

### Try This (Optional Challenges)

If you're feeling brave, try these small changes:

1. Change the message to "Hello, Lua Programming!"
2. Add another `print()` line with your name
3. Try with different punctuation or emojis: `"Hello, World! 😊"`

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```lua
print("Hello, World!")
```
- **`print`** = Built-in function that outputs text to the console
- **`()`** = Function call operator - executes the function with arguments
- **`"Hello, World!"`** = String argument passed to the print function
- **No semicolon** = Lua doesn't require statement terminators

### Lua Execution Environment

Lua can be run in several ways:

1. **Script mode** (what we're doing): `lua hello.lua`
2. **Interactive mode**: `lua` (then type commands directly)
3. **Embeddable**: Can be integrated into other applications

### Program Execution Process

1. **Parse**: Lua interpreter reads and parses the code for syntax errors
2. **Execute**: The code runs, executing each statement in order
3. **Output**: Results are displayed in the console

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `lua: command not found` | Lua not installed | Install Lua from lua.org or package manager |
| `attempt to call a nil value` | Function name typo | Check function spelling (case-sensitive) |
| `malformed number` | Numeric syntax error | Check number format |
| `unfinished string` | Missing closing quote | Ensure all strings have matching quotes |

### Bonus Knowledge

- **Lua History**: Created in 1993 by Roberto Ierusalimschy, Waldemar Celes, and Luiz Henrique de Figueiredo at PUC-Rio (Brazil)
- **Lua Name**: Means "moon" in Portuguese
- **Why "Hello, World!"?**: Tradition started with Brian Kernighan in 1978 (in C programming)
- **File extensions**: `.lua` for Lua files
- **Embeddability**: Lua is designed to be embedded in C/C++ applications

---

 **Congratulations! You've written your first Lua program!** 

*Keep moving forward - next up: Variables!*