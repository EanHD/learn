# Level 5: Conditionals and Decision Making

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Welcome to the power of decision-making in programming! Today you'll learn how to make your programs smart - able to check conditions and take different actions based on those conditions. This is where programs start thinking and responding intelligently!

---

### Learning Goals

- [ ] Master if, if-else, and if-else-if statements
- [ ] Learn comparison operators (==, !=, <, >, <=, >=)
- [ ] Understand logical operators (&&, ||, !)
- [ ] Practice nested conditionals
- [ ] Learn the switch statement for multiple choices
- [ ] Create programs that respond differently to different situations

---

### Your Task

**Copy the following code into a new file called `conditionals.c`**

```c
# include <stdio.h>

int main() {
    // Variables for testing
    int age;
    int score;
    char grade;
    float temperature;
    int day_of_week;
    float account_balance;
    bool is_student;
    bool has_discount_code;
    
    std::cout << "=== Intelligent Decision Making Program ===\n\n");
    
    // 1. Simple if statement
    std::cout << "--- Age Verification ---\n");
    std::cout << "Enter your age: ");
    scanf("%d", &age);
    
    if (age >= 18) {
        std::cout << " You are an adult! Welcome!\n");
        std::cout << "You can vote, sign contracts, and drive (if licensed).\n");
    }
    
    if (age < 18) {
        std::cout << " You are a minor! Stay in school!\n");
        std::cout << "Focus on learning and growing!\n");
    }
    
    // 2. If-else statement
    std::cout << "\n--- Score Evaluation ---\n");
    std::cout << "Enter your test score (0-100): ");
    scanf("%d", &score);
    
    if (score >= 60) {
        std::cout << " Congratulations! You passed!\n");
    } else {
        std::cout << " You didn't pass. Study more and try again!\n");
    }
    
    // 3. If-else-if chain
    std::cout << "\n--- Grade Calculator ---\n");
    std::cout << "Enter your numerical grade (0-100): ");
    scanf("%d", &score);
    
    if (score >= 90) {
        grade = 'A';
        std::cout << "Grade: A (Excellent! )\n");
    } else if (score >= 80) {
        grade = 'B';
        std::cout << "Grade: B (Good job! )\n");
    } else if (score >= 70) {
        grade = 'C';
        std::cout << "Grade: C (Satisfactory )\n");
    } else if (score >= 60) {
        grade = 'D';
        std::cout << "Grade: D (Needs improvement )\n");
    } else {
        grade = 'F';
        std::cout << "Grade: F (Failing - Please seek help )\n");
    }
    
    // 4. Logical operators (AND, OR, NOT)
    std::cout << "\n--- Temperature Alert System ---\n");
    std::cout << "Enter current temperature (°F): ");
    scanf("%f", &temperature);
    
    // AND operator - all conditions must be true
    if (temperature > 80 && temperature < 100) {
        std::cout << " Hot weather warning! Stay hydrated!\n");
    }
    
    // OR operator - at least one condition must be true
    if (temperature < 32 || temperature > 100) {
        std::cout << " Extreme temperature alert! Be careful!\n");
    }
    
    // NOT operator - reverses the condition
    bool is_freezing = temperature <= 32;
    if (!is_freezing) {
        std::cout << "No freezing conditions. Good!\n");
    }
    
    // 5. Nested conditionals
    std::cout << "\n--- Complex Eligibility Checker ---\n");
    std::cout << "Are you a student? (1 for yes, 0 for no): ");
    scanf("%d", &is_student);
    
    if (is_student) {
        std::cout << "Enter your GPA (0.0-4.0): ");
        float gpa;
        scanf("%f", &gpa);
        
        if (gpa >= 3.5) {
            std::cout << " Dean's List eligible!\n");
            if (gpa == 4.0) {
                std::cout << " Perfect GPA! Outstanding achievement!\n");
            }
        } else if (gpa >= 2.0) {
            std::cout << " Academic standing is good.\n");
        } else {
            std::cout << " Academic probation warning!\n");
        }
    } else {
        std::cout << "Student status not detected.\n");
    }
    
    // 6. Switch statement
    std::cout << "\n--- Day of the Week Analyzer ---\n");
    std::cout << "Enter day number (1-7): ");
    scanf("%d", &day_of_week);
    
    switch (day_of_week) {
        case 1:
            std::cout << "Monday: Start of the work week! \n");
            break;
        case 2:
            std::cout << "Tuesday: Productivity day! \n");
            break;
        case 3:
            std::cout << "Wednesday: Hump day! \n");
            break;
        case 4:
            std::cout << "Thursday: Almost there! \n");
            break;
        case 5:
            std::cout << "Friday: TGIF! \n");
            break;
        case 6:
            std::cout << "Saturday: Weekend fun! \n");
            break;
        case 7:
            std::cout << "Sunday: Rest & recharge! \n");
            break;
        default:
            std::cout << "Invalid day number! Please enter 1-7.\n");
            break;
    }
    
    // 7. Multiple conditions example
    std::cout << "\n--- Bank Account Status ---\n");
    std::cout << "Enter your account balance: $");
    scanf("%f", &account_balance);
    
    std::cout << "Do you have a student discount code? (1 for yes, 0 for no): ");
    scanf("%d", &has_discount_code);
    
    if (account_balance >= 10000) {
        std::cout << " VIP Status: Premium banking benefits!\n");
    } else if (account_balance >= 5000 && account_balance < 10000) {
        if (has_discount_code) {
            std::cout << " Gold Status with student discount: Good benefits!\n");
        } else {
            std::cout << " Gold Status: Standard benefits!\n");
        }
    } else if (account_balance >= 1000) {
        std::cout << " Regular account: Basic banking services.\n");
    } else if (account_balance >= 0) {
        std::cout << "ℹ Low balance: Consider monitoring your spending.\n");
    } else {
        std::cout << " OVERDRAFT WARNING: Negative balance!\n");
    }
    
    // 8. Conditional operator (ternary)
    std::cout << "\n--- Quick Decision Demo ---\n");
    int number;
    std::cout << "Enter a number: ");
    scanf("%d", &number);
    
    // Ternary operator: condition ? value_if_true : value_if_false
    char* message = (number > 0) ? "positive" : 
                   (number < 0) ? "negative" : "zero";
    
    std::cout << "The number is %s.\n", message);
    
    // 9. Complex real-world scenario
    std::cout << "\n--- Movie Ticket Calculator ---\n");
    int age_person;
    bool is_vip_member;
    int show_time; // 24-hour format
    
    std::cout << "Person's age: ");
    scanf("%d", &age_person);
    std::cout << "VIP member? (1 for yes, 0 for no): ");
    scanf("%d", &is_vip_member);
    std::cout << "Show time (24-hour, e.g., 14 for 2 PM): ");
    scanf("%d", &show_time);
    
    float ticket_price = 12.00; // Base price
    
    // Age discounts
    if (age_person < 12) {
        ticket_price *= 0.5; // 50% off for children
        std::cout << "Child discount applied (50%% off)\n");
    } else if (age_person >= 65) {
        ticket_price *= 0.7; // 30% off for seniors
        std::cout << "Senior discount applied (30%% off)\n");
    } else if (age_person >= 18 && age_person <= 25) {
        ticket_price *= 0.9; // 10% off for young adults
        std::cout << "Young adult discount applied (10%% off)\n");
    }
    
    // VIP member benefit
    if (is_vip_member) {
        ticket_price -= 3.00; // $3 off
        std::cout << "VIP member discount ($3.00 off)\n");
    }
    
    // Time-based pricing
    bool is_matinee = (show_time >= 10 && show_time < 17);
    bool is_late_show = (show_time >= 21 || show_time < 1);
    
    if (is_matinee) {
        ticket_price *= 0.8; // 20% off matinee
        std::cout << "Matinee discount applied (20%% off)\n");
    } else if (is_late_show) {
        ticket_price *= 1.1; // 10% extra for late shows
        std::cout << "Late show surcharge (10%% extra)\n");
    }
    
    std::cout << "Final ticket price: $%.2f\n", ticket_price);
    
    std::cout << "\n Program complete! You've mastered decision making!\n");
    
    return 0;
}
```bash

---

### How to Run

1. **Compile the code**:
   ```bash
   g++ conditionals.c -o conditionals
   ```bash
2. **Run your program**:
   ```bash
   ./conditionals
   ```bash
3. **Test different scenarios** with various inputs!

---

### Success Checklist

- [ ] Created a file named `conditionals.c`
- [ ] Copied all code correctly
- [ ] Compiled without errors
- [ ] Ran the program multiple times with different inputs
- [ ] Experienced all different types of conditional outcomes
- [ ] Observed how different conditions produce different results

---

### Key Conditional Concepts

1. **if statement** - Executes code only when condition is true
2. **if-else** - Choose between two options
3. **if-else-if** - Choose from multiple options in order
4. **switch** - Clean way to handle multiple specific values
5. **Logical operators** - Combine multiple conditions
6. **Nested conditionals** - Put if statements inside other if statements

---

### Try This (Optional Challenges)

1. Modify the temperature alerts to include more ranges
2. Add more cases to the switch statement (like 8 for "Sunday", but different meaning)
3. Create your own eligibility checker with multiple criteria
4. Experiment with removing `break;` statements from the switch case

---

## Quick Reference

### Comparison Operators
| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `age == 18` |
| `!=` | Not equal to | `age != 18` |
| `<` | Less than | `age < 18` |
| `>` | Greater than | `age > 18` |
| `<=` | Less than or equal | `age <= 18` |
| `>=` | Greater than or equal | `age >= 18` |

### Logical Operators
| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `&&` | AND (both true) | `age >= 18 && age < 65` | True for adults |
| `||` | OR (either true) | `age < 12 || age > 65` | True for children or seniors |
| `!` | NOT (reverses) | `!is_student` | True if not a student |

---

### Common Conditional Mistakes

1. **Using = instead of ==**
   ```c
   if (age = 18) { // WRONG - assigns 18 to age!
   if (age == 18) { // CORRECT - compares age to 18
   ```bash

2. **Forgotten semicolons**
   ```c
   if (x > 5); { // WRONG - semicolon ends the if!
   if (x > 5) {   // CORRECT
   ```bash

3. **Wrong operator for ranges**
   ```c
   if (12 < age < 18) // WRONG - doesn't work in C!
   if (age > 12 && age < 18) // CORRECT
   ```bash

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

#### 1. Simple if Statements

```c
if (age >= 18) {
    std::cout << " You are an adult! Welcome!\n");
}

if (age < 18) {
    std::cout << " You are a minor! Stay in school!\n");
}
```bash

**Key Points:**
- [ ] Each `if` statement stands alone
- [ ] Both conditions are checked independently
- [ ] Braces `{}` group the code that belongs to each if

**Best Practice:** Always use braces, even for single-line conditions:
```c
if (x > 5)
    std::cout << "Hello"); // Bad - confusing

if (x > 5) {
    std::cout << "Hello"); // Good - clear structure
}
```bash

#### 2. if-else Structure

```c
if (score >= 60) {
    std::cout << " Congratulations! You passed!\n");
} else {
    std::cout << " You didn't pass. Study more and try again!\n");
}
```bash

**Understanding Control Flow:**
- [ ] If condition is true → execute first block, skip the else
- [ ] If condition is false → skip first block, execute else block
- [ ] Exactly one block will always execute

#### 3. if-else-if Chain

```c
if (score >= 90) {
    grade = 'A';
    std::cout << "Grade: A (Excellent! )\n");
} else if (score >= 80) {
    grade = 'B';
    std::cout << "Grade: B (Good job! )\n");
} else if (score >= 70) {
    grade = 'C';
    std::cout << "Grade: C (Satisfactory )\n");
}
```bash

**Important Concept:** Conditions are checked in order, so:
- [ ] Score 85 → fails `>= 90`, passes `>= 80` → Grade: B
- [ ] Once a condition matches, the rest are skipped
- [ ] Final `else` catches everything that didn't match

#### 4. Logical Operators

```c
if (temperature > 80 && temperature < 100) {
    std::cout << " Hot weather warning! Stay hydrated!\n");
}
```bash

**AND (&&) Truth Table:**
| A | B | A && B |
|---|---|--------|
| true | true | true |
| true | false | false |
| false | true | false |
| false | false | false |

**OR (||) Truth Table:**
| A | B | A \|\| B |
|---|---|----------|
| true | true | true |
| true | false | true |
| false | true | true |
| false | false | false |

**NOT (!) Truth Table:**
| A | !A |
|---|-----|
| true | false |
| false | true |

#### 5. Nested Conditionals

```c
if (is_student) {
    std::cout << "Enter your GPA (0.0-4.0): ");
    float gpa;
    scanf("%f", &gpa);
    
    if (gpa >= 3.5) {
        std::cout << " Dean's List eligible!\n");
        if (gpa == 4.0) {
            std::cout << " Perfect GPA! Outstanding achievement!\n");
        }
    }
}
```bash

**Why Nest?** Sometimes you need to check conditions only when previous conditions are met.

#### 6. Switch Statement

```c
switch (day_of_week) {
    case 1:
        std::cout << "Monday: Start of the work week! \n");
        break;
    case 2:
        std::cout << "Tuesday: Productivity day! \n");
        break;
    default:
        std::cout << "Invalid day number! Please enter 1-7.\n");
        break;
}
```bash

**Critical Concept - The `break` statement:**
- [ ] Without `break`, execution "falls through" to the next case
- [ ] This is actually sometimes useful, but can be a source of bugs

**Fall-through example (useful):**
```c
case 1:
case 2:
case 3:
    std::cout << "You chose a low number\n");
    break;
case 4:
case 5:
    std::cout << "You chose a medium number\n");
    break;
```bash

#### 7. Ternary Operator

```c
char* message = (number > 0) ? "positive" : 
               (number < 0) ? "negative" : "zero";
```bash

**Understanding Nested Ternary:**
```c
// Equivalent to:
if (number > 0) {
    message = "positive";
} else {
    if (number < 0) {
        message = "negative";
    } else {
        message = "zero";
    }
}
```bash

### Advanced Conditional Concepts

#### Short-Circuit Evaluation

```c
if (x != 0 && y > 10) {
    // Both conditions must be true
}

// If x is 0, the second condition (y > 10) is never evaluated
// This prevents division by zero in cases like:
if (x != 0 && y / x > 10) {
    // Safe because y/x is only evaluated if x ≠ 0
}
```bash

#### De Morgan's Laws

**Original:** `if (!is_student || !has_discount)`
**Equivalent:** `if (!(is_student && has_discount))`

These can sometimes make complex conditions more readable.

#### Boolean Logic Optimization

Instead of:
```c
if (age >= 0 && age <= 120) {
    // valid age
}
```bash

You could write:
```c
if (age >= 0 && age <= 120) { // This is actually the clearest way
    // Keep it simple and readable!
}
```bash

### Real-World Conditional Patterns

#### Input Validation

```c
bool validate_input(int value, int min, int max) {
    return value >= min && value <= max;
}

void get_number(int* value, const char* prompt, int min, int max) {
    do {
        std::cout << "%s (%d-%d): ", prompt, min, max);
        scanf("%d", value);
        
        if (!validate_input(*value, min, max)) {
            std::cout << "Invalid input! Try again.\n");
        }
    } while (!validate_input(*value, min, max));
}
```bash

#### State Machine Pattern

```c
typedef enum {
    STATE_MENU,
    STATE_PLAYING,
    STATE_PAUSED,
    STATE_GAME_OVER
} GameState;

void update_game(GameState* state, int input) {
    switch (*state) {
        case STATE_MENU:
            if (input == 1) *state = STATE_PLAYING;
            break;
        case STATE_PLAYING:
            if (input == 'p') *state = STATE_PAUSED;
            else if (input == 'q') *state = STATE_GAME_OVER;
            break;
        case STATE_PAUSED:
            if (input == 'r') *state = STATE_PLAYING;
            break;
        case STATE_GAME_OVER:
            if (input == 'r') *state = STATE_MENU;
            break;
    }
}
```bash

### Performance Considerations

#### Order of Conditions

```c
// Less efficient - checks expensive condition first
if (expensive_calculation() && simple_check()) {
    // ...
}

// More efficient - cheap check first, uses short-circuit
if (simple_check() && expensive_calculation()) {
    // ...
}
```bash

#### Switch vs if-else-if

For a long series of integer comparisons, `switch` is often more readable and potentially faster:

```c
// if-else-if version
if (day == 1) { /* Monday */ }
else if (day == 2) { /* Tuesday */ }
else if (day == 3) { /* Wednesday */ }
// ... more cases

// switch version (usually preferred)
switch (day) {
    case 1: /* Monday */ break;
    case 2: /* Tuesday */ break;
    case 3: /* Wednesday */ break;
    // ... more cases
}
```bash

### Debugging Conditionals

#### Common Debugging Techniques

```c
int age = 25;
std::cout << "Debug: age = %d\n", age);
std::cout << "Debug: age >= 18 is %s\n", age >= 18 ? "true" : "false");

if (age >= 18) {
    std::cout << "Debug: Entered adult branch\n");
    std::cout << " You are an adult! Welcome!\n");
}
```bash

#### Conditional Tracing

```c
if (condition1) {
    std::cout << "Step 1: condition1 was true\n");
    if (condition2) {
        std::cout << "Step 2: condition2 was true\n");
        // do something
    } else {
        std::cout << "Step 2: condition2 was false\n");
    }
} else {
    std::cout << "Step 1: condition1 was false\n");
}
```bash

---

 **Incredible! You now have the power to make intelligent decisions in your programs!** 

*Your programs can now think and respond like a real AI! Next up: Loops for repeated actions! *

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
