# Grade Management System

A complete C application for managing student grades and academic records with file persistence.

## Features

- **Student Management**: Add and view student information
- **Grade Recording**: Record scores for assignments, quizzes, and exams
- **GPA Calculation**: Automatic GPA calculation with letter grades
- **Data Persistence**: Save and load data from binary files
- **Input Validation**: Robust error handling and user input validation
- **Menu-Driven Interface**: Easy-to-use console interface

## Quick Start

1. **Compile the program**:
   ```bash
   gcc main.c -o grade_manager
   ```

2. **Run the application**:
   ```bash
   ./grade_manager
   ```

3. **Use the menu system** to manage students and grades

4. **Data is automatically saved** to `grades.dat` when you exit

## Menu Options

### Main Menu
- **1. Add Student** - Register new students with ID and name
- **2. Add Grade** - Record grades for assignments
- **3. View Student Details** - Display student info and grades
- **4. View All Students** - List all registered students
- **5. Calculate GPA** - Compute GPA for a specific student
- **6. Save Data** - Manually save data to file
- **7. Exit** - Save and exit the program

## Usage Examples

### Adding a Student
```
 ADD NEW STUDENT
=================
Enter student ID: 12345
Enter student name: Alice Johnson
 Student 'Alice Johnson' added successfully with ID: 12345
```

### Recording a Grade
```
 ADD GRADE
============
Enter student ID: 12345
Enter assignment name: Midterm Exam
Enter score (0-100): 85.5
Enter maximum score: 100
 Grade added for Midterm Exam: 85.5/100.0
```

### Viewing Student Details
```
 VIEW STUDENT DETAILS
======================
Enter student ID: 12345
Student ID: 12345
Name: Alice Johnson
Total Grades: 2

 GRADES:
----------
Midterm Exam: 85.5/100.0 (85.5%)
Final Project: 92.0/100.0 (92.0%)
```

### GPA Calculation
```
 GPA CALCULATION
==================
Enter student ID: 12345
Student: Alice Johnson
Average Score: 88.8%
GPA: 3.0/4.0
Letter Grade: B
```

## Data Files

### grades.dat
- **Purpose**: Binary file storing all student and grade data
- **Auto-created**: Generated automatically when data is saved
- **Backup**: Consider backing up this file regularly

## GPA Scale

| Percentage | GPA | Letter Grade |
|------------|-----|--------------|
| 90-100%    | 4.0 | A            |
| 80-89%     | 3.0 | B            |
| 70-79%     | 2.0 | C            |
| 60-69%     | 1.0 | D            |
| 0-59%      | 0.0 | F            |

## Technical Details

### Data Structures
- **Student**: Contains ID, name, and grade count
- **Grade**: Links to student ID with assignment details and scores

### File Format
Binary format with:
- Student count (int)
- Student array (Student structs)
- Grade count (int)
- Grade array (Grade structs)

### Memory Management
- Fixed-size arrays for simplicity
- No dynamic memory allocation
- Stack-based data structures

## Limitations

- Maximum 100 students
- Maximum 500 grades total
- No grade deletion functionality
- Simple GPA calculation (average of percentages)

## Future Enhancements

### Potential Additions
- **Grade Deletion**: Remove incorrect grades
- **Student Removal**: Delete student records
- **Advanced GPA**: Weighted GPA calculations
- **Grade Categories**: Homework, quizzes, exams with different weights
- **Export Reports**: CSV or text file reports
- **Search Functionality**: Find students by name
- **Grade Statistics**: Class averages and distributions

### Technical Improvements
- **Dynamic Memory**: Use malloc/free for flexible sizing
- **Linked Lists**: More efficient data structures
- **Database Integration**: Replace file storage with SQL
- **Input Sanitization**: Better string input handling
- **Error Recovery**: Graceful handling of file corruption

## Learning Outcomes

This application demonstrates:
- **Struct Usage**: Defining and using custom data types
- **File I/O**: Binary file operations in C
- **Array Management**: Working with fixed-size arrays
- **Input Validation**: Robust user input handling
- **Modular Design**: Separating code into logical functions
- **Menu Systems**: Creating user-friendly interfaces
- **Data Persistence**: Saving and loading application state

## Compilation

### Requirements
- GCC compiler
- Standard C libraries (stdio.h, stdlib.h, string.h)

### Build Command
```bash
gcc main.c -o grade_manager -Wall -Wextra
```

### Clean Build
```bash
rm -f grade_manager grades.dat
gcc main.c -o grade_manager -Wall -Wextra
```

---

*Built as Level 1 of Stage 4: Full Problem Solving in the C/C++ Programming Curriculum*