# Level 3: Mathematical Pseudocode

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Math is everywhere in programming! You'll translate pseudocode that performs calculations into Rust code.

---

### Learning Goals

- Translate mathematical operations from pseudocode to Rust
- Understand operator precedence in both pseudocode and Rust
- Practice complex mathematical expressions
- Learn to display calculation results

---

### Your Task

**Read the pseudocode below, then write the equivalent Rust code in a file called `math_translation.rs`**

### Pseudocode:
```
START PROGRAM
    DECLARE a AS NUMBER
    SET a TO 10
    
    DECLARE b AS NUMBER
    SET b TO 3
    
    DECLARE sum AS NUMBER
    SET sum TO a + b
    
    DECLARE difference AS NUMBER
    SET difference TO a - b
    
    DECLARE product AS NUMBER
    SET product TO a * b
    
    DECLARE quotient AS NUMBER
    SET quotient TO a / b
    
    DISPLAY "a = " + a
    DISPLAY "b = " + b
    DISPLAY "Sum: " + sum
    DISPLAY "Difference: " + difference
    DISPLAY "Product: " + product
    DISPLAY "Quotient: " + quotient
    
    DECLARE complex AS NUMBER
    SET complex TO (a + b) * 2 - quotient
    DISPLAY "Complex calculation: " + complex
END PROGRAM
```

**Your task:** Create a Rust program that performs these mathematical operations.

---

### How to Create Your Solution

1. **Navigate to your working directory**:
   ```bash
   cd /path/to/your/folder
   ```
2. **Create your code file**:
   ```bash
   touch math_translation.rs
   ```
3. **Write the Rust code** that matches the pseudocode
4. **Compile and test**:
   ```bash
   rustc math_translation.rs -o math_translation
   ./math_translation
   ```

**Expected output:**
```
a = 10
b = 3
Sum: 13
Difference: 7
Product: 30
Quotient: 3
Complex calculation: 23
```

---

### Success Checklist

- [ ] Created `math_translation.rs` file
- [ ] Declared and assigned all variables
- [ ] Performed all arithmetic operations correctly
- [ ] Handled the complex calculation with proper precedence
- [ ] Program compiles and produces correct output

---

### What Did You Learn?

Mathematical operations in pseudocode translate directly to Rust operators.

**Key Translation Points:**
- `SET x TO a + b` → `let x = a + b;`
- `SET x TO a - b` → `let x = a - b;`
- `SET x TO a * b` → `let x = a * b;`
- `SET x TO a / b` → `let x = a / b;` (integer division)
- Parentheses work the same: `(a + b) * 2`

---

### Try This (Optional Challenges)

1. Add modulo operation (`a % b`)
2. Try floating-point division (use decimals)
3. Create more complex expressions

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
    DECLARE a AS NUMBER
    SET a TO 10
    
    DECLARE b AS NUMBER
    SET b TO 3
    
    DECLARE sum AS NUMBER
    SET sum TO a + b
    
    DECLARE difference AS NUMBER
    SET difference TO a - b
    
    DECLARE product AS NUMBER
    SET product TO a * b
    
    DECLARE quotient AS NUMBER
    SET quotient TO a / b
    
    DISPLAY "a = " + a
    DISPLAY "b = " + b
    DISPLAY "Sum: " + sum
    DISPLAY "Difference: " + difference
    DISPLAY "Product: " + product
    DISPLAY "Quotient: " + quotient
    
    DECLARE complex AS NUMBER
    SET complex TO (a + b) * 2 - quotient
    DISPLAY "Complex calculation: " + complex
END PROGRAM
```

**Rust Code:**
```rust
fn main() {
    let a = 10;
    let b = 3;
    
    let sum = a + b;
    let difference = a - b;
    let product = a * b;
    let quotient = a / b;
    
    println!("a = {}", a);
    println!("b = {}", b);
    println!("Sum: {}", sum);
    println!("Difference: {}", difference);
    println!("Product: {}", product);
    println!("Quotient: {}", quotient);
    
    let complex = (a + b) * 2 - quotient;
    println!("Complex calculation: {}", complex);
}
```

### Translation Guide

| Pseudocode | Rust Code | Explanation |
|------------|-----------|-------------|
| `DECLARE x AS NUMBER` | `let x = value;` | Variable declaration |
| `SET x TO expression` | `let x = expression;` | Assignment with calculation |
| `a + b` | `a + b` | Addition |
| `a - b` | `a - b` | Subtraction |
| `a * b` | `a * b` | Multiplication |
| `a / b` | `a / b` | Division |
| `(a + b) * 2` | `(a + b) * 2` | Parentheses for precedence |

### Common Mistakes & Solutions

| Common Error | Why It Happens | Solution |
|--------------|----------------|----------|
| `let sum = a + b` without `;` | Missing semicolon | Add `;` at end of statements |
| `println!("Sum: " + sum);` | Can't concatenate with + | Use `println!("Sum: {}", sum);` |
| Wrong calculation order | Operator precedence | Use parentheses when needed |
| `let quotient = a / b` with floats | Integer division | Use `10.0 / 3.0` for float division |

### Bonus Knowledge

- **Integer Division**: `10 / 3 = 3` (truncates decimal)
- **Operator Precedence**: `* /` before `+ -`
- **Complex Expressions**: Use parentheses to clarify order
- **Type Consistency**: All operands must be same type

---

 **Great! You can handle mathematical pseudocode!** 

*Next: Input/Output Pseudocode!*