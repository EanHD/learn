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

## Menu Options

1. **Check Balance** - Display current account balance
2. **Deposit Money** - Add money to account (must be positive amount)
3. **Withdraw Money** - Remove money from account (must not exceed balance)
4. **Exit** - End the banking session

## Validation Rules

- Deposit amounts must be positive
- Withdrawal amounts must be positive and not exceed current balance
- Menu choices must be between 1-4
- All monetary inputs must be valid numbers

## Starting Balance

The program begins with an initial balance of $1000.00.