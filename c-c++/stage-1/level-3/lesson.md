# Level 3: Basic Math Operations

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Time to become a mathematical wizard! Today you'll learn how C can be your calculator. We'll explore addition, subtraction, multiplication, division, and even some special operations that make programming powerful.

---

### Learning Goals

- [ ] Master all basic arithmetic operators in C
- [ ] Understand operator precedence (order of operations)
- [ ] Learn about the modulus operator (%)
- [ ] Practice using variables in mathematical expressions
- [ ] Discover the difference between integer and floating-point division

---

### Your Task

**Copy the following code into a new file called `math_ops.c`**

```c
# include <stdio.h>

int main() {
    // Basic variables for our calculations
    int a = 10;
    int b = 3;
    float x = 10.0;
    float y = 3.0;
    
    std::cout << "=== Basic Arithmetic Operations ===\n");
    std::cout << "Working with a = %d, b = %d\n", a, b);
    std::cout << "Working with x = %.1f, y = %.1f\n\n", x, y);
    
    // Addition
    int sum_int = a + b;
    float sum_float = x + y;
    std::cout << "Addition:\n");
    std::cout << "  %d + %d = %d\n", a, b, sum_int);
    std::cout << "  %.1f + %.1f = %.1f\n", x, y, sum_float);
    std::cout << "\n");
    
    // Subtraction
    int diff_int = a - b;
    float diff_float = x - y;
    std::cout << "Subtraction:\n");
    std::cout << "  %d - %d = %d\n", a, b, diff_int);
    std::cout << "  %.1f - %.1f = %.1f\n", x, y, diff_float);
    std::cout << "\n");
    
    // Multiplication
    int prod_int = a * b;
    float prod_float = x * y;
    std::cout << "Multiplication:\n");
    std::cout << "  %d * %d = %d\n", a, b, prod_int);
    std::cout << "  %.1f * %.1f = %.1f\n", x, y, prod_float);
    std::cout << "\n");
    
    // Division (THE TRICKY ONE!)
    std::cout << "Division:\n");
    std::cout << "  Integer division: %d / %d = %d\n", a, b, a / b);
    std::cout << "  Float division: %.1f / %.1f = %.6f\n", x, y, x / y);
    std::cout << "\n");
    
    // Modulus (remainder of division)
    int remainder = a % b;
    std::cout << "Modulus Operator:\n");
    std::cout << "  %d %% %d = %d (remainder)\n", a, b, remainder);
    std::cout << "\n");
    
    // Combined operations
    std::cout << "=== Combined Operations ===\n");
    int result1 = a + b * 2;
    int result2 = (a + b) * 2;
    std::cout << "  a + b * 2 = %d (without parentheses)\n", result1);
    std::cout << "  (a + b) * 2 = %d (with parentheses)\n", result2);
    std::cout << "\n");
    
    // More complex expressions
    std::cout << "=== Complex Expressions ===\n");
    int score = 85;
    int bonus = 15;
    int penalty = 5;
    
    int final_score = score + bonus - penalty * 2 + 10 / 3;
    std::cout << "Base score: %d\n", score);
    std::cout << "Final score: %d\n", final_score);
    std::cout << "\n");
    
    // Real-world example: Shopping
    std::cout << "=== Shopping Example ===\n");
    int apple_price = 2;
    int oranges = 3;
    int bananas = 5;
    float tax_rate = 0.08;
    
    int subtotal = apple_price * 5 + oranges * 3 + bananas * 1;
    float tax = subtotal * tax_rate;
    float total = subtotal + tax;
    
    std::cout << "  Apples (5): $%d\n", apple_price * 5);
    std::cout << "  Oranges (3): $%d\n", oranges * 3);
    std::cout << "  Bananas (5): $%d\n", bananas);
    std::cout << "  Subtotal: $%d\n", subtotal);
    std::cout << "  Tax (8%%): $%.2f\n", tax);
    std::cout << "  Total: $%.2f\n", total);
    
    return 0;
}
```bash

---

### How to Run

1. **Compile the code**:
   ```bash
   g++ math_ops.c -o math_ops
   ```bash
2. **Run your program**:
   ```bash
   ./math_ops
   ```bash

**Expected output:**
```bash
=== Basic Arithmetic Operations ===
Working with a = 10, b = 3
Working with x = 10.0, y = 3.0

Addition:
  10 + 3 = 13
  10.0 + 3.0 = 13.0

Subtraction:
  10 - 3 = 7
  10.0 - 3.0 = 7.0

Multiplication:
  10 * 3 = 30
  10.0 * 3.0 = 30.0

Division:
  Integer division: 10 / 3 = 3
  Float division: 10.0 / 3.0 = 3.333333

Modulus Operator:
  10 % 3 = 1 (remainder)

=== Combined Operations ===
  a + b * 2 = 16 (without parentheses)
  (a + b) * 2 = 26 (with parentheses)

=== Complex Expressions ===
Base score: 85
Final score: 91

=== Shopping Example ===
  Apples (5): $10
  Oranges (3): $9
  Bananas (5): $5
  Subtotal: $24
  Tax (8%): $1.92
  Total: $25.92
```bash

---

### Success Checklist

- [ ] Created a file named `math_ops.c`
- [ ] Copied all code correctly
- [ ] Compiled without errors
- [ ] Ran the program and saw all operations work
- [ ] Understood the difference between integer and float division
- [ ] Noticed how parentheses change the result

---

### Key Insights

Did you notice these important concepts?

1. **Integer Division**: `10 / 3 = 3` (decimal gets chopped off!)
2. **Float Division**: `10.0 / 3.0 = 3.333333` (kept the decimals)
3. **Order of Operations**: Multiplication happens before addition
4. **Modulus**: `%` gives the remainder (10 ÷ 3 = 3 remainder 1)

---

### Try This (Optional Challenges)

1. Change the variables to different numbers and see what happens
2. Add division by zero (what happens? why?)
3. Try making the tax rate a different value
4. Create your own shopping cart with different items

---

## Quick Reference

| Operator | What it does | Example | Result |
|----------|--------------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 3` | `1` (int) or `1.666` (float) |
| `%` | Modulus (remainder) | `5 % 3` | `2` |
| `()` | Parentheses | `5 * (2 + 3)` | `25` |

### Order of Operations (PEMDAS)

1. **P**arentheses `()`
2. **E**xponents (not covered yet)
3. **M**ultiplication `*` and **D**ivision `/` and **M**odulus `%` (left to right)
4. **A**ddition `+` and **S**ubtraction `-` (left to right)

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (Don't look until you've tried!)

### Code Breakdown

```c
# include <stdio.h>

int main() {
    // Basic variables for our calculations
    int a = 10;
    int b = 3;
    float x = 10.0;
    float y = 3.0;
```bash
We create both integer and float versions of the same numbers to show the difference in how C handles division.

```c
    // Addition
    int sum_int = a + b;
    float sum_float = x + y;
    std::cout << "Addition:\n");
    std::cout << "  %d + %d = %d\n", a, b, sum_int);
    std::cout << "  %.1f + %.1f = %.1f\n", x, y, sum_float);
```c
**Important**: We store results in variables before printing. This helps with debugging and makes code more readable.

```c
    // Division (THE TRICKY ONE!)
    std::cout << "Division:\n");
    std::cout << "  Integer division: %d / %d = %d\n", a, b, a / b);
    std::cout << "  Float division: %.1f / %.1f = %.6f\n", x, y, x / y);
```c
**Critical Concept**: Integer division truncates (chops off) decimals. Float division keeps them. This is a common source of bugs for beginners!

```c
    // Modulus (remainder of division)
    int remainder = a % b;
    std::cout << "Modulus Operator:\n");
    std::cout << "  %d %% %d = %d (remainder)\n", a, b, remainder);
```c
**Why `%%`?** Because `%` is a special character in printf, we need to escape it with another `%` to print a literal `%` symbol.

```c
    // Combined operations
    std::cout << "=== Combined Operations ===\n");
    int result1 = a + b * 2;
    int result2 = (a + b) * 2;
    std::cout << "  a + b * 2 = %d (without parentheses)\n", result1);
    std::cout << "  (a + b) * 2 = %d (with parentheses)\n", result2);
```bash
This demonstrates operator precedence:
- [ ] `result1 = 10 + 3 * 2 = 10 + 6 = 16` (multiplication first)
- [ ] `result2 = (10 + 3) * 2 = 13 * 2 = 26` (parentheses first)

### Deep Dive: Integer vs Float Division

```c
int i = 10 / 3;    // i = 3 (integer division)
float f = 10.0 / 3.0;  // f = 3.333333 (float division)

int i2 = 10 / 3.0;  // i2 = ???
```bash

**What happens in the third case?** `10` (int) gets promoted to float, division happens as float, then result gets converted back to int = 3!

### Understanding the Modulus Operator

The modulus operator (`%`) gives the remainder after integer division:

| Dividend | Divisor | Quotient | Remainder | `%` result |
|----------|---------|----------|-----------|------------|
| 10 | 3 | 3 | 1 | 1 |
| 15 | 5 | 3 | 0 | 0 |
| 7 | 4 | 1 | 3 | 3 |
| 8 | 2 | 4 | 0 | 0 |

**Practical uses of modulus:**
- [ ] Check if a number is even: `if (number % 2 == 0)`
- [ ] Extract the last digit: `last_digit = number % 10`
- [ ] Create cycles: `counter = (counter + 1) % 4` (cycles through 0,1,2,3)

### Type Promotion and Conversion Rules

When mixing types in expressions, C automatically promotes to the "larger" type:

```bash
char → int → long → float → double
```bash

**Example:**
```c
int a = 10;
float b = 3.0;
float result = a / b;  // a gets promoted to float
```bash

### Advanced Mathematical Functions

For more complex math, include `<math.h>`:

```c
# include <math.h>
# include <stdio.h>

int main() {
    double angle = 45.0;
    double radians = angle * 3.14159 / 180.0;
    
    std::cout << "sin(45°) = %.4f\n", sin(radians));
    std::cout << "cos(45°) = %.4f\n", cos(radians));
    std::cout << "sqrt(16) = %.0f\n", sqrt(16));
    std::cout << "pow(2, 8) = %.0f\n", pow(2, 8));
    
    return 0;
}
```bash

### Common Math Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Integer overflow | Result too big for int | Use `long long` or `double` |
| Division by zero | Dividing by 0 | Always check denominator ≠ 0 |
| Wrong result | Integer division when you want decimals | Use float literals (10.0 instead of 10) |
| Precision loss | Float has limited precision | Use `double` for more precision |

### Real-World Math Applications

1. **Temperature Conversion**: `fahrenheit = celsius * 9.0/5.0 + 32`
2. **Distance Calculation**: `distance = sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))`
3. **Financial Calculations**: `interest = principal * rate * time`
4. **Grade Averages**: `average = (grade1 + grade2 + grade3) / 3.0`

### Performance Tip

C's order of operations is designed for efficiency:

```c
// Slower:
result = value * 2 / 8;  // Multiplication first, then division

// Faster:
result = value / 4;      // Direct division by pre-calculated value
```bash

### Mental Math Challenge

Before running this code, try to predict the output:

```c
int x = 10, y = 3, z = 20;
int result = x / y + z % y * (x - y);

// Step 1: x / y = 10 / 3 = 3 (integer division)
// Step 2: z % y = 20 % 3 = 2
// Step 3: (x - y) = 10 - 3 = 7
// Step 4: z % y * (x - y) = 2 * 7 = 14
// Step 5: x / y + (result from step 4) = 3 + 14 = 17
```bash

**Answer**: 17

---

 **Fantastic! You've mastered mathematical operations in C!** 

*You're ready for the next level - making your programs interactive!*

---

### BONUS CHALLENGE

Create a simple calculator that:
- [ ] Asks for two numbers
- [ ] Performs all operations on them
- [ ] Shows the results in a nicely formatted output

*Hint: You'll need to learn about user input first... next lesson! *

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
