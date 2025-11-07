# Level 7: Functions - Code Organization

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Welcome to the world of functions! Today you'll learn how to organize your code into reusable pieces called functions. This is where programming becomes truly powerful and professional.

---

### Learning Goals

- Understand what functions are and why they're important
- Learn to define and call functions
- Practice using parameters and return values
- Create reusable code blocks
- Learn about scope and variable access in functions
- Understand different function features in Go

---

### Your Task

**Copy the following code into a new file called `functions.go`**

```
package main

import "fmt"

// Basic function that takes no parameters and returns nothing
func greetUser() {
    fmt.Println("Hello! Welcome to the wonderful world of functions!")
}

// Function with parameters
func greetByName(name string) {
    fmt.Printf("Hello, %s! Nice to meet you!\n", name)
}

// Function with multiple parameters
func introducePerson(name string, age int) {
    fmt.Printf("Hi, I'm %s and I'm %d years old.\n", name, age)
}

// Function with return value
func addNumbers(a int, b int) int {
    sum := a + b
    return sum // Send result back to caller
}

// Function with multiple return values
func divideWithRemainder(a, b int) (int, int) {
    if b == 0 {
        return 0, 0 // Avoid division by zero
    }
    return a / b, a % b // quotient, remainder
}

// Function with named return values
func calculateRectangle(length, width int) (area int, perimeter int) {
    area = length * width      // Direct assignment to named return
    perimeter = 2 * (length + width)
    return // Returns the named variables
}

// Variadic function (accepts variable number of arguments)
func sumAll(numbers ...int) int {
    total := 0
    for _, num := range numbers {
        total += num
    }
    return total
}

// Function that returns multiple different types
func getUserInfo(name string) (string, int, bool) {
    // In a real app, this might get data from a database
    if name == "admin" {
        return name, 30, true
    }
    return name, 25, false
}

func main() {
    fmt.Println("=== Basic Function Definition ===")
    // Call the function
    greetUser()
    greetUser() // Can be called multiple times

    fmt.Println()
    fmt.Println("=== Function with Parameters ===")
    // Call the function with different arguments
    greetByName("Alex")
    greetByName("Taylor")
    greetByName("Jordan")

    fmt.Println()
    fmt.Println("=== Function with Multiple Parameters ===")
    // Call the function with multiple arguments
    introducePerson("Sam", 25)
    introducePerson("Morgan", 30)

    fmt.Println()
    fmt.Println("=== Function with Return Value ===")
    // Use the returned value
    result1 := addNumbers(5, 3)
    result2 := addNumbers(10, 20)
    fmt.Printf("5 + 3 = %d\n", result1)
    fmt.Printf("10 + 20 = %d\n", result2)

    // Functions can be used directly in expressions
    fmt.Printf("The sum of 7 and 8 is: %d\n", addNumbers(7, 8))

    fmt.Println()
    fmt.Println("=== Function with Multiple Return Values ===")
    // Use multiple return values
    quotient, remainder := divideWithRemainder(17, 5)
    fmt.Printf("17 divided by 5: quotient=%d, remainder=%d\n", quotient, remainder)

    // Sometimes you only want one return value
    onlyQuotient, _ := divideWithRemainder(17, 5) // Use blank identifier
    fmt.Printf("Just the quotient: %d\n", onlyQuotient)

    fmt.Println()
    fmt.Println("=== Function with Named Return Values ===")
    area, perimeter := calculateRectangle(10, 5)
    fmt.Printf("Rectangle area: %d, perimeter: %d\n", area, perimeter)

    fmt.Println()
    fmt.Println("=== Variadic Function ===")
    // Call function with different numbers of arguments
    fmt.Printf("Sum of 1,2,3: %d\n", sumAll(1, 2, 3))
    fmt.Printf("Sum of 1,2,3,4,5: %d\n", sumAll(1, 2, 3, 4, 5))
    fmt.Printf("Sum of no numbers: %d\n", sumAll()) // Works with no arguments too

    fmt.Println()
    fmt.Println("=== Function with Mixed Return Types ===")
    name, age, isAdmin := getUserInfo("admin")
    fmt.Printf("Name: %s, Age: %d, Admin: %t\n", name, age, isAdmin)

    name2, age2, isAdmin2 := getUserInfo("regular")
    fmt.Printf("Name: %s, Age: %d, Admin: %t\n", name2, age2, isAdmin2)

    fmt.Println()
    fmt.Println("=== Function Expressions (Anonymous Functions) ===")
    // Define and use an anonymous function immediately
    multiply := func(a, b int) int {
        return a * b
    }

    result := multiply(4, 5)
    fmt.Printf("4 * 5 = %d\n", result)

    // Anonymous function used as an immediately invoked function expression (IIFE)
    func() {
        fmt.Println("This anonymous function runs immediately!")
    }()

    fmt.Println()
    fmt.Println("=== Practical Function Examples ===")
    rectangleArea := calculateAreaRectangle(10, 5)
    circleArea := calculateAreaCircle(7.0)
    fullName := formatFullName("John", "Doe")
    isEven := isNumberEven(12)

    fmt.Printf("Rectangle area (10 x 5): %d\n", rectangleArea)
    fmt.Printf("Circle area (radius 7): %.2f\n", circleArea)
    fmt.Printf("Full name: %s\n", fullName)
    fmt.Printf("Is 12 even? %t\n", isEven)
}

// Additional functions defined outside main
func calculateAreaRectangle(length, width int) int {
    return length * width
}

func calculateAreaCircle(radius float64) float64 {
    return 3.14159 * radius * radius
}

func formatFullName(firstName, lastName string) string {
    return firstName + " " + lastName
}

func isNumberEven(number int) bool {
    return number%2 == 0
}
```

---

### How to Execute

1. **Create or navigate to a Go module directory** (if not already in one):
   ```
   mkdir functions-example && cd functions-example
   go mod init functions
   ```
2. **Copy the code into `functions.go`**
3. **Run your program**:
   ```
   go run functions.go
   ```

**Expected output:**
```
=== Basic Function Definition ===
Hello! Welcome to the wonderful world of functions!
Hello! Welcome to the wonderful world of functions!

=== Function with Parameters ===
Hello, Alex! Nice to meet you!
Hello, Taylor! Nice to meet you!
Hello, Jordan! Nice to meet you!

=== Function with Multiple Parameters ===
Hi, I'm Sam and I'm 25 years old.
Hi, I'm Morgan and I'm 30 years old.

=== Function with Return Value ===
5 + 3 = 8
10 + 20 = 20
The sum of 7 and 8 is: 15

=== Function with Multiple Return Values ===
17 divided by 5: quotient=3, remainder=2
Just the quotient: 3

=== Function with Named Return Values ===
Rectangle area: 50, perimeter: 30

=== Variadic Function ===
Sum of 1,2,3: 6
Sum of 1,2,3,4,5: 15
Sum of no numbers: 0

=== Function with Mixed Return Types ===
Name: admin, Age: 30, Admin: true
Name: regular, Age: 25, Admin: false

=== Function Expressions (Anonymous Functions) ===
4 * 5 = 20
This anonymous function runs immediately!

=== Practical Function Examples ===
Rectangle area (10 x 5): 50
Circle area (radius 7): 153.94
Full name: John Doe
Is 12 even? true
```

---

### Success Checklist

- [ ] Created a file named `functions.go`
- [ ] Created a Go module if needed
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw functions being defined and called correctly
- [ ] Understood parameters, return values, and scope

---

### Function Types Summary

- **Standard functions**: `func name(params) returnType`
- **Multiple return values**: `func name(params) (type1, type2)`
- **Named returns**: `func name(params) (name1 type1, name2 type2)`
- **Variadic functions**: `func name(params ...type)`
- **Anonymous functions**: `func(params) type { }`

---

### Try This (Optional Challenges)

1. Create a calculator with functions for add, subtract, multiply, divide
2. Build a function that validates email addresses
3. Make a function that generates random passwords
4. Create a function that sorts an array of numbers

---

## Quick Reference

| Function Type | Syntax | When to Use |
|---------------|--------|-------------|
| Basic | `func name(params) returnType` | Most common functions |
| Multiple returns | `func name(params) (type1, type2)` | When you need multiple results |
| Named returns | `func name(params) (name1 type1, name2 type2)` | For documentation and clarity |
| Variadic | `func name(params ...type)` | Variable number of arguments |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```
func greetUser() {
    fmt.Println("Hello! Welcome to the wonderful world of functions!")
}
```
- **`func`** = Keyword to declare a function
- **`greetUser`** = Function name (follows Go naming conventions)
- **`()`** = Parameters (empty because no parameters needed)
- **`{}`** = Function body (code that runs when function is called)
- **No return** = Function runs code but doesn't return a value

```
func greetByName(name string) {
    fmt.Printf("Hello, %s! Nice to meet you!\n", name)
}
```
- **`name string`** = Parameter (name is the variable, string is the type)
- **Parameters** = Variables defined in function signature with their types
- **Arguments** = Actual values passed when calling the function

```
func addNumbers(a int, b int) int {
    sum := a + b
    return sum
}
```
- **`a int, b int`** = Multiple parameters with types
- **`int`** after parameters = Return type
- **`return`** = Sends value back to caller

```
result1 := addNumbers(5, 3)
```
- **`addNumbers(5, 3)`** = Function call with arguments
- **`5` and `3`** = Arguments passed to the function
- **Return value** = Value that function sends back
- **`result1`** = Variable that stores the returned value

### Function Declaration Syntax

**Basic function:**
```
func functionName(paramName paramType) returnType {
    // function body
    return value  // if function returns something
}
```

**Multiple parameters of same type:**
```
func add(a, b int) int {  // a and b are both integers
    return a + b
}
```

### Multiple Return Values

Go's unique feature - functions can return multiple values:

```
func divide(a, b float64) (float64, float64) {
    if b == 0 {
        return 0, 0  // return 2 values
    }
    return a/b, math.Mod(a, b)  // quotient and remainder
}

// Usage
quotient, remainder := divide(10, 3)
```

**Ignoring return values with blank identifier:**
```
onlyQuotient, _ := divide(10, 3)  // Ignore the remainder
```

### Named Return Values

Go allows you to name return values in the function signature:

```
func calculate(a, b int) (sum int, diff int) {
    sum = a + b   // Direct assignment to return variable
    diff = a - b  // Direct assignment to return variable
    return        // Returns the named variables automatically
}

// Equivalent to:
func calculate(a, b int) (int, int) {
    sum := a + b
    diff := a - b
    return sum, diff
}
```

### Variadic Functions

Functions that accept a variable number of arguments:

```
func sum(numbers ...int) int {  // ...int means 0 or more int arguments
    total := 0
    for _, num := range numbers {
        total += num
    }
    return total
}

// Usage
fmt.Println(sum(1, 2, 3))        // 6
fmt.Println(sum(1, 2, 3, 4, 5))  // 15
fmt.Println(sum())               // 0
```

**Passing a slice to variadic function:**
```
nums := []int{1, 2, 3, 4, 5}
result := sum(nums...)  // Note the ... to unpack the slice
```

### Function Scope

**Package level:**
```
var globalVar = "I'm accessible everywhere in the package"

func myFunc() {
    localVar := "I'm only accessible inside this function"
    fmt.Println(globalVar)  // OK: Accessing global variable
    fmt.Println(localVar)   // OK: Accessing local variable
}
// fmt.Println(localVar)   // Error: localVar is not accessible here
```

### Anonymous Functions

Functions without a name, often used as values:

```
// Assign function to variable
multiply := func(a, b int) int {
    return a * b
}
result := multiply(5, 3)  // Use like a regular function

// Immediately Invoked Function Expression (IIFE)
result := func(x int) int {
    return x * 2
}(5)  // Function is called immediately with argument 5
```

### First-Class Functions

In Go, functions are first-class values:

```
// Function that takes another function as parameter
func process(numbers []int, operation func(int) int) []int {
    result := make([]int, len(numbers))
    for i, num := range numbers {
        result[i] = operation(num)
    }
    return result
}

// Usage
numbers := []int{1, 2, 3, 4, 5}
doubled := process(numbers, func(n int) int { return n * 2 })
```

### Error Handling Pattern

A common Go pattern returns a value and an error:

```
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}

// Usage
result, err := divide(10, 2)
if err != nil {
    fmt.Println("Error:", err)
    return
}
fmt.Println("Result:", result)
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `undefined: function` | Function name typo or not in same package | Check spelling and package scope |
| Function doesn't return expected value | Forgot `return` statement | Add `return` for values you need |
| `too many arguments` or `not enough arguments` | Wrong number of arguments | Match function definition exactly |
| `cannot use value as type` | Return type mismatch | Ensure return values match declared types |
| `no new variables on left side of :=` | Re-declaring with := | Use `=` for assignment to existing variables |

### Function Best Practices

**Function naming:**
```
// Good - clear and descriptive
func calculateArea(length, width float64) float64 { ... }
func isEmailValid(email string) bool { ... }
func sendNotification(message string) error { ... }

// Go naming conventions: use MixedCaps (camelCase starting with capital)
func CalculateArea(length, width float64) float64 { ... }  // For exportable functions
```

**Function size:**
- Keep functions focused on a single task
- Aim for functions that are 5-10 lines when possible
- If a function gets too long, consider breaking it into smaller ones

**Single Responsibility Principle:**
```
// Good - one purpose
func calculateTax(amount, rate float64) float64 {
    return amount * rate
}

// Better than trying to do everything in one function
func processOrder(order Order) (float64, error) {
    tax := calculateTax(order.Amount, order.TaxRate)
    total := order.Amount + tax
    // ... other processing
    return total, nil
}
```

**Error handling in functions:**
```
import "errors"

func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("cannot divide by zero")
    }
    return a / b, nil
}
```

### Advanced Challenge (For the Brave!)

Try this comprehensive function example:

```
package main

import (
    "fmt"
    "errors"
)

// A comprehensive banking application using functions
func main() {
    fmt.Println("=== Banking Application with Functions ===")

    // Create accounts
    alexAccount, _ := createAccount("Alex", 1000.0)
    taylorAccount, _ := createAccount("Taylor", 500.0)

    // Perform transactions
    deposit(alexAccount, 200.0)
    withdraw(alexAccount, 150.0)
    transfer(alexAccount, taylorAccount, 300.0)
    checkBalance(alexAccount)
    checkBalance(taylorAccount)
}

type Account struct {
    Name     string
    Balance  float64
    History  []Transaction
}

type Transaction struct {
    Type   string
    Amount float64
    BalanceAfter float64
}

// Function to create a bank account object
func createAccount(name string, initialBalance float64) (*Account, error) {
    if initialBalance < 0 {
        return nil, errors.New("initial balance cannot be negative")
    }
    return &Account{
        Name:    name,
        Balance: initialBalance,
        History: []Transaction{},
    }, nil
}

// Function to deposit money
func deposit(account *Account, amount float64) error {
    if amount <= 0 {
        return errors.New("deposit amount must be positive")
    }

    account.Balance += amount
    account.History = append(account.History, Transaction{
        Type: "deposit",
        Amount: amount,
        BalanceAfter: account.Balance,
    })

    fmt.Printf("$%.2f deposited. New balance: $%.2f\n", amount, account.Balance)
    return nil
}

// Function to withdraw money
func withdraw(account *Account, amount float64) error {
    if amount <= 0 {
        return errors.New("withdrawal amount must be positive")
    }

    if amount > account.Balance {
        return errors.New("insufficient funds")
    }

    account.Balance -= amount
    account.History = append(account.History, Transaction{
        Type: "withdrawal",
        Amount: amount,
        BalanceAfter: account.Balance,
    })

    fmt.Printf("$%.2f withdrawn. New balance: $%.2f\n", amount, account.Balance)
    return nil
}

// Function to check balance
func checkBalance(account *Account) {
    fmt.Printf("%s's balance: $%.2f\n", account.Name, account.Balance)
}

// Function to transfer money between accounts
func transfer(fromAccount, toAccount *Account, amount float64) error {
    if err := withdraw(fromAccount, amount); err != nil {
        return fmt.Errorf("transfer failed: %v", err)
    }
    if err := deposit(toAccount, amount); err != nil {
        // If deposit fails, try to reverse the withdrawal (simplified approach)
        deposit(fromAccount, amount) // Attempt to reverse
        return fmt.Errorf("transfer failed: %v", err)
    }
    fmt.Printf("Transfer of $%.2f from %s to %s completed!\n",
               amount, fromAccount.Name, toAccount.Name)
    return nil
}
```

---

 **Excellent work! You now understand how to organize code using functions - a fundamental skill for all programmers!**

*This completes Stage 1 of Go learning! You've mastered the fundamentals of Go programming. Great job!*


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
