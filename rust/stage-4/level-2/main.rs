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
    println!("Assignment 1: {:.0}/100 (30%)", score1);
    println!("Assignment 2: {:.0}/100 (35%)", score2);
    println!("Assignment 3: {:.0}/100 (35%)", score3);
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