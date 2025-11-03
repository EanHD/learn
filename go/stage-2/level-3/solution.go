package main

import (
    "fmt"
    "math"
)

func main() {
    // Algorithm 1: Complex Arithmetic Expression
    a := 10
    b := 5
    c := 2

    result := (a + b) * c - float64(a) / float64(c)
    fmt.Println("Result: " + fmt.Sprintf("%f", result))

    result2 := float64(a) + float64(b)*float64(c) - float64(a)/float64(c)
    fmt.Println("Result without parentheses: " + fmt.Sprintf("%f", result2))

    result3 := (float64(a+b)*float64(c) - float64(a)) / float64(c)
    fmt.Println("Result with different grouping: " + fmt.Sprintf("%f", result3))

    fmt.Println() // Add some spacing

    // Algorithm 2: Quadratic Formula Calculator
    a2 := 1.0  // Renamed to avoid conflict
    b2 := -5.0
    c2 := 6.0

    discriminant := b2*b2 - 4*a2*c2
    sqrt_discriminant := math.Sqrt(discriminant)
    root1 := (-b2 + sqrt_discriminant) / (2 * a2)
    root2 := (-b2 - sqrt_discriminant) / (2 * a2)

    fmt.Println("Root 1: " + fmt.Sprintf("%f", root1))
    fmt.Println("Root 2: " + fmt.Sprintf("%f", root2))

    fmt.Println() // Add some spacing

    // Algorithm 3: Compound Interest Calculator
    principal := 1000.0
    rate := 0.05
    time := 10.0
    compounds_per_year := 12.0

    amount := principal * math.Pow(1+rate/compounds_per_year, compounds_per_year*time)
    interest := amount - principal

    fmt.Println("Principal: $" + fmt.Sprintf("%.2f", principal))
    fmt.Println("Final Amount: $" + fmt.Sprintf("%.2f", amount))
    fmt.Println("Interest Earned: $" + fmt.Sprintf("%.2f", interest))

    fmt.Println() // Add some spacing

    // Algorithm 4: Geometric Calculations
    radius := 5.0
    side := 4.0
    base := 6.0
    height := 8.0

    circle_area := math.Pi * radius * radius
    circle_circumference := 2 * math.Pi * radius
    square_area := side * side
    square_perimeter := 4 * side
    triangle_area := 0.5 * base * height

    fmt.Println("Circle - Area: " + fmt.Sprintf("%.2f", circle_area) + ", Circumference: " + fmt.Sprintf("%.2f", circle_circumference))
    fmt.Println("Square - Area: " + fmt.Sprintf("%.2f", square_area) + ", Perimeter: " + fmt.Sprintf("%.2f", square_perimeter))
    fmt.Println("Triangle - Area: " + fmt.Sprintf("%.2f", triangle_area))

    fmt.Println() // Add some spacing

    // Algorithm 5: Physics Formula Calculator
    mass := 5.5
    velocity := 10.0
    acceleration := 9.8
    time2 := 3.0  // Renamed to avoid conflict

    kinetic_energy := 0.5 * mass * velocity * velocity
    force := mass * acceleration
    distance := velocity*time2 + 0.5*acceleration*time2*time2
    momentum := mass * velocity

    fmt.Println("Kinetic Energy: " + fmt.Sprintf("%f", kinetic_energy))
    fmt.Println("Force: " + fmt.Sprintf("%f", force))
    fmt.Println("Distance: " + fmt.Sprintf("%f", distance))
    fmt.Println("Momentum: " + fmt.Sprintf("%f", momentum))

    fmt.Println() // Add some spacing

    // Algorithm 6: Temperature Conversion with Multiple Formulas
    celsius := 25.0
    fahrenheit := celsius*9/5 + 32
    kelvin := celsius + 273.15
    celsius_from_f := (fahrenheit - 32) * 5 / 9
    celsius_from_k := kelvin - 273.15

    fmt.Println("Celsius: " + fmt.Sprintf("%f", celsius))
    fmt.Println("Fahrenheit: " + fmt.Sprintf("%f", fahrenheit))
    fmt.Println("Kelvin: " + fmt.Sprintf("%f", kelvin))
    fmt.Println("F to C: " + fmt.Sprintf("%f", celsius_from_f))
    fmt.Println("K to C: " + fmt.Sprintf("%f", celsius_from_k))

    fmt.Println() // Add some spacing

    // Algorithm 7: Statistical Calculations
    num1 := 10.0
    num2 := 20.0
    num3 := 30.0

    sum := num1 + num2 + num3
    average := sum / 3
    range_val := num3 - num1 // assuming num3 is largest, num1 is smallest
    sum_of_squares := num1*num1 + num2*num2 + num3*num3
    mean_of_squares := sum_of_squares / 3
    variance := mean_of_squares - average*average
    std_deviation := math.Sqrt(variance)

    fmt.Println("Sum: " + fmt.Sprintf("%f", sum))
    fmt.Println("Average: " + fmt.Sprintf("%f", average))
    fmt.Println("Range: " + fmt.Sprintf("%f", range_val))
    fmt.Println("Variance: " + fmt.Sprintf("%f", variance))
    fmt.Println("Standard Deviation: " + fmt.Sprintf("%.2f", std_deviation))
}