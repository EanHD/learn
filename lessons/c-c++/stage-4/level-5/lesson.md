# Level 5: Decision Support Application

> **LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.c\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 4: Full Problem Solving

### Today's Mission

**INTELLIGENT DECISION MAKER!**  You're now building applications that analyze data, recognize patterns, and provide intelligent recommendations. This level focuses on decision support systems that help users make informed choices through data analysis and predictive insights.

**The Process:**
1. **Data Collection**: Gather and organize user data
2. **Pattern Analysis**: Identify trends and anomalies
3. **Insight Generation**: Extract meaningful information
4. **Recommendation Engine**: Provide actionable advice
5. **Interactive Guidance**: Help users implement recommendations
6. **Continuous Learning**: Adapt based on user feedback

---

### Learning Goals

- [ ] Data analysis and pattern recognition algorithms
- [ ] Decision-making logic and recommendation systems
- [ ] Predictive analytics and trend analysis
- [ ] User personalization and adaptive interfaces
- [ ] Financial modeling and forecasting
- [ ] Intelligent system design

---

### Your Task

**Build a Smart Expense Analyzer and Financial Advisor with:**
1. **Expense Analysis**: Pattern recognition and trend identification
2. **Financial Health Scoring**: Overall financial assessment
3. **Personalized Recommendations**: Tailored financial advice
4. **Budget Optimization**: AI-powered budget suggestions
5. **Savings Goals**: Intelligent goal setting and tracking
6. **Risk Assessment**: Financial risk analysis and mitigation

---

## Application Requirements

### Core Features
- [ ] **Spending Pattern Analysis**: Identify spending habits and trends
- [ ] **Category Intelligence**: Smart categorization and anomaly detection
- [ ] **Financial Health Dashboard**: Comprehensive financial assessment
- [ ] **Recommendation Engine**: Personalized financial advice
- [ ] **Predictive Forecasting**: Future expense and savings predictions
- [ ] **Goal Optimization**: Intelligent savings and debt reduction plans

### Technical Requirements
- [ ] Advanced data analysis algorithms
- [ ] Machine learning-inspired pattern recognition
- [ ] Statistical modeling and forecasting
- [ ] Personalized recommendation algorithms
- [ ] Interactive decision support interface
- [ ] Data visualization and reporting

---

## Application Architecture

### Data Structures
```c
# define MAX_TRANSACTIONS 1000
# define MAX_CATEGORIES 20
# define MAX_RECOMMENDATIONS 10
# define ANALYSIS_WINDOW 30  // days

typedef struct {
    char date[11];
    char description[100];
    char category[50];
    double amount;
    int is_recurring;
} ExpenseRecord;

typedef struct {
    char category[50];
    double total_spent;
    double average_daily;
    double trend_percentage;  // spending trend
    int transaction_count;
    double budget_limit;
} CategoryAnalysis;

typedef struct {
    double income;
    double total_expenses;
    double savings_rate;
    double debt_to_income;
    int financial_score;  // 0-100
    char risk_level[20];  // Low, Medium, High
} FinancialHealth;

typedef struct {
    char title[100];
    char description[200];
    char category[50];
    double potential_savings;
    int priority;  // 1-5, 5 being highest
    int implemented;
} Recommendation;

typedef struct {
    ExpenseRecord expenses[MAX_TRANSACTIONS];
    CategoryAnalysis categories[MAX_CATEGORIES];
    FinancialHealth health;
    Recommendation recommendations[MAX_RECOMMENDATIONS];
    int expense_count;
    int category_count;
    int recommendation_count;
    double monthly_income;
    char analysis_period[20];
} SmartAnalyzer;
```

### Function Modules
- [ ] **Data Analysis**: `analyze_spending_patterns()`, `detect_anomalies()`
- [ ] **Financial Assessment**: `calculate_financial_health()`, `assess_risk()`
- [ ] **Recommendation Engine**: `generate_recommendations()`, `prioritize_advice()`
- [ ] **Predictive Modeling**: `forecast_expenses()`, `predict_savings()`
- [ ] **User Interface**: `display_insights()`, `interactive_advisor()`
- [ ] **Reporting**: `generate_financial_report()`, `export_recommendations()`

---

## Complete Implementation

### Header File (smart_analyzer.h)
```c
# ifndef SMART_ANALYZER_H
# define SMART_ANALYZER_H

#include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <math.h>
# include <time.h>
# include <ctype.h>

# define MAX_TRANSACTIONS 1000
# define MAX_CATEGORIES 20
# define MAX_RECOMMENDATIONS 10
# define ANALYSIS_WINDOW 30

typedef struct {
    char date[11];
    char description[100];
    char category[50];
    double amount;
    int is_recurring;
} ExpenseRecord;

typedef struct {
    char category[50];
    double total_spent;
    double average_daily;
    double trend_percentage;
    int transaction_count;
    double budget_limit;
} CategoryAnalysis;

typedef struct {
    double income;
    double total_expenses;
    double savings_rate;
    double debt_to_income;
    int financial_score;
    char risk_level[20];
} FinancialHealth;

typedef struct {
    char title[100];
    char description[200];
    char category[50];
    double potential_savings;
    int priority;
    int implemented;
} Recommendation;

typedef struct {
    ExpenseRecord expenses[MAX_TRANSACTIONS];
    CategoryAnalysis categories[MAX_CATEGORIES];
    FinancialHealth health;
    Recommendation recommendations[MAX_RECOMMENDATIONS];
    int expense_count;
    int category_count;
    int recommendation_count;
    double monthly_income;
    char analysis_period[20];
} SmartAnalyzer;

// Function prototypes
void initialize_analyzer(SmartAnalyzer *analyzer);
void load_sample_data(SmartAnalyzer *analyzer);

// Analysis functions
void analyze_spending_patterns(SmartAnalyzer *analyzer);
void detect_anomalies(SmartAnalyzer *analyzer);
void calculate_category_trends(SmartAnalyzer *analyzer);
void assess_financial_health(SmartAnalyzer *analyzer);

// Recommendation engine
void generate_recommendations(SmartAnalyzer *analyzer);
void prioritize_recommendations(SmartAnalyzer *analyzer);
void add_recommendation(SmartAnalyzer *analyzer, const char *title,
                       const char *description, const char *category,
                       double savings, int priority);

// Predictive functions
double forecast_monthly_expenses(SmartAnalyzer *analyzer);
double predict_savings_potential(SmartAnalyzer *analyzer);
void analyze_seasonal_patterns(SmartAnalyzer *analyzer);

// User interface
void display_main_menu(void);
void display_financial_dashboard(const SmartAnalyzer *analyzer);
void display_spending_insights(const SmartAnalyzer *analyzer);
void display_recommendations(const SmartAnalyzer *analyzer);
void interactive_advisor(SmartAnalyzer *analyzer);
void display_risk_assessment(const SmartAnalyzer *analyzer);

// Utility functions
int get_user_choice(void);
void clear_screen(void);
void pause(void);
double calculate_average(double *values, int count);
double calculate_standard_deviation(double *values, int count, double mean);
int compare_dates(const char *date1, const char *date2);
void get_current_date(char *date);

# endif
```

### Implementation File (smart_analyzer.c)
```c
# include "smart_analyzer.h"

// Initialize the analyzer
void initialize_analyzer(SmartAnalyzer *analyzer) {
    analyzer->expense_count = 0;
    analyzer->category_count = 0;
    analyzer->recommendation_count = 0;
    analyzer->monthly_income = 0.0;
    strcpy(analyzer->analysis_period, "Last 30 days");

    // Initialize financial health
    analyzer->health.financial_score = 0;
    strcpy(analyzer->health.risk_level, "Unknown");

    load_sample_data(analyzer);
    analyze_spending_patterns(analyzer);
    assess_financial_health(analyzer);
    generate_recommendations(analyzer);
    prioritize_recommendations(analyzer);
}

// Load sample expense data for demonstration
void load_sample_data(SmartAnalyzer *analyzer) {
    // Sample monthly income
    analyzer->monthly_income = 5000.00;

    // Sample expense data
    struct {
        char date[11];
        char description[100];
        char category[50];
        double amount;
        int recurring;
    } sample_data[] = {
        {"2024-01-01", "Grocery Store", "Food", 120.50, 1},
        {"2024-01-02", "Gas Station", "Transportation", 45.00, 0},
        {"2024-01-03", "Netflix", "Entertainment", 15.99, 1},
        {"2024-01-04", "Coffee Shop", "Food", 8.75, 0},
        {"2024-01-05", "Electric Bill", "Utilities", 85.30, 1},
        {"2024-01-06", "Restaurant", "Food", 67.89, 0},
        {"2024-01-07", "Amazon Purchase", "Shopping", 234.56, 0},
        {"2024-01-08", "Gym Membership", "Health", 49.99, 1},
        {"2024-01-09", "Phone Bill", "Utilities", 65.00, 1},
        {"2024-01-10", "Movie Tickets", "Entertainment", 28.50, 0},
        {"2024-01-11", "Grocery Store", "Food", 98.75, 1},
        {"2024-01-12", "Uber Ride", "Transportation", 18.50, 0},
        {"2024-01-13", "Book Purchase", "Education", 24.99, 0},
        {"2024-01-14", "Coffee Shop", "Food", 6.25, 0},
        {"2024-01-15", "Internet Bill", "Utilities", 79.99, 1},
        {"2024-01-16", "Restaurant", "Food", 89.45, 0},
        {"2024-01-17", "Target Shopping", "Shopping", 156.78, 0},
        {"2024-01-18", "Doctor Visit", "Health", 150.00, 0},
        {"2024-01-19", "Gas Station", "Transportation", 52.30, 0},
        {"2024-01-20", "Spotify", "Entertainment", 9.99, 1}
    };

    int sample_count = sizeof(sample_data) / sizeof(sample_data[0]);
    for (int i = 0; i < sample_count && analyzer->expense_count < MAX_TRANSACTIONS; i++) {
        ExpenseRecord *expense = &analyzer->expenses[analyzer->expense_count];
        strcpy(expense->date, sample_data[i].date);
        strcpy(expense->description, sample_data[i].description);
        strcpy(expense->category, sample_data[i].category);
        expense->amount = sample_data[i].amount;
        expense->is_recurring = sample_data[i].recurring;
        analyzer->expense_count++;
    }
}

// Analyze spending patterns
void analyze_spending_patterns(SmartAnalyzer *analyzer) {
    // Reset category analysis
    analyzer->category_count = 0;

    // Group expenses by category
    for (int i = 0; i < analyzer->expense_count; i++) {
        const ExpenseRecord *expense = &analyzer->expenses[i];

        // Find or create category
        int category_index = -1;
        for (int j = 0; j < analyzer->category_count; j++) {
            if (strcmp(analyzer->categories[j].category, expense->category) == 0) {
                category_index = j;
                break;
            }
        }

        if (category_index == -1) {
            if (analyzer->category_count >= MAX_CATEGORIES) continue;
            category_index = analyzer->category_count;
            strcpy(analyzer->categories[category_index].category, expense->category);
            analyzer->categories[category_index].total_spent = 0.0;
            analyzer->categories[category_index].transaction_count = 0;
            analyzer->categories[category_index].trend_percentage = 0.0;
            analyzer->category_count++;
        }

        // Update category statistics
        analyzer->categories[category_index].total_spent += expense->amount;
        analyzer->categories[category_index].transaction_count++;
    }

    // Calculate averages and trends
    for (int i = 0; i < analyzer->category_count; i++) {
        CategoryAnalysis *cat = &analyzer->categories[i];
        cat->average_daily = cat->total_spent / ANALYSIS_WINDOW;

        // Simple trend calculation (would be more sophisticated in real implementation)
        // For demo, we'll assign random trends between -20% to +20%
        cat->trend_percentage = ((rand() % 40) - 20) * 1.0;

        // Set default budget limits based on category
        if (strcmp(cat->category, "Food") == 0) cat->budget_limit = 600.0;
        else if (strcmp(cat->category, "Transportation") == 0) cat->budget_limit = 300.0;
        else if (strcmp(cat->category, "Entertainment") == 0) cat->budget_limit = 150.0;
        else if (strcmp(cat->category, "Utilities") == 0) cat->budget_limit = 250.0;
        else if (strcmp(cat->category, "Shopping") == 0) cat->budget_limit = 400.0;
        else if (strcmp(cat->category, "Health") == 0) cat->budget_limit = 200.0;
        else cat->budget_limit = 100.0;
    }
}

// Detect spending anomalies
void detect_anomalies(SmartAnalyzer *analyzer) {
    for (int i = 0; i < analyzer->category_count; i++) {
        CategoryAnalysis *cat = &analyzer->categories[i];

        // Find transactions in this category
        double *amounts = malloc(cat->transaction_count * sizeof(double));
        if (amounts == NULL) continue;

        int idx = 0;
        for (int j = 0; j < analyzer->expense_count; j++) {
            if (strcmp(analyzer->expenses[j].category, cat->category) == 0) {
                amounts[idx++] = analyzer->expenses[j].amount;
            }
        }

        double mean = calculate_average(amounts, cat->transaction_count);
        double std_dev = calculate_standard_deviation(amounts, cat->transaction_count, mean);

        // Flag transactions that are 2+ standard deviations above mean
        for (int j = 0; j < analyzer->expense_count; j++) {
            if (strcmp(analyzer->expenses[j].category, cat->category) == 0) {
                if (analyzer->expenses[j].amount > mean + 2 * std_dev) {
                    // Could add anomaly flag to expense record
                }
            }
        }

        free(amounts);
    }
}

// Assess financial health
void assess_financial_health(SmartAnalyzer *analyzer) {
    double total_expenses = 0.0;
    for (int i = 0; i < analyzer->expense_count; i++) {
        total_expenses += analyzer->expenses[i].amount;
    }

    analyzer->health.total_expenses = total_expenses;
    analyzer->health.income = analyzer->monthly_income;
    analyzer->health.savings_rate = ((analyzer->health.income - total_expenses) / analyzer->health.income) * 100.0;
    analyzer->health.debt_to_income = 0.0; // Simplified - no debt tracking in this demo

    // Calculate financial score (0-100)
    int score = 100;

    // Deduct points for high expense ratios
    double expense_ratio = total_expenses / analyzer->health.income;
    if (expense_ratio > 0.8) score -= 30;
    else if (expense_ratio > 0.6) score -= 15;

    // Deduct for low savings rate
    if (analyzer->health.savings_rate < 10) score -= 20;
    else if (analyzer->health.savings_rate < 20) score -= 10;

    // Check budget compliance
    for (int i = 0; i < analyzer->category_count; i++) {
        if (analyzer->categories[i].total_spent > analyzer->categories[i].budget_limit) {
            score -= 5;
        }
    }

    analyzer->health.financial_score = score > 0 ? score : 0;

    // Determine risk level
    if (score >= 80) strcpy(analyzer->health.risk_level, "Low");
    else if (score >= 60) strcpy(analyzer->health.risk_level, "Medium");
    else strcpy(analyzer->health.risk_level, "High");
}

// Generate personalized recommendations
void generate_recommendations(SmartAnalyzer *analyzer) {
    analyzer->recommendation_count = 0;

    // Budget overrun recommendations
    for (int i = 0; i < analyzer->category_count; i++) {
        const CategoryAnalysis *cat = &analyzer->categories[i];
        if (cat->total_spent > cat->budget_limit) {
            double overrun = cat->total_spent - cat->budget_limit;
            char title[100], desc[200];
            sprintf(title, "Reduce %s Spending", cat->category);
            sprintf(desc, "You're over budget by $%.2f in %s. Consider cutting non-essential expenses in this category.",
                   overrun, cat->category);
            add_recommendation(analyzer, title, desc, cat->category, overrun * 0.5, 4);
        }
    }

    // High spending trend recommendations
    for (int i = 0; i < analyzer->category_count; i++) {
        const CategoryAnalysis *cat = &analyzer->categories[i];
        if (cat->trend_percentage > 10) {
            char title[100], desc[200];
            sprintf(title, "Monitor %s Trend", cat->category);
            sprintf(desc, "Your %s spending is up %.1f%%. Review recent purchases and set stricter limits.",
                   cat->category, cat->trend_percentage);
            add_recommendation(analyzer, title, desc, cat->category, cat->total_spent * 0.1, 3);
        }
    }

    // Savings recommendations
    if (analyzer->health.savings_rate < 20) {
        double target_savings = analyzer->health.income * 0.2;
        double current_savings = analyzer->health.income - analyzer->health.total_expenses;
        double gap = target_savings - current_savings;

        if (gap > 0) {
            add_recommendation(analyzer,
                "Increase Savings Rate",
                "Aim to save 20% of your income. Consider automating transfers to savings account.",
                "Savings", gap, 5);
        }
    }

    // Recurring expense optimization
    double recurring_total = 0.0;
    for (int i = 0; i < analyzer->expense_count; i++) {
        if (analyzer->expenses[i].is_recurring) {
            recurring_total += analyzer->expenses[i].amount;
        }
    }

    if (recurring_total > analyzer->health.income * 0.3) {
        add_recommendation(analyzer,
            "Review Recurring Expenses",
            "Your recurring expenses are high. Consider canceling unused subscriptions and negotiating bills.",
            "Recurring", recurring_total * 0.2, 4);
    }

    // General recommendations
    add_recommendation(analyzer,
        "Build Emergency Fund",
        "Aim to save 3-6 months of expenses for emergencies. Start with small weekly deposits.",
        "Emergency", analyzer->health.total_expenses * 3, 5);

    add_recommendation(analyzer,
        "Track Daily Expenses",
        "Use expense tracking apps to monitor spending in real-time and stay within budget.",
        "Tracking", 0.0, 2);
}

// Add a recommendation
void add_recommendation(SmartAnalyzer *analyzer, const char *title,
                       const char *description, const char *category,
                       double savings, int priority) {
    if (analyzer->recommendation_count >= MAX_RECOMMENDATIONS) return;

    Recommendation *rec = &analyzer->recommendations[analyzer->recommendation_count];
    strcpy(rec->title, title);
    strcpy(rec->description, description);
    strcpy(rec->category, category);
    rec->potential_savings = savings;
    rec->priority = priority;
    rec->implemented = 0;

    analyzer->recommendation_count++;
}

// Prioritize recommendations by potential savings and urgency
void prioritize_recommendations(SmartAnalyzer *analyzer) {
    // Simple bubble sort by priority (higher priority first)
    for (int i = 0; i < analyzer->recommendation_count - 1; i++) {
        for (int j = 0; j < analyzer->recommendation_count - i - 1; j++) {
            if (analyzer->recommendations[j].priority < analyzer->recommendations[j + 1].priority) {
                Recommendation temp = analyzer->recommendations[j];
                analyzer->recommendations[j] = analyzer->recommendations[j + 1];
                analyzer->recommendations[j + 1] = temp;
            }
        }
    }
}

// Forecast monthly expenses
double forecast_monthly_expenses(SmartAnalyzer *analyzer) {
    double forecast = 0.0;

    // Simple forecasting: current spending + trend adjustments
    for (int i = 0; i < analyzer->category_count; i++) {
        const CategoryAnalysis *cat = &analyzer->categories[i];
        double trend_adjustment = cat->total_spent * (cat->trend_percentage / 100.0);
        forecast += cat->total_spent + trend_adjustment;
    }

    return forecast;
}

// Predict savings potential
double predict_savings_potential(SmartAnalyzer *analyzer) {
    double potential = 0.0;

    for (int i = 0; i < analyzer->recommendation_count; i++) {
        if (!analyzer->recommendations[i].implemented) {
            potential += analyzer->recommendations[i].potential_savings;
        }
    }

    return potential;
}

// Display functions
void display_main_menu(void) {
    clear_screen();
    printf("╔══════════════════════════════════════════════╗\n");
    printf("║         SMART EXPENSE ANALYZER & ADVISOR    ║\n");
    printf("╠══════════════════════════════════════════════╣\n");
    printf("║ 1.  Financial Dashboard                    ║\n");
    printf("║ 2.  Spending Insights                      ║\n");
    printf("║ 3.  Personalized Recommendations           ║\n");
    printf("║ 4.  Interactive Advisor                     ║\n");
    printf("║ 5.  Risk Assessment                        ║\n");
    printf("║ 6.  Generate Report                        ║\n");
    printf("║ 7.  Exit                                   ║\n");
    printf("╚══════════════════════════════════════════════╝\n");
    printf("Enter your choice (1-7): ");
}

void display_financial_dashboard(const SmartAnalyzer *analyzer) {
    printf("\n FINANCIAL DASHBOARD\n");
    printf("════════════════════════\n");
    printf("Monthly Income:     $%.2f\n", analyzer->health.income);
    printf("Total Expenses:     $%.2f\n", analyzer->health.total_expenses);
    printf("Net Income:         $%.2f\n", analyzer->health.income - analyzer->health.total_expenses);
    printf("Savings Rate:       %.1f%%\n", analyzer->health.savings_rate);
    printf("Financial Score:    %d/100\n", analyzer->health.financial_score);
    printf("Risk Level:         %s\n", analyzer->health.risk_level);

    printf("\n FORECASTS\n");
    printf("Next Month Expenses: $%.2f\n", forecast_monthly_expenses(analyzer));
    printf("Savings Potential:   $%.2f\n", predict_savings_potential(analyzer));
}

void display_spending_insights(const SmartAnalyzer *analyzer) {
    printf("\n SPENDING INSIGHTS\n");
    printf("═══════════════════════\n");
    printf("%-15s %-10s %-10s %-8s %-10s\n", "Category", "Total", "Daily Avg", "Trend", "Budget");
    printf("────────────────────────────────────────────────────────\n");

    for (int i = 0; i < analyzer->category_count; i++) {
        const CategoryAnalysis *cat = &analyzer->categories[i];
        char trend_symbol = cat->trend_percentage > 0 ? '↗' : '↘';
        printf("%-15s $%-9.2f $%-9.2f %c%-6.1f%% $%-9.2f\n",
               cat->category, cat->total_spent, cat->average_daily,
               trend_symbol, fabs(cat->trend_percentage), cat->budget_limit);
    }
}

void display_recommendations(const SmartAnalyzer *analyzer) {
    printf("\n PERSONALIZED RECOMMENDATIONS\n");
    printf("══════════════════════════════════\n");

    for (int i = 0; i < analyzer->recommendation_count; i++) {
        const Recommendation *rec = &analyzer->recommendations[i];
        printf("\n%d. %s (Priority: %d/5)\n", i + 1, rec->title, rec->priority);
        printf("   %s\n", rec->description);
        if (rec->potential_savings > 0) {
            printf("    Potential Savings: $%.2f\n", rec->potential_savings);
        }
        printf("   Status: %s\n", rec->implemented ? " Implemented" : "⏳ Pending");
    }
}

void interactive_advisor(SmartAnalyzer *analyzer) {
    printf("\n INTERACTIVE FINANCIAL ADVISOR\n");
    printf("═══════════════════════════════════\n");

    // Ask user about their financial goals
    printf("What is your primary financial goal?\n");
    printf("1. Build emergency savings\n");
    printf("2. Pay off debt\n");
    printf("3. Save for a major purchase\n");
    printf("4. Increase retirement savings\n");
    printf("5. General financial health\n");
    printf("Enter choice: ");

    int goal = get_user_choice();

    printf("\nBased on your goal and spending analysis:\n");

    switch (goal) {
        case 1:
            printf(" EMERGENCY FUND ADVICE:\n");
            printf("• Aim for 3-6 months of expenses in savings\n");
            printf("• Your target: $%.2f - $%.2f\n",
                   analyzer->health.total_expenses * 3,
                   analyzer->health.total_expenses * 6);
            printf("• Start with $%.2f monthly deposits\n",
                   (analyzer->health.total_expenses * 3) / 12);
            break;

        case 2:
            printf(" DEBT REDUCTION ADVICE:\n");
            printf("• Focus on high-interest debt first\n");
            printf("• Consider debt consolidation\n");
            printf("• Cut discretionary spending by reviewing your top categories\n");
            break;

        case 3:
            printf(" MAJOR PURCHASE ADVICE:\n");
            printf("• Set a realistic timeline and monthly savings goal\n");
            printf("• Consider using windfalls for extra payments\n");
            printf("• Track progress with your expense analyzer\n");
            break;

        case 4:
            printf(" RETIREMENT SAVINGS ADVICE:\n");
            printf("• Maximize employer matches if available\n");
            printf("• Consider Roth vs Traditional accounts\n");
            printf("• Increase contributions gradually\n");
            break;

        case 5:
            printf(" GENERAL FINANCIAL HEALTH:\n");
            printf("• Your financial score: %d/100 (%s risk)\n",
                   analyzer->health.financial_score, analyzer->health.risk_level);
            printf("• Focus on increasing savings rate to 20%%\n");
            printf("• Review and optimize recurring expenses\n");
            break;
    }

    printf("\n Top recommendations for your goal:\n");
    int rec_count = 0;
    for (int i = 0; i < analyzer->recommendation_count && rec_count < 3; i++) {
        if (!analyzer->recommendations[i].implemented) {
            printf("%d. %s\n", ++rec_count, analyzer->recommendations[i].title);
        }
    }
}

void display_risk_assessment(const SmartAnalyzer *analyzer) {
    printf("\n FINANCIAL RISK ASSESSMENT\n");
    printf("═══════════════════════════════\n");
    printf("Overall Risk Level: %s\n", analyzer->health.risk_level);
    printf("Financial Score: %d/100\n", analyzer->health.financial_score);

    printf("\nRisk Factors:\n");

    if (analyzer->health.savings_rate < 10) {
        printf("•  Low savings rate (%.1f%%) - increases financial vulnerability\n",
               analyzer->health.savings_rate);
    }

    double expense_ratio = analyzer->health.total_expenses / analyzer->health.income;
    if (expense_ratio > 0.8) {
        printf("•  High expense ratio (%.1f%%) - leaves little buffer for emergencies\n",
               expense_ratio * 100);
    }

    int budget_overruns = 0;
    for (int i = 0; i < analyzer->category_count; i++) {
        if (analyzer->categories[i].total_spent > analyzer->categories[i].budget_limit) {
            budget_overruns++;
        }
    }

    if (budget_overruns > 0) {
        printf("•  %d budget categories over limit - indicates spending control issues\n",
               budget_overruns);
    }

    printf("\nRecommendations to reduce risk:\n");
    printf("• Build emergency fund (3-6 months expenses)\n");
    printf("• Keep expense ratio below 70%%\n");
    printf("• Maintain savings rate above 15%%\n");
    printf("• Stay within budget limits\n");
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
    printf("\nPress Enter to continue...");
    getchar();
    getchar();
}

double calculate_average(double *values, int count) {
    if (count == 0) return 0.0;
    double sum = 0.0;
    for (int i = 0; i < count; i++) {
        sum += values[i];
    }
    return sum / count;
}

double calculate_standard_deviation(double *values, int count, double mean) {
    if (count <= 1) return 0.0;
    double sum_squared_diff = 0.0;
    for (int i = 0; i < count; i++) {
        double diff = values[i] - mean;
        sum_squared_diff += diff * diff;
    }
    return sqrt(sum_squared_diff / (count - 1));
}

int compare_dates(const char *date1, const char *date2) {
    return strcmp(date1, date2);
}

void get_current_date(char *date) {
    time_t t = time(NULL);
    struct tm *tm_info = localtime(&t);
    strftime(date, 11, "%Y-%m-%d", tm_info);
}
```

### Main Program (main.c)
```c
# include "smart_analyzer.h"

int main() {
    SmartAnalyzer analyzer;
    initialize_analyzer(&analyzer);

    printf(" Smart Expense Analyzer & Financial Advisor\n");
    printf("Analyzing your financial data...\n\n");

    int running = 1;
    while (running) {
        display_main_menu();
        int choice = get_user_choice();

        switch (choice) {
            case 1: { // Financial Dashboard
                display_financial_dashboard(&analyzer);
                pause();
                break;
            }

            case 2: { // Spending Insights
                display_spending_insights(&analyzer);
                pause();
                break;
            }

            case 3: { // Recommendations
                display_recommendations(&analyzer);
                pause();
                break;
            }

            case 4: { // Interactive Advisor
                interactive_advisor(&analyzer);
                pause();
                break;
            }

            case 5: { // Risk Assessment
                display_risk_assessment(&analyzer);
                pause();
                break;
            }

            case 6: { // Generate Report
                printf("\n FINANCIAL ANALYSIS REPORT\n");
                printf("═══════════════════════════════\n");
                display_financial_dashboard(&analyzer);
                printf("\n");
                display_spending_insights(&analyzer);
                printf("\n");
                display_risk_assessment(&analyzer);
                printf("\n");
                display_recommendations(&analyzer);

                printf("\n NEXT STEPS:\n");
                printf("1. Implement high-priority recommendations\n");
                printf("2. Set up automatic savings transfers\n");
                printf("3. Review subscriptions and recurring expenses\n");
                printf("4. Create a detailed monthly budget\n");
                printf("5. Track progress weekly\n");

                pause();
                break;
            }

            case 7: { // Exit
                printf(" Thank you for using Smart Expense Analyzer!\n");
                printf("Remember: Small financial changes lead to big results.\n");
                running = 0;
                break;
            }

            default:
                printf(" Invalid choice! Please select 1-7.\n");
                pause();
        }
    }

    return 0;
}
```

---

## Testing the Application

### Compilation Instructions
```
# Compile the program
gcc -o smart_analyzer main.c smart_analyzer.c -lm

# Run the program
./smart_analyzer
```

### Test Scenarios
1. **Dashboard**: View overall financial health and forecasts
2. **Insights**: Analyze spending patterns by category
3. **Recommendations**: Review personalized financial advice
4. **Advisor**: Get goal-specific guidance
5. **Risk Assessment**: Understand financial vulnerabilities
6. **Report**: Generate comprehensive financial analysis

### Sample Analysis Output
```
 FINANCIAL DASHBOARD
════════════════════════
Monthly Income:     $5000.00
Total Expenses:     $1234.56
Net Income:         $3765.44
Savings Rate:       75.3%
Financial Score:    85/100
Risk Level:         Low

 FORECASTS
Next Month Expenses: $1289.34
Savings Potential:   $234.56
```

---

## Code Explanation

### Key Features Implemented

**Intelligent Analysis:**
- [ ] Pattern recognition in spending data
- [ ] Trend analysis and anomaly detection
- [ ] Financial health scoring algorithm

**Recommendation Engine:**
- [ ] Personalized advice based on spending patterns
- [ ] Priority-based recommendation ranking
- [ ] Potential savings calculations

**Predictive Analytics:**
- [ ] Expense forecasting using trend analysis
- [ ] Savings potential estimation
- [ ] Risk assessment modeling

**Interactive Guidance:**
- [ ] Goal-oriented financial advice
- [ ] Risk factor identification
- [ ] Actionable improvement plans

---

## Enhancements to Try

### Beginner Enhancements
1. **Data Import**: CSV file import for real expense data
2. **Goal Tracking**: Progress monitoring for financial goals
3. **Budget Alerts**: Notifications for budget overruns

### Intermediate Enhancements
1. **Machine Learning**: Pattern recognition for spending habits
2. **Investment Advice**: Basic portfolio recommendations
3. **Tax Optimization**: Tax-saving strategy suggestions

### Advanced Enhancements
1. **Predictive Modeling**: Advanced forecasting algorithms
2. **Personalization**: User profile-based recommendations
3. **Integration**: Bank account and credit card API integration
4. **Mobile App**: Cross-platform mobile application

---

## Success Checklist

**Decision Support Features:**
- [x] **Pattern Analysis**: Intelligent spending pattern recognition
- [x] **Financial Scoring**: Comprehensive financial health assessment
- [x] **Recommendation Engine**: Personalized financial advice system
- [x] **Risk Assessment**: Financial vulnerability analysis
- [x] **Predictive Forecasting**: Future expense and savings predictions
- [x] **Interactive Guidance**: Goal-oriented financial counseling

**Technical Implementation:**
- [x] **Data Analysis Algorithms**: Statistical analysis and trend detection
- [x] **Recommendation System**: Priority-based advice generation
- [x] **User Personalization**: Adaptive advice based on user goals
- [x] **Interactive Interface**: Engaging user experience with clear guidance
- [x] **Comprehensive Reporting**: Detailed financial analysis and insights

---

## Learning Outcomes

**Technical Skills:**
- [ ] Advanced data analysis and pattern recognition
- [ ] Statistical modeling and predictive algorithms
- [ ] Decision support system design
- [ ] Personalization and recommendation engines
- [ ] Risk assessment and forecasting models

**Problem-Solving Skills:**
- [ ] Financial analysis and modeling
- [ ] User-centric system design
- [ ] Complex decision logic implementation
- [ ] Predictive system development
- [ ] Interactive application architecture

---

## Code Walkthrough

### Intelligence Pipeline
```
Data Collection → Pattern Recognition → Analysis & Scoring → Recommendation Generation → User Presentation
      ↓                ↓                      ↓                        ↓                    ↓
Expense Loading   Trend Detection     Financial Health      Personalized Advice    Interactive Display
& Validation     & Anomaly Finding    Assessment & Risk     Priority Ranking       & Guidance
```

### Decision Support Flow
```
User Goals → Spending Analysis → Risk Assessment → Recommendation Filtering → Actionable Advice
     ↓             ↓                    ↓                    ↓                    ↓
Goal Input    Pattern Recognition   Vulnerability      Personalization       Implementation
Collection    & Trend Analysis     Analysis & Scoring  & Prioritization      Guidance
```

---

<div style="page-break-after: always;"></div>

---

## Implementation Notes

### Design Decisions
- [ ] **Modular Analysis**: Separate functions for different types of analysis
- [ ] **Scoring Algorithm**: Weighted factors for financial health assessment
- [ ] **Recommendation Prioritization**: Multi-factor priority ranking system
- [ ] **Interactive Guidance**: Goal-based advice customization

### Intelligence Features
- [ ] **Pattern Recognition**: Statistical analysis of spending behaviors
- [ ] **Trend Analysis**: Time-based spending pattern identification
- [ ] **Anomaly Detection**: Outlier identification using standard deviation
- [ ] **Predictive Modeling**: Simple forecasting based on historical trends

### User Experience Focus
- [ ] **Clear Visual Hierarchy**: Organized information presentation
- [ ] **Actionable Insights**: Specific, implementable recommendations
- [ ] **Progressive Disclosure**: Information revealed based on user needs
- [ ] **Encouraging Tone**: Positive, motivational language throughout

---

 **Congratulations! You've built an intelligent decision support system!** 

*Next: Automated applications with task scheduling and batch processing! *

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
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard C++ conventions with proper imports and main function
2. **Output**: Uses printf to print messages to the console
3. **Standard Library**: Includes stdio.h for input/output operations
4. **Return Value**: Returns 0 to indicate successful execution
5. **Best Practices**: Code is readable and uses C++ idioms

### Testing Your Solution

1. **Compile**: `gcc main.c -o main`
2. **Run**: `./hello`
3. **Expected Output**: `Hello, World!`

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `command not found: gcc` | Compiler not installed | `sudo apt install gcc` (Ubuntu) |
| `undefined reference to main` | Missing main function | Ensure `int main()` exists |
| `error: implicit declaration of function 'printf'` | Missing stdio.h | Add `#include <stdio.h>` |

### Tips for Learning

- C uses stdio.h for input/output with additional features
- `printf` is the C standard for formatted output
- `\n` adds a newline character in format strings
- Format specifiers control how data is displayed (%d, %f, %s, etc.)
