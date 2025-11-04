# Level 5: Conditionals and Decision Making

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Time to make programs that can make decisions! Today you'll learn how to write code that does different things based on different conditions. This is where programs become truly intelligent!

---

### Learning Goals

- Understand if/else statements and decision making
- Learn comparison operators (==, !=, <, >, <=, >=)
- Practice logical operators (&&, ||, !)
- Create programs that respond differently to different inputs
- Learn to chain multiple conditions together

---

### Your Task

**Copy the following code into a new file called `conditionals.go`**

```go
package main

import "fmt"

func main() {
    fmt.Println("=== Simple Age Check ===")
    // Input for age
    age := 20

    if age >= 18 {
        fmt.Println("You are an adult (18 or older)")
    } else {
        fmt.Println("You are a minor (under 18)")
    }

    fmt.Println()
    fmt.Println("=== Grade Classifier ===")
    // Input for grade
    grade := 85

    if grade >= 90 {
        fmt.Println("Grade: A (90-100)")
    } else if grade >= 80 {
        fmt.Println("Grade: B (80-89)")
    } else if grade >= 70 {
        fmt.Println("Grade: C (70-79)")
    } else if grade >= 60 {
        fmt.Println("Grade: D (60-69)")
    } else {
        fmt.Println("Grade: F (below 60)")
    }

    fmt.Println()
    fmt.Println("=== Temperature Adviser ===")
    // Input for temperature
    temperature := 75 // in Fahrenheit

    if temperature > 80 {
        fmt.Println("It's hot! Stay hydrated and wear light clothes.")
    } else if temperature > 60 {
        fmt.Println("It's a nice day! Perfect for outdoor activities.")
    } else {
        fmt.Println("It's cold! Don't forget your jacket.")
    }

    fmt.Println()
    fmt.Println("=== Username and Password Check ===")
    // Input for login
    username := "admin"
    password := "secret123"

    if username == "admin" && password == "secret123" {
        fmt.Println("Login successful! Welcome, admin.")
    } else {
        fmt.Println("Login failed! Invalid username or password.")
    }

    fmt.Println()
    fmt.Println("=== Multiple Condition Check ===")
    // Check if number is positive, even, and greater than 10
    number := 12

    if number > 0 {
        fmt.Println("The number is positive")
        if number%2 == 0 {
            fmt.Println("The number is even")
            if number > 10 {
                fmt.Println("The number is greater than 10")
                fmt.Println("This number is positive, even, and greater than 10!")
            } else {
                fmt.Println("This number is positive and even, but not greater than 10")
            }
        } else {
            fmt.Println("This number is positive and odd")
        }
    } else {
        fmt.Println("This number is not positive")
    }

    fmt.Println()
    fmt.Println("=== Logical Operators Demo ===")
    hasID := true
    hasMoney := true
    ageCheck := 21

    // Using AND operator (&&) - all conditions must be true
    if hasID && hasMoney && ageCheck >= 18 {
        fmt.Println("You can buy alcohol (if you're 18+ and have ID & money)")
    } else {
        fmt.Println("Cannot purchase: Missing ID, money, or age requirement")
    }

    // Using OR operator (||) - at least one condition must be true
    hasCreditCard := false
    hasDebitCard := true
    hasCash := false

    if hasCreditCard || hasDebitCard || hasCash {
        fmt.Println("Payment method available")
    } else {
        fmt.Println("No payment method available")
    }

    // Using NOT operator (!) - reverses the condition
    isRaining := false
    if !isRaining {
        fmt.Println("It's not raining, so no need for an umbrella!")
    } else {
        fmt.Println("It's raining, bring an umbrella!")
    }

    fmt.Println()
    fmt.Println("=== Switch Statement Demo ===")
    dayOfWeek := 3 // 1=Monday, 2=Tuesday, etc.

    switch dayOfWeek {
    case 1:
        fmt.Println("Today is Monday - start of the work week")
    case 2:
        fmt.Println("Today is Tuesday")
    case 3:
        fmt.Println("Today is Wednesday - middle of the week")
    case 4:
        fmt.Println("Today is Thursday")
    case 5:
        fmt.Println("Today is Friday - weekend is almost here!")
    case 6:
        fmt.Println("Today is Saturday - weekend fun!")
    case 7:
        fmt.Println("Today is Sunday - rest day")
    default:
        fmt.Println("Invalid day number! Please enter 1-7")
    }

    fmt.Println()
    fmt.Println("=== Switch with Multiple Values ===")
    gradeLetter := "B"

    switch gradeLetter {
    case "A", "A+":
        fmt.Println("Excellent performance!")
    case "B+", "B":
        fmt.Println("Good job!")
    case "C", "C+":
        fmt.Println("Satisfactory performance")
    case "D", "F":
        fmt.Println("Needs improvement")
    default:
        fmt.Println("Invalid grade")
    }

    fmt.Println()
    fmt.Println("=== Switch with Expressions ===")
    score := 88

    switch {
    case score >= 97:
        fmt.Println("Grade: A+")
    case score >= 93:
        fmt.Println("Grade: A")
    case score >= 90:
        fmt.Println("Grade: A-")
    case score >= 87:
        fmt.Println("Grade: B+")
    case score >= 83:
        fmt.Println("Grade: B")
    case score >= 80:
        fmt.Println("Grade: B-")
    case score >= 77:
        fmt.Println("Grade: C+")
    case score >= 73:
        fmt.Println("Grade: C")
    case score >= 70:
        fmt.Println("Grade: C-")
    default:
        fmt.Println("Grade: D or F")
    }

    fmt.Println()
    fmt.Println("=== Ternary Operator Alternative ===")
    // Go doesn't have a ternary operator, but you can create a function
    score = 88
    result := ternary(score >= 60, "Pass", "Fail")
    fmt.Printf("Score: %d, Result: %s\n", score, result)
}

// Helper function to simulate ternary operator
func ternary(condition bool, a string, b string) string {
    if condition {
        return a
    }
    return b
}
```

---

### How to Execute

1. **Create or navigate to a Go module directory** (if not already in one):
   ```bash
   mkdir conditionals-example && cd conditionals-example
   go mod init conditionals
   ```
2. **Copy the code into `conditionals.go`**
3. **Run your program**:
   ```bash
   go run conditionals.go
   ```

**Expected output:**
```
=== Simple Age Check ===
You are an adult (18 or older)

=== Grade Classifier ===
Grade: B (80-89)

=== Temperature Adviser ===
It's a nice day! Perfect for outdoor activities.

=== Username and Password Check ===
Login successful! Welcome, admin.

=== Multiple Condition Check ===
The number is positive
The number is even
The number is greater than 10
This number is positive, even, and greater than 10!

=== Logical Operators Demo ===
You can buy alcohol (if you're 18+ and have ID & money)
Payment method available
It's not raining, so no need for an umbrella!

=== Switch Statement Demo ===
Today is Wednesday - middle of the week

=== Switch with Multiple Values ===
Good job!

=== Switch with Expressions ===
Grade: B+
Score: 88, Result: Pass
```

---

### Success Checklist

- [ ] Created a file named `conditionals.go`
- [ ] Created a Go module if needed
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw different code paths execute based on conditions
- [ ] Understood if/else statements and logical operators

---

### Understanding Comparison Operators

In Go conditionals, you'll use these comparison operators:

- **`==`** = Equal to
- **`!=`** = Not equal to
- **`<`** = Less than
- **`>`** = Greater than
- **`<=`** = Less than or equal to
- **`>=`** = Greater than or equal to

---

### Try This (Optional Challenges)

1. Create a BMI classifier that gives different advice based on BMI ranges
2. Build a program that determines if a year is a leap year
3. Make a simple game where the computer picks a number and the user guesses
4. Create a traffic light simulator using conditionals

---

## Quick Reference

| Operator | Name | Purpose | Example | Result |
|----------|------|---------|---------|--------|
| `==` | Equal | Value comparison | `5 == 5` | `true` |
| `!=` | Not Equal | Value not equal | `5 != 3` | `true` |
| `<` | Less Than | Left less than right | `3 < 5` | `true` |
| `>` | Greater Than | Left greater than right | `5 < 3` | `true` |
| `<=` | Less or Equal | Left less than or equal | `5 <= 5` | `true` |
| `>=` | Greater or Equal | Left greater or equal | `5 >= 3` | `true` |
| `&&` | AND | Both conditions true | `true && false` | `false` |
| `||` | OR | At least one true | `true || false` | `true` |
| `!` | NOT | Reverse the condition | `!true` | `false` |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```go
if age >= 18 {
    fmt.Println("You are an adult (18 or older)")
} else {
    fmt.Println("You are a minor (under 18)")
}
```
- **`if`** = Start of conditional statement
- **`age >= 18`** = Condition that evaluates to true or false
- **`{}`** = Code block executed if condition is true
- **`else`** = Code block executed if condition is false

```go
if grade >= 90 {
    fmt.Println("Grade: A (90-100)")
} else if grade >= 80 {
    fmt.Println("Grade: B (80-89)")
} else if grade >= 70 {
    fmt.Println("Grade: C (70-79)")
} else if grade >= 60 {
    fmt.Println("Grade: D (60-69)")
} else {
    fmt.Println("Grade: F (below 60)")
}
```
- **`else if`** = Additional condition to check if the first was false
- **Execution order** matters: Go checks each condition in order and executes the first true one
- **Only one block** executes, not multiple blocks

```go
if username == "admin" && password == "secret123" {
    fmt.Println("Login successful! Welcome, admin.")
} else {
    fmt.Println("Login failed! Invalid username or password.")
}
```
- **`&&`** = Logical AND operator (both conditions must be true)
- **`==`** = Equality comparison operator
- **Security** considerations: Never hardcode credentials in real programs

### Comparison Operators Deep Dive

**Equality vs Assignment:**
```go
// Wrong! This assigns a value (would cause a compilation error)
if username = "admin" {  // ERROR: Cannot use assignment in condition

// Correct! This compares values
if username == "admin" {  // OK: Equality comparison
```

### Logical Operators

| Operator | Symbol | What it does | Example | Result |
|----------|--------|--------------|---------|--------|
| AND | `&&` | Both conditions true | `true && false` | `false` |
| OR | `||` | At least one true | `true || false` | `true` |
| NOT | `!` | Reverse condition | `!true` | `false` |

**More Examples:**
```go
// AND: All conditions must be true
age := 21
hasID := true
hasMoney := true
if age >= 21 && hasID && hasMoney {
    fmt.Println("Can buy alcohol")
}

// OR: At least one condition must be true
credit := true
debit := false
cash := false
if credit || debit || cash {
    fmt.Println("Payment available")
}

// NOT: Reverses the condition
isLoggedIn := false
if !isLoggedIn {
    fmt.Println("Please log in first")
}
```

### Nested Conditionals

```go
if number > 0 {
    fmt.Println("The number is positive")
    if number%2 == 0 {        // Nested if
        fmt.Println("The number is even")
        if number > 10 {         // Double nested if
            fmt.Println("The number is greater than 10")
        }
    }
}
```
- **Inner condition** only evaluated if outer condition is true
- **Be careful** with nesting - too deep can be hard to read

### Switch Statement

```go
switch dayOfWeek {
case 1:
    fmt.Println("Today is Monday")
case 2:
    fmt.Println("Today is Tuesday")
default:  // Executes if no case matches
    fmt.Println("Invalid day number")
}
```
- **Alternative to long if/else if** chains
- **Automatic break** after each case (no fallthrough by default)
- **`default`** = Catch-all case when no others match
- **`fallthrough`** keyword allows fallthrough behavior if needed

### Switch Variations

**Multiple values in one case:**
```go
grade := "A"
switch grade {
case "A", "A+", "A-":  // Multiple values
    fmt.Println("Excellent!")
case "B", "B+":
    fmt.Println("Good!")
}
```

**Switch without expression (like if/else if):**
```go
score := 88
switch {
case score >= 90:
    fmt.Println("A grade")
case score >= 80:
    fmt.Println("B grade")
case score >= 70:
    fmt.Println("C grade")
default:
    fmt.Println("F grade")
}
```

### Go's Logical Short-Circuiting

Go uses short-circuit evaluation for `&&` and `||`:

```go
// With &&, if the first condition is false, the second is not evaluated
if x != 0 && 10/x > 2 {  // If x is 0, 10/x is never evaluated (no division by zero)
    fmt.Println("This is safe!")
}

// With ||, if the first condition is true, the second is not evaluated
if x == 0 || 10/x > 2 {  // If x is 0, 10/x is never evaluated
    fmt.Println("This is also safe!")
}
```

### No Ternary Operator in Go

Unlike many languages, Go doesn't have a ternary operator (`condition ? a : b`). Instead, use if/else or a function:

```go
// Instead of: result = condition ? value1 : value2
var result string
if condition {
    result = value1
} else {
    result = value2
}

// Or create a helper function (as shown in the lesson):
func ternary(condition bool, a string, b string) string {
    if condition {
        return a
    }
    return b
}
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `expected '==', found '='` | Using `=` instead of `==` | Use `==` for comparison, `=` for assignment |
| `missing condition in switch` | Forgot expression in switch | Use `switch` without expression for if/else if pattern |
| Fallthrough behavior | Unexpected execution flow | Go doesn't fall through by default, use `fallthrough` if needed |
| Confusing `&&` and `||` | Wrong logic | Remember: AND needs ALL true, OR needs ANY true |
| Forgetting required brackets in if | Missing opening parenthesis | Always use `if (condition)` in some languages, but Go is `if condition` |

Wait, let me correct that last point - Go doesn't require parentheses around conditions:

### Corrected Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `expected '==', found '='` | Using `=` instead of `==` | Use `==` for comparison, `=` for assignment |
| `missing condition in switch` | Forgot expression in switch | Use `switch` without expression for if/else if pattern |
| Fallthrough behavior | Unexpected execution flow | Go doesn't fall through by default, use `fallthrough` if needed |
| Confusing `&&` and `||` | Wrong logic | Remember: AND needs ALL true, OR needs ANY true |
| Using parentheses around conditions | Thinking it's required like other languages | Go allows but doesn't require parentheses around conditions |

### Best Practices for Conditionals

**Use descriptive variable names:**
```go
// Good
if isAdult { ... }
if isValidEmail { ... }

// Avoid
if x { ... }
if flag { ... }
```

**Keep conditions simple:**
```go
// Good - store complex condition in variable
canVote := age >= 18 && isCitizen && !isInPrison
if canVote { ... }

// Avoid - hard to read
if age >= 18 && isCitizen && !isInPrison { ... }
```

**Consider switch vs if/else if:**
- Use `switch` for exact value matching
- Use `if/else if` for ranges and complex conditions

### Advanced Challenge (For the Brave!)

Try this complex conditional program:

```go
package main

import "fmt"

func main() {
    // A simple grading system with lots of conditions
    studentName := "Alex"
    examScore := 88
    homeworkScore := 92
    participation := true

    fmt.Println("=== Student Report for", studentName, "===")

    // Calculate overall grade
    overallScore := (float64(examScore) * 0.7) + (float64(homeworkScore) * 0.3)
    fmt.Printf("Overall Score: %.2f\n", overallScore)

    // Determine letter grade
    var letterGrade string
    if overallScore >= 97 {
        letterGrade = "A+"
    } else if overallScore >= 93 {
        letterGrade = "A"
    } else if overallScore >= 90 {
        letterGrade = "A-"
    } else if overallScore >= 87 {
        letterGrade = "B+"
    } else if overallScore >= 83 {
        letterGrade = "B"
    } else if overallScore >= 80 {
        letterGrade = "B-"
    } else if overallScore >= 77 {
        letterGrade = "C+"
    } else if overallScore >= 73 {
        letterGrade = "C"
    } else if overallScore >= 70 {
        letterGrade = "C-"
    } else if overallScore >= 67 {
        letterGrade = "D+"
    } else if overallScore >= 63 {
        letterGrade = "D"
    } else if overallScore >= 60 {
        letterGrade = "D-"
    } else {
        letterGrade = "F"
    }

    fmt.Println("Letter Grade:", letterGrade)

    // Special recognition
    switch {
    case letterGrade == "A+" && participation:
        fmt.Println("Outstanding performance! Keep up the excellent work!")
    case letterGrade == "A" || letterGrade == "A+":
        fmt.Println("Excellent work! Very impressive!")
    case letterGrade == "B" || letterGrade == "B+":
        fmt.Println("Good job! You're doing well!")
    case overallScore >= 70:
        fmt.Println("Satisfactory performance. Keep trying!")
    default:
        fmt.Println("Please see your instructor for additional help.")
    }

    // Graduation eligibility
    if overallScore >= 75 && participation {
        fmt.Println("Eligible for graduation with honors consideration")
    } else if overallScore >= 60 {
        fmt.Println("Eligible for graduation")
    } else {
        fmt.Println("Not eligible for graduation, must repeat course")
    }
}
```

---

 **Excellent work! You now understand how to make your programs make intelligent decisions!** 

*Ready for the next challenge? Let's learn about loops and repetition!*