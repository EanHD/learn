# Level 1: Simple Problem Analysis

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 3: Problem to Pseudocode

### Today's Mission

Welcome to Stage 3! Now you'll learn to analyze problems and design solutions before writing code. This is a crucial skill for programming - thinking through the logic first!

---

### Learning Goals

- Understand problem analysis methodology
- Learn to break down simple problems
- Practice designing step-by-step solutions
- Create clear, logical pseudocode

---

### Your Task

**Read the problem below, then write pseudocode to solve it. Create a file called `simple_analysis.md` with your pseudocode solution.**


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

### Problem: Temperature Converter

**Description:**
You need to create a program that converts temperatures between Celsius and Fahrenheit. The program should:

1. Ask the user what type of conversion they want (Celsius to Fahrenheit or Fahrenheit to Celsius)
2. Ask for the temperature value to convert
3. Perform the calculation
4. Display the result

**Conversion Formulas:**
- Celsius to Fahrenheit: `F = (C × 9/5) + 32`
- Fahrenheit to Celsius: `C = (F - 32) × 5/9`

**Example Interactions:**
```rust
What conversion do you want?
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
Enter choice (1 or 2): 1
Enter temperature in Celsius: 25
25°C is equal to 77°F
```rust

---

### How to Create Your Solution

1. **Navigate to your working directory**:
   ```bash
   cd /path/to/your/folder
   ```rust
2. **Create your pseudocode file**:
   ```bash
   touch simple_analysis.md
   ```rust
3. **Write pseudocode** that solves the problem step by step
4. **Think about edge cases** (what if user enters invalid choice?)

---

### Success Checklist

- [ ] Created `simple_analysis.md` file
- [ ] Identified all required inputs and outputs
- [ ] Planned the step-by-step logic
- [ ] Handled both conversion types
- [ ] Considered user input validation
- [ ] Pseudocode is clear and logical

---

### What Did You Learn?

Problem analysis involves:
- **Understanding requirements** - What does the program need to do?
- **Identifying inputs/outputs** - What data comes in and goes out?
- **Planning the logic flow** - What steps are needed?
- **Considering edge cases** - What could go wrong?

---

### Try This (Optional Challenges)

1. Add Kelvin conversion option
2. Validate that temperature inputs are reasonable
3. Add option to convert multiple temperatures

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Problem Analysis

**Inputs:**
- User's choice (1 for C→F, 2 for F→C)
- Temperature value (number)

**Outputs:**
- Converted temperature with units

**Process:**
1. Display menu options
2. Get user's conversion choice
3. Get temperature value
4. Apply appropriate formula
5. Display result

### Sample Pseudocode Solution

```rust
START PROGRAM
    DISPLAY "Temperature Converter"
    DISPLAY "What conversion do you want?"
    DISPLAY "1. Celsius to Fahrenheit"
    DISPLAY "2. Fahrenheit to Celsius"
    DISPLAY "Enter choice (1 or 2):"
    
    READ choice AS NUMBER
    
    IF choice == 1 THEN
        DISPLAY "Enter temperature in Celsius:"
        READ celsius AS NUMBER
        SET fahrenheit TO (celsius * 9/5) + 32
        DISPLAY celsius + "°C is equal to " + fahrenheit + "°F"
    ELSE IF choice == 2 THEN
        DISPLAY "Enter temperature in Fahrenheit:"
        READ fahrenheit AS NUMBER
        SET celsius TO (fahrenheit - 32) * 5/9
        DISPLAY fahrenheit + "°F is equal to " + celsius + "°C"
    ELSE
        DISPLAY "Invalid choice. Please enter 1 or 2."
    END IF
END PROGRAM
```rust

### Analysis Breakdown

**Why this approach?**
- **Clear user interface**: Menu makes choices obvious
- **Input validation**: Checks for valid menu choice
- **Mathematical accuracy**: Uses correct formulas
- **Good output formatting**: Shows both original and converted values

**Potential improvements:**
- Add input validation for temperature values
- Round decimal results
- Allow multiple conversions without restarting

### Common Analysis Mistakes

| Common Issue | Why It Happens | Solution |
|--------------|----------------|----------|
| Missing menu | User doesn't know options | Always provide clear choices |
| No input validation | Program crashes on bad input | Check inputs before processing |
| Wrong formula | Mental math error | Double-check calculations |
| Poor output format | Hard to read results | Include units and clear labels |

### Bonus Knowledge

- **Requirements Gathering**: Understanding what the program should do
- **User Experience**: Making programs easy and intuitive to use
- **Error Handling**: Planning for unexpected user inputs
- **Modular Design**: Breaking complex problems into smaller parts

---

 **Great job! You analyzed your first programming problem!** 

*Next: Data Management Problems!*


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
