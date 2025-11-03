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