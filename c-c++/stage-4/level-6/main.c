#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include <math.h>

// Constants
#define MAX_RECORDS 1000
#define MAX_FIELDS 20
#define MAX_FIELD_NAME_LENGTH 50
#define MAX_DATA_LENGTH 100
#define MAX_AUTOMATION_RULES 50
#define MAX_REPORTS 20
#define MAX_SCHEDULES 10

// Data Structures
typedef struct {
    char name[MAX_FIELD_NAME_LENGTH];
    char type[20]; // string, int, float, date
    int required;
} FieldDefinition;

typedef struct {
    char data[MAX_FIELDS][MAX_DATA_LENGTH];
    int field_count;
} DataRecord;

typedef struct {
    char name[MAX_FIELD_NAME_LENGTH];
    char condition[100]; // e.g., "age > 18", "status == 'active'"
    char action[100]; // e.g., "set discount = 10", "flag = true"
} AutomationRule;

typedef struct {
    char name[100];
    char type[50]; // summary, detailed, chart, export
    char data_source[100];
    char filters[200];
    char schedule[50]; // daily, weekly, monthly, manual
    time_t last_run;
} AutomatedReport;

typedef struct {
    char name[100];
    char operation[100]; // import, process, export, cleanup
    char parameters[200];
    char schedule[50]; // hourly, daily, weekly, monthly
    int enabled;
    time_t last_run;
    time_t next_run;
} AutomationSchedule;

typedef struct {
    FieldDefinition fields[MAX_FIELDS];
    DataRecord records[MAX_RECORDS];
    int field_count;
    int record_count;
    char name[100];
} DataSet;

// Global Variables
DataSet datasets[MAX_SCHEDULES];
int dataset_count = 0;
AutomationRule rules[MAX_AUTOMATION_RULES];
int rule_count = 0;
AutomatedReport reports[MAX_REPORTS];
int report_count = 0;
AutomationSchedule schedules[MAX_SCHEDULES];
int schedule_count = 0;

// Function Prototypes
void initialize_sample_data();
void display_main_menu();
void manage_datasets();
void manage_automation_rules();
void manage_automated_reports();
void manage_automation_schedules();
void run_automation();
void generate_reports();
void import_data();
void export_data();
void batch_process_data();

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

int evaluate_condition(const char *condition, DataRecord *record, DataSet *dataset) {
    // Simple condition evaluation - in a real system, this would be more sophisticated
    // For now, we'll implement basic string and numeric comparisons

    char field_name[MAX_FIELD_NAME_LENGTH];
    char operator[5];
    char value[MAX_DATA_LENGTH];

    // Parse condition like "age > 18" or "status == 'active'"
    if(sscanf(condition, "%s %s %s", field_name, operator, value) == 3) {
        // Find field index
        int field_index = -1;
        for(int i = 0; i < dataset->field_count; i++) {
            if(strcmp(dataset->fields[i].name, field_name) == 0) {
                field_index = i;
                break;
            }
        }

        if(field_index == -1) return 0;

        const char *field_value = record->data[field_index];

        // Remove quotes from value if present
        char clean_value[MAX_DATA_LENGTH];
        strcpy(clean_value, value);
        if(clean_value[0] == '\'') {
            memmove(clean_value, clean_value + 1, strlen(clean_value));
            if(clean_value[strlen(clean_value) - 1] == '\'') {
                clean_value[strlen(clean_value) - 1] = '\0';
            }
        }

        // Numeric comparison
        if(strcmp(dataset->fields[field_index].type, "int") == 0 ||
           strcmp(dataset->fields[field_index].type, "float") == 0) {
            double field_num = atof(field_value);
            double compare_num = atof(clean_value);

            if(strcmp(operator, ">") == 0) return field_num > compare_num;
            if(strcmp(operator, "<") == 0) return field_num < compare_num;
            if(strcmp(operator, ">=") == 0) return field_num >= compare_num;
            if(strcmp(operator, "<=") == 0) return field_num <= compare_num;
            if(strcmp(operator, "==") == 0) return field_num == compare_num;
            if(strcmp(operator, "!=") == 0) return field_num != compare_num;
        }
        // String comparison
        else {
            if(strcmp(operator, "==") == 0) return strcmp(field_value, clean_value) == 0;
            if(strcmp(operator, "!=") == 0) return strcmp(field_value, clean_value) != 0;
        }
    }

    return 0;
}

void apply_action(const char *action, DataRecord *record, DataSet *dataset) {
    // Simple action application - set field values
    char field_name[MAX_FIELD_NAME_LENGTH];
    char value[MAX_DATA_LENGTH];

    // Parse action like "discount = 10" or "status = 'approved'"
    if(sscanf(action, "%s = %s", field_name, value) == 2) {
        // Find field index
        int field_index = -1;
        for(int i = 0; i < dataset->field_count; i++) {
            if(strcmp(dataset->fields[i].name, field_name) == 0) {
                field_index = i;
                break;
            }
        }

        if(field_index != -1) {
            // Remove quotes from value if present
            char clean_value[MAX_DATA_LENGTH];
            strcpy(clean_value, value);
            if(clean_value[0] == '\'') {
                memmove(clean_value, clean_value + 1, strlen(clean_value));
                if(clean_value[strlen(clean_value) - 1] == '\'') {
                    clean_value[strlen(clean_value) - 1] = '\0';
                }
            }

            strcpy(record->data[field_index], clean_value);
        }
    }
}

// Core Functions
void initialize_sample_data() {
    // Create sample dataset
    strcpy(datasets[0].name, "Customer_Data");
    datasets[0].field_count = 5;
    datasets[0].record_count = 0;

    // Define fields
    strcpy(datasets[0].fields[0].name, "customer_id");
    strcpy(datasets[0].fields[0].type, "int");
    datasets[0].fields[0].required = 1;

    strcpy(datasets[0].fields[1].name, "name");
    strcpy(datasets[0].fields[1].type, "string");
    datasets[0].fields[1].required = 1;

    strcpy(datasets[0].fields[2].name, "age");
    strcpy(datasets[0].fields[2].type, "int");
    datasets[0].fields[2].required = 1;

    strcpy(datasets[0].fields[3].name, "status");
    strcpy(datasets[0].fields[3].type, "string");
    datasets[0].fields[3].required = 0;

    strcpy(datasets[0].fields[4].name, "discount");
    strcpy(datasets[0].fields[4].type, "float");
    datasets[0].fields[4].required = 0;

    // Add sample records
    strcpy(datasets[0].records[0].data[0], "1");
    strcpy(datasets[0].records[0].data[1], "John Doe");
    strcpy(datasets[0].records[0].data[2], "25");
    strcpy(datasets[0].records[0].data[3], "active");
    strcpy(datasets[0].records[0].data[4], "0.0");
    datasets[0].records[0].field_count = 5;

    strcpy(datasets[0].records[1].data[0], "2");
    strcpy(datasets[0].records[1].data[1], "Jane Smith");
    strcpy(datasets[0].records[1].data[2], "35");
    strcpy(datasets[0].records[1].data[3], "active");
    strcpy(datasets[0].records[1].data[4], "0.0");
    datasets[0].records[1].field_count = 5;

    strcpy(datasets[0].records[2].data[0], "3");
    strcpy(datasets[0].records[2].data[1], "Bob Johnson");
    strcpy(datasets[0].records[2].data[2], "45");
    strcpy(datasets[0].records[2].data[3], "inactive");
    strcpy(datasets[0].records[2].data[4], "0.0");
    datasets[0].records[2].field_count = 5;

    datasets[0].record_count = 3;
    dataset_count = 1;

    // Sample automation rules
    strcpy(rules[0].name, "Senior Discount");
    strcpy(rules[0].condition, "age >= 65");
    strcpy(rules[0].action, "discount = 15.0");

    strcpy(rules[1].name, "Loyalty Discount");
    strcpy(rules[1].condition, "age >= 30");
    strcpy(rules[1].action, "discount = 10.0");

    strcpy(rules[2].name, "Activate Senior");
    strcpy(rules[2].condition, "age >= 65");
    strcpy(rules[2].action, "status = 'senior'");

    rule_count = 3;

    // Sample automated reports
    strcpy(reports[0].name, "Customer Summary");
    strcpy(reports[0].type, "summary");
    strcpy(reports[0].data_source, "Customer_Data");
    strcpy(reports[0].filters, "status == 'active'");
    strcpy(reports[0].schedule, "weekly");
    reports[0].last_run = 0;

    strcpy(reports[1].name, "Discount Analysis");
    strcpy(reports[1].type, "detailed");
    strcpy(reports[1].data_source, "Customer_Data");
    strcpy(reports[1].filters, "discount > 0");
    strcpy(reports[1].schedule, "monthly");
    reports[1].last_run = 0;

    report_count = 2;

    // Sample automation schedules
    strcpy(schedules[0].name, "Daily Data Processing");
    strcpy(schedules[0].operation, "process");
    strcpy(schedules[0].parameters, "apply_rules");
    strcpy(schedules[0].schedule, "daily");
    schedules[0].enabled = 1;
    schedules[0].last_run = 0;
    schedules[0].next_run = get_current_time() + 86400; // 24 hours

    strcpy(schedules[1].name, "Weekly Report Generation");
    strcpy(schedules[1].operation, "generate_reports");
    strcpy(schedules[1].parameters, "all");
    strcpy(schedules[1].schedule, "weekly");
    schedules[1].enabled = 1;
    schedules[1].last_run = 0;
    schedules[1].next_run = get_current_time() + 604800; // 7 days

    schedule_count = 2;
}

void display_main_menu() {
    clear_screen();
    printf("🤖 AUTOMATED DATA PROCESSOR 🤖\n");
    printf("===============================\n\n");
    printf("Main Menu:\n");
    printf("1. 📊 Manage Datasets\n");
    printf("2. ⚙️  Manage Automation Rules\n");
    printf("3. 📋 Manage Automated Reports\n");
    printf("4. ⏰ Manage Automation Schedules\n");
    printf("5. ▶️  Run Automation\n");
    printf("6. 📄 Generate Reports\n");
    printf("7. 📥 Import Data\n");
    printf("8. 📤 Export Data\n");
    printf("9. 🔄 Batch Process Data\n");
    printf("0. 🚪 Exit\n\n");
    printf("Enter your choice (0-9): ");
}

void manage_datasets() {
    clear_screen();
    printf("📊 DATASET MANAGEMENT 📊\n");
    printf("=========================\n\n");

    printf("Dataset Options:\n");
    printf("1. Create Dataset\n");
    printf("2. View Datasets\n");
    printf("3. Add Records\n");
    printf("4. View Records\n");
    printf("5. Back to Main Menu\n\n");
    printf("Enter choice (1-5): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // Create Dataset
            if(dataset_count >= MAX_SCHEDULES) {
                printf("Dataset limit reached!\n");
                pause();
                return;
            }

            printf("\nCreate New Dataset:\n");
            printf("Dataset name: ");
            fgets(datasets[dataset_count].name, sizeof(datasets[dataset_count].name), stdin);
            datasets[dataset_count].name[strcspn(datasets[dataset_count].name, "\n")] = 0;

            printf("Number of fields: ");
            scanf("%d", &datasets[dataset_count].field_count);
            getchar();

            for(int i = 0; i < datasets[dataset_count].field_count; i++) {
                printf("Field %d name: ", i+1);
                fgets(datasets[dataset_count].fields[i].name, sizeof(datasets[dataset_count].fields[i].name), stdin);
                datasets[dataset_count].fields[i].name[strcspn(datasets[dataset_count].fields[i].name, "\n")] = 0;

                printf("Field %d type (string/int/float/date): ", i+1);
                fgets(datasets[dataset_count].fields[i].type, sizeof(datasets[dataset_count].fields[i].type), stdin);
                datasets[dataset_count].fields[i].type[strcspn(datasets[dataset_count].fields[i].type, "\n")] = 0;

                printf("Field %d required (1=yes, 0=no): ", i+1);
                scanf("%d", &datasets[dataset_count].fields[i].required);
                getchar();
            }

            datasets[dataset_count].record_count = 0;
            dataset_count++;

            printf("✅ Dataset created successfully!\n");
            break;
        }
        case 2: { // View Datasets
            printf("\nAvailable Datasets:\n");
            printf("===================\n");
            for(int i = 0; i < dataset_count; i++) {
                printf("%d. %s (%d fields, %d records)\n",
                       i+1, datasets[i].name, datasets[i].field_count, datasets[i].record_count);
            }
            if(dataset_count == 0) {
                printf("No datasets found.\n");
            }
            break;
        }
        case 3: { // Add Records
            printf("\nSelect dataset (1-%d): ", dataset_count);
            int dataset_choice;
            scanf("%d", &dataset_choice);
            getchar();

            if(dataset_choice < 1 || dataset_choice > dataset_count) {
                printf("Invalid dataset choice!\n");
                break;
            }

            DataSet *dataset = &datasets[dataset_choice - 1];

            if(dataset->record_count >= MAX_RECORDS) {
                printf("Record limit reached for this dataset!\n");
                break;
            }

            printf("\nAdd Record to %s:\n", dataset->name);
            for(int i = 0; i < dataset->field_count; i++) {
                printf("%s (%s): ", dataset->fields[i].name, dataset->fields[i].type);
                fgets(dataset->records[dataset->record_count].data[i],
                      sizeof(dataset->records[dataset->record_count].data[i]), stdin);
                dataset->records[dataset->record_count].data[i]
                    [strcspn(dataset->records[dataset->record_count].data[i], "\n")] = 0;
            }

            dataset->records[dataset->record_count].field_count = dataset->field_count;
            dataset->record_count++;

            printf("✅ Record added successfully!\n");
            break;
        }
        case 4: { // View Records
            printf("\nSelect dataset (1-%d): ", dataset_count);
            int dataset_choice;
            scanf("%d", &dataset_choice);
            getchar();

            if(dataset_choice < 1 || dataset_choice > dataset_count) {
                printf("Invalid dataset choice!\n");
                break;
            }

            DataSet *dataset = &datasets[dataset_choice - 1];

            printf("\nRecords in %s:\n", dataset->name);
            printf("================\n");

            // Print header
            for(int i = 0; i < dataset->field_count; i++) {
                printf("%s", dataset->fields[i].name);
                if(i < dataset->field_count - 1) printf(" | ");
            }
            printf("\n");

            // Print separator
            for(int i = 0; i < dataset->field_count; i++) {
                for(int j = 0; j < strlen(dataset->fields[i].name); j++) printf("-");
                if(i < dataset->field_count - 1) printf("-+-");
            }
            printf("\n");

            // Print records
            for(int i = 0; i < dataset->record_count; i++) {
                for(int j = 0; j < dataset->field_count; j++) {
                    printf("%s", dataset->records[i].data[j]);
                    if(j < dataset->field_count - 1) printf(" | ");
                }
                printf("\n");
            }

            if(dataset->record_count == 0) {
                printf("No records found.\n");
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

void manage_automation_rules() {
    clear_screen();
    printf("⚙️  AUTOMATION RULES MANAGEMENT ⚙️\n");
    printf("===================================\n\n");

    printf("Rules Options:\n");
    printf("1. Add Rule\n");
    printf("2. View Rules\n");
    printf("3. Test Rule\n");
    printf("4. Back to Main Menu\n\n");
    printf("Enter choice (1-4): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // Add Rule
            if(rule_count >= MAX_AUTOMATION_RULES) {
                printf("Rule limit reached!\n");
                pause();
                return;
            }

            printf("\nAdd Automation Rule:\n");
            printf("Rule name: ");
            fgets(rules[rule_count].name, sizeof(rules[rule_count].name), stdin);
            rules[rule_count].name[strcspn(rules[rule_count].name, "\n")] = 0;

            printf("Condition (e.g., 'age > 18'): ");
            fgets(rules[rule_count].condition, sizeof(rules[rule_count].condition), stdin);
            rules[rule_count].condition[strcspn(rules[rule_count].condition, "\n")] = 0;

            printf("Action (e.g., 'discount = 10.0'): ");
            fgets(rules[rule_count].action, sizeof(rules[rule_count].action), stdin);
            rules[rule_count].action[strcspn(rules[rule_count].action, "\n")] = 0;

            rule_count++;
            printf("✅ Rule added successfully!\n");
            break;
        }
        case 2: { // View Rules
            printf("\nAutomation Rules:\n");
            printf("=================\n");
            for(int i = 0; i < rule_count; i++) {
                printf("%d. %s\n", i+1, rules[i].name);
                printf("   Condition: %s\n", rules[i].condition);
                printf("   Action: %s\n\n", rules[i].action);
            }
            if(rule_count == 0) {
                printf("No rules found.\n");
            }
            break;
        }
        case 3: { // Test Rule
            printf("\nSelect rule to test (1-%d): ", rule_count);
            int rule_choice;
            scanf("%d", &rule_choice);
            getchar();

            if(rule_choice < 1 || rule_choice > rule_count) {
                printf("Invalid rule choice!\n");
                break;
            }

            printf("Select dataset (1-%d): ", dataset_count);
            int dataset_choice;
            scanf("%d", &dataset_choice);
            getchar();

            if(dataset_choice < 1 || dataset_choice > dataset_count) {
                printf("Invalid dataset choice!\n");
                break;
            }

            DataSet *dataset = &datasets[dataset_choice - 1];
            AutomationRule *rule = &rules[rule_choice - 1];

            printf("\nTesting rule '%s' on dataset '%s':\n", rule->name, dataset->name);
            printf("=====================================\n");

            int matches = 0;
            for(int i = 0; i < dataset->record_count; i++) {
                if(evaluate_condition(rule->condition, &dataset->records[i], dataset)) {
                    printf("Record %d matches condition:\n", i+1);
                    for(int j = 0; j < dataset->field_count; j++) {
                        printf("  %s: %s\n", dataset->fields[j].name, dataset->records[i].data[j]);
                    }
                    matches++;
                }
            }

            printf("\nTotal matches: %d\n", matches);
            break;
        }
        case 4:
            return;
        default:
            printf("Invalid choice!\n");
    }

    pause();
}

void manage_automated_reports() {
    clear_screen();
    printf("📋 AUTOMATED REPORTS MANAGEMENT 📋\n");
    printf("===================================\n\n");

    printf("Reports Options:\n");
    printf("1. Create Report\n");
    printf("2. View Reports\n");
    printf("3. Run Report\n");
    printf("4. Back to Main Menu\n\n");
    printf("Enter choice (1-4): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // Create Report
            if(report_count >= MAX_REPORTS) {
                printf("Report limit reached!\n");
                pause();
                return;
            }

            printf("\nCreate Automated Report:\n");
            printf("Report name: ");
            fgets(reports[report_count].name, sizeof(reports[report_count].name), stdin);
            reports[report_count].name[strcspn(reports[report_count].name, "\n")] = 0;

            printf("Report type (summary/detailed/chart/export): ");
            fgets(reports[report_count].type, sizeof(reports[report_count].type), stdin);
            reports[report_count].type[strcspn(reports[report_count].type, "\n")] = 0;

            printf("Data source (dataset name): ");
            fgets(reports[report_count].data_source, sizeof(reports[report_count].data_source), stdin);
            reports[report_count].data_source[strcspn(reports[report_count].data_source, "\n")] = 0;

            printf("Filters (optional, press Enter to skip): ");
            fgets(reports[report_count].filters, sizeof(reports[report_count].filters), stdin);
            reports[report_count].filters[strcspn(reports[report_count].filters, "\n")] = 0;

            printf("Schedule (daily/weekly/monthly/manual): ");
            fgets(reports[report_count].schedule, sizeof(reports[report_count].schedule), stdin);
            reports[report_count].schedule[strcspn(reports[report_count].schedule, "\n")] = 0;

            reports[report_count].last_run = 0;
            report_count++;

            printf("✅ Report created successfully!\n");
            break;
        }
        case 2: { // View Reports
            printf("\nAutomated Reports:\n");
            printf("==================\n");
            for(int i = 0; i < report_count; i++) {
                char last_run_str[20];
                if(reports[i].last_run == 0) {
                    strcpy(last_run_str, "Never");
                } else {
                    format_time(reports[i].last_run, last_run_str, sizeof(last_run_str));
                }

                printf("%d. %s (%s)\n", i+1, reports[i].name, reports[i].type);
                printf("   Data Source: %s\n", reports[i].data_source);
                printf("   Filters: %s\n", strlen(reports[i].filters) > 0 ? reports[i].filters : "None");
                printf("   Schedule: %s\n", reports[i].schedule);
                printf("   Last Run: %s\n\n", last_run_str);
            }
            if(report_count == 0) {
                printf("No reports found.\n");
            }
            break;
        }
        case 3: { // Run Report
            printf("\nSelect report to run (1-%d): ", report_count);
            int report_choice;
            scanf("%d", &report_choice);
            getchar();

            if(report_choice < 1 || report_choice > report_count) {
                printf("Invalid report choice!\n");
                break;
            }

            AutomatedReport *report = &reports[report_choice - 1];

            // Find dataset
            DataSet *dataset = NULL;
            for(int i = 0; i < dataset_count; i++) {
                if(strcmp(datasets[i].name, report->data_source) == 0) {
                    dataset = &datasets[i];
                    break;
                }
            }

            if(dataset == NULL) {
                printf("Data source '%s' not found!\n", report->data_source);
                break;
            }

            printf("\nGenerating report: %s\n", report->name);
            printf("======================\n");

            // Simple report generation
            int matching_records = 0;
            if(strcmp(report->type, "summary") == 0) {
                // Count records matching filters
                for(int i = 0; i < dataset->record_count; i++) {
                    int matches = 1;
                    if(strlen(report->filters) > 0) {
                        matches = evaluate_condition(report->filters, &dataset->records[i], dataset);
                    }
                    if(matches) matching_records++;
                }

                printf("Summary Report for %s\n", dataset->name);
                printf("Total Records: %d\n", dataset->record_count);
                printf("Matching Records: %d\n", matching_records);
                printf("Match Percentage: %.1f%%\n", (double)matching_records / dataset->record_count * 100);
            } else if(strcmp(report->type, "detailed") == 0) {
                printf("Detailed Report for %s\n", dataset->name);
                printf("Matching Records:\n");
                printf("=================\n");

                for(int i = 0; i < dataset->record_count; i++) {
                    int matches = 1;
                    if(strlen(report->filters) > 0) {
                        matches = evaluate_condition(report->filters, &dataset->records[i], dataset);
                    }
                    if(matches) {
                        printf("Record %d:\n", i+1);
                        for(int j = 0; j < dataset->field_count; j++) {
                            printf("  %s: %s\n", dataset->fields[j].name, dataset->records[i].data[j]);
                        }
                        printf("\n");
                        matching_records++;
                    }
                }
            }

            report->last_run = get_current_time();
            printf("✅ Report generated successfully! (%d matching records)\n", matching_records);
            break;
        }
        case 4:
            return;
        default:
            printf("Invalid choice!\n");
    }

    pause();
}

void manage_automation_schedules() {
    clear_screen();
    printf("⏰ AUTOMATION SCHEDULES MANAGEMENT ⏰\n");
    printf("=====================================\n\n");

    printf("Schedules Options:\n");
    printf("1. Create Schedule\n");
    printf("2. View Schedules\n");
    printf("3. Enable/Disable Schedule\n");
    printf("4. Back to Main Menu\n\n");
    printf("Enter choice (1-4): ");

    int choice;
    scanf("%d", &choice);
    getchar();

    switch(choice) {
        case 1: { // Create Schedule
            if(schedule_count >= MAX_SCHEDULES) {
                printf("Schedule limit reached!\n");
                pause();
                return;
            }

            printf("\nCreate Automation Schedule:\n");
            printf("Schedule name: ");
            fgets(schedules[schedule_count].name, sizeof(schedules[schedule_count].name), stdin);
            schedules[schedule_count].name[strcspn(schedules[schedule_count].name, "\n")] = 0;

            printf("Operation (process/generate_reports/import/export/cleanup): ");
            fgets(schedules[schedule_count].operation, sizeof(schedules[schedule_count].operation), stdin);
            schedules[schedule_count].operation[strcspn(schedules[schedule_count].operation, "\n")] = 0;

            printf("Parameters: ");
            fgets(schedules[schedule_count].parameters, sizeof(schedules[schedule_count].parameters), stdin);
            schedules[schedule_count].parameters[strcspn(schedules[schedule_count].parameters, "\n")] = 0;

            printf("Schedule (hourly/daily/weekly/monthly): ");
            fgets(schedules[schedule_count].schedule, sizeof(schedules[schedule_count].schedule), stdin);
            schedules[schedule_count].schedule[strcspn(schedules[schedule_count].schedule, "\n")] = 0;

            schedules[schedule_count].enabled = 1;
            schedules[schedule_count].last_run = 0;

            // Calculate next run time
            time_t now = get_current_time();
            if(strcmp(schedules[schedule_count].schedule, "hourly") == 0) {
                schedules[schedule_count].next_run = now + 3600;
            } else if(strcmp(schedules[schedule_count].schedule, "daily") == 0) {
                schedules[schedule_count].next_run = now + 86400;
            } else if(strcmp(schedules[schedule_count].schedule, "weekly") == 0) {
                schedules[schedule_count].next_run = now + 604800;
            } else if(strcmp(schedules[schedule_count].schedule, "monthly") == 0) {
                schedules[schedule_count].next_run = now + 2592000; // 30 days
            }

            schedule_count++;
            printf("✅ Schedule created successfully!\n");
            break;
        }
        case 2: { // View Schedules
            printf("\nAutomation Schedules:\n");
            printf("=====================\n");
            for(int i = 0; i < schedule_count; i++) {
                char last_run_str[20], next_run_str[20];
                if(schedules[i].last_run == 0) {
                    strcpy(last_run_str, "Never");
                } else {
                    format_time(schedules[i].last_run, last_run_str, sizeof(last_run_str));
                }
                format_time(schedules[i].next_run, next_run_str, sizeof(next_run_str));

                printf("%d. %s (%s)\n", i+1, schedules[i].name,
                       schedules[i].enabled ? "Enabled" : "Disabled");
                printf("   Operation: %s\n", schedules[i].operation);
                printf("   Parameters: %s\n", schedules[i].parameters);
                printf("   Schedule: %s\n", schedules[i].schedule);
                printf("   Last Run: %s\n", last_run_str);
                printf("   Next Run: %s\n\n", next_run_str);
            }
            if(schedule_count == 0) {
                printf("No schedules found.\n");
            }
            break;
        }
        case 3: { // Enable/Disable Schedule
            printf("\nSelect schedule (1-%d): ", schedule_count);
            int schedule_choice;
            scanf("%d", &schedule_choice);
            getchar();

            if(schedule_choice < 1 || schedule_choice > schedule_count) {
                printf("Invalid schedule choice!\n");
                break;
            }

            schedules[schedule_choice - 1].enabled = !schedules[schedule_choice - 1].enabled;
            printf("✅ Schedule %s %s!\n", schedules[schedule_choice - 1].name,
                   schedules[schedule_choice - 1].enabled ? "enabled" : "disabled");
            break;
        }
        case 4:
            return;
        default:
            printf("Invalid choice!\n");
    }

    pause();
}

void run_automation() {
    clear_screen();
    printf("▶️  RUN AUTOMATION ▶️\n");
    printf("====================\n\n");

    time_t now = get_current_time();
    int executed = 0;

    printf("Checking automation schedules...\n\n");

    for(int i = 0; i < schedule_count; i++) {
        if(schedules[i].enabled && now >= schedules[i].next_run) {
            printf("Executing: %s\n", schedules[i].name);

            if(strcmp(schedules[i].operation, "process") == 0) {
                batch_process_data();
            } else if(strcmp(schedules[i].operation, "generate_reports") == 0) {
                generate_reports();
            } else if(strcmp(schedules[i].operation, "import") == 0) {
                import_data();
            } else if(strcmp(schedules[i].operation, "export") == 0) {
                export_data();
            }

            schedules[i].last_run = now;

            // Calculate next run time
            if(strcmp(schedules[i].schedule, "hourly") == 0) {
                schedules[i].next_run = now + 3600;
            } else if(strcmp(schedules[i].schedule, "daily") == 0) {
                schedules[i].next_run = now + 86400;
            } else if(strcmp(schedules[i].schedule, "weekly") == 0) {
                schedules[i].next_run = now + 604800;
            } else if(strcmp(schedules[i].schedule, "monthly") == 0) {
                schedules[i].next_run = now + 2592000;
            }

            executed++;
            printf("✅ Completed: %s\n\n", schedules[i].name);
        }
    }

    if(executed == 0) {
        printf("No automation tasks due to run at this time.\n");
    } else {
        printf("✅ Automation run completed! (%d tasks executed)\n", executed);
    }

    pause();
}

void generate_reports() {
    printf("Generating automated reports...\n");

    for(int i = 0; i < report_count; i++) {
        AutomatedReport *report = &reports[i];
        time_t now = get_current_time();

        // Check if report should run based on schedule
        int should_run = 0;
        if(strcmp(report->schedule, "manual") != 0) {
            if(report->last_run == 0) {
                should_run = 1; // Never run before
            } else {
                double time_diff = difftime(now, report->last_run);
                if((strcmp(report->schedule, "daily") == 0 && time_diff >= 86400) ||
                   (strcmp(report->schedule, "weekly") == 0 && time_diff >= 604800) ||
                   (strcmp(report->schedule, "monthly") == 0 && time_diff >= 2592000)) {
                    should_run = 1;
                }
            }
        }

        if(should_run) {
            // Find dataset and generate report (simplified)
            DataSet *dataset = NULL;
            for(int j = 0; j < dataset_count; j++) {
                if(strcmp(datasets[j].name, report->data_source) == 0) {
                    dataset = &datasets[j];
                    break;
                }
            }

            if(dataset != NULL) {
                int matching_records = 0;
                for(int k = 0; k < dataset->record_count; k++) {
                    int matches = 1;
                    if(strlen(report->filters) > 0) {
                        matches = evaluate_condition(report->filters, &dataset->records[k], dataset);
                    }
                    if(matches) matching_records++;
                }

                printf("Generated report: %s (%d records)\n", report->name, matching_records);
                report->last_run = now;
            }
        }
    }
}

void import_data() {
    printf("Data import functionality would be implemented here.\n");
    printf("This would handle CSV, JSON, XML, or database imports.\n");
}

void export_data() {
    printf("Data export functionality would be implemented here.\n");
    printf("This would export data to CSV, JSON, XML, or databases.\n");
}

void batch_process_data() {
    printf("Applying automation rules to datasets...\n");

    int total_processed = 0;

    for(int i = 0; i < dataset_count; i++) {
        DataSet *dataset = &datasets[i];
        int dataset_processed = 0;

        for(int j = 0; j < dataset->record_count; j++) {
            DataRecord *record = &dataset->records[j];

            for(int k = 0; k < rule_count; k++) {
                AutomationRule *rule = &rules[k];

                if(evaluate_condition(rule->condition, record, dataset)) {
                    apply_action(rule->action, record, dataset);
                    dataset_processed++;
                    break; // Apply only first matching rule
                }
            }
        }

        if(dataset_processed > 0) {
            printf("Processed %d records in dataset '%s'\n", dataset_processed, dataset->name);
            total_processed += dataset_processed;
        }
    }

    printf("✅ Batch processing completed! (%d records processed)\n", total_processed);
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
                manage_datasets();
                break;
            case 2:
                manage_automation_rules();
                break;
            case 3:
                manage_automated_reports();
                break;
            case 4:
                manage_automation_schedules();
                break;
            case 5:
                run_automation();
                break;
            case 6:
                generate_reports();
                break;
            case 7:
                import_data();
                break;
            case 8:
                export_data();
                break;
            case 9:
                batch_process_data();
                break;
            case 0:
                printf("\nThank you for using the Automated Data Processor! 🤖\n");
                break;
            default:
                printf("Invalid choice! Please enter 0-9.\n");
                pause();
        }
    } while(choice != 0);

    return 0;
}