# Level 2: Data Management Problems

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 3: Problem to Pseudocode

### Today's Mission

Data management involves organizing, storing, and manipulating information. You'll analyze a problem that requires managing multiple pieces of data.

---

### Learning Goals

- Understand data organization principles
- Learn to manage multiple variables
- Practice data manipulation logic
- Design solutions for information processing

---

### Your Task

**Read the problem below, then write pseudocode to solve it. Create a file called `data_management.md` with your pseudocode solution.**


### How to Compile and Run

1. **Compile the code**:
   ```bash
   rustc hello.rs -o hello hello.rs
   ```

2. **Run your program**:
   ```bash
   ./hello hello
   ```

**Expected output:**
```
Hello, World!
```

### Problem: Student Grade Calculator

**Description:**
Create a program that helps teachers calculate final grades for students. The program should:

1. Ask for the student's name
2. Ask for scores from 3 assignments (each worth different percentages)
3. Calculate the weighted average
4. Determine the letter grade
5. Display a complete report

**Grading Scale:**
- A: 90-100%
- B: 80-89%
- C: 70-79%
- D: 60-69%
- F: Below 60%

**Assignment Weights:**
- Assignment 1: 30%
- Assignment 2: 35%
- Assignment 3: 35%

**Example Interaction:**
```rust
Enter student name: Alice Johnson
Enter Assignment 1 score (0-100): 85
Enter Assignment 2 score (0-100): 92
Enter Assignment 3 score (0-100): 78

Student Report for Alice Johnson
--------------------------
Assignment 1: 85/100 (30%)
Assignment 2: 92/100 (35%)
Assignment 3: 78/100 (35%)
Final Average: 84.9%
Letter Grade: B
```

---

### How to Create Your Solution

1. **Navigate to your working directory**:
   ```bash
   cd /path/to/your/folder
   ```
2. **Create your pseudocode file**:
   ```bash
   touch data_management.md
   ```
3. **Think about data storage** - What variables do you need?
4. **Plan calculations** - How to compute weighted average?
5. **Design output** - How to present the information clearly?

---

### Success Checklist

- [ ] Created `data_management.md` file
- [ ] Identified all data that needs to be stored
- [ ] Planned weighted average calculation
- [ ] Designed letter grade determination logic
- [ ] Considered input validation (scores 0-100)
- [ ] Planned clear report formatting

---

### What Did You Learn?

Data management involves:
- **Data collection** - Gathering all required information
- **Data storage** - Organizing information in variables
- **Data processing** - Performing calculations on the data
- **Data presentation** - Displaying results in a useful format

---

### Try This (Optional Challenges)

1. Add more assignments with different weights
2. Include extra credit points
3. Add class statistics (average, highest, lowest)

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Problem Analysis

**Data to Manage:**
- Student name (text)
- 3 assignment scores (numbers 0-100)
- 3 weight percentages (30%, 35%, 35%)
- Calculated average (number)
- Letter grade (text)

**Calculations Needed:**
- Weighted average = (score1 × 0.30) + (score2 × 0.35) + (score3 × 0.35)
- Letter grade based on average

### Sample Pseudocode Solution

```rust
START PROGRAM
    DISPLAY "Student Grade Calculator"
    DISPLAY "Enter student name:"
    READ student_name AS TEXT
    
    DISPLAY "Enter Assignment 1 score (0-100):"
    READ score1 AS NUMBER
    
    DISPLAY "Enter Assignment 2 score (0-100):"
    READ score2 AS NUMBER
    
    DISPLAY "Enter Assignment 3 score (0-100):"
    READ score3 AS NUMBER
    
    // Calculate weighted average
    SET weight1 TO 0.30
    SET weight2 TO 0.35
    SET weight3 TO 0.35
    
    SET weighted_score1 TO score1 * weight1
    SET weighted_score2 TO score2 * weight2
    SET weighted_score3 TO score3 * weight3
    
    SET final_average TO weighted_score1 + weighted_score2 + weighted_score3
    
    // Determine letter grade
    IF final_average >= 90 THEN
        SET letter_grade TO "A"
    ELSE IF final_average >= 80 THEN
        SET letter_grade TO "B"
    ELSE IF final_average >= 70 THEN
        SET letter_grade TO "C"
    ELSE IF final_average >= 60 THEN
        SET letter_grade TO "D"
    ELSE
        SET letter_grade TO "F"
    END IF
    
    // Display report
    DISPLAY "Student Report for " + student_name
    DISPLAY "--------------------------"
    DISPLAY "Assignment 1: " + score1 + "/100 (30%)"
    DISPLAY "Assignment 2: " + score2 + "/100 (35%)"
    DISPLAY "Assignment 3: " + score3 + "/100 (35%)"
    DISPLAY "Final Average: " + final_average + "%"
    DISPLAY "Letter Grade: " + letter_grade
END PROGRAM
```

### Analysis Breakdown

**Data Organization:**
- **Student info**: Name stored as text
- **Scores**: Three separate variables for clarity
- **Weights**: Constants for calculation accuracy
- **Results**: Average and grade derived from inputs

**Why this structure?**
- **Modular calculations**: Break down weighted average step-by-step
- **Clear grade boundaries**: Explicit ranges for each letter grade
- **Comprehensive output**: Shows all input data plus results
- **Readable format**: Organized report layout

**Potential improvements:**
- Input validation for scores (0-100 range)
- Round final average to 1 decimal place
- Add grade point average calculation

### Common Analysis Mistakes

| Common Issue | Why It Happens | Solution |
|--------------|----------------|----------|
| Wrong weights | Misunderstanding percentages | Convert to decimals (30% = 0.30) |
| No grade boundaries | Forgetting F grade | Include all ranges explicitly |
| Poor variable names | Unclear data meaning | Use descriptive names |
| Missing validation | Invalid score inputs | Check ranges before calculations |

### Bonus Knowledge

- **Data Flow**: How information moves through the program
- **State Management**: Tracking multiple related values
- **Business Logic**: Real-world calculation rules
- **Report Generation**: Formatting data for human consumption

---

 **Excellent! You managed multiple data points effectively!** 

*Next: Mathematical Problems!*
