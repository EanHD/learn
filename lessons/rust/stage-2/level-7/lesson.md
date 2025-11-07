# Level 7: Function Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Functions organize code into reusable pieces! You'll translate pseudocode that defines and uses functions into Rust code.

---

### Learning Goals

- Understand function definitions in pseudocode
- Practice creating functions in Rust
- Learn to call functions and use return values
- Create modular, organized code

---

### Your Task

**Read the pseudocode below, then write the equivalent Rust code in a file called `function_translation.rs`**


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
FUNCTION greet(name)
    DISPLAY "Hello, " + name + "!"
END FUNCTION

FUNCTION add_numbers(a, b)
    RETURN a + b
END FUNCTION

FUNCTION is_even(number)
    IF number % 2 == 0 THEN
        RETURN TRUE
    ELSE
        RETURN FALSE
    END IF
END FUNCTION

START PROGRAM
    CALL greet("World")
    CALL greet("Rust Programmer")
    
    DECLARE result AS NUMBER
    SET result TO CALL add_numbers(5, 3)
    DISPLAY "5 + 3 = " + result
    
    DECLARE num AS NUMBER
    SET num TO 7
    
    IF CALL is_even(num) THEN
        DISPLAY num + " is even"
    ELSE
        DISPLAY num + " is odd"
    END IF
    
    DISPLAY "Program complete!"
END PROGRAM
```rust

**Your task:** Create a Rust program with functions that match the pseudocode.

---

### How to Create Your Solution

1. **Navigate to your working directory**:
   ```bash
   cd /path/to/your/folder
   ```rust
2. **Create your code file**:
   ```bash
   touch function_translation.rs
   ```rust
3. **Write the Rust code** that matches the pseudocode
4. **Compile and test**:
   ```bash
   rustc function_translation.rs -o function_translation
   ./function_translation
   ```rust

**Expected output:**
```rust
Hello, World!
Hello, Rust Programmer!
5 + 3 = 8
7 is odd
Program complete!
```rust

---

### Success Checklist

- [ ] Created `function_translation.rs` file
- [ ] Defined `greet` function that takes a parameter
- [ ] Created `add_numbers` function that returns a value
- [ ] Implemented `is_even` function with conditional return
- [ ] Called all functions correctly in main
- [ ] Program produces expected output

---

### What Did You Learn?

Functions break complex programs into smaller, manageable pieces.

**Key Translation Points:**
- `FUNCTION name(parameters)` → `fn name(parameters) {`
- `RETURN value` → `value` (last expression) or `return value;`
- `END FUNCTION` → `}`
- `CALL function(args)` → `function(args)`
- Function calls can be used in expressions

---

### Try This (Optional Challenges)

1. Add a function that calculates factorial
2. Create a function that checks if a number is prime
3. Write functions for temperature conversion

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
FUNCTION greet(name)
    DISPLAY "Hello, " + name + "!"
END FUNCTION

FUNCTION add_numbers(a, b)
    RETURN a + b
END FUNCTION

FUNCTION is_even(number)
    IF number % 2 == 0 THEN
        RETURN TRUE
    ELSE
        RETURN FALSE
    END IF
END FUNCTION

START PROGRAM
    CALL greet("World")
    CALL greet("Rust Programmer")
    
    DECLARE result AS NUMBER
    SET result TO CALL add_numbers(5, 3)
    DISPLAY "5 + 3 = " + result
    
    DECLARE num AS NUMBER
    SET num TO 7
    
    IF CALL is_even(num) THEN
        DISPLAY num + " is even"
    ELSE
        DISPLAY num + " is odd"
    END IF
    
    DISPLAY "Program complete!"
END PROGRAM
```rust

**Rust Code:**
```rust
fn greet(name: &str) {
    println!("Hello, {}!", name);
}

fn add_numbers(a: i32, b: i32) -> i32 {
    a + b
}

fn is_even(number: i32) -> bool {
    if number % 2 == 0 {
        true
    } else {
        false
    }
}

fn main() {
    greet("World");
    greet("Rust Programmer");
    
    let result = add_numbers(5, 3);
    println!("5 + 3 = {}", result);
    
    let num = 7;
    
    if is_even(num) {
        println!("{} is even", num);
    } else {
        println!("{} is odd", num);
    }
    
    println!("Program complete!");
}
```rust

### Translation Guide

| Pseudocode | Rust Code | Explanation |
|------------|-----------|-------------|
| `FUNCTION name(params)` | `fn name(params) {` | Function definition |
| `RETURN value` | `value` or `return value;` | Return value |
| `END FUNCTION` | `}` | Close function |
| `CALL function(args)` | `function(args)` | Function call |
| `TRUE/FALSE` | `true/false` | Boolean literals |

### Common Mistakes & Solutions

| Common Error | Why It Happens | Solution |
|--------------|----------------|----------|
| `fn greet(name)` without type | Missing parameter type | Add `: &str` or `: i32` etc. |
| `return a + b;` with semicolon | Semicolon makes statement | Remove `;` for expression return |
| `greet("World");` with semicolon in fn | Not needed in functions | Remove extra semicolons |
| Wrong parameter types | Type mismatch | Match parameter types in calls |

### Bonus Knowledge

- **Type Annotations**: Parameters and returns need explicit types
- **String Slices**: `&str` for read-only strings
- **Return Expressions**: Last expression returns automatically
- **Function Scope**: Variables defined in functions are local

---

 **Congratulations! You've completed Stage 2: Pseudocode to Code!** 

*You've learned to translate written logic into working Rust programs. Excellent progress! Next stages will build on these skills.*


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
