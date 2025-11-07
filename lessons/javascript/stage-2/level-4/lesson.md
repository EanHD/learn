# Level 4: Input/Output Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Welcome to Level 4! Today we're focusing on input/output operations in pseudocode. You'll learn to translate pseudocode that handles user interaction into working JavaScript code, and understand how to properly manage input validation and output formatting.

---

### Learning Goals

- Understand how to represent input/output operations in pseudocode
- Learn to handle user input in various formats
- Practice input validation and error handling
- Create programs with clear user interaction
- Develop awareness of proper output formatting

---

### Input/Output Operations in Pseudocode

Input/Output expressions in pseudocode follow these patterns:

**Input operations:**
```
INPUT user_name
INPUT age
SET email TO INPUT("Enter your email: ")
SET number TO INPUT_INTEGER("Enter a number: ")
SET choice TO INPUT_CHOICE("A, B, C")
```

**Output operations:**
```
OUTPUT "Hello, " + user_name
OUTPUT "Your age is: " + age
DISPLAY message
PRINT formatted_output
```

**Combined I/O:**
```
OUTPUT "Enter your name: "
INPUT name
IF name IS EMPTY THEN
   OUTPUT "Name cannot be empty!"
ELSE
   OUTPUT "Hello, " + name + "!"
ENDIF
```

---

### Your Task

**For each pseudocode algorithm below, translate it into working JavaScript code. Pay special attention to input validation and output formatting.**

---


### How to Run

1. **Run the code**:
   ```
   node hello.js
   ```

**Expected output:**
```
Hello, World!
```

## Algorithm 1: Simple Input Validation

**Pseudocode:**
```
Algorithm: Validate User Age
1. OUTPUT "Please enter your age: "
2. INPUT age
3. IF age < 0 OR age > 150 THEN
   4. OUTPUT "Invalid age! Please enter an age between 0 and 150."
   5. STOP
5. ENDIF
6. OUTPUT "Thank you! You are " + age + " years old."
```

**Your Task:** Create a JavaScript program that validates user age input.

---

## Algorithm 2: User Information Form

**Pseudocode:**
```
Algorithm: Collect User Information
1. OUTPUT "User Information Form"
2. OUTPUT "==================="
3. OUTPUT "Enter your name: "
4. INPUT name
5. OUTPUT "Enter your age: "
6. INPUT age
7. OUTPUT "Enter your email: "
8. INPUT email
9. OUTPUT "Enter your favorite color: "
10. INPUT color
11. OUTPUT ""
12. OUTPUT "SUMMARY:"
13. OUTPUT "Name: " + name
14. OUTPUT "Age: " + age
15. OUTPUT "Email: " + email
16. OUTPUT "Favorite Color: " + color
17. OUTPUT "Form submitted successfully!"
```

**Your Task:** Create a JavaScript program that collects and displays user information.

---

## Algorithm 3: Number Validation Loop

**Pseudocode:**
```
Algorithm: Get Valid Number
1. SET valid_input TO FALSE
2. WHILE NOT valid_input DO
   3. OUTPUT "Enter a positive number: "
   4. INPUT number
   5. IF number > 0 THEN
      6. SET valid_input TO TRUE
      7. OUTPUT "Valid number entered: " + number
   8. ELSE
      9. OUTPUT "Invalid! Please enter a positive number."
   10. ENDIF
11. ENDWHILE
```

**Your Task:** Create a JavaScript program that keeps asking for input until valid.

---

## Algorithm 4: Grade Calculator with Input

**Pseudocode:**
```
Algorithm: Calculate Letter Grade
1. OUTPUT "Grade Calculator"
2. OUTPUT "==============="
3. OUTPUT "Enter assignment score: "
4. INPUT score
5. OUTPUT "Enter total possible points: "
6. INPUT total_points
7. SET percentage TO (score / total_points) * 100
8. SET letter_grade TO "F"
9. IF percentage >= 90 THEN SET letter_grade TO "A"
10. ELSE IF percentage >= 80 THEN SET letter_grade TO "B"
11. ELSE IF percentage >= 70 THEN SET letter_grade TO "C"
12. ELSE IF percentage >= 60 THEN SET letter_grade TO "D"
13. ENDIF
14. OUTPUT "Score: " + score + "/" + total_points
15. OUTPUT "Percentage: " + percentage + "%"
16. OUTPUT "Letter Grade: " + letter_grade
```

**Your Task:** Create a JavaScript program that calculates grades from user input.

---

## Algorithm 5: Temperature Converter with Menu

**Pseudocode:**
```
Algorithm: Temperature Converter Menu
1. OUTPUT "Temperature Converter"
2. OUTPUT "1. Celsius to Fahrenheit"
3. OUTPUT "2. Fahrenheit to Celsius"
4. OUTPUT "Choose an option (1 or 2): "
5. INPUT choice
6. IF choice = 1 THEN
   7. OUTPUT "Enter temperature in Celsius: "
   8. INPUT celsius
   9. SET fahrenheit TO celsius * 9 / 5 + 32
   10. OUTPUT celsius + "°C = " + fahrenheit + "°F"
11. ELSE IF choice = 2 THEN
   12. OUTPUT "Enter temperature in Fahrenheit: "
   13. INPUT fahrenheit
   14. SET celsius TO (fahrenheit - 32) * 5 / 9
   15. OUTPUT fahrenheit + "°F = " + celsius + "°C"
12. ELSE
   16. OUTPUT "Invalid choice! Please enter 1 or 2."
17. ENDIF
```

**Your Task:** Create a JavaScript program with a menu-based temperature converter.

---

## Algorithm 6: Input Validation with Multiple Fields

**Pseudocode:**
```
Algorithm: Validate Contact Information
1. SET is_valid TO TRUE
2. OUTPUT "Contact Information Form"
3. OUTPUT "Enter your full name: "
4. INPUT name
5. IF LENGTH(name) < 2 THEN
   6. OUTPUT "Name must be at least 2 characters long."
   7. SET is_valid TO FALSE
8. ENDIF
9. OUTPUT "Enter your phone number: "
10. INPUT phone
11. IF LENGTH(phone) < 10 THEN
   12. OUTPUT "Phone number must be at least 10 digits."
   13. SET is_valid TO FALSE
14. ENDIF
15. OUTPUT "Enter your email: "
16. INPUT email
17. IF email DOES NOT CONTAIN "@" THEN
   18. OUTPUT "Email must contain '@' symbol."
   19. SET is_valid TO FALSE
20. ENDIF
21. IF is_valid THEN
   22. OUTPUT "Form submitted successfully!"
23. ELSE
   24. OUTPUT "Form has errors. Please fix and resubmit."
25. ENDIF
```

**Your Task:** Create a JavaScript program that validates multiple input fields.

---

## Algorithm 7: Calculator with User Interaction

**Pseudocode:**
```
Algorithm: Interactive Calculator
1. OUTPUT "Simple Calculator"
2. OUTPUT "Enter first number: "
3. INPUT num1
4. OUTPUT "Enter operator (+, -, *, /): "
5. INPUT operator
6. OUTPUT "Enter second number: "
7. INPUT num2
8. SET result TO 0
9. SET has_error TO FALSE
10. IF operator = "+" THEN SET result TO num1 + num2
11. ELSE IF operator = "-" THEN SET result TO num1 - num2
12. ELSE IF operator = "*" THEN SET result TO num1 * num2
13. ELSE IF operator = "/" THEN
   14. IF num2 = 0 THEN
   15. OUTPUT "Error: Division by zero!"
   16. SET has_error TO TRUE
   17. ELSE
   18. SET result TO num1 / num2
   19. ENDIF
20. ELSE
   21. OUTPUT "Error: Invalid operator!"
   22. SET has_error TO TRUE
23. ENDIF
24. IF NOT has_error THEN
   25. OUTPUT num1 + " " + operator + " " + num2 + " = " + result
26. ENDIF
```

**Your Task:** Create a JavaScript program that simulates a basic calculator with error handling.

---

### Key Concepts for Input/Output Operations

**Input Handling:**
- In JavaScript (Node.js), use `readline-sync` for synchronous input
- Validate input immediately after receiving it
- Provide clear error messages for invalid input

**Output Formatting:**
- Use consistent formatting for all output messages
- Add spacing and headers to make output readable
- Format numbers appropriately for display

**User Experience:**
- Provide clear prompts for all input requests
- Validate input types (numeric vs text inputs)
- Offer helpful error messages for invalid entries

---

### Success Checklist

**For Each Algorithm:**
- [ ] Input operations correctly implemented
- [ ] Output formatting matches pseudocode
- [ ] Input validation properly implemented
- [ ] Error handling included where appropriate
- [ ] Program runs without errors

**Overall Progress:**
- [ ] Completed all 7 algorithms
- [ ] All programs work correctly
- [ ] User interaction is clear and intuitive

---

### Try This (Optional Challenges)

1. **Enhance Algorithm 1**: Add more detailed validation (e.g., check for numeric input)
2. **Enhance Algorithm 3**: Allow user to quit by entering "quit" or "exit"
3. **Enhance Algorithm 7**: Extend with more operations (power, square root, etc.)
4. **Create Your Own**: Design an input/output algorithm for a simple quiz or survey

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Simple Input Validation

```
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

// Algorithm: Validate User Age
console.log("Please enter your age: ");
let age = parseInt(readlineSync.question());

if (age < 0 || age > 150) {
    console.log("Invalid age! Please enter an age between 0 and 150.");
} else {
    console.log("Thank you! You are " + age + " years old.");
}
```

### Algorithm 2: User Information Form

```
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

// Algorithm: Collect User Information
console.log("User Information Form");
console.log("===================");

console.log("Enter your name: ");
let name = readlineSync.question();

console.log("Enter your age: ");
let age = readlineSync.question();

console.log("Enter your email: ");
let email = readlineSync.question();

console.log("Enter your favorite color: ");
let color = readlineSync.question();

console.log("");
console.log("SUMMARY:");
console.log("Name: " + name);
console.log("Age: " + age);
console.log("Email: " + email);
console.log("Favorite Color: " + color);
console.log("Form submitted successfully!");
```

### Algorithm 3: Number Validation Loop

```
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

// Algorithm: Get Valid Number
let valid_input = false;

while (!valid_input) {
    console.log("Enter a positive number: ");
    let number = parseFloat(readlineSync.question());

    if (number > 0) {
        valid_input = true;
        console.log("Valid number entered: " + number);
    } else {
        console.log("Invalid! Please enter a positive number.");
    }
}
```

### Algorithm 4: Grade Calculator with Input

```
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

// Algorithm: Calculate Letter Grade
console.log("Grade Calculator");
console.log("===============");

console.log("Enter assignment score: ");
let score = parseFloat(readlineSync.question());

console.log("Enter total possible points: ");
let total_points = parseFloat(readlineSync.question());

let percentage = (score / total_points) * 100;
let letter_grade = "F";

if (percentage >= 90) {
    letter_grade = "A";
} else if (percentage >= 80) {
    letter_grade = "B";
} else if (percentage >= 70) {
    letter_grade = "C";
} else if (percentage >= 60) {
    letter_grade = "D";
}

console.log("Score: " + score + "/" + total_points);
console.log("Percentage: " + percentage.toFixed(2) + "%");
console.log("Letter Grade: " + letter_grade);
```

### Algorithm 5: Temperature Converter with Menu

```
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

// Algorithm: Temperature Converter Menu
console.log("Temperature Converter");
console.log("1. Celsius to Fahrenheit");
console.log("2. Fahrenheit to Celsius");
console.log("Choose an option (1 or 2): ");

let choice = parseInt(readlineSync.question());

if (choice === 1) {
    console.log("Enter temperature in Celsius: ");
    let celsius = parseFloat(readlineSync.question());
    let fahrenheit = celsius * 9 / 5 + 32;
    console.log(celsius + "°C = " + fahrenheit.toFixed(2) + "°F");
} else if (choice === 2) {
    console.log("Enter temperature in Fahrenheit: ");
    let fahrenheit = parseFloat(readlineSync.question());
    let celsius = (fahrenheit - 32) * 5 / 9;
    console.log(fahrenheit + "°F = " + celsius.toFixed(2) + "°C");
} else {
    console.log("Invalid choice! Please enter 1 or 2.");
}
```

### Algorithm 6: Input Validation with Multiple Fields

```
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

// Algorithm: Validate Contact Information
let is_valid = true;

console.log("Contact Information Form");

console.log("Enter your full name: ");
let name = readlineSync.question();

if (name.length < 2) {
    console.log("Name must be at least 2 characters long.");
    is_valid = false;
}

console.log("Enter your phone number: ");
let phone = readlineSync.question();

if (phone.length < 10) {
    console.log("Phone number must be at least 10 digits.");
    is_valid = false;
}

console.log("Enter your email: ");
let email = readlineSync.question();

if (!email.includes("@")) {
    console.log("Email must contain '@' symbol.");
    is_valid = false;
}

if (is_valid) {
    console.log("Form submitted successfully!");
} else {
    console.log("Form has errors. Please fix and resubmit.");
}
```

### Algorithm 7: Calculator with User Interaction

```
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

// Algorithm: Interactive Calculator
console.log("Simple Calculator");

console.log("Enter first number: ");
let num1 = parseFloat(readlineSync.question());

console.log("Enter operator (+, -, *, /): ");
let operator = readlineSync.question();

console.log("Enter second number: ");
let num2 = parseFloat(readlineSync.question());

let result = 0;
let has_error = false;

if (operator === "+") {
    result = num1 + num2;
} else if (operator === "-") {
    result = num1 - num2;
} else if (operator === "*") {
    result = num1 * num2;
} else if (operator === "/") {
    if (num2 === 0) {
        console.log("Error: Division by zero!");
        has_error = true;
    } else {
        result = num1 / num2;
    }
} else {
    console.log("Error: Invalid operator!");
    has_error = true;
}

if (!has_error) {
    console.log(num1 + " " + operator + " " + num2 + " = " + result);
}
```

### I/O Operation Translation Patterns

| Pseudocode | JavaScript (Node.js) |
|------------|----------------------|
| `INPUT variable` | `variable = readlineSync.question()` |
| `OUTPUT message` | `console.log(message)` |
| `INPUT number` | `number = parseFloat(readlineSync.question())` |
| `INPUT integer` | `number = parseInt(readlineSync.question())` |
| `DISPLAY message` | `console.log(message)` |
| `LENGTH(string)` | `string.length` |
| `STRING CONTAINS` | `string.includes(substring)` |

### Important Notes

**Input Validation**: Always validate user input right after receiving it to prevent errors later in the program.

**Type Conversion**: Convert string inputs to appropriate types (numbers, booleans) when needed.

**User Experience**: Provide clear prompts and error messages to make your programs easy to use.

**Error Handling**: Check for common error conditions like division by zero.

---

 **Excellent work! You've mastered translating input/output operations from pseudocode to JavaScript!**

*Next up: Decision pseudocode!*


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic
