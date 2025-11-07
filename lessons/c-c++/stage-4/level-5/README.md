# Personal Finance Advisor

A comprehensive C application providing decision support for personal financial management, featuring transaction tracking, budget analysis, savings goals, investment management, and personalized financial advice.

## Features

- **Transaction Management**: Track income and expenses with categorization and search capabilities
- **Budget Analysis**: Monitor spending against budgeted amounts with detailed category breakdowns
- **Savings Goals**: Set and track progress toward financial goals with target dates
- **Investment Portfolio**: Manage investments with performance tracking and risk assessment
- **Financial Reporting**: Generate comprehensive financial reports and summaries
- **Decision Support**: Receive personalized financial advice based on your financial profile
- **Data Persistence**: Save and load financial data to/from files

## Quick Start

1. **Compile the program**:
   ```bash
   gcc main.c -o finance_advisor -lm
   ```

2. **Run the application**:
   ```bash
   ./finance_advisor
   ```

3. **Navigate using the main menu** to manage your finances and get advice

## Menu Structure

### Main Menu
- **1.  Manage Transactions** - Add/view/search income and expense transactions
- **2.  View Budget Analysis** - Analyze spending vs. budgeted amounts
- **3.  Manage Budget Categories** - Create and modify budget categories
- **4.  Manage Savings Goals** - Set and track savings objectives
- **5.  Manage Investments** - Track investment portfolio performance
- **6.  Generate Financial Report** - Create comprehensive financial summaries
- **7.  Get Financial Advice** - Receive personalized financial recommendations
- **8.  Save Financial Data** - Save all financial data to file
- **9.  Load Financial Data** - Load previously saved financial data
- **0.  Exit** - Exit the application

## Transaction Management

### Add Income/Expense
- **Date Entry**: YYYY-MM-DD format for transaction dates
- **Description**: Detailed transaction descriptions
- **Category**: Categorize transactions (Food, Housing, Transportation, etc.)
- **Amount**: Precise monetary amounts
- **Type**: Automatic classification as income or expense

### Transaction Search
- **By Category**: Find transactions in specific spending categories
- **By Date Range**: Filter transactions within date ranges
- **By Amount Range**: Search transactions within monetary ranges

### Transaction History
- **Complete Records**: View all transactions with full details
- **Organized Display**: Clear formatting with dates, descriptions, and amounts

## Budget Analysis

### Category Tracking
- **Budgeted Amounts**: Set spending limits for each category
- **Actual Spending**: Track real expenses against budgets
- **Remaining Amounts**: Calculate budget surpluses or deficits
- **Over-Budget Alerts**: Warnings for categories exceeding limits

### Budget Performance
- **Usage Percentages**: See what percentage of budget is used
- **Total Summary**: Overall budget status across all categories
- **Visual Indicators**: Clear warnings for budget overruns

## Budget Category Management

### Category Operations
- **Add Categories**: Create new budget categories with spending limits
- **Edit Categories**: Modify budgeted amounts for existing categories
- **Delete Categories**: Remove unused budget categories
- **View All**: Comprehensive list of all budget categories

### Category Details
- **Budgeted Amount**: Planned spending limit
- **Spent Amount**: Actual expenses in category
- **Remaining Amount**: Difference between budget and spending

## Savings Goals Management

### Goal Setting
- **Goal Names**: Descriptive names for savings objectives
- **Target Amounts**: Specific monetary targets
- **Current Progress**: Track current savings toward goals
- **Target Dates**: Deadline for achieving goals
- **Monthly Contributions**: Regular savings amounts

### Progress Tracking
- **Progress Percentages**: Visual progress indicators
- **Remaining Amounts**: How much more needed to reach goals
- **Achievement Status**: Clear indicators when goals are met
- **Monthly Planning**: Automated progress updates

## Investment Management

### Portfolio Tracking
- **Investment Types**: Stocks, bonds, mutual funds, real estate, savings
- **Initial Investment**: Original amounts invested
- **Current Values**: Real-time portfolio valuations
- **Performance Tracking**: Gains/losses and percentage returns

### Risk Assessment
- **Risk Levels**: Low, medium, high risk classifications
- **Expected Returns**: Anticipated annual percentage returns
- **Diversification**: Portfolio balance recommendations

### Market Simulation
- **Value Updates**: Simulated market fluctuations
- **Performance Analysis**: Portfolio-wide performance metrics
- **Rebalancing Alerts**: Recommendations for portfolio adjustments

## Financial Reporting

### Income & Expense Summary
- **Total Income**: Sum of all income transactions
- **Total Expenses**: Sum of all expense transactions
- **Net Income**: Income minus expenses
- **Savings Rate**: Percentage of income saved

### Budget Performance Report
- **Category Breakdown**: Spending vs. budget for each category
- **Usage Percentages**: How much of each budget is utilized
- **Overall Status**: Total budget performance summary

### Savings Goals Report
- **Goal Progress**: Current status of each savings goal
- **Completion Status**: Goals achieved vs. remaining
- **Timeline Analysis**: Progress toward target dates

### Investment Report
- **Portfolio Value**: Total current portfolio value
- **Total Returns**: Overall portfolio performance
- **Asset Allocation**: Breakdown by investment type

### Financial Health Metrics
- **Monthly Income**: Average monthly income
- **Monthly Expenses**: Average monthly spending
- **Debt-to-Income Ratio**: Debt burden assessment
- **Emergency Fund**: Months of expenses covered

## Financial Advice System

### Personalized Recommendations
- **Savings Rate Analysis**: Advice based on current savings percentage
- **Budget Compliance**: Recommendations for budget management
- **Goal Achievement**: Strategies for reaching savings goals
- **Investment Guidance**: Portfolio diversification advice

### Risk Assessments
- **Emergency Fund**: Recommendations for emergency savings
- **Debt Management**: Strategies for debt reduction
- **Investment Risk**: Risk tolerance and diversification advice

### Actionable Insights
- **Spending Patterns**: Analysis of expense categories
- **Savings Strategies**: Methods to increase savings rate
- **Investment Planning**: Long-term investment recommendations

## Data Persistence

### Save Functionality
- **Complete Data Export**: Save all financial data to text files
- **Structured Format**: Organized data storage with clear sections
- **Backup Capability**: Create multiple save files for different scenarios

### Load Functionality
- **Data Restoration**: Load previously saved financial data
- **State Recovery**: Restore complete application state
- **Data Validation**: Ensure data integrity during loading

## Technical Details

### Data Structures
- **Transaction Structure**: Date, description, category, amount, type
- **BudgetCategory Structure**: Name, budgeted, spent, remaining amounts
- **SavingsGoal Structure**: Name, target, current, date, monthly contribution
- **Investment Structure**: Name, type, initial/current value, return, risk
- **FinancialProfile Structure**: Income, expenses, ratios, fund coverage

### Memory Management
- **Fixed-size Arrays**: Pre-allocated storage for financial data
- **Bounds Checking**: Prevent array overflow and invalid access
- **Data Validation**: Input verification and error handling

### File Operations
- **Text File Format**: Human-readable data storage
- **Sectioned Storage**: Organized data sections for different data types
- **Error Handling**: Robust file operation error management

## Usage Examples

### Adding Transactions
```
 TRANSACTION MANAGEMENT
==========================

Transaction Options:
1. Add Income
2. Add Expense
3. View All Transactions
4. Search Transactions
5. Back to Main Menu
Enter choice (1-5): 2

Add Expense Transaction:
Date (YYYY-MM-DD): 2024-01-15
Description: Grocery shopping
Category: Food
Amount: $125.50

 Expense transaction added successfully!
```

### Budget Analysis
```
 BUDGET ANALYSIS
==================

Budget Category Analysis:
=========================
Food:
  Budgeted: $600.00
  Spent: $275.50
  Remaining: $324.50

Housing:
  Budgeted: $1200.00
  Spent: $1200.00
  Remaining: $0.00

Summary:
========
Total Budgeted: $1800.00
Total Spent: $1475.50
Total Remaining: $324.50
Budget Used: 82.0%
 Budget is under control.
```

### Savings Goals
```
 SAVINGS GOALS MANAGEMENT
============================

Goals Options:
1. Add Savings Goal
2. Update Goal Progress
3. View All Goals
4. Back to Main Menu
Enter choice (1-4): 3

All Savings Goals:
===================
1. Emergency Fund
   Target: $10000.00 by 2024-12-31
   Current: $2500.00 (25.0%)
   Monthly Contribution: $500.00
   Remaining: $7500.00
```

### Financial Advice
```
 FINANCIAL ADVICE
===================

PERSONALIZED FINANCIAL ADVICE
==============================

 MODERATE SAVINGS
Your savings rate of 15.0% is decent, but you could save more.

 BUDGET COMPLIANCE
You're staying within your budget limits. Great job!

 SAVINGS GOALS
You have 2 savings goals, with 0 completed.
Focus on your remaining goals and maintain regular contributions.

GENERAL RECOMMENDATIONS
=======================
1. Track your expenses regularly to identify spending patterns
2. Build and maintain an emergency fund
3. Pay off high-interest debt aggressively
4. Maximize retirement account contributions
5. Diversify your investments to manage risk
6. Review your financial plan annually
```

### Investment Portfolio
```
 INVESTMENT MANAGEMENT
========================

Investment Options:
1. Add Investment
2. Update Investment Values
3. View Portfolio
4. Back to Main Menu
Enter choice (1-4): 3

Investment Portfolio:
=====================
1. Tech Stock Portfolio (stocks)
   Initial: $5000.00
   Current: $5500.00
   Gain/Loss: $500.00 (10.00%)
   Expected Return: 12.0% annually
   Risk Level: high

Portfolio Summary:
==================
Total Invested: $5000.00
Total Current Value: $5500.00
Total Gain/Loss: $500.00 (10.00%)
```

## Financial Health Indicators

### Savings Rate Benchmarks
- **Poor**: < 10% of income
- **Fair**: 10-15% of income
- **Good**: 15-20% of income
- **Excellent**: > 20% of income

### Emergency Fund Guidelines
- **Minimum**: 3 months of expenses
- **Adequate**: 3-6 months of expenses
- **Strong**: 6-12 months of expenses
- **Excellent**: > 12 months of expenses

### Debt-to-Income Ratio
- **Excellent**: < 20%
- **Good**: 20-30%
- **Fair**: 30-40%
- **Poor**: > 40%

## Decision Support Features

### Budget Optimization
- **Category Analysis**: Identify overspending areas
- **Reallocation Suggestions**: Move funds between categories
- **Trend Analysis**: Spending pattern recognition

### Savings Strategies
- **Goal Prioritization**: Focus on high-priority goals
- **Contribution Optimization**: Adjust monthly savings amounts
- **Timeline Adjustments**: Modify target dates based on progress

### Investment Recommendations
- **Risk Assessment**: Match investments to risk tolerance
- **Diversification**: Balance portfolio across asset types
- **Performance Monitoring**: Regular portfolio reviews

## Limitations

- Fixed maximum limits for transactions, categories, goals, and investments
- Simple text-based file storage (no database)
- Basic market simulation (not real-time data)
- No currency conversion or multi-currency support
- Limited historical data analysis
- No integration with financial institutions

## Future Enhancements

### Advanced Analytics
- **Trend Analysis**: Historical spending and investment patterns
- **Predictive Modeling**: Future expense and income forecasting
- **Scenario Planning**: "What-if" financial scenario analysis
- **Tax Optimization**: Tax-efficient investment and savings strategies

### Integration Features
- **Bank Integration**: Direct connection to financial institutions
- **Real-time Data**: Live market data and exchange rates
- **Mobile App**: Smartphone application for on-the-go access
- **Cloud Sync**: Cross-device data synchronization

### Advanced Tools
- **Retirement Planning**: Comprehensive retirement calculators
- **Tax Planning**: Tax liability estimation and optimization
- **Insurance Analysis**: Insurance coverage gap analysis
- **Estate Planning**: Wealth transfer and inheritance planning

## Learning Outcomes

This application demonstrates:
- **Complex Data Management**: Multi-structure data organization and manipulation
- **Financial Logic Implementation**: Real-world financial calculations and algorithms
- **Decision Support Systems**: Rule-based recommendation engines
- **File I/O Operations**: Advanced data persistence and retrieval
- **User Interface Design**: Multi-level menu systems with context awareness
- **Error Handling**: Comprehensive input validation and error recovery
- **Modular Architecture**: Organized code with clear separation of concerns

## Compilation

### Requirements
- GCC compiler with math library support
- Standard C libraries (stdio.h, stdlib.h, string.h, ctype.h, time.h, math.h)

### Build Command
```bash
gcc main.c -o finance_advisor -lm -Wall -Wextra
```

### Debug Build
```bash
gcc main.c -o finance_advisor_debug -lm -Wall -Wextra -g -O0
```

### Clean Build
```bash
rm -f finance_advisor finance_advisor_debug
gcc main.c -o finance_advisor -lm -Wall -Wextra
```

---

*Built as Level 5 of Stage 4: Full Problem Solving in the C/C++ Programming Curriculum*