# Level 2: Variables and Data Types

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Welcome to the world of variables! Today you'll learn how to store and use data in your Go programs. Variables are like labeled boxes where you can store information - numbers, text, and more!

---

### Learning Goals

- Understand what variables are and why we need them
- Learn basic data types (string, int, float64, bool)
- Practice declaring and initializing variables
- Learn how to display variable values
- Understand Go's static typing system

---

### Your Task

**Copy the following code into a new file called `variables.go`**

```
package main

import "fmt"

func main() {
    // String variables (text)
    var name string = "Alex"
    var city string = "New York"
    var hobby string = "programming"
    
    // You can also use short declaration (available inside functions only)
    country := "USA"
    
    // Number variables (integers)
    var age int = 25
    var height int = 175
    var score int = 100
    
    // Number variables (floating point)
    var temperature float64 = 98.6
    var price float64 = 29.99
    var weight float64 = 150.5
    
    // Boolean variables (true/false)
    var isStudent bool = true
    var isEmployed bool = false
    var isHappy bool = true
    
    // Print all the variables
    fmt.Println("=== Personal Info ===")
    fmt.Println("Name: " + name)
    fmt.Println("City: " + city)
    fmt.Println("Hobby: " + hobby)
    fmt.Println("Country: " + country)
    fmt.Println()
    
    fmt.Println("=== Measurements ===")
    fmt.Println("Age:", age, "years old")
    fmt.Println("Height:", height, "cm")
    fmt.Println("Score:", score, "points")
    fmt.Println()
    
    fmt.Println("=== Decimal Measurements ===")
    fmt.Println("Temperature:", temperature, "degrees")
    fmt.Println("Price: $", price)
    fmt.Println("Weight:", weight, "lbs")
    fmt.Println()
    
    fmt.Println("=== Status ===")
    fmt.Println("Student:", isStudent)
    fmt.Println("Employed:", isEmployed)
    fmt.Println("Happy:", isHappy)
    
    // Multiple variable declarations
    var (
        firstName string = "John"
        lastName  string = "Doe"
        age2      int    = 35
    )
    
    fmt.Println()
    fmt.Println("=== Multiple Declaration Example ===")
    fmt.Println("Full Name:", firstName, lastName)
    fmt.Println("Age:", age2)
    
    // Go's static typing prevents type mismatches
    // The following would cause an error:
    // var number int = "this won't work" // Type mismatch error
}
```

---

### How to Execute

1. **Create or navigate to a Go module directory** (if not already in one):
   ```
   mkdir variables-example && cd variables-example
   go mod init variables
   ```
2. **Copy the code into `variables.go`**
3. **Run your program**:
   ```
   go run variables.go
   ```

**Expected output:**
```
=== Personal Info ===
Name: Alex
City: New York
Hobby: programming
Country: USA

=== Measurements ===
Age: 25 years old
Height: 175 cm
Score: 100 points

=== Decimal Measurements ===
Temperature: 98.6 degrees
Price: $ 29.99
Weight: 150.5 lbs

=== Status ===
Student: true
Employed: false
Happy: true

=== Multiple Declaration Example ===
Full Name: John Doe
Age: 35
```

---

### Success Checklist

- [ ] Created a file named `variables.go`
- [ ] Created a Go module if needed
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw all variable values printed correctly
- [ ] Understood how Go variables work

---

### What You Learned!

Go has several important concepts about variables:

- **Static typing** = Variable types are fixed at compile time
- **`var` declaration** = Standard way to declare variables
- **`:=` short declaration** = Shorthand for declaring AND initializing (inside functions only)
- **Multiple declarations** = Group syntax for declaring variables of different types

---

### Try This (Optional Challenges)

1. Change all the variable values to your own information
2. Add new variables for your favorite food and favorite color
3. Try creating a variable that combines multiple pieces of information
4. What happens if you try to assign a string to an integer variable?

---

## Quick Reference

| Data Type | What it holds | Examples | Example Declaration |
|-----------|---------------|----------|-------------------|
| `string` | Text | "Hello", "Go", "123" | `var name string = "Alex"` |
| `int` | Integers | 42, -17, 0 | `var age int = 25` |
| `float64` | Decimal numbers | 3.14, -2.5, 100.0 | `var price float64 = 19.99` |
| `bool` | True/false values | true, false | `var isStudent bool = true` |
| `int8/16/32/64` | Integers with specific sizes | Different integer ranges | `var smallNum int8 = 100` |
| `uint` | Unsigned integers | 0, 1, 2, ... | `var count uint = 42` |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```
var name string = "Alex"
```
- **`var`** = Keyword to declare a variable
- **`name`** = Variable name (follows Go naming conventions)
- **`string`** = Type declaration (Go is statically typed)
- **`=`** = Assignment operator (stores value on right into variable on left)
- **`"Alex"`** = String value (text in quotes)

```
country := "USA"
```
- **`:=`** = Short variable declaration (declare and initialize)
- **Available only** inside functions in Go
- **Type inferred** by Go from the assigned value

```
fmt.Println("Name: " + name)
```
- **`+`** = String concatenation operator (joins strings together)
- The variable `name` gets its value inserted into the output string

### Variable Declaration Methods in Go

Go has three main ways to declare variables:

1. **Standard declaration**:
```
var name string = "Alex"
var age int = 25
```

2. **Type omitted (inferred)**:
```
var name = "Alex"  // Type inferred as string
var age = 25       // Type inferred as int
```

3. **Short declaration** (inside functions only):
```
name := "Alex"     // Type inferred as string
age := 25          // Type inferred as int
```

### Variable Naming Rules

**Valid names**: `name`, `myAge`, `age1`, `student_score`, `studentScore`
**Invalid names**: `123age`, `my-age`, `func`, `age score`

**Rules to remember:**
1. Start with letter or underscore (_)
2. Use only letters, numbers, and underscores after the first character
3. Can't use reserved keywords (`var`, `func`, `package`, `import`, etc.)
4. Case sensitive (`age` ≠ `Age` ≠ `AGE`)
5. Use camelCase for multi-word names (firstName, studentCount)

### Data Types Deep Dive

| Type | Description | Examples | Zero Value |
|------|-------------|----------|------------|
| `string` | Text data | `"Hello"`, `"Go"`, `"123"` | `""` (empty string) |
| `int` | Integer (platform dependent) | `42`, `-17`, `0` | `0` |
| `int8` | 8-bit integer (-128 to 127) | `-100`, `50`, `127` | `0` |
| `int16` | 16-bit integer | `-32768 to 32767` | `0` |
| `int32` | 32-bit integer | `-2^31 to 2^31-1` | `0` |
| `int64` | 64-bit integer | `-2^63 to 2^63-1` | `0` |
| `uint` | Unsigned integer | `0`, `1`, `42` | `0` |
| `uint8` | 8-bit unsigned (0 to 255) | `0`, `100`, `255` | `0` |
| `float32` | 32-bit floating point | `3.14`, `-2.5` | `0.0` |
| `float64` | 64-bit floating point | `3.14159`, `-2.5` | `0.0` |
| `bool` | Boolean (true/false) | `true`, `false` | `false` |
| `byte` | Alias for uint8 | `65`, `97` | `0` |
| `rune` | Alias for int32 (Unicode code point) | `'A'`, 'π' | `0` |

### Zero Values

In Go, every variable has a zero value when declared without initialization:

```
var name string    // Zero value: ""
var age int        // Zero value: 0
var height float64 // Zero value: 0.0
var isTrue bool    // Zero value: false
```

### Multiple Variable Declarations

**Group syntax**:
```
var (
    name string = "Alex"
    age  int    = 25
    city string = "New York"
)
```

**Same type on one line**:
```
var name, city string = "Alex", "New York"
var age1, age2 int = 25, 30
```

### Static Typing

Go's static typing means you must be explicit about types, and type mismatches cause compile errors:

```
var age int = 25
// This will cause a compile error:
// age = "twenty five"  // Cannot assign string to int variable
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `cannot use "text" as type int` | Type mismatch | Ensure variable types match assigned values |
| `undefined: variable` | Variable name typo | Check spelling (case-sensitive) |
| `no new variables on left side of :=` | Re-declaring with := | Use `=` for assignment, not `:=` |
| `non-declaration statement outside function body` | Using := outside function | Use `var` declaration outside functions |

### Bonus Knowledge

- **Type Safety**: Go's static typing prevents many runtime errors
- **Performance**: Static typing allows Go compiler to optimize code
- **Memory**: Specific number types allow memory optimization
- **Zero Values**: Every type has a default "zero" value

### Advanced Challenge (For the Brave!)

Try this modified version:

```
package main

import "fmt"

func main() {
    // Let's do some calculations!
    var currentYear int = 2025
    var birthYear int = 2000
    var calculatedAge int = currentYear - birthYear
    
    fmt.Println("Born in", birthYear, ", now it's", currentYear)
    fmt.Println("Calculated age:", calculatedAge, "years old")
    
    // Working with different number types
    var integerNum int = 10
    var floatNum float64 = 3.5
    var result float64 = float64(integerNum) + floatNum  // Type conversion needed
    
    fmt.Println("Integer:", integerNum)
    fmt.Println("Float:", floatNum)
    fmt.Println("Result:", result)
    
    // Working with strings and characters
    var firstName string = "Jane"
    var lastName string = "Smith"
    var fullName string = firstName + " " + lastName
    
    fmt.Println("Full name:", fullName)
    
    // Using different boolean operations
    var isStudent bool = true
    var isEmployed bool = false
    var isRetired bool = false
    
    fmt.Println("Is student AND not employed:", isStudent && !isEmployed)
    fmt.Println("Is employed OR retired:", isEmployed || isRetired)
}
```

---

 **Excellent work! You now understand variables - the foundation of all programming!** 

*Ready for the next challenge? Let's do some math with our variables!*


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

```
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}

```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard go conventions with proper imports and main function
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
