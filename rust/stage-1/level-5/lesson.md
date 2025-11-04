# Level 5: Conditionals and Decision Making

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Programs need to make decisions! You'll learn how to use `if`, `else if`, and `else` statements to create programs that behave differently based on conditions.

---

### Learning Goals

- Understand conditional statements
- Learn comparison operators (>, <, ==, !=, >=, <=)
- Practice logical decision making
- Create programs that respond differently to different inputs

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `conditionals.rs`**

```rust
fn main() {
    let number = 7;
    
    // Simple if-else
    if number > 0 {
        println!("The number {} is positive", number);
    } else {
        println!("The number {} is not positive", number);
    }
    
    // Multiple conditions with else if
    let temperature = 25;
    
    if temperature > 30 {
        println!("It's very hot! {}°C", temperature);
    } else if temperature > 20 {
        println!("It's warm. {}°C", temperature);
    } else if temperature > 10 {
        println!("It's cool. {}°C", temperature);
    } else {
        println!("It's cold! {}°C", temperature);
    }
    
    // Comparison operators
    let a = 10;
    let b = 20;
    
    if a == b {
        println!("a equals b");
    } else if a != b {
        println!("a does not equal b");
    }
    
    if a < b {
        println!("a is less than b");
    }
    
    if a <= b {
        println!("a is less than or equal to b");
    }
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
   rustc conditionals.rs -o conditionals
   ```
3. **Run your program**:
   ```bash
   ./conditionals
   ```

**Expected output:**
```
The number 7 is positive
It's warm. 25°C
a does not equal b
a is less than b
a is less than or equal to b
```

---

### Success Checklist

- [ ] Created a file named `conditionals.rs`
- [ ] Copied the code exactly as shown
- [ ] Compiled without errors
- [ ] Ran the program successfully
- [ ] Verified the conditional logic works correctly

---

### What Happened?

Your program can now make decisions! Here's what you learned:

- **`if`** - Execute code if condition is true
- **`else if`** - Check another condition if previous were false
- **`else`** - Execute if no conditions were true
- **Comparison operators**: `>`, `<`, `==`, `!=`, `>=`, `<=`
- **Boolean expressions** - Conditions that evaluate to true/false

---

### Try This (Optional Challenges)

Experiment with these:

1. Change the values and see how output changes
2. Add more temperature ranges
3. Create a grading system (A, B, C, D, F based on score)

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```rust
    if number > 0 {
        println!("The number {} is positive", number);
    } else {
        println!("The number {} is not positive", number);
    }
```
- **`if number > 0`** = Condition: is number greater than 0?
- **`{ ... }`** = Code block executed if condition true
- **`else`** = Executed if condition false

```rust
    if temperature > 30 {
        println!("It's very hot! {}°C", temperature);
    } else if temperature > 20 {
        println!("It's warm. {}°C", temperature);
    } else if temperature > 10 {
        println!("It's cool. {}°C", temperature);
    } else {
        println!("It's cold! {}°C", temperature);
    }
```
- **Chain of conditions** checked in order
- **First true condition** executes, others skipped
- **else** catches any remaining cases

```rust
    if a == b {
        println!("a equals b");
    } else if a != b {
        println!("a does not equal b");
    }
```
- **`==`** = Equality comparison
- **`!=`** = Inequality comparison
- Note: `=` is assignment, `==` is comparison

### Comparison Operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `true` |
| `!=` | Not equal to | `5 != 3` | `true` |
| `>` | Greater than | `5 > 3` | `true` |
| `<` | Less than | `3 < 5` | `true` |
| `>=` | Greater or equal | `5 >= 5` | `true` |
| `<=` | Less or equal | `3 <= 5` | `true` |

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `error: expected \`{\`, found keyword \`else\`` | Missing braces | Add `{ }` around if/else blocks |
| `error: binary operation \`==\` cannot be applied` | Wrong types | Compare same types |
| `error: expected bool, found i32` | Not a condition | Use comparison operators |

### Bonus Knowledge

- **Short-circuiting**: `&&` and `||` operators stop early
- **Truthy/Falsy**: Only `bool` types allowed in conditions
- **Indentation**: 4 spaces standard in Rust
- **Blocks**: Create scopes for variables

---

 **Excellent! Your programs can now make decisions!** 

*Next: Loops and Repetition!*