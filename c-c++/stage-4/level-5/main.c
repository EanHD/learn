#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include <math.h>

// Constants
#define MAX_TRANSACTIONS 1000
#define MAX_CATEGORIES 20
#define MAX_GOALS 10
#define MAX_INVESTMENTS 50
#define MAX_NAME_LENGTH 100
#define MAX_DESCRIPTION_LENGTH 200

// Data Structures
typedef struct {
    char date[11]; // YYYY-MM-DD format
    char description[MAX_DESCRIPTION_LENGTH];
    char category[MAX_NAME_LENGTH];
    double amount;
    char type[10]; // "income" or "expense"
} Transaction;

typedef struct {
    char name[MAX_NAME_LENGTH];
    double budgeted_amount;
    double spent_amount;
    double remaining_amount;
} BudgetCategory;

typedef struct {
    char name[MAX_NAME_LENGTH];
    double target_amount;
    double current_amount;
    char target_date[11];
    double monthly_contribution;
} SavingsGoal;

typedef struct {
    char name[MAX_NAME_LENGTH];
    char type[MAX_NAME_LENGTH]; // stocks, bonds, mutual_funds, real_estate, savings
    double initial_investment;
    double current_value;
    double expected_return; // annual percentage
    char risk_level[20]; // low, medium, high
} Investment;

typedef struct {
    double monthly_income;
    double monthly_expenses;
    double savings_rate;
    double debt_to_income_ratio;
    double emergency_fund_months;
} FinancialProfile;

// Global Variables
Transaction transactions[MAX_TRANSACTIONS];
int transaction_count = 0;
BudgetCategory budget_categories[MAX_CATEGORIES];
int category_count = 0;
SavingsGoal savings_goals[MAX_GOALS];
int goal_count = 0;
Investment investments[MAX_INVESTMENTS];
int investment_count = 0;
FinancialProfile profile = {0};

// Function Prototypes
void initialize_sample_data();
void display_main_menu();
void manage_transactions();
void view_budget_analysis();
void manage_budget_categories();
void manage_savings_goals();
void manage_investments();
void generate_financial_report();
void get_financial_advice();
void save_financial_data();
void load_financial_data();

// Utility Functions
void clear_screen() {
    system("clear");
}

void pause() {
    printf("\nPress Enter to continue...");
    getchar();
    getchar(); // consume newline
}

double calculate_total_income() {
    double total = 0;
    for(int i = 0; i < transaction_count; i++) {
        if(strcmp(transactions[i].type, "income") == 0) {
            total += transactions[i].amount;
        }
    }
    return total;
}

double calculate_total_expenses() {
    double total = 0;
    for(int i = 0; i < transaction_count; i++) {
        if(strcmp(transactions[i].type, "expense") == 0) {
            total += transactions[i].amount;
        }
    }
    return total;
}

void update_budget_categories() {
    // Reset spent amounts
    for(int i = 0; i < category_count; i++) {
        budget_categories[i].spent_amount = 0;
    }

    // Calculate spent amounts from transactions
    for(int i = 0; i < transaction_count; i++) {
        if(strcmp(transactions[i].type, "expense") == 0) {
            for(int j = 0; j < category_count; j++) {
                if(strcmp(transactions[i].category, budget_categories[j].name) == 0) {
                    budget_categories[j].spent_amount += transactions[i].amount;
                    break;
                }
            }
        }
    }

    // Update remaining amounts
    for(int i = 0; i < category_count; i++) {
        budget_categories[i].remaining_amount =
            budget_categories[i].budgeted_amount - budget_categories[i].spent_amount;
    }
}

void update_savings_goals() {
    // This would typically be called periodically to update progress
    // For simplicity, we'll assume monthly contributions are made
    for(int i = 0; i < goal_count; i++) {
        if(savings_goals[i].monthly_contribution > 0) {
            savings_goals[i].current_amount += savings_goals[i].monthly_contribution;
            if(savings_goals[i].current_amount > savings_goals[i].target_amount) {
                savings_goals[i].current_amount = savings_goals[i].target_amount;
            }
        }
    }
}

void update_investment_values() {
    // Simulate market changes (simplified)
    srand(time(NULL));
    for(int i = 0; i < investment_count; i++) {
        // Random fluctuation between -5% and +10% monthly
        double change_percent = ((rand() % 150) - 50) / 1000.0; // -0.05 to +0.1
        double change = investments[i].current_value * change_percent;
        investments[i].current_value += change;

        // Ensure minimum value
        if(investments[i].current_value < investments[i].initial_investment * 0.5) {
            investments[i].current_value = investments[i].initial_investment * 0.5;
        }
    }
}

// Core Functions
void initialize_sample_data() {
    // Sample transactions
    strcpy(transactions[0].date, "2024-01-01");
    strcpy(transactions[0].description, "Salary");
    strcpy(transactions[0].category, "Income");
    transactions[0].amount = 5000.00;
    strcpy(transactions[0].type, "income");

    strcpy(transactions[1].date, "2024-01-02");
    strcpy(transactions[1].description, "Grocery shopping");
    strcpy(transactions[1].category, "Food");
    transactions[1].amount = 150.00;
    strcpy(transactions[1].type, "expense");

    strcpy(transactions[2].date, "2024-01-03");
    strcpy(transactions[2].description, "Rent payment");
    strcpy(transactions[2].category, "Housing");
    transactions[2].amount = 1200.00;
    strcpy(transactions[2].type, "expense");

    strcpy(transactions[3].date, "2024-01-04");
    strcpy(transactions[3].description, "Gas bill");
    strcpy(transactions[3].category, "Utilities");
    transactions[3].amount = 80.00;
    strcpy(transactions[3].type, "expense");

    transaction_count = 4;

    // Sample budget categories
    strcpy(budget_categories[0].name, "Food");
    budget_categories[0].budgeted_amount = 600.00;

    strcpy(budget_categories[1].name, "Housing");
    budget_categories[1].budgeted_amount = 1200.00;

    strcpy(budget_categories[2].name, "Utilities");
    budget_categories[2].budgeted_amount = 200.00;

    strcpy(budget_categories[3].name, "Transportation");
    budget_categories[3].budgeted_amount = 300.00;

    strcpy(budget_categories[4].name, "Entertainment");
    budget_categories[4].budgeted_amount = 200.00;

    category_count = 5;
    update_budget_categories();

    // Sample savings goals
    strcpy(savings_goals[0].name, "Emergency Fund");
    savings_goals[0].target_amount = 10000.00;
    savings_goals[0].current_amount = 2500.00;
    strcpy(savings_goals[0].target_date, "2024-12-31");
    savings_goals[0].monthly_contribution = 500.00;

    strcpy(savings_goals[1].name, "Vacation");
    savings_goals[1].target_amount = 3000.00;
    savings_goals[1].current_amount = 800.00;
    strcpy(savings_goals[1].target_date, "2024-07-01");
    savings_goals[1].monthly_contribution = 300.00;

    goal_count = 2;

    // Sample investments
    strcpy(investments[0].name, "Tech Stock Portfolio");
    strcpy(investments[0].type, "stocks");
    investments[0].initial_investment = 5000.00;
    investments[0].current_value = 5500.00;
    investments[0].expected_return = 12.0;
    strcpy(investments[0].risk_level, "high");

    strcpy(investments[1].name, "Government Bonds");
    strcpy(investments[1].type, "bonds");
    investments[1].initial_investment = 10000.00;
    investments[1].current_value = 10200.00;
    investments[1].expected_return = 4.0;
    strcpy(investments[1].risk_level, "low");

    investment_count = 2;

    // Financial profile
    profile.monthly_income = 5000.00;
    profile.monthly_expenses = 1830.00; // sum of sample expenses
    profile.savings_rate = 0.20;
    profile.debt_to_income_ratio = 0.25;
    profile.emergency_fund_months = 6.0;
}

void display_main_menu() {
    clear_screen();
    printf("💰 PERSONAL FINANCE ADVISOR 💰\n");
    printf("===============================\n\n");
    printf("Main Menu:\n");
    printf("1. 💳 Manage Transactions\n");
    printf("2. 📊 View Budget Analysis\n");
    printf("3. 📋 Manage Budget Categories\n");
    printf("4. 🎯 Manage Savings Goals\n");
    printf("5. 📈 Manage Investments\n");
    printf("6. 📋 Generate Financial Report\n");
    printf("7. 💡 Get Financial Advice\n");
    printf("8. 💾 Save Financial Data\n");
    printf("9. 📂 Load Financial Data\n");
    printf("0. 🚪 Exit\n\n");
    printf("Enter your choice (0-9): ");
}

void manage_transactions() {
    clear_screen();
    printf("💳 TRANSACTION MANAGEMENT 💳\n");
    printf("==============================\n\n");

    printf("Transaction Options:\n");
    printf("1. Add Income\n");
    printf("2. Add Expense\n");
    printf("3. View All Transactions\n");
    printf("4. Search Transactions\n");
    printf("5. Back to Main Menu\n\n");
    printf("Enter choice (1-5): ");

    int choice;
    scanf("%d", &choice);
    getchar(); // consume newline

    switch(choice) {
        case 1: { // Add Income
            if(transaction_count >= MAX_TRANSACTIONS) {
                printf("Transaction limit reached!\n");
                pause();
                return;
            }

            printf("\nAdd Income Transaction:\n");
            printf("Date (YYYY-MM-DD): ");
            fgets(transactions[transaction_count].date, sizeof(transactions[transaction_count].date), stdin);
            transactions[transaction_count].date[strcspn(transactions[transaction_count].date, "\n")] = 0;

            printf("Description: ");
            fgets(transactions[transaction_count].description, sizeof(transactions[transaction_count].description), stdin);
            transactions[transaction_count].description[strcspn(transactions[transaction_count].description, "\n")] = 0;

            printf("Category: ");
            fgets(transactions[transaction_count].category, sizeof(transactions[transaction_count].category), stdin);
            transactions[transaction_count].category[strcspn(transactions[transaction_count].category, "\n")] = 0;

            printf("Amount: $");
            scanf("%lf", &transactions[transaction_count].amount);
            getchar();

            strcpy(transactions[transaction_count].type, "income");
            transaction_count++;

            printf("✅ Income transaction added successfully!\n");
            break;
        }
        case 2: { // Add Expense
            if(transaction_count >= MAX_TRANSACTIONS) {
                printf("Transaction limit reached!\n");
                pause();
                return;
            }

            printf("\nAdd Expense Transaction:\n");
            printf("Date (YYYY-MM-DD): ");
            fgets(transactions[transaction_count].date, sizeof(transactions[transaction_count].date), stdin);
            transactions[transaction_count].date[strcspn(transactions[transaction_count].date, "\n")] = 0;

            printf("Description: ");
            fgets(transactions[transaction_count].description, sizeof(transactions[transaction_count].description), stdin);
            transactions[transaction_count].description[strcspn(transactions[transaction_count].description, "\n")] = 0;

            printf("Category: ");
            fgets(transactions[transaction_count].category, sizeof(transactions[transaction_count].category), stdin);
            transactions[transaction_count].category[strcspn(transactions[transaction_count].category, "\n")] = 0;

            printf("Amount: $");
            scanf("%lf", &transactions[transaction_count].amount);
            getchar();

            strcpy(transactions[transaction_count].type, "expense");
            transaction_count++;

            printf("✅ Expense transaction added successfully!\n");
            update_budget_categories();
            break;
        }
        case 3: { // View All Transactions
            printf("\nAll Transactions:\n");
            printf("=================\n");
            for(int i = 0; i < transaction_count; i++) {
                printf("%d. %s | %s | %s | $%.2f | %s\n",
                       i+1, transactions[i].date, transactions[i].description,
                       transactions[i].category, transactions[i].amount, transactions[i].type);
            }
            if(transaction_count == 0) {
                printf("No transactions found.\n");
            }
            break;
        }
        case 4: { // Search Transactions
            printf("\nSearch Options:\n");
            printf("1. By Category\n");
            printf("2. By Date Range\n");
            printf("3. By Amount Range\n");
            printf("Enter search choice (1-3): ");

            int search_choice;
            scanf("%d", &search_choice);
            getchar();

            int found = 0;
            printf("\nSearch Results:\n");
            printf("================\n");

            switch(search_choice) {
                case 1: {
                    char search_category[MAX_NAME_LENGTH];
                    printf("Enter category: ");
                    fgets(search_category, sizeof(search_category), stdin);
                    search_category[strcspn(search_category, "\n")] = 0;

                    for(int i = 0; i < transaction_count; i++) {
                        if(strstr(transactions[i].category, search_category) != NULL) {
                            printf("%s | %s | $%.2f | %s\n",
                                   transactions[i].date, transactions[i].description,
                                   transactions[i].amount, transactions[i].type);
                            found = 1;
                        }
                    }
                    break;
                }
                case 2: {
                    char start_date[11], end_date[11];
                    printf("Start date (YYYY-MM-DD): ");
                    fgets(start_date, sizeof(start_date), stdin);
                    start_date[strcspn(start_date, "\n")] = 0;
                    printf("End date (YYYY-MM-DD): ");
                    fgets(end_date, sizeof(end_date), stdin);
                    end_date[strcspn(end_date, "\n")] = 0;

                    for(int i = 0; i < transaction_count; i++) {
                        if(strcmp(transactions[i].date, start_date) >= 0 &&
                           strcmp(transactions[i].date, end_date) <= 0) {
                            printf("%s | %s | $%.2f | %s\n",
                                   transactions[i].date, transactions[i].description,
                                   transactions[i].amount, transactions[i].type);
                            found = 1;
                        }
                    }
                    break;
                }
                case 3: {
                    double min_amount, max_amount;
                    printf("Minimum amount: $");
                    scanf("%lf", &min_amount);
                    printf("Maximum amount: $");
                    scanf("%lf", &max_amount);
                    getchar();

                    for(int i = 0; i < transaction_count; i++) {
                        if(transactions[i].amount >= min_amount &&
                           transactions[i].amount <= max_amount) {
                            printf("%s | %s | $%.2f | %s\n",
                                   transactions[i].date, transactions[i].description,
                                   transactions[i].amount, transactions[i].type);
                            found = 1;
                        }
                    }
                    break;
                }
            }

            if(!found) {
                printf("No transactions found matching your criteria.\n");
            }
            break;
        }
        case 5:
            return;
        default:
            printf("Invalid choice!\n");
    }

    pause();
}

void view_budget_analysis() {
    clear_screen();
    printf("📊 BUDGET ANALYSIS 📊\n");
    printf("=====================\n\n");

    update_budget_categories();

    double total_budgeted = 0;
    double total_spent = 0;

    printf("Budget Category Analysis:\n");
    printf("=========================\n");
    for(int i = 0; i < category_count; i++) {
        printf("%s:\n", budget_categories[i].name);
        printf("  Budgeted: $%.2f\n", budget_categories[i].budgeted_amount);
        printf("  Spent: $%.2f\n", budget_categories[i].spent_amount);
        printf("  Remaining: $%.2f", budget_categories[i].remaining_amount);
        if(budget_categories[i].remaining_amount < 0) {
            printf(" ⚠️  OVER BUDGET!\n");
        } else {
            printf("\n");
        }
        printf("\n");

        total_budgeted += budget_categories[i].budgeted_amount;
        total_spent += budget_categories[i].spent_amount;
    }

    printf("Summary:\n");
    printf("========\n");
    printf("Total Budgeted: $%.2f\n", total_budgeted);
    printf("Total Spent: $%.2f\n", total_spent);
    printf("Total Remaining: $%.2f\n", total_budgeted - total_spent);

    double spent_percentage = (total_spent / total_budgeted) * 100;
    printf("Budget Used: %.1f%%\n", spent_percentage);

    if(spent_percentage > 100) {
        printf("⚠️  You are over budget!\n");
    } else if(spent_percentage > 90) {
        printf("⚠️  You are close to your budget limit!\n");
    } else {
        printf("✅ Budget is under control.\n");
    }

    pause();
}

void manage_budget_categories() {
    clear_screen();
    printf("📋 BUDGET CATEGORY MANAGEMENT 📋\n");
    printf("==================================\n\n");

    printf("Category Options:\n");
    printf("1. Add Category\n");
    printf("2. Edit Category\n");
    printf("3. Delete Category\n");
    printf("4. View All Categories\n");
    printf("5. Back to Main Menu\n\n");
    printf("Enter choice (1-5): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // Add Category
            if(category_count >= MAX_CATEGORIES) {
                printf("Category limit reached!\n");
                pause();
                return;
            }

            printf("\nAdd Budget Category:\n");
            printf("Category name: ");
            fgets(budget_categories[category_count].name, sizeof(budget_categories[category_count].name), stdin);
            budget_categories[category_count].name[strcspn(budget_categories[category_count].name, "\n")] = 0;

            printf("Budgeted amount: $");
            scanf("%lf", &budget_categories[category_count].budgeted_amount);
            getchar();

            budget_categories[category_count].spent_amount = 0;
            budget_categories[category_count].remaining_amount = budget_categories[category_count].budgeted_amount;
            category_count++;

            printf("✅ Category added successfully!\n");
            break;
        }
        case 2: { // Edit Category
            printf("\nCurrent Categories:\n");
            for(int i = 0; i < category_count; i++) {
                printf("%d. %s - $%.2f\n", i+1, budget_categories[i].name, budget_categories[i].budgeted_amount);
            }

            printf("Enter category number to edit: ");
            int edit_choice;
            scanf("%d", &edit_choice);
            getchar();

            if(edit_choice < 1 || edit_choice > category_count) {
                printf("Invalid category number!\n");
                break;
            }

            printf("New budgeted amount for %s: $", budget_categories[edit_choice-1].name);
            scanf("%lf", &budget_categories[edit_choice-1].budgeted_amount);
            getchar();

            update_budget_categories();
            printf("✅ Category updated successfully!\n");
            break;
        }
        case 3: { // Delete Category
            printf("\nCurrent Categories:\n");
            for(int i = 0; i < category_count; i++) {
                printf("%d. %s\n", i+1, budget_categories[i].name);
            }

            printf("Enter category number to delete: ");
            int delete_choice;
            scanf("%d", &delete_choice);
            getchar();

            if(delete_choice < 1 || delete_choice > category_count) {
                printf("Invalid category number!\n");
                break;
            }

            // Shift remaining categories
            for(int i = delete_choice-1; i < category_count-1; i++) {
                budget_categories[i] = budget_categories[i+1];
            }
            category_count--;

            printf("✅ Category deleted successfully!\n");
            break;
        }
        case 4: { // View All Categories
            printf("\nAll Budget Categories:\n");
            printf("======================\n");
            for(int i = 0; i < category_count; i++) {
                printf("%d. %s\n", i+1, budget_categories[i].name);
                printf("   Budgeted: $%.2f\n", budget_categories[i].budgeted_amount);
                printf("   Spent: $%.2f\n", budget_categories[i].spent_amount);
                printf("   Remaining: $%.2f\n\n", budget_categories[i].remaining_amount);
            }
            if(category_count == 0) {
                printf("No categories found.\n");
            }
            break;
        }
        case 5:
            return;
        default:
            printf("Invalid choice!\n");
    }

    pause();
}

void manage_savings_goals() {
    clear_screen();
    printf("🎯 SAVINGS GOALS MANAGEMENT 🎯\n");
    printf("==============================\n\n");

    printf("Goals Options:\n");
    printf("1. Add Savings Goal\n");
    printf("2. Update Goal Progress\n");
    printf("3. View All Goals\n");
    printf("4. Back to Main Menu\n\n");
    printf("Enter choice (1-4): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // Add Goal
            if(goal_count >= MAX_GOALS) {
                printf("Goal limit reached!\n");
                pause();
                return;
            }

            printf("\nAdd Savings Goal:\n");
            printf("Goal name: ");
            fgets(savings_goals[goal_count].name, sizeof(savings_goals[goal_count].name), stdin);
            savings_goals[goal_count].name[strcspn(savings_goals[goal_count].name, "\n")] = 0;

            printf("Target amount: $");
            scanf("%lf", &savings_goals[goal_count].target_amount);
            getchar();

            printf("Current amount: $");
            scanf("%lf", &savings_goals[goal_count].current_amount);
            getchar();

            printf("Target date (YYYY-MM-DD): ");
            fgets(savings_goals[goal_count].target_date, sizeof(savings_goals[goal_count].target_date), stdin);
            savings_goals[goal_count].target_date[strcspn(savings_goals[goal_count].target_date, "\n")] = 0;

            printf("Monthly contribution: $");
            scanf("%lf", &savings_goals[goal_count].monthly_contribution);
            getchar();

            goal_count++;
            printf("✅ Savings goal added successfully!\n");
            break;
        }
        case 2: { // Update Progress
            printf("\nCurrent Savings Goals:\n");
            for(int i = 0; i < goal_count; i++) {
                printf("%d. %s - Current: $%.2f / Target: $%.2f\n",
                       i+1, savings_goals[i].name, savings_goals[i].current_amount, savings_goals[i].target_amount);
            }

            printf("Enter goal number to update: ");
            int update_choice;
            scanf("%d", &update_choice);
            getchar();

            if(update_choice < 1 || update_choice > goal_count) {
                printf("Invalid goal number!\n");
                break;
            }

            printf("Additional amount to add: $");
            double additional;
            scanf("%lf", &additional);
            getchar();

            savings_goals[update_choice-1].current_amount += additional;

            if(savings_goals[update_choice-1].current_amount >= savings_goals[update_choice-1].target_amount) {
                printf("🎉 Goal achieved! %s\n", savings_goals[update_choice-1].name);
            } else {
                double remaining = savings_goals[update_choice-1].target_amount - savings_goals[update_choice-1].current_amount;
                printf("✅ Progress updated! $%.2f remaining.\n", remaining);
            }
            break;
        }
        case 3: { // View All Goals
            printf("\nAll Savings Goals:\n");
            printf("===================\n");
            for(int i = 0; i < goal_count; i++) {
                double progress_percent = (savings_goals[i].current_amount / savings_goals[i].target_amount) * 100;
                printf("%d. %s\n", i+1, savings_goals[i].name);
                printf("   Target: $%.2f by %s\n", savings_goals[i].target_amount, savings_goals[i].target_date);
                printf("   Current: $%.2f (%.1f%%)\n", savings_goals[i].current_amount, progress_percent);
                printf("   Monthly Contribution: $%.2f\n", savings_goals[i].monthly_contribution);

                if(savings_goals[i].current_amount >= savings_goals[i].target_amount) {
                    printf("   Status: ✅ ACHIEVED\n");
                } else {
                    double remaining = savings_goals[i].target_amount - savings_goals[i].current_amount;
                    printf("   Remaining: $%.2f\n", remaining);
                }
                printf("\n");
            }
            if(goal_count == 0) {
                printf("No savings goals found.\n");
            }
            break;
        }
        case 4:
            return;
        default:
            printf("Invalid choice!\n");
    }

    pause();
}

void manage_investments() {
    clear_screen();
    printf("📈 INVESTMENT MANAGEMENT 📈\n");
    printf("===========================\n\n");

    printf("Investment Options:\n");
    printf("1. Add Investment\n");
    printf("2. Update Investment Values\n");
    printf("3. View Portfolio\n");
    printf("4. Back to Main Menu\n\n");
    printf("Enter choice (1-4): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // Add Investment
            if(investment_count >= MAX_INVESTMENTS) {
                printf("Investment limit reached!\n");
                pause();
                return;
            }

            printf("\nAdd Investment:\n");
            printf("Investment name: ");
            fgets(investments[investment_count].name, sizeof(investments[investment_count].name), stdin);
            investments[investment_count].name[strcspn(investments[investment_count].name, "\n")] = 0;

            printf("Type (stocks, bonds, mutual_funds, real_estate, savings): ");
            fgets(investments[investment_count].type, sizeof(investments[investment_count].type), stdin);
            investments[investment_count].type[strcspn(investments[investment_count].type, "\n")] = 0;

            printf("Initial investment: $");
            scanf("%lf", &investments[investment_count].initial_investment);
            getchar();

            investments[investment_count].current_value = investments[investment_count].initial_investment;

            printf("Expected annual return (%%): ");
            scanf("%lf", &investments[investment_count].expected_return);
            getchar();

            printf("Risk level (low, medium, high): ");
            fgets(investments[investment_count].risk_level, sizeof(investments[investment_count].risk_level), stdin);
            investments[investment_count].risk_level[strcspn(investments[investment_count].risk_level, "\n")] = 0;

            investment_count++;
            printf("✅ Investment added successfully!\n");
            break;
        }
        case 2: { // Update Values
            update_investment_values();
            printf("✅ Investment values updated with market simulation!\n");
            break;
        }
        case 3: { // View Portfolio
            printf("\nInvestment Portfolio:\n");
            printf("=====================\n");

            double total_invested = 0;
            double total_current = 0;

            for(int i = 0; i < investment_count; i++) {
                double gain_loss = investments[i].current_value - investments[i].initial_investment;
                double gain_loss_percent = (gain_loss / investments[i].initial_investment) * 100;

                printf("%d. %s (%s)\n", i+1, investments[i].name, investments[i].type);
                printf("   Initial: $%.2f\n", investments[i].initial_investment);
                printf("   Current: $%.2f\n", investments[i].current_value);
                printf("   Gain/Loss: $%.2f (%.2f%%)\n", gain_loss, gain_loss_percent);
                printf("   Expected Return: %.1f%% annually\n", investments[i].expected_return);
                printf("   Risk Level: %s\n\n", investments[i].risk_level);

                total_invested += investments[i].initial_investment;
                total_current += investments[i].current_value;
            }

            if(investment_count > 0) {
                double total_gain_loss = total_current - total_invested;
                double total_gain_loss_percent = (total_gain_loss / total_invested) * 100;

                printf("Portfolio Summary:\n");
                printf("==================\n");
                printf("Total Invested: $%.2f\n", total_invested);
                printf("Total Current Value: $%.2f\n", total_current);
                printf("Total Gain/Loss: $%.2f (%.2f%%)\n", total_gain_loss, total_gain_loss_percent);
            } else {
                printf("No investments found.\n");
            }
            break;
        }
        case 4:
            return;
        default:
            printf("Invalid choice!\n");
    }

    pause();
}

void generate_financial_report() {
    clear_screen();
    printf("📋 FINANCIAL REPORT 📋\n");
    printf("======================\n\n");

    double total_income = calculate_total_income();
    double total_expenses = calculate_total_expenses();
    double net_income = total_income - total_expenses;

    printf("INCOME & EXPENSE SUMMARY\n");
    printf("========================\n");
    printf("Total Income: $%.2f\n", total_income);
    printf("Total Expenses: $%.2f\n", total_expenses);
    printf("Net Income: $%.2f\n", net_income);
    printf("Savings Rate: %.1f%%\n\n", (net_income / total_income) * 100);

    printf("BUDGET PERFORMANCE\n");
    printf("==================\n");
    update_budget_categories();
    for(int i = 0; i < category_count; i++) {
        double usage_percent = (budget_categories[i].spent_amount / budget_categories[i].budgeted_amount) * 100;
        printf("%s: $%.2f / $%.2f (%.1f%%)\n",
               budget_categories[i].name, budget_categories[i].spent_amount,
               budget_categories[i].budgeted_amount, usage_percent);
    }

    printf("\nSAVINGS GOALS PROGRESS\n");
    printf("=======================\n");
    for(int i = 0; i < goal_count; i++) {
        double progress_percent = (savings_goals[i].current_amount / savings_goals[i].target_amount) * 100;
        printf("%s: $%.2f / $%.2f (%.1f%%)\n",
               savings_goals[i].name, savings_goals[i].current_amount,
               savings_goals[i].target_amount, progress_percent);
    }

    printf("\nINVESTMENT PERFORMANCE\n");
    printf("=======================\n");
    double total_invested = 0, total_current = 0;
    for(int i = 0; i < investment_count; i++) {
        total_invested += investments[i].initial_investment;
        total_current += investments[i].current_value;
    }
    if(total_invested > 0) {
        double portfolio_return = ((total_current - total_invested) / total_invested) * 100;
        printf("Portfolio Value: $%.2f\n", total_current);
        printf("Total Return: %.2f%%\n", portfolio_return);
    }

    printf("\nFINANCIAL HEALTH METRICS\n");
    printf("=========================\n");
    printf("Monthly Income: $%.2f\n", profile.monthly_income);
    printf("Monthly Expenses: $%.2f\n", profile.monthly_expenses);
    printf("Debt-to-Income Ratio: %.1f%%\n", profile.debt_to_income_ratio * 100);
    printf("Emergency Fund: %.1f months\n", profile.emergency_fund_months);

    pause();
}

void get_financial_advice() {
    clear_screen();
    printf("💡 FINANCIAL ADVICE 💡\n");
    printf("======================\n\n");

    double total_income = calculate_total_income();
    double total_expenses = calculate_total_expenses();
    double savings_rate = ((total_income - total_expenses) / total_income) * 100;

    printf("PERSONALIZED FINANCIAL ADVICE\n");
    printf("==============================\n\n");

    // Savings Rate Advice
    if(savings_rate < 10) {
        printf("⚠️  SAVINGS RATE CONCERN\n");
        printf("Your current savings rate is %.1f%%. Aim for at least 20%% of your income.\n", savings_rate);
        printf("Consider cutting unnecessary expenses and increasing your savings.\n\n");
    } else if(savings_rate < 20) {
        printf("✅ MODERATE SAVINGS\n");
        printf("Your savings rate of %.1f%% is decent, but you could save more.\n\n", savings_rate);
    } else {
        printf("🎉 EXCELLENT SAVINGS HABIT\n");
        printf("Your savings rate of %.1f%% is excellent! Keep it up.\n\n", savings_rate);
    }

    // Budget Analysis
    update_budget_categories();
    int over_budget_count = 0;
    for(int i = 0; i < category_count; i++) {
        if(budget_categories[i].remaining_amount < 0) {
            over_budget_count++;
        }
    }

    if(over_budget_count > 0) {
        printf("⚠️  BUDGET OVERRUNS\n");
        printf("You are over budget in %d categories. Review your spending and adjust accordingly.\n\n", over_budget_count);
    } else {
        printf("✅ BUDGET COMPLIANCE\n");
        printf("You're staying within your budget limits. Great job!\n\n");
    }

    // Savings Goals
    int completed_goals = 0;
    for(int i = 0; i < goal_count; i++) {
        if(savings_goals[i].current_amount >= savings_goals[i].target_amount) {
            completed_goals++;
        }
    }

    if(goal_count > 0) {
        printf("🎯 SAVINGS GOALS\n");
        printf("You have %d savings goals, with %d completed.\n", goal_count, completed_goals);
        if(completed_goals < goal_count) {
            printf("Focus on your remaining goals and maintain regular contributions.\n");
        }
        printf("\n");
    }

    // Investment Advice
    if(investment_count == 0) {
        printf("📈 INVESTMENT RECOMMENDATION\n");
        printf("Consider starting an investment portfolio. Based on your risk tolerance:\n");
        printf("• Low risk: Bonds, high-yield savings, certificates of deposit\n");
        printf("• Medium risk: Index funds, diversified mutual funds\n");
        printf("• High risk: Individual stocks, cryptocurrencies\n\n");
    } else {
        double total_invested = 0, total_current = 0;
        for(int i = 0; i < investment_count; i++) {
            total_invested += investments[i].initial_investment;
            total_current += investments[i].current_value;
        }

        if(total_current > total_invested) {
            printf("📈 INVESTMENT PERFORMANCE\n");
            printf("Your investments are performing well. Consider maintaining your current strategy.\n\n");
        } else {
            printf("📉 INVESTMENT REVIEW\n");
            printf("Some investments are underperforming. Consider rebalancing your portfolio.\n\n");
        }
    }

    // Emergency Fund
    if(profile.emergency_fund_months < 3) {
        printf("🚨 EMERGENCY FUND\n");
        printf("Your emergency fund covers only %.1f months. Aim for 3-6 months of expenses.\n", profile.emergency_fund_months);
        printf("Prioritize building your emergency fund before other goals.\n\n");
    } else if(profile.emergency_fund_months < 6) {
        printf("✅ EMERGENCY FUND\n");
        printf("Your emergency fund covers %.1f months, which is adequate.\n\n", profile.emergency_fund_months);
    } else {
        printf("🎉 STRONG EMERGENCY FUND\n");
        printf("Your emergency fund covers %.1f months. Excellent preparedness!\n\n", profile.emergency_fund_months);
    }

    // Debt Management
    if(profile.debt_to_income_ratio > 0.36) {
        printf("⚠️  HIGH DEBT LEVELS\n");
        printf("Your debt-to-income ratio is %.1f%%. Consider debt reduction strategies.\n\n", profile.debt_to_income_ratio * 100);
    } else {
        printf("✅ MANAGEABLE DEBT\n");
        printf("Your debt levels are within acceptable ranges.\n\n");
    }

    printf("GENERAL RECOMMENDATIONS\n");
    printf("=======================\n");
    printf("1. Track your expenses regularly to identify spending patterns\n");
    printf("2. Build and maintain an emergency fund\n");
    printf("3. Pay off high-interest debt aggressively\n");
    printf("4. Maximize retirement account contributions\n");
    printf("5. Diversify your investments to manage risk\n");
    printf("6. Review your financial plan annually\n");

    pause();
}

void save_financial_data() {
    clear_screen();
    printf("💾 SAVE FINANCIAL DATA 💾\n");
    printf("==========================\n\n");

    char filename[100];
    printf("Enter filename to save (without extension): ");
    fgets(filename, sizeof(filename), stdin);
    filename[strcspn(filename, "\n")] = 0;
    strcat(filename, ".txt");

    FILE *file = fopen(filename, "w");
    if(file == NULL) {
        printf("Error opening file for writing!\n");
        pause();
        return;
    }

    // Save transactions
    fprintf(file, "TRANSACTIONS\n");
    fprintf(file, "%d\n", transaction_count);
    for(int i = 0; i < transaction_count; i++) {
        fprintf(file, "%s|%s|%s|%.2f|%s\n",
                transactions[i].date, transactions[i].description,
                transactions[i].category, transactions[i].amount, transactions[i].type);
    }

    // Save budget categories
    fprintf(file, "BUDGET_CATEGORIES\n");
    fprintf(file, "%d\n", category_count);
    for(int i = 0; i < category_count; i++) {
        fprintf(file, "%s|%.2f\n",
                budget_categories[i].name, budget_categories[i].budgeted_amount);
    }

    // Save savings goals
    fprintf(file, "SAVINGS_GOALS\n");
    fprintf(file, "%d\n", goal_count);
    for(int i = 0; i < goal_count; i++) {
        fprintf(file, "%s|%.2f|%.2f|%s|%.2f\n",
                savings_goals[i].name, savings_goals[i].target_amount,
                savings_goals[i].current_amount, savings_goals[i].target_date,
                savings_goals[i].monthly_contribution);
    }

    // Save investments
    fprintf(file, "INVESTMENTS\n");
    fprintf(file, "%d\n", investment_count);
    for(int i = 0; i < investment_count; i++) {
        fprintf(file, "%s|%s|%.2f|%.2f|%.2f|%s\n",
                investments[i].name, investments[i].type, investments[i].initial_investment,
                investments[i].current_value, investments[i].expected_return, investments[i].risk_level);
    }

    // Save financial profile
    fprintf(file, "FINANCIAL_PROFILE\n");
    fprintf(file, "%.2f|%.2f|%.2f|%.2f|%.2f\n",
            profile.monthly_income, profile.monthly_expenses, profile.savings_rate,
            profile.debt_to_income_ratio, profile.emergency_fund_months);

    fclose(file);
    printf("✅ Financial data saved to '%s' successfully!\n", filename);
    pause();
}

void load_financial_data() {
    clear_screen();
    printf("📂 LOAD FINANCIAL DATA 📂\n");
    printf("=========================\n\n");

    char filename[100];
    printf("Enter filename to load (without extension): ");
    fgets(filename, sizeof(filename), stdin);
    filename[strcspn(filename, "\n")] = 0;
    strcat(filename, ".txt");

    FILE *file = fopen(filename, "r");
    if(file == NULL) {
        printf("File '%s' not found!\n", filename);
        pause();
        return;
    }

    char line[500];
    char section[50] = "";

    while(fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = 0;

        if(strcmp(line, "TRANSACTIONS") == 0) {
            strcpy(section, "TRANSACTIONS");
            fgets(line, sizeof(line), file);
            transaction_count = atoi(line);
            for(int i = 0; i < transaction_count; i++) {
                fgets(line, sizeof(line), file);
                sscanf(line, "%[^|]|%[^|]|%[^|]|%lf|%s",
                       transactions[i].date, transactions[i].description,
                       transactions[i].category, &transactions[i].amount, transactions[i].type);
            }
        } else if(strcmp(line, "BUDGET_CATEGORIES") == 0) {
            strcpy(section, "BUDGET_CATEGORIES");
            fgets(line, sizeof(line), file);
            category_count = atoi(line);
            for(int i = 0; i < category_count; i++) {
                fgets(line, sizeof(line), file);
                sscanf(line, "%[^|]|%lf",
                       budget_categories[i].name, &budget_categories[i].budgeted_amount);
                budget_categories[i].spent_amount = 0;
                budget_categories[i].remaining_amount = budget_categories[i].budgeted_amount;
            }
        } else if(strcmp(line, "SAVINGS_GOALS") == 0) {
            strcpy(section, "SAVINGS_GOALS");
            fgets(line, sizeof(line), file);
            goal_count = atoi(line);
            for(int i = 0; i < goal_count; i++) {
                fgets(line, sizeof(line), file);
                sscanf(line, "%[^|]|%lf|%lf|%[^|]|%lf",
                       savings_goals[i].name, &savings_goals[i].target_amount,
                       &savings_goals[i].current_amount, savings_goals[i].target_date,
                       &savings_goals[i].monthly_contribution);
            }
        } else if(strcmp(line, "INVESTMENTS") == 0) {
            strcpy(section, "INVESTMENTS");
            fgets(line, sizeof(line), file);
            investment_count = atoi(line);
            for(int i = 0; i < investment_count; i++) {
                fgets(line, sizeof(line), file);
                sscanf(line, "%[^|]|%[^|]|%lf|%lf|%lf|%s",
                       investments[i].name, investments[i].type, &investments[i].initial_investment,
                       &investments[i].current_value, &investments[i].expected_return, investments[i].risk_level);
            }
        } else if(strcmp(line, "FINANCIAL_PROFILE") == 0) {
            strcpy(section, "FINANCIAL_PROFILE");
            fgets(line, sizeof(line), file);
            sscanf(line, "%lf|%lf|%lf|%lf|%lf",
                   &profile.monthly_income, &profile.monthly_expenses, &profile.savings_rate,
                   &profile.debt_to_income_ratio, &profile.emergency_fund_months);
        }
    }

    fclose(file);
    update_budget_categories();
    printf("✅ Financial data loaded from '%s' successfully!\n", filename);
    pause();
}

int main() {
    initialize_sample_data();

    int choice;
    do {
        display_main_menu();
        scanf("%d", &choice);
        getchar(); // consume newline

        switch(choice) {
            case 1:
                manage_transactions();
                break;
            case 2:
                view_budget_analysis();
                break;
            case 3:
                manage_budget_categories();
                break;
            case 4:
                manage_savings_goals();
                break;
            case 5:
                manage_investments();
                break;
            case 6:
                generate_financial_report();
                break;
            case 7:
                get_financial_advice();
                break;
            case 8:
                save_financial_data();
                break;
            case 9:
                load_financial_data();
                break;
            case 0:
                printf("\nThank you for using the Personal Finance Advisor! 💰\n");
                break;
            default:
                printf("Invalid choice! Please enter 0-9.\n");
                pause();
        }
    } while(choice != 0);

    return 0;
}