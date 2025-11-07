# Level 2: Variables in Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Welcome to Level 2! Today we're focusing on how to handle variables in your pseudocode. You'll learn to translate pseudocode that uses variables into working JavaScript code, and understand how to track variable changes as your algorithms run.

---

### Learning Goals

- Understand how to represent variables in pseudocode
- Learn to translate variable declarations and assignments from pseudocode
- Practice tracking variable changes through algorithms
- Create programs that properly manage data flow
- Develop awareness of variable scope and state

---

### Variable Concepts in Pseudocode

Variables in pseudocode follow simple patterns:

**Declaration and assignment:**
```javascript
SET name TO "John"
SET age TO 25
SET is_student TO TRUE
```javascript

**Reassignment:**
```javascript
SET age TO age + 1
SET total TO total + new_value
SET is_student TO FALSE
```javascript

**Calculations with variables:**
```javascript
SET area TO length * width
SET average TO (num1 + num2 + num3) / 3
SET is_adult TO age >= 18
```javascript

---

### Your Task

**For each pseudocode algorithm below, translate it into working JavaScript code. Pay special attention to how variables are declared, assigned, and modified.**

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

## Algorithm 1: Simple Variable Swapping

**Pseudocode:**
```javascript
Algorithm: Swap Two Variables
1. SET first_number TO 10
2. SET second_number TO 20
3. DISPLAY "Before swap: first=" + first_number + ", second=" + second_number
4. SET temp TO first_number
5. SET first_number TO second_number
6. SET second_number TO temp
7. DISPLAY "After swap: first=" + first_number + ", second=" + second_number
```javascript

**Your Task:** Create a JavaScript program that demonstrates variable swapping.

---

## Algorithm 2: Running Total Calculator

**Pseudocode:**
```javascript
Algorithm: Calculate Running Total
1. SET total TO 0
2. SET count TO 0
3. SET number TO 5
4. SET total TO total + number
5. SET count TO count + 1
6. SET number TO 10
7. SET total TO total + number
8. SET count TO count + 1
9. SET number TO 15
10. SET total TO total + number
11. SET count TO count + 1
12. SET average TO total / count
13. DISPLAY "Total: " + total
14. DISPLAY "Count: " + count
15. DISPLAY "Average: " + average
```javascript

**Your Task:** Create a JavaScript program that calculates a running total and average.

---

## Algorithm 3: Temperature Tracker

**Pseudocode:**
```javascript
Algorithm: Track Temperature Readings
1. SET min_temp TO 100
2. SET max_temp TO -100
3. SET current_temp TO 72
4. IF current_temp < min_temp THEN
   SET min_temp TO current_temp
5. IF current_temp > max_temp THEN
   SET max_temp TO current_temp
6. DISPLAY "Current: " + current_temp + ", Min: " + min_temp + ", Max: " + max_temp
7. SET current_temp TO 65
8. IF current_temp < min_temp THEN
   SET min_temp TO current_temp
9. IF current_temp > max_temp THEN
   SET max_temp TO current_temp
10. DISPLAY "Current: " + current_temp + ", Min: " + min_temp + ", Max: " + max_temp
11. SET current_temp TO 80
12. IF current_temp < min_temp THEN
   SET min_temp TO current_temp
13. IF current_temp > max_temp THEN
   SET max_temp TO current_temp
14. DISPLAY "Current: " + current_temp + ", Min: " + min_temp + ", Max: " + max_temp
```javascript

**Your Task:** Create a JavaScript program that tracks min/max temperatures.

---

## Algorithm 4: Account Balance Tracker

**Pseudocode:**
```javascript
Algorithm: Track Bank Account Balance
1. SET account_balance TO 1000
2. SET transaction_amount TO -50
3. SET account_balance TO account_balance + transaction_amount
4. DISPLAY "Balance after withdrawal: $" + account_balance
5. SET transaction_amount TO 200
6. SET account_balance TO account_balance + transaction_amount
7. DISPLAY "Balance after deposit: $" + account_balance
8. SET transaction_amount TO -75.50
9. SET account_balance TO account_balance + transaction_amount
10. DISPLAY "Balance after withdrawal: $" + account_balance
11. SET transaction_amount TO 150.25
12. SET account_balance TO account_balance + transaction_amount
13. DISPLAY "Balance after deposit: $" + account_balance
```javascript

**Your Task:** Create a JavaScript program that tracks account balance changes.

---

## Algorithm 5: Student Grade Calculator

**Pseudocode:**
```javascript
Algorithm: Calculate Student Grade
1. SET total_points TO 0
2. SET possible_points TO 0
3. SET assignment_points TO 85
4. SET assignment_possible TO 100
5. SET total_points TO total_points + assignment_points
6. SET possible_points TO possible_points + assignment_possible
7. SET assignment_points TO 92
8. SET assignment_possible TO 100
9. SET total_points TO total_points + assignment_points
10. SET possible_points TO possible_points + assignment_possible
11. SET assignment_points TO 78
12. SET assignment_possible TO 100
13. SET total_points TO total_points + assignment_points
14. SET possible_points TO possible_points + assignment_possible
15. SET percentage TO (total_points / possible_points) * 100
16. SET letter_grade TO "F"
17. IF percentage >= 90 THEN SET letter_grade TO "A"
18. ELSE IF percentage >= 80 THEN SET letter_grade TO "B"
19. ELSE IF percentage >= 70 THEN SET letter_grade TO "C"
20. ELSE IF percentage >= 60 THEN SET letter_grade TO "D"
21. DISPLAY "Total Points: " + total_points
22. DISPLAY "Possible Points: " + possible_points
23. DISPLAY "Percentage: " + percentage
24. DISPLAY "Letter Grade: " + letter_grade
```javascript

**Your Task:** Create a JavaScript program that calculates student grades.

---

## Algorithm 6: Counter Patterns

**Pseudocode:**
```javascript
Algorithm: Different Counter Patterns
1. SET counter TO 1
2. SET even_counter TO 2
3. SET odd_counter TO 1
4. WHILE counter <= 5 DO
   5. DISPLAY "Count: " + counter
   6. SET counter TO counter + 1
7. END WHILE
8. WHILE even_counter <= 10 DO
   9. DISPLAY "Even: " + even_counter
   10. SET even_counter TO even_counter + 2
11. END WHILE
12. WHILE odd_counter <= 10 DO
   13. DISPLAY "Odd: " + odd_counter
   14. SET odd_counter TO odd_counter + 2
15. END WHILE
```javascript

**Your Task:** Create a JavaScript program that demonstrates different counting patterns.

---

## Algorithm 7: Accumulator Pattern

**Pseudocode:**
```javascript
Algorithm: Calculate Statistics
1. SET sum TO 0
2. SET count TO 0
3. SET product TO 1
4. SET current_value TO 3
5. SET sum TO sum + current_value
6. SET count TO count + 1
7. SET product TO product * current_value
8. SET current_value TO 4
9. SET sum TO sum + current_value
10. SET count TO count + 1
11. SET product TO product * current_value
12. SET current_value TO 5
13. SET sum TO sum + current_value
14. SET count TO count + 1
15. SET product TO product * current_value
16. SET average TO sum / count
17. DISPLAY "Sum: " + sum
18. DISPLAY "Count: " + count
19. DISPLAY "Product: " + product
20. DISPLAY "Average: " + average
```javascript

**Your Task:** Create a JavaScript program that demonstrates accumulator patterns.

---

### Key Concepts for Variable Handling

**Variable Declaration:**
- In JavaScript, use `let` for variables that will change
- Use `const` for values that won't change after initialization

**Assignment vs Comparison:**
- Pseudocode `SET x TO value` becomes JavaScript `x = value`
- Pseudocode comparisons like `x > 5` become `x > 5` in JavaScript

**Tracking Variable Changes:**
- Each assignment statement updates the variable's value
- The order of operations matters in algorithms
- Variables can be used in calculations and then updated

---

### Success Checklist

**For Each Algorithm:**
- [ ] All variables properly declared using `let` or `const`
- [ ] Variable assignments correctly translated from pseudocode
- [ ] Program runs without errors
- [ ] Output matches expected results
- [ ] Variable state changes tracked correctly

**Overall Progress:**
- [ ] Completed all 7 algorithms
- [ ] All programs work correctly
- [ ] Code clearly shows variable tracking

---

### Try This (Optional Challenges)

1. **Enhance Algorithm 1**: Add multiple swaps in sequence to see how temporary variables work
2. **Enhance Algorithm 3**: Add more temperature readings and track how min/max change
3. **Enhance Algorithm 4**: Add a transaction history array to track all changes
4. **Create Your Own**: Write pseudocode for calculating compound interest with variables

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Simple Variable Swapping

```javascript
// Algorithm: Swap Two Variables
let first_number = 10;
let second_number = 20;

console.log("Before swap: first=" + first_number + ", second=" + second_number);

let temp = first_number;
first_number = second_number;
second_number = temp;

console.log("After swap: first=" + first_number + ", second=" + second_number);
```javascript

### Algorithm 2: Running Total Calculator

```javascript
// Algorithm: Calculate Running Total
let total = 0;
let count = 0;

let number = 5;
total = total + number;
count = count + 1;

number = 10;
total = total + number;
count = count + 1;

number = 15;
total = total + number;
count = count + 1;

let average = total / count;

console.log("Total: " + total);
console.log("Count: " + count);
console.log("Average: " + average);
```javascript

### Algorithm 3: Temperature Tracker

```javascript
// Algorithm: Track Temperature Readings
let min_temp = 100;
let max_temp = -100;

let current_temp = 72;
if (current_temp < min_temp) {
    min_temp = current_temp;
}
if (current_temp > max_temp) {
    max_temp = current_temp;
}
console.log("Current: " + current_temp + ", Min: " + min_temp + ", Max: " + max_temp);

current_temp = 65;
if (current_temp < min_temp) {
    min_temp = current_temp;
}
if (current_temp > max_temp) {
    max_temp = current_temp;
}
console.log("Current: " + current_temp + ", Min: " + min_temp + ", Max: " + max_temp);

current_temp = 80;
if (current_temp < min_temp) {
    min_temp = current_temp;
}
if (current_temp > max_temp) {
    max_temp = current_temp;
}
console.log("Current: " + current_temp + ", Min: " + min_temp + ", Max: " + max_temp);
```javascript

### Algorithm 4: Account Balance Tracker

```javascript
// Algorithm: Track Bank Account Balance
let account_balance = 1000;

let transaction_amount = -50;
account_balance = account_balance + transaction_amount;
console.log("Balance after withdrawal: $" + account_balance);

transaction_amount = 200;
account_balance = account_balance + transaction_amount;
console.log("Balance after deposit: $" + account_balance);

transaction_amount = -75.50;
account_balance = account_balance + transaction_amount;
console.log("Balance after withdrawal: $" + account_balance);

transaction_amount = 150.25;
account_balance = account_balance + transaction_amount;
console.log("Balance after deposit: $" + account_balance);
```javascript

### Algorithm 5: Student Grade Calculator

```javascript
// Algorithm: Calculate Student Grade
let total_points = 0;
let possible_points = 0;

let assignment_points = 85;
let assignment_possible = 100;
total_points = total_points + assignment_points;
possible_points = possible_points + assignment_possible;

assignment_points = 92;
assignment_possible = 100;
total_points = total_points + assignment_points;
possible_points = possible_points + assignment_possible;

assignment_points = 78;
assignment_possible = 100;
total_points = total_points + assignment_points;
possible_points = possible_points + assignment_possible;

let percentage = (total_points / possible_points) * 100;
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

console.log("Total Points: " + total_points);
console.log("Possible Points: " + possible_points);
console.log("Percentage: " + percentage);
console.log("Letter Grade: " + letter_grade);
```javascript

### Algorithm 6: Counter Patterns

```javascript
// Algorithm: Different Counter Patterns
let counter = 1;
while (counter <= 5) {
    console.log("Count: " + counter);
    counter = counter + 1;
}

let even_counter = 2;
while (even_counter <= 10) {
    console.log("Even: " + even_counter);
    even_counter = even_counter + 2;
}

let odd_counter = 1;
while (odd_counter <= 10) {
    console.log("Odd: " + odd_counter);
    odd_counter = odd_counter + 2;
}
```javascript

### Algorithm 7: Accumulator Pattern

```javascript
// Algorithm: Calculate Statistics
let sum = 0;
let count = 0;
let product = 1;

let current_value = 3;
sum = sum + current_value;
count = count + 1;
product = product * current_value;

current_value = 4;
sum = sum + current_value;
count = count + 1;
product = product * current_value;

current_value = 5;
sum = sum + current_value;
count = count + 1;
product = product * current_value;

let average = sum / count;

console.log("Sum: " + sum);
console.log("Count: " + count);
console.log("Product: " + product);
console.log("Average: " + average);
```javascript

### Variable Translation Patterns

| Pseudocode | JavaScript |
|------------|------------|
| `SET variable TO value` | `let variable = value;` |
| `SET variable TO variable + 1` | `variable = variable + 1;` or `variable += 1;` or `variable++;` |
| `SET variable TO variable * value` | `variable = variable * value;` or `variable *= value;` |
| `SET variable TO calculation` | `let variable = calculation;` |

### Important Notes

**Scope**: In JavaScript, `let` has block scope while `var` has function scope. Generally use `let` for modern code.

**Dynamic Typing**: JavaScript variables can change type, but for algorithm translation, the type usually stays consistent.

**Accumulator Pattern**: This is a common pattern where a variable accumulates values: `total = total + newValue`.

**Swapping Pattern**: To swap two variables, you need a temporary variable to hold one value during the swap.

---

 **Excellent work! You've mastered handling variables in pseudocode-to-code translation!** 

*Next up: Mathematical operations in pseudocode!*


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
