# Level 3: Mathematical Pseudocode

> **LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.c\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Mathematics is the language of algorithms! Today you'll translate mathematical concepts, formulas, and calculations from pseudocode into C programs. You'll work with geometry, finance, sequences, and complex mathematical operations.

---

### Learning Goals

- [ ] Translate mathematical formulas into C code
- [ ] Understand order of operations in algorithms
- [ ] Implement geometric calculations (area, volume, perimeter)
- [ ] Create financial calculation programs
- [ ] Work with mathematical series and sequences
- [ ] Handle complex mathematical expressions

---

### Mathematical Concepts in Programming

**Common Mathematical Operations:**
- [ ] **Arithmetic**: +, -, ×, ÷, exponents, roots
- [ ] **Geometry**: Area, perimeter, volume, surface area
- [ ] **Finance**: Interest, loans, investments
- [ ] **Statistics**: Average, percentage, ratios
- [ ] **Sequences**: Series, patterns, progressions

---

### Your Task

**Translate each mathematical pseudocode algorithm into working C code.**

---

## Algorithm 1: Geometry Calculator

**Pseudocode:**
```cpp
Algorithm: Calculate Circle Properties
1. Display "Circle Calculator"
2. Display "Enter radius: "
3. Get radius from user
4. Calculate area = π × radius²
5. Calculate circumference = 2 × π × radius
6. Calculate diameter = 2 × radius
7. Display "Radius: " + radius
8. Display "Diameter: " + diameter
9. Display "Area: " + area
10. Display "Circumference: " + circumference
```cpp

**Mathematical Notes:**
- [ ] π (pi) ≈ 3.14159
- [ ] Area formula: A = πr²
- [ ] Circumference formula: C = 2πr
- [ ] Use `3.14159` for π in calculations

**Your Task:** Create a circle geometry calculator.

---

## Algorithm 2: Right Triangle Solver

**Pseudocode:**
```cpp
Algorithm: Solve Right Triangle
1. Display "Right Triangle Calculator"
2. Display "Enter side A: "
3. Get side_a from user
4. Display "Enter side B: "
5. Get side_b from user
6. Calculate hypotenuse = √(side_a² + side_b²)
7. Calculate area = (side_a × side_b) ÷ 2
8. Calculate perimeter = side_a + side_b + hypotenuse
9. Display "Side A: " + side_a
10. Display "Side B: " + side_b
11. Display "Hypotenuse: " + hypotenuse
12. Display "Area: " + area
13. Display "Perimeter: " + perimeter
```cpp

**Mathematical Notes:**
- [ ] Pythagorean theorem: c² = a² + b² (where c is hypotenuse)
- [ ] Area formula: A = (ab)/2
- [ ] Need square root function: `sqrt()` from `<math.h>`

**Your Task:** Build a right triangle calculator.

---

## Algorithm 3: Compound Interest Calculator

**Pseudocode:**
```cpp
Algorithm: Calculate Compound Interest
1. Display "Compound Interest Calculator"
2. Display "Enter principal amount: $"
3. Get principal from user
4. Display "Enter annual interest rate (%): "
5. Get rate from user
6. Display "Enter number of years: "
7. Get years from user
8. Display "Enter compounding frequency (1=annual, 12=monthly): "
9. Get frequency from user
10. Calculate rate_decimal = rate ÷ 100
11. Calculate total_compounds = years × frequency
12. Calculate compound_rate = rate_decimal ÷ frequency
13. Calculate final_amount = principal × (1 + compound_rate)^total_compounds
14. Calculate total_interest = final_amount - principal
15. Display "Principal: $" + principal
16. Display "Final Amount: $" + final_amount
17. Display "Total Interest: $" + total_interest
```cpp

**Mathematical Notes:**
- [ ] Compound interest formula: A = P(1 + r/n)^(nt)
- [ ] Where: P = principal, r = rate, n = frequency, t = years
- [ ] Need power function: `pow()` from `<math.h>`

**Your Task:** Create a compound interest calculator.

---

## Algorithm 4: Quadratic Equation Solver

**Pseudocode:**
```cpp
Algorithm: Solve Quadratic Equation
1. Display "Quadratic Equation Solver"
2. Display "For equation ax² + bx + c = 0"
3. Display "Enter coefficient a: "
4. Get a from user
5. Display "Enter coefficient b: "
6. Get b from user
7. Display "Enter coefficient c: "
8. Get c from user
9. Calculate discriminant = b² - 4ac
10. If discriminant > 0:
   a. Calculate root1 = (-b + √discriminant) ÷ (2a)
   b. Calculate root2 = (-b - √discriminant) ÷ (2a)
   c. Display "Two real roots: " + root1 + " and " + root2
11. Else if discriminant = 0:
   a. Calculate root = -b ÷ (2a)
   b. Display "One real root: " + root
12. Else:
   a. Display "No real roots (complex solutions)"
13. Display "Discriminant: " + discriminant
```cpp

**Mathematical Notes:**
- [ ] Quadratic formula: x = [-b ± √(b² - 4ac)] / 2a
- [ ] Discriminant D = b² - 4ac determines number of roots
- [ ] D > 0: Two real roots, D = 0: One root, D < 0: Complex roots

**Your Task:** Build a quadratic equation solver.

---

## Algorithm 5: Fibonacci Sequence Generator

**Pseudocode:**
```cpp
Algorithm: Generate Fibonacci Sequence
1. Display "Fibonacci Sequence Generator"
2. Display "Enter number of terms: "
3. Get n from user
4. Initialize first = 0
5. Initialize second = 1
6. Display "Fibonacci sequence:"
7. If n >= 1:
   a. Display first
8. If n >= 2:
   a. Display second
9. Initialize count = 3
10. While count <= n:
   a. Calculate next = first + second
   b. Display next
   c. Set first = second
   d. Set second = next
   e. Add 1 to count
11. Display "Sequence complete"
```cpp

**Mathematical Notes:**
- [ ] Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
- [ ] Each term is sum of previous two terms
- [ ] F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)

**Your Task:** Create a Fibonacci sequence generator.

---

## Algorithm 6: Statistical Calculator

**Pseudocode:**
```cpp
Algorithm: Calculate Statistics
1. Display "Statistical Calculator"
2. Initialize sum = 0
3. Initialize count = 0
4. Initialize sum_squares = 0
5. Initialize has_more = true
6. While has_more is true:
   a. Display "Enter number " + (count + 1) + " (or 0 to finish): "
   b. Get number from user
   c. If number equals 0:
      i. Set has_more to false
   d. Else:
      i. Add number to sum
      ii. Add 1 to count
      iii. Add (number × number) to sum_squares
7. If count > 0:
   a. Calculate mean = sum ÷ count
   b. Calculate variance = (sum_squares ÷ count) - (mean × mean)
   c. Calculate standard_deviation = √variance
   d. Display "Count: " + count
   e. Display "Sum: " + sum
   f. Display "Mean: " + mean
   g. Display "Standard Deviation: " + standard_deviation
8. Else:
   a. Display "No numbers entered"
```cpp

**Mathematical Notes:**
- [ ] Mean (average): μ = Σx / n
- [ ] Variance: σ² = (Σx² / n) - μ²
- [ ] Standard deviation: σ = √variance
- [ ] Need square root function for standard deviation

**Your Task:** Build a statistical calculator.

---

## Algorithm 7: Distance Calculator (Coordinate Geometry)

**Pseudocode:**
```cpp
Algorithm: Calculate Distance Between Points
1. Display "Distance Between Two Points"
2. Display "Enter coordinates for point 1:"
3. Display "X1: "
4. Get x1 from user
5. Display "Y1: "
6. Get y1 from user
7. Display "Enter coordinates for point 2:"
8. Display "X2: "
9. Get x2 from user
10. Display "Y2: "
11. Get y2 from user
12. Calculate delta_x = x2 - x1
13. Calculate delta_y = y2 - y1
14. Calculate distance = √(delta_x² + delta_y²)
15. Display "Point 1: (" + x1 + ", " + y1 + ")"
16. Display "Point 2: (" + x2 + ", " + y2 + ")"
17. Display "Distance: " + distance
```cpp

**Mathematical Notes:**
- [ ] Distance formula: d = √[(x₂ - x₁)² + (y₂ - y₁)²]
- [ ] Works for any two points in 2D coordinate plane
- [ ] Can be extended to 3D: d = √[(x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²]

**Your Task:** Create a coordinate distance calculator.

---

### Mathematical Functions in C

**Required Headers:**
```c
#include <stdio.h>
# include <math.h>  // For mathematical functions
```cpp

**Common Math Functions:**
- [ ] `sqrt(x)` - Square root
- [ ] `pow(x, y)` - Power (x^y)
- [ ] `fabs(x)` - Absolute value (float)
- [ ] `ceil(x)` - Ceiling (round up)
- [ ] `floor(x)` - Floor (round down)

---

### Success Checklist

**For Each Algorithm:**
- [ ] Included necessary headers (`<math.h>` for math functions)
- [ ] Used correct mathematical formulas
- [ ] Handled order of operations properly
- [ ] Used appropriate data types (float for decimals)
- [ ] Provided clear output formatting

**Mathematical Accuracy:**
- [ ] Implemented formulas correctly
- [ ] Used proper operator precedence
- [ ] Handled potential division by zero
- [ ] Used correct constants (π, etc.)

---

### Try This (Optional Challenges)

1. **Add Input Validation**: Check for negative radii, valid coefficients
2. **Extended Features**: Add more geometric shapes, loan amortization
3. **Multiple Calculations**: Allow calculating multiple equations in one run
4. **Save Results**: Store calculation history

---

## Mathematical Formula Reference

### Geometry Formulas
| Shape | Area | Perimeter/Circumference |
|-------|------|------------------------|
| Circle | πr² | 2πr |
| Rectangle | length × width | 2(length + width) |
| Triangle | (base × height) ÷ 2 | a + b + c |
| Square | side² | 4 × side |

### Financial Formulas
| Concept | Formula | Variables |
|---------|---------|-----------|
| Simple Interest | P × r × t | P=principal, r=rate, t=time |
| Compound Interest | P(1 + r/n)^(nt) | n=compounding frequency |
| Loan Payment | P × r(1+r)^n / ((1+r)^n - 1) | Monthly payment calculation |

### Statistical Formulas
| Measure | Formula | Description |
|---------|---------|-------------|
| Mean | Σx / n | Average value |
| Variance | Σ(x-μ)² / n | Spread of data |
| Standard Deviation | √variance | Typical deviation from mean |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Geometry Calculator

```c
#include <stdio.h>

int main() {
    float radius, area, circumference, diameter;
    const float PI = 3.14159;
    
    printf("Circle Calculator\n");
    printf("Enter radius: ");
    scanf("%f", &radius);
    
    area = PI * radius * radius;
    circumference = 2 * PI * radius;
    diameter = 2 * radius;
    
    printf("Radius: %.2f\n", radius);
    printf("Diameter: %.2f\n", diameter);
    printf("Area: %.2f\n", area);
    printf("Circumference: %.2f\n", circumference);
    
    return 0;
}
```cpp

**Key Concepts:**
- [ ] Constant PI defined as `const float`
- [ ] Order of operations: multiplication before addition
- [ ] Float precision for decimal results

---

### Algorithm 2: Right Triangle Solver

```c
#include <stdio.h>
# include <math.h>

int main() {
    float side_a, side_b, hypotenuse, area, perimeter;
    
    printf("Right Triangle Calculator\n");
    printf("Enter side A: ");
    scanf("%f", &side_a);
    printf("Enter side B: ");
    scanf("%f", &side_b);
    
    hypotenuse = sqrt(side_a * side_a + side_b * side_b);
    area = (side_a * side_b) / 2;
    perimeter = side_a + side_b + hypotenuse;
    
    printf("Side A: %.2f\n", side_a);
    printf("Side B: %.2f\n", side_b);
    printf("Hypotenuse: %.2f\n", hypotenuse);
    printf("Area: %.2f\n", area);
    printf("Perimeter: %.2f\n", perimeter);
    
    return 0;
}
```cpp

**Key Concepts:**
- [ ] `#include <math.h>` for `sqrt()` function
- [ ] Pythagorean theorem implementation
- [ ] Proper parentheses for order of operations

---

### Algorithm 3: Compound Interest Calculator

```c
#include <stdio.h>
# include <math.h>

int main() {
    float principal, rate, years, frequency;
    float rate_decimal, total_compounds, compound_rate, final_amount, total_interest;
    
    printf("Compound Interest Calculator\n");
    printf("Enter principal amount: $");
    scanf("%f", &principal);
    printf("Enter annual interest rate (%%): ");
    scanf("%f", &rate);
    printf("Enter number of years: ");
    scanf("%f", &years);
    printf("Enter compounding frequency (1=annual, 12=monthly): ");
    scanf("%f", &frequency);
    
    rate_decimal = rate / 100;
    total_compounds = years * frequency;
    compound_rate = rate_decimal / frequency;
    
    final_amount = principal * pow(1 + compound_rate, total_compounds);
    total_interest = final_amount - principal;
    
    printf("Principal: $%.2f\n", principal);
    printf("Final Amount: $%.2f\n", final_amount);
    printf("Total Interest: $%.2f\n", total_interest);
    
    return 0;
}
```cpp

**Key Concepts:**
- [ ] Complex compound interest formula
- [ ] `pow()` function for exponentiation
- [ ] Multiple intermediate calculations

---

### Algorithm 4: Quadratic Equation Solver

```c
#include <stdio.h>
# include <math.h>

int main() {
    float a, b, c, discriminant, root1, root2, root;
    
    printf("Quadratic Equation Solver\n");
    printf("For equation ax² + bx + c = 0\n");
    printf("Enter coefficient a: ");
    scanf("%f", &a);
    printf("Enter coefficient b: ");
    scanf("%f", &b);
    printf("Enter coefficient c: ");
    scanf("%f", &c);
    
    discriminant = b * b - 4 * a * c;
    
    printf("Discriminant: %.2f\n", discriminant);
    
    if (discriminant > 0) {
        root1 = (-b + sqrt(discriminant)) / (2 * a);
        root2 = (-b - sqrt(discriminant)) / (2 * a);
        printf("Two real roots: %.2f and %.2f\n", root1, root2);
    } else if (discriminant == 0) {
        root = -b / (2 * a);
        printf("One real root: %.2f\n", root);
    } else {
        printf("No real roots (complex solutions)\n");
    }
    
    return 0;
}
```cpp

**Key Concepts:**
- [ ] Discriminant determines number of roots
- [ ] Proper handling of three cases
- [ ] Careful with parentheses in quadratic formula

---

### Algorithm 5: Fibonacci Sequence Generator

```c
#include <stdio.h>

int main() {
    int n, first = 0, second = 1, next, count = 3;
    
    printf("Fibonacci Sequence Generator\n");
    printf("Enter number of terms: ");
    scanf("%d", &n);
    
    printf("Fibonacci sequence:\n");
    
    if (n >= 1) {
        printf("%d ", first);
    }
    if (n >= 2) {
        printf("%d ", second);
    }
    
    while (count <= n) {
        next = first + second;
        printf("%d ", next);
        
        first = second;
        second = next;
        count++;
    }
    
    printf("\nSequence complete\n");
    
    return 0;
}
```cpp

**Key Concepts:**
- [ ] Iterative Fibonacci calculation
- [ ] Variable swapping technique
- [ ] Handling edge cases (n >= 1, n >= 2)

---

### Algorithm 6: Statistical Calculator

```c
#include <stdio.h>
# include <math.h>

int main() {
    float sum = 0, sum_squares = 0, number, mean, variance, std_dev;
    int count = 0, has_more = 1;
    
    printf("Statistical Calculator\n");
    
    while (has_more) {
        printf("Enter number %d (or 0 to finish): ", count + 1);
        scanf("%f", &number);
        
        if (number == 0) {
            has_more = 0;
        } else {
            sum += number;
            count++;
            sum_squares += number * number;
        }
    }
    
    if (count > 0) {
        mean = sum / count;
        variance = (sum_squares / count) - (mean * mean);
        std_dev = sqrt(variance);
        
        printf("Count: %d\n", count);
        printf("Sum: %.2f\n", sum);
        printf("Mean: %.2f\n", mean);
        printf("Standard Deviation: %.2f\n", std_dev);
    } else {
        printf("No numbers entered\n");
    }
    
    return 0;
}
```cpp

**Key Concepts:**
- [ ] Statistical formulas implementation
- [ ] Accumulation of sum and sum of squares
- [ ] Variance and standard deviation calculations

---

### Algorithm 7: Distance Calculator

```c
#include <stdio.h>
# include <math.h>

int main() {
    float x1, y1, x2, y2, delta_x, delta_y, distance;
    
    printf("Distance Between Two Points\n");
    printf("Enter coordinates for point 1:\n");
    printf("X1: ");
    scanf("%f", &x1);
    printf("Y1: ");
    scanf("%f", &y1);
    
    printf("Enter coordinates for point 2:\n");
    printf("X2: ");
    scanf("%f", &x2);
    printf("Y2: ");
    scanf("%f", &y2);
    
    delta_x = x2 - x1;
    delta_y = y2 - y1;
    distance = sqrt(delta_x * delta_x + delta_y * delta_y);
    
    printf("Point 1: (%.2f, %.2f)\n", x1, y1);
    printf("Point 2: (%.2f, %.2f)\n", x2, y2);
    printf("Distance: %.2f\n", distance);
    
    return 0;
}
```cpp

**Key Concepts:**
- [ ] Distance formula implementation
- [ ] Delta calculations (differences)
- [ ] Pythagorean distance in 2D plane

---

### Mathematical Constants and Precision

**Common Constants:**
```c
const float PI = 3.14159265359;
const float E = 2.71828182846;
const float GRAVITY = 9.80665;
```cpp

**Precision Considerations:**
- [ ] Use `double` for high-precision calculations
- [ ] Be aware of floating-point limitations
- [ ] Consider significant digits in output

### Common Mathematical Errors

**Operator Precedence:**
```c
// Wrong: 2 + 3 * 4 = 14 (multiplication first)
result = 2 + 3 * 4;

// Correct: (2 + 3) * 4 = 20 (parentheses force addition first)
result = (2 + 3) * 4;
```cpp

**Integer Division:**
```c
// Wrong: 5 / 2 = 2 (integer division)
float result = 5 / 2;

// Correct: 5.0 / 2 = 2.5 (float division)
float result = 5.0 / 2;
```cpp

**Power Operations:**
```c
// Wrong: Can't use ^ for power in C
result = 2 ^ 3;  // Bitwise XOR, not power!

// Correct: Use pow() function
result = pow(2, 3);  // 2^3 = 8
```cpp

---

 **Fantastic! You've mastered mathematical algorithms in code!** 

*Mathematics and programming are perfect partners. Next: Input/Output operations in pseudocode! *

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

```cpp
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard C++ conventions with proper imports and main function
2. **Output**: Uses printf to print messages to the console
3. **Standard Library**: Includes stdio.h for input/output operations
4. **Return Value**: Returns 0 to indicate successful execution
5. **Best Practices**: Code is readable and uses C++ idioms

### Testing Your Solution

1. **Compile**: `gcc main.c -o main`
2. **Run**: `./hello`
3. **Expected Output**: `Hello, World!`

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `command not found: gcc` | Compiler not installed | `sudo apt install gcc` (Ubuntu) |
| `undefined reference to main` | Missing main function | Ensure `int main()` exists |
| `error: implicit declaration of function 'printf'` | Missing stdio.h | Add `#include <stdio.h>` |

### Tips for Learning

- C uses stdio.h for input/output with additional features
- `printf` is the C standard for formatted output
- `\n` adds a newline character in format strings
- Format specifiers control how data is displayed (%d, %f, %s, etc.)
