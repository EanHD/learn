# Level 7: Functions - Code Organization
## Stage 1: Copying Code

### Today's Mission

Functions let you organize code into reusable pieces! You'll learn how to define functions, pass parameters, and return values in Rust.

---

### Learning Goals

- Understand function definition and calling
- Learn parameters and return values
- Practice code organization
- Create reusable code blocks

---

### Your Task

**Copy the following code EXACTLY as shown below into a new file called `functions.rs`**

```rust
// Function that takes a parameter but returns nothing
fn greet(name: &str) {
    println!("Hello, {}!", name);
}

// Function that takes parameters and returns a value
fn add(a: i32, b: i32) -> i32 {
    a + b
}

// Function that calculates area
fn calculate_area(length: i32, width: i32) -> i32 {
    length * width
}

fn main() {
    // Call functions
    greet("World");
    greet("Rust");
    
    let sum = add(5, 3);
    println!("5 + 3 = {}", sum);
    
    let area = calculate_area(10, 5);
    println!("Area of 10x5 rectangle = {}", area);
    
    // Functions can call other functions
    let total = add(calculate_area(2, 3), add(1, 2));
    println!("Complex calculation: (2*3) + (1+2) = {}", total);
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
   rustc functions.rs -o functions
   ```
3. **Run your program**:
   ```bash
   ./functions
   ```

**Expected output:**
```
Hello, World!
Hello, Rust!
5 + 3 = 8
Area of 10x5 rectangle = 50
Complex calculation: (2*3) + (1+2) = 11
```

---

### Success Checklist

- [ ] Created a file named `functions.rs`
- [ ] Copied the code exactly as shown
- [ ] Compiled without errors
- [ ] Ran the program successfully
- [ ] Verified function calls and returns work

---

### What Happened?

Functions make code reusable! Here's what you learned:

- **`fn function_name(parameters)`** - Function definition
- **`-> ReturnType`** - Return type annotation
- **Parameters** - Input values to functions
- **Return values** - Output from functions
- **Function calls** - Using functions in your code

---

### Try This (Optional Challenges)

Experiment with these:

1. Create a function that converts Celsius to Fahrenheit
2. Write a function that checks if a number is even
3. Create functions for basic calculator operations

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

```rust
fn greet(name: &str) {
    println!("Hello, {}!", name);
}
```
- **`fn greet`** = Function declaration
- **`(name: &str)`** = Parameter: `name` of type string slice
- **`{ ... }`** = Function body
- **No return type** = Returns `()` (unit type)

```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}
```
- **`-> i32`** = Returns 32-bit integer
- **Last expression** `a + b` is returned (no semicolon!)
- **Parameters** `a` and `b` are both `i32`

```rust
fn calculate_area(length: i32, width: i32) -> i32 {
    length * width
}
```
- **Same pattern** as `add` function
- **Multiplication** instead of addition

```rust
    let sum = add(5, 3);
    println!("5 + 3 = {}", sum);
```
- **Function call** `add(5, 3)` returns `8`
- **Store result** in `sum` variable
- **Print result**

```rust
    let total = add(calculate_area(2, 3), add(1, 2));
```
- **Nested calls**: Functions can call other functions
- **Evaluation order**: Innermost calls first
- **Result**: `add(6, 3)` → `add(6, 3)` → `9`

### Function Components

| Component | Example | Purpose |
|-----------|---------|---------|
| Name | `greet` | Identifier for calling |
| Parameters | `(name: &str)` | Input values |
| Return Type | `-> i32` | Output type |
| Body | `{ a + b }` | Code to execute |
| Call | `add(5, 3)` | Execute function |

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `error: not all control paths return a value` | Missing return in some branches | Ensure all paths return value |
| `error: expected \`;\`, found \`}\`` | Semicolon on return expression | Remove `;` from last expression |
| `error: function takes 2 arguments but 1 was supplied` | Wrong number of arguments | Provide correct number of parameters |

### Bonus Knowledge

- **String slices**: `&str` for read-only strings
- **Ownership**: Functions can take ownership or borrow
- **Unit type**: `()` for functions that don't return values
- **Expression-based**: Last expression is return value

---

 **Congratulations! You've completed Stage 1: Copying Code!** 

*You've learned the fundamentals of Rust programming. Great job! Next stages will build on these concepts.*