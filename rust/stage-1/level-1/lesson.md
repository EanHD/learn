# Level 1: Hello World
## Stage 1: Copying Code

### Today's Mission

Welcome to your first step into programming with Rust! Today, you'll learn how to create your very first Rust program. Don't worry about understanding everything yet - just focus on getting the code typed correctly and watching it work!

---

### Learning Goals

- Understand the basic structure of a Rust program
- Learn how to compile and run code
- See your first program output "Hello, World!"
- Get comfortable with your text editor

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `hello.rs`**

```rust
fn main() {
    println!("Hello, World!");
}
```

---

### How to Compile and Run

1. **Open your terminal** (or command prompt)
2. **Navigate to where you saved your file**:
   ```bash
   cd /path/to/your/folder
   ```
3. **Compile the code**:
   ```bash
   rustc hello.rs -o hello
   ```
4. **Run your program**:
   ```bash
   ./hello
   ```

**Expected output:**
```
Hello, World!
```

---

### Success Checklist

- [ ] Created a file named `hello.rs`
- [ ] Copied the code exactly as shown
- [ ] Compiled without errors
- [ ] Ran the program successfully
- [ ] Saw "Hello, World!" printed on screen

---

### What Happened?

You just created a real computer program! Here's what each part does:

- `fn main()` - The main function where every Rust program starts
- `println!(...)` - A macro that prints text to the screen
- `"Hello, World!"` - The message to print
- The curly braces `{}` - Define the function body

---

### Try This (Optional Challenges)

If you're feeling brave, try these small changes:

1. Change the message to "Hello, Rust Programming!"
2. Add another println!() line with your name
3. Remove the exclamation mark from println

---

## Need Help with Vim?

Remember to check the `VIM_CHEATSHEET.md` in the root directory for basic Vim commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```rust
fn main() {
```
- **`fn`** = Function keyword - declares a function
- **`main`** = Function name - every Rust program starts here
- **`()`** = Parameters (empty means no inputs needed)
- **`{`** = Opening brace - start of function body

```rust
    println!("Hello, World!");
```
- **`println!`** = Print line macro - prints text followed by newline
- **`!`** = Indicates this is a macro, not a function
- **`"`** = String literal start/end
- **`;`** = Statement terminator - EVERY statement must end with this!

```rust
}
```
- **`}`** = Closing brace - end of function body

### Compilation Process

1. **Parsing**: Code is analyzed for syntax correctness
2. **Type Checking**: Rust checks types and ownership rules
3. **Code Generation**: Converts to machine code
4. **Linking**: Creates the executable file
5. **Result**: Your `hello` program is ready to run!

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `error: expected item, found keyword \`fn\`` | Wrong file extension | Use `.rs` extension, not `.c` |
| `error: unresolved name \`println\`` | Missing exclamation mark | Use `println!()`, not `println()` |
| `error: expected \`;\`, found \`}\`` | Missing semicolon | Add `;` after println! |
| `rustc: command not found` | Rust not installed | Install with: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \| sh` |

### Bonus Knowledge

- **Rust History**: Created by Graydon Hoare, first released in 2010
- **Why "Hello, World!"?**: Tradition started with Brian Kernighan in 1978
- **What is rustc?**: Rust compiler
- **File extensions**: `.rs` for source, no extension for Linux executables

---

 **Congratulations! You've written your first Rust program!** 

*Keep moving forward - next up: Variables!*