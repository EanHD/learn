# Level 6: Loops and Repetition

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Sometimes you need to repeat actions! You'll learn different types of loops in Rust: `for`, `while`, and `loop` to automate repetitive tasks.

---

### Learning Goals

- Understand different loop types
- Learn loop control with `break` and `continue`
- Practice counting and iteration
- Create programs that repeat actions

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `loops.rs`**

```
fn main() {
    // For loop - iterate over a range
    println!("For loop counting:");
    for i in 1..=5 {
        println!("Count: {}", i);
    }
    
    // While loop - repeat while condition is true
    println!("\nWhile loop counting:");
    let mut count = 1;
    while count <= 5 {
        println!("Count: {}", count);
        count = count + 1;
    }
    
    // Loop with break - infinite loop that we break out of
    println!("\nLoop with break:");
    let mut number = 1;
    loop {
        println!("Number: {}", number);
        if number >= 3 {
            break;  // Exit the loop
        }
        number = number + 1;
    }
    
    // Loop with continue - skip even numbers
    println!("\nSkipping even numbers:");
    for i in 1..=10 {
        if i % 2 == 0 {
            continue;  // Skip to next iteration
        }
        println!("Odd number: {}", i);
    }
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
   rustc loops.rs -o loops
   ```
3. **Run your program**:
   ```
   ./loops
   ```

**Expected output:**
```
For loop counting:
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5

While loop counting:
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5

Loop with break:
Number: 1
Number: 2
Number: 3

Skipping even numbers:
Odd number: 1
Odd number: 3
Odd number: 5
Odd number: 7
Odd number: 9
```

---

### Success Checklist

- [ ] Created a file named `loops.rs`
- [ ] Copied the code exactly as shown
- [ ] Compiled without errors
- [ ] Ran the program successfully
- [ ] Observed different loop behaviors

---

### What Happened?

Loops let you repeat code! Here's what you learned:

- **`for i in 1..=5`** - Loop 5 times, `i` gets values 1,2,3,4,5
- **`while condition`** - Repeat while condition is true
- **`loop { ... }`** - Infinite loop (use `break` to exit)
- **`break`** - Exit the loop immediately
- **`continue`** - Skip to next iteration

---

### Try This (Optional Challenges)

Experiment with these:

1. Change the range in the for loop
2. Create a countdown with while loop
3. Print multiplication table using loops

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```
    for i in 1..=5 {
        println!("Count: {}", i);
    }
```
- **`for i in 1..=5`** = `i` takes values 1, 2, 3, 4, 5
- **`..=`** = Inclusive range (includes 5)
- **`i`** = Loop variable, different each iteration

```
    let mut count = 1;
    while count <= 5 {
        println!("Count: {}", count);
        count = count + 1;
    }
```
- **`mut count`** = Mutable variable for counting
- **`while count <= 5`** = Continue while condition true
- **`count = count + 1`** = Increment counter

```
    loop {
        println!("Number: {}", number);
        if number >= 3 {
            break;
        }
        number = number + 1;
    }
```
- **`loop`** = Infinite loop
- **`break`** = Exit loop when condition met
- **Must have break** or loop runs forever!

```
    for i in 1..=10 {
        if i % 2 == 0 {
            continue;
        }
        println!("Odd number: {}", i);
    }
```
- **`continue`** = Skip rest of iteration, go to next
- **Even numbers** skipped, only odds printed

### Loop Types

| Loop Type | Use Case | Example |
|-----------|----------|---------|
| `for` | Known number of iterations | `for i in 1..=10` |
| `while` | Unknown iterations, condition-based | `while x < 100` |
| `loop` | Infinite loops with manual break | `loop { if done { break; } }` |

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `error: \`break\` outside of loop` | break not in loop | Move break inside loop body |
| Infinite loop | Forgot break condition | Add proper break condition |
| `error: cannot assign to immutable variable` | Forgot mut | Add `mut` to loop variables |

### Bonus Knowledge

- **Range syntax**: `1..5` (1 to 4), `1..=5` (1 to 5)
- **Iterator**: `for` works with any iterable type
- **Loop labels**: Name loops for nested breaks
- **Performance**: `for` often preferred when possible

---

 **Fantastic! You can now create repeating programs!** 

*Next: Functions - Code Organization!*


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
