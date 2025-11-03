use std::io::{self, Write};

fn main() {
    let mut balance = 1000.0;
    let mut running = true;

    println!("Welcome to Simple Bank System!");

    while running {
        // Display menu with current balance
        println!("\nSimple Bank System");
        println!("==================");
        println!("Current Balance: ${:.2}", balance);
        println!();
        println!("Choose an option:");
        println!("1. Check Balance");
        println!("2. Deposit Money");
        println!("3. Withdraw Money");
        println!("4. Exit");
        println!();
        print!("Enter your choice (1-4): ");
        io::stdout().flush().unwrap();

        let choice = get_valid_choice(1, 4);

        match choice {
            1 => {
                // Check balance
                println!("Your current balance is: ${:.2}", balance);
            }
            2 => {
                // Deposit
                print!("Enter deposit amount: $");
                io::stdout().flush().unwrap();
                let amount = get_positive_amount();

                balance += amount;
                println!("Deposit successful! New balance: ${:.2}", balance);
            }
            3 => {
                // Withdraw
                print!("Enter withdrawal amount: $");
                io::stdout().flush().unwrap();
                let amount = get_positive_amount();

                if amount <= balance {
                    balance -= amount;
                    println!("Withdrawal successful! New balance: ${:.2}", balance);
                } else {
                    println!("Insufficient funds. Your balance is ${:.2}", balance);
                }
            }
            4 => {
                // Exit
                running = false;
                println!("Thank you for using Simple Bank System!");
            }
            _ => {
                // This shouldn't happen due to validation, but just in case
                println!("Invalid choice. Please select 1-4.");
            }
        }
    }
}

fn get_valid_choice(min: u32, max: u32) -> u32 {
    loop {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        match input.trim().parse::<u32>() {
            Ok(choice) if choice >= min && choice <= max => return choice,
            Ok(_) => {
                print!("Please enter a number between {} and {}: ", min, max);
                io::stdout().flush().unwrap();
            }
            Err(_) => {
                print!("Please enter a valid number: ");
                io::stdout().flush().unwrap();
            }
        }
    }
}

fn get_positive_amount() -> f64 {
    loop {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();

        match input.trim().parse::<f64>() {
            Ok(amount) if amount > 0.0 => return amount,
            Ok(_) => {
                print!("Please enter a positive amount: $");
                io::stdout().flush().unwrap();
            }
            Err(_) => {
                print!("Please enter a valid number: $");
                io::stdout().flush().unwrap();
            }
        }
    }
}