# Level 5: Conditionals and Decision Making

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Welcome to the power of decision-making in programming! Today you'll learn how to make your programs smart - able to check conditions and take different actions based on those conditions. This is where programs start thinking and responding intelligently!

---

### Learning Goals

- Master if, if-else, and if-else-if statements
- Learn comparison operators (==, !=, <, >, <=, >=)
- Understand logical operators (&&, ||, !)
- Practice nested conditionals
- Learn the switch statement for multiple choices
- Create programs that respond differently to different situations

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
    
    printf("=== Intelligent Decision Making Program ===\n\n");
    
    // 1. Simple if statement
    printf("--- Age Verification ---\n");
    printf("Enter your age: ");
    scanf("%d", &age);
    
    if (age >= 18) {
        printf(" You are an adult! Welcome!\n");
        printf("You can vote, sign contracts, and drive (if licensed).\n");
    }
    
    if (age < 18) {
        printf(" You are a minor! Stay in school!\n");
        printf("Focus on learning and growing!\n");
    }
    
    // 2. If-else statement
    printf("\n--- Score Evaluation ---\n");
    printf("Enter your test score (0-100): ");
    scanf("%d", &score);
    
    if (score >= 60) {
        printf(" Congratulations! You passed!\n");
    } else {
        printf(" You didn't pass. Study more and try again!\n");
    }
    
    // 3. If-else-if chain
    printf("\n--- Grade Calculator ---\n");
    printf("Enter your numerical grade (0-100): ");
    scanf("%d", &score);
    
    if (score >= 90) {
        grade = 'A';
        printf("Grade: A (Excellent! )\n");
    } else if (score >= 80) {
        grade = 'B';
        printf("Grade: B (Good job! )\n");
    } else if (score >= 70) {
        grade = 'C';
        printf("Grade: C (Satisfactory )\n");
    } else if (score >= 60) {
        grade = 'D';
        printf("Grade: D (Needs improvement )\n");
    } else {
        grade = 'F';
        printf("Grade: F (Failing - Please seek help )\n");
    }
    
    // 4. Logical operators (AND, OR, NOT)
    printf("\n--- Temperature Alert System ---\n");
    printf("Enter current temperature (°F): ");
    scanf("%f", &temperature);
    
    // AND operator - all conditions must be true
    if (temperature > 80 && temperature < 100) {
        printf(" Hot weather warning! Stay hydrated!\n");
    }
    
    // OR operator - at least one condition must be true
    if (temperature < 32 || temperature > 100) {
        printf(" Extreme temperature alert! Be careful!\n");
    }
    
    // NOT operator - reverses the condition
    bool is_freezing = temperature <= 32;
    if (!is_freezing) {
        printf("No freezing conditions. Good!\n");
    }
    
    // 5. Nested conditionals
    printf("\n--- Complex Eligibility Checker ---\n");
    printf("Are you a student? (1 for yes, 0 for no): ");
    scanf("%d", &is_student);
    
    if (is_student) {
        printf("Enter your GPA (0.0-4.0): ");
        float gpa;
        scanf("%f", &gpa);
        
        if (gpa >= 3.5) {
            printf(" Dean's List eligible!\n");
            if (gpa == 4.0) {
                printf(" Perfect GPA! Outstanding achievement!\n");
            }
        } else if (gpa >= 2.0) {
            printf(" Academic standing is good.\n");
        } else {
            printf(" Academic probation warning!\n");
        }
    } else {
        printf("Student status not detected.\n");
    }
    
    // 6. Switch statement
    printf("\n--- Day of the Week Analyzer ---\n");
    printf("Enter day number (1-7): ");
    scanf("%d", &day_of_week);
    
    switch (day_of_week) {
        case 1:
            printf("Monday: Start of the work week! \n");
            break;
        case 2:
            printf("Tuesday: Productivity day! \n");
            break;
        case 3:
            printf("Wednesday: Hump day! \n");
            break;
        case 4:
            printf("Thursday: Almost there! \n");
            break;
        case 5:
            printf("Friday: TGIF! \n");
            break;
        case 6:
            printf("Saturday: Weekend fun! \n");
            break;
        case 7:
            printf("Sunday: Rest & recharge! \n");
            break;
        default:
            printf("Invalid day number! Please enter 1-7.\n");
            break;
    }
    
    // 7. Multiple conditions example
    printf("\n--- Bank Account Status ---\n");
    printf("Enter your account balance: $");
    scanf("%f", &account_balance);
    
    printf("Do you have a student discount code? (1 for yes, 0 for no): ");
    scanf("%d", &has_discount_code);
    
    if (account_balance >= 10000) {
        printf(" VIP Status: Premium banking benefits!\n");
    } else if (account_balance >= 5000 && account_balance < 10000) {
        if (has_discount_code) {
            printf(" Gold Status with student discount: Good benefits!\n");
        } else {
            printf(" Gold Status: Standard benefits!\n");
        }
    } else if (account_balance >= 1000) {
        printf(" Regular account: Basic banking services.\n");
    } else if (account_balance >= 0) {
        printf("ℹ Low balance: Consider monitoring your spending.\n");
    } else {
        printf(" OVERDRAFT WARNING: Negative balance!\n");
    }
    
    // 8. Conditional operator (ternary)
    printf("\n--- Quick Decision Demo ---\n");
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);
    
    // Ternary operator: condition ? value_if_true : value_if_false
    char* message = (number > 0) ? "positive" : 
                   (number < 0) ? "negative" : "zero";
    
    printf("The number is %s.\n", message);
    
    // 9. Complex real-world scenario
    printf("\n--- Movie Ticket Calculator ---\n");
    int age_person;
    bool is_vip_member;
    int show_time; // 24-hour format
    
    printf("Person's age: ");
    scanf("%d", &age_person);
    printf("VIP member? (1 for yes, 0 for no): ");
    scanf("%d", &is_vip_member);
    printf("Show time (24-hour, e.g., 14 for 2 PM): ");
    scanf("%d", &show_time);
    
    float ticket_price = 12.00; // Base price
    
    // Age discounts
    if (age_person < 12) {
        ticket_price *= 0.5; // 50% off for children
        printf("Child discount applied (50%% off)\n");
    } else if (age_person >= 65) {
        ticket_price *= 0.7; // 30% off for seniors
        printf("Senior discount applied (30%% off)\n");
    } else if (age_person >= 18 && age_person <= 25) {
        ticket_price *= 0.9; // 10% off for young adults
        printf("Young adult discount applied (10%% off)\n");
    }
    
    // VIP member benefit
    if (is_vip_member) {
        ticket_price -= 3.00; // $3 off
        printf("VIP member discount ($3.00 off)\n");
    }
    
    // Time-based pricing
    bool is_matinee = (show_time >= 10 && show_time < 17);
    bool is_late_show = (show_time >= 21 || show_time < 1);
    
    if (is_matinee) {
        ticket_price *= 0.8; // 20% off matinee
        printf("Matinee discount applied (20%% off)\n");
    } else if (is_late_show) {
        ticket_price *= 1.1; // 10% extra for late shows
        printf("Late show surcharge (10%% extra)\n");
    }
    
    printf("Final ticket price: $%.2f\n", ticket_price);
    
    printf("\n Program complete! You've mastered decision making!\n");
    
    return 0;
}
```

---

### How to Compile and Run

1. **Compile the code**:
   ```bash
   gcc conditionals.c -o conditionals
   ```
2. **Run your program**:
   ```bash
   ./conditionals
   ```
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
   ```

2. **Forgotten semicolons**
   ```c
   if (x > 5); { // WRONG - semicolon ends the if!
   if (x > 5) {   // CORRECT
   ```

3. **Wrong operator for ranges**
   ```c
   if (12 < age < 18) // WRONG - doesn't work in C!
   if (age > 12 && age < 18) // CORRECT
   ```

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

#### 1. Simple if Statements

```c
if (age >= 18) {
    printf(" You are an adult! Welcome!\n");
}

if (age < 18) {
    printf(" You are a minor! Stay in school!\n");
}
```

**Key Points:**
- Each `if` statement stands alone
- Both conditions are checked independently
- Braces `{}` group the code that belongs to each if

**Best Practice:** Always use braces, even for single-line conditions:
```c
if (x > 5)
    printf("Hello"); // Bad - confusing

if (x > 5) {
    printf("Hello"); // Good - clear structure
}
```

#### 2. if-else Structure

```c
if (score >= 60) {
    printf(" Congratulations! You passed!\n");
} else {
    printf(" You didn't pass. Study more and try again!\n");
}
```

**Understanding Control Flow:**
- If condition is true → execute first block, skip the else
- If condition is false → skip first block, execute else block
- Exactly one block will always execute

#### 3. if-else-if Chain

```c
if (score >= 90) {
    grade = 'A';
    printf("Grade: A (Excellent! )\n");
} else if (score >= 80) {
    grade = 'B';
    printf("Grade: B (Good job! )\n");
} else if (score >= 70) {
    grade = 'C';
    printf("Grade: C (Satisfactory )\n");
}
```

**Important Concept:** Conditions are checked in order, so:
- Score 85 → fails `>= 90`, passes `>= 80` → Grade: B
- Once a condition matches, the rest are skipped
- Final `else` catches everything that didn't match

#### 4. Logical Operators

```c
if (temperature > 80 && temperature < 100) {
    printf(" Hot weather warning! Stay hydrated!\n");
}
```

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
    printf("Enter your GPA (0.0-4.0): ");
    float gpa;
    scanf("%f", &gpa);
    
    if (gpa >= 3.5) {
        printf(" Dean's List eligible!\n");
        if (gpa == 4.0) {
            printf(" Perfect GPA! Outstanding achievement!\n");
        }
    }
}
```

**Why Nest?** Sometimes you need to check conditions only when previous conditions are met.

#### 6. Switch Statement

```c
switch (day_of_week) {
    case 1:
        printf("Monday: Start of the work week! \n");
        break;
    case 2:
        printf("Tuesday: Productivity day! \n");
        break;
    default:
        printf("Invalid day number! Please enter 1-7.\n");
        break;
}
```

**Critical Concept - The `break` statement:**
- Without `break`, execution "falls through" to the next case
- This is actually sometimes useful, but can be a source of bugs

**Fall-through example (useful):**
```c
case 1:
case 2:
case 3:
    printf("You chose a low number\n");
    break;
case 4:
case 5:
    printf("You chose a medium number\n");
    break;
```

#### 7. Ternary Operator

```c
char* message = (number > 0) ? "positive" : 
               (number < 0) ? "negative" : "zero";
```

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
```

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
```

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
```

You could write:
```c
if (age >= 0 && age <= 120) { // This is actually the clearest way
    // Keep it simple and readable!
}
```

### Real-World Conditional Patterns

#### Input Validation

```c
bool validate_input(int value, int min, int max) {
    return value >= min && value <= max;
}

void get_number(int* value, const char* prompt, int min, int max) {
    do {
        printf("%s (%d-%d): ", prompt, min, max);
        scanf("%d", value);
        
        if (!validate_input(*value, min, max)) {
            printf("Invalid input! Try again.\n");
        }
    } while (!validate_input(*value, min, max));
}
```

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
```

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
```

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
```

### Debugging Conditionals

#### Common Debugging Techniques

```c
int age = 25;
printf("Debug: age = %d\n", age);
printf("Debug: age >= 18 is %s\n", age >= 18 ? "true" : "false");

if (age >= 18) {
    printf("Debug: Entered adult branch\n");
    printf(" You are an adult! Welcome!\n");
}
```

#### Conditional Tracing

```c
if (condition1) {
    printf("Step 1: condition1 was true\n");
    if (condition2) {
        printf("Step 2: condition2 was true\n");
        // do something
    } else {
        printf("Step 2: condition2 was false\n");
    }
} else {
    printf("Step 1: condition1 was false\n");
}
```

---

 **Incredible! You now have the power to make intelligent decisions in your programs!** 

*Your programs can now think and respond like a real AI! Next up: Loops for repeated actions! *