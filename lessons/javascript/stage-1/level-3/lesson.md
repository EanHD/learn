# Level 3: Basic Math Operations

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Time to do some math! Today you'll learn how to perform mathematical operations in JavaScript. You'll work with numbers, calculate results, and see how JavaScript handles different mathematical operations.

---

### Learning Goals

- Learn JavaScript arithmetic operators (+, -, *, /, %, **)
- Practice mathematical calculations
- Understand operator precedence
- Learn about the modulo operator (%)
- Understand how JavaScript handles different number types

---

### Your Task

**Copy the following code into a new file called `math.js`**

```
// Basic arithmetic operations
console.log("=== Basic Arithmetic ===");

// Addition
let sum = 5 + 3;
console.log("5 + 3 = " + sum);

// Subtraction
let difference = 10 - 4;
console.log("10 - 4 = " + difference);

// Multiplication
let product = 6 * 7;
console.log("6 * 7 = " + product);

// Division
let quotient = 15 / 3;
console.log("15 / 3 = " + quotient);

// Modulo (remainder)
let remainder = 17 % 5;
console.log("17 % 5 = " + remainder + " (remainder)");

// Exponentiation (new in ES2016)
let power = 2 ** 3;
console.log("2 ** 3 = " + power + " (2 to the power of 3)");

console.log("");
console.log("=== Order of Operations ===");

// Parentheses change the order
let withParentheses = (10 + 5) * 2;
console.log("(10 + 5) * 2 = " + withParentheses);

let withoutParentheses = 10 + 5 * 2;
console.log("10 + 5 * 2 = " + withoutParentheses);

console.log("");
console.log("=== Real-World Calculations ===");

// Calculate area of rectangle
let length = 10;
let width = 5;
let area = length * width;
console.log("Rectangle area (" + length + " x " + width + "): " + area);

// Calculate circle area (π * r²)
let radius = 7;
let circleArea = 3.14159 * radius * radius;
console.log("Circle area (radius " + radius + "): " + circleArea);

// Calculate average of three numbers
let num1 = 10;
let num2 = 20;
let num3 = 30;
let average = (num1 + num2 + num3) / 3;
console.log("Average of " + num1 + ", " + num2 + ", " + num3 + ": " + average);

console.log("");
console.log("=== Increment and Decrement ===");

// Pre-increment (++variable)
let count = 5;
console.log("Initial count: " + count);
console.log("Pre-increment (++count): " + (++count));
console.log("After pre-increment: " + count);

// Post-increment (variable++)
let count2 = 5;
console.log("Initial count2: " + count2);
console.log("Post-increment (count2++): " + (count2++));
console.log("After post-increment: " + count2);

console.log("");
console.log("=== Compound Assignment Operators ===");

let value = 10;
console.log("Initial value: " + value);

value += 5;  // Same as: value = value + 5
console.log("After += 5: " + value);

value -= 3;  // Same as: value = value - 3
console.log("After -= 3: " + value);

value *= 2;  // Same as: value = value * 2
console.log("After *= 2: " + value);

value /= 4;  // Same as: value = value / 4
console.log("After /= 4: " + value);
```

---

### How to Execute

1. **Run your program**:
   ```
   node math.js
   ```

**Expected output:**
```
=== Basic Arithmetic ===
5 + 3 = 8
10 - 4 = 6
6 * 7 = 42
15 / 3 = 5
17 % 5 = 2 (remainder)
2 ** 3 = 8 (2 to the power of 3)

=== Order of Operations ===
(10 + 5) * 2 = 30
10 + 5 * 2 = 20

=== Real-World Calculations ===
Rectangle area (10 x 5): 50
Circle area (radius 7): 153.93804000000003
Average of 10, 20, 30: 20

=== Increment and Decrement ===
Initial count: 5
Pre-increment (++count): 6
After pre-increment: 6
Initial count2: 5
Post-increment (count2++): 5
After post-increment: 6

=== Compound Assignment Operators ===
Initial value: 10
After += 5: 15
After -= 3: 12
After *= 2: 24
After /= 4: 6
```

---

### Success Checklist

- [ ] Created a file named `math.js`
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw all mathematical operations working correctly
- [ ] Understood operator precedence and different operations

---

### What's That Math Symbol Mean?

In JavaScript math, you saw some operators:

- **`+`** = Addition
- **`-`** = Subtraction
- **`*`** = Multiplication
- **`/`** = Division
- **`%`** = Modulo (remainder after division)
- **`**`** = Exponentiation (to the power of)
- **`++`** = Increment (add 1)
- **`--`** = Decrement (subtract 1)

---

### Try This (Optional Challenges)

1. Calculate compound interest: A = P(1+r/n)^nt
2. Create a temperature converter (Celsius to Fahrenheit)
3. Calculate the hypotenuse of a right triangle using the Pythagorean theorem
4. Experiment with dividing by zero - what happens?

---

## Quick Reference

| Operator | What it does | Example | Result |
|----------|--------------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `6 / 3` | `2` |
| `%` | Modulo (remainder) | `7 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |
| `++` | Increment | `x++` | `x = x + 1` |
| `--` | Decrement | `x--` | `x = x - 1` |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```
let sum = 5 + 3;
console.log("5 + 3 = " + sum);
```
- **`=`** = Assignment operator (stores the result of 5 + 3 into variable 'sum')
- **`+`** = Addition operator (performs arithmetic addition)
- **String concatenation**: The `+` operator also joins strings when one operand is a string

```
let remainder = 17 % 5;
console.log("17 % 5 = " + remainder + " (remainder)");
```
- **`%`** = Modulo operator (returns the remainder after division)
- 17 ÷ 5 = 3 remainder 2, so 17 % 5 = 2
- Useful for checking if numbers are even (n % 2 === 0) or cycling through values

```
let power = 2 ** 3;
console.log("2 ** 3 = " + power + " (2 to the power of 3)");
```
- **`**`** = Exponentiation operator (new in ES2016)
- 2 ** 3 = 2 to the power of 3 = 2 × 2 × 2 = 8
- Alternative to Math.pow(2, 3)

### Order of Operations (PEMDAS)

JavaScript follows the standard mathematical order of operations:

1. **P**arentheses `()`
2. **E**xponents `**`
3. **M**ultiplication `*` and **D**ivision `/` (left to right)
4. **A**ddition `+` and **S**ubtraction `-` (left to right)

Examples:
```
// Without parentheses: Multiplication before addition
10 + 5 * 2;  // = 10 + 10 = 20 (not 30!)

// With parentheses: Addition before multiplication
(10 + 5) * 2;  // = 15 * 2 = 30
```

### Increment/Decrement Operators

JavaScript has special operators for adding/subtracting 1:

```
let x = 5;

// Pre-increment (++x): Add 1 FIRST, then return the new value
console.log(++x);  // Prints: 6 (x is now 6)

// Post-increment (x++): Return the current value FIRST, then add 1
let y = 5;
console.log(y++);  // Prints: 5 (y is now 6)
console.log(y);    // Prints: 6
```

### Compound Assignment Operators

These combine an operation with assignment:

```
let value = 10;

value += 5;  // Same as: value = value + 5;  // value is now 15
value -= 3;  // Same as: value = value - 3;  // value is now 12
value *= 2;  // Same as: value = value * 2;  // value is now 24
value /= 4;  // Same as: value = value / 4;  // value is now 6
value %= 3;  // Same as: value = value % 3;  // value is now 0
```

### Important JavaScript Math Notes

**Floating Point Precision:**
```
console.log(0.1 + 0.2);  // Output: 0.30000000000000004 (not exactly 0.3!)
```
This is due to how JavaScript (and most programming languages) store decimal numbers internally.

**Division by Zero:**
```
console.log(5 / 0);     // Output: Infinity
console.log(-5 / 0);    // Output: -Infinity
console.log(0 / 0);     // Output: NaN (Not a Number)
```

**Mathematical Functions:**
For more complex math, JavaScript has a built-in Math object:
```
Math.sqrt(16);     // Square root: 4
Math.max(1, 5, 3); // Maximum: 5
Math.min(1, 5, 3); // Minimum: 1
Math.round(4.7);   // Round: 5
Math.floor(4.7);   // Floor: 4
Math.ceil(4.2);    // Ceiling: 5
Math.PI;           // Pi: 3.141592653589793
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Unexpected result like `0.30000000000000004` | Floating point precision | Use `toFixed()` for display: `(0.1+0.2).toFixed(1)` |
| `NaN` in calculations | Invalid mathematical operation | Check that all operands are numbers |
| `Infinity` result | Division by 0 | Check for zero denominators |
| Operator precedence issues | Wrong order of operations | Use parentheses to clarify order |

### Math in Real Life

JavaScript math is used everywhere:
- **E-commerce**: Calculating totals, taxes, discounts
- **Gaming**: Physics calculations, score tracking
- **Finance**: Interest calculations, currency conversions
- **Data**: Statistics, averages, percentages
- **Graphics**: Positioning elements, animations

### Advanced Challenge (For the Brave!)

Try this complex calculation:

```
// Compound interest calculation
let principal = 1000;  // Initial amount
let rate = 0.05;       // 5% annual interest rate
let timesCompounded = 12;  // Compounded monthly
let years = 10;        // 10 years

// Formula: A = P(1 + r/n)^(nt)
let amount = principal * Math.pow(1 + rate/timesCompounded, timesCompounded * years);

console.log("Initial investment: $" + principal);
console.log("After " + years + " years at " + (rate*100) + "% interest: $" + amount.toFixed(2));

// Calculate percentage change
let original = 100;
let newAmount = 125;
let percentageChange = ((newAmount - original) / original) * 100;
console.log("Percentage change from " + original + " to " + newAmount + ": " + percentageChange + "%");
```

---

 **Excellent work! You're becoming a mathematical wizard in JavaScript!** 

*Ready for the next challenge? Let's learn how to get input from users!*


### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim


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
