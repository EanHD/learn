# Level 3: Mathematical Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Welcome to Level 3! Today we're focusing on mathematical operations in pseudocode. You'll learn to translate complex mathematical formulas and calculations from pseudocode into working Go code, and understand operator precedence in algorithmic calculations.

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

**For each pseudocode algorithm below, translate it into working Go code. Pay special attention to operator precedence and mathematical formula accuracy.**

---


### How to Run

1. **Run the code**:
   ```
   go run hello.go
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

**Your Task:** Create a Go program that evaluates complex arithmetic expressions.

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

**Your Task:** Create a Go program that solves quadratic equations using the quadratic formula.

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

**Your Task:** Create a Go program that calculates compound interest.

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

**Your Task:** Create a Go program that calculates geometric properties.

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

**Your Task:** Create a Go program that calculates physics formulas.

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

**Your Task:** Create a Go program that performs multiple temperature conversions.

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

**Your Task:** Create a Go program that calculates statistical measures.

---

### Key Concepts for Mathematical Operations

**Operator Precedence in Go:**
- Parentheses `()`
- Multiplication `*`, Division `/`, Modulus `%`, and others (left to right)
- Addition `+`, Subtraction `-` (left to right)

**Mathematical Functions:**
- `math.Sqrt(x)` - Square root
- `math.Pow(base, exponent)` - Power
- `math.Floor(x)` - Round down
- `math.Ceil(x)` - Round up
- `math.Pi` - Pi constant
- Go requires importing the `math` package for mathematical functions

---

### Success Checklist

**For Each Algorithm:**
- [ ] Mathematical formulas correctly translated from pseudocode
- [ ] Operator precedence properly observed
- [ ] Program compiles and runs without errors
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
3. **Enhance Algorithm 7**: Calculate standard deviation for any number of inputs using slices
4. **Create Your Own**: Write pseudocode for calculating the volume of a cylinder and cone

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Complex Arithmetic Expression

```
package main

import "fmt"

func main() {
    // Algorithm: Evaluate Complex Expression
    a := 10
    b := 5
    c := 2

    result := (a + b) * c - float64(a) / float64(c)
    fmt.Println("Result: " + fmt.Sprintf("%f", result))

    result2 := float64(a) + float64(b)*float64(c) - float64(a)/float64(c)
    fmt.Println("Result without parentheses: " + fmt.Sprintf("%f", result2))

    result3 := (float64(a+b)*float64(c) - float64(a)) / float64(c)
    fmt.Println("Result with different grouping: " + fmt.Sprintf("%f", result3))
}
```

### Algorithm 2: Quadratic Formula Calculator

```
package main

import (
    "fmt"
    "math"
)

func main() {
    // Algorithm: Solve Quadratic Equation
    a := 1.0
    b := -5.0
    c := 6.0

    discriminant := b*b - 4*a*c
    sqrt_discriminant := math.Sqrt(discriminant)
    root1 := (-b + sqrt_discriminant) / (2 * a)
    root2 := (-b - sqrt_discriminant) / (2 * a)

    fmt.Println("Root 1: " + fmt.Sprintf("%f", root1))
    fmt.Println("Root 2: " + fmt.Sprintf("%f", root2))
}
```

### Algorithm 3: Compound Interest Calculator

```
package main

import (
    "fmt"
    "math"
)

func main() {
    // Algorithm: Calculate Compound Interest
    principal := 1000.0
    rate := 0.05
    time := 10.0
    compounds_per_year := 12.0

    amount := principal * math.Pow(1+rate/compounds_per_year, compounds_per_year*time)
    interest := amount - principal

    fmt.Println("Principal: $" + fmt.Sprintf("%.2f", principal))
    fmt.Println("Final Amount: $" + fmt.Sprintf("%.2f", amount))
    fmt.Println("Interest Earned: $" + fmt.Sprintf("%.2f", interest))
}
```

### Algorithm 4: Geometric Calculations

```
package main

import (
    "fmt"
    "math"
)

func main() {
    // Algorithm: Calculate Geometric Properties
    radius := 5.0
    side := 4.0
    base := 6.0
    height := 8.0

    circle_area := math.Pi * radius * radius
    circle_circumference := 2 * math.Pi * radius
    square_area := side * side
    square_perimeter := 4 * side
    triangle_area := 0.5 * base * height

    fmt.Println("Circle - Area: " + fmt.Sprintf("%.2f", circle_area) + ", Circumference: " + fmt.Sprintf("%.2f", circle_circumference))
    fmt.Println("Square - Area: " + fmt.Sprintf("%.2f", square_area) + ", Perimeter: " + fmt.Sprintf("%.2f", square_perimeter))
    fmt.Println("Triangle - Area: " + fmt.Sprintf("%.2f", triangle_area))
}
```

### Algorithm 5: Physics Formula Calculator

```
package main

import "fmt"

func main() {
    // Algorithm: Physics Calculations
    mass := 5.5
    velocity := 10.0
    acceleration := 9.8
    time := 3.0

    kinetic_energy := 0.5 * mass * velocity * velocity
    force := mass * acceleration
    distance := velocity*time + 0.5*acceleration*time*time
    momentum := mass * velocity

    fmt.Println("Kinetic Energy: " + fmt.Sprintf("%f", kinetic_energy))
    fmt.Println("Force: " + fmt.Sprintf("%f", force))
    fmt.Println("Distance: " + fmt.Sprintf("%f", distance))
    fmt.Println("Momentum: " + fmt.Sprintf("%f", momentum))
}
```

### Algorithm 6: Temperature Conversion with Multiple Formulas

```
package main

import "fmt"

func main() {
    // Algorithm: Multiple Temperature Conversions
    celsius := 25.0
    fahrenheit := celsius*9/5 + 32
    kelvin := celsius + 273.15
    celsius_from_f := (fahrenheit - 32) * 5 / 9
    celsius_from_k := kelvin - 273.15

    fmt.Println("Celsius: " + fmt.Sprintf("%f", celsius))
    fmt.Println("Fahrenheit: " + fmt.Sprintf("%f", fahrenheit))
    fmt.Println("Kelvin: " + fmt.Sprintf("%f", kelvin))
    fmt.Println("F to C: " + fmt.Sprintf("%f", celsius_from_f))
    fmt.Println("K to C: " + fmt.Sprintf("%f", celsius_from_k))
}
```

### Algorithm 7: Statistical Calculations

```
package main

import (
    "fmt"
    "math"
)

func main() {
    // Algorithm: Calculate Statistics for Three Numbers
    num1 := 10.0
    num2 := 20.0
    num3 := 30.0

    sum := num1 + num2 + num3
    average := sum / 3
    range_val := num3 - num1 // assuming num3 is largest, num1 is smallest
    sum_of_squares := num1*num1 + num2*num2 + num3*num3
    mean_of_squares := sum_of_squares / 3
    variance := mean_of_squares - average*average
    std_deviation := math.Sqrt(variance)

    fmt.Println("Sum: " + fmt.Sprintf("%f", sum))
    fmt.Println("Average: " + fmt.Sprintf("%f", average))
    fmt.Println("Range: " + fmt.Sprintf("%f", range_val))
    fmt.Println("Variance: " + fmt.Sprintf("%f", variance))
    fmt.Println("Standard Deviation: " + fmt.Sprintf("%.2f", std_deviation))
}
```

### Mathematical Operation Translation Patterns

| Pseudocode | Go |
|------------|-----|
| `SET result TO a + b` | `result := float64(a) + float64(b)` |
| `SET result TO a - b` | `result := float64(a) - float64(b)` |
| `SET result TO a * b` | `result := float64(a) * float64(b)` |
| `SET result TO a / b` | `result := float64(a) / float64(b)` |
| `SET result TO POWER(a, b)` | `result := math.Pow(float64(a), float64(b))` |
| `SET result TO SQRT(a)` | `result := math.Sqrt(float64(a))` |
| `USE PI` | `math.Pi` |

### Important Notes

**Static Typing**: Go requires explicit type handling. When performing operations with integers and getting fractional results, convert to float64.

**Math Library**: Go's math library provides many useful mathematical functions but needs to be imported with `import "math"`.

**Operator Precedence**: Go follows standard mathematical order of operations.

**Type Safety**: Go's strong typing helps prevent certain mathematical errors at compile time.

---

 **Excellent work! You've mastered translating mathematical operations from pseudocode to Go!**

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
