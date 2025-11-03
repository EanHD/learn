#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include <math.h>

// Constants
#define MAX_PRODUCTS 500
#define MAX_CUSTOMERS 200
#define MAX_SALES 1000
#define MAX_INVENTORY 1000
#define MAX_SUPPLIERS 50
#define MAX_EMPLOYEES 20
#define MAX_NAME_LENGTH 100
#define MAX_DESCRIPTION_LENGTH 300
#define MAX_ADDRESS_LENGTH 200

// Data Structures
typedef struct {
    int id;
    char name[MAX_NAME_LENGTH];
    char description[MAX_DESCRIPTION_LENGTH];
    double price;
    double cost;
    int stock_quantity;
    int reorder_level;
    char category[MAX_NAME_LENGTH];
    int supplier_id;
    time_t created_date;
    time_t last_updated;
} Product;

typedef struct {
    int id;
    char name[MAX_NAME_LENGTH];
    char email[MAX_NAME_LENGTH];
    char phone[MAX_NAME_LENGTH];
    char address[MAX_ADDRESS_LENGTH];
    double total_purchases;
    int loyalty_points;
    char membership_level[20]; // bronze, silver, gold, platinum
    time_t registration_date;
    time_t last_purchase;
} Customer;

typedef struct {
    int id;
    int customer_id;
    int employee_id;
    time_t sale_date;
    double subtotal;
    double tax_amount;
    double discount_amount;
    double total_amount;
    char payment_method[20]; // cash, credit, debit, check
    char status[20]; // pending, completed, cancelled, refunded
    int item_count;
} Sale;

typedef struct {
    int sale_id;
    int product_id;
    int quantity;
    double unit_price;
    double line_total;
} SaleItem;

typedef struct {
    int id;
    char name[MAX_NAME_LENGTH];
    char contact_person[MAX_NAME_LENGTH];
    char email[MAX_NAME_LENGTH];
    char phone[MAX_NAME_LENGTH];
    char address[MAX_ADDRESS_LENGTH];
    double total_orders;
    time_t last_order_date;
} Supplier;

typedef struct {
    int id;
    char name[MAX_NAME_LENGTH];
    char position[MAX_NAME_LENGTH];
    double salary;
    char department[MAX_NAME_LENGTH];
    time_t hire_date;
    char status[10]; // active, inactive
} Employee;

typedef struct {
    double total_revenue;
    double total_cost;
    double total_profit;
    int total_sales;
    int total_customers;
    int total_products;
    double average_order_value;
    time_t report_date;
} BusinessMetrics;

// Global Variables
Product products[MAX_PRODUCTS];
int product_count = 0;
Customer customers[MAX_CUSTOMERS];
int customer_count = 0;
Sale sales[MAX_SALES];
int sale_count = 0;
SaleItem sale_items[MAX_INVENTORY];
int sale_item_count = 0;
Supplier suppliers[MAX_SUPPLIERS];
int supplier_count = 0;
Employee employees[MAX_EMPLOYEES];
int employee_count = 0;

// Function Prototypes
void initialize_sample_data();
void display_main_menu();
void manage_products();
void manage_customers();
void manage_sales();
void manage_inventory();
void manage_suppliers();
void manage_employees();
void generate_reports();
void business_analytics();
void system_backup();

// Utility Functions
void clear_screen() {
    system("clear");
}

void pause() {
    printf("\nPress Enter to continue...");
    getchar();
    getchar(); // consume newline
}

time_t get_current_time() {
    return time(NULL);
}

void format_time(time_t timestamp, char *buffer, size_t size) {
    struct tm *timeinfo = localtime(&timestamp);
    strftime(buffer, size, "%Y-%m-%d %H:%M:%S", timeinfo);
}

void format_date(time_t timestamp, char *buffer, size_t size) {
    struct tm *timeinfo = localtime(&timestamp);
    strftime(buffer, size, "%Y-%m-%d", timeinfo);
}

int generate_id() {
    static int id_counter = 1000;
    return id_counter++;
}

double calculate_tax(double amount) {
    return amount * 0.08; // 8% tax rate
}

void update_customer_loyalty(Customer *customer, double purchase_amount) {
    customer->total_purchases += purchase_amount;
    customer->loyalty_points += (int)(purchase_amount / 10); // 1 point per $10 spent

    // Update membership level
    if(customer->loyalty_points >= 1000) {
        strcpy(customer->membership_level, "platinum");
    } else if(customer->loyalty_points >= 500) {
        strcpy(customer->membership_level, "gold");
    } else if(customer->loyalty_points >= 200) {
        strcpy(customer->membership_level, "silver");
    } else {
        strcpy(customer->membership_level, "bronze");
    }
}

void check_inventory_alerts() {
    printf("\n📢 INVENTORY ALERTS 📢\n");
    printf("======================\n");

    int alerts = 0;
    for(int i = 0; i < product_count; i++) {
        if(products[i].stock_quantity <= products[i].reorder_level) {
            printf("⚠️  LOW STOCK: %s (Current: %d, Reorder: %d)\n",
                   products[i].name, products[i].stock_quantity, products[i].reorder_level);
            alerts++;
        }
    }

    if(alerts == 0) {
        printf("✅ All products are adequately stocked.\n");
    } else {
        printf("\n%d product(s) need reordering.\n", alerts);
    }
}

// Core Functions
void initialize_sample_data() {
    // Sample Products
    products[0].id = generate_id();
    strcpy(products[0].name, "Wireless Headphones");
    strcpy(products[0].description, "High-quality wireless headphones with noise cancellation");
    products[0].price = 199.99;
    products[0].cost = 120.00;
    products[0].stock_quantity = 25;
    products[0].reorder_level = 10;
    strcpy(products[0].category, "Electronics");
    products[0].supplier_id = 1;
    products[0].created_date = get_current_time();
    products[0].last_updated = get_current_time();

    products[1].id = generate_id();
    strcpy(products[1].name, "Office Chair");
    strcpy(products[1].description, "Ergonomic office chair with lumbar support");
    products[1].price = 299.99;
    products[1].cost = 150.00;
    products[1].stock_quantity = 15;
    products[1].reorder_level = 5;
    strcpy(products[1].category, "Furniture");
    products[1].supplier_id = 2;
    products[1].created_date = get_current_time();
    products[1].last_updated = get_current_time();

    product_count = 2;

    // Sample Customers
    customers[0].id = generate_id();
    strcpy(customers[0].name, "John Smith");
    strcpy(customers[0].email, "john.smith@email.com");
    strcpy(customers[0].phone, "(555) 123-4567");
    strcpy(customers[0].address, "123 Main St, Anytown, USA");
    customers[0].total_purchases = 499.98;
    customers[0].loyalty_points = 50;
    strcpy(customers[0].membership_level, "silver");
    customers[0].registration_date = get_current_time() - 86400 * 30; // 30 days ago
    customers[0].last_purchase = get_current_time() - 86400 * 2; // 2 days ago

    customers[1].id = generate_id();
    strcpy(customers[1].name, "Sarah Johnson");
    strcpy(customers[1].email, "sarah.j@email.com");
    strcpy(customers[1].phone, "(555) 987-6543");
    strcpy(customers[1].address, "456 Oak Ave, Somewhere, USA");
    customers[1].total_purchases = 199.99;
    customers[1].loyalty_points = 20;
    strcpy(customers[1].membership_level, "bronze");
    customers[1].registration_date = get_current_time() - 86400 * 15; // 15 days ago
    customers[1].last_purchase = get_current_time() - 86400 * 5; // 5 days ago

    customer_count = 2;

    // Sample Suppliers
    suppliers[0].id = 1;
    strcpy(suppliers[0].name, "Tech Supplies Inc.");
    strcpy(suppliers[0].contact_person, "Mike Wilson");
    strcpy(suppliers[0].email, "mike@techsupplies.com");
    strcpy(suppliers[0].phone, "(555) 111-2222");
    strcpy(suppliers[0].address, "789 Tech Blvd, Silicon Valley, CA");
    suppliers[0].total_orders = 2500.00;
    suppliers[0].last_order_date = get_current_time() - 86400 * 7; // 7 days ago

    suppliers[1].id = 2;
    strcpy(suppliers[1].name, "Office Furniture Co.");
    strcpy(suppliers[1].contact_person, "Lisa Brown");
    strcpy(suppliers[1].email, "lisa@officefurn.com");
    strcpy(suppliers[1].phone, "(555) 333-4444");
    strcpy(suppliers[1].address, "321 Business Park, Industrial City, NY");
    suppliers[1].total_orders = 1800.00;
    suppliers[1].last_order_date = get_current_time() - 86400 * 3; // 3 days ago

    supplier_count = 2;

    // Sample Employees
    employees[0].id = generate_id();
    strcpy(employees[0].name, "Alice Cooper");
    strcpy(employees[0].position, "Store Manager");
    employees[0].salary = 55000.00;
    strcpy(employees[0].department, "Management");
    employees[0].hire_date = get_current_time() - 86400 * 365; // 1 year ago
    strcpy(employees[0].status, "active");

    employees[1].id = generate_id();
    strcpy(employees[1].name, "Bob Davis");
    strcpy(employees[1].position, "Sales Associate");
    employees[1].salary = 35000.00;
    strcpy(employees[1].department, "Sales");
    employees[1].hire_date = get_current_time() - 86400 * 180; // 6 months ago
    strcpy(employees[1].status, "active");

    employee_count = 2;
}

void display_main_menu() {
    clear_screen();
    printf("🏢 COMPREHENSIVE BUSINESS MANAGEMENT SYSTEM 🏢\n");
    printf("===============================================\n\n");
    printf("Main Menu:\n");
    printf("1. 📦 Manage Products\n");
    printf("2. 👥 Manage Customers\n");
    printf("3. 💰 Manage Sales\n");
    printf("4. 📊 Manage Inventory\n");
    printf("5. 🚚 Manage Suppliers\n");
    printf("6. 👷 Manage Employees\n");
    printf("7. 📈 Generate Reports\n");
    printf("8. 📊 Business Analytics\n");
    printf("9. 💾 System Backup\n");
    printf("0. 🚪 Exit\n\n");
    printf("Enter your choice (0-9): ");
}

void manage_products() {
    clear_screen();
    printf("📦 PRODUCT MANAGEMENT 📦\n");
    printf("=========================\n\n");

    printf("Product Options:\n");
    printf("1. Add Product\n");
    printf("2. View Products\n");
    printf("3. Update Product\n");
    printf("4. Delete Product\n");
    printf("5. Search Products\n");
    printf("6. Back to Main Menu\n\n");
    printf("Enter choice (1-6): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // Add Product
            if(product_count >= MAX_PRODUCTS) {
                printf("Product limit reached!\n");
                pause();
                return;
            }

            printf("\nAdd New Product:\n");
            products[product_count].id = generate_id();

            printf("Product name: ");
            fgets(products[product_count].name, sizeof(products[product_count].name), stdin);
            products[product_count].name[strcspn(products[product_count].name, "\n")] = 0;

            printf("Description: ");
            fgets(products[product_count].description, sizeof(products[product_count].description), stdin);
            products[product_count].description[strcspn(products[product_count].description, "\n")] = 0;

            printf("Price: $");
            scanf("%lf", &products[product_count].price);
            getchar();

            printf("Cost: $");
            scanf("%lf", &products[product_count].cost);
            getchar();

            printf("Stock quantity: ");
            scanf("%d", &products[product_count].stock_quantity);
            getchar();

            printf("Reorder level: ");
            scanf("%d", &products[product_count].reorder_level);
            getchar();

            printf("Category: ");
            fgets(products[product_count].category, sizeof(products[product_count].category), stdin);
            products[product_count].category[strcspn(products[product_count].category, "\n")] = 0;

            printf("Supplier ID: ");
            scanf("%d", &products[product_count].supplier_id);
            getchar();

            products[product_count].created_date = get_current_time();
            products[product_count].last_updated = get_current_time();

            product_count++;
            printf("✅ Product added successfully! ID: %d\n", products[product_count-1].id);
            break;
        }
        case 2: { // View Products
            printf("\nProduct Inventory:\n");
            printf("==================\n");
            for(int i = 0; i < product_count; i++) {
                printf("ID: %d\n", products[i].id);
                printf("Name: %s\n", products[i].name);
                printf("Category: %s\n", products[i].category);
                printf("Price: $%.2f | Cost: $%.2f\n", products[i].price, products[i].cost);
                printf("Stock: %d | Reorder Level: %d\n", products[i].stock_quantity, products[i].reorder_level);
                printf("Profit Margin: %.1f%%\n", ((products[i].price - products[i].cost) / products[i].cost) * 100);
                printf("\n");
            }
            if(product_count == 0) {
                printf("No products found.\n");
            }
            break;
        }
        case 3: { // Update Product
            printf("\nEnter product ID to update: ");
            int product_id;
            scanf("%d", &product_id);
            getchar();

            int found = -1;
            for(int i = 0; i < product_count; i++) {
                if(products[i].id == product_id) {
                    found = i;
                    break;
                }
            }

            if(found == -1) {
                printf("Product not found!\n");
                break;
            }

            printf("Update %s:\n", products[found].name);
            printf("New stock quantity: ");
            scanf("%d", &products[found].stock_quantity);
            getchar();

            printf("New price: $");
            scanf("%lf", &products[found].price);
            getchar();

            products[found].last_updated = get_current_time();
            printf("✅ Product updated successfully!\n");
            break;
        }
        case 4: { // Delete Product
            printf("\nEnter product ID to delete: ");
            int product_id;
            scanf("%d", &product_id);
            getchar();

            int found = -1;
            for(int i = 0; i < product_count; i++) {
                if(products[i].id == product_id) {
                    found = i;
                    break;
                }
            }

            if(found == -1) {
                printf("Product not found!\n");
                break;
            }

            // Shift remaining products
            for(int i = found; i < product_count - 1; i++) {
                products[i] = products[i + 1];
            }
            product_count--;

            printf("✅ Product deleted successfully!\n");
            break;
        }
        case 5: { // Search Products
            printf("\nSearch by (1) Category or (2) Name: ");
            int search_type;
            scanf("%d", &search_type);
            getchar();

            if(search_type == 1) {
                char category[MAX_NAME_LENGTH];
                printf("Enter category: ");
                fgets(category, sizeof(category), stdin);
                category[strcspn(category, "\n")] = 0;

                printf("\nProducts in category '%s':\n", category);
                for(int i = 0; i < product_count; i++) {
                    if(strstr(products[i].category, category) != NULL) {
                        printf("• %s (ID: %d) - $%.2f\n", products[i].name, products[i].id, products[i].price);
                    }
                }
            } else if(search_type == 2) {
                char name_search[MAX_NAME_LENGTH];
                printf("Enter product name: ");
                fgets(name_search, sizeof(name_search), stdin);
                name_search[strcspn(name_search, "\n")] = 0;

                printf("\nProducts matching '%s':\n", name_search);
                for(int i = 0; i < product_count; i++) {
                    if(strstr(products[i].name, name_search) != NULL) {
                        printf("• %s (ID: %d) - $%.2f\n", products[i].name, products[i].id, products[i].price);
                    }
                }
            }
            break;
        }
        case 6:
            return;
        default:
            printf("Invalid choice!\n");
    }

    pause();
}

void manage_customers() {
    clear_screen();
    printf("👥 CUSTOMER MANAGEMENT 👥\n");
    printf("=========================\n\n");

    printf("Customer Options:\n");
    printf("1. Add Customer\n");
    printf("2. View Customers\n");
    printf("3. Update Customer\n");
    printf("4. Customer Loyalty Program\n");
    printf("5. Back to Main Menu\n\n");
    printf("Enter choice (1-5): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // Add Customer
            if(customer_count >= MAX_CUSTOMERS) {
                printf("Customer limit reached!\n");
                pause();
                return;
            }

            printf("\nAdd New Customer:\n");
            customers[customer_count].id = generate_id();

            printf("Customer name: ");
            fgets(customers[customer_count].name, sizeof(customers[customer_count].name), stdin);
            customers[customer_count].name[strcspn(customers[customer_count].name, "\n")] = 0;

            printf("Email: ");
            fgets(customers[customer_count].email, sizeof(customers[customer_count].email), stdin);
            customers[customer_count].email[strcspn(customers[customer_count].email, "\n")] = 0;

            printf("Phone: ");
            fgets(customers[customer_count].phone, sizeof(customers[customer_count].phone), stdin);
            customers[customer_count].phone[strcspn(customers[customer_count].phone, "\n")] = 0;

            printf("Address: ");
            fgets(customers[customer_count].address, sizeof(customers[customer_count].address), stdin);
            customers[customer_count].address[strcspn(customers[customer_count].address, "\n")] = 0;

            customers[customer_count].total_purchases = 0.0;
            customers[customer_count].loyalty_points = 0;
            strcpy(customers[customer_count].membership_level, "bronze");
            customers[customer_count].registration_date = get_current_time();
            customers[customer_count].last_purchase = 0;

            customer_count++;
            printf("✅ Customer added successfully! ID: %d\n", customers[customer_count-1].id);
            break;
        }
        case 2: { // View Customers
            printf("\nCustomer Database:\n");
            printf("==================\n");
            for(int i = 0; i < customer_count; i++) {
                printf("ID: %d\n", customers[i].id);
                printf("Name: %s\n", customers[i].name);
                printf("Email: %s | Phone: %s\n", customers[i].email, customers[i].phone);
                printf("Membership: %s (%d points)\n", customers[i].membership_level, customers[i].loyalty_points);
                printf("Total Purchases: $%.2f\n", customers[i].total_purchases);

                char reg_date[20], last_purchase[20];
                format_date(customers[i].registration_date, reg_date, sizeof(reg_date));
                if(customers[i].last_purchase > 0) {
                    format_date(customers[i].last_purchase, last_purchase, sizeof(last_purchase));
                    printf("Last Purchase: %s\n", last_purchase);
                } else {
                    printf("Last Purchase: Never\n");
                }
                printf("Registration: %s\n\n", reg_date);
            }
            if(customer_count == 0) {
                printf("No customers found.\n");
            }
            break;
        }
        case 3: { // Update Customer
            printf("\nEnter customer ID to update: ");
            int customer_id;
            scanf("%d", &customer_id);
            getchar();

            int found = -1;
            for(int i = 0; i < customer_count; i++) {
                if(customers[i].id == customer_id) {
                    found = i;
                    break;
                }
            }

            if(found == -1) {
                printf("Customer not found!\n");
                break;
            }

            printf("Update %s:\n", customers[found].name);
            printf("New phone: ");
            fgets(customers[found].phone, sizeof(customers[found].phone), stdin);
            customers[found].phone[strcspn(customers[found].phone, "\n")] = 0;

            printf("New email: ");
            fgets(customers[found].email, sizeof(customers[found].email), stdin);
            customers[found].email[strcspn(customers[found].email, "\n")] = 0;

            printf("✅ Customer updated successfully!\n");
            break;
        }
        case 4: { // Loyalty Program
            printf("\nCustomer Loyalty Program:\n");
            printf("=========================\n");
            for(int i = 0; i < customer_count; i++) {
                printf("• %s: %s (%d points) - $%.2f spent\n",
                       customers[i].name, customers[i].membership_level,
                       customers[i].loyalty_points, customers[i].total_purchases);
            }

            printf("\nMembership Levels:\n");
            printf("Bronze: 0-199 points\n");
            printf("Silver: 200-499 points\n");
            printf("Gold: 500-999 points\n");
            printf("Platinum: 1000+ points\n");
            break;
        }
        case 5:
            return;
        default:
            printf("Invalid choice!\n");
    }

    pause();
}

void manage_sales() {
    clear_screen();
    printf("💰 SALES MANAGEMENT 💰\n");
    printf("======================\n\n");

    printf("Sales Options:\n");
    printf("1. New Sale\n");
    printf("2. View Sales\n");
    printf("3. Sales by Date Range\n");
    printf("4. Sales by Customer\n");
    printf("5. Back to Main Menu\n\n");
    printf("Enter choice (1-5): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // New Sale
            if(sale_count >= MAX_SALES) {
                printf("Sale limit reached!\n");
                pause();
                return;
            }

            printf("\nNew Sale Transaction:\n");

            // Select customer
            printf("Available customers:\n");
            for(int i = 0; i < customer_count; i++) {
                printf("%d. %s\n", customers[i].id, customers[i].name);
            }

            printf("Enter customer ID: ");
            int customer_id;
            scanf("%d", &customer_id);
            getchar();

            int customer_found = -1;
            for(int i = 0; i < customer_count; i++) {
                if(customers[i].id == customer_id) {
                    customer_found = i;
                    break;
                }
            }

            if(customer_found == -1) {
                printf("Customer not found!\n");
                break;
            }

            // Select employee (for now, use first active employee)
            int employee_id = employees[0].id;

            // Create sale record
            sales[sale_count].id = generate_id();
            sales[sale_count].customer_id = customer_id;
            sales[sale_count].employee_id = employee_id;
            sales[sale_count].sale_date = get_current_time();
            sales[sale_count].subtotal = 0.0;
            sales[sale_count].tax_amount = 0.0;
            sales[sale_count].discount_amount = 0.0;
            sales[sale_count].total_amount = 0.0;
            strcpy(sales[sale_count].payment_method, "cash");
            strcpy(sales[sale_count].status, "pending");
            sales[sale_count].item_count = 0;

            // Add sale items
            char add_more = 'y';
            while(add_more == 'y' || add_more == 'Y') {
                printf("\nAvailable products:\n");
                for(int i = 0; i < product_count; i++) {
                    printf("%d. %s - $%.2f (Stock: %d)\n",
                           products[i].id, products[i].name, products[i].price, products[i].stock_quantity);
                }

                printf("Enter product ID: ");
                int product_id;
                scanf("%d", &product_id);
                getchar();

                int product_found = -1;
                for(int i = 0; i < product_count; i++) {
                    if(products[i].id == product_id) {
                        product_found = i;
                        break;
                    }
                }

                if(product_found == -1) {
                    printf("Product not found!\n");
                    continue;
                }

                printf("Enter quantity: ");
                int quantity;
                scanf("%d", &quantity);
                getchar();

                if(quantity > products[product_found].stock_quantity) {
                    printf("Insufficient stock! Available: %d\n", products[product_found].stock_quantity);
                    continue;
                }

                // Add sale item
                sale_items[sale_item_count].sale_id = sales[sale_count].id;
                sale_items[sale_item_count].product_id = product_id;
                sale_items[sale_item_count].quantity = quantity;
                sale_items[sale_item_count].unit_price = products[product_found].price;
                sale_items[sale_item_count].line_total = quantity * products[product_found].price;

                sales[sale_count].subtotal += sale_items[sale_item_count].line_total;
                sales[sale_count].item_count++;
                sale_item_count++;

                // Update inventory
                products[product_found].stock_quantity -= quantity;

                printf("Added %d x %s. Line total: $%.2f\n", quantity, products[product_found].name,
                       sale_items[sale_item_count-1].line_total);

                printf("Add another item? (y/n): ");
                scanf("%c", &add_more);
                getchar();
            }

            // Calculate totals
            sales[sale_count].tax_amount = calculate_tax(sales[sale_count].subtotal);

            // Apply customer discount based on membership
            double discount_rate = 0.0;
            if(strcmp(customers[customer_found].membership_level, "silver") == 0) discount_rate = 0.05;
            else if(strcmp(customers[customer_found].membership_level, "gold") == 0) discount_rate = 0.10;
            else if(strcmp(customers[customer_found].membership_level, "platinum") == 0) discount_rate = 0.15;

            sales[sale_count].discount_amount = sales[sale_count].subtotal * discount_rate;
            sales[sale_count].total_amount = sales[sale_count].subtotal + sales[sale_count].tax_amount - sales[sale_count].discount_amount;

            strcpy(sales[sale_count].status, "completed");

            // Update customer loyalty
            update_customer_loyalty(&customers[customer_found], sales[sale_count].total_amount);
            customers[customer_found].last_purchase = get_current_time();

            sale_count++;

            printf("\n✅ Sale completed successfully!\n");
            printf("Sale ID: %d\n", sales[sale_count-1].id);
            printf("Subtotal: $%.2f\n", sales[sale_count-1].subtotal);
            printf("Tax: $%.2f\n", sales[sale_count-1].tax_amount);
            printf("Discount: $%.2f\n", sales[sale_count-1].discount_amount);
            printf("Total: $%.2f\n", sales[sale_count-1].total_amount);
            break;
        }
        case 2: { // View Sales
            printf("\nSales History:\n");
            printf("==============\n");
            for(int i = 0; i < sale_count; i++) {
                char sale_date[20];
                format_date(sales[i].sale_date, sale_date, sizeof(sale_date));

                printf("Sale ID: %d | Date: %s\n", sales[i].id, sale_date);
                printf("Customer ID: %d | Items: %d\n", sales[i].customer_id, sales[i].item_count);
                printf("Total: $%.2f | Status: %s\n", sales[i].total_amount, sales[i].status);

                // Show sale items
                printf("Items:\n");
                for(int j = 0; j < sale_item_count; j++) {
                    if(sale_items[j].sale_id == sales[i].id) {
                        // Find product name
                        char product_name[MAX_NAME_LENGTH] = "Unknown";
                        for(int k = 0; k < product_count; k++) {
                            if(products[k].id == sale_items[j].product_id) {
                                strcpy(product_name, products[k].name);
                                break;
                            }
                        }
                        printf("  • %s x%d @ $%.2f = $%.2f\n",
                               product_name, sale_items[j].quantity,
                               sale_items[j].unit_price, sale_items[j].line_total);
                    }
                }
                printf("\n");
            }
            if(sale_count == 0) {
                printf("No sales found.\n");
            }
            break;
        }
        case 3: { // Sales by Date Range
            printf("\nEnter date range (YYYY-MM-DD):\n");
            printf("Start date: ");
            char start_date[11];
            fgets(start_date, sizeof(start_date), stdin);
            start_date[strcspn(start_date, "\n")] = 0;

            printf("End date: ");
            char end_date[11];
            fgets(end_date, sizeof(end_date), stdin);
            end_date[strcspn(end_date, "\n")] = 0;

            printf("\nSales from %s to %s:\n", start_date, end_date);
            double total_sales_amount = 0.0;
            int sales_count = 0;

            for(int i = 0; i < sale_count; i++) {
                char sale_date_str[11];
                format_date(sales[i].sale_date, sale_date_str, sizeof(sale_date_str));

                if(strcmp(sale_date_str, start_date) >= 0 && strcmp(sale_date_str, end_date) <= 0) {
                    printf("Sale ID %d: $%.2f on %s\n", sales[i].id, sales[i].total_amount, sale_date_str);
                    total_sales_amount += sales[i].total_amount;
                    sales_count++;
                }
            }

            printf("\nSummary: %d sales totaling $%.2f\n", sales_count, total_sales_amount);
            break;
        }
        case 4: { // Sales by Customer
            printf("\nEnter customer ID: ");
            int customer_id;
            scanf("%d", &customer_id);
            getchar();

            printf("\nSales for Customer ID %d:\n", customer_id);
            double total_customer_sales = 0.0;
            int customer_sales_count = 0;

            for(int i = 0; i < sale_count; i++) {
                if(sales[i].customer_id == customer_id) {
                    char sale_date[20];
                    format_date(sales[i].sale_date, sale_date, sizeof(sale_date));

                    printf("Sale ID %d: $%.2f on %s\n", sales[i].id, sales[i].total_amount, sale_date);
                    total_customer_sales += sales[i].total_amount;
                    customer_sales_count++;
                }
            }

            printf("\nTotal: %d sales amounting to $%.2f\n", customer_sales_count, total_customer_sales);
            break;
        }
        case 5:
            return;
        default:
            printf("Invalid choice!\n");
    }

    pause();
}

void manage_inventory() {
    clear_screen();
    printf("📊 INVENTORY MANAGEMENT 📊\n");
    printf("===========================\n\n");

    check_inventory_alerts();
    printf("\n");

    printf("Inventory Options:\n");
    printf("1. Stock Report\n");
    printf("2. Low Stock Alert\n");
    printf("3. Reorder Products\n");
    printf("4. Inventory Valuation\n");
    printf("5. Back to Main Menu\n\n");
    printf("Enter choice (1-5): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // Stock Report
            printf("\nComplete Stock Report:\n");
            printf("======================\n");
            printf("%-30s %-10s %-12s %-15s\n", "Product", "Stock", "Reorder", "Status");
            printf("%-30s %-10s %-12s %-15s\n", "------------------------------", "----------", "------------", "---------------");

            for(int i = 0; i < product_count; i++) {
                char status[15];
                if(products[i].stock_quantity == 0) {
                    strcpy(status, "OUT OF STOCK");
                } else if(products[i].stock_quantity <= products[i].reorder_level) {
                    strcpy(status, "LOW STOCK");
                } else {
                    strcpy(status, "IN STOCK");
                }

                printf("%-30s %-10d %-12d %-15s\n",
                       products[i].name, products[i].stock_quantity,
                       products[i].reorder_level, status);
            }
            break;
        }
        case 2: { // Low Stock Alert (already shown above)
            break;
        }
        case 3: { // Reorder Products
            printf("\nProducts needing reorder:\n");
            printf("=========================\n");

            int reorder_count = 0;
            for(int i = 0; i < product_count; i++) {
                if(products[i].stock_quantity <= products[i].reorder_level) {
                    printf("%d. %s (Current: %d, Reorder at: %d)\n",
                           i+1, products[i].name, products[i].stock_quantity, products[i].reorder_level);

                    printf("Enter reorder quantity for %s: ", products[i].name);
                    int reorder_qty;
                    scanf("%d", &reorder_qty);
                    getchar();

                    products[i].stock_quantity += reorder_qty;
                    products[i].last_updated = get_current_time();

                    printf("✅ Restocked %s with %d units\n", products[i].name, reorder_qty);
                    reorder_count++;
                }
            }

            if(reorder_count == 0) {
                printf("No products need reordering.\n");
            } else {
                printf("\n✅ Reordering completed for %d product(s).\n", reorder_count);
            }
            break;
        }
        case 4: { // Inventory Valuation
            printf("\nInventory Valuation:\n");
            printf("====================\n");

            double total_value = 0.0;
            double total_cost = 0.0;

            for(int i = 0; i < product_count; i++) {
                double product_value = products[i].stock_quantity * products[i].price;
                double product_cost = products[i].stock_quantity * products[i].cost;
                double profit_potential = product_value - product_cost;

                printf("%s:\n", products[i].name);
                printf("  Quantity: %d\n", products[i].stock_quantity);
                printf("  Retail Value: $%.2f\n", product_value);
                printf("  Cost Value: $%.2f\n", product_cost);
                printf("  Potential Profit: $%.2f\n\n", profit_potential);

                total_value += product_value;
                total_cost += product_cost;
            }

            printf("TOTALS:\n");
            printf("=======\n");
            printf("Total Retail Value: $%.2f\n", total_value);
            printf("Total Cost Value: $%.2f\n", total_cost);
            printf("Total Potential Profit: $%.2f\n", total_value - total_cost);
            break;
        }
        case 5:
            return;
        default:
            printf("Invalid choice!\n");
    }

    pause();
}

void manage_suppliers() {
    clear_screen();
    printf("🚚 SUPPLIER MANAGEMENT 🚚\n");
    printf("=========================\n\n");

    printf("Supplier Options:\n");
    printf("1. Add Supplier\n");
    printf("2. View Suppliers\n");
    printf("3. Update Supplier\n");
    printf("4. Supplier Performance\n");
    printf("5. Back to Main Menu\n\n");
    printf("Enter choice (1-5): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // Add Supplier
            if(supplier_count >= MAX_SUPPLIERS) {
                printf("Supplier limit reached!\n");
                pause();
                return;
            }

            printf("\nAdd New Supplier:\n");
            suppliers[supplier_count].id = generate_id();

            printf("Supplier name: ");
            fgets(suppliers[supplier_count].name, sizeof(suppliers[supplier_count].name), stdin);
            suppliers[supplier_count].name[strcspn(suppliers[supplier_count].name, "\n")] = 0;

            printf("Contact person: ");
            fgets(suppliers[supplier_count].contact_person, sizeof(suppliers[supplier_count].contact_person), stdin);
            suppliers[supplier_count].contact_person[strcspn(suppliers[supplier_count].contact_person, "\n")] = 0;

            printf("Email: ");
            fgets(suppliers[supplier_count].email, sizeof(suppliers[supplier_count].email), stdin);
            suppliers[supplier_count].email[strcspn(suppliers[supplier_count].email, "\n")] = 0;

            printf("Phone: ");
            fgets(suppliers[supplier_count].phone, sizeof(suppliers[supplier_count].phone), stdin);
            suppliers[supplier_count].phone[strcspn(suppliers[supplier_count].phone, "\n")] = 0;

            printf("Address: ");
            fgets(suppliers[supplier_count].address, sizeof(suppliers[supplier_count].address), stdin);
            suppliers[supplier_count].address[strcspn(suppliers[supplier_count].address, "\n")] = 0;

            suppliers[supplier_count].total_orders = 0.0;
            suppliers[supplier_count].last_order_date = 0;

            supplier_count++;
            printf("✅ Supplier added successfully! ID: %d\n", suppliers[supplier_count-1].id);
            break;
        }
        case 2: { // View Suppliers
            printf("\nSupplier Directory:\n");
            printf("===================\n");
            for(int i = 0; i < supplier_count; i++) {
                printf("ID: %d\n", suppliers[i].id);
                printf("Name: %s\n", suppliers[i].name);
                printf("Contact: %s\n", suppliers[i].contact_person);
                printf("Email: %s | Phone: %s\n", suppliers[i].email, suppliers[i].phone);
                printf("Total Orders: $%.2f\n", suppliers[i].total_orders);

                if(suppliers[i].last_order_date > 0) {
                    char last_order[20];
                    format_date(suppliers[i].last_order_date, last_order, sizeof(last_order));
                    printf("Last Order: %s\n", last_order);
                } else {
                    printf("Last Order: Never\n");
                }
                printf("\n");
            }
            if(supplier_count == 0) {
                printf("No suppliers found.\n");
            }
            break;
        }
        case 3: { // Update Supplier
            printf("\nEnter supplier ID to update: ");
            int supplier_id;
            scanf("%d", &supplier_id);
            getchar();

            int found = -1;
            for(int i = 0; i < supplier_count; i++) {
                if(suppliers[i].id == supplier_id) {
                    found = i;
                    break;
                }
            }

            if(found == -1) {
                printf("Supplier not found!\n");
                break;
            }

            printf("Update %s:\n", suppliers[found].name);
            printf("New contact person: ");
            fgets(suppliers[found].contact_person, sizeof(suppliers[found].contact_person), stdin);
            suppliers[found].contact_person[strcspn(suppliers[found].contact_person, "\n")] = 0;

            printf("New email: ");
            fgets(suppliers[found].email, sizeof(suppliers[found].email), stdin);
            suppliers[found].email[strcspn(suppliers[found].email, "\n")] = 0;

            printf("New phone: ");
            fgets(suppliers[found].phone, sizeof(suppliers[found].phone), stdin);
            suppliers[found].phone[strcspn(suppliers[found].phone, "\n")] = 0;

            printf("✅ Supplier updated successfully!\n");
            break;
        }
        case 4: { // Supplier Performance
            printf("\nSupplier Performance Report:\n");
            printf("=============================\n");

            for(int i = 0; i < supplier_count; i++) {
                printf("%s (ID: %d)\n", suppliers[i].name, suppliers[i].id);
                printf("Total Order Value: $%.2f\n", suppliers[i].total_orders);

                // Count products from this supplier
                int product_count_from_supplier = 0;
                for(int j = 0; j < product_count; j++) {
                    if(products[j].supplier_id == suppliers[i].id) {
                        product_count_from_supplier++;
                    }
                }

                printf("Products Supplied: %d\n", product_count_from_supplier);

                if(suppliers[i].last_order_date > 0) {
                    char last_order[20];
                    format_date(suppliers[i].last_order_date, last_order, sizeof(last_order));
                    printf("Last Order Date: %s\n", last_order);
                } else {
                    printf("Last Order Date: Never\n");
                }
                printf("\n");
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

void manage_employees() {
    clear_screen();
    printf("👷 EMPLOYEE MANAGEMENT 👷\n");
    printf("=========================\n\n");

    printf("Employee Options:\n");
    printf("1. Add Employee\n");
    printf("2. View Employees\n");
    printf("3. Update Employee\n");
    printf("4. Employee Performance\n");
    printf("5. Back to Main Menu\n\n");
    printf("Enter choice (1-5): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // Add Employee
            if(employee_count >= MAX_EMPLOYEES) {
                printf("Employee limit reached!\n");
                pause();
                return;
            }

            printf("\nAdd New Employee:\n");
            employees[employee_count].id = generate_id();

            printf("Employee name: ");
            fgets(employees[employee_count].name, sizeof(employees[employee_count].name), stdin);
            employees[employee_count].name[strcspn(employees[employee_count].name, "\n")] = 0;

            printf("Position: ");
            fgets(employees[employee_count].position, sizeof(employees[employee_count].position), stdin);
            employees[employee_count].position[strcspn(employees[employee_count].position, "\n")] = 0;

            printf("Department: ");
            fgets(employees[employee_count].department, sizeof(employees[employee_count].department), stdin);
            employees[employee_count].department[strcspn(employees[employee_count].department, "\n")] = 0;

            printf("Salary: $");
            scanf("%lf", &employees[employee_count].salary);
            getchar();

            employees[employee_count].hire_date = get_current_time();
            strcpy(employees[employee_count].status, "active");

            employee_count++;
            printf("✅ Employee added successfully! ID: %d\n", employees[employee_count-1].id);
            break;
        }
        case 2: { // View Employees
            printf("\nEmployee Directory:\n");
            printf("===================\n");
            for(int i = 0; i < employee_count; i++) {
                printf("ID: %d\n", employees[i].id);
                printf("Name: %s\n", employees[i].name);
                printf("Position: %s | Department: %s\n", employees[i].position, employees[i].department);
                printf("Salary: $%.2f/year\n", employees[i].salary);
                printf("Status: %s\n", employees[i].status);

                char hire_date[20];
                format_date(employees[i].hire_date, hire_date, sizeof(hire_date));
                printf("Hire Date: %s\n\n", hire_date);
            }
            if(employee_count == 0) {
                printf("No employees found.\n");
            }
            break;
        }
        case 3: { // Update Employee
            printf("\nEnter employee ID to update: ");
            int employee_id;
            scanf("%d", &employee_id);
            getchar();

            int found = -1;
            for(int i = 0; i < employee_count; i++) {
                if(employees[i].id == employee_id) {
                    found = i;
                    break;
                }
            }

            if(found == -1) {
                printf("Employee not found!\n");
                break;
            }

            printf("Update %s:\n", employees[found].name);
            printf("New position: ");
            fgets(employees[found].position, sizeof(employees[found].position), stdin);
            employees[found].position[strcspn(employees[found].position, "\n")] = 0;

            printf("New department: ");
            fgets(employees[found].department, sizeof(employees[found].department), stdin);
            employees[found].department[strcspn(employees[found].department, "\n")] = 0;

            printf("New salary: $");
            scanf("%lf", &employees[found].salary);
            getchar();

            printf("✅ Employee updated successfully!\n");
            break;
        }
        case 4: { // Employee Performance
            printf("\nEmployee Performance Report:\n");
            printf("=============================\n");

            for(int i = 0; i < employee_count; i++) {
                printf("%s (ID: %d)\n", employees[i].name, employees[i].id);
                printf("Position: %s | Department: %s\n", employees[i].position, employees[i].department);
                printf("Salary: $%.2f/year\n", employees[i].salary);

                // Count sales by this employee
                int employee_sales = 0;
                double employee_revenue = 0.0;
                for(int j = 0; j < sale_count; j++) {
                    if(sales[j].employee_id == employees[i].id) {
                        employee_sales++;
                        employee_revenue += sales[j].total_amount;
                    }
                }

                printf("Sales Made: %d\n", employee_sales);
                printf("Revenue Generated: $%.2f\n", employee_revenue);

                if(employee_sales > 0) {
                    printf("Average Sale: $%.2f\n", employee_revenue / employee_sales);
                }

                char hire_date[20];
                format_date(employees[i].hire_date, hire_date, sizeof(hire_date));
                printf("Hire Date: %s\n", hire_date);
                printf("Status: %s\n\n", employees[i].status);
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

void generate_reports() {
    clear_screen();
    printf("📈 BUSINESS REPORTS 📈\n");
    printf("======================\n\n");

    printf("Report Options:\n");
    printf("1. Sales Report\n");
    printf("2. Inventory Report\n");
    printf("3. Customer Report\n");
    printf("4. Financial Summary\n");
    printf("5. Back to Main Menu\n\n");
    printf("Enter choice (1-5): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // Sales Report
            printf("\nSALES REPORT\n");
            printf("============\n");

            double total_revenue = 0.0;
            double total_cost = 0.0;
            int total_items_sold = 0;

            for(int i = 0; i < sale_count; i++) {
                total_revenue += sales[i].total_amount;

                // Calculate cost of goods sold
                for(int j = 0; j < sale_item_count; j++) {
                    if(sale_items[j].sale_id == sales[i].id) {
                        // Find product cost
                        for(int k = 0; k < product_count; k++) {
                            if(products[k].id == sale_items[j].product_id) {
                                total_cost += sale_items[j].quantity * products[k].cost;
                                total_items_sold += sale_items[j].quantity;
                                break;
                            }
                        }
                    }
                }
            }

            printf("Total Sales: %d\n", sale_count);
            printf("Total Revenue: $%.2f\n", total_revenue);
            printf("Cost of Goods Sold: $%.2f\n", total_cost);
            printf("Gross Profit: $%.2f\n", total_revenue - total_cost);
            printf("Profit Margin: %.1f%%\n", ((total_revenue - total_cost) / total_revenue) * 100);
            printf("Items Sold: %d\n", total_items_sold);

            if(sale_count > 0) {
                printf("Average Order Value: $%.2f\n", total_revenue / sale_count);
            }
            break;
        }
        case 2: { // Inventory Report
            printf("\nINVENTORY REPORT\n");
            printf("=================\n");

            double total_inventory_value = 0.0;
            double total_inventory_cost = 0.0;
            int low_stock_items = 0;
            int out_of_stock_items = 0;

            for(int i = 0; i < product_count; i++) {
                total_inventory_value += products[i].stock_quantity * products[i].price;
                total_inventory_cost += products[i].stock_quantity * products[i].cost;

                if(products[i].stock_quantity == 0) out_of_stock_items++;
                else if(products[i].stock_quantity <= products[i].reorder_level) low_stock_items++;
            }

            printf("Total Products: %d\n", product_count);
            printf("Inventory Value: $%.2f\n", total_inventory_value);
            printf("Inventory Cost: $%.2f\n", total_inventory_cost);
            printf("Potential Profit: $%.2f\n", total_inventory_value - total_inventory_cost);
            printf("Low Stock Items: %d\n", low_stock_items);
            printf("Out of Stock Items: %d\n", out_of_stock_items);
            break;
        }
        case 3: { // Customer Report
            printf("\nCUSTOMER REPORT\n");
            printf("===============\n");

            double total_customer_spending = 0.0;
            int active_customers = 0;

            for(int i = 0; i < customer_count; i++) {
                total_customer_spending += customers[i].total_purchases;
                if(customers[i].last_purchase > 0) active_customers++;
            }

            printf("Total Customers: %d\n", customer_count);
            printf("Active Customers: %d\n", active_customers);
            printf("Total Customer Spending: $%.2f\n", total_customer_spending);

            if(customer_count > 0) {
                printf("Average Customer Value: $%.2f\n", total_customer_spending / customer_count);
            }

            printf("\nMembership Breakdown:\n");
            int bronze = 0, silver = 0, gold = 0, platinum = 0;
            for(int i = 0; i < customer_count; i++) {
                if(strcmp(customers[i].membership_level, "bronze") == 0) bronze++;
                else if(strcmp(customers[i].membership_level, "silver") == 0) silver++;
                else if(strcmp(customers[i].membership_level, "gold") == 0) gold++;
                else if(strcmp(customers[i].membership_level, "platinum") == 0) platinum++;
            }

            printf("Bronze: %d | Silver: %d | Gold: %d | Platinum: %d\n", bronze, silver, gold, platinum);
            break;
        }
        case 4: { // Financial Summary
            printf("\nFINANCIAL SUMMARY\n");
            printf("=================\n");

            double total_revenue = 0.0, total_cost = 0.0, total_tax = 0.0, total_discounts = 0.0;

            for(int i = 0; i < sale_count; i++) {
                total_revenue += sales[i].total_amount;
                total_cost += sales[i].subtotal - (sales[i].subtotal * 0.3); // Estimate 30% cost of goods
                total_tax += sales[i].tax_amount;
                total_discounts += sales[i].discount_amount;
            }

            double net_profit = total_revenue - total_cost - total_tax;

            printf("Revenue: $%.2f\n", total_revenue);
            printf("Cost of Goods: $%.2f\n", total_cost);
            printf("Taxes: $%.2f\n", total_tax);
            printf("Discounts: $%.2f\n", total_discounts);
            printf("Net Profit: $%.2f\n", net_profit);
            printf("Profit Margin: %.1f%%\n", (net_profit / total_revenue) * 100);
            break;
        }
        case 5:
            return;
        default:
            printf("Invalid choice!\n");
    }

    pause();
}

void business_analytics() {
    clear_screen();
    printf("📊 BUSINESS ANALYTICS 📊\n");
    printf("========================\n\n");

    // Calculate key metrics
    double total_revenue = 0.0;
    double total_cost = 0.0;
    int total_transactions = sale_count;

    for(int i = 0; i < sale_count; i++) {
        total_revenue += sales[i].total_amount;
        // Estimate cost as 70% of revenue (rough estimate)
        total_cost += sales[i].subtotal * 0.7;
    }

    double net_profit = total_revenue - total_cost;
    double profit_margin = (net_profit / total_revenue) * 100;

    printf("KEY PERFORMANCE INDICATORS\n");
    printf("===========================\n");
    printf("Total Revenue: $%.2f\n", total_revenue);
    printf("Total Cost: $%.2f\n", total_cost);
    printf("Net Profit: $%.2f\n", net_profit);
    printf("Profit Margin: %.1f%%\n", profit_margin);
    printf("Total Transactions: %d\n", total_transactions);

    if(total_transactions > 0) {
        printf("Average Transaction Value: $%.2f\n", total_revenue / total_transactions);
    }

    printf("\nBUSINESS HEALTH METRICS\n");
    printf("========================\n");

    // Customer metrics
    int active_customers = 0;
    double total_customer_value = 0.0;
    for(int i = 0; i < customer_count; i++) {
        total_customer_value += customers[i].total_purchases;
        if(customers[i].last_purchase > (get_current_time() - (30 * 24 * 60 * 60))) { // Last 30 days
            active_customers++;
        }
    }

    printf("Total Customers: %d\n", customer_count);
    printf("Active Customers (30 days): %d\n", active_customers);
    printf("Customer Retention Rate: %.1f%%\n", ((double)active_customers / customer_count) * 100);

    if(customer_count > 0) {
        printf("Average Customer Lifetime Value: $%.2f\n", total_customer_value / customer_count);
    }

    // Inventory metrics
    int low_stock_products = 0;
    int out_of_stock_products = 0;
    double inventory_value = 0.0;

    for(int i = 0; i < product_count; i++) {
        inventory_value += products[i].stock_quantity * products[i].price;
        if(products[i].stock_quantity == 0) out_of_stock_products++;
        else if(products[i].stock_quantity <= products[i].reorder_level) low_stock_products++;
    }

    printf("\nINVENTORY METRICS\n");
    printf("==================\n");
    printf("Total Products: %d\n", product_count);
    printf("Inventory Value: $%.2f\n", inventory_value);
    printf("Low Stock Products: %d\n", low_stock_products);
    printf("Out of Stock Products: %d\n", out_of_stock_products);
    printf("Stock Health: %.1f%%\n", ((double)(product_count - low_stock_products - out_of_stock_products) / product_count) * 100);

    // Sales trends (simple analysis)
    printf("\nSALES TRENDS\n");
    printf("=============\n");

    // Group sales by month (simplified)
    double monthly_sales[12] = {0};
    for(int i = 0; i < sale_count; i++) {
        struct tm *timeinfo = localtime(&sales[i].sale_date);
        int month = timeinfo->tm_mon;
        monthly_sales[month] += sales[i].total_amount;
    }

    printf("Monthly Sales Breakdown:\n");
    char *months[] = {"Jan", "Feb", "Mar", "Apr", "May", "Jun",
                     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"};

    for(int i = 0; i < 12; i++) {
        if(monthly_sales[i] > 0) {
            printf("%s: $%.2f\n", months[i], monthly_sales[i]);
        }
    }

    // Recommendations
    printf("\n📋 BUSINESS RECOMMENDATIONS\n");
    printf("============================\n");

    if(profit_margin < 20) {
        printf("• Consider increasing prices or reducing costs to improve profit margins\n");
    }

    if(low_stock_products > product_count * 0.2) {
        printf("• High number of low-stock items - consider bulk ordering\n");
    }

    if(active_customers < customer_count * 0.7) {
        printf("• Customer retention could be improved - consider loyalty programs\n");
    }

    if(total_transactions < 50) {
        printf("• Low transaction volume - consider marketing campaigns\n");
    }

    printf("• Monitor inventory levels regularly to prevent stockouts\n");
    printf("• Focus on high-value customers for personalized service\n");
    printf("• Analyze sales trends to optimize product offerings\n");

    pause();
}

void system_backup() {
    clear_screen();
    printf("💾 SYSTEM BACKUP 💾\n");
    printf("===================\n\n");

    printf("Backup Options:\n");
    printf("1. Export All Data\n");
    printf("2. Import Data\n");
    printf("3. Clear All Data\n");
    printf("4. System Statistics\n");
    printf("5. Back to Main Menu\n\n");
    printf("Enter choice (1-5): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // Export All Data
            char filename[100];
            printf("Enter backup filename (without extension): ");
            fgets(filename, sizeof(filename), stdin);
            filename[strcspn(filename, "\n")] = 0;
            strcat(filename, ".backup");

            FILE *file = fopen(filename, "w");
            if(file == NULL) {
                printf("Error creating backup file!\n");
                break;
            }

            // Export products
            fprintf(file, "PRODUCTS %d\n", product_count);
            for(int i = 0; i < product_count; i++) {
                fprintf(file, "%d|%s|%s|%.2f|%.2f|%d|%d|%s|%d|%ld|%ld\n",
                        products[i].id, products[i].name, products[i].description,
                        products[i].price, products[i].cost, products[i].stock_quantity,
                        products[i].reorder_level, products[i].category, products[i].supplier_id,
                        products[i].created_date, products[i].last_updated);
            }

            // Export customers
            fprintf(file, "CUSTOMERS %d\n", customer_count);
            for(int i = 0; i < customer_count; i++) {
                fprintf(file, "%d|%s|%s|%s|%s|%.2f|%d|%s|%ld|%ld\n",
                        customers[i].id, customers[i].name, customers[i].email,
                        customers[i].phone, customers[i].address, customers[i].total_purchases,
                        customers[i].loyalty_points, customers[i].membership_level,
                        customers[i].registration_date, customers[i].last_purchase);
            }

            // Export sales and sale items
            fprintf(file, "SALES %d\n", sale_count);
            for(int i = 0; i < sale_count; i++) {
                fprintf(file, "%d|%d|%d|%ld|%.2f|%.2f|%.2f|%.2f|%s|%s|%d\n",
                        sales[i].id, sales[i].customer_id, sales[i].employee_id, sales[i].sale_date,
                        sales[i].subtotal, sales[i].tax_amount, sales[i].discount_amount,
                        sales[i].total_amount, sales[i].payment_method, sales[i].status, sales[i].item_count);
            }

            fprintf(file, "SALE_ITEMS %d\n", sale_item_count);
            for(int i = 0; i < sale_item_count; i++) {
                fprintf(file, "%d|%d|%d|%.2f|%.2f\n",
                        sale_items[i].sale_id, sale_items[i].product_id, sale_items[i].quantity,
                        sale_items[i].unit_price, sale_items[i].line_total);
            }

            // Export suppliers
            fprintf(file, "SUPPLIERS %d\n", supplier_count);
            for(int i = 0; i < supplier_count; i++) {
                fprintf(file, "%d|%s|%s|%s|%s|%s|%.2f|%ld\n",
                        suppliers[i].id, suppliers[i].name, suppliers[i].contact_person,
                        suppliers[i].email, suppliers[i].phone, suppliers[i].address,
                        suppliers[i].total_orders, suppliers[i].last_order_date);
            }

            // Export employees
            fprintf(file, "EMPLOYEES %d\n", employee_count);
            for(int i = 0; i < employee_count; i++) {
                fprintf(file, "%d|%s|%s|%.2f|%s|%ld|%s\n",
                        employees[i].id, employees[i].name, employees[i].position,
                        employees[i].salary, employees[i].department, employees[i].hire_date,
                        employees[i].status);
            }

            fclose(file);
            printf("✅ System backup created: %s\n", filename);
            break;
        }
        case 2: { // Import Data
            printf("⚠️  Import will overwrite existing data. Continue? (y/n): ");
            char confirm;
            scanf("%c", &confirm);
            getchar();

            if(confirm != 'y' && confirm != 'Y') {
                printf("Import cancelled.\n");
                break;
            }

            char filename[100];
            printf("Enter backup filename (without extension): ");
            fgets(filename, sizeof(filename), stdin);
            filename[strcspn(filename, "\n")] = 0;
            strcat(filename, ".backup");

            FILE *file = fopen(filename, "r");
            if(file == NULL) {
                printf("Backup file not found!\n");
                break;
            }

            // Reset counters
            product_count = customer_count = sale_count = sale_item_count = supplier_count = employee_count = 0;

            char line[1000];
            while(fgets(line, sizeof(line), file)) {
                char section[20];
                int count;

                if(sscanf(line, "%s %d", section, &count) == 2) {
                    if(strcmp(section, "PRODUCTS") == 0) {
                        for(int i = 0; i < count; i++) {
                            fgets(line, sizeof(line), file);
                            sscanf(line, "%d|%[^|]|%[^|]|%lf|%lf|%d|%d|%[^|]|%d|%ld|%ld",
                                   &products[product_count].id, products[product_count].name,
                                   products[product_count].description, &products[product_count].price,
                                   &products[product_count].cost, &products[product_count].stock_quantity,
                                   &products[product_count].reorder_level, products[product_count].category,
                                   &products[product_count].supplier_id, &products[product_count].created_date,
                                   &products[product_count].last_updated);
                            product_count++;
                        }
                    } else if(strcmp(section, "CUSTOMERS") == 0) {
                        for(int i = 0; i < count; i++) {
                            fgets(line, sizeof(line), file);
                            sscanf(line, "%d|%[^|]|%[^|]|%[^|]|%[^|]|%lf|%d|%[^|]|%ld|%ld",
                                   &customers[customer_count].id, customers[customer_count].name,
                                   customers[customer_count].email, customers[customer_count].phone,
                                   customers[customer_count].address, &customers[customer_count].total_purchases,
                                   &customers[customer_count].loyalty_points, customers[customer_count].membership_level,
                                   &customers[customer_count].registration_date, &customers[customer_count].last_purchase);
                            customer_count++;
                        }
                    }
                    // Add similar parsing for other sections...
                }
            }

            fclose(file);
            printf("✅ Data imported successfully!\n");
            break;
        }
        case 3: { // Clear All Data
            printf("⚠️  This will delete ALL data. Are you sure? (type 'DELETE' to confirm): ");
            char confirmation[10];
            fgets(confirmation, sizeof(confirmation), stdin);
            confirmation[strcspn(confirmation, "\n")] = 0;

            if(strcmp(confirmation, "DELETE") == 0) {
                product_count = customer_count = sale_count = sale_item_count = supplier_count = employee_count = 0;
                printf("✅ All data cleared!\n");
            } else {
                printf("Clear operation cancelled.\n");
            }
            break;
        }
        case 4: { // System Statistics
            printf("\nSYSTEM STATISTICS\n");
            printf("=================\n");
            printf("Products: %d\n", product_count);
            printf("Customers: %d\n", customer_count);
            printf("Sales: %d\n", sale_count);
            printf("Sale Items: %d\n", sale_item_count);
            printf("Suppliers: %d\n", supplier_count);
            printf("Employees: %d\n", employee_count);

            // Memory usage estimate
            size_t memory_used = (product_count * sizeof(Product)) +
                               (customer_count * sizeof(Customer)) +
                               (sale_count * sizeof(Sale)) +
                               (sale_item_count * sizeof(SaleItem)) +
                               (supplier_count * sizeof(Supplier)) +
                               (employee_count * sizeof(Employee));

            printf("Estimated Memory Usage: %.2f KB\n", memory_used / 1024.0);

            // Data integrity check
            int integrity_errors = 0;
            for(int i = 0; i < sale_count; i++) {
                int customer_found = 0;
                for(int j = 0; j < customer_count; j++) {
                    if(customers[j].id == sales[i].customer_id) {
                        customer_found = 1;
                        break;
                    }
                }
                if(!customer_found) integrity_errors++;
            }

            printf("Data Integrity: %s\n", integrity_errors == 0 ? "GOOD" : "ISSUES FOUND");
            if(integrity_errors > 0) {
                printf("Integrity Errors: %d\n", integrity_errors);
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

int main() {
    initialize_sample_data();

    int choice;
    do {
        display_main_menu();
        scanf("%d", &choice);
        getchar(); // consume newline

        switch(choice) {
            case 1:
                manage_products();
                break;
            case 2:
                manage_customers();
                break;
            case 3:
                manage_sales();
                break;
            case 4:
                manage_inventory();
                break;
            case 5:
                manage_suppliers();
                break;
            case 6:
                manage_employees();
                break;
            case 7:
                generate_reports();
                break;
            case 8:
                business_analytics();
                break;
            case 9:
                system_backup();
                break;
            case 0:
                printf("\nThank you for using the Comprehensive Business Management System! 🏢\n");
                break;
            default:
                printf("Invalid choice! Please enter 0-9.\n");
                pause();
        }
    } while(choice != 0);

    return 0;
}