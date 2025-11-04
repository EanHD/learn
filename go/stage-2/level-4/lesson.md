# Level 4: Loops in Go

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 2: Pseudocode to Code

### Your Task

Translate this pseudocode into Go:

```
PROGRAM: Count
1. Loop from 1 to 10
2. Print each number
```

---

## ANSWER KEY

```go
package main

import "fmt"

func main() {
    for i := 1; i <= 10; i++ {
        fmt.Println(i)
    }
}
```

---

**For loops and iteration!**
