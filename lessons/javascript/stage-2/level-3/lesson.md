# Level 3: Mathematical Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Welcome to Level 3! Today we're focusing on mathematical operations in pseudocode. You'll learn to translate complex mathematical formulas and calculations from pseudocode into working JavaScript code, and understand operator precedence in algorithmic calculations.

---

### Learning Goals

- Understand how to represent mathematical operations in pseudocode
- Learn to translate complex mathematical formulas from pseudocode
- Practice operator precedence in algorithmic calculations
- Create programs that perform complex mathematical computations
- Develop awareness of precision and rounding in calculations

---

### Mathematical Operations in Pseudocode

Mathematical expressions in pseudocode follow standard notation:

**Basic operations:**
```
SET result TO 5 + 3
SET result TO 10 - 4
SET result TO 6 * 7
SET result TO 15 / 3
SET remainder TO 17 MOD 5
```

**Complex expressions:**
```
SET area TO length * width
SET volume TO length * width * height
SET average TO (num1 + num2 + num3) / 3
SET tax TO price * 0.08
SET discount TO original_price * discount_rate
```

**Order of operations:**
```
SET result TO 2 + 3 * 4     // result = 14 (not 20), multiplication first
SET result TO (2 + 3) * 4   // result = 20, parentheses override
SET result TO 10 / 2 + 3    // result = 8, division first
```

**Mathematical functions:**
```
SET result TO POWER(2, 3)    // 2 to the power of 3
SET result TO SQRT(16)       // square root of 16
SET result TO ROUND(3.7)     // round to nearest integer
```

---

### Your Task

**For each pseudocode algorithm below, translate it into working JavaScript code. Pay special attention to operator precedence and mathematical formula accuracy.**

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

## Algorithm 1: Complex Arithmetic Expression

**Pseudocode:**
```
Algorithm: Evaluate Complex Expression
1. SET a TO 10
2. SET b TO 5
3. SET c TO 2
4. SET result TO (a + b) * c - a / c
5. DISPLAY "Result: " + result
6. SET result2 TO a + b * c - a / c
7. DISPLAY "Result without parentheses: " + result2
8. SET result3 TO ((a + b) * c - a) / c
9. DISPLAY "Result with different grouping: " + result3
```

**Your Task:** Create a JavaScript program that evaluates complex arithmetic expressions.

---

## Algorithm 2: Quadratic Formula Calculator

**Pseudocode:**
```
Algorithm: Solve Quadratic Equation
1. SET a TO 1
2. SET b TO -5
3. SET c TO 6
4. SET discriminant TO b * b - 4 * a * c
5. SET sqrt_discriminant TO SQRT(discriminant)
6. SET root1 TO (-b + sqrt_discriminant) / (2 * a)
7. SET root2 TO (-b - sqrt_discriminant) / (2 * a)
8. DISPLAY "Root 1: " + root1
9. DISPLAY "Root 2: " + root2
```

**Your Task:** Create a JavaScript program that solves quadratic equations using the quadratic formula.

---

## Algorithm 3: Compound Interest Calculator

**Pseudocode:**
```
Algorithm: Calculate Compound Interest
1. SET principal TO 1000
2. SET rate TO 0.05
3. SET time TO 10
4. SET compounds_per_year TO 12
5. SET amount TO principal * POWER(1 + rate / compounds_per_year, compounds_per_year * time)
6. SET interest TO amount - principal
7. DISPLAY "Principal: $" + principal
8. DISPLAY "Final Amount: $" + amount
9. DISPLAY "Interest Earned: $" + interest
```

**Your Task:** Create a JavaScript program that calculates compound interest.

---

## Algorithm 4: Geometric Calculations

**Pseudocode:**
```
Algorithm: Calculate Geometric Properties
1. SET radius TO 5
2. SET side TO 4
3. SET base TO 6
4. SET height TO 8
5. SET circle_area TO PI * radius * radius
6. SET circle_circumference TO 2 * PI * radius
7. SET square_area TO side * side
8. SET square_perimeter TO 4 * side
9. SET triangle_area TO 0.5 * base * height
10. DISPLAY "Circle - Area: " + circle_area + ", Circumference: " + circle_circumference
11. DISPLAY "Square - Area: " + square_area + ", Perimeter: " + square_perimeter
12. DISPLAY "Triangle - Area: " + triangle_area
```

**Your Task:** Create a JavaScript program that calculates geometric properties.

---

## Algorithm 5: Physics Formula Calculator

**Pseudocode:**
```
Algorithm: Physics Calculations
1. SET mass TO 5.5
2. SET velocity TO 10
3. SET acceleration TO 9.8
4. SET time TO 3
5. SET kinetic_energy TO 0.5 * mass * velocity * velocity
6. SET force TO mass * acceleration
7. SET distance TO velocity * time + 0.5 * acceleration * time * time
8. SET momentum TO mass * velocity
9. DISPLAY "Kinetic Energy: " + kinetic_energy
10. DISPLAY "Force: " + force
11. DISPLAY "Distance: " + distance
12. DISPLAY "Momentum: " + momentum
```

**Your Task:** Create a JavaScript program that calculates physics formulas.

---

## Algorithm 6: Temperature Conversion with Multiple Formulas

**Pseudocode:**
```
Algorithm: Multiple Temperature Conversions
1. SET celsius TO 25
2. SET fahrenheit TO celsius * 9 / 5 + 32
3. SET kelvin TO celsius + 273.15
4. SET celsius_from_f TO (fahrenheit - 32) * 5 / 9
5. SET celsius_from_k TO kelvin - 273.15
6. DISPLAY "Celsius: " + celsius
7. DISPLAY "Fahrenheit: " + fahrenheit
8. DISPLAY "Kelvin: " + kelvin
9. DISPLAY "F to C: " + celsius_from_f
10. DISPLAY "K to C: " + celsius_from_k
```

**Your Task:** Create a JavaScript program that performs multiple temperature conversions.

---

## Algorithm 7: Statistical Calculations

**Pseudocode:**
```
Algorithm: Calculate Statistics for Three Numbers
1. SET num1 TO 10
2. SET num2 TO 20
3. SET num3 TO 30
4. SET sum TO num1 + num2 + num3
5. SET average TO sum / 3
6. SET range TO num3 - num1  // assuming num3 is largest, num1 is smallest
7. SET sum_of_squares TO num1 * num1 + num2 * num2 + num3 * num3
8. SET mean_of_squares TO sum_of_squares / 3
9. SET variance TO mean_of_squares - average * average
10. SET std_deviation TO SQRT(variance)
11. DISPLAY "Sum: " + sum
12. DISPLAY "Average: " + average
13. DISPLAY "Range: " + range
14. DISPLAY "Variance: " + variance
15. DISPLAY "Standard Deviation: " + std_deviation
```

**Your Task:** Create a JavaScript program that calculates statistical measures.

---

### Key Concepts for Mathematical Operations

**Operator Precedence in JavaScript:**
- Parentheses `()`
- Exponentiation `**`
- Multiplication `*`, Division `/`, Modulus `%` (left to right)
- Addition `+`, Subtraction `-` (left to right)

**Mathematical Functions:**
- `Math.sqrt(x)` - Square root
- `Math.pow(base, exponent)` - Power
- `Math.round(x)` - Round to nearest integer
- `Math.floor(x)` - Round down
- `Math.ceil(x)` - Round up
- `Math.PI` - Pi constant

---

### Success Checklist

**For Each Algorithm:**
- [ ] Mathematical formulas correctly translated from pseudocode
- [ ] Operator precedence properly observed
- [ ] Program runs without errors
- [ ] Output matches expected mathematical results
- [ ] Calculations are accurate

**Overall Progress:**
- [ ] Completed all 7 algorithms
- [ ] All programs work correctly
- [ ] Mathematical computations are accurate

---

### Try This (Optional Challenges)

1. **Enhance Algorithm 2**: Add complex number handling for cases where the discriminant is negative
2. **Enhance Algorithm 3**: Add monthly contribution calculations to compound interest
3. **Enhance Algorithm 7**: Calculate standard deviation for any number of inputs using arrays
4. **Create Your Own**: Write pseudocode for calculating the volume of a cylinder and cone

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Complex Arithmetic Expression

```
// Algorithm: Evaluate Complex Expression
let a = 10;
let b = 5;
let c = 2;

let result = (a + b) * c - a / c;
console.log("Result: " + result);

let result2 = a + b * c - a / c;
console.log("Result without parentheses: " + result2);

let result3 = ((a + b) * c - a) / c;
console.log("Result with different grouping: " + result3);
```

### Algorithm 2: Quadratic Formula Calculator

```
// Algorithm: Solve Quadratic Equation
let a = 1;
let b = -5;
let c = 6;

let discriminant = b * b - 4 * a * c;
let sqrt_discriminant = Math.sqrt(discriminant);
let root1 = (-b + sqrt_discriminant) / (2 * a);
let root2 = (-b - sqrt_discriminant) / (2 * a);

console.log("Root 1: " + root1);
console.log("Root 2: " + root2);
```

### Algorithm 3: Compound Interest Calculator

```
// Algorithm: Calculate Compound Interest
let principal = 1000;
let rate = 0.05;
let time = 10;
let compounds_per_year = 12;

let amount = principal * Math.pow(1 + rate / compounds_per_year, compounds_per_year * time);
let interest = amount - principal;

console.log("Principal: $" + principal);
console.log("Final Amount: $" + amount.toFixed(2));
console.log("Interest Earned: $" + interest.toFixed(2));
```

### Algorithm 4: Geometric Calculations

```
// Algorithm: Calculate Geometric Properties
let radius = 5;
let side = 4;
let base = 6;
let height = 8;

let circle_area = Math.PI * radius * radius;
let circle_circumference = 2 * Math.PI * radius;
let square_area = side * side;
let square_perimeter = 4 * side;
let triangle_area = 0.5 * base * height;

console.log("Circle - Area: " + circle_area.toFixed(2) + ", Circumference: " + circle_circumference.toFixed(2));
console.log("Square - Area: " + square_area + ", Perimeter: " + square_perimeter);
console.log("Triangle - Area: " + triangle_area);
```

### Algorithm 5: Physics Formula Calculator

```
// Algorithm: Physics Calculations
let mass = 5.5;
let velocity = 10;
let acceleration = 9.8;
let time = 3;

let kinetic_energy = 0.5 * mass * velocity * velocity;
let force = mass * acceleration;
let distance = velocity * time + 0.5 * acceleration * time * time;
let momentum = mass * velocity;

console.log("Kinetic Energy: " + kinetic_energy);
console.log("Force: " + force);
console.log("Distance: " + distance);
console.log("Momentum: " + momentum);
```

### Algorithm 6: Temperature Conversion with Multiple Formulas

```
// Algorithm: Multiple Temperature Conversions
let celsius = 25;
let fahrenheit = celsius * 9 / 5 + 32;
let kelvin = celsius + 273.15;
let celsius_from_f = (fahrenheit - 32) * 5 / 9;
let celsius_from_k = kelvin - 273.15;

console.log("Celsius: " + celsius);
console.log("Fahrenheit: " + fahrenheit);
console.log("Kelvin: " + kelvin);
console.log("F to C: " + celsius_from_f);
console.log("K to C: " + celsius_from_k);
```

### Algorithm 7: Statistical Calculations

```
// Algorithm: Calculate Statistics for Three Numbers
let num1 = 10;
let num2 = 20;
let num3 = 30;

let sum = num1 + num2 + num3;
let average = sum / 3;
let range = num3 - num1; // assuming num3 is largest, num1 is smallest
let sum_of_squares = num1 * num1 + num2 * num2 + num3 * num3;
let mean_of_squares = sum_of_squares / 3;
let variance = mean_of_squares - average * average;
let std_deviation = Math.sqrt(variance);

console.log("Sum: " + sum);
console.log("Average: " + average);
console.log("Range: " + range);
console.log("Variance: " + variance);
console.log("Standard Deviation: " + std_deviation.toFixed(2));
```

### Mathematical Operation Translation Patterns

| Pseudocode | JavaScript |
|------------|------------|
| `SET result TO a + b` | `result = a + b;` |
| `SET result TO a - b` | `result = a - b;` |
| `SET result TO a * b` | `result = a * b;` |
| `SET result TO a / b` | `result = a / b;` |
| `SET result TO POWER(a, b)` | `result = Math.pow(a, b);` or `result = a ** b;` |
| `SET result TO SQRT(a)` | `result = Math.sqrt(a);` |
| `SET result TO ROUND(a)` | `result = Math.round(a);` |
| `USE PI` | `Math.PI` |

### Important Notes

**Operator Precedence**: JavaScript follows the standard mathematical order of operations (PEMDAS/BODMAS).

**Floating Point Precision**: Be aware that JavaScript uses floating-point arithmetic which can lead to small precision errors in calculations.

**Math Library**: JavaScript's Math library provides many useful mathematical functions for complex calculations.

---

 **Excellent work! You've mastered translating mathematical operations from pseudocode to JavaScript!**

*Next up: Input/Output operations in pseudocode!*


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic
