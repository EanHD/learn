package main

import "fmt"

func main() {
    fmt.Println("=== For Loop - Counting ===")
    // Basic for loop: for initialization; condition; increment
    for i := 1; i <= 5; i++ {
        fmt.Println("Count:", i)
    }

    fmt.Println()
    fmt.Println("=== For Loop - Countdown ===")
    // Countdown from 10 to 1
    for i := 10; i >= 1; i-- {
        fmt.Println("Countdown:", i)
    }
    fmt.Println("Blast off! 🚀")

    fmt.Println()
    fmt.Println("=== For Loop - Even Numbers ===")
    // Print even numbers from 2 to 10
    for i := 2; i <= 10; i += 2 {
        fmt.Println("Even number:", i)
    }

    fmt.Println()
    fmt.Println("=== For Loop - Sum of Numbers ===")
    // Calculate sum of numbers 1 to 10
    sum := 0
    for i := 1; i <= 10; i++ {
        sum += i // Same as: sum = sum + i
    }
    fmt.Printf("Sum of 1 to 10: %d\n", sum)

    fmt.Println()
    fmt.Println("=== While Loop Equivalent - Counting ===")
    // Go doesn't have while loops, but for loops can simulate them
    count := 1
    for count <= 5 {
        fmt.Println("While count:", count)
        count++
    }

    fmt.Println()
    fmt.Println("=== For Loop with Break ===")
    // Using break to exit a loop early
    for i := 1; i <= 10; i++ {
        if i == 7 {
            fmt.Println("Found 7, stopping the loop!")
            break // Exit the loop completely
        }
        fmt.Println("Number:", i)
    }

    fmt.Println()
    fmt.Println("=== For Loop with Continue ===")
    // Using continue to skip an iteration
    for i := 1; i <= 10; i++ {
        if i%2 == 0 { // If even number
            fmt.Printf("%d is even - skipping\n", i)
            continue // Skip the rest of this iteration
        }
        fmt.Printf("Odd number: %d\n", i)
    }

    fmt.Println()
    fmt.Println("=== Range Loop - Array ===")
    // Loop through an array/slice
    fruits := []string{"apple", "banana", "orange", "grape", "mango"}

    for index, fruit := range fruits {
        fmt.Printf("Fruit at index %d: %s\n", index, fruit)
    }

    fmt.Println()
    fmt.Println("=== Range Loop - Array (Index only) ===")
    // If you only need the index
    for index := range fruits {
        fmt.Printf("Index: %d, Fruit: %s\n", index, fruits[index])
    }

    fmt.Println()
    fmt.Println("=== Range Loop - Array (Value only) ===")
    // If you only need the value (use blank identifier for index)
    for _, fruit := range fruits {
        fmt.Printf("Fruit: %s\n", fruit)
    }

    fmt.Println()
    fmt.Println("=== Range Loop - Map ===")
    // Loop through a map (key-value pairs)
    person := map[string]int{
        "age": 25,
        "height": 175,
        "score": 100,
    }

    for key, value := range person {
        fmt.Printf("%s: %d\n", key, value)
    }

    fmt.Println()
    fmt.Println("=== Nested Loops - Multiplication Table ===")
    // Create a multiplication table (3x3)
    for i := 1; i <= 3; i++ {
        row := ""
        for j := 1; j <= 3; j++ {
            product := i * j
            row += fmt.Sprintf("%d\t", product) // \t is a tab character
        }
        fmt.Println(row)
    }

    fmt.Println()
    fmt.Println("=== Pattern - Stars ===")
    // Create a right triangle pattern
    for i := 1; i <= 5; i++ {
        pattern := ""
        for j := 1; j <= i; j++ {
            pattern += "* "
        }
        fmt.Println(pattern)
    }

    fmt.Println()
    fmt.Println("=== Looping Through String Characters ===")
    // Loop through each character in a string
    message := "Go!"
    for i, char := range message {
        fmt.Printf("Position %d: %c (rune: %d)\n", i, char, char)
    }

    fmt.Println()
    fmt.Println("=== Infinite Loop (with break condition) ===")
    // Example of a loop with a break condition instead of a counter
    counter := 0
    for {
        counter++
        fmt.Printf("Infinite loop iteration %d\n", counter)
        if counter >= 3 {
            fmt.Println("Breaking out of infinite loop")
            break
        }
    }
}