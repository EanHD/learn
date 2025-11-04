# Level 1: Hello World

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Welcome to your first step into Go programming! Today, you'll learn how to create your very first Go program. Don't worry about understanding everything yet - just focus on getting the code typed correctly and watching it work!

---

### Learning Goals

- Understand the basic structure of a Go program
- Learn how to compile and run Go code
- See your first program output "Hello, World!"
- Get comfortable with your text editor
- Learn about Go modules and packages

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `hello.go`**

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

---

### How to Execute

1. **Open your terminal** (or command prompt)
2. **Navigate to where you saved your file**:
   ```bash
   cd /path/to/your/folder
   ```
3. **Create a Go module** (if this is your first program in the directory):
   ```bash
   go mod init hello
   ```
4. **Run your program**:
   ```bash
   go run hello.go
   ```

**Expected output:**
```
Hello, World!
```

---

### Success Checklist

- [ ] Created a file named `hello.go`
- [ ] Copied the code exactly as shown
- [ ] Program executed without errors
- [ ] Saw "Hello, World!" printed on screen
- [ ] Understood the basic program structure

---

### What Happened?

You just created a real Go program! Here's what each part does:

- `package main` - Defines this file as part of the main package (executable programs)
- `import "fmt"` - Imports the format package for input/output functions
- `func main()` - The main function where every Go program starts
- `fmt.Println(...)` - A function that prints text to the screen and adds a newline
- `{ }` - Code blocks that contain the function body

Go is a compiled language created by Google, designed to be simple, efficient, and safe!

---

### Try This (Optional Challenges)

If you're feeling brave, try these small changes:

1. Change the message to "Hello, Go Programming!"
2. Add another `fmt.Println()` line with your name
3. Try with different punctuation or emojis: `"Hello, World! 😊"`

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```go
package main
```
- **`package`** = Keyword that defines a package
- **`main`** = Special package name that indicates an executable program
- Every Go program must belong to a package

```go
import "fmt"
```
- **`import`** = Keyword to include other packages
- **`"fmt"`** = Format package that provides functions for formatted I/O
- **Needed for** `fmt.Println()` function

```go
func main() {
    fmt.Println("Hello, World!")
}
```
- **`func`** = Keyword to define a function
- **`main`** = Special function name that's the entry point of every Go program
- **`()`** = Parameters list (empty means no inputs needed)
- **`{ }`** = Code block containing function body
- **`fmt.Println()`** = Function from fmt package to print with newline

### Go Execution Process

1. **Compile**: `go run` or `go build` converts human-readable code to machine code
2. **Execute**: The compiled program runs and produces output
3. **Return**: Program exits and returns control to the terminal

### Go Modules

Go modules manage dependencies and versions:
```bash
go mod init hello        # Creates go.mod file
go mod tidy             # Downloads required dependencies
```

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `command not found: go` | Go not installed | Install Go from golang.org |
| `package main is not a main package` | Missing main function | Ensure you have a main() function |
| `undefined: fmt` | Package not imported | Add `import "fmt"` |
| `syntax error` | Missing brackets, semicolons, etc. | Check syntax carefully |

### Bonus Knowledge

- **Go History**: Created at Google by Robert Griesemer, Rob Pike, and Ken Thompson in 2007
- **Go Name**: Also known as Golang (not to be confused with the Go board game)
- **Why "Hello, World!"?**: Tradition started with Brian Kernighan in 1978 (in C programming)
- **File extensions**: `.go` for Go files
- **Compilation**: Go compiles to fast, efficient native binaries

---

 **Congratulations! You've written your first Go program!** 

*Keep moving forward - next up: Variables!*