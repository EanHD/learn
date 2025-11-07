# Level 2: Data Processing Application

> **LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.c\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 4: Full Problem Solving

### Today's Mission

**DATA PROCESSING POWERHOUSE!**  You're now building applications that can read, process, analyze, and transform data. This level focuses on file I/O operations, data parsing, statistical calculations, and report generation.

**The Process:**
1. **Data Input**: Read and parse structured data files
2. **Data Processing**: Clean, validate, and transform data
3. **Analysis**: Perform calculations and generate insights
4. **Output**: Create formatted reports and export data
5. **User Interface**: Provide easy access to all features
6. **Error Handling**: Robust file and data validation

---

### Learning Goals

- [ ] Advanced file I/O operations
- [ ] CSV parsing and data validation
- [ ] Statistical data analysis
- [ ] Report generation and formatting
- [ ] Data filtering and searching
- [ ] Memory management for large datasets

---

### Your Task

**Build a complete Sales Data Analyzer with:**
1. **CSV Import**: Read sales data from CSV files
2. **Data Validation**: Clean and validate input data
3. **Statistical Analysis**: Calculate totals, averages, trends
4. **Filtering & Search**: Find specific data patterns
5. **Report Generation**: Create formatted output reports
6. **Data Export**: Save processed results to files

---

## Application Requirements

### Core Features
- [ ] **CSV Processing**: Parse sales data (date, product, quantity, price)
- [ ] **Data Validation**: Check for errors and missing data
- [ ] **Statistical Calculations**: Totals, averages, best/worst performers
- [ ] **Time-based Analysis**: Daily, weekly, monthly summaries
- [ ] **Product Analysis**: Best-selling items, revenue by product
- [ ] **Report Export**: Save analysis results to files

### Technical Requirements
- [ ] Handle CSV files with proper parsing
- [ ] Dynamic memory allocation for variable data sizes
- [ ] Date parsing and manipulation
- [ ] Floating-point precision handling
- [ ] Efficient data structures for analysis

---

## Application Architecture

### Data Structures
```c
# define MAX_LINE_LENGTH 1024
# define MAX_PRODUCT_NAME 100
# define MAX_DATE_LENGTH 20

typedef struct {
    char date[MAX_DATE_LENGTH];
    char product[MAX_PRODUCT_NAME];
    int quantity;
    float unit_price;
    float total_amount;
} SaleRecord;

typedef struct {
    SaleRecord *records;
    int count;
    int capacity;
    char filename[256];
} SalesData;

typedef struct {
    float total_revenue;
    int total_sales;
    float average_sale;
    char best_day[MAX_DATE_LENGTH];
    float best_day_revenue;
    char top_product[MAX_PRODUCT_NAME];
    float top_product_revenue;
} SalesStats;
```

### Function Modules
- [ ] **File Operations**: `load_csv()`, `save_report()`
- [ ] **Data Processing**: `parse_record()`, `validate_data()`
- [ ] **Analysis**: `calculate_stats()`, `analyze_by_date()`, `analyze_by_product()`
- [ ] **Reporting**: `generate_summary()`, `export_data()`
- [ ] **User Interface**: `display_menu()`, `handle_user_input()`

---

## Complete Implementation

### Header File (sales_analyzer.h)
```c
# ifndef SALES_ANALYZER_H
# define SALES_ANALYZER_H

#include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <ctype.h>
# include <math.h>

# define MAX_LINE_LENGTH 1024
# define MAX_PRODUCT_NAME 100
# define MAX_DATE_LENGTH 20
# define INITIAL_CAPACITY 100

typedef struct {
    char date[MAX_DATE_LENGTH];
    char product[MAX_PRODUCT_NAME];
    int quantity;
    float unit_price;
    float total_amount;
} SaleRecord;

typedef struct {
    SaleRecord *records;
    int count;
    int capacity;
    char filename[256];
} SalesData;

typedef struct {
    float total_revenue;
    int total_sales;
    float average_sale;
    char best_day[MAX_DATE_LENGTH];
    float best_day_revenue;
    char top_product[MAX_PRODUCT_NAME];
    float top_product_revenue;
} SalesStats;

// Function prototypes
void initialize_sales_data(SalesData *data, const char *filename);
void free_sales_data(SalesData *data);
int load_csv(SalesData *data);
int parse_sale_record(const char *line, SaleRecord *record);
int validate_sale_record(const SaleRecord *record);
void calculate_statistics(const SalesData *data, SalesStats *stats);
void analyze_by_date(const SalesData *data);
void analyze_by_product(const SalesData *data);
void generate_summary_report(const SalesData *data, const SalesStats *stats);
int save_report(const char *filename, const SalesData *data, const SalesStats *stats);
void display_menu(void);
int get_user_choice(void);
void display_records(const SalesData *data, int limit);

# endif
```

### Implementation File (sales_analyzer.c)
```c
# include "sales_analyzer.h"

// Initialize sales data structure
void initialize_sales_data(SalesData *data, const char *filename) {
    data->records = malloc(INITIAL_CAPACITY * sizeof(SaleRecord));
    if (data->records == NULL) {
        printf("Error: Memory allocation failed.\n");
        exit(1);
    }
    data->count = 0;
    data->capacity = INITIAL_CAPACITY;
    strcpy(data->filename, filename);
}

// Free allocated memory
void free_sales_data(SalesData *data) {
    free(data->records);
    data->records = NULL;
    data->count = 0;
    data->capacity = 0;
}

// Resize array if needed
int resize_sales_data(SalesData *data) {
    int new_capacity = data->capacity * 2;
    SaleRecord *new_records = realloc(data->records, new_capacity * sizeof(SaleRecord));

    if (new_records == NULL) {
        printf("Error: Memory reallocation failed.\n");
        return 0;
    }

    data->records = new_records;
    data->capacity = new_capacity;
    return 1;
}

// Load CSV file
int load_csv(SalesData *data) {
    FILE *file = fopen(data->filename, "r");
    if (file == NULL) {
        printf("Error: Could not open file '%s'\n", data->filename);
        return 0;
    }

    char line[MAX_LINE_LENGTH];
    int line_number = 0;
    int valid_records = 0;

    // Skip header line
    if (fgets(line, sizeof(line), file) == NULL) {
        printf("Error: Empty file or read error.\n");
        fclose(file);
        return 0;
    }
    line_number++;

    // Read data lines
    while (fgets(line, sizeof(line), file) != NULL) {
        line_number++;

        // Remove trailing newline
        line[strcspn(line, "\n")] = 0;

        if (strlen(line) == 0) continue; // Skip empty lines

        SaleRecord record;
        if (parse_sale_record(line, &record)) {
            if (validate_sale_record(&record)) {
                if (data->count >= data->capacity) {
                    if (!resize_sales_data(data)) {
                        break;
                    }
                }
                data->records[data->count] = record;
                data->count++;
                valid_records++;
            } else {
                printf("Warning: Invalid data on line %d, skipping.\n", line_number);
            }
        } else {
            printf("Warning: Parse error on line %d, skipping.\n", line_number);
        }
    }

    fclose(file);
    printf("Loaded %d valid records from %s\n", valid_records, data->filename);
    return valid_records;
}

// Parse CSV line into SaleRecord
int parse_sale_record(const char *line, SaleRecord *record) {
    char temp[MAX_LINE_LENGTH];
    strcpy(temp, line);

    // Parse date
    char *token = strtok(temp, ",");
    if (token == NULL) return 0;
    strcpy(record->date, token);

    // Parse product
    token = strtok(NULL, ",");
    if (token == NULL) return 0;
    strcpy(record->product, token);

    // Parse quantity
    token = strtok(NULL, ",");
    if (token == NULL) return 0;
    record->quantity = atoi(token);

    // Parse unit price
    token = strtok(NULL, ",");
    if (token == NULL) return 0;
    record->unit_price = atof(token);

    // Calculate total amount
    record->total_amount = record->quantity * record->unit_price;

    return 1;
}

// Validate sale record
int validate_sale_record(const SaleRecord *record) {
    if (strlen(record->date) == 0 || strlen(record->product) == 0) return 0;
    if (record->quantity <= 0) return 0;
    if (record->unit_price <= 0.0) return 0;
    return 1;
}

// Calculate statistics
void calculate_statistics(const SalesData *data, SalesStats *stats) {
    if (data->count == 0) {
        memset(stats, 0, sizeof(SalesStats));
        return;
    }

    stats->total_revenue = 0.0;
    stats->total_sales = data->count;
    stats->best_day_revenue = 0.0;
    stats->top_product_revenue = 0.0;

    // Use temporary storage for aggregation
    float daily_totals[365] = {0}; // Assume max 365 days
    char dates[365][MAX_DATE_LENGTH];
    int date_count = 0;

    float product_totals[100] = {0}; // Assume max 100 products
    char products[100][MAX_PRODUCT_NAME];
    int product_count = 0;

    for (int i = 0; i < data->count; i++) {
        const SaleRecord *record = &data->records[i];
        stats->total_revenue += record->total_amount;

        // Track daily totals
        int date_index = -1;
        for (int j = 0; j < date_count; j++) {
            if (strcmp(dates[j], record->date) == 0) {
                date_index = j;
                break;
            }
        }
        if (date_index == -1 && date_count < 365) {
            strcpy(dates[date_count], record->date);
            date_index = date_count;
            date_count++;
        }
        if (date_index != -1) {
            daily_totals[date_index] += record->total_amount;
        }

        // Track product totals
        int product_index = -1;
        for (int j = 0; j < product_count; j++) {
            if (strcmp(products[j], record->product) == 0) {
                product_index = j;
                break;
            }
        }
        if (product_index == -1 && product_count < 100) {
            strcpy(products[product_count], record->product);
            product_index = product_count;
            product_count++;
        }
        if (product_index != -1) {
            product_totals[product_index] += record->total_amount;
        }
    }

    stats->average_sale = stats->total_revenue / stats->total_sales;

    // Find best day
    for (int i = 0; i < date_count; i++) {
        if (daily_totals[i] > stats->best_day_revenue) {
            stats->best_day_revenue = daily_totals[i];
            strcpy(stats->best_day, dates[i]);
        }
    }

    // Find top product
    for (int i = 0; i < product_count; i++) {
        if (product_totals[i] > stats->top_product_revenue) {
            stats->top_product_revenue = product_totals[i];
            strcpy(stats->top_product, products[i]);
        }
    }
}

// Display menu
void display_menu(void) {
    printf("\n=== Sales Data Analyzer ===\n");
    printf("1. Load Sales Data\n");
    printf("2. View Records\n");
    printf("3. Generate Statistics\n");
    printf("4. Analyze by Date\n");
    printf("5. Analyze by Product\n");
    printf("6. Generate Report\n");
    printf("7. Exit\n");
    printf("Enter your choice (1-7): ");
}

// Get user choice
int get_user_choice(void) {
    int choice;
    scanf("%d", &choice);
    return choice;
}

// Display records with limit
void display_records(const SalesData *data, int limit) {
    if (data->count == 0) {
        printf("No data loaded.\n");
        return;
    }

    int display_count = (limit > 0 && limit < data->count) ? limit : data->count;

    printf("\n=== Sales Records (showing %d of %d) ===\n", display_count, data->count);
    printf("%-12s %-15s %8s %10s %10s\n", "Date", "Product", "Qty", "Unit Price", "Total");
    printf("------------------------------------------------------------\n");

    for (int i = 0; i < display_count; i++) {
        const SaleRecord *record = &data->records[i];
        printf("%-12s %-15s %8d %10.2f %10.2f\n",
               record->date, record->product, record->quantity,
               record->unit_price, record->total_amount);
    }
}

// Generate summary report
void generate_summary_report(const SalesData *data, const SalesStats *stats) {
    printf("\n=== Sales Summary Report ===\n");
    printf("Total Records: %d\n", data->count);
    printf("Total Revenue: $%.2f\n", stats->total_revenue);
    printf("Average Sale: $%.2f\n", stats->average_sale);
    printf("Best Day: %s ($%.2f)\n", stats->best_day, stats->best_day_revenue);
    printf("Top Product: %s ($%.2f)\n", stats->top_product, stats->top_product_revenue);
}

// Save report to file
int save_report(const char *filename, const SalesData *data, const SalesStats *stats) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error: Could not create report file.\n");
        return 0;
    }

    fprintf(file, "Sales Data Analysis Report\n");
    fprintf(file, "==========================\n\n");
    fprintf(file, "Summary Statistics:\n");
    fprintf(file, "Total Records: %d\n", data->count);
    fprintf(file, "Total Revenue: $%.2f\n", stats->total_revenue);
    fprintf(file, "Average Sale: $%.2f\n", stats->average_sale);
    fprintf(file, "Best Day: %s ($%.2f)\n", stats->best_day, stats->best_day_revenue);
    fprintf(file, "Top Product: %s ($%.2f)\n\n", stats->top_product, stats->top_product_revenue);

    fprintf(file, "Detailed Records:\n");
    fprintf(file, "%-12s %-15s %8s %10s %10s\n", "Date", "Product", "Qty", "Unit Price", "Total");
    fprintf(file, "------------------------------------------------------------\n");

    for (int i = 0; i < data->count; i++) {
        const SaleRecord *record = &data->records[i];
        fprintf(file, "%-12s %-15s %8d %10.2f %10.2f\n",
                record->date, record->product, record->quantity,
                record->unit_price, record->total_amount);
    }

    fclose(file);
    printf("Report saved to %s\n", filename);
    return 1;
}

// Analyze by date
void analyze_by_date(const SalesData *data) {
    if (data->count == 0) {
        printf("No data to analyze.\n");
        return;
    }

    // Simple date analysis - group by date
    printf("\n=== Sales by Date ===\n");
    printf("%-12s %8s %12s\n", "Date", "Sales", "Revenue");
    printf("------------------------------\n");

    char current_date[MAX_DATE_LENGTH] = "";
    int date_sales = 0;
    float date_revenue = 0.0;

    for (int i = 0; i < data->count; i++) {
        const SaleRecord *record = &data->records[i];

        if (strcmp(current_date, record->date) != 0) {
            // Print previous date if exists
            if (strlen(current_date) > 0) {
                printf("%-12s %8d %12.2f\n", current_date, date_sales, date_revenue);
            }

            // Start new date
            strcpy(current_date, record->date);
            date_sales = 0;
            date_revenue = 0.0;
        }

        date_sales++;
        date_revenue += record->total_amount;
    }

    // Print last date
    if (strlen(current_date) > 0) {
        printf("%-12s %8d %12.2f\n", current_date, date_sales, date_revenue);
    }
}

// Analyze by product
void analyze_by_product(const SalesData *data) {
    if (data->count == 0) {
        printf("No data to analyze.\n");
        return;
    }

    printf("\n=== Sales by Product ===\n");
    printf("%-15s %8s %12s %8s\n", "Product", "Sales", "Revenue", "Avg Price");
    printf("--------------------------------------------------\n");

    char current_product[MAX_PRODUCT_NAME] = "";
    int product_sales = 0;
    float product_revenue = 0.0;
    float total_quantity = 0;

    for (int i = 0; i < data->count; i++) {
        const SaleRecord *record = &data->records[i];

        if (strcmp(current_product, record->product) != 0) {
            // Print previous product if exists
            if (strlen(current_product) > 0) {
                float avg_price = product_revenue / total_quantity;
                printf("%-15s %8d %12.2f %8.2f\n",
                       current_product, product_sales, product_revenue, avg_price);
            }

            // Start new product
            strcpy(current_product, record->product);
            product_sales = 0;
            product_revenue = 0.0;
            total_quantity = 0;
        }

        product_sales++;
        product_revenue += record->total_amount;
        total_quantity += record->quantity;
    }

    // Print last product
    if (strlen(current_product) > 0) {
        float avg_price = product_revenue / total_quantity;
        printf("%-15s %8d %12.2f %8.2f\n",
               current_product, product_sales, product_revenue, avg_price);
    }
}
```

### Main Program (main.c)
```c
# include "sales_analyzer.h"

int main() {
    SalesData data;
    SalesStats stats;
    int data_loaded = 0;

    initialize_sales_data(&data, "sales_data.csv");

    printf("Sales Data Analyzer\n");
    printf("===================\n");

    int running = 1;
    while (running) {
        display_menu();
        int choice = get_user_choice();

        switch (choice) {
            case 1: { // Load Sales Data
                if (load_csv(&data) > 0) {
                    data_loaded = 1;
                    printf("Data loaded successfully.\n");
                } else {
                    printf("Failed to load data.\n");
                }
                break;
            }

            case 2: { // View Records
                if (!data_loaded) {
                    printf("Please load data first.\n");
                    break;
                }
                int limit;
                printf("Enter number of records to display (0 for all): ");
                scanf("%d", &limit);
                display_records(&data, limit);
                break;
            }

            case 3: { // Generate Statistics
                if (!data_loaded) {
                    printf("Please load data first.\n");
                    break;
                }
                calculate_statistics(&data, &stats);
                generate_summary_report(&data, &stats);
                break;
            }

            case 4: { // Analyze by Date
                if (!data_loaded) {
                    printf("Please load data first.\n");
                    break;
                }
                analyze_by_date(&data);
                break;
            }

            case 5: { // Analyze by Product
                if (!data_loaded) {
                    printf("Please load data first.\n");
                    break;
                }
                analyze_by_product(&data);
                break;
            }

            case 6: { // Generate Report
                if (!data_loaded) {
                    printf("Please load data first.\n");
                    break;
                }
                calculate_statistics(&data, &stats);
                save_report("sales_report.txt", &data, &stats);
                break;
            }

            case 7: { // Exit
                printf("Goodbye!\n");
                running = 0;
                break;
            }

            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    free_sales_data(&data);
    return 0;
}
```

---

## Testing the Application

### Sample CSV Data (sales_data.csv)
```csv
Date,Product,Quantity,UnitPrice
2024-01-01,Laptop,2,999.99
2024-01-01,Mouse,5,25.50
2024-01-02,Laptop,1,999.99
2024-01-02,Keyboard,3,75.00
2024-01-03,Mouse,2,25.50
2024-01-03,Monitor,1,299.99
2024-01-04,Laptop,3,999.99
2024-01-04,Mouse,4,25.50
```

### Compilation Instructions
```
# Compile the program
gcc -o sales_analyzer main.c sales_analyzer.c -lm

# Run the program
./sales_analyzer
```

### Test Scenarios
1. **Load Data**: Import the sample CSV file
2. **View Records**: Display first 5 records
3. **Statistics**: Generate summary statistics
4. **Date Analysis**: See sales grouped by date
5. **Product Analysis**: Analyze performance by product
6. **Export Report**: Save analysis to text file

---

## Code Explanation

### Key Features Implemented

**CSV Processing:**
- [ ] Robust CSV parsing with error handling
- [ ] Dynamic memory allocation for variable data sizes
- [ ] Data validation and error reporting

**Statistical Analysis:**
- [ ] Revenue calculations with floating-point precision
- [ ] Grouping and aggregation by date and product
- [ ] Summary statistics generation

**File I/O Operations:**
- [ ] CSV reading with proper error handling
- [ ] Text report generation and export
- [ ] Memory-efficient data loading

**Data Structures:**
- [ ] Dynamic arrays for variable-sized datasets
- [ ] Structured data organization
- [ ] Efficient memory management

---

## Enhancements to Try

### Beginner Enhancements
1. **Data Filtering**: Filter by date range or product type
2. **Sorting Options**: Sort data by various criteria
3. **Search Functionality**: Find specific records

### Intermediate Enhancements
1. **Multiple File Support**: Load and merge multiple CSV files
2. **Advanced Statistics**: Calculate standard deviation, median
3. **Date Range Analysis**: Analyze sales within specific periods

### Advanced Enhancements
1. **Database Integration**: Store data in SQLite database
2. **Graphical Reports**: Generate charts and graphs
3. **Web Interface**: Create web-based data visualization

---

## Success Checklist

**Data Processing Features:**
- [x] **CSV Import**: Parse and validate CSV data files
- [x] **Data Validation**: Check data integrity and handle errors
- [x] **Statistical Analysis**: Calculate totals, averages, and trends
- [x] **Grouping Operations**: Analyze data by date and product
- [x] **Report Generation**: Create formatted text reports
- [x] **File Export**: Save analysis results to files

**Technical Implementation:**
- [x] **Dynamic Memory**: Handle variable-sized datasets
- [x] **Error Handling**: Robust file and data validation
- [x] **Modular Design**: Separate functions for different operations
- [x] **User Interface**: Complete menu-driven application

---

## Learning Outcomes

**Technical Skills:**
- [ ] Advanced file I/O and CSV parsing
- [ ] Dynamic memory allocation and management
- [ ] Statistical data analysis algorithms
- [ ] Report generation and formatting
- [ ] Data validation and error handling

**Problem-Solving Skills:**
- [ ] Data processing pipeline design
- [ ] Memory-efficient data structures
- [ ] Algorithm optimization for large datasets
- [ ] User experience considerations for data tools

---

## Code Walkthrough

### Data Processing Pipeline
```
CSV File → Parse Records → Validate Data → Store in Memory
      ↓           ↓            ↓           ↓
   Error     Clean Data    Validated    In-Memory
  Handling   Extraction    Records      Database
```

### Analysis Workflow
```
Raw Data → Statistical Calculations → Grouping Operations → Report Generation
     ↓               ↓                      ↓              ↓
Data Loading    Summary Stats        Date/Product     Formatted Output
Validation      & Averages           Analysis         & File Export
```

---

<div style="page-break-after: always;"></div>

---

## Implementation Notes

### Design Decisions
- [ ] **Dynamic Arrays**: Allow processing of any size dataset
- [ ] **Simple CSV Format**: Focus on core functionality over complex parsing
- [ ] **In-Memory Processing**: Fast analysis for reasonable dataset sizes
- [ ] **Text-Based Reports**: Human-readable output format

### Performance Considerations
- [ ] **Memory Efficiency**: Resize arrays only when needed
- [ ] **Linear Processing**: Single-pass algorithms where possible
- [ ] **Limited Aggregation**: Fixed-size arrays for grouping operations
- [ ] **File I/O Optimization**: Read once, process in memory

### Error Handling Strategy
- [ ] **File Operations**: Check all file open/close operations
- [ ] **Memory Allocation**: Verify malloc/realloc success
- [ ] **Data Validation**: Comprehensive input checking
- [ ] **User Feedback**: Clear error messages and recovery options

---

 **Congratulations! You've built a powerful data processing application!**

*Next: Mathematical applications with advanced formula implementations! *

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
