# Level 4: Input/Output Pseudocode

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Programs become interactive when they can accept input and provide output! You'll translate pseudocode that reads user input and displays results.

---

### Learning Goals

- Understand input/output operations in pseudocode
- Practice reading user input in Rust
- Learn to process and display input data
- Handle string parsing for numbers

---

### Your Task

**Read the pseudocode below, then write the equivalent Rust code in a file called `io_translation.rs`**

### Pseudocode:
```
START PROGRAM
    DISPLAY "Welcome to the calculator!"
    
    DISPLAY "Enter first number:"
    READ first_number AS NUMBER
    
    DISPLAY "Enter second number:"
    READ second_number AS NUMBER
    
    DECLARE sum AS NUMBER
    SET sum TO first_number + second_number
    
    DECLARE product AS NUMBER
    SET product TO first_number * second_number
    
    DISPLAY "Numbers entered: " + first_number + " and " + second_number
    DISPLAY "Sum: " + sum
    DISPLAY "Product: " + product
    DISPLAY "Thank you for using the calculator!"
END PROGRAM
```

**Your task:** Create an interactive Rust program that matches this pseudocode.

---

### How to Create Your Solution

1. **Navigate to your working directory**:
   ```bash
   cd /path/to/your/folder
   ```
2. **Create your code file**:
   ```bash
   touch io_translation.rs
   ```
3. **Write the Rust code** that matches the pseudocode
4. **Compile and test**:
   ```bash
   rustc io_translation.rs -o io_translation
   ./io_translation
   ```

**Example interaction:**
```
Welcome to the calculator!
Enter first number:
5
Enter second number:
3
Numbers entered: 5 and 3
Sum: 8
Product: 15
Thank you for using the calculator!
```

---

### Success Checklist

- [ ] Created `io_translation.rs` file
- [ ] Program displays welcome message
- [ ] Reads two numbers from user input
- [ ] Performs calculations correctly
- [ ] Displays results with proper formatting
- [ ] Shows thank you message

---

### What Did You Learn?

Input/Output operations connect your program with users.

**Key Translation Points:**
- `DISPLAY "text"` → `println!("text");`
- `READ variable AS NUMBER` → Read string, then parse to number
- String concatenation in pseudocode → `println!("{} {}", var1, var2);`

---

### Try This (Optional Challenges)

1. Add subtraction and division operations
2. Ask for user's name and personalize messages
3. Add input validation (check if numbers are valid)

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
    DISPLAY "Welcome to the calculator!"
    
    DISPLAY "Enter first number:"
    READ first_number AS NUMBER
    
    DISPLAY "Enter second number:"
    READ second_number AS NUMBER
    
    DECLARE sum AS NUMBER
    SET sum TO first_number + second_number
    
    DECLARE product AS NUMBER
    SET product TO first_number * second_number
    
    DISPLAY "Numbers entered: " + first_number + " and " + second_number
    DISPLAY "Sum: " + sum
    DISPLAY "Product: " + product
    DISPLAY "Thank you for using the calculator!"
END PROGRAM
```

**Rust Code:**
```rust
use std::io;

fn main() {
    println!("Welcome to the calculator!");
    
    println!("Enter first number:");
    let mut first_input = String::new();
    io::stdin().read_line(&mut first_input).expect("Failed to read line");
    let first_number: i32 = first_input.trim().parse().expect("Please enter a number");
    
    println!("Enter second number:");
    let mut second_input = String::new();
    io::stdin().read_line(&mut second_input).expect("Failed to read line");
    let second_number: i32 = second_input.trim().parse().expect("Please enter a number");
    
    let sum = first_number + second_number;
    let product = first_number * second_number;
    
    println!("Numbers entered: {} and {}", first_number, second_number);
    println!("Sum: {}", sum);
    println!("Product: {}", product);
    println!("Thank you for using the calculator!");
}
```

### Translation Guide

| Pseudocode | Rust Code | Explanation |
|------------|-----------|-------------|
| `DISPLAY "text"` | `println!("text");` | Output text |
| `READ var AS NUMBER` | Read string + parse | Input handling |
| `var1 + " and " + var2` | `"{} and {}", var1, var2` | String formatting |
| `SET sum TO a + b` | `let sum = a + b;` | Calculation |

### Common Mistakes & Solutions

| Common Error | Why It Happens | Solution |
|--------------|----------------|----------|
| `let first_number = io::stdin().read_line(...)` | Wrong return type | Read to String, then parse |
| `println!("Numbers: " + first_number);` | Can't use + for display | Use `println!("Numbers: {}", first_number);` |
| `parse()` without error handling | May panic on invalid input | Add `.expect("message")` |
| `trim()` forgotten | Newline included in string | Always trim input strings |

### Bonus Knowledge

- **Input Buffer**: `read_line` includes newline character
- **Parsing**: Converting strings to numbers safely
- **Error Handling**: `.expect()` for development (proper error handling later)
- **User Experience**: Clear prompts make programs user-friendly

---

 **Awesome! You can handle interactive pseudocode!** 

*Next: Decision Pseudocode!*