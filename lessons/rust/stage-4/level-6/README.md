# Student Grade Analyzer

An automated Rust application that processes student grade data from files and generates comprehensive analysis reports with GPA calculations, grade distributions, and performance insights.

## Features

- **Automated batch processing** of student data from files
- **GPA calculation** and letter grade assignment (4.0 scale)
- **Class statistics** including average GPA and grade distribution
- **Individual student reports** with detailed performance analysis
- **File-based input/output** with error handling
- **Robust data validation** for malformed input
- **Comprehensive reporting** in both console and file formats

## Data Format

Create a `students.txt` file in the following CSV-like format:

```
# Student Grade Data File
# Format: ID,Name,Subject1:Score,Subject2:Score,...
1001,Alice Johnson,Math:95,Science:92,English:98,History:96
1002,Bob Smith,Math:87,Science:89,English:85,History:88
1003,Carol Davis,Math:78,Science:82,English:75,History:80
```

### Format Rules

- **Comments**: Lines starting with `#` are ignored
- **Empty lines**: Automatically skipped
- **Student record**: `ID,Name,Subject:Score,Subject:Score,...`
- **ID**: Unique numeric identifier
- **Name**: Student full name (can contain spaces)
- **Grades**: Subject:Score pairs separated by commas
- **Scores**: Numeric values from 0-100

## How to Run

1. **Create your data file**:
   ```bash
   # Create students.txt with your student data
   nano students.txt
   ```

2. **Compile the program**:
   ```bash
   rustc main.rs
   ```

3. **Run the analyzer**:
   ```bash
   ./main
   ```

4. **View results**:
   - Reports display on screen
   - Detailed report saved to `grade_report.txt`

## Example Output

```
Student Grade Analyzer
======================

Processing student data from file...

 CLASS SUMMARY REPORT
======================

Total Students: 5
Class Average GPA: 3.42
Grade Distribution:
  A: 2 students (40.0%)
  B: 1 students (20.0%)
  C: 1 students (20.0%)
  D: 1 students (20.0%)
  F: 0 students (0.0%)

Top Performer: Alice Johnson (4.00 GPA)
Needs Improvement: Charlie Brown (2.10 GPA)

 INDIVIDUAL STUDENT REPORTS
==============================

Student: Alice Johnson
ID: 1001
Grades: Math:95, Science:92, English:98, History:96
Average: 95.25% (A)
GPA: 4.00
Status: Excellent performance!

Analysis complete! Reports saved to grade_report.txt
```

## Grading Scale

| Percentage Range | Letter Grade | GPA |
|------------------|--------------|-----|
| 90.0 - 100.0    | A           | 4.0 |
| 80.0 - 89.9     | B           | 3.0 |
| 70.0 - 79.9     | C           | 2.0 |
| 60.0 - 69.9     | D           | 1.0 |
| 0.0 - 59.9      | F           | 0.0 |

## Program Architecture

### Core Components

1. **Data Reader**: Parses student data from text files with error handling
2. **Student Struct**: Encapsulates all student information and calculations
3. **Grade Calculator**: Automated GPA and letter grade computation
4. **Report Generator**: Creates formatted reports for console and file output
5. **Statistics Engine**: Calculates class averages and distributions

### Key Features

- **Error Recovery**: Continues processing despite malformed data
- **Flexible Subjects**: Supports any number of subjects per student
- **Performance Analysis**: Identifies top/bottom performers automatically
- **File Output**: Saves detailed reports for record keeping
- **Validation**: Ensures data integrity and reasonable score ranges

## Sample Data Files

### Basic Example
```
1001,Alice Johnson,Math:95,Science:92
1002,Bob Smith,Math:87,Science:89
```

### Comprehensive Example
```
# Advanced Student Data
1001,Alice Johnson,Math:95,Science:92,English:98,History:96,Art:94
1002,Bob Smith,Math:87,Science:89,English:85,History:88,PE:91
1003,Carol Davis,Math:78,Science:82,English:75,History:80,Computer:88
```

## Error Handling

The program handles various error conditions gracefully:

- **Missing file**: Clear error message with instructions
- **Malformed data**: Skips invalid lines with warnings
- **Invalid scores**: Rejects scores outside 0-100 range
- **Missing grades**: Warns about students with no valid grades
- **File write errors**: Continues execution with warning

## Output Files

### Console Output
- Real-time processing status
- Class summary with statistics
- Individual student reports
- Processing completion message

### File Output (`grade_report.txt`)
- Timestamped report header
- Complete class statistics
- Detailed individual reports
- Formatted for printing/archiving

## Technical Details

- **Language**: Rust
- **File I/O**: Standard library `std::fs`
- **Data Structures**: `HashMap` for grades, `Vec` for students
- **Error Handling**: `Result<T, E>` with `?` operator
- **Memory Management**: Efficient processing of student data
- **Type Safety**: Compile-time guarantees for data integrity

## Customization Options

### Grading Scale
Modify the `calculate_gpa()` and `calculate_letter_grade()` functions to change grading criteria.

### Report Format
Customize output formatting in `generate_class_summary()` and `generate_individual_reports()`.

### Data Validation
Adjust validation rules in `read_student_data()` for different requirements.

## Troubleshooting

### Common Issues

| Problem | Symptom | Solution |
|---------|---------|----------|
| File not found | "Error reading student data" | Ensure `students.txt` exists in current directory |
| No valid data | "No valid student data found" | Check data format matches specification |
| Compilation error | Rust compiler errors | Verify Rust installation and syntax |
| Permission denied | Cannot write report file | Check write permissions in directory |

### Data Format Issues

- **Extra commas**: Ensure proper CSV formatting
- **Missing colons**: Subject:Score format required
- **Invalid scores**: Must be numeric 0-100
- **Empty fields**: All fields (ID, Name, at least one grade) required

## Learning Outcomes

This automated application demonstrates:
- **File I/O operations** in Rust
- **Data parsing and validation**
- **Struct-based data organization**
- **Error handling and recovery**
- **Automated report generation**
- **Batch processing techniques**

---

*Built as part of Stage 4: Full Problem Solving in the Rust Programming Curriculum*