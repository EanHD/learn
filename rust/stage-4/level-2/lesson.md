# Level 2: Data Processing Application
## Stage 4: Full Problem Solving

### Today's Mission

Now you'll implement a data processing application that manages multiple pieces of information and performs calculations on them.

---

### Learning Goals

- Implement data collection and storage in Rust
- Handle multiple input values
- Perform mathematical calculations with stored data
- Create formatted output reports
- Manage program state across operations

---

### Your Task

**Implement the Student Grade Calculator program in Rust. Create the following files:**

1. **`main.rs`** - The main program file
2. **`README.md`** - Instructions for running the program

### Program Requirements

Based on your Stage 3 pseudocode, implement a student grade calculator that:

1. **Collects student information** (name and 3 assignment scores)
2. **Validates input data** (scores must be 0-100)
3. **Calculates weighted average** using assignment weights
4. **Determines letter grade** based on standard scale
5. **Displays comprehensive report** with all information

**Assignment Weights:**
- Assignment 1: 30%
- Assignment 2: 35%
- Assignment 3: 35%

**Grading Scale:**
- A: 90-100%
- B: 80-89%
- C: 70-79%
- D: 60-69%
- F: Below 60%

---

### Implementation Steps

1. **Create the project structure**:
   ```bash
   cd /home/eanhd/LEARN/rust/stage-4-full-problem-solving/level-2-data-processing-application
   ```

2. **Create `main.rs`** with your Rust implementation

3. **Test your program**:
   ```bash
   rustc main.rs
   ./main
   ```

4. **Create `README.md`** with usage instructions

---

### Success Checklist

- [ ] Created `main.rs` file
- [ ] Program collects student name and 3 scores
- [ ] Input validation ensures scores are 0-100
- [ ] Weighted average calculation is correct
- [ ] Letter grade determination works properly
- [ ] Formatted report displays all information clearly

---

### What You'll Learn

Data processing involves:
- **Data collection** - Gathering multiple related inputs
- **Data validation** - Ensuring input quality
- **Data manipulation** - Performing calculations on stored data
- **Data presentation** - Formatting results for users

---

### Implementation Tips

1. **Use variables** to store student data
2. **Validate inputs** before calculations
3. **Use floating-point math** for percentages
4. **Format output** clearly with labels
5. **Test with different score combinations**

---

## Need Help with Rust?

- **Multiple inputs**: Collect data step by step
- **Validation**: Check ranges with conditional statements
- **Calculations**: Use `f64` for precise math
- **Output formatting**: Use `println!` with descriptive text

---

<div style="page-break-after: always;"></div>

---

## SOLUTION GUIDE (No cheating until you've tried!)

### Expected Program Behavior

```
Student Grade Calculator
========================
Enter student name: Alice Johnson
Enter Assignment 1 score (0-100): 85
Enter Assignment 2 score (0-100): 92
Enter Assignment 3 score (0-100): 78

Student Report for Alice Johnson
-------------------------------
Assignment 1: 85/100 (30%)
Assignment 2: 92/100 (35%)
Assignment 3: 78/100 (35%)
Final Average: 84.9%
Letter Grade: B
```

### Sample Implementation

```rust
use std::io::{self, Write};

fn main() {
    println!("Student Grade Calculator");
    println!("========================");

    // Get student name
    print!("Enter student name: ");
    io::stdout().flush().unwrap();
    let mut student_name = String::new();
    io::stdin().read_line(&mut student_name).unwrap();
    let student_name = student_name.trim();

    // Get assignment scores with validation
    let score1 = get_valid_score("Enter Assignment 1 score (0-100): ");
    let score2 = get_valid_score("Enter Assignment 2 score (0-100): ");
    let score3 = get_valid_score("Enter Assignment 3 score (0-100): ");

    // Calculate weighted average
    let weight1 = 0.30;
    let weight2 = 0.35;
    let weight3 = 0.35;

    let final_average = (score1 * weight1) + (score2 * weight2) + (score3 * weight3);

    // Determine letter grade
    let letter_grade = if final_average >= 90.0 {
        "A"
    } else if final_average >= 80.0 {
        "B"
    } else if final_average >= 70.0 {
        "C"
    } else if final_average >= 60.0 {
        "D"
    } else {
        "F"
    };

    // Display report
    println!("\nStudent Report for {}", student_name);
    println!("-------------------------------");
    println!("Assignment 1: {}/100 (30%)", score1);
    println!("Assignment 2: {}/100 (35%)", score2);
    println!("Assignment 3: {}/100 (35%)", score3);
    println!("Final Average: {:.1}%", final_average);
    println!("Letter Grade: {}", letter_grade);
}

fn get_valid_score(prompt: &str) -> f64 {
    loop {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        match input.trim().parse::<f64>() {
            Ok(score) if score >= 0.0 && score <= 100.0 => return score,
            Ok(_) => println!("Score must be between 0 and 100."),
            Err(_) => println!("Please enter a valid number."),
        }
    }
}
```

### Implementation Analysis

**Key Rust Concepts Used:**
- **Functions**: `get_valid_score()` for reusable input validation
- **Loop for validation**: `loop` with input checking
- **Pattern matching**: `match` for parsing and validation
- **Floating-point math**: `f64` for precise calculations
- **String handling**: `trim()` for clean input
- **Formatted output**: `println!` with placeholders

**Program Structure:**
- **Main function**: Orchestrates the program flow
- **Helper function**: Handles input validation logic
- **Data collection**: Gathers all required information
- **Calculations**: Performs weighted average computation
- **Output**: Displays formatted report

**Why this structure?**
- **Modular design**: Separate function for input validation
- **Error handling**: Comprehensive input checking
- **Clear calculations**: Step-by-step weighted average
- **Professional output**: Well-formatted report

### Common Implementation Mistakes

| Common Issue | Why It Happens | Solution |
|--------------|----------------|----------|
| No input validation | Program crashes on invalid input | Use loops with validation checks |
| Wrong weight calculation | Forgetting decimal conversion | Use 0.30 not 30 for percentages |
| Integer division | Loss of precision in averages | Use `f64` for all calculations |
| Poor error messages | Users confused about mistakes | Provide clear feedback |
| No function reuse | Duplicate validation code | Create helper functions |

### Testing Your Program

**Test Cases to Try:**
1. **Perfect scores**: 100, 100, 100 → Should be A
2. **Boundary cases**: 89.9, 79.9, 69.9, 59.9 → Different grades
3. **Invalid inputs**: Negative numbers, numbers > 100, text input
4. **Decimal scores**: 85.5, 92.3, 78.8 → Should work correctly

### README.md Template

```markdown
# Student Grade Calculator

A Rust program that calculates weighted final grades for students based on assignment scores.

## How to Run

1. Compile the program:
   ```bash
   rustc main.rs
   ```

2. Run the program:
   ```bash
   ./main
   ```

3. Enter student information and scores as prompted.

## Features

- Input validation for scores (0-100 range)
- Weighted average calculation (30%, 35%, 35%)
- Automatic letter grade assignment
- Formatted student report

## Example Usage

```
Student Grade Calculator
========================
Enter student name: Alice Johnson
Enter Assignment 1 score (0-100): 85
Enter Assignment 2 score (0-100): 92
Enter Assignment 3 score (0-100): 78

Student Report for Alice Johnson
-------------------------------
Assignment 1: 85/100 (30%)
Assignment 2: 92/100 (35%)
Assignment 3: 78/100 (35%)
Final Average: 84.9%
Letter Grade: B
```
```

### Bonus Challenges

1. **Multiple students** - Process several students in one run
2. **Custom weights** - Allow teachers to set their own weight percentages
3. **Grade statistics** - Show class averages and distributions
4. **File output** - Save reports to text files

---

 **Great! You built a data processing application!** 

*Next: Mathematical Application (Compound Interest Calculator)!*