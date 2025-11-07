# Level 6: Automated Application - File Organizer

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Learning Objectives

By completing this level, you will:

- Understand how to create automated batch processing applications
- Learn file system operations and path manipulation
- Practice command-line argument parsing and configuration
- Implement safe file operations with error handling
- Design applications that work with minimal user interaction

## Code Analysis

### Application Structure

The File Organizer demonstrates automated processing:

1. **Configuration Phase**: Parse command-line arguments and setup
2. **Discovery Phase**: Scan directory for files to process
3. **Analysis Phase**: Determine appropriate categories for each file
4. **Execution Phase**: Move files to categorized directories
5. **Reporting Phase**: Provide summary of operations performed

### Key Components

**File Categorization System:**
```python
self.categories = {
    'Documents': ['.pdf', '.doc', '.docx', ...],
    'Images': ['.jpg', '.jpeg', '.png', ...],
    # ...
}
```python
Uses a dictionary to map file extensions to organizational categories.

**Path Handling:**
Utilizes Python's `pathlib` for cross-platform file operations:
- `Path` objects for directory and file manipulation
- Automatic path resolution and validation
- Safe handling of different operating systems

**Command-Line Interface:**
```python
parser = argparse.ArgumentParser(description='Automatically organize files by type')
parser.add_argument('directory', help='Directory to organize')
parser.add_argument('--dry-run', action='store_true', help='Show what would be done')
```bash

### Automation Principles

1. **Batch Processing**: Handles multiple files in a single operation
2. **Idempotent Operations**: Can be run multiple times safely
3. **Error Recovery**: Continues processing even if individual files fail
4. **Preview Mode**: Dry-run capability for safe testing
5. **Comprehensive Reporting**: Detailed feedback on all operations

## Success Checklist

- [ ] Application accepts directory path as command-line argument
- [ ] Dry-run mode shows intended operations without executing them
- [ ] Files are correctly categorized by extension
- [ ] Category directories are created automatically
- [ ] Duplicate filenames are handled gracefully
- [ ] Comprehensive error handling for file operations
- [ ] Summary statistics are displayed at completion
- [ ] Application works on different file types and extensions
- [ ] Code handles edge cases (empty directories, permission errors)

## Key Concepts Demonstrated

- [ ] **Automated Processing**: Applications that run with minimal user intervention
- [ ] **File System Operations**: Reading, moving, and organizing files programmatically
- [ ] **Command-Line Interfaces**: Argument parsing and configuration through CLI
- [ ] **Error Handling**: Robust exception handling for I/O operations
- [ ] **Data Structures**: Dictionary-based categorization and mapping
- [ ] **Path Manipulation**: Cross-platform file path handling with pathlib
- [ ] **Batch Operations**: Processing multiple items efficiently

## Potential Enhancements

- [ ] Add recursive directory processing
- [ ] Implement custom categorization rules
- [ ] Add file size or date-based organization
- [ ] Create undo functionality
- [ ] Add compression for archive categories
- [ ] Implement logging to track operations
- [ ] Add progress bars for large operations

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

> **NEEDS_AUTHOR:** This lesson needs a complete answer key with code breakdown, execution process explanation, common errors table, and bonus knowledge section. Reference c-c++/stage-1/level-1/lesson.md for the gold standard format.

### Key Concepts

- Review the code structure specific to Python
- Understand the execution flow
- Learn common pitfalls and solutions

### Next Steps

Practice the code and experiment with variations!

---

**Congratulations! Keep coding!**


### Learning Goals

- Understand core concepts
- Practice implementation


### Your Task

1. Review the code structure
2. Implement the required functionality
3. Test your solution


### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim


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
Automated File Organizer
A script that automatically organizes files in a directory based on their file types.
"""

import os
import shutil
from pathlib import Path
import argparse
import sys

class FileOrganizer:
    def __init__(self, target_directory, dry_run=False):
        self.target_directory = Path(target_directory)
        self.dry_run = dry_run
        self.stats = {
            'files_processed': 0,
            'files_moved': 0,
            'directories_created': 0,
            'errors': 0
        }

        # Define file type categories and their extensions
        self.categories = {
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.ico'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
            'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
            'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go', '.rs'],
            'Executables': ['.exe', '.msi', '.dmg', '.app', '.deb', '.rpm'],
            'Others': []  # Catch-all for unrecognized extensions
        }

    def get_category(self, file_path):
        """Determine the category for a file based on its extension."""
        extension = file_path.suffix.lower()

        for category, extensions in self.categories.items():
            if extension in extensions:
                return category

        return 'Others'

    def create_category_directory(self, category):
        """Create a directory for the specified category if it doesn't exist."""
        category_dir = self.target_directory / category

        if not category_dir.exists():
            if not self.dry_run:
                try:
                    category_dir.mkdir(parents=True, exist_ok=True)
                    print(f"Created directory: {category_dir}")
                except Exception as e:
                    print(f"Error creating directory {category_dir}: {e}")
                    self.stats['errors'] += 1
                    return None
            else:
                print(f"Would create directory: {category_dir}")

            self.stats['directories_created'] += 1

        return category_dir

    def move_file(self, source_path, destination_dir):
        """Move a file to the destination directory."""
        filename = source_path.name
        destination_path = destination_dir / filename

        # Handle filename conflicts
        counter = 1
        while destination_path.exists():
            stem = source_path.stem
            suffix = source_path.suffix
            new_filename = f"{stem}_{counter}{suffix}"
            destination_path = destination_dir / new_filename
            counter += 1

        if not self.dry_run:
            try:
                shutil.move(str(source_path), str(destination_path))
                print(f"Moved: {source_path} → {destination_path}")
            except Exception as e:
                print(f"Error moving {source_path}: {e}")
                self.stats['errors'] += 1
                return False
        else:
            print(f"Would move: {source_path} → {destination_path}")

        self.stats['files_moved'] += 1
        return True

    def organize_files(self):
        """Main method to organize all files in the target directory."""
        if not self.target_directory.exists():
            print(f"Error: Directory '{self.target_directory}' does not exist.")
            return False

        if not self.target_directory.is_dir():
            print(f"Error: '{self.target_directory}' is not a directory.")
            return False

        print(f"Starting file organization in: {self.target_directory}")
        if self.dry_run:
            print("DRY RUN MODE - No files will be moved")
        print("-" * 50)

        # Get all files in the directory (not subdirectories)
        files = [f for f in self.target_directory.iterdir() if f.is_file()]

        if not files:
            print("No files found to organize.")
            return True

        for file_path in files:
            self.stats['files_processed'] += 1

            # Skip the script itself if it's in the target directory
            if file_path.name == 'main.py':
                continue

            category = self.get_category(file_path)
            category_dir = self.create_category_directory(category)

            if category_dir:
                self.move_file(file_path, category_dir)

        return True

    def print_summary(self):
        """Print a summary of the organization process."""
        print("\n" + "="*50)
        print("ORGANIZATION SUMMARY")
        print("="*50)
        print(f"Files processed: {self.stats['files_processed']}")
        print(f"Files moved: {self.stats['files_moved']}")
        print(f"Directories created: {self.stats['directories_created']}")
        print(f"Errors encountered: {self.stats['errors']}")

        if self.dry_run:
            print("\nThis was a dry run. No files were actually moved.")
            print("Run without --dry-run to perform the actual organization.")
        else:
            print("\nFile organization completed successfully!")

def main():
    """Main application entry point."""
    parser = argparse.ArgumentParser(description='Automatically organize files by type')
    parser.add_argument('directory', help='Directory to organize')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be done without making changes')

    args = parser.parse_args()

    # If no directory provided, use current directory
    if not args.directory:
        args.directory = '.'

    organizer = FileOrganizer(args.directory, args.dry_run)

    success = organizer.organize_files()
    organizer.print_summary()

    if not success:
        sys.exit(1)

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
