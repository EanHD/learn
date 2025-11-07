# Sales Data Analyzer

A comprehensive C application for processing, analyzing, and reporting sales data from CSV files with advanced statistical capabilities.

## Features

- **CSV Data Import**: Parse sales data from CSV files with validation
- **Statistical Analysis**: Calculate totals, averages, and performance metrics
- **Product Analytics**: Identify best-selling products and revenue analysis
- **Date-based Filtering**: Search and analyze sales by specific dates
- **Report Generation**: Create detailed sales reports and summaries
- **Data Export**: Save processed data to CSV files
- **Sample Data Generation**: Automatic sample data creation for testing

## Quick Start

1. **Compile the program**:
   ```bash
   gcc main.c -o sales_analyzer
   ```

2. **Run the application**:
   ```bash
   ./sales_analyzer
   ```

3. **Load or generate data** and use the analysis features

4. **Export results** to CSV files for further processing

## Menu Options

### Main Menu
- **1. Load CSV Data** - Import sales data from CSV file
- **2. Display All Sales** - View all sales records in tabular format
- **3. Calculate Statistics** - Generate comprehensive sales statistics
- **4. Search by Product** - Find sales for specific products
- **5. Search by Date** - Filter sales by date
- **6. Generate Report** - Create product-based revenue reports
- **7. Export Data** - Save data to CSV file
- **8. Exit** - Exit the program

## CSV File Format

The application expects CSV files with the following format:

```csv
Date,Product,Quantity,Price
2024-01-15,Laptop,2,999.99
2024-01-15,Mouse,5,25.50
2024-01-16,Keyboard,3,75.00
```

### Field Descriptions
- **Date**: Sale date in YYYY-MM-DD format
- **Product**: Product name (string)
- **Quantity**: Number of items sold (integer)
- **Price**: Unit price in dollars (float)

## Usage Examples

### Loading CSV Data
```
 LOAD CSV DATA
================
Enter CSV filename (or 'sales.csv' for default): sales.csv
 Loaded 150 sales records from 'sales.csv'
```

### Viewing Statistics
```
 SALES STATISTICS
===================
Total Revenue: $45678.50
Average Sale: $304.52
Total Transactions: 150
Best Selling Product: Laptop ($25678.50)
Highest Revenue Day: 2024-01-15 ($12345.67)
```

### Product Search
```
 SEARCH BY PRODUCT
====================
Enter product name to search: Laptop

Search Results for 'Laptop':
Date         Product         Qty      Price      Total
----------------------------------------------------
2024-01-15   Laptop          2        $999.99    $1999.98
2024-01-16   Laptop          1        $999.99    $999.99

Found 2 sales, Total Revenue: $2999.97
```

### Date Search
```
 SEARCH BY DATE
=================
Enter date (YYYY-MM-DD): 2024-01-15

Sales for 2024-01-15:
Product         Qty      Price      Total
----------------------------------------
Laptop          2        $999.99    $1999.98
Mouse           5        $25.50     $127.50
Monitor         1        $299.99    $299.99

Found 3 sales, Total Revenue: $2427.47
```

## Sample Data

If no CSV file is found, the program automatically creates sample data:

- **4 sample sales records** across 2 days
- **3 different products**: Laptop, Mouse, Keyboard
- **Realistic pricing** and quantities
- **Demonstrates all features** without requiring external files

## Technical Details

### Data Structures
- **Sale Structure**: Contains date, product, quantity, price, and calculated total
- **Fixed-size Arrays**: Simple memory management for up to 1000 sales records
- **String Processing**: Custom whitespace trimming and CSV parsing

### CSV Parsing
- **Header Detection**: Automatically skips CSV header row
- **Field Validation**: Ensures all required fields are present
- **Data Type Conversion**: Converts strings to integers and floats
- **Error Handling**: Skips malformed lines with error reporting

### Statistical Calculations
- **Revenue Totals**: Sum of all sale totals
- **Average Calculations**: Mean sale amount
- **Product Grouping**: Aggregates sales by product name
- **Date Analysis**: Groups sales by date for trend analysis

## File Operations

### Input Files
- **CSV Format**: Comma-separated values with header row
- **Automatic Fallback**: Creates sample data if file not found
- **Error Recovery**: Graceful handling of missing or corrupted files

### Output Files
- **CSV Export**: Recreates data in standard CSV format
- **All Records**: Exports complete dataset with calculated totals
- **Custom Filenames**: User-specified output filenames

## Analysis Features

### Statistical Metrics
- **Total Revenue**: Sum of all sales
- **Average Sale**: Mean transaction value
- **Transaction Count**: Total number of sales records
- **Best Performers**: Top products and dates by revenue

### Search Capabilities
- **Product Search**: Partial name matching
- **Date Filtering**: Exact date matching
- **Revenue Aggregation**: Automatic totals for search results

### Reporting
- **Product Reports**: Revenue breakdown by product
- **Summary Statistics**: Key performance indicators
- **Formatted Output**: Human-readable tabular displays

## Limitations

- Maximum 1000 sales records
- Fixed-size data structures
- Simple CSV parsing (no quoted fields)
- In-memory processing only

## Future Enhancements

### Data Processing
- **Large Dataset Support**: Dynamic memory allocation
- **Advanced CSV Parsing**: Handle quoted fields and complex data
- **Multiple File Import**: Merge data from several CSV files
- **Data Validation**: More sophisticated error checking

### Analysis Features
- **Time Series Analysis**: Trend analysis over time periods
- **Customer Segmentation**: Group by customer if available
- **Predictive Analytics**: Sales forecasting capabilities
- **Interactive Charts**: Graphical data visualization

### Export Options
- **Multiple Formats**: JSON, XML, and database export
- **Filtered Export**: Export only search results
- **Report Templates**: Customizable report formats
- **Automated Reporting**: Scheduled report generation

## Learning Outcomes

This application demonstrates:
- **File I/O Operations**: Reading and writing CSV files
- **String Processing**: Parsing and manipulating text data
- **Data Structures**: Organizing related data efficiently
- **Statistical Analysis**: Basic data analysis algorithms
- **User Interface Design**: Creating functional console applications
- **Error Handling**: Robust input validation and error recovery
- **Memory Management**: Working with arrays and fixed-size buffers

## Compilation

### Requirements
- GCC compiler
- Standard C libraries (stdio.h, stdlib.h, string.h, ctype.h)

### Build Command
```bash
gcc main.c -o sales_analyzer -Wall -Wextra
```

### Clean Build
```bash
rm -f sales_analyzer sales_export.csv
gcc main.c -o sales_analyzer -Wall -Wextra
```

---

*Built as Level 2 of Stage 4: Full Problem Solving in the C/C++ Programming Curriculum*