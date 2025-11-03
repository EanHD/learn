use std::io::{self, Write};

fn main() {
    println!("Temperature Converter");
    println!("=====================");
    println!("What conversion do you want?");
    println!("1. Celsius to Fahrenheit");
    println!("2. Fahrenheit to Celsius");
    print!("Enter choice (1 or 2): ");

    // Flush stdout to ensure prompt appears
    io::stdout().flush().unwrap();

    let mut choice = String::new();
    io::stdin().read_line(&mut choice).unwrap();
    let choice: u32 = match choice.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Invalid choice. Please enter 1 or 2.");
            return;
        }
    };

    if choice == 1 {
        // Celsius to Fahrenheit
        print!("Enter temperature in Celsius: ");
        io::stdout().flush().unwrap();

        let mut celsius = String::new();
        io::stdin().read_line(&mut celsius).unwrap();
        let celsius: f64 = match celsius.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Invalid temperature. Please enter a number.");
                return;
            }
        };

        let fahrenheit = (celsius * 9.0 / 5.0) + 32.0;
        println!("{:.1}°C is equal to {:.1}°F", celsius, fahrenheit);

    } else if choice == 2 {
        // Fahrenheit to Celsius
        print!("Enter temperature in Fahrenheit: ");
        io::stdout().flush().unwrap();

        let mut fahrenheit = String::new();
        io::stdin().read_line(&mut fahrenheit).unwrap();
        let fahrenheit: f64 = match fahrenheit.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Invalid temperature. Please enter a number.");
                return;
            }
        };

        let celsius = (fahrenheit - 32.0) * 5.0 / 9.0;
        println!("{:.1}°F is equal to {:.1}°C", fahrenheit, celsius);

    } else {
        println!("Invalid choice. Please enter 1 or 2.");
    }
}