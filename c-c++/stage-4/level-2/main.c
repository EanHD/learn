#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Constants
#define MAX_SALES 1000
#define MAX_LINE_LENGTH 256
#define MAX_PRODUCT_NAME 50
#define MAX_DATE_LENGTH 11

// Data structures
typedef struct {
    char date[MAX_DATE_LENGTH];
    char product[MAX_PRODUCT_NAME];
    int quantity;
    float price;
    float total;
} Sale;

// Global variables
Sale sales[MAX_SALES];
int sale_count = 0;

// Function prototypes
void display_menu();
void load_csv_data();
void display_all_sales();
void calculate_statistics();
void search_by_product();
void search_by_date();
void generate_report();
void export_data();
int get_menu_choice();
void trim_whitespace(char* str);
int parse_csv_line(char* line, Sale* sale);
void display_sale(const Sale* sale);
float calculate_total_revenue();
float calculate_average_sale();
int find_best_selling_product(char* product_name, float* revenue);
int find_highest_revenue_day(char* date, float* revenue);

int main() {
    printf("📊 SALES DATA ANALYZER\n");
    printf("======================\n\n");

    // Load data if available
    load_csv_data();

    // Main menu loop
    int choice;
    do {
        display_menu();
        choice = get_menu_choice();

        switch(choice) {
            case 1:
                load_csv_data();
                break;
            case 2:
                display_all_sales();
                break;
            case 3:
                calculate_statistics();
                break;
            case 4:
                search_by_product();
                break;
            case 5:
                search_by_date();
                break;
            case 6:
                generate_report();
                break;
            case 7:
                export_data();
                break;
            case 8:
                printf("Thank you for using the Sales Data Analyzer!\n");
                break;
            default:
                printf("❌ Invalid choice. Please try again.\n");
        }
        printf("\n");
    } while (choice != 8);

    return 0;
}

void display_menu() {
    printf("📋 MAIN MENU\n");
    printf("============\n");
    printf("1. Load CSV Data\n");
    printf("2. Display All Sales\n");
    printf("3. Calculate Statistics\n");
    printf("4. Search by Product\n");
    printf("5. Search by Date\n");
    printf("6. Generate Report\n");
    printf("7. Export Data\n");
    printf("8. Exit\n");
    printf("Enter choice (1-8): ");
}

void load_csv_data() {
    char filename[100];
    printf("📁 LOAD CSV DATA\n");
    printf("================\n");
    printf("Enter CSV filename (or 'sales.csv' for default): ");
    fgets(filename, sizeof(filename), stdin);
    trim_whitespace(filename);

    if (strlen(filename) == 0) {
        strcpy(filename, "sales.csv");
    }

    FILE* file = fopen(filename, "r");
    if (!file) {
        printf("❌ Could not open file '%s'. Creating sample data instead.\n", filename);
        create_sample_data();
        return;
    }

    // Skip header line
    char line[MAX_LINE_LENGTH];
    fgets(line, sizeof(line), file);

    sale_count = 0;
    while (fgets(line, sizeof(line), file) && sale_count < MAX_SALES) {
        if (parse_csv_line(line, &sales[sale_count])) {
            sale_count++;
        }
    }

    fclose(file);
    printf("✅ Loaded %d sales records from '%s'\n", sale_count, filename);
}

void create_sample_data() {
    // Create sample sales data for demonstration
    strcpy(sales[0].date, "2024-01-15");
    strcpy(sales[0].product, "Laptop");
    sales[0].quantity = 2;
    sales[0].price = 999.99;
    sales[0].total = sales[0].quantity * sales[0].price;

    strcpy(sales[1].date, "2024-01-15");
    strcpy(sales[1].product, "Mouse");
    sales[1].quantity = 5;
    sales[1].price = 25.50;
    sales[1].total = sales[1].quantity * sales[1].price;

    strcpy(sales[2].date, "2024-01-16");
    strcpy(sales[2].product, "Keyboard");
    sales[2].quantity = 3;
    sales[2].price = 75.00;
    sales[2].total = sales[2].quantity * sales[2].price;

    strcpy(sales[3].date, "2024-01-16");
    strcpy(sales[3].product, "Laptop");
    sales[3].quantity = 1;
    sales[3].price = 999.99;
    sales[3].total = sales[3].quantity * sales[3].price;

    sale_count = 4;
    printf("✅ Created %d sample sales records\n", sale_count);
}

int parse_csv_line(char* line, Sale* sale) {
    char* token;
    int field_count = 0;

    // Parse date
    token = strtok(line, ",");
    if (!token) return 0;
    trim_whitespace(token);
    strcpy(sale->date, token);
    field_count++;

    // Parse product
    token = strtok(NULL, ",");
    if (!token) return 0;
    trim_whitespace(token);
    strcpy(sale->product, token);
    field_count++;

    // Parse quantity
    token = strtok(NULL, ",");
    if (!token) return 0;
    trim_whitespace(token);
    sale->quantity = atoi(token);
    field_count++;

    // Parse price
    token = strtok(NULL, ",");
    if (!token) return 0;
    trim_whitespace(token);
    sale->price = atof(token);
    field_count++;

    // Calculate total
    sale->total = sale->quantity * sale->price;

    return field_count == 4;
}

void display_all_sales() {
    printf("📊 ALL SALES RECORDS\n");
    printf("====================\n");

    if (sale_count == 0) {
        printf("No sales data available.\n");
        return;
    }

    printf("%-12s %-15s %-8s %-10s %-10s\n",
           "Date", "Product", "Qty", "Price", "Total");
    printf("----------------------------------------------------\n");

    for (int i = 0; i < sale_count; i++) {
        printf("%-12s %-15s %-8d $%-9.2f $%-9.2f\n",
               sales[i].date, sales[i].product, sales[i].quantity,
               sales[i].price, sales[i].total);
    }

    printf("\nTotal Records: %d\n", sale_count);
}

void calculate_statistics() {
    printf("📈 SALES STATISTICS\n");
    printf("===================\n");

    if (sale_count == 0) {
        printf("No sales data available.\n");
        return;
    }

    float total_revenue = calculate_total_revenue();
    float average_sale = calculate_average_sale();

    printf("Total Revenue: $%.2f\n", total_revenue);
    printf("Average Sale: $%.2f\n", average_sale);
    printf("Total Transactions: %d\n", sale_count);

    // Find best selling product
    char best_product[MAX_PRODUCT_NAME];
    float best_revenue;
    if (find_best_selling_product(best_product, &best_revenue)) {
        printf("Best Selling Product: %s ($%.2f)\n", best_product, best_revenue);
    }

    // Find highest revenue day
    char best_day[MAX_DATE_LENGTH];
    float day_revenue;
    if (find_highest_revenue_day(best_day, &day_revenue)) {
        printf("Highest Revenue Day: %s ($%.2f)\n", best_day, day_revenue);
    }
}

void search_by_product() {
    printf("🔍 SEARCH BY PRODUCT\n");
    printf("====================\n");

    char search_term[MAX_PRODUCT_NAME];
    printf("Enter product name to search: ");
    fgets(search_term, sizeof(search_term), stdin);
    trim_whitespace(search_term);

    if (strlen(search_term) == 0) {
        printf("❌ Please enter a product name.\n");
        return;
    }

    printf("\nSearch Results for '%s':\n", search_term);
    printf("%-12s %-15s %-8s %-10s %-10s\n",
           "Date", "Product", "Qty", "Price", "Total");
    printf("----------------------------------------------------\n");

    int found = 0;
    float total_revenue = 0;

    for (int i = 0; i < sale_count; i++) {
        if (strstr(sales[i].product, search_term) != NULL) {
            printf("%-12s %-15s %-8d $%-9.2f $%-9.2f\n",
                   sales[i].date, sales[i].product, sales[i].quantity,
                   sales[i].price, sales[i].total);
            total_revenue += sales[i].total;
            found++;
        }
    }

    if (found == 0) {
        printf("No products found matching '%s'\n", search_term);
    } else {
        printf("\nFound %d sales, Total Revenue: $%.2f\n", found, total_revenue);
    }
}

void search_by_date() {
    printf("📅 SEARCH BY DATE\n");
    printf("=================\n");

    char search_date[MAX_DATE_LENGTH];
    printf("Enter date (YYYY-MM-DD): ");
    fgets(search_date, sizeof(search_date), stdin);
    trim_whitespace(search_date);

    if (strlen(search_date) == 0) {
        printf("❌ Please enter a date.\n");
        return;
    }

    printf("\nSales for %s:\n", search_date);
    printf("%-15s %-8s %-10s %-10s\n",
           "Product", "Qty", "Price", "Total");
    printf("----------------------------------------\n");

    int found = 0;
    float total_revenue = 0;

    for (int i = 0; i < sale_count; i++) {
        if (strcmp(sales[i].date, search_date) == 0) {
            printf("%-15s %-8d $%-9.2f $%-9.2f\n",
                   sales[i].product, sales[i].quantity,
                   sales[i].price, sales[i].total);
            total_revenue += sales[i].total;
            found++;
        }
    }

    if (found == 0) {
        printf("No sales found for date '%s'\n", search_date);
    } else {
        printf("\nFound %d sales, Total Revenue: $%.2f\n", found, total_revenue);
    }
}

void generate_report() {
    printf("📋 SALES REPORT\n");
    printf("===============\n");

    if (sale_count == 0) {
        printf("No sales data available.\n");
        return;
    }

    // Group by product
    printf("📊 REVENUE BY PRODUCT\n");
    printf("=====================\n");

    char processed_products[MAX_SALES][MAX_PRODUCT_NAME];
    int processed_count = 0;

    for (int i = 0; i < sale_count; i++) {
        int already_processed = 0;
        for (int j = 0; j < processed_count; j++) {
            if (strcmp(processed_products[j], sales[i].product) == 0) {
                already_processed = 1;
                break;
            }
        }

        if (!already_processed) {
            strcpy(processed_products[processed_count], sales[i].product);
            processed_count++;

            float product_revenue = 0;
            int product_quantity = 0;

            for (int j = 0; j < sale_count; j++) {
                if (strcmp(sales[j].product, sales[i].product) == 0) {
                    product_revenue += sales[j].total;
                    product_quantity += sales[j].quantity;
                }
            }

            printf("%-15s Qty: %-3d Revenue: $%-10.2f\n",
                   sales[i].product, product_quantity, product_revenue);
        }
    }
}

void export_data() {
    printf("💾 EXPORT DATA\n");
    printf("==============\n");

    char filename[100];
    printf("Enter export filename (or 'sales_export.csv' for default): ");
    fgets(filename, sizeof(filename), stdin);
    trim_whitespace(filename);

    if (strlen(filename) == 0) {
        strcpy(filename, "sales_export.csv");
    }

    FILE* file = fopen(filename, "w");
    if (!file) {
        printf("❌ Could not create export file '%s'\n", filename);
        return;
    }

    // Write header
    fprintf(file, "Date,Product,Quantity,Price,Total\n");

    // Write data
    for (int i = 0; i < sale_count; i++) {
        fprintf(file, "%s,%s,%d,%.2f,%.2f\n",
                sales[i].date, sales[i].product, sales[i].quantity,
                sales[i].price, sales[i].total);
    }

    fclose(file);
    printf("✅ Exported %d sales records to '%s'\n", sale_count, filename);
}

// Utility functions
int get_menu_choice() {
    int choice;
    while (scanf("%d", &choice) != 1) {
        while (getchar() != '\n'); // Clear input buffer
        printf("Please enter a valid number: ");
    }
    while (getchar() != '\n'); // Clear newline
    return choice;
}

void trim_whitespace(char* str) {
    // Remove trailing whitespace
    int len = strlen(str);
    while (len > 0 && isspace(str[len - 1])) {
        str[len - 1] = '\0';
        len--;
    }

    // Remove leading whitespace
    char* start = str;
    while (*start && isspace(*start)) {
        start++;
    }

    if (start != str) {
        memmove(str, start, strlen(start) + 1);
    }
}

float calculate_total_revenue() {
    float total = 0;
    for (int i = 0; i < sale_count; i++) {
        total += sales[i].total;
    }
    return total;
}

float calculate_average_sale() {
    if (sale_count == 0) return 0;
    return calculate_total_revenue() / sale_count;
}

int find_best_selling_product(char* product_name, float* revenue) {
    if (sale_count == 0) return 0;

    char best_product[MAX_PRODUCT_NAME] = "";
    float best_revenue = 0;

    for (int i = 0; i < sale_count; i++) {
        float product_rev = 0;
        for (int j = 0; j < sale_count; j++) {
            if (strcmp(sales[j].product, sales[i].product) == 0) {
                product_rev += sales[j].total;
            }
        }

        if (product_rev > best_revenue) {
            best_revenue = product_rev;
            strcpy(best_product, sales[i].product);
        }
    }

    if (strlen(best_product) > 0) {
        strcpy(product_name, best_product);
        *revenue = best_revenue;
        return 1;
    }

    return 0;
}

int find_highest_revenue_day(char* date, float* revenue) {
    if (sale_count == 0) return 0;

    char best_date[MAX_DATE_LENGTH] = "";
    float best_revenue = 0;

    for (int i = 0; i < sale_count; i++) {
        float day_rev = 0;
        for (int j = 0; j < sale_count; j++) {
            if (strcmp(sales[j].date, sales[i].date) == 0) {
                day_rev += sales[j].total;
            }
        }

        if (day_rev > best_revenue) {
            best_revenue = day_rev;
            strcpy(best_date, sales[i].date);
        }
    }

    if (strlen(best_date) > 0) {
        strcpy(date, best_date);
        *revenue = best_revenue;
        return 1;
    }

    return 0;
}