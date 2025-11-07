# Level 4: User Input

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Programs become much more interesting when they can interact with users! You'll learn how to read input from the keyboard and process it in your Rust programs.

---

### Learning Goals

- Learn how to read text input from users
- Understand string handling in Rust
- Practice converting strings to numbers
- Create interactive programs

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `input.rs`**

```
use std::io;

fn main() {
    // Read a string input
    println!("What's your name?");
    
    let mut name = String::new();
    io::stdin().read_line(&mut name).expect("Failed to read line");
    
    println!("Hello, {}!", name.trim());
    
    // Read a number input
    println!("Enter your age:");
    
    let mut age_str = String::new();
    io::stdin().read_line(&mut age_str).expect("Failed to read line");
    
    let age: i32 = age_str.trim().parse().expect("Please enter a valid number");
    
    println!("You are {} years old!", age);
    println!("Next year you'll be {}!", age + 1);
}
```

---

### How to Run

1. **Navigate to your working directory**:
   ```
   cd /path/to/your/folder
   ```
2. **Compile the code**:
   ```
   rustc input.rs -o input
   ```
3. **Run your program**:
   ```
   ./input
   ```

**Example interaction:**
```
What's your name?
Alice
Hello, Alice!
Enter your age:
25
You are 25 years old!
Next year you'll be 26!
```

---

### Success Checklist

- [ ] Created a file named `input.rs`
- [ ] Copied the code exactly as shown
- [ ] Compiled without errors
- [ ] Ran the program and provided input
- [ ] Saw personalized output with your input

---

### What Happened?

Your program can now talk to users! Here's what you learned:

- **`use std::io;`** - Import input/output functionality
- **`String::new()`** - Create an empty string to store input
- **`io::stdin().read_line()`** - Read a line of text from keyboard
- **`.trim()`** - Remove whitespace/newlines from input
- **`.parse()`** - Convert string to number

---

### Try This (Optional Challenges)

Experiment with these:

1. Ask for favorite color and repeat it back
2. Ask for two numbers and add them
3. Create a simple calculator that asks for operation (+, -, *, /)

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```
use std::io;
```
- **`use`** = Import statement
- **`std::io`** = Standard library input/output module

```
    let mut name = String::new();
```
- **`mut`** = Mutable (can be changed)
- **`String::new()`** = Create empty string
- **Why mutable?** `read_line` modifies the string

```
    io::stdin().read_line(&mut name).expect("Failed to read line");
```
- **`io::stdin()`** = Get standard input handle
- **`.read_line(&mut name)`** = Read line into `name`
- **`&mut`** = Mutable reference
- **`.expect(...)`** = Handle potential errors

```
    println!("Hello, {}!", name.trim());
```
- **`.trim()`** = Remove leading/trailing whitespace
- **Needed because** `read_line` includes the newline character

```
    let age: i32 = age_str.trim().parse().expect("Please enter a valid number");
```
- **`age: i32`** = Type annotation (32-bit integer)
- **`.parse()`** = Convert string to number
- **`.expect(...)`** = Error message if parsing fails

### Input/Output Concepts

| Concept | Purpose | Example |
|---------|---------|---------|
| `std::io` | Input/output operations | `use std::io;` |
| `String` | Text data | `let mut s = String::new();` |
| `read_line` | Read user input | `io::stdin().read_line(&mut s)` |
| `trim` | Remove whitespace | `" hello ".trim()` → `"hello"` |
| `parse` | Convert to number | `"42".parse::<i32>()` → `42` |

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `error: cannot borrow immutable local variable` | Forgot `mut` | Add `mut` to variable declaration |
| `error: expected \`i32\`, found enum \`Result\`` | Forgot `.expect()` | Add error handling after `.parse()` |
| `thread 'main' panicked` | Invalid number input | Enter valid numbers when prompted |

### Bonus Knowledge

- **Standard Input**: Usually the keyboard
- **Newline Character**: `\n` added by Enter key
- **Type Safety**: Rust prevents invalid conversions
- **Error Handling**: `.expect()` crashes on errors (for learning)

---

 **Awesome! Your programs can now interact with users!** 

*Next: Conditionals and Decision Making!*


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
