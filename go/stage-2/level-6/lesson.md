# Level 6: Functions in Go

## Stage 2: Pseudocode to Code

### Your Task

Translate this pseudocode into Go:

```
PROGRAM: Arithmetic
FUNCTION add(a, b)
  return a + b
FUNCTION multiply(a, b)
  return a * b
MAIN
  print add(5, 3)
  print multiply(4, 7)
```

---

## ANSWER KEY

```go
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
```

---

**Functions with return types!**
