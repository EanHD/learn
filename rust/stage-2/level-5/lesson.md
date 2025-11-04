# Level 5: Decision Pseudocode

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Programs make decisions! You'll translate pseudocode that uses conditional logic (if-else statements) into Rust code.

---

### Learning Goals

- Understand decision-making in pseudocode
- Practice if-else statements in Rust
- Learn comparison operators
- Create programs that respond differently based on conditions

---

### Your Task

**Read the pseudocode below, then write the equivalent Rust code in a file called `decision_translation.rs`**

### Pseudocode:
```
START PROGRAM
    DISPLAY "Number Classifier"
    DISPLAY "Enter a number:"
    READ number AS NUMBER
    
    IF number > 0 THEN
        DISPLAY number + " is positive"
    ELSE IF number < 0 THEN
        DISPLAY number + " is negative"
    ELSE
        DISPLAY number + " is zero"
    END IF
    
    IF number % 2 == 0 THEN
        DISPLAY number + " is even"
    ELSE
        DISPLAY number + " is odd"
    END IF
    
    IF number >= 10 THEN
        DISPLAY "That's a big number!"
    ELSE IF number >= 0 THEN
        DISPLAY "That's a small number!"
    ELSE
        DISPLAY "That's a negative number!"
    END IF
END PROGRAM
```

**Your task:** Create a Rust program that classifies numbers based on the pseudocode logic.

---

### How to Create Your Solution

1. **Navigate to your working directory**:
   ```bash
   cd /path/to/your/folder
   ```
2. **Create your code file**:
   ```bash
   touch decision_translation.rs
   ```
3. **Write the Rust code** that matches the pseudocode
4. **Compile and test**:
   ```bash
   rustc decision_translation.rs -o decision_translation
   ./decision_translation
   ```

**Example interaction:**
```
Number Classifier
Enter a number:
7
7 is positive
7 is odd
That's a small number!
```

---

### Success Checklist

- [ ] Created `decision_translation.rs` file
- [ ] Reads a number from user input
- [ ] Correctly identifies positive/negative/zero
- [ ] Determines if number is even or odd
- [ ] Classifies number size correctly
- [ ] All conditional logic works as expected

---

### What Did You Learn?

Conditional statements let programs make decisions based on data.

**Key Translation Points:**
- `IF condition THEN` → `if condition {`
- `ELSE IF condition THEN` → `} else if condition {`
- `ELSE` → `} else {`
- `END IF` → `}`
- Comparison operators (`>`, `<`, `==`) work the same

---

### Try This (Optional Challenges)

1. Add more number classifications (prime, perfect square, etc.)
2. Ask for two numbers and compare them
3. Create a grading system (A, B, C, D, F based on score)

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
    DISPLAY "Number Classifier"
    DISPLAY "Enter a number:"
    READ number AS NUMBER
    
    IF number > 0 THEN
        DISPLAY number + " is positive"
    ELSE IF number < 0 THEN
        DISPLAY number + " is negative"
    ELSE
        DISPLAY number + " is zero"
    END IF
    
    IF number % 2 == 0 THEN
        DISPLAY number + " is even"
    ELSE
        DISPLAY number + " is odd"
    END IF
    
    IF number >= 10 THEN
        DISPLAY "That's a big number!"
    ELSE IF number >= 0 THEN
        DISPLAY "That's a small number!"
    ELSE
        DISPLAY "That's a negative number!"
    END IF
END PROGRAM
```

**Rust Code:**
```rust
use std::io;

fn main() {
    println!("Number Classifier");
    println!("Enter a number:");
    
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let number: i32 = input.trim().parse().expect("Please enter a number");
    
    if number > 0 {
        println!("{} is positive", number);
    } else if number < 0 {
        println!("{} is negative", number);
    } else {
        println!("{} is zero", number);
    }
    
    if number % 2 == 0 {
        println!("{} is even", number);
    } else {
        println!("{} is odd", number);
    }
    
    if number >= 10 {
        println!("That's a big number!");
    } else if number >= 0 {
        println!("That's a small number!");
    } else {
        println!("That's a negative number!");
    }
}
```

### Translation Guide

| Pseudocode | Rust Code | Explanation |
|------------|-----------|-------------|
| `IF condition THEN` | `if condition {` | Start conditional block |
| `ELSE IF condition THEN` | `} else if condition {` | Alternative condition |
| `ELSE` | `} else {` | Default case |
| `END IF` | `}` | Close conditional block |
| `number % 2 == 0` | `number % 2 == 0` | Modulo and equality |

### Common Mistakes & Solutions

| Common Error | Why It Happens | Solution |
|--------------|----------------|----------|
| `if number > 0` without `{ }` | Missing braces | Add braces around if blocks |
| `} else if` with wrong braces | Brace mismatch | Ensure proper brace pairing |
| `number % 2 = 0` | Assignment instead of comparison | Use `==` for comparison |
| Wrong condition order | Logic error | Check condition precedence |

### Bonus Knowledge

- **Boolean Expressions**: Conditions evaluate to true/false
- **Short-circuiting**: `&&` and `||` operators stop early when possible
- **Nested Conditions**: if statements inside other if statements
- **Code Style**: Consistent indentation makes logic clear

---

 **Excellent! You can handle decision-making pseudocode!** 

*Next: Loop Pseudocode!*