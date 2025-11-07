# Level 4: Interactive Application

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 4: Full Problem Solving

### Today's Mission

**INTERACTIVE MASTERPIECE!**  You're now creating highly interactive applications with sophisticated user interfaces, real-time feedback, and engaging user experiences. This level focuses on user-centered design, input validation, and creating applications that feel professional and responsive.

**The Process:**
1. **User Experience Design**: Plan intuitive navigation and workflows
2. **Interactive Architecture**: Design multi-level menus and user flows
3. **Real-time Feedback**: Provide immediate responses and validation
4. **Data Persistence**: Save and restore user progress
5. **Error Recovery**: Handle mistakes gracefully with helpful guidance
6. **Engagement Features**: Add progress tracking and achievements
7. **Professional Polish**: Create a cohesive, professional application

---

### Learning Goals

- [ ] Advanced user interface design
- [ ] Multi-level menu systems
- [ ] Real-time input validation
- [ ] User experience optimization
- [ ] Data persistence and state management
- [ ] Interactive application architecture
- [ ] Error handling and user guidance

---

### Your Task

**Build a complete Personal Budget Tracker with:**
1. **Account Management**: Multiple accounts with balances
2. **Transaction Tracking**: Income and expense recording
3. **Budget Planning**: Category-based budgeting
4. **Financial Goals**: Savings targets and progress tracking
5. **Reports & Analytics**: Spending analysis and trends
6. **Data Visualization**: Text-based charts and graphs
7. **User Guidance**: Help system and tutorials

---

## Application Requirements

### Core Features
- [ ] **Multi-Account Support**: Checking, savings, credit cards
- [ ] **Transaction Management**: Add, edit, delete transactions
- [ ] **Category System**: Organize expenses by category
- [ ] **Budget Monitoring**: Set and track spending limits
- [ ] **Goal Setting**: Financial targets with progress tracking
- [ ] **Financial Reports**: Monthly summaries and analytics
- [ ] **Data Export**: Save reports and backup data

### Technical Requirements
- [ ] Persistent data storage with file I/O
- [ ] Real-time balance calculations
- [ ] Input validation and error recovery
- [ ] Multi-level navigation system
- [ ] Progress saving and restoration
- [ ] User-friendly help system

---

## Application Architecture

### Data Structures
```c
# define MAX_ACCOUNTS 10
# define MAX_TRANSACTIONS 1000
# define MAX_CATEGORIES 20
# define MAX_NAME_LENGTH 50
# define MAX_DESCRIPTION_LENGTH 100

typedef enum {
    INCOME,
    EXPENSE
} TransactionType;

typedef enum {
    CHECKING,
    SAVINGS,
    CREDIT_CARD,
    INVESTMENT
} AccountType;

typedef struct {
    int id;
    char date[11];  // YYYY-MM-DD
    char description[MAX_DESCRIPTION_LENGTH];
    char category[MAX_NAME_LENGTH];
    TransactionType type;
    double amount;
    int account_id;
} Transaction;

typedef struct {
    int id;
    char name[MAX_NAME_LENGTH];
    AccountType type;
    double balance;
    double credit_limit;  // For credit cards
} Account;

typedef struct {
    char category[MAX_NAME_LENGTH];
    double budgeted_amount;
    double spent_amount;
} BudgetCategory;

typedef struct {
    char description[MAX_DESCRIPTION_LENGTH];
    double target_amount;
    double current_amount;
    char target_date[11];
} FinancialGoal;

typedef struct {
    Account accounts[MAX_ACCOUNTS];
    Transaction transactions[MAX_TRANSACTIONS];
    BudgetCategory budget[MAX_CATEGORIES];
    FinancialGoal goals[5];
    int account_count;
    int transaction_count;
    int budget_count;
    int goal_count;
    char data_file[256];
} BudgetTracker;
```

### Function Modules
- [ ] **User Interface**: `display_main_menu()`, `handle_navigation()`
- [ ] **Account Management**: `add_account()`, `update_balance()`
- [ ] **Transaction Processing**: `add_transaction()`, `edit_transaction()`
- [ ] **Budget System**: `set_budget()`, `check_budget_limits()`
- [ ] **Goal Tracking**: `add_goal()`, `update_goal_progress()`
- [ ] **Reporting**: `generate_report()`, `display_analytics()`
- [ ] **Data Management**: `save_data()`, `load_data()`

---

## Complete Implementation

### Header File (budget_tracker.h)
```c
# ifndef BUDGET_TRACKER_H
# define BUDGET_TRACKER_H

# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <time.h>
# include <ctype.h>

# define MAX_ACCOUNTS 10
# define MAX_TRANSACTIONS 1000
# define MAX_CATEGORIES 20
# define MAX_NAME_LENGTH 50
# define MAX_DESCRIPTION_LENGTH 100

typedef enum {
    INCOME,
    EXPENSE
} TransactionType;

typedef enum {
    CHECKING,
    SAVINGS,
    CREDIT_CARD,
    INVESTMENT
} AccountType;

typedef struct {
    int id;
    char date[11];  // YYYY-MM-DD
    char description[MAX_DESCRIPTION_LENGTH];
    char category[MAX_NAME_LENGTH];
    TransactionType type;
    double amount;
    int account_id;
} Transaction;

typedef struct {
    int id;
    char name[MAX_NAME_LENGTH];
    AccountType type;
    double balance;
    double credit_limit;  // For credit cards
} Account;

typedef struct {
    char category[MAX_NAME_LENGTH];
    double budgeted_amount;
    double spent_amount;
} BudgetCategory;

typedef struct {
    char description[MAX_DESCRIPTION_LENGTH];
    double target_amount;
    double current_amount;
    char target_date[11];
} FinancialGoal;

typedef struct {
    Account accounts[MAX_ACCOUNTS];
    Transaction transactions[MAX_TRANSACTIONS];
    BudgetCategory budget[MAX_CATEGORIES];
    FinancialGoal goals[5];
    int account_count;
    int transaction_count;
    int budget_count;
    int goal_count;
    char data_file[256];
} BudgetTracker;

// Function prototypes
void initialize_budget_tracker(BudgetTracker *tracker, const char *filename);
void display_main_menu(void);
void display_accounts_menu(void);
void display_transactions_menu(void);
void display_budget_menu(void);
void display_goals_menu(void);
void display_reports_menu(void);

int get_user_choice(void);
void clear_screen(void);
void pause(void);

// Account management
int add_account(BudgetTracker *tracker);
void display_accounts(const BudgetTracker *tracker);
int find_account(const BudgetTracker *tracker, int id);
void update_account_balance(BudgetTracker *tracker, int account_id, double amount, TransactionType type);

// Transaction management
int add_transaction(BudgetTracker *tracker);
void display_transactions(const BudgetTracker *tracker, int limit);
int edit_transaction(BudgetTracker *tracker);
int delete_transaction(BudgetTracker *tracker);
void display_transaction_summary(const BudgetTracker *tracker);

// Budget management
int set_budget_category(BudgetTracker *tracker);
void display_budget_status(const BudgetTracker *tracker);
void update_budget_spending(BudgetTracker *tracker, const char *category, double amount);
int check_budget_limit(const BudgetTracker *tracker, const char *category, double amount);

// Goal management
int add_financial_goal(BudgetTracker *tracker);
void display_goals(const BudgetTracker *tracker);
void update_goal_progress(BudgetTracker *tracker, int goal_id, double amount);
double calculate_goal_progress(const FinancialGoal *goal);

// Reporting and analytics
void generate_monthly_report(const BudgetTracker *tracker);
void display_spending_by_category(const BudgetTracker *tracker);
void display_income_vs_expenses(const BudgetTracker *tracker);
void display_budget_vs_actual(const BudgetTracker *tracker);

// Data persistence
int save_data(const BudgetTracker *tracker);
int load_data(BudgetTracker *tracker);

// Utility functions
void get_current_date(char *date);
int validate_date(const char *date);
double get_positive_amount(const char *prompt);
void display_help(void);

# endif
```

### Implementation File (budget_tracker.c)
```c
# include "budget_tracker.h"

// Initialize budget tracker
void initialize_budget_tracker(BudgetTracker *tracker, const char *filename) {
    tracker->account_count = 0;
    tracker->transaction_count = 0;
    tracker->budget_count = 0;
    tracker->goal_count = 0;
    strcpy(tracker->data_file, filename);
    load_data(tracker);
}

// Display functions
void display_main_menu(void) {
    clear_screen();
    std::cout << "╔══════════════════════════════════════════════╗\n");
    std::cout << "║            PERSONAL BUDGET TRACKER         ║\n");
    std::cout << "╠══════════════════════════════════════════════╣\n");
    std::cout << "║ 1.  View Dashboard                        ║\n");
    std::cout << "║ 2.  Manage Accounts                       ║\n");
    std::cout << "║ 3.  Manage Transactions                   ║\n");
    std::cout << "║ 4.  Budget Planning                       ║\n");
    std::cout << "║ 5.  Financial Goals                       ║\n");
    std::cout << "║ 6.  Reports & Analytics                   ║\n");
    std::cout << "║ 7.  Help                                   ║\n");
    std::cout << "║ 8.  Save Data                             ║\n");
    std::cout << "║ 9.  Exit                                  ║\n");
    std::cout << "╚══════════════════════════════════════════════╝\n");
    std::cout << "Enter your choice (1-9): ");
}

void display_accounts_menu(void) {
    std::cout << "\n Account Management\n");
    std::cout << "═══════════════════════\n");
    std::cout << "1. Add Account\n");
    std::cout << "2. View Accounts\n");
    std::cout << "3. Back to Main Menu\n");
    std::cout << "Enter choice: ");
}

void display_transactions_menu(void) {
    std::cout << "\n Transaction Management\n");
    std::cout << "═══════════════════════════\n");
    std::cout << "1. Add Transaction\n");
    std::cout << "2. View Transactions\n");
    std::cout << "3. Edit Transaction\n");
    std::cout << "4. Delete Transaction\n");
    std::cout << "5. Back to Main Menu\n");
    std::cout << "Enter choice: ");
}

void display_budget_menu(void) {
    std::cout << "\n Budget Planning\n");
    std::cout << "════════════════════\n");
    std::cout << "1. Set Budget Category\n");
    std::cout << "2. View Budget Status\n");
    std::cout << "3. Back to Main Menu\n");
    std::cout << "Enter choice: ");
}

void display_goals_menu(void) {
    std::cout << "\n Financial Goals\n");
    std::cout << "════════════════════\n");
    std::cout << "1. Add Goal\n");
    std::cout << "2. View Goals\n");
    std::cout << "3. Update Goal Progress\n");
    std::cout << "4. Back to Main Menu\n");
    std::cout << "Enter choice: ");
}

void display_reports_menu(void) {
    std::cout << "\n Reports & Analytics\n");
    std::cout << "════════════════════════\n");
    std::cout << "1. Monthly Report\n");
    std::cout << "2. Spending by Category\n");
    std::cout << "3. Income vs Expenses\n");
    std::cout << "4. Budget vs Actual\n");
    std::cout << "5. Back to Main Menu\n");
    std::cout << "Enter choice: ");
}

// Utility functions
int get_user_choice(void) {
    int choice;
    scanf("%d", &choice);
    return choice;
}

void clear_screen(void) {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

void pause(void) {
    std::cout << "\nPress Enter to continue...");
    getchar();
    getchar(); // Second getchar for the newline
}

// Account management
int add_account(BudgetTracker *tracker) {
    if (tracker->account_count >= MAX_ACCOUNTS) {
        std::cout << " Maximum number of accounts reached!\n");
        return 0;
    }

    Account *account = &tracker->accounts[tracker->account_count];
    account->id = tracker->account_count + 1;

    std::cout << "Enter account name: ");
    scanf(" %[^\n]", account->name);

    std::cout << "Account type:\n");
    std::cout << "1. Checking\n2. Savings\n3. Credit Card\n4. Investment\n");
    std::cout << "Enter type (1-4): ");
    int type_choice = get_user_choice();

    switch (type_choice) {
        case 1: account->type = CHECKING; break;
        case 2: account->type = SAVINGS; break;
        case 3: account->type = CREDIT_CARD; break;
        case 4: account->type = INVESTMENT; break;
        default:
            std::cout << " Invalid account type!\n");
            return 0;
    }

    std::cout << "Enter starting balance: $");
    scanf("%lf", &account->balance);

    if (account->type == CREDIT_CARD) {
        std::cout << "Enter credit limit: $");
        scanf("%lf", &account->credit_limit);
    } else {
        account->credit_limit = 0.0;
    }

    tracker->account_count++;
    std::cout << " Account '%s' added successfully!\n", account->name);
    return 1;
}

void display_accounts(const BudgetTracker *tracker) {
    if (tracker->account_count == 0) {
        std::cout << " No accounts found. Add your first account!\n");
        return;
    }

    std::cout << "\n Your Accounts\n");
    std::cout << "═══════════════════════════════════════════════════════════════\n");
    std::cout << "%-3s %-20s %-12s %-15s %-10s\n", "ID", "Name", "Type", "Balance", "Limit");
    std::cout << "───────────────────────────────────────────────────────────────\n");

    for (int i = 0; i < tracker->account_count; i++) {
        const Account *acc = &tracker->accounts[i];
        const char *type_str = (acc->type == CHECKING) ? "Checking" :
                              (acc->type == SAVINGS) ? "Savings" :
                              (acc->type == CREDIT_CARD) ? "Credit Card" : "Investment";

        std::cout << "%-3d %-20s %-12s $%-14.2f", acc->id, acc->name, type_str, acc->balance);

        if (acc->type == CREDIT_CARD) {
            std::cout << "$%-10.2f", acc->credit_limit);
        } else {
            std::cout << "N/A        ");
        }
        std::cout << "\n");
    }
}

int find_account(const BudgetTracker *tracker, int id) {
    for (int i = 0; i < tracker->account_count; i++) {
        if (tracker->accounts[i].id == id) {
            return i;
        }
    }
    return -1;
}

void update_account_balance(BudgetTracker *tracker, int account_id, double amount, TransactionType type) {
    int index = find_account(tracker, account_id);
    if (index == -1) return;

    Account *account = &tracker->accounts[index];

    if (type == INCOME) {
        account->balance += amount;
    } else { // EXPENSE
        account->balance -= amount;
    }
}

// Transaction management
int add_transaction(BudgetTracker *tracker) {
    if (tracker->transaction_count >= MAX_TRANSACTIONS) {
        std::cout << " Maximum number of transactions reached!\n");
        return 0;
    }

    if (tracker->account_count == 0) {
        std::cout << " Please add an account first!\n");
        return 0;
    }

    Transaction *trans = &tracker->transactions[tracker->transaction_count];
    trans->id = tracker->transaction_count + 1;

    // Get current date
    get_current_date(trans->date);

    std::cout << "Enter description: ");
    scanf(" %[^\n]", trans->description);

    std::cout << "Enter category: ");
    scanf(" %[^\n]", trans->category);

    std::cout << "Transaction type:\n1. Income\n2. Expense\nEnter type (1-2): ");
    int type_choice = get_user_choice();
    trans->type = (type_choice == 1) ? INCOME : EXPENSE;

    std::cout << "Enter amount: $");
    trans->amount = get_positive_amount("");

    std::cout << "Select account:\n");
    display_accounts(tracker);
    std::cout << "Enter account ID: ");
    scanf("%d", &trans->account_id);

    if (find_account(tracker, trans->account_id) == -1) {
        std::cout << " Invalid account ID!\n");
        return 0;
    }

    // Update account balance
    update_account_balance(tracker, trans->account_id, trans->amount, trans->type);

    // Update budget if it's an expense
    if (trans->type == EXPENSE) {
        update_budget_spending(tracker, trans->category, trans->amount);
    }

    tracker->transaction_count++;
    std::cout << " Transaction added successfully!\n");
    return 1;
}

void display_transactions(const BudgetTracker *tracker, int limit) {
    if (tracker->transaction_count == 0) {
        std::cout << " No transactions found. Add your first transaction!\n");
        return;
    }

    int display_count = (limit > 0 && limit < tracker->transaction_count) ?
                       limit : tracker->transaction_count;

    std::cout << "\n Recent Transactions (showing %d of %d)\n", display_count, tracker->transaction_count);
    std::cout << "═══════════════════════════════════════════════════════════════════════════════\n");
    std::cout << "%-3s %-12s %-20s %-15s %-8s %-10s %-10s\n",
           "ID", "Date", "Description", "Category", "Type", "Amount", "Account");
    std::cout << "───────────────────────────────────────────────────────────────────────────────\n");

    for (int i = tracker->transaction_count - display_count; i < tracker->transaction_count; i++) {
        const Transaction *trans = &tracker->transactions[i];
        const char *type_str = (trans->type == INCOME) ? "Income" : "Expense";

        std::cout << "%-3d %-12s %-20s %-15s %-8s $%-9.2f %-10d\n",
               trans->id, trans->date, trans->description, trans->category,
               type_str, trans->amount, trans->account_id);
    }
}

void display_transaction_summary(const BudgetTracker *tracker) {
    double total_income = 0.0, total_expenses = 0.0;

    for (int i = 0; i < tracker->transaction_count; i++) {
        const Transaction *trans = &tracker->transactions[i];
        if (trans->type == INCOME) {
            total_income += trans->amount;
        } else {
            total_expenses += trans->amount;
        }
    }

    std::cout << "\n Financial Summary\n");
    std::cout << "═══════════════════════\n");
    std::cout << "Total Income:    $%.2f\n", total_income);
    std::cout << "Total Expenses:  $%.2f\n", total_expenses);
    std::cout << "Net Income:      $%.2f\n", total_income - total_expenses);
}

// Budget management
int set_budget_category(BudgetTracker *tracker) {
    if (tracker->budget_count >= MAX_CATEGORIES) {
        std::cout << " Maximum number of budget categories reached!\n");
        return 0;
    }

    BudgetCategory *budget = &tracker->budget[tracker->budget_count];

    std::cout << "Enter category name: ");
    scanf(" %[^\n]", budget->category);

    std::cout << "Enter budgeted amount: $");
    budget->budgeted_amount = get_positive_amount("");

    budget->spent_amount = 0.0;

    // Calculate current spending in this category
    for (int i = 0; i < tracker->transaction_count; i++) {
        const Transaction *trans = &tracker->transactions[i];
        if (trans->type == EXPENSE && strcmp(trans->category, budget->category) == 0) {
            budget->spent_amount += trans->amount;
        }
    }

    tracker->budget_count++;
    std::cout << " Budget category '%s' set successfully!\n", budget->category);
    return 1;
}

void display_budget_status(const BudgetTracker *tracker) {
    if (tracker->budget_count == 0) {
        std::cout << " No budget categories set. Create your first budget!\n");
        return;
    }

    std::cout << "\n Budget Status\n");
    std::cout << "═══════════════════════════════════════════════════════════════\n");
    std::cout << "%-20s %-12s %-12s %-12s %-10s\n", "Category", "Budgeted", "Spent", "Remaining", "Status");
    std::cout << "───────────────────────────────────────────────────────────────\n");

    for (int i = 0; i < tracker->budget_count; i++) {
        const BudgetCategory *budget = &tracker->budget[i];
        double remaining = budget->budgeted_amount - budget->spent_amount;
        double percent_used = (budget->spent_amount / budget->budgeted_amount) * 100.0;

        const char *status = (percent_used > 100.0) ? " Over" :
                           (percent_used > 80.0) ? "  High" : " Good";

        std::cout << "%-20s $%-11.2f $%-11.2f $%-11.2f %-10s\n",
               budget->category, budget->budgeted_amount, budget->spent_amount,
               remaining, status);
    }
}

void update_budget_spending(BudgetTracker *tracker, const char *category, double amount) {
    for (int i = 0; i < tracker->budget_count; i++) {
        if (strcmp(tracker->budget[i].category, category) == 0) {
            tracker->budget[i].spent_amount += amount;
            break;
        }
    }
}

// Goal management
int add_financial_goal(BudgetTracker *tracker) {
    if (tracker->goal_count >= 5) {
        std::cout << " Maximum number of goals reached!\n");
        return 0;
    }

    FinancialGoal *goal = &tracker->goals[tracker->goal_count];

    std::cout << "Enter goal description: ");
    scanf(" %[^\n]", goal->description);

    std::cout << "Enter target amount: $");
    goal->target_amount = get_positive_amount("");

    std::cout << "Enter target date (YYYY-MM-DD): ");
    scanf("%s", goal->target_date);

    goal->current_amount = 0.0;

    tracker->goal_count++;
    std::cout << " Goal '%s' added successfully!\n", goal->description);
    return 1;
}

void display_goals(const BudgetTracker *tracker) {
    if (tracker->goal_count == 0) {
        std::cout << " No goals set. Create your first financial goal!\n");
        return;
    }

    std::cout << "\n Your Financial Goals\n");
    std::cout << "═══════════════════════════════════════════════════════════════════════════════\n");
    std::cout << "%-25s %-12s %-12s %-12s %-10s\n", "Goal", "Target", "Current", "Remaining", "Progress");
    std::cout << "───────────────────────────────────────────────────────────────────────────────\n");

    for (int i = 0; i < tracker->goal_count; i++) {
        const FinancialGoal *goal = &tracker->goals[i];
        double remaining = goal->target_amount - goal->current_amount;
        double progress = calculate_goal_progress(goal);

        std::cout << "%-25s $%-11.2f $%-11.2f $%-11.2f %6.1f%%\n",
               goal->description, goal->target_amount, goal->current_amount,
               remaining, progress);
    }
}

double calculate_goal_progress(const FinancialGoal *goal) {
    if (goal->target_amount == 0.0) return 0.0;
    return (goal->current_amount / goal->target_amount) * 100.0;
}

// Utility functions
void get_current_date(char *date) {
    time_t t = time(NULL);
    struct tm *tm_info = localtime(&t);
    strftime(date, 11, "%Y-%m-%d", tm_info);
}

double get_positive_amount(const char *prompt) {
    double amount;
    do {
        scanf("%lf", &amount);
        if (amount <= 0) {
            std::cout << " Amount must be positive. Please enter again: $");
        }
    } while (amount <= 0);
    return amount;
}

void display_help(void) {
    clear_screen();
    std::cout << "╔══════════════════════════════════════════════╗\n");
    std::cout << "║                  HELP SYSTEM                 ║\n");
    std::cout << "╠══════════════════════════════════════════════╣\n");
    std::cout << "║ • Use the main menu to navigate features     ║\n");
    std::cout << "║ • Always save your data regularly           ║\n");
    std::cout << "║ • Set budgets to control spending           ║\n");
    std::cout << "║ • Track goals to achieve financial targets  ║\n");
    std::cout << "║ • Review reports to understand spending     ║\n");
    std::cout << "║ • Press Enter after each menu selection     ║\n");
    std::cout << "╚══════════════════════════════════════════════╝\n");
    pause();
}

// Data persistence (simplified - would be more robust in real application)
int save_data(const BudgetTracker *tracker) {
    FILE *file = fopen(tracker->data_file, "w");
    if (file == NULL) {
        std::cout << " Error saving data!\n");
        return 0;
    }

    // Save basic counts
    fprintf(file, "%d %d %d %d\n", tracker->account_count, tracker->transaction_count,
            tracker->budget_count, tracker->goal_count);

    // Save accounts
    for (int i = 0; i < tracker->account_count; i++) {
        const Account *acc = &tracker->accounts[i];
        fprintf(file, "%d %s %d %.2f %.2f\n", acc->id, acc->name, acc->type,
                acc->balance, acc->credit_limit);
    }

    // Save transactions
    for (int i = 0; i < tracker->transaction_count; i++) {
        const Transaction *trans = &tracker->transactions[i];
        fprintf(file, "%d %s %s %s %d %.2f %d\n", trans->id, trans->date,
                trans->description, trans->category, trans->type, trans->amount, trans->account_id);
    }

    // Save budget categories
    for (int i = 0; i < tracker->budget_count; i++) {
        const BudgetCategory *budget = &tracker->budget[i];
        fprintf(file, "%s %.2f %.2f\n", budget->category, budget->budgeted_amount, budget->spent_amount);
    }

    // Save goals
    for (int i = 0; i < tracker->goal_count; i++) {
        const FinancialGoal *goal = &tracker->goals[i];
        fprintf(file, "%s %.2f %.2f %s\n", goal->description, goal->target_amount,
                goal->current_amount, goal->target_date);
    }

    fclose(file);
    std::cout << " Data saved successfully!\n");
    return 1;
}

int load_data(BudgetTracker *tracker) {
    FILE *file = fopen(tracker->data_file, "r");
    if (file == NULL) {
        std::cout << " No existing data found. Starting fresh!\n");
        return 0;
    }

    // Load basic counts
    fscanf(file, "%d %d %d %d", &tracker->account_count, &tracker->transaction_count,
           &tracker->budget_count, &tracker->goal_count);

    // Load accounts
    for (int i = 0; i < tracker->account_count; i++) {
        Account *acc = &tracker->accounts[i];
        fscanf(file, "%d %s %d %lf %lf", &acc->id, acc->name, (int*)&acc->type,
               &acc->balance, &acc->credit_limit);
    }

    // Load transactions
    for (int i = 0; i < tracker->transaction_count; i++) {
        Transaction *trans = &tracker->transactions[i];
        fscanf(file, "%d %s %s %s %d %lf %d", &trans->id, trans->date,
               trans->description, trans->category, (int*)&trans->type, &trans->amount, &trans->account_id);
    }

    // Load budget categories
    for (int i = 0; i < tracker->budget_count; i++) {
        BudgetCategory *budget = &tracker->budget[i];
        fscanf(file, "%s %lf %lf", budget->category, &budget->budgeted_amount, &budget->spent_amount);
    }

    // Load goals
    for (int i = 0; i < tracker->goal_count; i++) {
        FinancialGoal *goal = &tracker->goals[i];
        fscanf(file, "%s %lf %lf %s", goal->description, &goal->target_amount,
               &goal->current_amount, goal->target_date);
    }

    fclose(file);
    std::cout << " Data loaded successfully!\n");
    return 1;
}
```

### Main Program (main.c)
```c
# include "budget_tracker.h"

int main() {
    BudgetTracker tracker;
    initialize_budget_tracker(&tracker, "budget_data.txt");

    int running = 1;
    while (running) {
        display_main_menu();
        int choice = get_user_choice();

        switch (choice) {
            case 1: { // View Dashboard
                clear_screen();
                std::cout << "╔══════════════════════════════════════════════╗\n");
                std::cout << "║               FINANCIAL DASHBOARD           ║\n");
                std::cout << "╚══════════════════════════════════════════════╝\n");

                display_accounts(&tracker);
                display_transaction_summary(&tracker);
                display_budget_status(&tracker);
                display_goals(&tracker);

                pause();
                break;
            }

            case 2: { // Manage Accounts
                int account_running = 1;
                while (account_running) {
                    display_accounts_menu();
                    int acc_choice = get_user_choice();

                    switch (acc_choice) {
                        case 1:
                            add_account(&tracker);
                            pause();
                            break;
                        case 2:
                            display_accounts(&tracker);
                            pause();
                            break;
                        case 3:
                            account_running = 0;
                            break;
                        default:
                            std::cout << " Invalid choice!\n");
                            pause();
                    }
                }
                break;
            }

            case 3: { // Manage Transactions
                int trans_running = 1;
                while (trans_running) {
                    display_transactions_menu();
                    int trans_choice = get_user_choice();

                    switch (trans_choice) {
                        case 1:
                            add_transaction(&tracker);
                            pause();
                            break;
                        case 2:
                            display_transactions(&tracker, 10);
                            pause();
                            break;
                        case 3:
                            // Edit transaction (simplified)
                            std::cout << "Edit transaction feature coming soon!\n");
                            pause();
                            break;
                        case 4:
                            // Delete transaction (simplified)
                            std::cout << "Delete transaction feature coming soon!\n");
                            pause();
                            break;
                        case 5:
                            trans_running = 0;
                            break;
                        default:
                            std::cout << " Invalid choice!\n");
                            pause();
                    }
                }
                break;
            }

            case 4: { // Budget Planning
                int budget_running = 1;
                while (budget_running) {
                    display_budget_menu();
                    int budget_choice = get_user_choice();

                    switch (budget_choice) {
                        case 1:
                            set_budget_category(&tracker);
                            pause();
                            break;
                        case 2:
                            display_budget_status(&tracker);
                            pause();
                            break;
                        case 3:
                            budget_running = 0;
                            break;
                        default:
                            std::cout << " Invalid choice!\n");
                            pause();
                    }
                }
                break;
            }

            case 5: { // Financial Goals
                int goal_running = 1;
                while (goal_running) {
                    display_goals_menu();
                    int goal_choice = get_user_choice();

                    switch (goal_choice) {
                        case 1:
                            add_financial_goal(&tracker);
                            pause();
                            break;
                        case 2:
                            display_goals(&tracker);
                            pause();
                            break;
                        case 3:
                            // Update goal progress (simplified)
                            std::cout << "Update goal progress feature coming soon!\n");
                            pause();
                            break;
                        case 4:
                            goal_running = 0;
                            break;
                        default:
                            std::cout << " Invalid choice!\n");
                            pause();
                    }
                }
                break;
            }

            case 6: { // Reports & Analytics
                int report_running = 1;
                while (report_running) {
                    display_reports_menu();
                    int report_choice = get_user_choice();

                    switch (report_choice) {
                        case 1:
                            generate_monthly_report(&tracker);
                            pause();
                            break;
                        case 2:
                            display_spending_by_category(&tracker);
                            pause();
                            break;
                        case 3:
                            display_income_vs_expenses(&tracker);
                            pause();
                            break;
                        case 4:
                            display_budget_vs_actual(&tracker);
                            pause();
                            break;
                        case 5:
                            report_running = 0;
                            break;
                        default:
                            std::cout << " Invalid choice!\n");
                            pause();
                    }
                }
                break;
            }

            case 7: { // Help
                display_help();
                break;
            }

            case 8: { // Save Data
                save_data(&tracker);
                pause();
                break;
            }

            case 9: { // Exit
                save_data(&tracker);
                std::cout << " Thank you for using Personal Budget Tracker!\n");
                running = 0;
                break;
            }

            default:
                std::cout << " Invalid choice! Please select 1-9.\n");
                pause();
        }
    }

    return 0;
}

// Report generation functions (simplified implementations)
void generate_monthly_report(const BudgetTracker *tracker) {
    std::cout << "\n Monthly Financial Report\n");
    std::cout << "═════════════════════════════\n");

    double total_income = 0.0, total_expenses = 0.0;
    int income_count = 0, expense_count = 0;

    for (int i = 0; i < tracker->transaction_count; i++) {
        const Transaction *trans = &tracker->transactions[i];
        if (trans->type == INCOME) {
            total_income += trans->amount;
            income_count++;
        } else {
            total_expenses += trans->amount;
            expense_count++;
        }
    }

    std::cout << "Income Transactions: %d ($%.2f)\n", income_count, total_income);
    std::cout << "Expense Transactions: %d ($%.2f)\n", expense_count, total_expenses);
    std::cout << "Net Income: $%.2f\n", total_income - total_expenses);
}

void display_spending_by_category(const BudgetTracker *tracker) {
    std::cout << "\n Spending by Category\n");
    std::cout << "═════════════════════════\n");

    // Simple implementation - would be more sophisticated in real app
    for (int i = 0; i < tracker->budget_count; i++) {
        const BudgetCategory *budget = &tracker->budget[i];
        std::cout << "%s: $%.2f spent of $%.2f budgeted\n",
               budget->category, budget->spent_amount, budget->budgeted_amount);
    }
}

void display_income_vs_expenses(const BudgetTracker *tracker) {
    std::cout << "\n Income vs Expenses\n");
    std::cout << "═══════════════════════\n");

    double total_income = 0.0, total_expenses = 0.0;

    for (int i = 0; i < tracker->transaction_count; i++) {
        const Transaction *trans = &tracker->transactions[i];
        if (trans->type == INCOME) {
            total_income += trans->amount;
        } else {
            total_expenses += trans->amount;
        }
    }

    std::cout << "Total Income: $%.2f\n", total_income);
    std::cout << "Total Expenses: $%.2f\n", total_expenses);
    std::cout << "Difference: $%.2f\n", total_income - total_expenses);
}

void display_budget_vs_actual(const BudgetTracker *tracker) {
    std::cout << "\n Budget vs Actual\n");
    std::cout << "═════════════════════\n");

    display_budget_status(tracker);
}
```

---

## Testing the Application

### Compilation Instructions
```
# Compile the program
g++ -o budget_tracker main.c budget_tracker.c

# Run the program
./budget_tracker
```

### Test Scenarios
1. **Setup**: Add a checking account with $1000 balance
2. **Transactions**: Add income and expense transactions
3. **Budgeting**: Set budget categories and monitor spending
4. **Goals**: Create financial goals and track progress
5. **Reports**: Generate various financial reports
6. **Persistence**: Save and reload data

### Sample Usage Flow
```
=== Main Menu ===
1.  View Dashboard
2.  Manage Accounts
...
Enter your choice (1-9): 2

 Account Management
1. Add Account
2. View Accounts
3. Back to Main Menu
Enter choice: 1
Enter account name: My Checking
Account type:
1. Checking
2. Savings
3. Credit Card
4. Investment
Enter type (1-4): 1
Enter starting balance: $1000
 Account 'My Checking' added successfully!
```

---

## Code Explanation

### Key Features Implemented

**Multi-Level Menus:**
- [ ] Hierarchical navigation system
- [ ] Context-aware sub-menus
- [ ] Consistent user interface design

**Data Persistence:**
- [ ] File-based data storage
- [ ] Automatic save on exit
- [ ] Data validation on load

**Real-Time Updates:**
- [ ] Balance calculations after transactions
- [ ] Budget tracking with spending updates
- [ ] Goal progress monitoring

**User Experience:**
- [ ] Clear visual formatting with borders
- [ ] Helpful error messages and validation
- [ ] Progress indicators and status updates

---

## Enhancements to Try

### Beginner Enhancements
1. **Transaction Editing**: Full edit/delete functionality
2. **Date Filtering**: Filter transactions by date range
3. **Category Management**: Add/edit/delete categories

### Intermediate Enhancements
1. **Advanced Reports**: Charts and graphs (text-based)
2. **Recurring Transactions**: Automatic monthly bills
3. **Account Transfers**: Move money between accounts

### Advanced Enhancements
1. **Multi-User Support**: Different user profiles
2. **Financial Projections**: Future balance predictions
3. **Import/Export**: CSV import/export functionality
4. **Mobile Interface**: Web-based interface

---

## Success Checklist

**Interactive Features:**
- [x] **Multi-Level Menus**: Hierarchical navigation system
- [x] **Real-Time Feedback**: Immediate response to user actions
- [x] **Input Validation**: Comprehensive error checking
- [x] **Data Persistence**: Save and load user data
- [x] **User Guidance**: Help system and clear instructions
- [x] **Progress Tracking**: Visual progress indicators

**Application Features:**
- [x] **Account Management**: Multiple account types and balances
- [x] **Transaction Processing**: Income/expense tracking
- [x] **Budget System**: Category-based spending limits
- [x] **Goal Tracking**: Financial target monitoring
- [x] **Report Generation**: Financial summaries and analytics
- [x] **Professional UI**: Clean, intuitive interface

---

## Learning Outcomes

**Technical Skills:**
- [ ] Complex user interface design
- [ ] Multi-level application architecture
- [ ] Advanced data persistence
- [ ] Real-time data processing
- [ ] User experience optimization
- [ ] Error handling and recovery

**Problem-Solving Skills:**
- [ ] Application workflow design
- [ ] User interaction modeling
- [ ] Data relationship management
- [ ] Feature prioritization
- [ ] Scalable architecture planning

---

## Code Walkthrough

### Application Flow
```
Start → Load Data → Main Menu Loop → Feature Selection → Sub-Menu Navigation
   ↓         ↓            ↓              ↓                ↓
Initialize  File I/O    User Choice   Process Request  Context Menus
Structures  Operations  Validation    Execute Action   User Input
```

### Data Management
```
User Actions → Input Validation → Data Processing → Storage Update → UI Refresh
     ↓              ↓                ↓              ↓            ↓
Menu Selection  Constraint  Business Logic  File I/O    Display Update
and Input       Checking    Calculations    Operations  Results
```

---

<div style="page-break-after: always;"></div>

---

## Implementation Notes

### Design Decisions
- [ ] **Hierarchical Menus**: Clear navigation structure
- [ ] **Persistent Storage**: Text file format for simplicity
- [ ] **Real-Time Updates**: Immediate calculation of balances and budgets
- [ ] **User-Friendly**: Visual formatting and helpful messages

### User Experience Focus
- [ ] **Consistent Interface**: Similar menu patterns throughout
- [ ] **Clear Feedback**: Success/error messages for all actions
- [ ] **Progressive Disclosure**: Show information as needed
- [ ] **Error Recovery**: Allow users to correct mistakes

### Data Integrity
- [ ] **Validation**: Check all user inputs for validity
- [ ] **Atomic Operations**: Complete transactions or rollback
- [ ] **Backup Safety**: Save data before major operations
- [ ] **Recovery**: Load last good state on startup

---

 **Congratulations! You've built a professional interactive application!** 

*Next: Decision support applications with intelligent recommendations! *

### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim


### Additional Content

Understand the key concepts:

- [ ] Review each function
- [ ] Understand the flow
- [ ] Learn the patterns used


### Code Review

Key functions and their purpose:

- [ ] Main function: Entry point
- [ ] Helper functions: Support logic


### <div style="page-break-after: always;"></div>

Answer Key

Expected implementation provided.

<div style="page-break-after: always;"></div>

---

## Answer Key

### Complete Solution

```
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard C++ conventions with proper imports and main function
2. **Output**: Uses std::cout to print messages to the console
3. **Standard Library**: Includes iostream for input/output operations
4. **Return Value**: Returns 0 to indicate successful execution
5. **Best Practices**: Code is readable and uses C++ idioms

### Testing Your Solution

1. **Compile**: `g++ hello.cpp -o hello`
2. **Run**: `./hello`
3. **Expected Output**: `Hello, World!`

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `command not found: g++` | Compiler not installed | `sudo apt install g++` (Ubuntu) |
| `undefined reference to main` | Missing main function | Ensure `int main()` exists |
| `error: unknown type name 'cout'` | Missing iostream | Add `#include <iostream>` |

### Tips for Learning

- C++ is a superset of C with additional features
- `std::cout` is the C++ way to print (replaces `printf`)
- `std::endl` adds a newline and flushes the buffer
- The `std::` prefix means these are from the "standard" namespace
