# Level 2: Data Processing Application

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


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
    ```

2. **Create a sample data file** (or use the provided one):
    ```bash
    # Create sample_data.txt
    Name,Age,City,Salary
    John,25,New York,50000
    Jane,30,London,60000
    Bob,35,Paris,55000
    Alice,28,Berlin,52000
    ```

3. **Run the program**:
    ```bash
    python3 main.py
    ```

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
```

- **`data`**: Each inner list represents one row of data
- **`headers`**: Column names corresponding to data columns
- **Relationship**: `len(headers)` should equal `len(row)` for each row

### File I/O Operations

```python
def load_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
```

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
```

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
```

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
```

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
```

- **Lambda Function**: Anonymous function for sort key
- **Safety Check**: Prevents index errors with conditional
- **String Sorting**: Default string comparison for mixed data

**Statistics Calculation:**
```python
total = sum(values)
average = total / len(values)
minimum = min(values)
maximum = max(values)
```

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
