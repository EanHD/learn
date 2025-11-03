# Level 5: Slices in Go

## Stage 2: Pseudocode to Code

### Your Task

Translate this pseudocode into Go:

```
PROGRAM: Sum Array
1. Create slice [10, 20, 30]
2. Loop through
3. Sum values
4. Print sum
```

---

## ANSWER KEY

```go
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
```

---

**Slices and accumulators!**
