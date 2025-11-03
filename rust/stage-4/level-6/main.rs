use std::fs;
use std::io::Write;
use std::collections::HashMap;

#[derive(Debug, Clone)]
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
            println!("Make sure 'students.txt' exists in the current directory.");
            return;
        }
    };

    if students.is_empty() {
        println!("No valid student data found in file.");
        return;
    }

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
    let mut line_number = 0;

    for line in content.lines() {
        line_number += 1;

        // Skip empty lines and comments
        if line.trim().is_empty() || line.starts_with('#') {
            continue;
        }

        let parts: Vec<&str> = line.split(',').map(|s| s.trim()).collect();
        if parts.len() < 3 {
            eprintln!("Warning: Skipping malformed line {}: insufficient data", line_number);
            continue;
        }

        // Parse student ID
        let id: u32 = match parts[0].parse() {
            Ok(id) => id,
            Err(_) => {
                eprintln!("Warning: Skipping line {}: invalid student ID '{}'", line_number, parts[0]);
                continue;
            }
        };

        let name = parts[1].to_string();

        // Parse grades
        let mut grades = HashMap::new();
        let mut valid_grades = 0;

        for grade_part in &parts[2..] {
            let grade_parts: Vec<&str> = grade_part.split(':').map(|s| s.trim()).collect();
            if grade_parts.len() == 2 {
                let subject = grade_parts[0].to_string();
                match grade_parts[1].parse::<f64>() {
                    Ok(score) => {
                        if score >= 0.0 && score <= 100.0 {
                            grades.insert(subject, score);
                            valid_grades += 1;
                        } else {
                            eprintln!("Warning: Skipping invalid score {} for {} (must be 0-100)", score, subject);
                        }
                    }
                    Err(_) => {
                        eprintln!("Warning: Skipping invalid score '{}' for {}", grade_parts[1], subject);
                    }
                }
            } else {
                eprintln!("Warning: Skipping malformed grade data: '{}'", grade_part);
            }
        }

        if valid_grades > 0 {
            students.push(Student::new(id, name, grades));
        } else {
            eprintln!("Warning: Skipping student {}: no valid grades found", name);
        }
    }

    Ok(students)
}

fn generate_class_summary(students: &[Student]) {
    println!("📊 CLASS SUMMARY REPORT");
    println!("======================");
    println!();

    println!("Total Students: {}", students.len());

    if students.is_empty() {
        return;
    }

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
        let percentage = if students.len() > 0 {
            (*count as f64 / students.len() as f64) * 100.0
        } else {
            0.0
        };
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
    println!("📋 INDIVIDUAL STUDENT REPORTS");
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

    // Get current date/time (simplified version)
    let now = std::time::SystemTime::now();
    let datetime = format!("{:?}", now); // Simplified timestamp

    writeln!(file, "STUDENT GRADE ANALYSIS REPORT")?;
    writeln!(file, "Generated: {}", datetime)?;
    writeln!(file, "================================\n")?;

    // Class summary
    writeln!(file, "CLASS SUMMARY")?;
    writeln!(file, "-------------")?;
    writeln!(file, "Total Students: {}", students.len())?;

    if !students.is_empty() {
        let total_gpa: f64 = students.iter().map(|s| s.gpa).sum();
        let class_avg_gpa = total_gpa / students.len() as f64;
        writeln!(file, "Class Average GPA: {:.2}", class_avg_gpa)?;
    }

    // Grade distribution
    let mut grade_counts = HashMap::new();
    for student in students {
        *grade_counts.entry(student.letter_grade.clone()).or_insert(0) += 1;
    }

    writeln!(file, "\nGrade Distribution:")?;
    let grades = ["A", "B", "C", "D", "F"];
    for grade in &grades {
        let count = grade_counts.get(*grade).unwrap_or(&0);
        let percentage = if students.len() > 0 {
            (*count as f64 / students.len() as f64) * 100.0
        } else {
            0.0
        };
        writeln!(file, "  {}: {} students ({:.1}%)", grade, count, percentage)?;
    }

    // Individual reports
    writeln!(file, "\nINDIVIDUAL REPORTS")?;
    writeln!(file, "------------------")?;

    for student in students {
        writeln!(file, "\nStudent: {} (ID: {})", student.name, student.id)?;

        // Write grades
        write!(file, "Grades: ")?;
        let grade_strings: Vec<String> = student.grades.iter()
            .map(|(subject, score)| format!("{}:{:.0}", subject, score))
            .collect();
        writeln!(file, "{}", grade_strings.join(", "))?;

        writeln!(file, "Average: {:.2}% ({})", student.average, student.letter_grade)?;
        writeln!(file, "GPA: {:.2}", student.gpa)?;
        writeln!(file, "Status: {}", student.get_status())?;
    }

    Ok(())
}