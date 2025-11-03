# Level 1: Sum Problem

## Stage 3: Problem to Pseudocode

---

## ANSWER KEY

```go
package main

import "fmt"

func main() {
    sum := 0
    for i := 1; i <= 5; i++ {
        sum = sum + i
    }
    fmt.Println("Sum of 1 to 5 =", sum)
}
```

---

**Accumulator pattern!**
