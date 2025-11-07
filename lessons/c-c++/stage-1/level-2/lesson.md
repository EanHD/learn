# Level 2: Variables and Basic Types in C

> **LESSON NOTE:** This lesson file is **read-only**. Write your code in `main.c` in the right window.

## Stage 1: Working with Variables

### Learning Goals

- Declare and initialize variables in C
- Understand basic data types (`int`, `float`, `char`)
- Use `printf()` with format specifiers
- Perform simple arithmetic

---

### Your Task

Create `main.c` with this code:

```c
#include <stdio.h>

int main() {
    // Integer variables
    int age = 25;
    int year = 2025;

    // Floating point
    float height = 5.9;
    float price = 19.99;

    // Character
    char grade = 'A';

    // Print them all
    printf("Age: %d\n", age);
    printf("Year: %d\n", year);
    printf("Height: %.1f feet\n", height);
    printf("Price: $%.2f\n", price);
    printf("Grade: %c\n", grade);

    // Basic arithmetic
    int sum = age + 5;
    printf("In 5 years you'll be: %d\n", sum);

    return 0;
}
```

### Compile and Run

```
gcc main.c -o main
./main
```

---

### Format Specifiers

- `%d` - Integer (int)
- `%f` - Float (default 6 decimal places)
- `%.2f` - Float with 2 decimal places
- `%c` - Single character
- `%s` - String (we'll learn later)

---

### Try This

1. Create variables for your name's length (int) and favorite number (float)
2. Calculate and print: `age * 2`
3. Try printing a float with `%d` - what happens?
4. Change the grade to your actual grade

---

### Common Mistakes

- Forgetting semicolons `;`
- Using wrong format specifier (crashes or garbage output)
- Not initializing variables before use
- Using `=` (assignment) instead of `==` (comparison)

---

**Next: User input with scanf()!**

---

## ANSWER KEY (No cheating until you've tried!)

### Solution

```c
#include <stdio.h>

int main() {
    // Integer variables
    int age = 25;
    int year = 2025;

    // Floating point
    float height = 5.9;
    float price = 19.99;

    // Character
    char grade = 'A';

    // Print them all
    printf("Age: %d\n", age);
    printf("Year: %d\n", year);
    printf("Height: %.1f feet\n", height);
    printf("Price: $%.2f\n", price);
    printf("Grade: %c\n", grade);

    // Basic arithmetic
    int sum = age + 5;
    printf("In 5 years you'll be: %d\n", sum);

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
