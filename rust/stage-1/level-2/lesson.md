# Level 2: Variables

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Now that you know how to create and run a basic Rust program, let's learn about variables! Variables are like containers that store data. You'll learn how to declare variables, assign values, and display them.

---

### Learning Goals

- Understand what variables are and why we use them
- Learn different data types in Rust
- Practice declaring and using variables
- See how variables make code more flexible

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `variables.rs`**

```rust
fn main() {
    // Integer variable
    let x = 42;
    
    // Floating-point variable
    let pi = 3.14159;
    
    // String variable
    let greeting = "Hello, Rust!";
    
    // Boolean variable
    let is_rust_fun = true;
    
    // Print the variables
    println!("x = {}", x);
    println!("pi = {}", pi);
    println!("greeting = {}", greeting);
    println!("is_rust_fun = {}", is_rust_fun);
}
```

---

### How to Compile and Run

1. **Navigate to your working directory**:
   ```bash
   cd /path/to/your/folder
   ```
2. **Compile the code**:
   ```bash
   rustc variables.rs -o variables
   ```
3. **Run your program**:
   ```bash
   ./variables
   ```

**Expected output:**
```
x = 42
pi = 3.14159
greeting = Hello, Rust!
is_rust_fun = true
```

---

### Success Checklist

- [ ] Created a file named `variables.rs`
- [ ] Copied the code exactly as shown
- [ ] Compiled without errors
- [ ] Ran the program successfully
- [ ] Saw all variable values printed correctly

---

### What Happened?

Variables are the building blocks of programming! Here's what you learned:

- **`let`** - Keyword to declare a variable
- **Variable names** - Like `x`, `pi`, `greeting` (descriptive names are better!)
- **Data types** - Rust infers types automatically (integers, floats, strings, booleans)
- **`{}` in println!** - Placeholders for variable values
- **Comments** - `//` starts a comment (ignored by compiler)

---

### Try This (Optional Challenges)

Experiment with these modifications:

1. Change the values of the variables
2. Add a new variable with your name
3. Try printing multiple variables in one println! statement
4. Change `true` to `false` and see what happens

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```rust
fn main() {
```
- Same as before - entry point of the program

```rust
    // Integer variable
    let x = 42;
```
- **`let`** = Variable declaration keyword
- **`x`** = Variable name (identifier)
- **`42`** = Integer literal value
- **`;`** = Statement end

```rust
    // Floating-point variable
    let pi = 3.14159;
```
- **`pi`** = Variable name
- **`3.14159`** = Floating-point literal (decimal number)

```rust
    // String variable
    let greeting = "Hello, Rust!";
```
- **`"Hello, Rust!"`** = String literal (text)
- Strings are enclosed in double quotes

```rust
    // Boolean variable
    let is_rust_fun = true;
```
- **`true`** = Boolean literal (true/false values)

```rust
    // Print the variables
    println!("x = {}", x);
```
- **`{}`** = Placeholder for variable value
- **`x`** = Variable to insert at placeholder

### Variable Types in Rust

| Type | Example | Description |
|------|---------|-------------|
| `i32` | `42` | 32-bit signed integer |
| `f64` | `3.14159` | 64-bit floating point |
| `&str` | `"hello"` | String slice |
| `bool` | `true` | Boolean (true/false) |

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `error: expected expression, found keyword \`let\`` | Missing semicolon on previous line | Add `;` after previous statement |
| `error: cannot find value \`x\` in this scope` | Using variable before declaration | Move `println!` after `let x = ...` |
| `error: mismatched types` | Wrong type assignment | Use correct literal syntax |

### Bonus Knowledge

- **Type Inference**: Rust figures out types automatically
- **Immutability**: Variables are immutable by default (can't change value)
- **Ownership**: Rust's unique memory management system
- **Snake Case**: Rust convention for variable names (`my_variable`)

---

 **Great job! You now understand variables in Rust!** 

*Next: Basic Math Operations!*
