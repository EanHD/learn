# Level 4: Interactive Application
## Stage 4: Full Problem Solving

### Today's Mission

Now you'll implement an interactive application that manages ongoing user interactions and maintains program state across multiple operations.

---

### Learning Goals

- Implement interactive menu-driven applications
- Manage program state across multiple user interactions
- Create robust input validation and error handling
- Design intuitive user interfaces with clear feedback
- Use loops for repeated user interactions

---

### Your Task

**Implement the Simple Banking System program in Rust. Create the following files:**

1. **`main.rs`** - The main program file
2. **`README.md`** - Instructions for running the program

### Program Requirements

Based on your Stage 3 pseudocode, implement a simple banking system that:

1. **Starts with initial balance** of $1000
2. **Displays interactive menu** with current balance
3. **Handles multiple operations**:
   - Check balance
   - Deposit money (with validation)
   - Withdraw money (with balance and amount validation)
   - Exit program
4. **Uses a main loop** that continues until user chooses to exit
5. **Provides clear feedback** for all transactions
6. **Maintains state** across multiple operations

**Menu Structure:**
```
Simple Bank System
==================
Current Balance: $1000.00

Choose an option:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice (1-4):
```

---

### Implementation Steps

1. **Create the project structure**:
   ```bash
   cd /home/eanhd/LEARN/rust/stage-4-full-problem-solving/level-4-interactive-application
   ```

2. **Create `main.rs`** with your Rust implementation

3. **Test your program**:
   ```bash
   rustc main.rs
   ./main
   ```

4. **Create `README.md`** with usage instructions

---

### Success Checklist

- [ ] Created `main.rs` file
- [ ] Program starts with $1000 balance
- [ ] Interactive menu displays current balance
- [ ] All 4 menu options work correctly
- [ ] Input validation for deposits and withdrawals
- [ ] Balance updates correctly after transactions
- [ ] Program exits cleanly when requested

---

### What You'll Learn

Interactive applications involve:
- **State management** - Tracking data across operations
- **Loop control** - Managing program flow with user input
- **Input validation** - Ensuring data integrity
- **User experience** - Clear interfaces and feedback

---

### Implementation Tips

1. **Use a main loop** with exit condition
2. **Store balance** in a mutable variable
3. **Validate all inputs** before processing
4. **Provide clear feedback** for all operations
5. **Handle edge cases** like insufficient funds

---

## Need Help with Rust?

- **Main loop**: Use `loop` with `break` condition
- **Mutable variables**: Use `let mut balance = 1000.0`
- **Menu display**: Print menu in each loop iteration
- **Input handling**: Validate choices and amounts

---

<div style="page-break-after: always;"></div>

---

## SOLUTION GUIDE (No cheating until you've tried!)

### Expected Program Behavior

```
Simple Bank System
==================
Current Balance: $1000.00

Choose an option:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice (1-4): 2
Enter deposit amount: $500

Deposit successful! New balance: $1500.00

Choose an option:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice (1-4): 4

Thank you for using Simple Bank System!
```

### Sample Implementation

```rust
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
```

### Implementation Analysis

**Key Rust Concepts Used:**
- **Mutable variables**: `let mut balance = 1000.0` for changing balance
- **Main loop**: `while running` with exit condition
- **Pattern matching**: `match choice` for menu handling
- **Functions**: Helper functions for input validation
- **Loop validation**: Input checking with retry loops
- **Formatted output**: Currency formatting with `{:.2}`

**Program Structure:**
- **State management**: Balance persists across menu interactions
- **Menu-driven interface**: Clear options displayed each time
- **Input validation**: Comprehensive checking for all inputs
- **Transaction processing**: Different logic for each operation
- **Clean exit**: Proper termination with farewell message

**Why this structure?**
- **Interactive design**: Menu loop allows multiple operations
- **State persistence**: Balance maintained throughout session
- **Error handling**: Validation prevents invalid operations
- **User-friendly**: Clear feedback and error messages

### Common Implementation Mistakes

| Common Issue | Why It Happens | Solution |
|--------------|----------------|----------|
| Balance not mutable | Can't update balance | Use `let mut balance` |
| No loop exit | Program runs forever | Include `running = false` in exit case |
| Wrong validation | Invalid transactions allowed | Check conditions before balance changes |
| Poor menu display | Menu not shown each time | Display menu inside the loop |
| No input flushing | Prompts don't appear | Use `io::stdout().flush().unwrap()` |

### Testing Your Program

**Test Scenarios to Try:**
1. **Check balance**: Should show current balance
2. **Valid deposit**: Add money, balance should increase
3. **Valid withdrawal**: Remove money, balance should decrease
4. **Invalid withdrawal**: Try withdrawing more than balance
5. **Invalid deposit**: Try depositing negative or zero amount
6. **Invalid menu choice**: Enter number outside 1-4 range
7. **Multiple transactions**: Do several operations in sequence

### README.md Template

```markdown
# Simple Banking System

A Rust program that simulates basic banking operations with an interactive menu system.

## How to Run

1. Compile the program:
   ```bash
   rustc main.rs
   ```

2. Run the program:
   ```bash
   ./main
   ```

3. Use the menu to perform banking operations.

## Features

- Interactive menu-driven interface
- Balance checking, deposits, and withdrawals
- Input validation for all operations
- Real-time balance updates
- Clean exit functionality

## Example Usage

```
Simple Bank System
==================
Current Balance: $1000.00

Choose an option:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice (1-4): 2
Enter deposit amount: $500

Deposit successful! New balance: $1500.00
```
```

### Bonus Challenges

1. **Transaction history** - Track and display all transactions
2. **Multiple accounts** - Support multiple user accounts
3. **Transaction fees** - Add fees for certain operations
4. **Daily limits** - Implement withdrawal limits

---

 **Fantastic! You built an interactive banking application!** 

*Next: Decision Support Application (Travel Recommendation System)!*