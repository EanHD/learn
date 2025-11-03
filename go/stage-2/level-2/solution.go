package main

import "fmt"

func main() {
    // Algorithm 1: Simple Variable Swapping
    first_number := 10
    second_number := 20

    fmt.Println("Before swap: first=" + fmt.Sprintf("%d", first_number) + ", second=" + fmt.Sprintf("%d", second_number))

    temp := first_number
    first_number = second_number
    second_number = temp

    fmt.Println("After swap: first=" + fmt.Sprintf("%d", first_number) + ", second=" + fmt.Sprintf("%d", second_number))

    fmt.Println() // Add some spacing

    // Algorithm 2: Running Total Calculator
    total := 0
    count := 0

    number := 5
    total = total + number
    count = count + 1

    number = 10
    total = total + number
    count = count + 1

    number = 15
    total = total + number
    count = count + 1

    average := float64(total) / float64(count)

    fmt.Println("Total: " + fmt.Sprintf("%d", total))
    fmt.Println("Count: " + fmt.Sprintf("%d", count))
    fmt.Println("Average: " + fmt.Sprintf("%.2f", average))

    fmt.Println() // Add some spacing

    // Algorithm 3: Temperature Tracker
    min_temp := 100
    max_temp := -100

    current_temp := 72
    if current_temp < min_temp {
        min_temp = current_temp
    }
    if current_temp > max_temp {
        max_temp = current_temp
    }
    fmt.Println("Current: " + fmt.Sprintf("%d", current_temp) + ", Min: " + fmt.Sprintf("%d", min_temp) + ", Max: " + fmt.Sprintf("%d", max_temp))

    current_temp = 65
    if current_temp < min_temp {
        min_temp = current_temp
    }
    if current_temp > max_temp {
        max_temp = current_temp
    }
    fmt.Println("Current: " + fmt.Sprintf("%d", current_temp) + ", Min: " + fmt.Sprintf("%d", min_temp) + ", Max: " + fmt.Sprintf("%d", max_temp))

    current_temp = 80
    if current_temp < min_temp {
        min_temp = current_temp
    }
    if current_temp > max_temp {
        max_temp = current_temp
    }
    fmt.Println("Current: " + fmt.Sprintf("%d", current_temp) + ", Min: " + fmt.Sprintf("%d", min_temp) + ", Max: " + fmt.Sprintf("%d", max_temp))

    fmt.Println() // Add some spacing

    // Algorithm 4: Account Balance Tracker
    account_balance := 1000.0

    transaction_amount := -50.0
    account_balance = account_balance + transaction_amount
    fmt.Println("Balance after withdrawal: $" + fmt.Sprintf("%.2f", account_balance))

    transaction_amount = 200.0
    account_balance = account_balance + transaction_amount
    fmt.Println("Balance after deposit: $" + fmt.Sprintf("%.2f", account_balance))

    transaction_amount = -75.50
    account_balance = account_balance + transaction_amount
    fmt.Println("Balance after withdrawal: $" + fmt.Sprintf("%.2f", account_balance))

    transaction_amount = 150.25
    account_balance = account_balance + transaction_amount
    fmt.Println("Balance after deposit: $" + fmt.Sprintf("%.2f", account_balance))

    fmt.Println() // Add some spacing

    // Algorithm 5: Student Grade Calculator
    total_points := 0
    possible_points := 0

    assignment_points := 85
    assignment_possible := 100
    total_points = total_points + assignment_points
    possible_points = possible_points + assignment_possible

    assignment_points = 92
    assignment_possible = 100
    total_points = total_points + assignment_points
    possible_points = possible_points + assignment_possible

    assignment_points = 78
    assignment_possible = 100
    total_points = total_points + assignment_points
    possible_points = possible_points + assignment_possible

    percentage := float64(total_points) / float64(possible_points) * 100
    letter_grade := "F"

    if percentage >= 90 {
        letter_grade = "A"
    } else if percentage >= 80 {
        letter_grade = "B"
    } else if percentage >= 70 {
        letter_grade = "C"
    } else if percentage >= 60 {
        letter_grade = "D"
    }

    fmt.Println("Total Points: " + fmt.Sprintf("%d", total_points))
    fmt.Println("Possible Points: " + fmt.Sprintf("%d", possible_points))
    fmt.Println("Percentage: " + fmt.Sprintf("%.2f", percentage))
    fmt.Println("Letter Grade: " + letter_grade)

    fmt.Println() // Add some spacing

    // Algorithm 6: Counter Patterns
    counter := 1
    for counter <= 5 {
        fmt.Println("Count: " + fmt.Sprintf("%d", counter))
        counter = counter + 1
    }

    even_counter := 2
    for even_counter <= 10 {
        fmt.Println("Even: " + fmt.Sprintf("%d", even_counter))
        even_counter = even_counter + 2
    }

    odd_counter := 1
    for odd_counter <= 10 {
        fmt.Println("Odd: " + fmt.Sprintf("%d", odd_counter))
        odd_counter = odd_counter + 2
    }

    fmt.Println() // Add some spacing

    // Algorithm 7: Accumulator Pattern
    sum := 0
    count := 0
    product := 1

    current_value := 3
    sum = sum + current_value
    count = count + 1
    product = product * current_value

    current_value = 4
    sum = sum + current_value
    count = count + 1
    product = product * current_value

    current_value = 5
    sum = sum + current_value
    count = count + 1
    product = product * current_value

    average := float64(sum) / float64(count)

    fmt.Println("Sum: " + fmt.Sprintf("%d", sum))
    fmt.Println("Count: " + fmt.Sprintf("%d", count))
    fmt.Println("Product: " + fmt.Sprintf("%d", product))
    fmt.Println("Average: " + fmt.Sprintf("%.2f", average))
}