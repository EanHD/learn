# Level 6: Loops and Repetition
## Stage 1: Copying Code

### Today's Mission

Time to make your programs repeat actions! Today you'll learn how to write code that runs multiple times without having to copy and paste. Loops are one of the most powerful concepts in programming.

---

### Learning Goals

- Understand for loops for counting and repetition
- Learn range loops for iterating through collections
- Use break and continue statements to control loops
- Iterate through arrays, slices, and maps
- Create patterns and repetitive calculations

---

### Your Task

**Copy the following code into a new file called `loops.go`**

```go
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
```

---

### How to Execute

1. **Create or navigate to a Go module directory** (if not already in one):
   ```bash
   mkdir loops-example && cd loops-example
   go mod init loops
   ```
2. **Copy the code into `loops.go`**
3. **Run your program**:
   ```bash
   go run loops.go
   ```

**Expected output:**
```
=== For Loop - Counting ===
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5

=== For Loop - Countdown ===
Countdown: 10
Countdown: 9
Countdown: 8
Countdown: 7
Countdown: 6
Countdown: 5
Countdown: 4
Countdown: 3
Countdown: 2
Countdown: 1
Blast off! 🚀

=== For Loop - Even Numbers ===
Even number: 2
Even number: 4
Even number: 6
Even number: 8
Even number: 10

=== For Loop - Sum of Numbers ===
Sum of 1 to 10: 55

=== While Loop Equivalent - Counting ===
While count: 1
While count: 2
While count: 3
While count: 4
While count: 5

=== For Loop with Break ===
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
Number: 6
Found 7, stopping the loop!

=== For Loop with Continue ===
1 is odd - skipping
2 is even - skipping
3 is odd - skipping
4 is even - skipping
5 is odd - skipping
6 is even - skipping
7 is odd - skipping
8 is even - skipping
9 is odd - skipping
10 is even - skipping

=== Range Loop - Array ===
Fruit at index 0: apple
Fruit at index 1: banana
Fruit at index 2: orange
Fruit at index 3: grape
Fruit at index 4: mango

=== Range Loop - Array (Index only) ===
Index: 0, Fruit: apple
Index: 1, Fruit: banana
Index: 2, Fruit: orange
Index: 3, Fruit: grape
Index: 4, Fruit: mango

=== Range Loop - Array (Value only) ===
Fruit: apple
Fruit: banana
Fruit: orange
Fruit: grape
Fruit: mango

=== Range Loop - Map ===
age: 25
height: 175
score: 100

=== Nested Loops - Multiplication Table ===
1	2	3	
2	4	6	
3	6	9	

=== Pattern - Stars ===
* 
* * 
* * * 
* * * * 
* * * * * 

=== Looping Through String Characters ===
Position 0: G (rune: 71)
Position 1: o (rune: 111)
Position 2: ! (rune: 33)

=== Infinite Loop (with break condition) ===
Infinite loop iteration 1
Infinite loop iteration 2
Infinite loop iteration 3
Breaking out of infinite loop
```

---

### Success Checklist

- [ ] Created a file named `loops.go`
- [ ] Created a Go module if needed
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw different types of loops working correctly
- [ ] Understood how break and continue work

---

### Loop Types Summary

- **For loop**: Go's only loop type, can function as for, while, and do-while loops
- **Range loop**: Special syntax for iterating through slices, arrays, maps, and strings
- **Infinite loop**: `for {}` - must use break to exit

---

### Try This (Optional Challenges)

1. Create a Fibonacci sequence generator using loops
2. Build a password validation program that checks multiple requirements
3. Make a prime number checker
4. Create a simple text-based game using loops for turns

---

## Quick Reference

| Loop Type | Syntax | When to Use |
|-----------|--------|-------------|
| For Loop | `for init; condition; increment` | When you know the number of iterations |
| While Equivalent | `for condition` | When you repeat while condition is true |
| Range Loop | `for index, value := range collection` | When iterating through collections |
| Infinite Loop | `for {}` | When you need to loop until break |

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Code Breakdown

```go
for i := 1; i <= 5; i++ {
    fmt.Println("Count:", i)
}
```
- **`for`** = Loop keyword (Go's only loop type)
- **`i := 1`** = Initialization: set up the counter variable
- **`i <= 5`** = Condition: keep looping while this is true
- **`i++`** = Increment: update the counter after each iteration
- **`{}`** = Code block that runs each iteration
- **Loop execution**: 1, 2, 3, 4, 5 (stops when i becomes 6)

```go
for count <= 5 {
    fmt.Println("While count:", count)
    count++
}
```
- **Go doesn't have** while loops, but this for loop acts like one
- **No initialization or increment part** - just the condition
- **Condition checked first** before each iteration

### For Loop Variations

**Different increment patterns:**
```go
// Count by 5s
for i := 0; i <= 25; i += 5 {
    fmt.Println(i) // 0, 5, 10, 15, 20, 25
}

// Count backwards
for i := 10; i > 0; i-- {
    fmt.Println(i) // 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
}

// Infinite loop (be careful!)
for {
    fmt.Println("This runs forever unless there's a break")
    // ... some condition
    // if someCondition { break }
}
```

### Range Loop

Go's `range` is a special loop for iterating over collections:

```go
// For slices/arrays
fruits := []string{"apple", "banana", "orange"}
for index, fruit := range fruits {
    fmt.Println(index, fruit)
    // 0 apple
    // 1 banana
    // 2 orange
}

// For maps
ages := map[string]int{"Alice": 25, "Bob": 30}
for name, age := range ages {
    fmt.Printf("%s is %d years old\n", name, age)
}

// For strings (iterates over runes/characters)
text := "Go"
for i, char := range text {
    fmt.Printf("Position %d: %c\n", i, char)
}
```

**Using blank identifier (`_`)** to ignore the index:
```go
for _, value := range collection {
    // Only care about values, not indices
    fmt.Println(value)
}
```

### Break and Continue

**`break`** = Exits the loop completely:
```go
for i := 1; i <= 10; i++ {
    if i == 5 {
        break  // Loop stops here
    }
    fmt.Println(i)  // Prints: 1, 2, 3, 4
}
```

**`continue`** = Skips the rest of current iteration:
```go
for i := 1; i <= 5; i++ {
    if i == 3 {
        continue  // Skip to next iteration
    }
    fmt.Println(i)  // Prints: 1, 2, 4, 5 (skips 3)
}
```

### Nested Loops

```go
for i := 1; i <= 3; i++ {          // Outer loop
    for j := 1; j <= 3; j++ {      // Inner loop
        fmt.Printf("i=%d, j=%d\n", i, j)
    }
}
```
**Output:**
```
i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
i=2, j=2
i=2, j=3
i=3, j=1
i=3, j=2
i=3, j=3
```
- **Inner loop** completes all iterations for each outer loop iteration
- **Total iterations**: 3 × 3 = 9

### String Iteration

When iterating over strings, Go uses runes (Unicode code points):

```go
text := "Hello"
for i, char := range text {
    fmt.Printf("Index: %d, Character: %c, Rune: %d\n", i, char, char)
}
```

### Loop Performance Considerations

**Minimize work in loops:**
```go
// Avoid: Calculating the same thing every iteration
items := []string{"a", "b", "c"}
for i := 0; i < len(items); i++ {  // len() called every time
    fmt.Println(items[i])
}

// Better: Calculate once
items := []string{"a", "b", "c"}
n := len(items)  // Calculate once
for i := 0; i < n; i++ {  // Use pre-calculated value
    fmt.Println(items[i])
}
```

**Prefer range loops for collections:**
```go
// Range is more idiomatic and often more efficient
for _, item := range items {
    fmt.Println(item)
}
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| Infinite loop | Not updating loop variable | Always update the variable that controls the loop |
| Never executes | Wrong condition | Double-check your condition logic |
| Off-by-one error | `<=` vs `<` confusion | Test with small examples to verify |
| Index out of bounds | Using wrong loop bounds | Use `i < len(slice)` not `i <= len(slice)` |
| Range loop with wrong types | Not matching expected types | Use correct types for index and value |

### When to Use Each Loop Pattern

**Use full for loop when:**
- You need a counter variable
- You're iterating with specific increments
- You need to repeat a known number of times

**Use condition-only for loop when:**
- You don't know how many iterations you need
- You're waiting for a condition to be met

**Use range loop when:**
- You're iterating through arrays, slices, maps, or strings
- You want to access both keys and values (index and element)

**Use infinite for loop with break when:**
- You have complex exit conditions
- You're implementing a state machine or game loop

### Advanced Challenge (For the Brave!)

Try this complex loop program:

```go
package main

import (
    "fmt"
    "math"
)

func main() {
    fmt.Println("=== Advanced Loop Examples ===")

    // Prime number finder
    fmt.Println("Prime numbers from 2 to 30:")
    for num := 2; num <= 30; num++ {
        isPrime := true
        
        // Check if num is divisible by any number from 2 to sqrt(num)
        for divisor := 2; divisor <= int(math.Sqrt(float64(num))); divisor++ {
            if num%divisor == 0 {
                isPrime = false
                break  // Found a divisor, not prime
            }
        }
        
        if isPrime {
            fmt.Printf("%d is prime\n", num)
        }
    }

    fmt.Println()
    // Factorial calculator
    fmt.Println("Factorials from 1 to 7:")
    for n := 1; n <= 7; n++ {
        factorial := 1
        for i := 1; i <= n; i++ {
            factorial *= i
        }
        fmt.Printf("%d! = %d\n", n, factorial)
    }

    fmt.Println()
    // Fibonacci sequence
    fmt.Println("First 10 numbers in Fibonacci sequence:")
    a, b := 0, 1
    fmt.Printf("0: %d\n", a)
    fmt.Printf("1: %d\n", b)

    for i := 2; i < 10; i++ {
        next := a + b
        fmt.Printf("%d: %d\n", i, next)
        a, b = b, next  // Multiple assignment
    }

    fmt.Println()
    // Multiplication table (1-5)
    fmt.Println("Multiplication table (1-5):")
    for i := 1; i <= 5; i++ {
        row := fmt.Sprintf("%d | ", i)
        for j := 1; j <= 5; j++ {
            product := i * j
            row += fmt.Sprintf("%3d ", product)
        }
        fmt.Println(row)
    }
}
```

---

 **Excellent work! You now understand how to repeat actions efficiently with loops!** 

*Ready for the next challenge? Let's learn about functions - the building blocks of reusable code!*