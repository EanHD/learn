# Level 2: Variables

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Welcome to the world of variables! Today you'll learn how to store and use data in your programs. Variables are like boxes where you can store information - numbers, text, and more!

---

### Learning Goals

- [ ] Understand what variables are and why we need them
- [ ] Learn basic data types (int, float, char)
- [ ] Practice declaring and initializing variables
- [ ] Learn how to display variable values

---

### Your Task

**Copy the following code into a new file called `variables.c`**

```c
# include <stdio.h>

int main() {
    // Integer variables (whole numbers)
    int age = 25;
    int height = 175;
    int score = 100;
    
    // Floating point variables (decimal numbers)
    float temperature = 98.6;
    float price = 29.99;
    float weight = 150.5;
    
    // Character variables (single letters)
    char grade = 'A';
    char initial = 'J';
    char symbol = '$';
    
    // Print all the variables
    std::cout << "=== My Profile ===\n");
    std::cout << "Age: %d years old\n", age);
    std::cout << "Height: %d cm\n", height);
    std::cout << "Score: %d points\n", score);
    std::cout << "\n");
    
    std::cout << "=== Measurements ===\n");
    std::cout << "Temperature: %.1f degrees\n", temperature);
    std::cout << "Price: $%.2f\n", price);
    std::cout << "Weight: %.1f lbs\n", weight);
    std::cout << "\n");
    
    std::cout << "=== Symbols ===\n");
    std::cout << "Grade: %c\n", grade);
    std::cout << "Initial: %c\n", initial);
    std::cout << "Symbol: %c\n", symbol);
    
    return 0;
}
```bash

---

### How to Run

1. **Compile the code**:
   ```bash
   g++ variables.c -o variables
   ```bash
2. **Run your program**:
   ```bash
   ./variables
   ```bash

**Expected output:**
```bash
=== My Profile ===
Age: 25 years old
Height: 175 cm
Score: 100 points

=== Measurements ===
Temperature: 98.6 degrees
Price: $29.99
Weight: 150.5 lbs

=== Symbols ===
Grade: A
Initial: J
Symbol: $
```bash

---

### Success Checklist

- [ ] Created a file named `variables.c`
- [ ] Copied the code exactly as shown
- [ ] Compiled without errors
- [ ] Ran the program successfully
- [ ] Saw all variable values printed with correct formatting

---

### What Those Symbols Mean!

In the `printf()` statements, you saw some weird symbols:

- [ ] **`%d`** = decimal integer (for `int` variables)
- [ ] **`%f`** = floating point number (for `float` variables)
- [ ] **`%c`** = character (for `char` variables)
- [ ] **`%.1f`** = float with 1 decimal place
- [ ] **`%.2f`** = float with 2 decimal places

---

### Try This (Optional Challenges)

1. Change all the variable values to your own information
2. Add new variables for your name (hint: use a string!)
3. Try changing the precision in the printf statements
4. What happens if you use wrong format specifiers?

---

### Pro Tip

Variables can be changed! Try adding these lines before `return 0;`:
```c
age = age + 1;
std::cout << "Next year I'll be %d\n", age);
```bash

---

## Quick Reference

| Data Type | What it holds | Examples | Format Specifier |
|-----------|---------------|----------|------------------|
| `int` | Whole numbers | 42, -17, 0 | `%d` |
| `float` | Decimal numbers | 3.14, -2.5, 100.0 | `%f`, `%.1f`, `%.2f` |
| `char` | Single characters | 'A', 'b', '7', '$' | `%c` |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```c
# include <stdio.h>
```c
- [ ] Includes the standard input/output library for printf function

```c
int main() {
```bash
- [ ] The starting point of our program

```c
    // Integer variables (whole numbers)
    int age = 25;
```bash
- [ ] **`//`** = Single-line comment (ignored by computer)
- [ ] **`int`** = Data type for whole numbers
- [ ] **`age`** = Variable name (follows naming rules)
- [ ] **`=`** = Assignment operator (stores value on right into variable on left)
- [ ] **`25`** = Initial value
- [ ] **`;`** = End of statement

```c
    // Floating point variables (decimal numbers)
    float temperature = 98.6;
```bash
- [ ] **`float`** = Data type for decimal numbers
- [ ] Can hold fractional values like 98.6, 3.14, -0.5

```c
    // Character variables (single letters)
    char grade = 'A';
```bash
- [ ] **`char`** = Data type for single characters
- [ ] **`'A'`** = Character literal (uses single quotes, not double!)
- [ ] Only holds ONE character at a time

```c
    std::cout << "Age: %d years old\n", age);
```bash
- [ ] **`%d`** = Placeholder for integer variable
- [ ] The `%d` gets replaced by the value of `age`
- [ ] Variables are passed to printf in the same order as placeholders

### Variable Naming Rules

 **Valid names**: `age`, `myAge`, `age1`, `student_score`
 **Invalid names**: `123age`, `my-age`, `int`, `age score`

**Rules to remember:**
1. Start with letter or underscore (_)
2. Use only letters, numbers, and underscores
3. Can't use reserved keywords (like `int`, `float`, `return`)
4. Case sensitive (age ≠ Age)

### Format Specifiers Deep Dive

| Specifier | Usage | Precision Example |
|-----------|-------|-------------------|
| `%d` | Basic integer | `std::cout << "Age: %d", age);` |
| `%5d` | Integer, 5 spaces wide, right-aligned | `std::cout << "Num: %5d", 42);` → `"Num:    42"` |
| `%05d` | Integer, 5 spaces, leading zeros | `std::cout << "Num: %05d", 42);` → `"Num: 00042"` |
| `%f` | Basic float (6 decimal places default) | `std::cout << "Val: %f", 3.14);` → `"Val: 3.140000"` |
| `%.2f` | Float, 2 decimal places | `std::cout << "$%.2f", 29.5);` → `"$29.50"` |
| `%10.2f` | Float, 10 chars wide, 2 decimals | `std::cout << "Val: %10.2f", 3.14);` → `"Val:       3.14"` |
| `%c` | Single character | `std::cout << "Grade: %c", 'A');` |

### Understanding Memory

Each variable takes up memory:

- [ ] **`char`** = 1 byte (enough for 1 character)
- [ ] **`int`** = Usually 4 bytes (can store: -2,147,483,648 to 2,147,483,647)
- [ ] **`float`** = Usually 4 bytes (can store: ~±3.4 × 10³⁸)

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `implicit declaration of function printf` | Missing `#include <iostream>` | Add the include at top |
| `format '%d' expects argument of type 'int'` | Wrong format specifier | Match specifier to variable type |
| `overflow` | Number too big for data type | Use larger type like `long` |
| `invalid initializer` | Wrong syntax for initialization | Check quotes, semicolons |

### Bonus Knowledge

- [ ] **Why called "variables"?** Because their values can vary (change) during program execution
- [ ] **Constants**: If you want a value that cannot change, use `const int AGE = 25;`
- [ ] **ASCII Table**: Characters are stored as numbers (A=65, B=66, etc.)
- [ ] **Memory Address**: Every variable has an address: `std::cout << "%p", &age);` shows where it's stored

### Advanced Challenge (For the Brave!)

Try this modified version:

```c
// Let's do some calculations!
int current_year = 2024;
int birth_year = 2000;
int calculated_age = current_year - birth_year;

std::cout << "Born in %d, now it's %d\n", birth_year, current_year);
std::cout << "Calculated age: %d years old\n", calculated_age);

// What's my grade average?
int math_grade = 90;
int science_grade = 85;
float average = (math_grade + science_grade) / 2.0f;
std::cout << "Grade average: %.1f\n", average);
```bash

---

 **Excellent work! You now understand variables - the foundation of all programming!** 

*Ready for the next challenge? Let's do some math with our variables!*

### Additional Content

Understand the key concepts:

- [ ] Review each function
- [ ] Understand the flow
- [ ] Learn the patterns used


### Code Review

Key functions and their purpose:

- [ ] Main function: Entry point
- [ ] Helper functions: Support logic


<div style="page-break-after: always;"></div>

## Answer Key

### Complete Solution

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard C++ conventions with proper imports and main function
2. **Output**: Uses std::cout to print messages to the console
3. **Standard Library**: Includes iostream for input/output operations
4. **Return Value**: Returns 0 to indicate successful execution
5. **Best Practices**: Code is readable and uses C++ idioms

### Testing Your Solution

1. **Compile**: `g++ hello.cpp -o hello`
2. **Run**: `./hello`
3. **Expected Output**: `Hello, World!`

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `command not found: g++` | Compiler not installed | `sudo apt install g++` (Ubuntu) |
| `undefined reference to main` | Missing main function | Ensure `int main()` exists |
| `error: unknown type name 'cout'` | Missing iostream | Add `#include <iostream>` |

### Tips for Learning

- C++ is a superset of C with additional features
- `std::cout` is the C++ way to print (replaces `printf`)
- `std::endl` adds a newline and flushes the buffer
- The `std::` prefix means these are from the "standard" namespace
