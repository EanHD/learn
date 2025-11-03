# Level 7: String Operations in Go

## Stage 2: Pseudocode to Code

### Your Task

Translate this pseudocode into Go:

```
PROGRAM: Greet
1. Store name "Alice"
2. Concatenate "Hello, " + name
3. Print result
```

---

## ANSWER KEY

```go
package main

import "fmt"

func main() {
    name := "Alice"
    greeting := "Hello, " + name
    fmt.Println(greeting)
}
```

---

**String concatenation in Go!**
