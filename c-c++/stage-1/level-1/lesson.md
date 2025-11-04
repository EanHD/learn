# Level 1: Hello World

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`main.cpp` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.

## Stage 1: Copying Code

### Today's Mission

Welcome to your first step into programming! Today, you'll learn how to create your very first C program. Don't worry about understanding everything yet - just focus on getting the code typed correctly and watching it work!

---

### Learning Goals

- Understand the basic structure of a C program
- Learn how to compile and run code
- See your first program output "Hello, World!"
- Get comfortable with your text editor

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `hello.c`**

```c
# include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

---

### How to Compile and Run

1. **Open your terminal** (or command prompt)
2. **Navigate to where you saved your file**:
   ```bash
   cd /path/to/your/folder
   ```
3. **Compile the code**:
   ```bash
   gcc hello.c -o hello
   ```
4. **Run your program**:
   ```bash
   ./hello
   ```

**Expected output:**
```
Hello, World!
```

---

### Success Checklist

- [ ] Created a file named `hello.c`
- [ ] Copied the code exactly as shown
- [ ] Compiled without errors
- [ ] Ran the program successfully
- [ ] Saw "Hello, World!" printed on screen

---

### What Happened?

You just created a real computer program! Here's what each part does:

- `#include <stdio.h>` - Tells C to include helpful tools for input/output
- `int main()` - The main function where every C program starts
- `printf(...)` - A function that prints text to the screen
- `"Hello, World!\n"` - The message to print (the `\n` creates a new line)
- `return 0;` - Tells the computer the program finished successfully

---

### Try This (Optional Challenges)

If you're feeling brave, try these small changes:

1. Change the message to "Hello, C Programming!"
2. Add another printf() line with your name
3. Remove the `\n` and see what happens

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```c
# include <stdio.h>
```
- **`#include`** = A preprocessor command that includes libraries
- **`<stdio.h>`** = Standard Input/Output library - gives us printf()
- **Purpose**: Lets us use functions like printf() for printing

```c
int main() {
```
- **`int`** = Return type - this function will return an integer
- **`main`** = Function name - every C program starts here
- **`()`** = Parameters (empty means no inputs needed)
- **`{`** = Opening brace - start of function body

```c
    printf("Hello, World!\n");
```
- **`printf`** = "print formatted" function from stdio.h
- **`"`** = String literal start/end
- **`\n`** = Escape sequence for newline (moves cursor to next line)
- **`;`** = Statement terminator - EVERY statement must end with this!

```c
    return 0;
}
```
- **`return 0`** = Returns 0 to indicate successful execution
- **`}`** = Closing brace - end of function body

### Compilation Process

1. **Preprocessing**: `#include` statements are processed
2. **Compilation**: Code is converted to machine-readable object files
3. **Linking**: Object files are linked to create executable
4. **Result**: Your `hello` program is ready to run!

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `fatal error: stdio.h: No such file` | GCC not installed | Install with: `sudo apt-get install gcc` (Ubuntu) |
| `undefined reference to printf` | Missing #include | Add `#include <stdio.h>` |
| `syntax error` | Missing semicolon or brace | Check every line has `;` and braces match |
| `Permission denied` | Can't execute | Run `chmod +x hello` |

### Bonus Knowledge

- **C Development Timeline**: Dennis Ritchie created C in 1972 at Bell Labs
- **Why "Hello, World!"?**: Tradition started with Brian Kernighan in 1978
- **What does GCC stand for?**: GNU Compiler Collection
- **File extensions**: `.c` for source, `.o` for object, no extension for Linux executables

---

 **Congratulations! You've written your first C program!** 

*Keep moving forward - next up: Variables!*