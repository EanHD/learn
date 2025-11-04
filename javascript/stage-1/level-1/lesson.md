# Level 1: Hello World

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Welcome to your first step into JavaScript programming! Today, you'll learn how to create your very first JavaScript program. Don't worry about understanding everything yet - just focus on getting the code typed correctly and watching it work!

---

### Learning Goals

- Understand the basic structure of a JavaScript program
- Learn how to execute JavaScript code
- See your first program output "Hello, World!"
- Get comfortable with your text editor
- Learn about Node.js execution

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `hello.js`**

```javascript
console.log("Hello, World!");
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
   node hello.js
   ```

**Expected output:**
```
Hello, World!
```

---

### Success Checklist

- [ ] Created a file named `hello.js`
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw "Hello, World!" printed on screen
- [ ] Understood the basic console output

---

### What Happened?

You just created a real JavaScript program! Here's what each part does:

- `console.log()` - A function that prints text to the console (similar to printf in other languages)
- `"Hello, World!"` - The string literal that we want to print
- `()` - Parentheses contain the argument passed to the function
- `;` - Statement terminator (optional in JavaScript but good practice)

JavaScript is the language of the web, but can also be run server-side using Node.js!

---

### Try This (Optional Challenges)

If you're feeling brave, try these small changes:

1. Change the message to "Hello, JavaScript Programming!"
2. Add another `console.log()` line with your name
3. Try with different punctuation or emojis: `"Hello, World! 😊"`

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```javascript
console.log("Hello, World!");
```
- **`console`** = Built-in object that provides access to the browser's debugging console (or Node.js terminal)
- **`.`** = Property accessor - accesses the log function inside console object
- **`log`** = Method (function) that prints messages to the console
- **`()`** = Function call operator - executes the function
- **`"Hello, World!"`** = String argument passed to the log function
- **`;`** = Statement terminator - optional in JavaScript but good practice

### JavaScript Execution Environments

There are two main ways to run JavaScript:

1. **Browser Environment**: Runs in web browsers (client-side)
2. **Node.js Environment**: Runs on servers/computers (server-side)

Today's lesson uses Node.js, which allows us to run JavaScript outside the browser.

### Program Execution Process

1. **Parse**: JavaScript engine reads and parses the code for syntax errors
2. **Compile**: Code is compiled to optimized machine code
3. **Execute**: The code runs, executing each statement in order
4. **Output**: Results are displayed in the console

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `node: command not found` | Node.js not installed | Install Node.js from nodejs.org |
| `SyntaxError` | Missing quotes, comma, or brace | Check syntax carefully |
| `ReferenceError` | Using undefined variable | Check variable names |
| `TypeError` | Using wrong type of value | Verify data types match usage |

### Bonus Knowledge

- **JavaScript History**: Created by Brendan Eich in 1995 at Netscape (in just 10 days!)
- **Why \"Hello, World!\"?**: Tradition started with Brian Kernighan in 1978 (in C programming)
- **What does Node.js stand for?**: Server-side JavaScript runtime environment
- **File extensions**: `.js` for JavaScript files
- **JavaScript vs Java**: Despite similar names, they are very different languages

---

 **Congratulations! You've written your first JavaScript program!** 

*Keep moving forward - next up: Variables!*