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