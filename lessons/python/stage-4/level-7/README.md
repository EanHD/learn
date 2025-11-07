# Personal Finance Manager - Capstone Project

A comprehensive personal finance management application that combines interactive features, decision support, automated reporting, and data persistence. This capstone project demonstrates the integration of multiple programming concepts into a complete, real-world application.

## Features

- **Transaction Tracking**: Record income and expenses with categories and descriptions
- **Budget Management**: Set and monitor spending limits by category
- **Financial Reports**: Generate comprehensive spending reports and analytics
- **Budget Advisor**: AI-powered recommendations based on spending patterns
- **Budget Alerts**: Automatic notifications when approaching or exceeding limits
- **Data Persistence**: Save and load financial data between sessions
- **Interactive Interface**: User-friendly menu-driven application

## How to Run

```bash
python3 main.py
```

## Usage

1. **Add Transactions**: Record income and expenses with detailed categorization
2. **Monitor Budgets**: Set spending limits and receive alerts
3. **View Reports**: Generate financial summaries and spending analysis
4. **Get Advice**: Receive personalized budget recommendations
5. **Track Progress**: View recent transactions and spending patterns

## Example Workflow

```
1. Add Income: $3000 (Salary, Monthly paycheck)
2. Add Expense: $800 (Housing, Rent payment)
3. Add Expense: $300 (Food, Groceries)
4. Set Budget: Food, $400
5. View Balance: $1900 remaining
6. Generate Report: See spending breakdown
7. Get Budget Advice: Receive personalized recommendations
```

## Data Storage

Financial data is automatically saved to `finance_data.json`:
```json
{
  "transactions": [
    {
      "amount": 3000.0,
      "category": "Salary",
      "description": "Monthly paycheck",
      "date": "2024-01-15"
    }
  ],
  "budgets": {
    "Food": 400.0,
    "Housing": 1000.0
  }
}
```

## Learning Concepts

This capstone project demonstrates:
- Integration of multiple programming paradigms (OOP, procedural, functional)
- Complex data structures and algorithms
- File I/O and data persistence
- User interface design and input validation
- Business logic implementation
- Error handling and exception management
- Modular code organization
- Real-world application development

## Application Architecture

- **Data Layer**: Transaction and budget data management
- **Business Logic**: Financial calculations and budget analysis
- **Presentation Layer**: Interactive menu system
- **Persistence Layer**: JSON-based data storage
- **Analytics Layer**: Reporting and recommendation engine