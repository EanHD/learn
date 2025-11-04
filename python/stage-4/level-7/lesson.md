# Level 7: Capstone Project - Personal Finance Manager

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Learning Objectives

By completing this level, you will:

- Integrate multiple programming concepts into a comprehensive application
- Design and implement complex data models with relationships
- Create persistent data storage and retrieval systems
- Build interactive applications with multiple features
- Implement business logic for real-world problem solving
- Practice modular design and code organization
- Develop user-friendly interfaces for complex applications

## Code Analysis

### Application Architecture

The Personal Finance Manager demonstrates full-stack application development:

1. **Data Model**: Transaction and budget classes with serialization
2. **Business Logic**: Financial calculations, budgeting, and analytics
3. **User Interface**: Interactive menu system with input validation
4. **Data Persistence**: JSON-based storage with error handling
5. **Reporting System**: Automated report generation and insights

### Key Components

**Data Structures:**
- **Transaction Class**: Encapsulates financial transaction data
- **FinanceManager Class**: Core business logic and data management
- **Dictionary-based Budgets**: Simple key-value storage for budget limits

**Core Features Integration:**
- **CRUD Operations**: Create, read, update transactions and budgets
- **Data Analysis**: Category totals, balance calculations, spending trends
- **Decision Support**: Budget recommendations based on spending patterns
- **Automated Processing**: Report generation and budget alert checking

**Data Flow:**
```python
User Input → Validation → Business Logic → Data Storage → UI Feedback
```python

### Advanced Concepts

**Object-Oriented Design:**
- Classes for data encapsulation (Transaction)
- Manager class for business operations (FinanceManager)
- Separation of concerns between data and logic

**Data Persistence:**
- JSON serialization for cross-session data storage
- Error handling for file operations
- Data integrity and recovery

**Complex Algorithms:**
- Budget analysis and recommendation engine
- Statistical calculations for spending patterns
- Date-based filtering and aggregation

## Success Checklist

- [ ] Application maintains financial data between sessions
- [ ] Users can add income and expense transactions
- [ ] Budgets can be set and monitored by category
- [ ] Financial reports show accurate calculations
- [ ] Budget advisor provides meaningful recommendations
- [ ] Alert system notifies users of budget issues
- [ ] Menu navigation is intuitive and error-free
- [ ] Data validation prevents invalid inputs
- [ ] Application handles edge cases gracefully
- [ ] Code is well-organized into logical modules

## Key Concepts Demonstrated

- [ ] **Full Application Development**: Complete software solution with multiple features
- [ ] **Data Modeling**: Complex data structures and relationships
- [ ] **Business Logic**: Real-world financial calculations and rules
- [ ] **User Experience**: Intuitive interface design and feedback
- [ ] **Data Persistence**: Long-term data storage and retrieval
- [ ] **Error Handling**: Robust exception management throughout
- [ ] **Modular Architecture**: Separation of concerns and reusable components
- [ ] **Integration**: Combining multiple programming paradigms effectively

## Capstone Project Achievements

This project successfully combines:

- [ ] **Object-Oriented Programming** (classes, encapsulation, inheritance)
- [ ] **Data Structures** (lists, dictionaries, custom objects)
- [ ] **File I/O** (JSON serialization, error handling)
- [ ] **User Interfaces** (menu systems, input validation)
- [ ] **Algorithms** (financial calculations, recommendations)
- [ ] **Error Handling** (try-except, validation, recovery)
- [ ] **Modular Design** (separation of concerns, reusable functions)

## Potential Enhancements

- [ ] Add data visualization with charts
- [ ] Implement recurring transaction scheduling
- [ ] Add financial goal tracking
- [ ] Create import/export functionality
- [ ] Add user authentication and multiple accounts
- [ ] Implement cloud backup and sync
- [ ] Add mobile-responsive web interface
- [ ] Integrate with financial APIs for real data

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

> **NEEDS_AUTHOR:** This lesson needs a complete answer key with code breakdown, execution process explanation, common errors table, and bonus knowledge section. Reference c-c++/stage-1/level-1/lesson.md for the gold standard format.

### Key Concepts

- Review the code structure specific to Python
- Understand the execution flow
- Learn common pitfalls and solutions

### Next Steps

Practice the code and experiment with variations!

---

**Congratulations! Keep coding!**


### Learning Goals

- Understand core concepts
- Practice implementation


### Your Task

1. Review the code structure
2. Implement the required functionality
3. Test your solution


### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic


<div style="page-break-after: always;"></div>

## Answer Key

### Complete Solution

```py
#!/usr/bin/env python3
"""
Personal Finance Manager - Capstone Project
A comprehensive personal finance management application combining multiple features.
"""

import json
import os
from datetime import datetime, timedelta
from collections import defaultdict
import statistics

class Transaction:
    def __init__(self, amount, category, description, date=None):
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = date or datetime.now().strftime('%Y-%m-%d')

    def to_dict(self):
        return {
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['amount'], data['category'], data['description'], data['date'])

class FinanceManager:
    def __init__(self, data_file='finance_data.json'):
        self.data_file = data_file
        self.transactions = []
        self.budgets = {}
        self.load_data()

    def load_data(self):
        """Load transactions and budgets from file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.transactions = [Transaction.from_dict(t) for t in data.get('transactions', [])]
                    self.budgets = data.get('budgets', {})
            except Exception as e:
                print(f"Error loading data: {e}")

    def save_data(self):
        """Save transactions and budgets to file."""
        data = {
            'transactions': [t.to_dict() for t in self.transactions],
            'budgets': self.budgets
        }
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_transaction(self, amount, category, description):
        """Add a new transaction."""
        transaction = Transaction(amount, category, description)
        self.transactions.append(transaction)
        self.save_data()
        print(f"Transaction added: {description} - ${amount:.2f}")

    def get_balance(self):
        """Calculate current balance."""
        return sum(t.amount for t in self.transactions)

    def get_category_totals(self, days=30):
        """Get spending totals by category for the last N days."""
        cutoff_date = datetime.now() - timedelta(days=days)
        cutoff_str = cutoff_date.strftime('%Y-%m-%d')

        totals = defaultdict(float)
        for transaction in self.transactions:
            if transaction.date >= cutoff_str and transaction.amount < 0:
                totals[transaction.category] += abs(transaction.amount)

        return dict(totals)

    def get_budget_advice(self):
        """Provide personalized budget recommendations."""
        monthly_spending = self.get_category_totals(30)
        total_spending = sum(monthly_spending.values())

        if total_spending == 0:
            return "No spending data available. Start tracking expenses to get budget advice."

        # Calculate recommended budget allocations
        recommendations = {
            'Housing': total_spending * 0.30,
            'Food': total_spending * 0.15,
            'Transportation': total_spending * 0.15,
            'Entertainment': total_spending * 0.10,
            'Savings': total_spending * 0.20,
            'Miscellaneous': total_spending * 0.10
        }

        advice = "Based on your spending patterns, here's a recommended monthly budget:\n\n"

        for category, recommended in recommendations.items():
            actual = monthly_spending.get(category, 0)
            status = "✓" if actual <= recommended else "⚠"
            advice += f"{category}: ${recommended:.2f} (spent: ${actual:.2f}) {status}\n"

        return advice

    def generate_report(self):
        """Generate a comprehensive financial report."""
        balance = self.get_balance()
        monthly_spending = self.get_category_totals(30)

        report = f"""
FINANCIAL REPORT - {datetime.now().strftime('%B %Y')}

CURRENT BALANCE: ${balance:.2f}

MONTHLY SPENDING BY CATEGORY:
"""

        for category, amount in sorted(monthly_spending.items(), key=lambda x: x[1], reverse=True):
            report += f"  {category}: ${amount:.2f}\n"

        total_spending = sum(monthly_spending.values())
        report += f"\nTOTAL MONTHLY SPENDING: ${total_spending:.2f}"

        if monthly_spending:
            avg_transaction = statistics.mean(abs(t.amount) for t in self.transactions if t.amount < 0)
            report += f"\nAVERAGE TRANSACTION: ${avg_transaction:.2f}"

        return report.strip()

    def set_budget(self, category, amount):
        """Set a budget for a category."""
        self.budgets[category] = float(amount)
        self.save_data()
        print(f"Budget set for {category}: ${amount:.2f}")

    def check_budget_alerts(self):
        """Check for budget alerts."""
        alerts = []
        monthly_spending = self.get_category_totals(30)

        for category, budget in self.budgets.items():
            spent = monthly_spending.get(category, 0)
            if spent > budget:
                alerts.append(f"⚠ OVER BUDGET: {category} (${spent:.2f} / ${budget:.2f})")
            elif spent > budget * 0.8:
                alerts.append(f"⚡ NEARING LIMIT: {category} (${spent:.2f} / ${budget:.2f})")

        return alerts

def display_menu():
    """Display the main menu."""
    print("\n" + "="*55)
    print("         PERSONAL FINANCE MANAGER")
    print("="*55)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Spending by Category")
    print("5. Set Budget")
    print("6. Get Budget Advice")
    print("7. Generate Report")
    print("8. View Recent Transactions")
    print("9. Check Budget Alerts")
    print("10. Exit")
    print("="*55)

def get_user_choice():
    """Get validated menu choice."""
    while True:
        try:
            choice = int(input("Enter your choice (1-10): "))
            if 1 <= choice <= 10:
                return choice
            print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")

def add_transaction_menu(manager, is_income=True):
    """Menu for adding transactions."""
    transaction_type = "income" if is_income else "expense"

    try:
        amount = float(input(f"Enter {transaction_type} amount: $"))
        if not is_income:
            amount = -abs(amount)  # Ensure expenses are negative

        category = input(f"Enter category for this {transaction_type}: ").strip()
        description = input("Enter description: ").strip()

        if category and description:
            manager.add_transaction(amount, category, description)
        else:
            print("Category and description cannot be empty.")
    except ValueError:
        print("Please enter a valid amount.")

def main():
    """Main application loop."""
    manager = FinanceManager()

    print("Welcome to Personal Finance Manager!")
    print("Take control of your finances with comprehensive tracking and insights.")

    while True:
        # Check for budget alerts
        alerts = manager.check_budget_alerts()
        if alerts:
            print("\nBUDGET ALERTS:")
            for alert in alerts:
                print(f"  {alert}")

        display_menu()
        choice = get_user_choice()

        if choice == 1:  # Add Income
            add_transaction_menu(manager, is_income=True)

        elif choice == 2:  # Add Expense
            add_transaction_menu(manager, is_income=False)

        elif choice == 3:  # View Balance
            balance = manager.get_balance()
            print(f"\nCurrent Balance: ${balance:.2f}")

        elif choice == 4:  # View Spending by Category
            spending = manager.get_category_totals(30)
            if spending:
                print("\nMonthly Spending by Category:")
                for category, amount in sorted(spending.items(), key=lambda x: x[1], reverse=True):
                    print(f"  {category}: ${amount:.2f}")
            else:
                print("No spending data available.")

        elif choice == 5:  # Set Budget
            category = input("Enter category: ").strip()
            try:
                amount = float(input("Enter budget amount: $"))
                manager.set_budget(category, amount)
            except ValueError:
                print("Please enter a valid amount.")

        elif choice == 6:  # Get Budget Advice
            advice = manager.get_budget_advice()
            print(f"\n{advice}")

        elif choice == 7:  # Generate Report
            report = manager.generate_report()
            print(f"\n{report}")

        elif choice == 8:  # View Recent Transactions
            if manager.transactions:
                print("\nRecent Transactions (last 10):")
                for transaction in manager.transactions[-10:]:
                    print(f"  {transaction.date}: {transaction.description} - ${transaction.amount:.2f} ({transaction.category})")
            else:
                print("No transactions recorded yet.")

        elif choice == 9:  # Check Budget Alerts
            alerts = manager.check_budget_alerts()
            if alerts:
                print("\nCurrent Budget Alerts:")
                for alert in alerts:
                    print(f"  {alert}")
            else:
                print("No budget alerts at this time.")

        elif choice == 10:  # Exit
            print("Thank you for using Personal Finance Manager. Goodbye!")
            break

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard python conventions with proper imports and main function
2. **Variables**: Data types are correctly declared and initialized
3. **Logic**: The program implements the required functionality
4. **Output**: Results are displayed clearly to the user
5. **Best Practices**: Code is readable and follows naming conventions

### Testing Your Solution

Try these test cases to verify your code works correctly:

1. **Basic Test**: Run the program with standard inputs
2. **Edge Cases**: Test with boundary values (0, -1, very large numbers)
3. **Error Handling**: Verify the program handles invalid inputs gracefully

### Tips for Understanding

- Review each section carefully
- Try modifying values to see how output changes
- Add your own printf/print statements to trace execution
- Experiment with different inputs
