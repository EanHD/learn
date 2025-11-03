package main

import "fmt"

func main() {
    numbers := []int{10, 20, 30}
    sum := 0
    for i := 0; i < len(numbers); i++ {
        sum = sum + numbers[i]
    }
    fmt.Println("Sum:", sum)
}
