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