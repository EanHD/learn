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
    
    // Algorithm 1: Greeting Program
    fmt.Println("Algorithm 1: Greeting Program")
    
    // Display "Hello! What's your name?" to the user
    fmt.Print("Hello! What's your name? ")
    name, _ := reader.ReadString('\n')
    name = strings.TrimSpace(name)
    
    // Display "Nice to meet you, " followed by the user's name
    fmt.Println("Nice to meet you, " + name)
    
    // Display "Welcome to programming!"
    fmt.Println("Welcome to programming!")
    
    fmt.Println() // Add some spacing
    
    // Algorithm 2: Simple Calculator
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
    
    fmt.Println() // Add some spacing
    
    // Algorithm 3: Age Calculator
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
    
    fmt.Println() // Add some spacing
    
    // Algorithm 4: Temperature Converter
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
    
    fmt.Println() // Add some spacing
    
    // Algorithm 5: Rectangle Area Calculator
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
    
    fmt.Println() // Add some spacing
    
    // Algorithm 6: Simple Interest Calculator
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
    
    fmt.Println() // Add some spacing
    
    // Algorithm 7: BMI Calculator
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