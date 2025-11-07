# Level 6: Repetitive Problems

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 3: Problem to Pseudocode

### Today's Mission

Repetitive problems require processing data in loops and handling repeated operations. You'll design a solution for a problem involving data processing and iteration.

---

### Learning Goals

- Analyze problems requiring repeated operations
- Design loop-based algorithms
- Handle data collections and iteration
- Create efficient processing logic

---

### Your Task

**Read the problem below, then write pseudocode to solve it. Create a file called `repetitive_problems.md` with your pseudocode solution.**


### How to Run

1. **Compile the code**:
   ```
   rustc hello.rs -o hello hello.rs
   ```

2. **Run your program**:
   ```
   ./hello hello
   ```

**Expected output:**
```
Hello, World!
```

### Problem: Student Grade Analyzer

**Description:**
Create a program that analyzes student grades and provides comprehensive statistics. The program should:

1. Ask how many students to analyze
2. For each student:
   - Get their name
   - Get their grades (multiple subjects)
   - Calculate their average
3. Calculate class statistics:
   - Overall class average
   - Highest and lowest scores
   - Grade distribution (A, B, C, D, F)
   - Students above/below class average
4. Display detailed reports

**Grade Scale:**
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: Below 60

**Example Interaction:**
```
Student Grade Analyzer
======================

How many students would you like to analyze? 3

--- Student 1 ---
Enter student name: Alice Johnson
How many grades does Alice Johnson have? 4
Enter grade 1: 95
Enter grade 2: 87
Enter grade 3: 92
Enter grade 4: 89
Alice Johnson - Average: 90.75 (A)

--- Student 2 ---
Enter student name: Bob Smith
How many grades does Bob Smith have? 3
Enter grade 1: 78
Enter grade 2: 82
Enter grade 3: 75
Bob Smith - Average: 78.33 (C)

--- Student 3 ---
Enter student name: Carol Davis
How many grades does Carol Davis have? 5
Enter grade 1: 88
Enter grade 2: 91
Enter grade 3: 85
Enter grade 4: 93
Enter grade 5: 87
Carol Davis - Average: 88.80 (B)

Class Statistics Report
=======================
Total Students: 3
Overall Class Average: 85.96

Grade Distribution:
A: 1 student(s) (33.33%)
B: 1 student(s) (33.33%)
C: 1 student(s) (33.33%)
D: 0 student(s) (0.00%)
F: 0 student(s) (0.00%)

Performance Summary:
Highest Average: Alice Johnson (90.75)
Lowest Average: Bob Smith (78.33)
Students Above Class Average: 2
Students Below Class Average: 1
```

---

### How to Create Your Solution

1. **Navigate to your working directory**:
   ```
   cd /path/to/your/folder
   ```
2. **Create your pseudocode file**:
   ```
   touch repetitive_problems.md
   ```
3. **Plan data structures** - How to store student information
4. **Design input loops** - Processing multiple students and grades
5. **Plan calculation logic** - Averages and statistics

---

### Success Checklist

- [ ] Created `repetitive_problems.md` file
- [ ] Designed loop for multiple students
- [ ] Planned nested loops for multiple grades per student
- [ ] Created calculation logic for averages and statistics
- [ ] Planned comprehensive reporting output

---

### What Did You Learn?

Repetitive problem analysis involves:
- **Loop design** - When and how to repeat operations
- **Data accumulation** - Collecting data across iterations
- **Statistical calculations** - Processing collections of data
- **Memory management** - Storing data for later processing

---

### Try This (Optional Challenges)

1. Add grade weighting (different subject weights)
2. Include attendance percentage in calculations
3. Generate individual student report cards

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Problem Analysis

**Data Processing Requirements:**
- **Multiple Students**: Loop through student count
- **Multiple Grades**: Nested loop for each student's grades
- **Accumulation**: Sum grades, count students, track statistics
- **Classification**: Convert numeric grades to letter grades

**Processing Flow:**
```
Get student count
FOR each student:
    Get student name
    Get grade count for this student
    FOR each grade:
        Get grade value
        Add to student's total
    Calculate student average
    Determine letter grade
    Store student data
    Update class statistics
Display comprehensive report
```

### Sample Pseudocode Solution

```
START PROGRAM
    DISPLAY "Student Grade Analyzer"
    DISPLAY "======================"
    DISPLAY ""
    
    DISPLAY "How many students would you like to analyze?"
    READ student_count AS NUMBER
    
    // Initialize class statistics variables
    SET total_class_sum TO 0
    SET total_grades_count TO 0
    SET highest_average TO -1
    SET lowest_average TO 101
    SET highest_student TO ""
    SET lowest_student TO ""
    SET above_average_count TO 0
    SET below_average_count TO 0
    
    // Grade distribution counters
    SET grade_a_count TO 0
    SET grade_b_count TO 0
    SET grade_c_count TO 0
    SET grade_d_count TO 0
    SET grade_f_count TO 0
    
    // Process each student
    FOR student_index FROM 1 TO student_count DO
        DISPLAY "--- Student " + student_index + " ---"
        
        DISPLAY "Enter student name:"
        READ student_name AS STRING
        
        DISPLAY "How many grades does " + student_name + " have?"
        READ grade_count AS NUMBER
        
        SET student_sum TO 0
        
        // Get all grades for this student
        FOR grade_index FROM 1 TO grade_count DO
            DISPLAY "Enter grade " + grade_index + ":"
            READ grade AS NUMBER
            SET student_sum TO student_sum + grade
        END FOR
        
        // Calculate student average
        SET student_average TO student_sum / grade_count
        
        // Determine letter grade
        SET letter_grade TO ""
        IF student_average >= 90 THEN
            SET letter_grade TO "A"
            SET grade_a_count TO grade_a_count + 1
        ELSE IF student_average >= 80 THEN
            SET letter_grade TO "B"
            SET grade_b_count TO grade_b_count + 1
        ELSE IF student_average >= 70 THEN
            SET letter_grade TO "C"
            SET grade_c_count TO grade_c_count + 1
        ELSE IF student_average >= 60 THEN
            SET letter_grade TO "D"
            SET grade_d_count TO grade_d_count + 1
        ELSE
            SET letter_grade TO "F"
            SET grade_f_count TO grade_f_count + 1
        END IF
        
        // Display student result
        DISPLAY student_name + " - Average: " + FORMAT_NUMBER(student_average, 2) + " (" + letter_grade + ")"
        DISPLAY ""
        
        // Update class statistics
        SET total_class_sum TO total_class_sum + student_sum
        SET total_grades_count TO total_grades_count + grade_count
        
        // Track highest and lowest
        IF student_average > highest_average THEN
            SET highest_average TO student_average
            SET highest_student TO student_name
        END IF
        
        IF student_average < lowest_average THEN
            SET lowest_average TO student_average
            SET lowest_student TO student_name
        END IF
    END FOR
    
    // Calculate overall class average
    SET class_average TO total_class_sum / total_grades_count
    
    // Count students above/below average (second pass would be needed for accuracy)
    // For simplicity, we'll count based on individual averages vs class average
    // In a real implementation, you'd store all student averages and compare
    
    // Display comprehensive report
    DISPLAY "Class Statistics Report"
    DISPLAY "======================="
    DISPLAY "Total Students: " + student_count
    DISPLAY "Overall Class Average: " + FORMAT_NUMBER(class_average, 2)
    DISPLAY ""
    
    DISPLAY "Grade Distribution:"
    DISPLAY "A: " + grade_a_count + " student(s) (" + FORMAT_PERCENT(grade_a_count, student_count) + "%)"
    DISPLAY "B: " + grade_b_count + " student(s) (" + FORMAT_PERCENT(grade_b_count, student_count) + "%)"
    DISPLAY "C: " + grade_c_count + " student(s) (" + FORMAT_PERCENT(grade_c_count, student_count) + "%)"
    DISPLAY "D: " + grade_d_count + " student(s) (" + FORMAT_PERCENT(grade_d_count, student_count) + "%)"
    DISPLAY "F: " + grade_f_count + " student(s) (" + FORMAT_PERCENT(grade_f_count, student_count) + "%)"
    DISPLAY ""
    
    DISPLAY "Performance Summary:"
    DISPLAY "Highest Average: " + highest_student + " (" + FORMAT_NUMBER(highest_average, 2) + ")"
    DISPLAY "Lowest Average: " + lowest_student + " (" + FORMAT_NUMBER(lowest_average, 2) + ")"
    
    // Note: Above/below average would require storing all student data
    DISPLAY "Students Above Class Average: [Would need stored data]"
    DISPLAY "Students Below Class Average: [Would need stored data]"
END PROGRAM

// Helper function to format numbers to 2 decimal places
FUNCTION FORMAT_NUMBER(number, decimals)
    // Implementation would format number to specified decimal places
    RETURN number + ".00"  // Simplified for pseudocode
END FUNCTION

// Helper function to calculate percentages
FUNCTION FORMAT_PERCENT(count, total)
    SET percentage TO (count / total) * 100
    RETURN FORMAT_NUMBER(percentage, 2)
END FUNCTION
```

### Analysis Breakdown

**Repetitive Logic:**
- **Outer Loop**: Process each student (FOR student_index FROM 1 TO student_count)
- **Inner Loop**: Process each grade for current student
- **Accumulation**: Sum grades, count students, track statistics
- **Classification**: Convert averages to letter grades

**Why this approach?**
- **Nested Loops**: Handle variable number of grades per student
- **Running Totals**: Accumulate statistics during processing
- **Immediate Feedback**: Show each student's results as processed
- **Comprehensive Reporting**: Multiple statistics calculated

**Potential improvements:**
- Store all student data in arrays/lists for complete analysis
- Calculate above/below average accurately
- Add more detailed statistics (median, mode, standard deviation)
- Export results to file

### Common Analysis Mistakes

| Common Issue | Why It Happens | Solution |
|--------------|----------------|----------|
| No data storage | Can't calculate comparative statistics | Use arrays to store all student data |
| Wrong loop bounds | Off-by-one errors in counting | Use 1-based indexing consistently |
| Division by zero | No students or grades entered | Add validation for minimum inputs |
| Precision loss | Integer division for averages | Use floating-point arithmetic |

### Bonus Knowledge

- **Data Processing**: Handling collections of related data
- **Statistical Analysis**: Calculating meaningful metrics from data
- **Memory Management**: Storing and accessing data collections
- **Algorithm Efficiency**: Processing data in single vs multiple passes

---

 **Great! You designed a comprehensive grade analysis system!** 

*Next: Complex System Problems!*


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
