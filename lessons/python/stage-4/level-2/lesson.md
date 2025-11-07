# Level 2: Data Processing Application

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 4: Full Problem Solving

### Today's Mission

Building on the temperature converter, now we'll create a more complex application that processes real data. This data processor can load, filter, sort, and analyze tabular data - skills essential for real-world programming tasks.

---

### Learning Goals

- Work with file input/output operations
- Implement data structures for storing tabular data
- Create algorithms for filtering and sorting data
- Perform statistical calculations on datasets
- Handle data validation and error conditions
- Design a multi-function menu-driven application

---

### Your Task

**Study the provided `main.py` and understand how it processes data. Then create your own data processing features or enhance the existing ones.**

The data processor should handle:
1. Loading data from text files (CSV-like format)
2. Displaying data in organized tables
3. Filtering records based on criteria
4. Sorting data by different columns
5. Calculating statistics for numeric columns
6. Exporting processed data

---

### How to Run

1. **Navigate to this level's directory**:
    ```bash
    cd python/stage-4-full-problem-solving/level-2-data-processing-application
    ```bash

2. **Create a sample data file** (or use the provided one):
    ```bash
    # Create sample_data.txt
    Name,Age,City,Salary
    John,25,New York,50000
    Jane,30,London,60000
    Bob,35,Paris,55000
    Alice,28,Berlin,52000
    ```python

3. **Run the program**:
    ```bash
    python3 main.py
    ```python

4. **Test all menu options** with your data

---

### Success Checklist

- [ ] Program loads data files correctly
- [ ] Data displays in readable tabular format
- [ ] Filtering works for different criteria
- [ ] Sorting works for different columns
- [ ] Statistics calculate correctly for numeric data
- [ ] Export functionality saves data properly
- [ ] Error handling prevents crashes

---

### Data Processing Concepts

This application introduces several important data processing concepts:

- **Data Persistence**: Saving and loading data from files
- **Data Structures**: Using lists of lists for tabular data
- **Data Validation**: Ensuring data integrity and handling malformed input
- **Data Transformation**: Filtering, sorting, and statistical operations
- **User-Driven Operations**: Menu systems for user control

---

### Enhancement Ideas

Try these advanced features:

1. **Multiple File Support** - Load and merge multiple data files
2. **Advanced Filtering** - Support for numeric ranges and multiple conditions
3. **Data Visualization** - Simple text-based charts and graphs
4. **Data Export Formats** - Support for different output formats
5. **Data Validation Rules** - Custom validation for different data types
6. **Search Functionality** - Find records containing specific text

---

## Code Analysis

### Key Data Structures

```python
# Global data storage
data = []      # List of lists containing the actual data rows
headers = []   # List of column headers
```python

- **`data`**: Each inner list represents one row of data
- **`headers`**: Column names corresponding to data columns
- **Relationship**: `len(headers)` should equal `len(row)` for each row

### File I/O Operations

```python
def load_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
```python

- **Context Manager**: `with` statement ensures file is properly closed
- **Read All Lines**: `readlines()` gives us a list of all lines
- **Error Handling**: Try/except blocks for file operation failures

### Data Processing Functions

```python
def filter_data():
    # Find records matching criteria
    filtered_data = []
    for row in data:
        if col_choice < len(row) and str(row[col_choice]) == filter_value:
            filtered_data.append(row)
```python

- **List Comprehension Alternative**: Could use `[row for row in data if condition]`
- **Data Integrity**: Checks ensure we don't access invalid indices
- **Type Conversion**: `str()` ensures string comparison works

### Statistical Calculations

```python
def calculate_stats():
    values = []
    for row in data:
        try:
            values.append(float(row[col_idx]))
        except ValueError:
            continue
```python

- **Type Safety**: Try/except handles non-numeric data gracefully
- **Robust Statistics**: Only processes valid numeric values
- **Multiple Metrics**: Calculates sum, average, min, max in one pass

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (Study the implementation!)

### Data Format Specification

**CSV-like Format Requirements:**
```python
Header1,Header2,Header3,...
Value1,Value2,Value3,...
Value1,Value2,Value3,...
```python

- **Header Row**: First line contains column names
- **Data Rows**: Subsequent lines contain data values
- **Delimiter**: Comma separation (`,`)
- **No Quotes**: Simple format without quoted strings
- **No Escaping**: No special character handling

### Error Handling Strategy

| Error Type | Detection | Response |
|------------|-----------|----------|
| **File Not Found** | `os.path.exists()` | Clear error message |
| **Empty File** | `not lines` | Informative message |
| **Malformed Row** | Length mismatch | Skip with warning |
| **Invalid Input** | Try/except | Retry prompt |
| **No Numeric Data** | ValueError on float() | Skip invalid values |

### Algorithm Analysis

**Sorting Implementation:**
```python
data.sort(key=lambda row: row[col_choice] if col_choice < len(row) else "", reverse=reverse)
```python

- **Lambda Function**: Anonymous function for sort key
- **Safety Check**: Prevents index errors with conditional
- **String Sorting**: Default string comparison for mixed data

**Statistics Calculation:**
```python
total = sum(values)
average = total / len(values)
minimum = min(values)
maximum = max(values)
```python

- **Built-in Functions**: Python's `sum()`, `min()`, `max()` are efficient
- **Single Pass**: All statistics calculated in one iteration
- **Type Consistency**: All values converted to float for calculation

### Performance Considerations

| Operation | Complexity | Optimization |
|-----------|------------|--------------|
| **Loading** | O(n) | Read all lines at once |
| **Filtering** | O(n) | Single pass through data |
| **Sorting** | O(n log n) | Python's Timsort algorithm |
| **Statistics** | O(n) | Single pass with accumulation |
| **Display** | O(n*m) | n rows, m columns |

### Testing Strategy

**Test Data Scenarios:**
- Normal data with all columns filled
- Missing values in some rows
- Non-numeric data in numeric columns
- Empty rows or extra whitespace
- Very large datasets (performance testing)

**Edge Cases:**
- File with only headers, no data
- Single column data
- Data with special characters
- Very long column values
- Empty filter results

---

 **Excellent! You now understand data processing fundamentals!** 

*Next up: Mathematical Application - building calculators and solvers!*


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic


<div style="page-break-after: always;"></div>

## Answer Key

### Complete Solution

```py
#!/usr/bin/env python3
"""
Simple Data Processor
A Python program for loading, processing, and analyzing tabular data.
"""

import os

# Global data storage
data = []
headers = []

def load_data(filename):
    """Load data from a CSV-like file."""
    global data, headers

    if not os.path.exists(filename):
        print(f"❌ File '{filename}' not found!")
        return False

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        if not lines:
            print("❌ File is empty!")
            return False

        # Parse headers
        headers = [col.strip() for col in lines[0].split(',')]

        # Parse data rows
        data = []
        for line in lines[1:]:
            if line.strip():  # Skip empty lines
                row = [col.strip() for col in line.split(',')]
                if len(row) == len(headers):
                    data.append(row)
                else:
                    print(f"⚠️  Skipping malformed row: {line.strip()}")

        print(f"✅ Data loaded successfully! ({len(data)} records)")
        return True

    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return False

def display_data():
    """Display data in tabular format."""
    if not data:
        print("❌ No data loaded. Please load a data file first.")
        return

    # Calculate column widths
    col_widths = []
    for i, header in enumerate(headers):
        max_width = len(header)
        for row in data:
            if i < len(row):
                max_width = max(max_width, len(str(row[i])))
        col_widths.append(max_width)

    # Print headers
    header_line = ""
    for i, header in enumerate(headers):
        header_line += f"{header:<{col_widths[i]}} "
    print(header_line)
    print("-" * len(header_line))

    # Print data rows
    for row in data:
        row_line = ""
        for i, cell in enumerate(row):
            if i < len(col_widths):
                row_line += f"{cell:<{col_widths[i]}} "
        print(row_line)

def filter_data():
    """Filter data based on user criteria."""
    if not data:
        print("❌ No data loaded. Please load a data file first.")
        return

    print("Available columns:")
    for i, header in enumerate(headers):
        print(f"{i+1}. {header}")

    try:
        col_choice = int(input("Choose column to filter by (number): ")) - 1
        if col_choice < 0 or col_choice >= len(headers):
            print("❌ Invalid column choice!")
            return

        filter_value = input(f"Enter value to filter for in '{headers[col_choice]}': ")

        filtered_data = []
        for row in data:
            if col_choice < len(row) and str(row[col_choice]) == filter_value:
                filtered_data.append(row)

        print(f"\nFiltered Results ({len(filtered_data)} matches):")
        if filtered_data:
            # Temporarily replace data for display
            original_data = data[:]
            data[:] = filtered_data
            display_data()
            data[:] = original_data
        else:
            print("No matching records found.")

    except ValueError:
        print("❌ Invalid input. Please enter a number.")

def sort_data():
    """Sort data by a specified column."""
    if not data:
        print("❌ No data loaded. Please load a data file first.")
        return

    print("Available columns:")
    for i, header in enumerate(headers):
        print(f"{i+1}. {header}")

    try:
        col_choice = int(input("Choose column to sort by (number): ")) - 1
        if col_choice < 0 or col_choice >= len(headers):
            print("❌ Invalid column choice!")
            return

        reverse = input("Sort ascending? (y/n): ").lower() == 'n'

        # Sort data
        data.sort(key=lambda row: row[col_choice] if col_choice < len(row) else "", reverse=reverse)

        print(f"✅ Data sorted by '{headers[col_choice]}' ({'descending' if reverse else 'ascending'})")
        display_data()

    except ValueError:
        print("❌ Invalid input. Please enter a number.")

def calculate_stats():
    """Calculate statistics for numeric columns."""
    if not data:
        print("❌ No data loaded. Please load a data file first.")
        return

    # Find numeric columns
    numeric_cols = []
    for i, header in enumerate(headers):
        # Check if column contains numeric data
        is_numeric = True
        for row in data:
            if i < len(row):
                try:
                    float(row[i])
                except ValueError:
                    is_numeric = False
                    break
        if is_numeric:
            numeric_cols.append(i)

    if not numeric_cols:
        print("❌ No numeric columns found in the data.")
        return

    print("Numeric columns available:")
    for i, col_idx in enumerate(numeric_cols):
        print(f"{i+1}. {headers[col_idx]}")

    try:
        col_choice = int(input("Choose column for statistics (number): ")) - 1
        if col_choice < 0 or col_choice >= len(numeric_cols):
            print("❌ Invalid column choice!")
            return

        col_idx = numeric_cols[col_choice]
        values = []

        for row in data:
            if col_idx < len(row):
                try:
                    values.append(float(row[col_idx]))
                except ValueError:
                    continue

        if not values:
            print("❌ No valid numeric values found in column.")
            return

        total = sum(values)
        average = total / len(values)
        minimum = min(values)
        maximum = max(values)

        print(f"\nStatistics for '{headers[col_idx]}':")
        print(f"Count: {len(values)}")
        print(f"Sum: {total:.2f}")
        print(f"Average: {average:.2f}")
        print(f"Minimum: {minimum:.2f}")
        print(f"Maximum: {maximum:.2f}")

    except ValueError:
        print("❌ Invalid input. Please enter a number.")

def export_data():
    """Export current data to a file."""
    if not data:
        print("❌ No data to export. Please load data first.")
        return

    filename = input("Enter export filename: ")
    if not filename.endswith('.txt'):
        filename += '.txt'

    try:
        with open(filename, 'w') as file:
            # Write headers
            file.write(','.join(headers) + '\n')

            # Write data
            for row in data:
                file.write(','.join(row) + '\n')

        print(f"✅ Data exported to '{filename}' successfully!")

    except Exception as e:
        print(f"❌ Error exporting data: {e}")

def main():
    """Main program function."""
    print("📊 Simple Data Processor 📊")
    print("=" * 30)

    while True:
        print("\nData Operations Menu:")
        print("1. Load Data File")
        print("2. View Data")
        print("3. Filter Data")
        print("4. Sort Data")
        print("5. Calculate Statistics")
        print("6. Export Data")
        print("7. Exit")

        try:
            choice = int(input("Enter choice (1-7): "))

            if choice == 1:
                filename = input("Enter filename: ")
                load_data(filename)
            elif choice == 2:
                display_data()
            elif choice == 3:
                filter_data()
            elif choice == 4:
                sort_data()
            elif choice == 5:
                calculate_stats()
            elif choice == 6:
                export_data()
            elif choice == 7:
                print("\nThank you for using the Simple Data Processor! 📊")
                break
            else:
                print("❌ Invalid choice. Please enter 1-7.")

        except ValueError:
            print("❌ Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard python conventions with proper imports and main function
2. **Variables**: Data types are correctly declared and initialized
3. **Logic**: The program implements the required functionality
4. **Output**: Results are displayed clearly to the user
5. **Best Practices**: Code is readable and follows naming conventions

### Testing Your Solution

Try these test cases to verify your code works correctly:

1. **Basic Test**: Run the program with standard inputs
2. **Edge Cases**: Test with boundary values (0, -1, very large numbers)
3. **Error Handling**: Verify the program handles invalid inputs gracefully

### Tips for Understanding

- Review each section carefully
- Try modifying values to see how output changes
- Add your own printf/print statements to trace execution
- Experiment with different inputs
