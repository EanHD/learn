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
```
self.categories = {
    'Documents': ['.pdf', '.doc', '.docx', ...],
    'Images': ['.jpg', '.jpeg', '.png', ...],
    # ...
}
```
Uses a dictionary to map file extensions to organizational categories.

**Path Handling:**
Utilizes Python's `pathlib` for cross-platform file operations:
- `Path` objects for directory and file manipulation
- Automatic path resolution and validation
- Safe handling of different operating systems

**Command-Line Interface:**
```
parser = argparse.ArgumentParser(description='Automatically organize files by type')
parser.add_argument('directory', help='Directory to organize')
parser.add_argument('--dry-run', action='store_true', help='Show what would be done')
```

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
