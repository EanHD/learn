# Level 1: Hello World

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 1: Copying Code

### Today's Mission

Welcome to Dart! Today, you'll create your first Dart program. Dart is a modern language built by Google, used for Flutter app development and server applications.

### Learning Goals

- Understand Dart program structure
- Learn how to run Dart code
- Create your first output
- Get comfortable with Dart syntax

### Your Task

Copy the following code EXACTLY as shown into a new file called `hello.dart`:

```
void main() {
  print("Hello, World!");
}
```

### How to Execute

```
dart hello.dart
```

Expected output:

```
Hello, World!
```

### Success Checklist

- [ ] Created a file named `hello.dart`
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw "Hello, World!" printed

---

**Dart is compiled to native code and JavaScript. Great for cross-platform development!**

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### The Complete Solution

```
void main() {
  print("Hello, World!");
}
```

### Code Breakdown

```c
# include <stdio.h>
```
- **`#include`** = A preprocessor command that includes libraries
- **`<stdio.h>`** = Standard Input/Output library - gives us printf()
- **Purpose**: Lets us use functions like printf() for printing

```c
main function {
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

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `fatal error: stdio.h: No such file` | GCC not installed | Install with: `sudo apt-get install gcc` (Ubuntu) |
| `undefined reference to printf` | Missing import/include statement | Add `import/include statement <stdio.h>` |
| `syntax error` | Missing semicolon or brace | Check every line has `;` and braces match |
| `Permission denied` | Can't execute | Run `chmod +x hello` |


### Bonus Knowledge

- **C Development Timeline**: Dennis Ritchie created C in 1972 at Bell Labs
- **Why "Hello, World!"?**: Tradition started with Brian Kernighan in 1978
- **What does GCC stand for?**: GNU Compiler Collection
- **File extensions**: `.c` for source, `.o` for object, no extension for Linux executables

---

**Great work! Ready for the next lesson?**

---

**Congratulations! Keep coding!**


### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim


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

```
void main() {
    print("Hello, World!");
}

```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard dart conventions with proper imports and main function
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
