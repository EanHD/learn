# Level 2: Variables in Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Variables are essential for storing and manipulating data. In this lesson, you'll translate pseudocode that uses variables into working Rust code.

---

### Learning Goals

- Understand how variables work in pseudocode
- Practice declaring and using variables in Rust
- Learn to track variable values through a program
- Master variable assignment and display

---

### Your Task

**Read the pseudocode below, then write the equivalent Rust code in a file called `variables_translation.rs`**


### How to Run

1. **Compile the code**:
   ```
   rustc hello.rs -o hello hello.rs
   ```

2. **Run your program**:
   ```
   ./hello hello
   ```

**Expected output:**
```
Hello, World!
```

### Pseudocode:
```
START PROGRAM
    DECLARE name AS TEXT
    SET name TO "Alice"
    
    DECLARE age AS NUMBER
    SET age TO 25
    
    DECLARE is_student AS BOOLEAN
    SET is_student TO TRUE
    
    DISPLAY "Name: " + name
    DISPLAY "Age: " + age
    DISPLAY "Is student: " + is_student
END PROGRAM
```

**Your task:** Create a Rust program that implements this pseudocode exactly.

---

### How to Create Your Solution

1. **Navigate to your working directory**:
   ```
   cd /path/to/your/folder
   ```
2. **Create your code file**:
   ```
   touch variables_translation.rs
   ```
3. **Write the Rust code** that matches the pseudocode
4. **Compile and test**:
   ```
   rustc variables_translation.rs -o variables_translation
   ./variables_translation
   ```

**Expected output:**
```
Name: Alice
Age: 25
Is student: true
```

---

### Success Checklist

- [ ] Created `variables_translation.rs` file
- [ ] Declared variables for name, age, and is_student
- [ ] Assigned appropriate values to each variable
- [ ] Displayed all variables with labels
- [ ] Program compiles and runs correctly

---

### What Did You Learn?

Variables in pseudocode map directly to Rust variables, but the syntax is different.

**Key Translation Points:**
- `DECLARE x AS TEXT` → `let x = "value";`
- `DECLARE x AS NUMBER` → `let x = 42;`
- `DECLARE x AS BOOLEAN` → `let x = true;`
- `SET x TO value` → `let x = value;` (or `x = value;` if mutable)
- `DISPLAY "text" + variable` → `println!("text {}", variable);`

---

### Try This (Optional Challenges)

1. Add another variable for favorite programming language
2. Change the values and see how output changes
3. Try displaying variables in different orders

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Step-by-Step Translation

**Pseudocode:**
```
START PROGRAM
    DECLARE name AS TEXT
    SET name TO "Alice"
    
    DECLARE age AS NUMBER
    SET age TO 25
    
    DECLARE is_student AS BOOLEAN
    SET is_student TO TRUE
    
    DISPLAY "Name: " + name
    DISPLAY "Age: " + age
    DISPLAY "Is student: " + is_student
END PROGRAM
```

**Rust Code:**
```
fn main() {
    let name = "Alice";
    let age = 25;
    let is_student = true;
    
    println!("Name: {}", name);
    println!("Age: {}", age);
    println!("Is student: {}", is_student);
}
```

### Translation Guide

| Pseudocode | Rust Code | Explanation |
|------------|-----------|-------------|
| `DECLARE x AS TEXT` | `let x = "value";` | String variable |
| `DECLARE x AS NUMBER` | `let x = 42;` | Integer variable |
| `DECLARE x AS BOOLEAN` | `let x = true;` | Boolean variable |
| `SET x TO value` | `let x = value;` | Assignment |
| `DISPLAY a + b` | `println!("{} {}", a, b);` | String concatenation |

### Common Mistakes & Solutions

| Common Error | Why It Happens | Solution |
|--------------|----------------|----------|
| `let name: String = "Alice";` | Over-complicating types | Use `let name = "Alice";` (type inference) |
| `println!("Name: " + name);` | Can't add &str + &str | Use `println!("Name: {}", name);` |
| `let age = "25";` | Wrong type | Use `let age = 25;` for numbers |
| `let is_student = "true";` | Wrong type | Use `let is_student = true;` for booleans |

### Bonus Knowledge

- **Type Inference**: Rust figures out types automatically
- **String Literals**: `&str` vs `String` (we use `&str` here)
- **Display Trait**: `println!` uses `{}` for any displayable type
- **Variable Naming**: Use descriptive names (snake_case in Rust)

---

 **Excellent! You can now work with variables in pseudocode!** 

*Next: Mathematical Pseudocode!*


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
