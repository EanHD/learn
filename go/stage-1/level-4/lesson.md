# Level 4: User Input

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Now let's make our programs interactive! Today you'll learn how to get input from users and respond to their information. This is where programs become truly useful!

---

### Learning Goals

- Learn how to get input from users
- Understand Go's fmt and bufio packages for input
- Practice creating interactive programs
- Learn to combine input with variables and math
- Handle different types of user input

---

### Your Task

**Copy the following code into a new file called `input.go`**

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
    
    fmt.Println("=== Interactive Greeting Program ===")
    // Get input from user
    fmt.Print("What's your name? ")
    name, _ := reader.ReadString('\n')
    name = strings.TrimSpace(name)  // Remove newline character
    fmt.Println("Hello,", name, "! Nice to meet you!")
    
    fmt.Println()
    fmt.Println("=== Simple Calculator ===")
    // Get two numbers from user
    fmt.Print("Enter first number: ")
    input1, _ := reader.ReadString('\n')
    input1 = strings.TrimSpace(input1)
    num1, err1 := strconv.ParseFloat(input1, 64)
    if err1 != nil {
        fmt.Println("Invalid number entered!")
        return
    }
    
    fmt.Print("Enter second number: ")
    input2, _ := reader.ReadString('\n')
    input2 = strings.TrimSpace(input2)
    num2, err2 := strconv.ParseFloat(input2, 64)
    if err2 != nil {
        fmt.Println("Invalid number entered!")
        return
    }
    
    // Perform calculations
    sum := num1 + num2
    difference := num1 - num2
    product := num1 * num2
    quotient := num1 / num2
    
    // Display results
    fmt.Printf("%.2f + %.2f = %.2f\n", num1, num2, sum)
    fmt.Printf("%.2f - %.2f = %.2f\n", num1, num2, difference)
    fmt.Printf("%.2f * %.2f = %.2f\n", num1, num2, product)
    fmt.Printf("%.2f / %.2f = %.2f\n", num1, num2, quotient)
    
    fmt.Println()
    fmt.Println("=== Age Calculator ===")
    // Ask for birth year and calculate age
    fmt.Print("What year were you born? ")
    birthYearStr, _ := reader.ReadString('\n')
    birthYearStr = strings.TrimSpace(birthYearStr)
    birthYear, err := strconv.Atoi(birthYearStr)
    if err != nil {
        fmt.Println("Please enter a valid year!")
        return
    }
    
    // Simple age calculation (assuming current year is 2025)
    currentYear := 2025
    age := currentYear - birthYear
    fmt.Printf("If you were born in %d, you are about %d years old.\n", birthYear, age)
    
    fmt.Println()
    fmt.Println("=== Simple Quiz ===")
    // Create a simple quiz
    fmt.Print("What is the capital of France? ")
    answer, _ := reader.ReadString('\n')
    answer = strings.TrimSpace(strings.ToLower(answer))
    
    if answer == "paris" {
        fmt.Println("Correct! Well done!")
    } else {
        fmt.Println("Not quite! The answer is Paris.")
    }
    
    fmt.Println()
    fmt.Println("=== Yes/No Question ===")
    // Get a yes/no response (as text)
    fmt.Print("Do you like Go programming? (yes/no): ")
    response, _ := reader.ReadString('\n')
    response = strings.TrimSpace(strings.ToLower(response))
    
    if response == "yes" || response == "y" {
        fmt.Println("Great! Go is a fantastic language!")
    } else {
        fmt.Println("That's okay, everyone has different preferences!")
    }
    
    fmt.Println()
    fmt.Println("=== Multiple Inputs ===")
    // Collect multiple pieces of information
    fmt.Print("What's your favorite color? ")
    color, _ := reader.ReadString('\n')
    color = strings.TrimSpace(color)
    
    fmt.Print("How many pets do you have? ")
    petStr, _ := reader.ReadString('\n')
    petStr = strings.TrimSpace(petStr)
    petCount, err := strconv.Atoi(petStr)
    if err != nil {
        fmt.Println("Please enter a valid number for pets!")
        petCount = 0  // Default value
    }
    
    fmt.Print("What's your favorite food? ")
    food, _ := reader.ReadString('\n')
    food = strings.TrimSpace(food)
    
    fmt.Println()
    fmt.Println("=== Your Profile ===")
    fmt.Printf("Favorite color: %s\n", color)
    fmt.Printf("Number of pets: %d\n", petCount)
    fmt.Printf("Favorite food: %s\n", food)
    fmt.Printf("Thanks for sharing, %s!\n", name)
    
    fmt.Println()
    fmt.Println("=== Input Validation Example ===")
    // Demonstrate input validation
    fmt.Print("Enter a positive number: ")
    userInput, _ := reader.ReadString('\n')
    userInput = strings.TrimSpace(userInput)
    number, err := strconv.ParseFloat(userInput, 64)
    
    if err != nil {
        fmt.Println("Invalid input! That wasn't a number.")
    } else if number > 0 {
        fmt.Printf("Valid positive number: %.2f\n", number)
        fmt.Printf("Its square is: %.2f\n", number*number)
    } else {
        fmt.Println("That's not a positive number!")
    }
}
```

---

### How to Execute

1. **Create or navigate to a Go module directory** (if not already in one):
   ```bash
   mkdir input-example && cd input-example
   go mod init input
   ```
2. **Copy the code into `input.go`**
3. **Run your program**:
   ```bash
   go run input.go
   ```

**Expected interaction:**
```
=== Interactive Greeting Program ===
What's your name? [User types their name and presses Enter]
Hello, [User's name] ! Nice to meet you!

=== Simple Calculator ===
Enter first number: [User enters a number]
Enter second number: [User enters another number]
[Calculations are performed and results shown]

=== Age Calculator ===
What year were you born? [User enters a year]
[Age calculation is performed and shown]

[Additional prompts will ask for input and respond accordingly...]
```

---

### Success Checklist

- [ ] Created file named `input.go`
- [ ] Created a Go module if needed
- [ ] Program executed without errors
- [ ] Interacted with the program by providing input
- [ ] Saw programs respond to input appropriately
- [ ] Understood how to get input from users

---

### What You Learned!

- **`bufio.NewReader(os.Stdin)`** = Creates a reader for standard input
- **`reader.ReadString('\n')`** = Reads input until newline character
- **`strings.TrimSpace()`** = Removes whitespace including newlines
- **`strconv.Atoi()`/`ParseFloat()`** = Converts strings to numbers
- **Input validation** = Checking if inputs are valid before using them

---

### Try This (Optional Challenges)

1. Create a BMI calculator that asks for height and weight
2. Make a basic chatbot that responds to different inputs
3. Create a simple math quiz with multiple questions
4. Build a program that converts temperatures based on user input

---

## Quick Reference

| Method | Purpose | Example | Notes |
|--------|---------|---------|-------|
| `bufio.NewReader()` | Create input reader | `reader := bufio.NewReader(os.Stdin)` | For text input |
| `reader.ReadString()` | Get text input | `input, _ := reader.ReadString('\n')` | Include delimiter |
| `strings.TrimSpace()` | Remove whitespace | `clean := strings.TrimSpace(input)` | Including newlines |
| `strconv.Atoi()` | String to integer | `num, err := strconv.Atoi("42")` | Returns error |
| `strconv.ParseFloat()` | String to float | `num, err := strconv.ParseFloat("42.5", 64)` | Returns error |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```go
reader := bufio.NewReader(os.Stdin)
```
- **`bufio.NewReader()`** = Creates a buffered reader for efficient input
- **`os.Stdin`** = Standard input (keyboard)
- **Buffered reader** = More efficient than direct input reading

```go
name, _ := reader.ReadString('\n')
```
- **`reader.ReadString()`** = Reads input until specified delimiter
- **`'\n'`** = Newline character (Enter key creates this)
- **`_`** = Blank identifier to ignore error value (not ideal for production)

```go
name = strings.TrimSpace(name)
```
- **`strings.TrimSpace()`** = Removes leading/trailing whitespace
- **Important** because input includes the newline character
- **Alternative**: `strings.TrimSuffix(name, "\n")`

### Input Processing in Go

**Reading different types of input:**
```go
// Reading string
reader := bufio.NewReader(os.Stdin)
text, _ := reader.ReadString('\n')

// Reading integer
input, _ := reader.ReadString('\n')
number, err := strconv.Atoi(strings.TrimSpace(input))

// Reading float
input, _ := reader.ReadString('\n')
number, err := strconv.ParseFloat(strings.TrimSpace(input), 64)
```

### Error Handling

It's important to handle errors from input conversion:

```go
// Proper error handling
input, err := reader.ReadString('\n')
if err != nil {
    fmt.Println("Error reading input:", err)
    return
}
number, err := strconv.Atoi(strings.TrimSpace(input))
if err != nil {
    fmt.Println("Invalid number entered!")
    return
}
// Now you can safely use 'number'
```

### String Manipulation

Common string operations with input:

```go
import "strings"

// Remove whitespace
clean := strings.TrimSpace(input)

// Convert to lowercase for comparison
lower := strings.ToLower(input)

// Split input by a delimiter
parts := strings.Split(input, " ")

// Check if string contains substring
if strings.Contains(input, "hello") { ... }
```

### Converting Strings to Numbers

Go provides several functions to convert strings to numbers:

```go
import "strconv"

// String to integer
intVal, err := strconv.Atoi("123")           // int (base 10)
intVal, err := strconv.ParseInt("123", 10, 64)  // int64 with base and bit size

// String to float
floatVal, err := strconv.ParseFloat("123.45", 64)  // float64

// String to boolean
boolVal, err := strconv.ParseBool("true")   // bool
```

### Alternative Input Methods

**Using fmt.Scanf for formatted input:**
```go
var name string
var age int
fmt.Print("Enter name and age: ")
fmt.Scanf("%s %d", &name, &age)  // Reads formatted input
```

**Note**: `fmt.Scanf` can be trickier to use reliably, so the bufio approach is often preferred.

### Reading a Single Character

```go
fmt.Print("Press any key to continue: ")
char, _, _ := reader.ReadRune()  // Read a single Unicode character
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `unexpected newline` | Not trimming input | Always use `strings.TrimSpace()` |
| `invalid syntax` in ParseInt | Converting non-numeric string | Validate input before conversion |
| `out of range` | Number too large for type | Use appropriate size (int64 vs int32) |
| Input doesn't capture properly | Using wrong delimiter | Use `'\n'` for line-based input |

### Best Practices for Input

**Always validate user input:**
```go
input, _ := reader.ReadString('\n')
input = strings.TrimSpace(input)

// Validate the input
if input == "" {
    fmt.Println("Input cannot be empty!")
    return
}

// Convert and check for errors
number, err := strconv.Atoi(input)
if err != nil {
    fmt.Println("Please enter a valid number!")
    return
}

if number < 0 || number > 100 {
    fmt.Println("Number must be between 0 and 100!")
    return
}
```

**Handle errors properly:**
```go
// Always check errors, especially for number conversion
number, err := strconv.Atoi(input)
if err != nil {
    // Handle the error appropriately
    fmt.Println("Invalid input:", err)
    return  // or continue with default value
}
```

### Security Considerations

When accepting user input:
- **Validation**: Always validate and sanitize input
- **Length limits**: Set reasonable limits on input length
- **Injection attacks**: Be careful with string formatting

### Advanced Challenge (For the Brave!)

Try this full interactive program:

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
    
    fmt.Println("=== Personal Finance Calculator ===")
    
    // Get user's income
    fmt.Print("Enter your monthly income: $")
    incomeStr, _ := reader.ReadString('\n')
    incomeStr = strings.TrimSpace(incomeStr)
    monthlyIncome, err := strconv.ParseFloat(incomeStr, 64)
    if err != nil {
        fmt.Println("Invalid income amount!")
        return
    }
    
    // Get expenses
    fmt.Print("Enter monthly rent: $")
    rentStr, _ := reader.ReadString('\n')
    rentStr = strings.TrimSpace(rentStr)
    rent, err := strconv.ParseFloat(rentStr, 64)
    if err != nil {
        fmt.Println("Invalid rent amount!")
        return
    }
    
    fmt.Print("Enter monthly grocery cost: $")
    groceriesStr, _ := reader.ReadString('\n')
    groceriesStr = strings.TrimSpace(groceriesStr)
    groceries, err := strconv.ParseFloat(groceriesStr, 64)
    if err != nil {
        fmt.Println("Invalid grocery cost!")
        return
    }
    
    fmt.Print("Enter monthly utilities: $")
    utilitiesStr, _ := reader.ReadString('\n')
    utilitiesStr = strings.TrimSpace(utilitiesStr)
    utilities, err := strconv.ParseFloat(utilitiesStr, 64)
    if err != nil {
        fmt.Println("Invalid utilities amount!")
        return
    }
    
    fmt.Print("Enter monthly transportation: $")
    transportStr, _ := reader.ReadString('\n')
    transportStr = strings.TrimSpace(transportStr)
    transportation, err := strconv.ParseFloat(transportStr, 64)
    if err != nil {
        fmt.Println("Invalid transportation amount!")
        return
    }
    
    // Calculate totals
    totalExpenses := rent + groceries + utilities + transportation
    remaining := monthlyIncome - totalExpenses
    savingsPercentage := (remaining / monthlyIncome) * 100
    
    // Display results
    fmt.Println()
    fmt.Println("=== FINANCIAL SUMMARY ===")
    fmt.Printf("Monthly Income: $%.2f\n", monthlyIncome)
    fmt.Printf("Total Expenses: $%.2f\n", totalExpenses)
    fmt.Printf("Remaining: $%.2f\n", remaining)
    fmt.Printf("Savings Rate: %.1f%%\n", savingsPercentage)
    
    if remaining > 0 {
        fmt.Println("Great! You're saving money each month.")
    } else {
        fmt.Println("You're spending more than you earn. Consider reducing expenses.")
    }
}
```

---

 **Excellent work! You now know how to make interactive programs that respond to user input!** 

*Ready for the next challenge? Let's make programs that make decisions!*
