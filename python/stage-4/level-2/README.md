# Simple Data Processor

A Python program that reads, processes, and analyzes simple tabular data.

## How to Run

1. **Run the program**:
    ```bash
    python3 main.py
    ```

2. **Follow the menu options** to load data, perform operations, and view results.

## Features

- Load data from text files
- Perform basic data operations (filtering, sorting, calculations)
- Display data in tabular format
- Calculate statistics (sum, average, min, max)
- Export processed data

## Data Format

The program expects data in a simple CSV-like format:
```
Name,Age,City,Salary
John,25,New York,50000
Jane,30,London,60000
Bob,35,Paris,55000
```

## Example Usage

```
Simple Data Processor
=====================

Data Operations Menu:
1. Load Data File
2. View Data
3. Filter Data
4. Sort Data
5. Calculate Statistics
6. Export Data
7. Exit

Enter choice (1-7): 1
Enter filename: sample_data.txt
 Data loaded successfully! (4 records)

Enter choice (1-7): 5
Column to analyze: Salary
Sum: 165000.0
Average: 41250.0
Minimum: 50000.0
Maximum: 60000.0
```

## Learning Outcomes

This application demonstrates:
- **File I/O**: Reading and writing text files
- **Data Structures**: Using lists and dictionaries for data storage
- **Data Processing**: Filtering, sorting, and analyzing data
- **Error Handling**: Managing file and data errors
- **User Interface**: Creating a menu-driven application
- **Data Validation**: Ensuring data integrity

## Code Structure

- `main()`: Program entry point and menu system
- `load_data()`: Reads data from file into memory
- `display_data()`: Shows data in tabular format
- `filter_data()`: Filters records based on conditions
- `sort_data()`: Sorts data by specified column
- `calculate_stats()`: Computes statistical measures
- `export_data()`: Saves processed data to file

---

*Built as Level 2 of Stage 4: Full Problem Solving in the Python Programming Curriculum*