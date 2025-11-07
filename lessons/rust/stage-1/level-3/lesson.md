# Level 3: Basic Math Operations

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 1: Copying Code

### Today's Mission

Time to do some math! Programming is all about calculations. You'll learn how to use arithmetic operators to perform calculations and display results.

---

### Learning Goals

- Learn basic arithmetic operators (+, -, *, /, %)
- Understand integer vs floating-point division
- Practice combining operations
- See how math works in code

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `math.rs`**

```
fn main() {
    // Integer variables
    let a = 15;
    let b = 4;

    // Basic arithmetic operations
    println!("a = {}", a);
    println!("b = {}", b);
    println!("a + b = {}", a + b);  // Addition
    println!("a - b = {}", a - b);  // Subtraction
    println!("a * b = {}", a * b);  // Multiplication
    println!("a / b = {}", a / b);  // Integer division
    println!("a % b = {}", a % b);  // Modulo (remainder)

    // Floating-point division
    let x = 15.0;
    let y = 4.0;
    println!("x / y = {}", x / y);  // Float division

    // Order of operations
    let result = 2 + 3 * 4;  // Multiplication before addition
    println!("2 + 3 * 4 = {}", result);
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
   rustc math.rs -o math
   ```
3. **Run your program**:
   ```
   ./math
   ```

**Expected output:**
```
a = 15
b = 4
a + b = 19
a - b = 11
a * b = 60
a / b = 3
a % b = 3
x / y = 3.75
2 + 3 * 4 = 14
```

---

### Success Checklist

- [ ] Created a file named `math.rs`
- [ ] Copied the code exactly as shown
- [ ] Compiled without errors
- [ ] Ran the program successfully
- [ ] Verified all calculations are correct

---

### What Happened?

Math in programming follows the same rules as regular math! Here's what you saw:

- **Arithmetic operators**: `+` (add), `-` (subtract), `*` (multiply), `/` (divide), `%` (modulo)
- **Integer division**: `15 / 4 = 3` (truncates decimal part)
- **Float division**: `15.0 / 4.0 = 3.75` (keeps decimal part)
- **Order of operations**: Multiplication before addition (PEMDAS/BODMAS)

---

### Try This (Optional Challenges)

Experiment with these:

1. Change the values of `a` and `b`
2. Add more complex expressions like `(2 + 3) * 4`
3. Try negative numbers
4. Calculate area of a rectangle: `length * width`

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```
    let a = 15;
    let b = 4;
```
- Declare integer variables for calculations

```
    println!("a + b = {}", a + b);
```
- **`+`** = Addition operator
- Combines values of `a` and `b`

```
    println!("a / b = {}", a / b);
```
- **Integer division**: `15 / 4 = 3` (no decimal)
- Rust truncates toward zero

```
    let x = 15.0;
    let y = 4.0;
    println!("x / y = {}", x / y);
```
- **Float division**: Keeps decimal precision
- `15.0 / 4.0 = 3.75`

```
    let result = 2 + 3 * 4;
    println!("2 + 3 * 4 = {}", result);
```
- **Operator precedence**: `*` before `+`
- `3 * 4 = 12`, then `2 + 12 = 14`

### Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 3` | `1` (integer), `1.666...` (float) |
| `%` | Modulo | `5 % 3` | `2` (remainder) |

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `error: cannot add \`&str\` to \`{integer}\`` | Mixing types | Use same types for operations |
| `error: attempt to divide by zero` | Division by zero | Check divisor before dividing |
| `error: mismatched types` | Int vs float | Use `.0` for float literals |

### Bonus Knowledge

- **PEMDAS**: Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
- **Integer overflow**: Large numbers may wrap around
- **Floating-point precision**: Not always exact (0.1 + 0.2 ≠ 0.3)

---

 **Excellent! You can now do math in Rust!**

*Next: User Input!*


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic
