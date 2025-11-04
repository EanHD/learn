# Level 6: Loop Pseudocode

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Repetition is powerful! You'll translate pseudocode that uses loops to repeat actions into Rust code.

---

### Learning Goals

- Understand loop structures in pseudocode
- Practice different loop types in Rust
- Learn loop control with break and continue
- Create programs that automate repetitive tasks

---

### Your Task

**Read the pseudocode below, then write the equivalent Rust code in a file called `loop_translation.rs`**

### Pseudocode:
```
START PROGRAM
    DISPLAY "Countdown Program"
    
    DECLARE counter AS NUMBER
    SET counter TO 5
    
    WHILE counter > 0 DO
        DISPLAY "Count: " + counter
        SET counter TO counter - 1
    END WHILE
    
    DISPLAY "Blast off!"
    
    DISPLAY "Even numbers from 1 to 10:"
    FOR i FROM 1 TO 10 DO
        IF i % 2 == 0 THEN
            DISPLAY i
        END IF
    END FOR
    
    DISPLAY "Loop with break:"
    DECLARE num AS NUMBER
    SET num TO 1
    
    WHILE TRUE DO
        DISPLAY "Number: " + num
        IF num >= 4 THEN
            BREAK
        END IF
        SET num TO num + 1
    END WHILE
END PROGRAM
```

**Your task:** Create a Rust program that implements these looping constructs.

---

### How to Create Your Solution

1. **Navigate to your working directory**:
   ```bash
   cd /path/to/your/folder
   ```
2. **Create your code file**:
   ```bash
   touch loop_translation.rs
   ```
3. **Write the Rust code** that matches the pseudocode
4. **Compile and test**:
   ```bash
   rustc loop_translation.rs -o loop_translation
   ./loop_translation
   ```

**Expected output:**
```
Countdown Program
Count: 5
Count: 4
Count: 3
Count: 2
Count: 1
Blast off!
Even numbers from 1 to 10:
2
4
6
8
10
Loop with break:
Number: 1
Number: 2
Number: 3
Number: 4
```

---

### Success Checklist

- [ ] Created `loop_translation.rs` file
- [ ] Implemented countdown with while loop
- [ ] Used for loop to find even numbers
- [ ] Created loop with break condition
- [ ] All loops work correctly and produce expected output

---

### What Did You Learn?

Loops let you repeat code efficiently instead of writing it multiple times.

**Key Translation Points:**
- `WHILE condition DO` → `while condition {`
- `END WHILE` → `}`
- `FOR i FROM start TO end DO` → `for i in start..=end {`
- `IF condition THEN BREAK` → `if condition { break; }`
- `WHILE TRUE DO` → `loop {`

---

### Try This (Optional Challenges)

1. Add a countdown from user-specified number
2. Print multiplication table using nested loops
3. Skip odd numbers instead of printing even numbers

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
    DISPLAY "Countdown Program"
    
    DECLARE counter AS NUMBER
    SET counter TO 5
    
    WHILE counter > 0 DO
        DISPLAY "Count: " + counter
        SET counter TO counter - 1
    END WHILE
    
    DISPLAY "Blast off!"
    
    DISPLAY "Even numbers from 1 to 10:"
    FOR i FROM 1 TO 10 DO
        IF i % 2 == 0 THEN
            DISPLAY i
        END IF
    END FOR
    
    DISPLAY "Loop with break:"
    DECLARE num AS NUMBER
    SET num TO 1
    
    WHILE TRUE DO
        DISPLAY "Number: " + num
        IF num >= 4 THEN
            BREAK
        END IF
        SET num TO num + 1
    END WHILE
END PROGRAM
```

**Rust Code:**
```rust
fn main() {
    println!("Countdown Program");
    
    let mut counter = 5;
    
    while counter > 0 {
        println!("Count: {}", counter);
        counter = counter - 1;
    }
    
    println!("Blast off!");
    
    println!("Even numbers from 1 to 10:");
    for i in 1..=10 {
        if i % 2 == 0 {
            println!("{}", i);
        }
    }
    
    println!("Loop with break:");
    let mut num = 1;
    
    loop {
        println!("Number: {}", num);
        if num >= 4 {
            break;
        }
        num = num + 1;
    }
}
```

### Translation Guide

| Pseudocode | Rust Code | Explanation |
|------------|-----------|-------------|
| `WHILE condition DO` | `while condition {` | Conditional loop |
| `END WHILE` | `}` | Close while loop |
| `FOR i FROM 1 TO 10 DO` | `for i in 1..=10 {` | Range-based loop |
| `WHILE TRUE DO` | `loop {` | Infinite loop |
| `BREAK` | `break;` | Exit loop |
| `SET counter TO counter - 1` | `counter = counter - 1;` | Decrement |

### Common Mistakes & Solutions

| Common Error | Why It Happens | Solution |
|--------------|----------------|----------|
| `while counter > 0` without `mut` | Trying to modify immutable | Add `mut` to counter |
| `for i in 1..10` | Range excludes 10 | Use `1..=10` for inclusive |
| `break` outside loop | break not in loop | Move break inside loop body |
| Infinite loop | Forgot break condition | Add proper exit condition |

### Bonus Knowledge

- **Loop Variables**: `for` loop variables are immutable by default
- **Mutable Counters**: Use `mut` for variables that change in loops
- **Range Syntax**: `..` excludes end, `..=` includes end
- **Loop Control**: `break` exits, `continue` skips to next iteration

---

 **Fantastic! You can handle looping pseudocode!** 

*Next: Function Pseudocode!*