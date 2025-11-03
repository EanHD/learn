package main

import "fmt"

func add(a int, b int) int {
    return a + b
}

func multiply(a int, b int) int {
    return a * b
}

func main() {
    fmt.Println(add(5, 3))
    fmt.Println(multiply(4, 7))
}
