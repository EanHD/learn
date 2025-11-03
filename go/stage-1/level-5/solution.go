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
    score := 88
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