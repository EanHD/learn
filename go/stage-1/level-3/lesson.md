# Level 3: Basic Math Operations

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Time to do some math! Today you'll learn how to perform mathematical operations in Go. You'll work with numbers, calculate results, and see how Go handles different mathematical operations.

---

### Learning Goals

- Learn Go arithmetic operators (+, -, *, /, %)
- Practice mathematical calculations
- Understand operator precedence
- Learn about the modulo operator (%)
- Understand how Go handles different number types in math

---

### Your Task

**Copy the following code into a new file called `math.go`**

```go
package main

import "fmt"

func main() {
    // Basic arithmetic operations
    fmt.Println("=== Basic Arithmetic ===")
    
    // Addition
    sum := 5 + 3
    fmt.Println("5 + 3 =", sum)
    
    // Subtraction
    difference := 10 - 4
    fmt.Println("10 - 4 =", difference)
    
    // Multiplication
    product := 6 * 7
    fmt.Println("6 * 7 =", product)
    
    // Division (integer division when both operands are integers)
    quotient := 15 / 3
    fmt.Println("15 / 3 =", quotient)
    
    // Modulo (remainder)
    remainder := 17 % 5
    fmt.Println("17 % 5 =", remainder, "(remainder)")
    
    fmt.Println()
    fmt.Println("=== Integer vs Float Division ===")
    
    // Integer division
    intResult := 7 / 2
    fmt.Println("Integer division 7/2 =", intResult) // Output: 3 (truncated)
    
    // Float division
    floatResult := 7.0 / 2.0
    fmt.Println("Float division 7.0/2.0 =", floatResult) // Output: 3.5
    
    // Mixed division (int converted to float)
    mixedResult := float64(7) / 2.0
    fmt.Println("Mixed division float64(7)/2.0 =", mixedResult)
    
    fmt.Println()
    fmt.Println("=== Order of Operations ===")
    
    // Parentheses change the order
    withParentheses := (10 + 5) * 2
    fmt.Println("(10 + 5) * 2 =", withParentheses)
    
    withoutParentheses := 10 + 5 * 2
    fmt.Println("10 + 5 * 2 =", withoutParentheses)
    
    fmt.Println()
    fmt.Println("=== Real-World Calculations ===")
    
    // Calculate area of rectangle
    length := 10
    width := 5
    area := length * width
    fmt.Println("Rectangle area (", length, "x", width, "):", area)
    
    // Calculate circle area (π * r²)
    radius := 7.0
    circleArea := 3.14159 * radius * radius
    fmt.Println("Circle area (radius", radius, "):", circleArea)
    
    // Calculate average of three numbers
    num1 := 10
    num2 := 20
    num3 := 30
    average := (num1 + num2 + num3) / 3
    fmt.Println("Average of", num1, ",", num2, ",", num3, ":", average)
    
    fmt.Println()
    fmt.Println("=== Increment and Decrement ===")
    
    // Go has increment (++) and decrement (--) operators, but they are statements, not expressions
    count := 5
    fmt.Println("Initial count:", count)
    
    count++  // Increment by 1 (equivalent to: count = count + 1)
    fmt.Println("After increment:", count)
    
    count--  // Decrement by 1 (equivalent to: count = count - 1)
    fmt.Println("After decrement:", count)
    
    fmt.Println()
    fmt.Println("=== Compound Assignment Operations ===")
    
    value := 10
    fmt.Println("Initial value:", value)
    
    value += 5  // Same as: value = value + 5
    fmt.Println("After += 5:", value)
    
    value -= 3  // Same as: value = value - 3
    fmt.Println("After -= 3:", value)
    
    value *= 2  // Same as: value = value * 2
    fmt.Println("After *= 2:", value)
    
    value /= 4  // Same as: value = value / 4
    fmt.Println("After /= 4:", value)
    value %= 3  // Same as: value = value % 3
    fmt.Println("After %= 3:", value)
    
    fmt.Println()
    fmt.Println("=== Advanced Math Operations ===")
    
    // Go doesn't have a built-in exponentiation operator
    // We need to use the math package for exponentiation
    importMathExample()
    
    // Integer overflow example (with smaller integer types)
    var smallInt int8 = 127  // Maximum value for int8
    fmt.Println("Max int8 value:", smallInt)
    
    // This would cause overflow (but Go will catch it at runtime in some cases)
    // For now, just showing the concept:
    overflown := int8(smallInt) + 1
    fmt.Println("Max int8 + 1 (overflow):", overflown) // Will wrap around to -128
    
    fmt.Println()
    fmt.Println("=== Type Conversion in Math ===")
    
    // When doing math with different types, you need to convert
    var intNum int = 10
    var floatNum float64 = 3.5
    
    // Need to convert to the same type
    result1 := float64(intNum) + floatNum
    result2 := intNum + int(floatNum) // This truncates floatNum to 3
    
    fmt.Println("intNum + floatNum (with conversion):", result1)
    fmt.Println("intNum + int(floatNum) (truncated):", result2)
}

// Example that imports the math package for advanced operations
func importMathExample() {
    import (  // We can't import inside functions in Go, so this is just illustrative
        "math"
    )
    
    // Since we can't actually import in a function, let's show how it would work:
    // squareRoot := math.Sqrt(16)  // Square root
    // power := math.Pow(2, 3)      // 2 to the power of 3
    // rounded := math.Round(4.7)   // Round to nearest integer
    
    // For this example, we'll just show integer exponentiation
    base := 2
    power := 3
    result := 1
    for i := 0; i < power; i++ {
        result *= base
    }
    fmt.Println("2^3 (manual):", result)
}
```

Actually, let me fix the above code as we can't import inside functions in Go. Here's the corrected version:

```go
package main

import (
    "fmt"
    "math"
)

func main() {
    // Basic arithmetic operations
    fmt.Println("=== Basic Arithmetic ===")
    
    // Addition
    sum := 5 + 3
    fmt.Println("5 + 3 =", sum)
    
    // Subtraction
    difference := 10 - 4
    fmt.Println("10 - 4 =", difference)
    
    // Multiplication
    product := 6 * 7
    fmt.Println("6 * 7 =", product)
    
    // Division (integer division when both operands are integers)
    quotient := 15 / 3
    fmt.Println("15 / 3 =", quotient)
    
    // Modulo (remainder)
    remainder := 17 % 5
    fmt.Println("17 % 5 =", remainder, "(remainder)")
    
    fmt.Println()
    fmt.Println("=== Integer vs Float Division ===")
    
    // Integer division
    intResult := 7 / 2
    fmt.Println("Integer division 7/2 =", intResult) // Output: 3 (truncated)
    
    // Float division
    floatResult := 7.0 / 2.0
    fmt.Println("Float division 7.0/2.0 =", floatResult) // Output: 3.5
    
    // Mixed division (int converted to float)
    mixedResult := float64(7) / 2.0
    fmt.Println("Mixed division float64(7)/2.0 =", mixedResult)
    
    fmt.Println()
    fmt.Println("=== Order of Operations ===")
    
    // Parentheses change the order
    withParentheses := (10 + 5) * 2
    fmt.Println("(10 + 5) * 2 =", withParentheses)
    
    withoutParentheses := 10 + 5 * 2
    fmt.Println("10 + 5 * 2 =", withoutParentheses)
    
    fmt.Println()
    fmt.Println("=== Real-World Calculations ===")
    
    // Calculate area of rectangle
    length := 10
    width := 5
    area := length * width
    fmt.Println("Rectangle area (", length, "x", width, "):", area)
    
    // Calculate circle area (π * r²)
    radius := 7.0
    circleArea := 3.14159 * radius * radius
    fmt.Println("Circle area (radius", radius, "):", circleArea)
    
    // Calculate average of three numbers
    num1 := 10
    num2 := 20
    num3 := 30
    average := (num1 + num2 + num3) / 3
    fmt.Println("Average of", num1, ",", num2, ",", num3, ":", average)
    
    fmt.Println()
    fmt.Println("=== Increment and Decrement ===")
    
    // Go has increment (++) and decrement (--) operators, but they are statements, not expressions
    count := 5
    fmt.Println("Initial count:", count)
    
    count++  // Increment by 1 (equivalent to: count = count + 1)
    fmt.Println("After increment:", count)
    
    count--  // Decrement by 1 (equivalent to: count = count - 1)
    fmt.Println("After decrement:", count)
    
    fmt.Println()
    fmt.Println("=== Compound Assignment Operations ===")
    
    value := 10
    fmt.Println("Initial value:", value)
    
    value += 5  // Same as: value = value + 5
    fmt.Println("After += 5:", value)
    
    value -= 3  // Same as: value = value - 3
    fmt.Println("After -= 3:", value)
    
    value *= 2  // Same as: value = value * 2
    fmt.Println("After *= 2:", value)
    
    value /= 4  // Same as: value = value / 4
    fmt.Println("After /= 4:", value)
    value %= 3  // Same as: value = value % 3
    fmt.Println("After %= 3:", value)
    
    fmt.Println()
    fmt.Println("=== Advanced Math with Math Package ===")
    
    // Square root
    sqrtResult := math.Sqrt(16)
    fmt.Println("Square root of 16:", sqrtResult)
    
    // Power
    powerResult := math.Pow(2, 3)
    fmt.Println("2^3:", powerResult)
    
    // Round
    rounded := math.Round(4.7)
    fmt.Println("Round 4.7:", rounded)
    
    // Ceiling
    ceiling := math.Ceil(4.2)
    fmt.Println("Ceiling of 4.2:", ceiling)
    
    // Floor
    floor := math.Floor(4.7)
    fmt.Println("Floor of 4.7:", floor)
    
    // Absolute value
    absValue := math.Abs(-10.5)
    fmt.Println("Absolute value of -10.5:", absValue)
    
    fmt.Println()
    fmt.Println("=== Integer Overflow Example ===")
    
    // Integer overflow example (with smaller integer types)
    var smallInt int8 = 127  // Maximum value for int8
    fmt.Println("Max int8 value:", smallInt)
    
    // This demonstrates overflow behavior
    overflown := int8(smallInt) + 1
    fmt.Println("Max int8 + 1 (overflow):", overflown) // Will wrap around to -128
    
    fmt.Println()
    fmt.Println("=== Type Conversion in Math ===")
    
    // When doing math with different types, you need to convert
    var intNum int = 10
    var floatNum float64 = 3.5
    
    // Need to convert to the same type
    result1 := float64(intNum) + floatNum
    result2 := intNum + int(floatNum) // This truncates floatNum to 3
    
    fmt.Println("intNum + floatNum (with conversion):", result1)
    fmt.Println("intNum + int(floatNum) (truncated):", result2)
}
```

---

### How to Execute

1. **Create or navigate to a Go module directory** (if not already in one):
   ```bash
   mkdir math-example && cd math-example
   go mod init math
   ```
2. **Copy the code into `math.go`**
3. **Run your program**:
   ```bash
   go run math.go
   ```

**Expected output:**
```
=== Basic Arithmetic ===
5 + 3 = 8
10 - 4 = 6
6 * 7 = 42
15 / 3 = 5
17 % 5 = 2 (remainder)

=== Integer vs Float Division ===
Integer division 7/2 = 3
Float division 7.0/2.0 = 3.5
Mixed division float64(7)/2.0 = 3.5

=== Order of Operations ===
(10 + 5) * 2 = 30
10 + 5 * 2 = 20

=== Real-World Calculations ===
Rectangle area ( 10 x 5 ): 50
Circle area (radius 7): 153.93804000000003
Average of 10 , 20 , 30 : 20

=== Increment and Decrement ===
Initial count: 5
After increment: 6
After decrement: 6

=== Compound Assignment Operations ===
Initial value: 10
After += 5: 15
After -= 3: 12
After *= 2: 24
After /= 4: 6
After %= 3: 0

=== Advanced Math with Math Package ===
Square root of 16: 4
2^3: 8
Round 4.7: 5
Ceiling of 4.2: 5
Floor of 4.7: 4
Absolute value of -10.5: 10.5

=== Integer Overflow Example ===
Max int8 value: 127
Max int8 + 1 (overflow): -128

=== Type Conversion in Math ===
intNum + floatNum (with conversion): 13.5
intNum + int(floatNum) (truncated): 13
```

---

### Success Checklist

- [ ] Created a file named `math.go`
- [ ] Created a Go module if needed
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw all mathematical operations working correctly
- [ ] Understood operator precedence and different operations

---

### What's That Math Symbol Mean?

In Go math, you saw some operators:

- **`+`** = Addition
- **`-`** = Subtraction
- **`*`** = Multiplication
- **`/`** = Division
- **`%`** = Modulo (remainder after division)

---

### Try This (Optional Challenges)

1. Calculate compound interest: A = P(1+r/n)^nt
2. Create a temperature converter (Celsius to Fahrenheit)
3. Calculate the hypotenuse of a right triangle using the Pythagorean theorem
4. Experiment with different integer types (int8, int16, int32) and see overflow behavior

---

## Quick Reference

| Operator | What it does | Example | Result |
|----------|--------------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `6 / 3` | `2` (or `2.0` if floats) |
| `%` | Modulo (remainder) | `7 % 3` | `1` |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```go
sum := 5 + 3
fmt.Println("5 + 3 =", sum)
```
- **`:=`** = Short variable declaration (declare and initialize)
- **`+`** = Addition operator (performs arithmetic addition)
- **Variable declaration** happens at the same time as initialization

```go
remainder := 17 % 5
fmt.Println("17 % 5 =", remainder, "(remainder)")
```
- **`%`** = Modulo operator (returns the remainder after division)
- 17 ÷ 5 = 3 remainder 2, so 17 % 5 = 2
- Useful for checking if numbers are even (n % 2 == 0) or cycling through values

### Integer vs Float Division

In Go, when both operands in division are integers, the result is truncated to an integer:

```go
result := 7 / 2      // Result is 3 (integer truncated)
result := 7.0 / 2.0  // Result is 3.5 (float division)
result := 7 / 2.0    // Result is 3.5 (mixed, converted to float)
```

### Order of Operations (PEMDAS)

Go follows the standard mathematical order of operations:

1. **P**arentheses `()`
2. **M**ultiplication `*`, **D**ivision `/`, **M**odulo `%` (left to right)
3. **A**ddition `+`, **S**ubtraction `-` (left to right)

Examples:
```go
// Without parentheses: Multiplication before addition
result := 10 + 5 * 2  // = 10 + 10 = 20 (not 30!)

// With parentheses: Addition before multiplication
result := (10 + 5) * 2  // = 15 * 2 = 30
```

### Go's Math Package

The math package provides advanced mathematical functions:

```go
import "math"

// Basic operations
math.Sqrt(16)     // Square root: 4.0
math.Abs(-5)      // Absolute value: 5.0
math.Min(1, 5)    // Minimum: 1.0
math.Max(1, 5)    // Maximum: 5.0

// Rounding functions
math.Floor(4.7)   // Floor (round down): 4.0
math.Ceil(4.2)    // Ceiling (round up): 5.0
math.Round(4.7)   // Round: 5.0

// Exponents
math.Pow(2, 3)    // 2 to the power of 3: 8.0

// Constants
math.Pi   // π: 3.141592653589793
math.E    // e: 2.718281828459045
```

### Increment and Decrement Operators

Go has `++` and `--` operators, but they are statements, not expressions:

```go
count := 5
count++  // OK: increments count by 1
count--  // OK: decrements count by 1

// NOT OK in Go (unlike C/C++/Java):
// result := count++  // Syntax error! Can't use as expression
```

### Compound Assignment Operators

Go supports all compound assignment operators:

```go
value := 10
value += 5  // Same as: value = value + 5
value -= 3  // Same as: value = value - 3
value *= 2  // Same as: value = value * 2
value /= 4  // Same as: value = value / 4
value %= 3  // Same as: value = value % 3
```

### Important Go Math Notes

**No exponentiation operator**: Go doesn't have a `^` operator for exponentiation (it's used for bitwise XOR). Use `math.Pow()` instead:

```go
result := math.Pow(2, 3)  // 2^3 = 8
```

**Integer overflow**: Go has types of different sizes. When you exceed the limit of a type, it wraps around:

```go
var small int8 = 127  // Maximum for int8
small = small + 1     // Now small becomes -128 (overflow)
```

**Type conversions**: In Go, you must explicitly convert between numeric types:

```go
var intVal int = 5
var floatVal float64 = 2.5

// This will cause an error:
// result := intVal + floatVal  // Type mismatch!

// Must convert explicitly:
result1 := float64(intVal) + floatVal  // Convert int to float64
result2 := intVal + int(floatVal)      // Convert float64 to int (truncates)
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `invalid operation: mismatched types` | Mixing incompatible types | Convert types explicitly with Type() |
| `constant [number] overflows [type]` | Number too large for type | Use larger type (int32 to int64) |
| `syntax error: unexpected ++` | Using ++ or -- incorrectly | These can't be used as expressions |
| Operator precedence issues | Wrong order of operations | Use parentheses to clarify order |

### Advanced Challenge (For the Brave!)

Try this complex calculation:

```go
package main

import (
    "fmt"
    "math"
)

func main() {
    fmt.Println("=== Complex Math Example ===")
    
    // Compound interest calculation
    principal := 1000.0           // Initial amount
    rate := 0.05                  // 5% annual interest rate
    timesCompounded := 12.0       // Compounded monthly
    years := 10.0                 // 10 years
    
    // Formula: A = P(1 + r/n)^(nt)
    amount := principal * math.Pow(1 + rate/timesCompounded, timesCompounded * years)
    
    fmt.Println("Initial investment: $", principal)
    fmt.Printf("After %.0f years at %.0f%% interest: $%.2f\n", years, rate*100, amount)
    
    // Calculate percentage change
    original := 100.0
    newAmount := 125.0
    percentageChange := ((newAmount - original) / original) * 100
    fmt.Printf("Percentage change from %.0f to %.0f: %.2f%%\n", original, newAmount, percentageChange)
    
    // Pythagorean theorem (a² + b² = c²)
    sideA := 3.0
    sideB := 4.0
    hypotenuse := math.Sqrt(sideA*sideA + sideB*sideB)
    fmt.Printf("Right triangle with sides %.0f and %.0f has hypotenuse: %.2f\n", sideA, sideB, hypotenuse)
    
    // Working with different number sizes and overflow
    var counter int32 = 2147483647  // Maximum for int32
    fmt.Println("Max int32:", counter)
    fmt.Println("Max int32 + 1:", counter + 1)  // This will overflow to negative
}
```

---

 **Excellent work! You're becoming a mathematical wizard in Go!** 

*Ready for the next challenge? Let's learn how to get input from users!*
