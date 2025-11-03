use std::io::{self, Write};

fn main() {
    println!("Compound Interest Calculator");
    println!("============================");

    // Get principal amount
    let principal = get_positive_number("Enter principal amount: $");

    // Get annual interest rate
    let rate_percent = get_valid_rate("Enter annual interest rate (%): ");
    let rate = rate_percent / 100.0; // Convert to decimal

    // Get number of years
    let years = get_positive_integer("Enter number of years: ");

    // Get compounding frequency
    println!("Compounding frequency:");
    println!("1. Yearly");
    println!("2. Quarterly");
    println!("3. Monthly");
    let frequency_choice = get_valid_choice("Enter choice (1-3): ", 1, 3);

    // Set compounding frequency values
    let (n, frequency_name) = match frequency_choice {
        1 => (1.0, "Yearly"),
        2 => (4.0, "Quarterly"),
        3 => (12.0, "Monthly"),
        _ => (1.0, "Yearly"), // Default fallback
    };

    // Calculate compound interest
    let base = 1.0 + (rate / n);
    let exponent = n * years as f64;
    let final_amount = principal * base.powf(exponent);
    let total_interest = final_amount - principal;

    // Display results
    println!("\nInvestment Summary");
    println!("------------------");
    println!("Principal: ${:.2}", principal);
    println!("Interest Rate: {:.2}%", rate_percent);
    println!("Years: {}", years);
    println!("Compounding: {}", frequency_name);
    println!("Final Amount: ${:.2}", final_amount);
    println!("Total Interest: ${:.2}", total_interest);
}

fn get_positive_number(prompt: &str) -> f64 {
    loop {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        match input.trim().parse::<f64>() {
            Ok(num) if num > 0.0 => return num,
            Ok(_) => println!("Please enter a positive number."),
            Err(_) => println!("Please enter a valid number."),
        }
    }
}

fn get_valid_rate(prompt: &str) -> f64 {
    loop {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        match input.trim().parse::<f64>() {
            Ok(rate) if rate >= 0.0 && rate <= 100.0 => return rate,
            Ok(_) => println!("Rate must be between 0% and 100%."),
            Err(_) => println!("Please enter a valid number."),
        }
    }
}

fn get_positive_integer(prompt: &str) -> u32 {
    loop {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        match input.trim().parse::<u32>() {
            Ok(num) if num > 0 => return num,
            Ok(_) => println!("Please enter a positive number."),
            Err(_) => println!("Please enter a valid integer."),
        }
    }
}

fn get_valid_choice(prompt: &str, min: u32, max: u32) -> u32 {
    loop {
        print!("{}", prompt);
        io::stdout().flush().unwrap();

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        match input.trim().parse::<u32>() {
            Ok(choice) if choice >= min && choice <= max => return choice,
            Ok(_) => println!("Please enter a number between {} and {}.", min, max),
            Err(_) => println!("Please enter a valid number."),
        }
    }
}