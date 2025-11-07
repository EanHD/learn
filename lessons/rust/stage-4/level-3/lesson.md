# Level 3: Mathematical Application

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 4: Full Problem Solving

### Today's Mission

Now you'll implement a mathematical application that performs complex financial calculations using advanced formulas.

---

### Learning Goals

- Implement complex mathematical formulas in Rust
- Handle financial calculations with precision
- Create user-friendly financial interfaces
- Validate numerical inputs appropriately
- Format currency and percentage outputs

---

### Your Task

**Implement the Compound Interest Calculator program in Rust. Create the following files:**

1. **`main.rs`** - The main program file
2. **`README.md`** - Instructions for running the program

### Program Requirements

Based on your Stage 3 pseudocode, implement a compound interest calculator that:

1. **Collects investment parameters** (principal, rate, years, compounding frequency)
2. **Validates all inputs** (positive amounts, reasonable rates)
3. **Calculates compound interest** using the correct formula
4. **Handles different compounding frequencies** (yearly, quarterly, monthly)
5. **Displays professional financial report** with all details

**Compound Interest Formula:**
```
A = P(1 + r/n)^(nt)
```
Where:
- A = Final amount
- P = Principal amount
- r = Annual interest rate (decimal)
- n = Number of times interest is compounded per year
- t = Number of years

**Compounding Options:**
- Yearly: n = 1
- Quarterly: n = 4
- Monthly: n = 12

---

### Implementation Steps

1. **Create the project structure**:
   ```
   cd /home/eanhd/LEARN/rust/stage-4-full-problem-solving/level-3-mathematical-application
   ```

2. **Create `main.rs`** with your Rust implementation

3. **Test your program**:
   ```
   rustc main.rs
   ./main
   ```

4. **Create `README.md`** with usage instructions

---

### Success Checklist

- [ ] Created `main.rs` file
- [ ] Program collects all required financial parameters
- [ ] Input validation ensures reasonable values
- [ ] Compound interest formula implemented correctly
- [ ] Different compounding frequencies work properly
- [ ] Professional financial report with currency formatting

---

### What You'll Learn

Mathematical applications involve:
- **Formula implementation** - Translating equations to code
- **Precision handling** - Managing floating-point calculations
- **Financial formatting** - Professional output presentation
- **Mathematical validation** - Ensuring calculation accuracy

---

### Implementation Tips

1. **Use `f64`** for all financial calculations
2. **Validate inputs** for positive values and reasonable ranges
3. **Use exponentiation** with `powf()` method
4. **Format currency** with proper decimal places
5. **Test with known values** to verify calculations

---

## Need Help with Rust?

- **Exponentiation**: Use `powf()` method on `f64`
- **Input validation**: Check ranges and handle errors
- **Currency formatting**: Use `println!` with `{:.2}` for 2 decimals
- **Mathematical operations**: All standard operators work with `f64`

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

```
Compound Interest Calculator
============================
Enter principal amount: $1000
Enter annual interest rate (%): 5
Enter number of years: 3
Compounding frequency:
1. Yearly
2. Quarterly
3. Monthly
Enter choice (1-3): 2

Investment Summary
------------------
Principal: $1000.00
Interest Rate: 5.00%
Years: 3
Compounding: Quarterly
Final Amount: $1161.54
Total Interest: $161.54
```

### Sample Implementation

```
use std::io::{self, Write};

fn main() {
    println!("Compound Interest Calculator");
    println!("============================");

    // Get principal amount
    let principal = get_positive_number("Enter principal amount: $");

    // Get annual interest rate
    let rate_percent = get_valid_rate("Enter annual interest rate (%): ");
    let rate = rate_percent / 100.0; // Convert to decimal

    // Get number of years
    let years = get_positive_integer("Enter number of years: ");

    // Get compounding frequency
    println!("Compounding frequency:");
    println!("1. Yearly");
    println!("2. Quarterly");
    println!("3. Monthly");
    let frequency_choice = get_valid_choice("Enter choice (1-3): ", 1, 3);

    // Set compounding frequency values
    let (n, frequency_name) = match frequency_choice {
        1 => (1.0, "Yearly"),
        2 => (4.0, "Quarterly"),
        3 => (12.0, "Monthly"),
        _ => (1.0, "Yearly"), // Default fallback
    };

    // Calculate compound interest
    let base = 1.0 + (rate / n);
    let exponent = n * years as f64;
    let final_amount = principal * base.powf(exponent);
    let total_interest = final_amount - principal;

    // Display results
    println!("\nInvestment Summary");
    println!("------------------");
    println!("Principal: ${:.2}", principal);
    println!("Interest Rate: {:.2}%", rate_percent);
    println!("Years: {}", years);
    println!("Compounding: {}", frequency_name);
    println!("Final Amount: ${:.2}", final_amount);
    println!("Total Interest: ${:.2}", total_interest);
}

fn get_positive_number(prompt: &str) -> f64 {
    loop {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        match input.trim().parse::<f64>() {
            Ok(num) if num > 0.0 => return num,
            Ok(_) => println!("Please enter a positive number."),
            Err(_) => println!("Please enter a valid number."),
        }
    }
}

fn get_valid_rate(prompt: &str) -> f64 {
    loop {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        match input.trim().parse::<f64>() {
            Ok(rate) if rate >= 0.0 && rate <= 100.0 => return rate,
            Ok(_) => println!("Rate must be between 0% and 100%."),
            Err(_) => println!("Please enter a valid number."),
        }
    }
}

fn get_positive_integer(prompt: &str) -> u32 {
    loop {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        match input.trim().parse::<u32>() {
            Ok(num) if num > 0 => return num,
            Ok(_) => println!("Please enter a positive number."),
            Err(_) => println!("Please enter a valid integer."),
        }
    }
}

fn get_valid_choice(prompt: &str, min: u32, max: u32) -> u32 {
    loop {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        match input.trim().parse::<u32>() {
            Ok(choice) if choice >= min && choice <= max => return choice,
            Ok(_) => println!("Please enter a number between {} and {}.", min, max),
            Err(_) => println!("Please enter a valid number."),
        }
    }
}
```

### Implementation Analysis

**Key Rust Concepts Used:**
- **Functions**: Modular input validation functions
- **Pattern matching**: `match` for menu choices and validation
- **Floating-point math**: `f64` for precise financial calculations
- **Exponentiation**: `powf()` method for compound interest formula
- **Input validation**: Comprehensive checking with helpful error messages
- **Formatted output**: Currency formatting with `{:.2}`

**Mathematical Implementation:**
- **Formula accuracy**: A = P(1 + r/n)^(nt) implemented correctly
- **Type safety**: Using appropriate numeric types
- **Precision**: Floating-point arithmetic for financial calculations
- **Edge cases**: Handling various compounding frequencies

**Why this structure?**
- **Modular validation**: Separate functions for different input types
- **Error handling**: Clear feedback for invalid inputs
- **Mathematical precision**: Proper use of floating-point operations
- **Professional output**: Financial report formatting

### Common Implementation Mistakes

| Common Issue | Why It Happens | Solution |
|--------------|----------------|----------|
| Wrong exponentiation | Using `^` instead of `powf()` | Use `powf()` method for floating-point |
| Integer division | Loss of precision in calculations | Use `f64` for all financial math |
| No input validation | Program crashes on invalid input | Validate all inputs with loops |
| Wrong formula order | Incorrect operator precedence | Use parentheses: `principal * base.powf(exponent)` |
| Poor formatting | Hard to read financial output | Use `{:.2}` for currency |

### Testing Your Program

**Test Cases to Verify:**
1. **Simple case**: $1000 at 5% for 1 year yearly → $1050.00
2. **Quarterly compounding**: $1000 at 5% for 1 year quarterly → $1050.95
3. **Multi-year**: $1000 at 5% for 3 years yearly → $1157.63
4. **Edge cases**: Very small/large amounts, 0% interest

### README.md Template

```
# Compound Interest Calculator

A Rust program that calculates compound interest for savings and investments.

## How to Run

1. Compile the program:
   ```
   rustc main.rs
```

2. Run the program:
   ```
   ./main
```

3. Enter investment details as prompted.

## Features

- Calculates compound interest with different compounding frequencies
- Input validation for all parameters
- Professional financial report formatting
- Support for yearly, quarterly, and monthly compounding

## Example Usage

```
Compound Interest Calculator
============================
Enter principal amount: $1000
Enter annual interest rate (%): 5
Enter number of years: 3
Compounding frequency:
1. Yearly
2. Quarterly
3. Monthly
Enter choice (1-3): 2

Investment Summary
------------------
Principal: $1000.00
Interest Rate: 5.00%
Years: 3
Compounding: Quarterly
Final Amount: $1161.54
Total Interest: $161.54


### Bonus Challenges

1. **Daily compounding** - Add daily compounding option
2. **Year-by-year breakdown** - Show growth for each year
3. **Comparison mode** - Compare different compounding frequencies
4. **Investment goals** - Calculate years needed to reach target amount

---

 **Excellent! You built a mathematical financial application!**

*Next: Interactive Application (Simple Banking System)!*


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic
