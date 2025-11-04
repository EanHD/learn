# Level 1: Basic Pseudocode Translation

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Welcome to Stage 2! Now that you understand Rust syntax, you'll learn to translate written instructions (pseudocode) into working code. This is a crucial skill for programming - turning ideas into reality!

---

### Learning Goals

- Understand pseudocode as a programming planning tool
- Practice translating written logic to Rust code
- Learn the step-by-step process of implementation
- Build confidence in converting ideas to code

---

### Your Task

**Read the pseudocode below, then write the equivalent Rust code in a file called `basic_translation.rs`**


### How to Run

1. **Compile the code**:
   ```bash
   rustc hello.rs -o hello hello.rs
   ```rust

2. **Run your program**:
   ```bash
   ./hello hello
   ```rust

**Expected output:**
```rust
Hello, World!
```rust

### Pseudocode:
```rust
START PROGRAM
    DISPLAY "Welcome to Rust programming!"
    DISPLAY "This is your first pseudocode translation!"
END PROGRAM
```rust

**Your task:** Create a Rust program that does exactly what the pseudocode describes.

---

### How to Create Your Solution

1. **Navigate to your working directory**:
   ```bash
   cd /path/to/your/folder
   ```rust
2. **Create your code file**:
   ```bash
   touch basic_translation.rs
   ```rust
3. **Write the Rust code** that matches the pseudocode
4. **Compile and test**:
   ```bash
   rustc basic_translation.rs -o basic_translation
   ./basic_translation
   ```rust

**Expected output:**
```rust
Welcome to Rust programming!
This is your first pseudocode translation!
```rust

---

### Success Checklist

- [ ] Created `basic_translation.rs` file
- [ ] Wrote Rust code that matches the pseudocode exactly
- [ ] Program compiles without errors
- [ ] Output matches expected result
- [ ] Code follows Rust conventions

---

### What Did You Learn?

Pseudocode is like a recipe - it describes what to do in plain English. Your job is to translate it to the specific "language" of Rust code.

**Key Translation Points:**
- `START PROGRAM` → `fn main() {`
- `DISPLAY "text"` → `println!("text");`
- `END PROGRAM` → `}`

---

### Try This (Optional Challenges)

1. Add another DISPLAY line with your own message
2. Change the messages to something fun
3. Try different quote styles (but remember Rust uses double quotes!)

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Step-by-Step Translation

**Pseudocode:**
```rust
START PROGRAM
    DISPLAY "Welcome to Rust programming!"
    DISPLAY "This is your first pseudocode translation!"
END PROGRAM
```rust

**Rust Code:**
```rust
fn main() {
    println!("Welcome to Rust programming!");
    println!("This is your first pseudocode translation!");
}
```rust

### Translation Guide

| Pseudocode | Rust Code | Explanation |
|------------|-----------|-------------|
| `START PROGRAM` | `fn main() {` | Program entry point |
| `DISPLAY "text"` | `println!("text");` | Print with newline |
| `END PROGRAM` | `}` | Close main function |

### Common Mistakes & Solutions

| Common Error | Why It Happens | Solution |
|--------------|----------------|----------|
| `println("text")` | Forgot `!` | Use `println!("text")` |
| `print!("text")` | Wrong function | Use `println!` for lines |
| `fn main()` | Missing braces | Add `{ }` around function body |
| Wrong quotes | Used single quotes | Rust strings use double quotes |

### Bonus Knowledge

- **Pseudocode Standards**: Different programmers use different styles
- **Comments**: You can add `//` comments to explain your code
- **Readability**: Good code is clear and self-documenting
- **Testing**: Always test your code after writing

---

 **Great job! You've translated your first pseudocode!** 

*Next: Variables in Pseudocode!*


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic


<div style="page-break-after: always;"></div>

## Answer Key

### Complete Solution

```rs
fn main() {
    println!("Hello, World!");
}

```rs

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard rust conventions with proper imports and main function
2. **Variables**: Data types are correctly declared and initialized
3. **Logic**: The program implements the required functionality
4. **Output**: Results are displayed clearly to the user
5. **Best Practices**: Code is readable and follows naming conventions

### Testing Your Solution

Try these test cases to verify your code works correctly:

1. **Basic Test**: Run the program with standard inputs
2. **Edge Cases**: Test with boundary values (0, -1, very large numbers)
3. **Error Handling**: Verify the program handles invalid inputs gracefully

### Tips for Understanding

- Review each section carefully
- Try modifying values to see how output changes
- Add your own printf/print statements to trace execution
- Experiment with different inputs
