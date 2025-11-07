# Level 1: Basic Pseudocode Translation

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Welcome to Stage 2! You've mastered copying code - now it's time to think like a programmer! Today you'll learn to translate written instructions (pseudocode) into working JavaScript programs. This is where programming becomes creative problem-solving!

---

### Learning Goals

- Understand what pseudocode is and why it's useful
- Learn to read and interpret algorithmic descriptions
- Practice translating simple algorithms into JavaScript code
- Develop logical thinking for programming
- Create working programs from written instructions

---

### What is Pseudocode?

**Pseudocode** is a way to write programming logic in plain English (or your native language) before writing actual code. It's like writing a recipe or instructions for a task.

**Example:**
```javascript
Algorithm: Make a sandwich
1. Get bread from pantry
2. Get peanut butter from fridge
3. Get jelly from pantry
4. Spread peanut butter on one bread slice
5. Spread jelly on the other bread slice
6. Put slices together
7. Enjoy your sandwich!
```javascript

This is much easier to understand than trying to write code first!

---

### Your Task

**For each pseudocode algorithm below, translate it into working JavaScript code.**

---


### How to Run

1. **Run the code**:
   ```bash
   node hello.js
   ```java

**Expected output:**
```javascript
Hello, World!
```javascript

## Algorithm 1: Greeting Program

**Pseudocode:**
```javascript
Algorithm: Display Personal Greeting
1. Display "Hello! What's your name?" to the user
2. Get the user's name from input
3. Display "Nice to meet you, " followed by the user's name
4. Display "Welcome to programming!"
```javascript

**Your Task:** Create a JavaScript program that follows these exact steps.

---

## Algorithm 2: Simple Calculator

**Pseudocode:**
```javascript
Algorithm: Add Two Numbers
1. Ask user for first number
2. Get first number from user
3. Ask user for second number
4. Get second number from user
5. Calculate sum of the two numbers
6. Display "The sum is: " followed by the sum
```javascript

**Your Task:** Create a JavaScript program that implements this calculator.

---

## Algorithm 3: Age Calculator

**Pseudocode:**
```javascript
Algorithm: Calculate Age in Days
1. Display "Enter your age in years: "
2. Get age in years from user
3. Calculate days = age × 365
4. Display "You are approximately " + days + " days old"
5. Display "That's a lot of days!"
```javascript

**Your Task:** Create a program that calculates approximate age in days.

---

## Algorithm 4: Temperature Converter

**Pseudocode:**
```javascript
Algorithm: Celsius to Fahrenheit Converter
1. Display "Enter temperature in Celsius: "
2. Get temperature in Celsius from user
3. Calculate Fahrenheit = (Celsius × 9/5) + 32
4. Display the Celsius temperature
5. Display "°C = "
6. Display the Fahrenheit temperature
7. Display "°F"
```javascript

**Your Task:** Create a temperature conversion program.

---

## Algorithm 5: Rectangle Area Calculator

**Pseudocode:**
```javascript
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
```javascript

**Your Task:** Create a program that calculates both area and perimeter.

---

## Algorithm 6: Simple Interest Calculator

**Pseudocode:**
```javascript
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
```javascript

**Your Task:** Implement the complete interest calculation.

---

## Algorithm 7: BMI Calculator

**Pseudocode:**
```javascript
Algorithm: Calculate Body Mass Index
1. Display "BMI Calculator"
2. Display "Enter weight in kg: "
3. Get weight from user
4. Display "Enter height in meters: "
5. Get height from user
6. Calculate bmi = weight ÷ (height × height)
7. Display "Your BMI is: " + bmi
8. If bmi < 18.5 then
   Display "Category: Underweight"
9. Else if bmi < 25 then
   Display "Category: Normal weight"
10. Else if bmi < 30 then
   Display "Category: Overweight"
11. Else
   Display "Category: Obesity"
```javascript

**Your Task:** Create a program that calculates BMI with categorization.

---

### How to Approach Each Algorithm

**Step-by-Step Process:**

1. **Read Carefully**: Understand what the algorithm does
2. **Identify Inputs**: What information does the user provide?
3. **Identify Outputs**: What should the program display?
4. **Identify Calculations**: What math is needed?
5. **Plan the Code Structure**:
   - Define variables for user input
   - Use appropriate functions for input/output
   - Perform calculations
   - Display results

**Example Planning for Algorithm 1:**
- **Inputs**: User's name (string)
- **Outputs**: Greeting messages
- **No calculations needed**
- **Structure**: Input statement → Output statements

---

### Success Checklist

**For Each Algorithm:**
- [ ] Program compiles without errors
- [ ] Program runs and produces expected output
- [ ] Followed the pseudocode steps exactly
- [ ] Used appropriate variable names
- [ ] Included clear output messages

**Overall Progress:**
- [ ] Completed all 7 algorithms
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
```javascript
Algorithm: Process User Data
1. Get user's name
2. Get user's age
3. If age >= 18 then
   Display "Adult user"
Else
   Display "Minor user"
4. Display "Data processed"
```javascript

### Bad Pseudocode (Too Vague)
```javascript
Algorithm: Do stuff
1. Get things
2. Calculate something
3. Show results
```javascript

### Good Pseudocode (Clear and Specific)
```javascript
Algorithm: Calculate BMI
1. Display "BMI Calculator"
2. Display "Enter weight in kg: "
3. Get weight from user
4. Display "Enter height in meters: "
5. Get height from user
6. Calculate BMI = weight ÷ (height × height)
7. Display "Your BMI is: " + BMI
```javascript

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Greeting Program

```javascript
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

console.log("Algorithm 1: Greeting Program");

// Display "Hello! What's your name?" to the user
let name = readlineSync.question("Hello! What's your name? ");

// Display "Nice to meet you, " followed by the user's name
console.log("Nice to meet you, " + name);

// Display "Welcome to programming!"
console.log("Welcome to programming!");
```javascript

### Algorithm 2: Simple Calculator

```javascript
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

console.log("Algorithm 2: Simple Calculator");

// Ask user for first number
let firstNum = parseFloat(readlineSync.question("Enter first number: "));

// Ask user for second number
let secondNum = parseFloat(readlineSync.question("Enter second number: "));

// Calculate sum of the two numbers
let sum = firstNum + secondNum;

// Display "The sum is: " followed by the sum
console.log("The sum is: " + sum);
```javascript

### Algorithm 3: Age Calculator

```javascript
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

console.log("Algorithm 3: Age Calculator");

// Display "Enter your age in years: "
let age = parseInt(readlineSync.question("Enter your age in years: "));

// Calculate days = age × 365
let days = age * 365;

// Display messages
console.log("You are approximately " + days + " days old");
console.log("That's a lot of days!");
```javascript

### Algorithm 4: Temperature Converter

```javascript
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

console.log("Algorithm 4: Temperature Converter");

// Display "Enter temperature in Celsius: "
let celsius = parseFloat(readlineSync.question("Enter temperature in Celsius: "));

// Calculate Fahrenheit = (Celsius × 9/5) + 32
let fahrenheit = (celsius * 9/5) + 32;

// Display the results
console.log(celsius + "°C = " + fahrenheit + "°F");
```javascript

### Algorithm 5: Rectangle Area Calculator

```javascript
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

console.log("Rectangle Area Calculator");

// Get length from user
let length = parseFloat(readlineSync.question("Enter length: "));

// Get width from user
let width = parseFloat(readlineSync.question("Enter width: "));

// Calculate area = length × width
let area = length * width;

// Calculate perimeter = 2 × (length + width)
let perimeter = 2 * (length + width);

// Display results
console.log("Area: " + area);
console.log("Perimeter: " + perimeter);
```javascript

### Algorithm 6: Simple Interest Calculator

```javascript
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

console.log("Simple Interest Calculator");

// Get principal from user
let principal = parseFloat(readlineSync.question("Enter principal amount: $"));

// Get rate from user
let rate = parseFloat(readlineSync.question("Enter interest rate (%): "));

// Get time from user
let time = parseFloat(readlineSync.question("Enter time in years: "));

// Calculate interest = (principal × rate × time) ÷ 100
let interest = (principal * rate * time) / 100;

// Calculate total = principal + interest
let total = principal + interest;

// Display results
console.log("Principal: $" + principal.toFixed(2));
console.log("Interest: $" + interest.toFixed(2));
console.log("Total: $" + total.toFixed(2));
```javascript

### Algorithm 7: BMI Calculator

```javascript
// For Node.js environment with readline-sync
const readlineSync = require('readline-sync');

console.log("BMI Calculator");

// Get weight from user
let weight = parseFloat(readlineSync.question("Enter weight in kg: "));

// Get height from user
let height = parseFloat(readlineSync.question("Enter height in meters: "));

// Calculate bmi = weight ÷ (height × height)
let bmi = weight / (height * height);

// Display the BMI
console.log("Your BMI is: " + bmi.toFixed(2));

// Category determination
if (bmi < 18.5) {
    console.log("Category: Underweight");
} else if (bmi < 25) {
    console.log("Category: Normal weight");
} else if (bmi < 30) {
    console.log("Category: Overweight");
} else {
    console.log("Category: Obesity");
}
```javascript

### Common Translation Patterns

| Pseudocode Pattern | JavaScript Equivalent |
|-------------------|------------------------|
| `Display message` | `console.log(message);` |
| `Get variable from user` | `readlineSync.question("prompt");` |
| `Calculate result = a + b` | `result = a + b;` |
| `If condition then` | `if (condition) {` |
| `Else if` | `else if (condition) {` |
| `Else` | `else {` |

### Debugging Tips

**"Program doesn't compile":**
- Check semicolons at end of statements
- Verify variable declarations
- Ensure proper braces `{ }`

**"Wrong output":**
- Check variable names match (case-sensitive)
- Verify data types match usage
- Check mathematical formulas

**"Program crashes":**
- Make sure variables are declared before use
- Check array sizes for strings
- Verify input functions are properly called

### Variable Naming Best Practices

**Good Names:**
- `userAge` (clear what it stores)
- `temperatureCelsius` (descriptive)
- `rectangleArea` (specific purpose)

**Bad Names:**
- `x` (too vague)
- `temp` (unclear what kind of temperature)
- `var1` (meaningless)

### Input/Output Patterns

**Getting Numbers:**
```javascript
let age = parseFloat(readlineSync.question("Enter age: "));
```javascript

**Getting Text:**
```javascript
let name = readlineSync.question("Enter name: ");
```javascript

**Displaying Results:**
```javascript
console.log("Result: " + result);
console.log("Price: $" + price.toFixed(2));
console.log("Hello, " + name + "!");
```javascript

---

 **Congratulations! You've translated your first pseudocode algorithms into working JavaScript programs!** 

*This is a major milestone - you're now thinking like a programmer! Next up: Variables in pseudocode!*


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

```js
console.log("Hello, World!");

```js

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard javascript conventions with proper imports and main function
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
