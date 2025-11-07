# Level 1: Hello World in Pure C

> **LESSON NOTE:** This lesson file is **read-only**. Write your code in `main.c` in the right window.

## Stage 1: Your First C Program

### Learning Goals

- Write your first C program
- Understand basic C structure
- Learn compilation and execution
- Use `printf()` for output

---

### Your Task

Create a file called `main.c` and type this code:

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

### How to Compile and Run

```
gcc main.c -o main
./main
```

**Expected Output:**
```
Hello, World!
```

---

### Code Explanation

- `#include <stdio.h>` - Includes Standard Input/Output library
- `int main()` - Main function where program starts
- `printf()` - Function to print text (from stdio.h)
- `"Hello, World!\n"` - String to print (`\n` = newline)
- `return 0;` - Exit successfully

---

### Try This

1. Change the message to "Hello, C!"
2. Add another `printf()` line with your name
3. Try removing `\n` and see what happens

---

### Success Checklist

- [ ] File named `main.c` created
- [ ] Code compiles without errors
- [ ] Program runs and prints message
- [ ] You understand each line

---

**Next: Variables and data types!**

---

## ANSWER KEY (No cheating until you've tried!)

### Solution

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

### Explanation

This solution demonstrates the key concepts from this lesson:

1. **Basic Structure**: The program follows the standard structure for c
2. **Output**: The code produces the expected output
3. **Syntax**: Pay attention to the syntax details - they're important!

### Success Criteria

- [ ] Code runs without errors
- [ ] Output matches expected result
- [ ] You understand what each line does

---

**Great job! You've completed this lesson!**
