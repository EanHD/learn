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