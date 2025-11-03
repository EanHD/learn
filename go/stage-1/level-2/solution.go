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