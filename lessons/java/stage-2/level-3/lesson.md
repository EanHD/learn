# Level 3: Mathematical Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`Main.java` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Mathematics is the language of algorithms! Today you'll translate mathematical concepts, formulas, and calculations from pseudocode into Java programs. You'll work with geometry, finance, sequences, and complex mathematical operations.

---

### Learning Goals

- Translate mathematical formulas into Java code
- Understand order of operations in algorithms
- Implement geometric calculations (area, volume, perimeter)
- Create financial calculation programs
- Work with mathematical series and sequences
- Handle complex mathematical expressions

---

### Mathematical Concepts in Programming

**Common Mathematical Operations:**
- **Arithmetic**: +, -, ×, ÷, exponents, roots
- **Geometry**: Area, perimeter, volume, surface area
- **Finance**: Interest, loans, investments
- **Statistics**: Average, percentage, ratios
- **Sequences**: Series, patterns, progressions

---

### Your Task

**Translate each mathematical pseudocode algorithm into working Java code.**

---


### How to Compile and Run

1. **Compile the code**:
   ```bash
   javac hello.java
   ```

2. **Run your program**:
   ```bash
   java hello
   ```

**Expected output:**
```java
Hello, World!
```java

## Algorithm 1: Geometry Calculator

**Pseudocode:**
```java
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
```java

**Mathematical Notes:**
- π (pi) ≈ 3.14159 (or use `Math.PI`)
- Area formula: A = πr²
- Circumference formula: C = 2πr

**Your Task:** Create a circle geometry calculator.

---

## Algorithm 2: Right Triangle Solver

**Pseudocode:**
```java
Algorithm: Solve Right Triangle
1. Display "Right Triangle Calculator"
2. Display "Enter side A: "
3. Get sideA from user
4. Display "Enter side B: "
5. Get sideB from user
6. Calculate hypotenuse = √(sideA² + sideB²)
7. Calculate area = (sideA × sideB) ÷ 2
8. Calculate perimeter = sideA + sideB + hypotenuse
9. Display "Side A: " + sideA
10. Display "Side B: " + sideB
11. Display "Hypotenuse: " + hypotenuse
12. Display "Area: " + area
13. Display "Perimeter: " + perimeter
```java

**Mathematical Notes:**
- Pythagorean theorem: c² = a² + b² (where c is hypotenuse)
- Area formula: A = (ab)/2
- Use `Math.sqrt()` for square root

**Your Task:** Build a right triangle calculator.

---

## Algorithm 3: Compound Interest Calculator

**Pseudocode:**
```java
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
10. Calculate rateDecimal = rate ÷ 100
11. Calculate totalCompounds = years × frequency
12. Calculate compoundRate = rateDecimal ÷ frequency
13. Calculate finalAmount = principal × (1 + compoundRate)^totalCompounds
14. Calculate totalInterest = finalAmount - principal
15. Display "Principal: $" + principal
16. Display "Final Amount: $" + finalAmount
17. Display "Total Interest: $" + totalInterest
```java

**Mathematical Notes:**
- Compound interest formula: A = P(1 + r/n)^(nt)
- Where: P = principal, r = rate, n = frequency, t = years
- Use `Math.pow()` for exponentiation

**Your Task:** Create a compound interest calculator.

---

## Algorithm 4: Quadratic Equation Solver

**Pseudocode:**
```java
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
```java

**Mathematical Notes:**
- Quadratic formula: x = [-b ± √(b² - 4ac)] / 2a
- Discriminant D = b² - 4ac determines number of roots
- D > 0: Two real roots, D = 0: One root, D < 0: Complex roots

**Your Task:** Build a quadratic equation solver.

---

## Algorithm 5: Fibonacci Sequence Generator

**Pseudocode:**
```java
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
```java

**Mathematical Notes:**
- Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
- Each term is sum of previous two terms
- F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)

**Your Task:** Create a Fibonacci sequence generator.

---

## Algorithm 6: Statistical Calculator

**Pseudocode:**
```java
Algorithm: Calculate Statistics
1. Display "Statistical Calculator"
2. Initialize sum = 0
3. Initialize count = 0
4. Initialize sumSquares = 0
5. Initialize hasMore = true
6. While hasMore is true:
   a. Display "Enter number " + (count + 1) + " (or 0 to finish): "
   b. Get number from user
   c. If number equals 0:
      i. Set hasMore to false
   d. Else:
      i. Add number to sum
      ii. Add 1 to count
      iii. Add (number × number) to sumSquares
7. If count > 0:
   a. Calculate mean = sum ÷ count
   b. Calculate variance = (sumSquares ÷ count) - (mean × mean)
   c. Calculate standardDeviation = √variance
   d. Display "Count: " + count
   e. Display "Sum: " + sum
   f. Display "Mean: " + mean
   g. Display "Standard Deviation: " + standardDeviation
8. Else:
   a. Display "No numbers entered"
```java

**Mathematical Notes:**
- Mean (average): μ = Σx / n
- Variance: σ² = (Σx² / n) - μ²
- Standard deviation: σ = √variance

**Your Task:** Build a statistical calculator.

---

## Algorithm 7: Distance Calculator (Coordinate Geometry)

**Pseudocode:**
```java
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
12. Calculate deltaX = x2 - x1
13. Calculate deltaY = y2 - y1
14. Calculate distance = √(deltaX² + deltaY²)
15. Display "Point 1: (" + x1 + ", " + y1 + ")"
16. Display "Point 2: (" + x2 + ", " + y2 + ")"
17. Display "Distance: " + distance
```java

**Mathematical Notes:**
- Distance formula: d = √[(x₂ - x₁)² + (y₂ - y₁)²]
- Works for any two points in 2D coordinate plane
- Can be extended to 3D

**Your Task:** Create a coordinate distance calculator.

---

### Mathematical Functions in Java

**Available in Math class:**
- `Math.sqrt(x)` - Square root
- `Math.pow(x, y)` - Power (x^y)
- `Math.abs(x)` - Absolute value
- `Math.ceil(x)` - Ceiling (round up)
- `Math.floor(x)` - Floor (round down)
- `Math.PI` - π constant (3.14159...)

---

### Success Checklist

**For Each Algorithm:**
- [ ] Used Math class for mathematical functions
- [ ] Applied correct mathematical formulas
- [ ] Handled order of operations properly
- [ ] Used appropriate data types (double for decimals)
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

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Circle Calculator");
        System.out.print("Enter radius: ");
        double radius = scanner.nextDouble();
        
        double area = Math.PI * radius * radius;
        double circumference = 2 * Math.PI * radius;
        double diameter = 2 * radius;
        
        System.out.printf("Radius: %.2f\n", radius);
        System.out.printf("Diameter: %.2f\n", diameter);
        System.out.printf("Area: %.2f\n", area);
        System.out.printf("Circumference: %.2f\n", circumference);
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- `Math.PI` constant for π
- Order of operations: multiplication before addition
- `double` for precision with decimals

**Java Advantages:**
- Built-in `Math.PI` (more accurate than 3.14159)
- No need to declare constant separately

---

### Algorithm 2: Right Triangle Solver

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Right Triangle Calculator");
        System.out.print("Enter side A: ");
        double sideA = scanner.nextDouble();
        System.out.print("Enter side B: ");
        double sideB = scanner.nextDouble();
        
        double hypotenuse = Math.sqrt(sideA * sideA + sideB * sideB);
        double area = (sideA * sideB) / 2;
        double perimeter = sideA + sideB + hypotenuse;
        
        System.out.printf("Side A: %.2f\n", sideA);
        System.out.printf("Side B: %.2f\n", sideB);
        System.out.printf("Hypotenuse: %.2f\n", hypotenuse);
        System.out.printf("Area: %.2f\n", area);
        System.out.printf("Perimeter: %.2f\n", perimeter);
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- `Math.sqrt()` for square root function
- Pythagorean theorem implementation
- Proper parentheses for order of operations

**Java Notes:**
- No need to import `java.lang.Math` (automatically available)
- Can also write: `Math.pow(sideA, 2)` instead of `sideA * sideA`

---

### Algorithm 3: Compound Interest Calculator

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Compound Interest Calculator");
        System.out.print("Enter principal amount: $");
        double principal = scanner.nextDouble();
        System.out.print("Enter annual interest rate (%): ");
        double rate = scanner.nextDouble();
        System.out.print("Enter number of years: ");
        double years = scanner.nextDouble();
        System.out.print("Enter compounding frequency (1=annual, 12=monthly): ");
        double frequency = scanner.nextDouble();
        
        double rateDecimal = rate / 100;
        double totalCompounds = years * frequency;
        double compoundRate = rateDecimal / frequency;
        
        double finalAmount = principal * Math.pow(1 + compoundRate, totalCompounds);
        double totalInterest = finalAmount - principal;
        
        System.out.printf("Principal: $%.2f\n", principal);
        System.out.printf("Final Amount: $%.2f\n", finalAmount);
        System.out.printf("Total Interest: $%.2f\n", totalInterest);
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Complex compound interest formula
- `Math.pow()` for exponentiation (base, exponent)
- Multiple intermediate calculations for clarity

**Financial Note:**
- Always use `double` for monetary calculations
- Format currency with `printf("$%.2f")` for 2 decimal places

---

### Algorithm 4: Quadratic Equation Solver

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Quadratic Equation Solver");
        System.out.println("For equation ax² + bx + c = 0");
        System.out.print("Enter coefficient a: ");
        double a = scanner.nextDouble();
        System.out.print("Enter coefficient b: ");
        double b = scanner.nextDouble();
        System.out.print("Enter coefficient c: ");
        double c = scanner.nextDouble();
        
        double discriminant = b * b - 4 * a * c;
        
        System.out.printf("Discriminant: %.2f\n", discriminant);
        
        if (discriminant > 0) {
            double root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
            double root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
            System.out.printf("Two real roots: %.2f and %.2f\n", root1, root2);
        } else if (discriminant == 0) {
            double root = -b / (2 * a);
            System.out.printf("One real root: %.2f\n", root);
        } else {
            System.out.println("No real roots (complex solutions)");
        }
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Discriminant determines number of roots
- Proper handling of three cases
- Careful with parentheses in quadratic formula

**Mathematical Logic:**
- Check discriminant first to determine root type
- Avoid square root of negative numbers (no real solution)

---

### Algorithm 5: Fibonacci Sequence Generator

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Fibonacci Sequence Generator");
        System.out.print("Enter number of terms: ");
        int n = scanner.nextInt();
        
        int first = 0, second = 1, count = 3;
        
        System.out.println("Fibonacci sequence:");
        
        if (n >= 1) {
            System.out.print(first + " ");
        }
        if (n >= 2) {
            System.out.print(second + " ");
        }
        
        while (count <= n) {
            int next = first + second;
            System.out.print(next + " ");
            
            first = second;
            second = next;
            count++;
        }
        
        System.out.println("\nSequence complete");
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Iterative Fibonacci calculation
- Variable swapping technique
- Handling edge cases (n >= 1, n >= 2)

**Algorithm Efficiency:**
- This iterative approach is O(n) time complexity
- Much better than recursive version for large n
- Uses only 3 variables (memory efficient)

---

### Algorithm 6: Statistical Calculator

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        double sum = 0, sumSquares = 0;
        int count = 0;
        boolean hasMore = true;
        
        System.out.println("Statistical Calculator");
        
        while (hasMore) {
            System.out.print("Enter number " + (count + 1) + " (or 0 to finish): ");
            double number = scanner.nextDouble();
            
            if (number == 0) {
                hasMore = false;
            } else {
                sum += number;
                count++;
                sumSquares += number * number;
            }
        }
        
        if (count > 0) {
            double mean = sum / count;
            double variance = (sumSquares / count) - (mean * mean);
            double stdDev = Math.sqrt(variance);
            
            System.out.println("Count: " + count);
            System.out.printf("Sum: %.2f\n", sum);
            System.out.printf("Mean: %.2f\n", mean);
            System.out.printf("Standard Deviation: %.2f\n", stdDev);
        } else {
            System.out.println("No numbers entered");
        }
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Statistical formulas implementation
- Accumulation of sum and sum of squares
- Variance and standard deviation calculations

**Statistical Notes:**
- Mean = average value
- Variance measures data spread
- Standard deviation = square root of variance

---

### Algorithm 7: Distance Calculator

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Distance Between Two Points");
        
        System.out.println("Enter coordinates for point 1:");
        System.out.print("X1: ");
        double x1 = scanner.nextDouble();
        System.out.print("Y1: ");
        double y1 = scanner.nextDouble();
        
        System.out.println("Enter coordinates for point 2:");
        System.out.print("X2: ");
        double x2 = scanner.nextDouble();
        System.out.print("Y2: ");
        double y2 = scanner.nextDouble();
        
        double deltaX = x2 - x1;
        double deltaY = y2 - y1;
        double distance = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
        
        System.out.println("Point 1: (" + x1 + ", " + y1 + ")");
        System.out.println("Point 2: (" + x2 + ", " + y2 + ")");
        System.out.printf("Distance: %.2f\n", distance);
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Distance formula in coordinate geometry
- Breaking formula into steps (deltaX, deltaY)
- Clean formatting of coordinate output

**Geometric Insight:**
- This is essentially Pythagorean theorem
- Horizontal distance = |x2 - x1|
- Vertical distance = |y2 - y1|
- Diagonal distance = √(horizontal² + vertical²)

---

### Common Math Mistakes in Java

**Integer Division:**
```java
int result = 5 / 2;  // Result: 2 (not 2.5!)
double result = 5.0 / 2;  // Result: 2.5 
```java

**Parentheses Matter:**
```java
double wrong = 1 + 2 * 3;  // 7 (multiplication first)
double right = (1 + 2) * 3;  // 9 (parentheses first)
```java

**Power vs Multiplication:**
```java
double wrong = x * 2;  // This is x × 2, not x²
double right = x * x;  // This is x²
double alsoRight = Math.pow(x, 2);  // Also x²
```java

---

### Math Class Quick Reference

```java
// Constants
Math.PI          // 3.14159265358979323846
Math.E           // 2.71828182845904523536

// Power and Root
Math.pow(2, 3)   // 8.0 (2³)
Math.sqrt(16)    // 4.0 (√16)
Math.cbrt(27)    // 3.0 (∛27)

// Rounding
Math.ceil(4.2)   // 5.0 (round up)
Math.floor(4.8)  // 4.0 (round down)
Math.round(4.5)  // 5 (nearest integer)

// Absolute and Sign
Math.abs(-5)     // 5 (absolute value)
Math.max(3, 7)   // 7 (maximum)
Math.min(3, 7)   // 3 (minimum)

// Trigonometry (radians)
Math.sin(x)
Math.cos(x)
Math.tan(x)
```java

---

**Excellent! You've mastered mathematical pseudocode translation in Java!**

*Mathematics + Programming = Powerful Problem Solving. Next: Input/Output operations!*
