# Level 6: Automated Application
## Stage 4: Full Problem Solving

### Today's Mission

Now you'll implement an automated application that processes data in batches, reads from files, and generates comprehensive reports - perfect for real-world automation tasks.

---

### Learning Goals

- Implement file I/O operations in Rust
- Create automated batch processing systems
- Design comprehensive reporting features
- Handle data validation and error recovery
- Build scalable data processing applications

---

### Your Task

**Implement the Student Grade Analyzer program in Rust. Create the following files:**

1. **`main.rs`** - The main program file
2. **`students.txt`** - Sample student data file
3. **`README.md`** - Instructions for running the program

### Program Requirements

Based on your Stage 3 pseudocode, implement a student grade analyzer that:

1. **Reads student data from a file** automatically
2. **Processes multiple students** in batch mode
3. **Calculates comprehensive statistics** (averages, distributions, rankings)
4. **Generates detailed reports** with individual and class performance
5. **Handles data validation** and error recovery
6. **Provides automated analysis** without user interaction

**Data Processing Features:**
- **Batch file processing** - Read entire class data at once
- **Automated calculations** - GPA, letter grades, weighted averages
- **Statistical analysis** - Class averages, grade distributions, rankings
- **Report generation** - Individual student reports and class summaries
- **Error handling** - Invalid data detection and recovery

---

### Implementation Steps

1. **Create the project structure**:
   ```bash
   cd /home/eanhd/LEARN/rust/stage-4-full-problem-solving/level-6-automated-application
   ```

2. **Create `students.txt`** with sample data

3. **Create `main.rs`** with your Rust implementation

4. **Test your program**:
   ```bash
   rustc main.rs
   ./main
   ```

5. **Create `README.md`** with usage instructions

---

### Success Checklist

- [ ] Created `students.txt` file with sample data
- [ ] Created `main.rs` file with automated processing
- [ ] Program reads data from file automatically
- [ ] Calculates all required statistics and grades
- [ ] Generates comprehensive reports
- [ ] Handles errors gracefully

---

### What You'll Learn

Automated applications involve:
- **File I/O** - Reading and writing data files
- **Batch processing** - Handling multiple data items efficiently
- **Data structures** - Organizing complex student information
- **Error handling** - Robust processing with validation
- **Report generation** - Creating formatted output automatically

---

### Implementation Tips

1. **Use `std::fs`** for file operations
2. **Parse data** carefully with error handling
3. **Create data structures** for student information
4. **Implement calculation functions** for reusability
5. **Generate formatted reports** with clear sections

---

<div style="page-break-after: always;"></div>

---

## SOLUTION GUIDE (No cheating until you've tried!)

### Expected Program Behavior

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

Student: Bob Smith
ID: 1002
Grades: Math:87, Science:89, English:85, History:88
Average: 87.25% (B)
GPA: 3.00
Status: Good performance!

Student: Carol Davis
ID: 1003
Grades: Math:78, Science:82, English:75, History:80
Average: 78.75% (C)
GPA: 2.00
Status: Satisfactory performance.

Student: David Wilson
ID: 1004
Grades: Math:72, Science:68, English:70, History:75
Average: 71.25% (D)
GPA: 1.00
Status: Needs improvement.

Student: Eve Garcia
ID: 1005
Grades: Math:65, Science:70, English:68, History:72
Average: 68.75% (D)
GPA: 1.00
Status: Needs improvement.

Analysis complete! Reports saved to grade_report.txt
```

### Sample Implementation

```rust
use std::fs;
use std::io::Write;
use std::collections::HashMap;

# [derive(Debug, Clone)]
struct Student {
    id: u32,
    name: String,
    grades: HashMap<String, f64>,
    average: f64,
    letter_grade: String,
    gpa: f64,
}

impl Student {
    fn new(id: u32, name: String, grades: HashMap<String, f64>) -> Self {
        let average = Self::calculate_average(&grades);
        let letter_grade = Self::calculate_letter_grade(average);
        let gpa = Self::calculate_gpa(average);

        Student {
            id,
            name,
            grades,
            average,
            letter_grade,
            gpa,
        }
    }

    fn calculate_average(grades: &HashMap<String, f64>) -> f64 {
        let sum: f64 = grades.values().sum();
        sum / grades.len() as f64
    }

    fn calculate_letter_grade(average: f64) -> String {
        match average {
            90.0..=100.0 => "A",
            80.0..=89.9 => "B",
            70.0..=79.9 => "C",
            60.0..=69.9 => "D",
            _ => "F",
        }.to_string()
    }

    fn calculate_gpa(average: f64) -> f64 {
        match average {
            90.0..=100.0 => 4.0,
            80.0..=89.9 => 3.0,
            70.0..=79.9 => 2.0,
            60.0..=69.9 => 1.0,
            _ => 0.0,
        }
    }

    fn get_status(&self) -> String {
        match self.gpa {
            4.0 => "Excellent performance!",
            3.0 => "Good performance!",
            2.0 => "Satisfactory performance.",
            1.0 => "Needs improvement.",
            _ => "Academic probation required.",
        }.to_string()
    }
}

fn main() {
    println!("Student Grade Analyzer");
    println!("======================");
    println!();

    // Read student data from file
    let students = match read_student_data("students.txt") {
        Ok(students) => students,
        Err(e) => {
            println!("Error reading student data: {}", e);
            return;
        }
    };

    println!("Processing student data from file...\n");

    // Generate and display reports
    generate_class_summary(&students);
    println!();
    generate_individual_reports(&students);

    // Save detailed report to file
    if let Err(e) = save_report_to_file(&students) {
        println!("Warning: Could not save report to file: {}", e);
    } else {
        println!("\nAnalysis complete! Reports saved to grade_report.txt");
    }
}

fn read_student_data(filename: &str) -> Result<Vec<Student>, Box<dyn std::error::Error>> {
    let content = fs::read_to_string(filename)?;
    let mut students = Vec::new();

    for line in content.lines() {
        if line.trim().is_empty() || line.starts_with('#') {
            continue; // Skip empty lines and comments
        }

        let parts: Vec<&str> = line.split(',').map(|s| s.trim()).collect();
        if parts.len() < 3 {
            continue; // Skip malformed lines
        }

        let id: u32 = parts[0].parse()?;
        let name = parts[1].to_string();

        let mut grades = HashMap::new();
        for grade_part in &parts[2..] {
            let grade_parts: Vec<&str> = grade_part.split(':').map(|s| s.trim()).collect();
            if grade_parts.len() == 2 {
                let subject = grade_parts[0].to_string();
                let score: f64 = grade_parts[1].parse()?;
                grades.insert(subject, score);
            }
        }

        if !grades.is_empty() {
            students.push(Student::new(id, name, grades));
        }
    }

    Ok(students)
}

fn generate_class_summary(students: &[Student]) {
    println!(" CLASS SUMMARY REPORT");
    println!("======================");
    println!();

    println!("Total Students: {}", students.len());

    // Calculate class average GPA
    let total_gpa: f64 = students.iter().map(|s| s.gpa).sum();
    let class_avg_gpa = total_gpa / students.len() as f64;
    println!("Class Average GPA: {:.2}", class_avg_gpa);

    // Calculate grade distribution
    let mut grade_counts = HashMap::new();
    for student in students {
        *grade_counts.entry(student.letter_grade.clone()).or_insert(0) += 1;
    }

    println!("Grade Distribution:");
    let grades = ["A", "B", "C", "D", "F"];
    for grade in &grades {
        let count = grade_counts.get(*grade).unwrap_or(&0);
        let percentage = (*count as f64 / students.len() as f64) * 100.0;
        println!("  {}: {} students ({:.1}%)", grade, count, percentage);
    }

    // Find top and bottom performers
    if let Some(top_student) = students.iter().max_by(|a, b| a.gpa.partial_cmp(&b.gpa).unwrap()) {
        println!("Top Performer: {} ({:.2} GPA)", top_student.name, top_student.gpa);
    }

    if let Some(bottom_student) = students.iter().min_by(|a, b| a.gpa.partial_cmp(&b.gpa).unwrap()) {
        println!("Needs Improvement: {} ({:.2} GPA)", bottom_student.name, bottom_student.gpa);
    }
}

fn generate_individual_reports(students: &[Student]) {
    println!(" INDIVIDUAL STUDENT REPORTS");
    println!("==============================\n");

    for student in students {
        println!("Student: {}", student.name);
        println!("ID: {}", student.id);

        // Display grades
        print!("Grades: ");
        let grade_strings: Vec<String> = student.grades.iter()
            .map(|(subject, score)| format!("{}:{:.0}", subject, score))
            .collect();
        println!("{}", grade_strings.join(", "));

        println!("Average: {:.2}% ({})", student.average, student.letter_grade);
        println!("GPA: {:.2}", student.gpa);
        println!("Status: {}", student.get_status());
        println!();
    }
}

fn save_report_to_file(students: &[Student]) -> Result<(), Box<dyn std::error::Error>> {
    let mut file = fs::File::create("grade_report.txt")?;

    writeln!(file, "STUDENT GRADE ANALYSIS REPORT")?;
    writeln!(file, "Generated: {}", chrono::Utc::now().format("%Y-%m-%d %H:%M:%S"))?;
    writeln!(file, "================================\n")?;

    // Class summary
    writeln!(file, "CLASS SUMMARY")?;
    writeln!(file, "-------------")?;
    writeln!(file, "Total Students: {}", students.len())?;

    let total_gpa: f64 = students.iter().map(|s| s.gpa).sum();
    let class_avg_gpa = total_gpa / students.len() as f64;
    writeln!(file, "Class Average GPA: {:.2}", class_avg_gpa)?;

    // Individual reports
    writeln!(file, "\nINDIVIDUAL REPORTS")?;
    writeln!(file, "------------------")?;

    for student in students {
        writeln!(file, "\nStudent: {} (ID: {})", student.name, student.id)?;
        writeln!(file, "Average: {:.2}% ({})", student.average, student.letter_grade)?;
        writeln!(file, "GPA: {:.2}", student.gpa)?;
        writeln!(file, "Status: {}", student.get_status())?;
    }

    Ok(())
}
```

### Implementation Analysis

**Key Rust Concepts Used:**
- **File I/O**: `fs::read_to_string()` and `fs::File::create()`
- **Error handling**: `Result<T, E>` and `?` operator
- **Data structures**: `HashMap` for grades, `Vec` for students
- **Structs and impl**: Custom `Student` struct with methods
- **Pattern matching**: Grade calculation logic
- **Iterators**: Processing collections efficiently

**Program Structure:**
- **Data reading**: Parse CSV-like format from file
- **Student struct**: Encapsulate all student information
- **Calculation methods**: Modular grade computation
- **Report generation**: Both console and file output
- **Error recovery**: Skip malformed data gracefully

**Why this structure?**
- **Separation of concerns**: Different functions for different tasks
- **Error resilience**: Program continues despite bad data
- **Extensible design**: Easy to add new subjects or calculations
- **Comprehensive reporting**: Multiple output formats
- **Type safety**: Rust's type system prevents many errors

### Common Implementation Mistakes

| Common Issue | Why It Happens | Solution |
|--------------|----------------|----------|
| File not found errors | Wrong path or filename | Use relative paths, check file exists |
| Parse errors crashing program | Invalid data in file | Use `Result` and skip bad data |
| Memory inefficiency | Loading all data at once | Consider streaming for large files |
| Poor error messages | Generic error handling | Provide specific error context |
| Hard-coded subjects | Inflexible design | Use dynamic subject handling |

### Testing Your Program

**Test Data Format:**
```
1001,Alice Johnson,Math:95,Science:92,English:98,History:96
1002,Bob Smith,Math:87,Science:89,English:85,History:88
1003,Carol Davis,Math:78,Science:82,English:75,History:80
```

**Expected Calculations:**
- Alice: (95+92+98+96)/4 = 95.25% → A (4.0 GPA)
- Bob: (87+89+85+88)/4 = 87.25% → B (3.0 GPA)
- Carol: (78+82+75+80)/4 = 78.75% → C (2.0 GPA)

### README.md Template

```markdown
# Student Grade Analyzer

An automated Rust application that processes student grade data from files and generates comprehensive analysis reports.

## Features

- Automated batch processing of student data
- GPA calculation and letter grade assignment
- Class statistics and grade distribution analysis
- Individual student performance reports
- File-based input and output
- Error handling for malformed data

## Data Format

Create a `students.txt` file with the following format:
```
ID,Name,Subject1:Score,Subject2:Score,...
1001,Alice Johnson,Math:95,Science:92,English:98
```

## Usage

1. Create your student data file
2. Run the analyzer:
   ```bash
   rustc main.rs
   ./main
   ```
3. View reports on screen and in `grade_report.txt`
```

---

 **Outstanding! You built a complete automated data processing system!** 

*Next: Capstone Project (Library Management System)!*