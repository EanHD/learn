# Level 1: Simple Application

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 4: Full Problem Solving

### Today's Mission

Welcome to Stage 4! Now you'll implement complete Rust programs based on the pseudocode designs from Stage 3. This is where theory becomes practice!

---

### Learning Goals

- Implement complete Rust applications
- Handle user input and output
- Apply mathematical operations in code
- Create user-friendly command-line interfaces
- Debug and test your programs

---

### Your Task

**Implement the Temperature Converter program in Rust. Create the following files:**

1. **`main.rs`** - The main program file
2. **`README.md`** - Instructions for running the program

### Program Requirements

Based on your Stage 3 pseudocode, implement a temperature converter that:

1. **Displays a menu** for conversion choices
2. **Reads user input** for conversion type and temperature
3. **Performs calculations** using the correct formulas
4. **Displays results** with proper formatting
5. **Handles invalid input** gracefully

**Conversion Formulas:**
- Celsius to Fahrenheit: `F = (C × 9/5) + 32`
- Fahrenheit to Celsius: `C = (F - 32) × 5/9`

---

### Implementation Steps

1. **Create the project structure**:
   ```bash
   cd /home/eanhd/LEARN/rust/stage-4-full-problem-solving/level-1-simple-application
   ```rust

2. **Create `main.rs`** with your Rust implementation

3. **Test your program**:
   ```bash
   rustc main.rs
   ./main
   ```rust

4. **Create `README.md`** with usage instructions

---

### Success Checklist

- [ ] Created `main.rs` file
- [ ] Program compiles without errors
- [ ] Menu displays correctly
- [ ] Both conversion directions work
- [ ] Input validation handles invalid choices
- [ ] Results display with proper units
- [ ] Created `README.md` with instructions

---

### What You'll Learn

Full problem solving involves:
- **Code implementation** - Turning pseudocode into working code
- **Error handling** - Managing invalid inputs and edge cases
- **User interface** - Creating intuitive command-line interfaces
- **Testing** - Verifying your program works correctly

---

### Implementation Tips

1. **Use `std::io`** for input/output operations
2. **Handle input parsing** carefully (numbers vs strings)
3. **Use floating-point** arithmetic for temperatures
4. **Format output** clearly with units
5. **Test edge cases** like invalid menu choices

---

## Need Help with Rust?

- **Input/Output**: Use `std::io::stdin()` and `read_line()`
- **String to Number**: Use `parse::<f64>()` for temperature conversion
- **Error Handling**: Use `match` or `if let` for parsing results
- **Compilation**: `rustc main.rs` to compile, `./main` to run

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

> **NEEDS_AUTHOR:** This lesson needs a complete answer key with code breakdown, execution process explanation, common errors table, and bonus knowledge section. Reference c-c++/stage-1/level-1/lesson.md for the gold standard format.

### Key Concepts

- Review the code structure specific to Rust
- Understand the execution flow
- Learn common pitfalls and solutions

### Next Steps

Practice the code and experiment with variations!

---

**Congratulations! Keep coding!**


---

## SOLUTION GUIDE (No cheating until you've tried!)

### Expected Program Behavior

```rust
Temperature Converter
=====================
What conversion do you want?
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
Enter choice (1 or 2): 1
Enter temperature in Celsius: 25
25°C is equal to 77°F

Temperature Converter
=====================
What conversion do you want?
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
Enter choice (1 or 2): 2
Enter temperature in Fahrenheit: 77
77°F is equal to 25°C
```rust

### Sample Implementation

```rust
use std::io;

fn main() {
    println!("Temperature Converter");
    println!("=====================");
    println!("What conversion do you want?");
    println!("1. Celsius to Fahrenheit");
    println!("2. Fahrenheit to Celsius");
    print!("Enter choice (1 or 2): ");
    
    // Flush stdout to ensure prompt appears
    io::Write::flush(&mut io::stdout()).unwrap();
    
    let mut choice = String::new();
    io::stdin().read_line(&mut choice).unwrap();
    let choice: u32 = match choice.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Invalid choice. Please enter 1 or 2.");
            return;
        }
    };
    
    if choice == 1 {
        // Celsius to Fahrenheit
        print!("Enter temperature in Celsius: ");
        io::Write::flush(&mut io::stdout()).unwrap();
        
        let mut celsius = String::new();
        io::stdin().read_line(&mut celsius).unwrap();
        let celsius: f64 = match celsius.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Invalid temperature. Please enter a number.");
                return;
            }
        };
        
        let fahrenheit = (celsius * 9.0 / 5.0) + 32.0;
        println!("{:.1}°C is equal to {:.1}°F", celsius, fahrenheit);
        
    } else if choice == 2 {
        // Fahrenheit to Celsius
        print!("Enter temperature in Fahrenheit: ");
        io::Write::flush(&mut io::stdout()).unwrap();
        
        let mut fahrenheit = String::new();
        io::stdin().read_line(&mut fahrenheit).unwrap();
        let fahrenheit: f64 = match fahrenheit.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Invalid temperature. Please enter a number.");
                return;
            }
        };
        
        let celsius = (fahrenheit - 32.0) * 5.0 / 9.0;
        println!("{:.1}°F is equal to {:.1}°C", fahrenheit, celsius);
        
    } else {
        println!("Invalid choice. Please enter 1 or 2.");
    }
}
```rust

### Implementation Analysis

**Key Rust Concepts Used:**
- **`use std::io`** - Import input/output functionality
- **`println!` and `print!`** - Output macros
- **`io::Write::flush`** - Ensure prompts display immediately
- **`String::new()`** - Create mutable string for input
- **`read_line()`** - Read user input
- **`trim().parse()`** - Convert string to number with error handling
- **`match` expressions** - Handle parsing results
- **Floating-point arithmetic** - `f64` for temperature calculations
- **Formatted output** - `{:.1}` for one decimal place

**Error Handling:**
- **Invalid menu choice** - Check if input is 1 or 2
- **Non-numeric input** - Use `match` to handle parsing errors
- **Early returns** - Exit gracefully on invalid input

**Why this structure?**
- **Clear separation** - Menu choice determines conversion type
- **Input validation** - Check all inputs before processing
- **Mathematical precision** - Use floating-point for accurate calculations
- **User-friendly output** - Clear formatting with units

### Common Implementation Mistakes

| Common Issue | Why It Happens | Solution |
|--------------|----------------|----------|
| No `io::Write::flush` | Prompts don't appear before input | Flush stdout after print! |
| Wrong number type | Integer division gives wrong results | Use `f64` for temperatures |
| No error handling | Program panics on bad input | Use `match` for parsing |
| Wrong formula | Mental math error | Double-check: C→F: (C×9/5)+32, F→C: (F-32)×5/9 |
| Poor formatting | Hard to read output | Use `{:.1}` for one decimal place |

### Testing Your Program

**Test Cases to Try:**
1. **Normal conversions**: 0°C → 32°F, 100°C → 212°F
2. **Decimal inputs**: 25.5°C, 77.3°F
3. **Invalid menu choice**: Enter "3" or "abc"
4. **Invalid temperature**: Enter "not-a-number"
5. **Edge cases**: Very large/small numbers

### README.md Template

```markdown
# Temperature Converter

A simple Rust program that converts temperatures between Celsius and Fahrenheit.

## How to Run

1. Compile the program:
   ```bash
   rustc main.rs
```rust

2. Run the program:
   ```bash
   ./main
```rust

3. Follow the on-screen prompts to convert temperatures.

## Features

- Convert Celsius to Fahrenheit
- Convert Fahrenheit to Celsius
- Input validation for menu choices and temperatures
- Clear, formatted output with units

## Example Usage

```rust
Temperature Converter
=====================
What conversion do you want?
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
Enter choice (1 or 2): 1
Enter temperature in Celsius: 25
25.0°C is equal to 77.0°F
```rust
```rust

### Bonus Challenges

1. **Add Kelvin conversion** - Include absolute temperature scale
2. **Multiple conversions** - Allow converting several temperatures in one run
3. **Temperature validation** - Check for physically reasonable temperatures
4. **Better formatting** - Use tables or colored output

---

 **Congratulations! You built your first complete Rust application!** 

*Next: Data Processing Application (Student Grade Calculator)!*


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
use std::io::{self, Write};

fn main() {
    println!("Temperature Converter");
    println!("=====================");
    println!("What conversion do you want?");
    println!("1. Celsius to Fahrenheit");
    println!("2. Fahrenheit to Celsius");
    print!("Enter choice (1 or 2): ");

    // Flush stdout to ensure prompt appears
    io::stdout().flush().unwrap();

    let mut choice = String::new();
    io::stdin().read_line(&mut choice).unwrap();
    let choice: u32 = match choice.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Invalid choice. Please enter 1 or 2.");
            return;
        }
    };

    if choice == 1 {
        // Celsius to Fahrenheit
        print!("Enter temperature in Celsius: ");
        io::stdout().flush().unwrap();

        let mut celsius = String::new();
        io::stdin().read_line(&mut celsius).unwrap();
        let celsius: f64 = match celsius.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Invalid temperature. Please enter a number.");
                return;
            }
        };

        let fahrenheit = (celsius * 9.0 / 5.0) + 32.0;
        println!("{:.1}°C is equal to {:.1}°F", celsius, fahrenheit);

    } else if choice == 2 {
        // Fahrenheit to Celsius
        print!("Enter temperature in Fahrenheit: ");
        io::stdout().flush().unwrap();

        let mut fahrenheit = String::new();
        io::stdin().read_line(&mut fahrenheit).unwrap();
        let fahrenheit: f64 = match fahrenheit.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Invalid temperature. Please enter a number.");
                return;
            }
        };

        let celsius = (fahrenheit - 32.0) * 5.0 / 9.0;
        println!("{:.1}°F is equal to {:.1}°C", fahrenheit, celsius);

    } else {
        println!("Invalid choice. Please enter 1 or 2.");
    }
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
