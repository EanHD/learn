# Level 1: Basic Pseudocode Translation
## Stage 2: Pseudocode to Code

### Today's Mission

Welcome to Stage 2! You've mastered copying code - now it's time to think like a programmer! Today you'll learn to translate written instructions (pseudocode) into working Go programs. This is where programming becomes creative problem-solving!

---

### Learning Goals

- Understand what pseudocode is and why it's useful
- Learn to read and interpret algorithmic descriptions
- Practice translating simple algorithms into Go code
- Develop logical thinking for programming
- Create working programs from written instructions

---

### What is Pseudocode?

**Pseudocode** is a way to write programming logic in plain English (or your native language) before writing actual code. It's like writing a recipe or instructions for a task.

**Example:**
```
Algorithm: Make a sandwich
1. Get bread from pantry
2. Get peanut butter from fridge
3. Get jelly from pantry
4. Spread peanut butter on one bread slice
5. Spread jelly on the other bread slice
6. Put slices together
7. Enjoy your sandwich!
```

This is much easier to understand than trying to write code first!

---

### Your Task

**For each pseudocode algorithm below, translate it into working Go code.**

---

## Algorithm 1: Greeting Program

**Pseudocode:**
```
Algorithm: Display Personal Greeting
1. Display "Hello! What's your name?" to the user
2. Get the user's name from input
3. Display "Nice to meet you, " followed by the user's name
4. Display "Welcome to programming!"
```

**Your Task:** Create a Go program that follows these exact steps.

---

## Algorithm 2: Simple Calculator

**Pseudocode:**
```
Algorithm: Add Two Numbers
1. Ask user for first number
2. Get first number from user
3. Ask user for second number
4. Get second number from user
5. Calculate sum of the two numbers
6. Display "The sum is: " followed by the sum
```

**Your Task:** Create a Go program that implements this calculator.

---

## Algorithm 3: Age Calculator

**Pseudocode:**
```
Algorithm: Calculate Age in Days
1. Display "Enter your age in years: "
2. Get age in years from user
3. Calculate days = age × 365
4. Display "You are approximately " + days + " days old"
5. Display "That's a lot of days!"
```

**Your Task:** Create a program that calculates approximate age in days.

---

## Algorithm 4: Temperature Converter

**Pseudocode:**
```
Algorithm: Celsius to Fahrenheit Converter
1. Display "Enter temperature in Celsius: "
2. Get temperature in Celsius from user
3. Calculate Fahrenheit = (Celsius × 9/5) + 32
4. Display the Celsius temperature
5. Display "°C = "
6. Display the Fahrenheit temperature
7. Display "°F"
```

**Your Task:** Create a temperature conversion program.

---

## Algorithm 5: Rectangle Area Calculator

**Pseudocode:**
```
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
```

**Your Task:** Create a program that calculates both area and perimeter.

---

## Algorithm 6: Simple Interest Calculator

**Pseudocode:**
```
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
```

**Your Task:** Implement the complete interest calculation.

---

## Algorithm 7: BMI Calculator

**Pseudocode:**
```
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
```

**Your Task:** Create a program that calculates BMI with categorization.

---

### How to Approach Each Algorithm

**Step-by-Step Process:**

1. **Read Carefully**: Understand what the algorithm does
2. **Identify Inputs**: What information does the user provide?
3. **Identify Outputs**: What should the program display?
4. **Identify Calculations**: What math is needed?
5. **Plan the Code Structure**:
   - Import necessary packages
   - Define variables for user input
   - Use appropriate functions for input/output
   - Perform calculations
   - Display results with proper formatting

**Example Planning for Algorithm 1:**
- **Imports**: `fmt` for output, `bufio` and `os` for input
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
- [ ] Proper error handling for user input

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
```
Algorithm: Process User Data
1. Get user's name
2. Get user's age
3. If age >= 18 then
   Display "Adult user"
Else
   Display "Minor user"
4. Display "Data processed"
```

### Bad Pseudocode (Too Vague)
```
Algorithm: Do stuff
1. Get things
2. Calculate something
3. Show results
```

### Good Pseudocode (Clear and Specific)
```
Algorithm: Calculate BMI
1. Display "BMI Calculator"
2. Display "Enter weight in kg: "
3. Get weight from user
4. Display "Enter height in meters: "
5. Get height from user
6. Calculate BMI = weight ÷ (height × height)
7. Display "Your BMI is: " + BMI
```

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Greeting Program

```go
package main

import (
    "bufio"
    "fmt"
    "os"
    "strings"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    
    fmt.Println("Algorithm 1: Greeting Program")
    
    // Display "Hello! What's your name?" to the user
    fmt.Print("Hello! What's your name? ")
    name, _ := reader.ReadString('\n')
    name = strings.TrimSpace(name)
    
    // Display "Nice to meet you, " followed by the user's name
    fmt.Println("Nice to meet you, " + name)
    
    // Display "Welcome to programming!"
    fmt.Println("Welcome to programming!")
}
```

### Algorithm 2: Simple Calculator

```go
package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    
    fmt.Println("Algorithm 2: Simple Calculator")
    
    // Ask user for first number
    fmt.Print("Enter first number: ")
    firstInput, _ := reader.ReadString('\n')
    firstNum, err := strconv.ParseFloat(strings.TrimSpace(firstInput), 64)
    if err != nil {
        fmt.Println("Invalid number entered!")
        return
    }
    
    // Ask user for second number
    fmt.Print("Enter second number: ")
    secondInput, _ := reader.ReadString('\n')
    secondNum, err := strconv.ParseFloat(strings.TrimSpace(secondInput), 64)
    if err != nil {
        fmt.Println("Invalid number entered!")
        return
    }
    
    // Calculate sum of the two numbers
    sum := firstNum + secondNum
    
    // Display "The sum is: " followed by the sum
    fmt.Println("The sum is: " + fmt.Sprintf("%g", sum))
}
```

### Algorithm 3: Age Calculator

```go
package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    
    fmt.Println("Algorithm 3: Age Calculator")
    
    // Display "Enter your age in years: "
    fmt.Print("Enter your age in years: ")
    ageInput, _ := reader.ReadString('\n')
    age, err := strconv.Atoi(strings.TrimSpace(ageInput))
    if err != nil {
        fmt.Println("Invalid number entered!")
        return
    }
    
    // Calculate days = age × 365
    days := age * 365
    
    // Display messages
    fmt.Println("You are approximately " + strconv.Itoa(days) + " days old")
    fmt.Println("That's a lot of days!")
}
```

### Algorithm 4: Temperature Converter

```go
package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    
    fmt.Println("Algorithm 4: Temperature Converter")
    
    // Display "Enter temperature in Celsius: "
    fmt.Print("Enter temperature in Celsius: ")
    celsiusInput, _ := reader.ReadString('\n')
    celsius, err := strconv.ParseFloat(strings.TrimSpace(celsiusInput), 64)
    if err != nil {
        fmt.Println("Invalid number entered!")
        return
    }
    
    // Calculate Fahrenheit = (Celsius × 9/5) + 32
    fahrenheit := (celsius * 9/5) + 32
    
    // Display the results
    fmt.Printf("%.2f°C = %.2f°F\n", celsius, fahrenheit)
}
```

### Algorithm 5: Rectangle Area Calculator

```go
package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    
    fmt.Println("Rectangle Area Calculator")
    
    // Get length from user
    fmt.Print("Enter length: ")
    lengthInput, _ := reader.ReadString('\n')
    length, err := strconv.ParseFloat(strings.TrimSpace(lengthInput), 64)
    if err != nil {
        fmt.Println("Invalid number entered!")
        return
    }
    
    // Get width from user
    fmt.Print("Enter width: ")
    widthInput, _ := reader.ReadString('\n')
    width, err := strconv.ParseFloat(strings.TrimSpace(widthInput), 64)
    if err != nil {
        fmt.Println("Invalid number entered!")
        return
    }
    
    // Calculate area = length × width
    area := length * width
    
    // Calculate perimeter = 2 × (length + width)
    perimeter := 2 * (length + width)
    
    // Display results
    fmt.Println("Area: " + fmt.Sprintf("%g", area))
    fmt.Println("Perimeter: " + fmt.Sprintf("%g", perimeter))
}
```

### Algorithm 6: Simple Interest Calculator

```go
package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    
    fmt.Println("Simple Interest Calculator")
    
    // Get principal from user
    fmt.Print("Enter principal amount: $")
    principalInput, _ := reader.ReadString('\n')
    principal, err := strconv.ParseFloat(strings.TrimSpace(principalInput), 64)
    if err != nil {
        fmt.Println("Invalid number entered!")
        return
    }
    
    // Get rate from user
    fmt.Print("Enter interest rate (%): ")
    rateInput, _ := reader.ReadString('\n')
    rate, err := strconv.ParseFloat(strings.TrimSpace(rateInput), 64)
    if err != nil {
        fmt.Println("Invalid number entered!")
        return
    }
    
    // Get time from user
    fmt.Print("Enter time in years: ")
    timeInput, _ := reader.ReadString('\n')
    time, err := strconv.ParseFloat(strings.TrimSpace(timeInput), 64)
    if err != nil {
        fmt.Println("Invalid number entered!")
        return
    }
    
    // Calculate interest = (principal × rate × time) ÷ 100
    interest := (principal * rate * time) / 100
    
    // Calculate total = principal + interest
    total := principal + interest
    
    // Display results
    fmt.Printf("Principal: $%.2f\n", principal)
    fmt.Printf("Interest: $%.2f\n", interest)
    fmt.Printf("Total: $%.2f\n", total)
}
```

### Algorithm 7: BMI Calculator

```go
package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

func main() {
    reader := bufio.NewReader(os.Stdin)
    
    fmt.Println("BMI Calculator")
    
    // Get weight from user
    fmt.Print("Enter weight in kg: ")
    weightInput, _ := reader.ReadString('\n')
    weight, err := strconv.ParseFloat(strings.TrimSpace(weightInput), 64)
    if err != nil {
        fmt.Println("Invalid number entered!")
        return
    }
    
    // Get height from user
    fmt.Print("Enter height in meters: ")
    heightInput, _ := reader.ReadString('\n')
    height, err := strconv.ParseFloat(strings.TrimSpace(heightInput), 64)
    if err != nil {
        fmt.Println("Invalid number entered!")
        return
    }
    
    // Calculate bmi = weight ÷ (height × height)
    bmi := weight / (height * height)
    
    // Display the BMI
    fmt.Printf("Your BMI is: %.2f\n", bmi)
    
    // Category determination
    if bmi < 18.5 {
        fmt.Println("Category: Underweight")
    } else if bmi < 25 {
        fmt.Println("Category: Normal weight")
    } else if bmi < 30 {
        fmt.Println("Category: Overweight")
    } else {
        fmt.Println("Category: Obesity")
    }
}
```

### Common Translation Patterns

| Pseudocode Pattern | Go Equivalent |
|-------------------|---------------|
| `Display message` | `fmt.Println(message)` or `fmt.Printf(format, values)` |
| `Get variable from user` | Use `bufio.NewReader` with `ReadString` and `strconv` for conversion |
| `Calculate result = a + b` | `result := a + b` |
| `If condition then` | `if condition {` |
| `Else if` | `else if condition {` |
| `Else` | `else {` |

### Debugging Tips

**"Program doesn't compile":**
- Check that all required packages are imported
- Verify syntax like colons and commas
- Ensure proper function calls and conversions

**"Wrong output":**
- Check variable names match (case-sensitive)
- Verify data types match usage
- Check mathematical formulas

**"Input not working":**
- Ensure proper string trimming with `strings.TrimSpace`
- Use correct `strconv` functions for type conversion
- Handle errors properly with proper error checking

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
```go
fmt.Print("Enter age: ")
input, _ := reader.ReadString('\n')
age, err := strconv.Atoi(strings.TrimSpace(input))
```

**Getting Text:**
```go
fmt.Print("Enter name: ")
input, _ := reader.ReadString('\n')
name := strings.TrimSpace(input)
```

**Displaying Results:**
```go
fmt.Println("Result: " + result)
fmt.Printf("Price: $%.2f\n", price)
fmt.Println("Hello, " + name + "!")
```

---

 **Congratulations! You've translated your first pseudocode algorithms into working Go programs!** 

*This is a major milestone - you're now thinking like a programmer! Next up: Variables in pseudocode!*