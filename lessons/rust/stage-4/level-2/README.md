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

## Grading Scale

- A: 90-100%
- B: 80-89%
- C: 70-79%
- D: 60-69%
- F: Below 60%

## Test Cases

Try these combinations:
- Perfect student: 100, 100, 100 (should be A)
- Average student: 80, 80, 80 (should be B)
- Failing student: 50, 50, 50 (should be F)