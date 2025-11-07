# Level 1: Basic Pseudocode Translation

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Welcome to Stage 2!  You've mastered copying code - now it's time to think like a programmer! Today you'll learn to translate written instructions (pseudocode) into working C programs. This is where programming becomes creative problem-solving!

---

### Learning Goals

- [ ] Understand what pseudocode is and why it's useful
- [ ] Learn to read and interpret algorithmic descriptions
- [ ] Practice translating simple algorithms into C code
- [ ] Develop logical thinking for programming
- [ ] Create working programs from written instructions

---

### What is Pseudocode?

**Pseudocode** is a way to write programming logic in plain English (or your native language) before writing actual code. It's like writing a recipe or instructions for a task.

**Example:**
```
Algorithm: Make a sandwich
1. Get bread from pantry
2. Get peanut butter from fridge
3. Get jelly from pantry
4. Spread peanut butter on one bread slice
5. Spread jelly on the other bread slice
6. Put slices together
7. Enjoy your sandwich!
```

This is much easier to understand than trying to write code first!

---

### Your Task

**For each pseudocode algorithm below, translate it into working C code.**

---

## Algorithm 1: Greeting Program

**Pseudocode:**
```
Algorithm: Display Personal Greeting
1. Display "Hello! What's your name?" to the user
2. Get the user's name from input
3. Display "Nice to meet you, " followed by the user's name
4. Display "Welcome to programming!"
```

**Your Task:** Create a C program that follows these exact steps.

---

## Algorithm 2: Simple Calculator

**Pseudocode:**
```
Algorithm: Add Two Numbers
1. Ask user for first number
2. Get first number from user
3. Ask user for second number
4. Get second number from user
5. Calculate sum of the two numbers
6. Display "The sum is: " followed by the sum
```

**Your Task:** Create a C program that implements this calculator.

---

## Algorithm 3: Age Calculator

**Pseudocode:**
```
Algorithm: Calculate Age in Days
1. Display "Enter your age in years: "
2. Get age in years from user
3. Calculate days = age × 365
4. Display "You are approximately " + days + " days old"
5. Display "That's a lot of days! "
```

**Your Task:** Create a program that calculates approximate age in days.

---

## Algorithm 4: Temperature Converter

**Pseudocode:**
```
Algorithm: Celsius to Fahrenheit Converter
1. Display "Enter temperature in Celsius: "
2. Get temperature in Celsius from user
3. Calculate Fahrenheit = (Celsius × 9/5) + 32
4. Display the Celsius temperature
5. Display "°C = "
6. Display the Fahrenheit temperature
7. Display "°F"
```

**Your Task:** Create a temperature conversion program.

---

## Algorithm 5: Rectangle Area Calculator

**Pseudocode:**
```
Algorithm: Calculate Rectangle Area
1. Display "Rectangle Area Calculator"
2. Display "Enter length: "
3. Get length from user
4. Display "Enter width: "
5. Get width from user
6. Calculate area = length × width
7. Calculate perimeter = 2 × (length + width)
8. Display "Area: " + area
9. Display "Perimeter: " + perimeter
```

**Your Task:** Create a program that calculates both area and perimeter.

---

## Algorithm 6: Simple Interest Calculator

**Pseudocode:**
```
Algorithm: Calculate Simple Interest
1. Display "Simple Interest Calculator"
2. Display "Enter principal amount: $"
3. Get principal from user
4. Display "Enter interest rate (%): "
5. Get rate from user
6. Display "Enter time in years: "
7. Get time from user
8. Calculate interest = (principal × rate × time) ÷ 100
9. Calculate total = principal + interest
10. Display "Principal: $" + principal
11. Display "Interest: $" + interest
12. Display "Total: $" + total
```

**Your Task:** Implement the complete interest calculation.

---

### How to Approach Each Algorithm

**Step-by-Step Process:**

1. **Read Carefully**: Understand what the algorithm does
2. **Identify Inputs**: What information does the user provide?
3. **Identify Outputs**: What should the program display?
4. **Identify Calculations**: What math is needed?
5. **Plan the Code Structure**:
   - `#include <iostream>`
   - `int main() {`
   - Variable declarations
   - Input statements
   - Calculations
   - Output statements
   - `return 0;`
   - `}`

**Example Planning for Algorithm 1:**
- [ ] **Inputs**: User's name (string)
- [ ] **Outputs**: Greeting messages
- [ ] **No calculations needed**
- [ ] **Structure**: Simple input/output program

---

### Success Checklist

**For Each Algorithm:**
- [ ] Created a separate C file (e.g., `greeting.c`, `calculator.c`)
- [ ] Program compiles without errors
- [ ] Program runs and produces expected output
- [ ] Followed the pseudocode steps exactly
- [ ] Used appropriate variable names
- [ ] Included clear output messages

**Overall Progress:**
- [ ] Completed all 6 algorithms
- [ ] All programs work correctly
- [ ] Code is well-organized and readable

---

### Try This (Optional Challenges)

1. **Modify Algorithm 1**: Add a question about favorite color and respond to it
2. **Modify Algorithm 3**: Make the calculation more accurate (account for leap years)
3. **Combine Algorithms**: Create a program that does temperature conversion AND age calculation
4. **Add Validation**: Check if user enters valid numbers (no negative ages, etc.)

---

## Pseudocode Best Practices

### Good Pseudocode
```
Algorithm: Process User Data
1. Get user's name
2. Get user's age
3. If age >= 18 then
   Display "Adult user"
Else
   Display "Minor user"
4. Display "Data processed"
```

### Bad Pseudocode (Too Vague)
```
Algorithm: Do stuff
1. Get things
2. Calculate something
3. Show results
```

### Good Pseudocode (Clear and Specific)
```
Algorithm: Calculate BMI
1. Display "BMI Calculator"
2. Display "Enter weight in kg: "
3. Get weight from user
4. Display "Enter height in meters: "
5. Get height from user
6. Calculate BMI = weight ÷ (height × height)
7. Display "Your BMI is: " + BMI
```

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Greeting Program

```c
# include <stdio.h>

int main() {
    char name[50];
    
    std::cout << "Hello! What's your name? ");
    scanf("%s", name);
    
    std::cout << "Nice to meet you, %s\n", name);
    std::cout << "Welcome to programming!\n");
    
    return 0;
}
```

**Key Concepts:**
- [ ] `char name[50];` - String variable to store the name
- [ ] `scanf("%s", name);` - Read string input
- [ ] `std::cout << "Nice to meet you, %s\n", name);` - Display with variable

---

### Algorithm 2: Simple Calculator

```c
# include <stdio.h>

int main() {
    int num1, num2, sum;
    
    std::cout << "Enter first number: ");
    scanf("%d", &num1);
    
    std::cout << "Enter second number: ");
    scanf("%d", &num2);
    
    sum = num1 + num2;
    
    std::cout << "The sum is: %d\n", sum);
    
    return 0;
}
```

**Key Concepts:**
- [ ] Multiple variables: `num1`, `num2`, `sum`
- [ ] Arithmetic operation: `sum = num1 + num2;`
- [ ] Clear input prompts for each value

---

### Algorithm 3: Age Calculator

```c
# include <stdio.h>

int main() {
    int age_years, age_days;
    
    std::cout << "Enter your age in years: ");
    scanf("%d", &age_years);
    
    age_days = age_years * 365;
    
    std::cout << "You are approximately %d days old\n", age_days);
    std::cout << "That's a lot of days! \n");
    
    return 0;
}
```

**Key Concepts:**
- [ ] Simple multiplication: `age_days = age_years * 365;`
- [ ] Clear variable naming: `age_years`, `age_days`
- [ ] Fun output message with emoji

---

### Algorithm 4: Temperature Converter

```c
# include <stdio.h>

int main() {
    float celsius, fahrenheit;
    
    std::cout << "Enter temperature in Celsius: ");
    scanf("%f", &celsius);
    
    fahrenheit = (celsius * 9.0/5.0) + 32;
    
    std::cout << "%.1f°C = %.1f°F\n", celsius, fahrenheit);
    
    return 0;
}
```

**Key Concepts:**
- [ ] `float` variables for decimal temperatures
- [ ] Complex formula: `(celsius * 9.0/5.0) + 32`
- [ ] Formatted output with degree symbols: `%.1f°C`

---

### Algorithm 5: Rectangle Area Calculator

```c
# include <stdio.h>

int main() {
    float length, width, area, perimeter;
    
    std::cout << "Rectangle Area Calculator\n");
    std::cout << "Enter length: ");
    scanf("%f", &length);
    
    std::cout << "Enter width: ");
    scanf("%f", &width);
    
    area = length * width;
    perimeter = 2 * (length + width);
    
    std::cout << "Area: %.2f\n", area);
    std::cout << "Perimeter: %.2f\n", perimeter);
    
    return 0;
}
```

**Key Concepts:**
- [ ] Multiple calculations: area and perimeter
- [ ] Parentheses for order: `2 * (length + width)`
- [ ] Descriptive output labels

---

### Algorithm 6: Simple Interest Calculator

```c
# include <stdio.h>

int main() {
    float principal, rate, time, interest, total;
    
    std::cout << "Simple Interest Calculator\n");
    std::cout << "Enter principal amount: $");
    scanf("%f", &principal);
    
    std::cout << "Enter interest rate (%%): ");
    scanf("%f", &rate);
    
    std::cout << "Enter time in years: ");
    scanf("%f", &time);
    
    interest = (principal * rate * time) / 100;
    total = principal + interest;
    
    std::cout << "Principal: $%.2f\n", principal);
    std::cout << "Interest: $%.2f\n", interest);
    std::cout << "Total: $%.2f\n", total);
    
    return 0;
}
```

**Key Concepts:**
- [ ] Complex formula: `(principal * rate * time) / 100`
- [ ] Dollar sign formatting: `$%.2f`
- [ ] Multiple output lines with clear labels

---

### Common Translation Patterns

| Pseudocode Pattern | C Code Equivalent |
|-------------------|-------------------|
| `Display "message"` | `std::cout << "message\n");` |
| `Get variable from user` | `scanf("%d", &variable);` |
| `Calculate result = a + b` | `result = a + b;` |
| `If condition then` | `if (condition) {` |
| `Display variable` | `std::cout << "%d\n", variable);` |

### Debugging Tips

**"Program doesn't compile":**
- [ ] Check semicolons at end of statements
- [ ] Verify variable declarations
- [ ] Ensure proper braces `{ }`

**"Wrong output":**
- [ ] Check variable names match (case-sensitive)
- [ ] Verify scanf format specifiers (`%d` for int, `%f` for float)
- [ ] Check mathematical formulas

**"Program crashes":**
- [ ] Make sure variables are declared before use
- [ ] Check array sizes for strings
- [ ] Verify scanf has `&` for non-string variables

### Variable Naming Best Practices

**Good Names:**
- [ ] `user_age` (clear what it stores)
- [ ] `temperature_celsius` (descriptive)
- [ ] `rectangle_area` (specific purpose)

**Bad Names:**
- [ ] `x` (too vague)
- [ ] `temp` (unclear what kind of temperature)
- [ ] `var1` (meaningless)

### Input/Output Patterns

**Getting Numbers:**
```c
int age;
std::cout << "Enter age: ");
scanf("%d", &age);
```

**Getting Decimals:**
```c
float price;
std::cout << "Enter price: $");
scanf("%f", &price);
```

**Getting Text:**
```c
char name[50];
std::cout << "Enter name: ");
scanf("%s", name);
```

**Displaying Results:**
```c
std::cout << "Result: %d\n", result);
std::cout << "Price: $%.2f\n", price);
std::cout << "Hello, %s!\n", name);
```

---

 **Congratulations! You've translated your first pseudocode algorithms into working C programs!** 

*This is a major milestone - you're now thinking like a programmer! Next up: Variables in pseudocode! *

### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim


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

```
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
