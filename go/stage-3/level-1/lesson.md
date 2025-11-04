# Level 1: Sum Problem

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



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
