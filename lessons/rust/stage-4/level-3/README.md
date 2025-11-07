# Compound Interest Calculator

A Rust program that calculates compound interest for savings and investments.

## How to Run

1. Compile the program:
   ```bash
   rustc main.rs
   ```

2. Run the program:
   ```bash
   ./main
   ```

3. Enter investment details as prompted.

## Features

- Calculates compound interest with different compounding frequencies
- Input validation for all parameters
- Professional financial report formatting
- Support for yearly, quarterly, and monthly compounding

## Example Usage

```
Compound Interest Calculator
============================
Enter principal amount: $1000
Enter annual interest rate (%): 5
Enter number of years: 3
Compounding frequency:
1. Yearly
2. Quarterly
3. Monthly
Enter choice (1-3): 2

Investment Summary
------------------
Principal: $1000.00
Interest Rate: 5.00%
Years: 3
Compounding: Quarterly
Final Amount: $1161.54
Total Interest: $161.54
```

## Formula Used

The compound interest formula is:
```
A = P(1 + r/n)^(nt)
```

Where:
- A = Final amount
- P = Principal amount
- r = Annual interest rate (as decimal)
- n = Number of times interest is compounded per year
- t = Number of years

## Test Cases

Try these calculations to verify accuracy:
- $1000 at 5% for 1 year (yearly): $1050.00
- $1000 at 5% for 1 year (quarterly): $1050.95
- $1000 at 5% for 3 years (yearly): $1157.63