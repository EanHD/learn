# Automated Data Processor

A comprehensive C application for automated data processing, featuring rule-based operations, scheduled tasks, batch processing, and automated report generation.

## Features

- **Dataset Management**: Create and manage structured datasets with custom field definitions
- **Automation Rules**: Define conditional rules for automatic data processing and transformation
- **Automated Reports**: Schedule and generate various types of reports from data sources
- **Task Scheduling**: Set up automated tasks to run on hourly, daily, weekly, or monthly schedules
- **Batch Processing**: Apply rules and transformations to large datasets automatically
- **Data Import/Export**: Framework for importing and exporting data in various formats
- **Rule Engine**: Conditional processing with support for numeric and string comparisons

## Quick Start

1. **Compile the program**:
   ```bash
   gcc main.c -o data_processor
   ```

2. **Run the application**:
   ```bash
   ./data_processor
   ```

3. **Navigate using the main menu** to set up datasets, rules, and automation

## Menu Structure

### Main Menu
- **1.  Manage Datasets** - Create datasets, add records, view data
- **2.   Manage Automation Rules** - Define conditional processing rules
- **3.  Manage Automated Reports** - Set up scheduled report generation
- **4. ⏰ Manage Automation Schedules** - Configure timed automation tasks
- **5. ▶  Run Automation** - Execute scheduled automation tasks
- **6.  Generate Reports** - Manually generate reports
- **7.  Import Data** - Import data from external sources
- **8.  Export Data** - Export data to external formats
- **9.  Batch Process Data** - Apply rules to datasets
- **0.  Exit** - Exit the application

## Dataset Management

### Creating Datasets
- **Dataset Names**: Unique identifiers for data collections
- **Field Definitions**: Custom fields with types (string, int, float, date)
- **Required Fields**: Mark fields as mandatory or optional
- **Record Storage**: Automatic record management and validation

### Data Types Supported
- **String**: Text data of variable length
- **Integer**: Whole numbers for IDs and counts
- **Float**: Decimal numbers for measurements and calculations
- **Date**: Date values (YYYY-MM-DD format)

### Record Management
- **Add Records**: Input data following field definitions
- **View Records**: Tabular display of all dataset records
- **Data Validation**: Type checking and required field validation
- **Record Limits**: Configurable maximum records per dataset

## Automation Rules

### Rule Components
- **Rule Names**: Descriptive identifiers for automation rules
- **Conditions**: Logical expressions for rule triggering
- **Actions**: Data transformations to apply when conditions are met

### Condition Syntax
- **Numeric Comparisons**: `age > 18`, `score >= 90`, `price < 100.50`
- **String Comparisons**: `status == 'active'`, `category != 'inactive'`
- **Field References**: Use dataset field names in conditions

### Action Syntax
- **Field Assignment**: `discount = 10.0`, `status = 'approved'`
- **Value Types**: Support for strings (in quotes) and numbers
- **Field Updates**: Modify existing record fields based on conditions

### Rule Processing
- **Sequential Evaluation**: Rules processed in order until match found
- **First Match Wins**: Only first matching rule applied per record
- **Batch Application**: Rules applied to entire datasets automatically

## Automated Reports

### Report Types
- **Summary Reports**: Statistical overviews and counts
- **Detailed Reports**: Complete record listings with filters
- **Chart Reports**: Data visualization (framework provided)
- **Export Reports**: Data extraction for external use

### Report Configuration
- **Data Sources**: Specify which datasets to report on
- **Filters**: Apply conditions to limit reported data
- **Scheduling**: Set automatic generation intervals
- **Output Formats**: Define report structure and content

### Scheduling Options
- **Manual**: Reports generated on-demand only
- **Daily**: Automatic generation every 24 hours
- **Weekly**: Automatic generation every 7 days
- **Monthly**: Automatic generation every 30 days

## Automation Schedules

### Schedule Types
- **Process**: Apply automation rules to datasets
- **Generate Reports**: Create scheduled reports
- **Import**: Automated data importing
- **Export**: Automated data exporting
- **Cleanup**: Data maintenance and optimization

### Scheduling Intervals
- **Hourly**: Tasks run every hour
- **Daily**: Tasks run once per day
- **Weekly**: Tasks run once per week
- **Monthly**: Tasks run once per month

### Schedule Management
- **Enable/Disable**: Control which schedules are active
- **Next Run Calculation**: Automatic scheduling based on intervals
- **Execution Tracking**: Monitor schedule execution history
- **Manual Override**: Force execution outside normal schedule

## Batch Processing

### Processing Operations
- **Rule Application**: Apply all active automation rules
- **Data Transformation**: Modify records based on conditions
- **Bulk Updates**: Process large numbers of records efficiently
- **Progress Tracking**: Monitor processing status and completion

### Processing Logic
- **Dataset Iteration**: Process each dataset in sequence
- **Record Evaluation**: Check each record against all rules
- **Action Execution**: Apply matching rule actions
- **Result Reporting**: Summary of processing outcomes

## Data Import/Export

### Import Capabilities
- **CSV Files**: Comma-separated value imports
- **JSON Format**: JavaScript Object Notation support
- **XML Files**: Extensible Markup Language imports
- **Database Connections**: Direct database imports

### Export Capabilities
- **CSV Export**: Data export to spreadsheet-compatible format
- **JSON Export**: Structured data for web applications
- **XML Export**: Hierarchical data representation
- **Database Export**: Direct database insertions

## Technical Details

### Data Structures
- **DataSet Structure**: Contains fields, records, and metadata
- **FieldDefinition Structure**: Field properties and constraints
- **DataRecord Structure**: Individual record data storage
- **AutomationRule Structure**: Condition-action rule definitions

### Rule Engine
- **Condition Parser**: Simple expression evaluation
- **Type Checking**: Data type validation in comparisons
- **Action Processor**: Field modification and updates
- **Error Handling**: Graceful failure handling

### Scheduling System
- **Time Management**: Unix timestamp-based scheduling
- **Interval Calculation**: Automatic next-run time computation
- **Execution Tracking**: Last run and next run timestamps
- **Status Monitoring**: Schedule enable/disable states

## Usage Examples

### Creating a Dataset
```
 DATASET MANAGEMENT
=====================

Dataset Options:
1. Create Dataset
2. View Datasets
3. Add Records
4. View Records
5. Back to Main Menu
Enter choice (1-5): 1

Create New Dataset:
Dataset name: Customer_Data
Number of fields: 4
Field 1 name: customer_id
Field 1 type (string/int/float/date): int
Field 1 required (1=yes, 0=no): 1
Field 2 name: name
Field 2 type (string/int/float/date): string
Field 2 required (1=yes, 0=no): 1
Field 3 name: age
Field 3 type (string/int/float/date): int
Field 3 required (1=yes, 0=no): 1
Field 4 name: discount
Field 4 type (string/int/float/date): float
Field 4 required (1=yes, 0=no): 0

 Dataset created successfully!
```

### Creating Automation Rules
```
  AUTOMATION RULES MANAGEMENT
================================

Rules Options:
1. Add Rule
2. View Rules
3. Test Rule
4. Back to Main Menu
Enter choice (1-4): 1

Add Automation Rule:
Rule name: Senior Discount
Condition (e.g., 'age > 18'): age >= 65
Action (e.g., 'discount = 10.0'): discount = 15.0

 Rule added successfully!
```

### Setting Up Automated Reports
```
 AUTOMATED REPORTS MANAGEMENT
=================================

Reports Options:
1. Create Report
2. View Reports
3. Run Report
4. Back to Main Menu
Enter choice (1-4): 1

Create Automated Report:
Report name: Customer Summary
Report type (summary/detailed/chart/export): summary
Data source (dataset name): Customer_Data
Filters (optional, press Enter to skip): status == 'active'
Schedule (daily/weekly/monthly/manual): weekly

 Report created successfully!
```

### Batch Processing Results
```
 Batch Process Data
=====================

Applying automation rules to datasets...
Processed 2 records in dataset 'Customer_Data'
 Batch processing completed! (2 records processed)
```

### Automation Schedule Management
```
⏰ AUTOMATION SCHEDULES MANAGEMENT
====================================

Schedules Options:
1. Create Schedule
2. View Schedules
3. Enable/Disable Schedule
4. Back to Main Menu
Enter choice (1-4): 1

Create Automation Schedule:
Schedule name: Daily Data Processing
Operation (process/generate_reports/import/export/cleanup): process
Parameters: apply_rules
Schedule (hourly/daily/weekly/monthly): daily

 Schedule created successfully!
```

## Rule Examples

### Customer Discount Rules
```
Rule: Senior Discount
Condition: age >= 65
Action: discount = 15.0

Rule: Loyalty Discount
Condition: age >= 30
Action: discount = 10.0

Rule: VIP Status
Condition: discount >= 10.0
Action: status = 'vip'
```

### Data Validation Rules
```
Rule: Age Validation
Condition: age < 0
Action: age = 0

Rule: Status Normalization
Condition: status == ''
Action: status = 'active'
```

## Report Examples

### Summary Report Output
```
Summary Report for Customer_Data
=================================
Total Records: 150
Matching Records: 120
Match Percentage: 80.0%
Average Age: 35.2
Active Customers: 120
Inactive Customers: 30
```

### Detailed Report Output
```
Detailed Report for Customer_Data
=================================
Matching Records:
=================
Record 1:
  customer_id: 1
  name: John Doe
  age: 25
  discount: 0.0

Record 2:
  customer_id: 2
  name: Jane Smith
  age: 35
  discount: 10.0
```

## Automation Scenarios

### E-commerce Processing
- **Order Validation**: Check order completeness and validity
- **Discount Application**: Apply promotional discounts automatically
- **Shipping Calculation**: Determine shipping costs based on location
- **Tax Computation**: Calculate taxes based on location and product type

### Customer Management
- **Segment Classification**: Categorize customers based on purchase history
- **Loyalty Program**: Award points and status based on activity
- **Communication Triggers**: Flag customers for follow-up communications
- **Risk Assessment**: Identify high-risk accounts for review

### Inventory Management
- **Stock Level Monitoring**: Alert when inventory falls below thresholds
- **Reorder Automation**: Automatically generate purchase orders
- **Price Optimization**: Adjust pricing based on demand and competition
- **Supplier Evaluation**: Rate suppliers based on delivery performance

## Performance Considerations

### Processing Limits
- **Dataset Size**: Maximum 1000 records per dataset
- **Field Count**: Maximum 20 fields per dataset
- **Rule Count**: Maximum 50 automation rules
- **Schedule Count**: Maximum 10 automation schedules

### Optimization Features
- **Batch Processing**: Efficient bulk operations
- **Indexed Lookups**: Fast field and record access
- **Memory Management**: Fixed-size arrays for predictable memory usage
- **Sequential Processing**: Ordered rule application

## Extensibility

### Adding New Data Types
- **Custom Types**: Extend type system for specialized data
- **Validation Rules**: Add custom validation logic
- **Conversion Functions**: Support data type conversions

### Enhanced Rule Engine
- **Complex Conditions**: Support AND/OR logic and parentheses
- **Mathematical Operations**: Allow calculations in conditions
- **String Functions**: Add string manipulation capabilities

### Integration APIs
- **Database Connectors**: Direct database integration
- **Web Services**: REST API integration for external data
- **File System**: Advanced file format support

## Learning Outcomes

This application demonstrates:
- **Automated Processing**: Rule-based data manipulation and transformation
- **Scheduling Systems**: Time-based task automation and execution
- **Batch Operations**: Efficient processing of large datasets
- **Report Generation**: Automated report creation and scheduling
- **Data Pipeline Management**: End-to-end data processing workflows
- **Rule Engine Implementation**: Conditional logic and action processing
- **Modular Architecture**: Organized code with clear component separation

## Compilation

### Requirements
- GCC compiler
- Standard C libraries (stdio.h, stdlib.h, string.h, ctype.h, time.h)

### Build Command
```bash
gcc main.c -o data_processor -Wall -Wextra
```

### Debug Build
```bash
gcc main.c -o data_processor_debug -Wall -Wextra -g -O0
```

### Clean Build
```bash
rm -f data_processor data_processor_debug
gcc main.c -o data_processor -Wall -Wextra
```

---

*Built as Level 6 of Stage 4: Full Problem Solving in the C/C++ Programming Curriculum*