# Level 2: Data Management Problems

> **LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.c\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 3: Problem to Pseudocode

### Today's Mission

Data management is at the heart of most programs! Today you'll tackle problems involving collections of data, arrays, data manipulation, and information organization. You'll learn to design algorithms that store, update, search, and analyze data effectively.

---

### Learning Goals

- [ ] Design data structures for storing collections of information
- [ ] Create algorithms for data manipulation and updates
- [ ] Implement search and filter operations
- [ ] Handle data validation and integrity
- [ ] Organize complex data relationships

---

### Data Management Concepts

**Data Organization:**
- [ ] **Arrays**: Fixed-size collections of similar data
- [ ] **Records**: Related pieces of information grouped together
- [ ] **Collections**: Groups of related items
- [ ] **Relationships**: How different data pieces connect

**Data Operations:**
- [ ] **CRUD**: Create, Read, Update, Delete
- [ ] **Search**: Find specific items
- [ ] **Filter**: Select items meeting criteria
- [ ] **Sort**: Organize data in specific order
- [ ] **Validate**: Ensure data integrity

---

### Your Task

**For each data management problem:**
1. **Analyze** the data requirements
2. **Design** appropriate data structures
3. **Plan** the data operations needed
4. **Write pseudocode** for your solution
5. **Implement** in C code with proper data management

---

## Problem 1: Student Grade Book

**Problem Description:**
Create a program that manages student grades for a class. The program should:
- [ ] Store up to 25 students with their names and grades
- [ ] Allow adding new students and their grades
- [ ] Display all students and their grades
- [ ] Calculate and display class statistics (average, highest, lowest)
- [ ] Find students with grades above a certain threshold

**Data Requirements:**
- [ ] Student names (strings)
- [ ] Student grades (0-100)
- [ ] Class statistics
- [ ] Search/filter capabilities

**Example Usage:**
```
1. Add Student
2. View All Students
3. Show Statistics
4. Find High Performers
5. Exit

Choice: 1
Enter student name: Alice
Enter grade: 95
Student added!

Choice: 3
Class Statistics:
Average: 87.5%
Highest: 95% (Alice)
Lowest: 80% (Bob)
```

**Your Task:**
1. Design data structures for student information
2. Write pseudocode for all operations
3. Implement complete grade book system

---

## Problem 2: Inventory Tracker

**Problem Description:**
Create an inventory management system for a small store with:
- [ ] Up to 50 different products
- [ ] Each product has name, price, and stock quantity
- [ ] Track total inventory value
- [ ] Alert when items are low stock (< 5 units)
- [ ] Search products by name
- [ ] Update stock levels

**Data Requirements:**
- [ ] Product catalog with multiple attributes
- [ ] Inventory calculations
- [ ] Stock level monitoring
- [ ] Search functionality

**Example Usage:**
```
Inventory System:
1. Add Product
2. Update Stock
3. Search Product
4. Show Low Stock Alert
5. Display Total Value
6. Exit

Choice: 1
Enter product name: Laptop
Enter price: $999.99
Enter initial stock: 10
Product added!

Choice: 4
Low Stock Alert:
- [ ] Mouse: 3 units remaining
- [ ] Keyboard: 2 units remaining
```

**Your Task:**
1. Design product data structure
2. Plan inventory operations
3. Write comprehensive pseudocode
4. Implement full inventory system

---

## Problem 3: Contact List Manager

**Problem Description:**
Build a digital address book that can:
- [ ] Store up to 100 contacts
- [ ] Each contact has name, phone number, and email
- [ ] Add new contacts
- [ ] Search contacts by name
- [ ] Display all contacts alphabetically
- [ ] Delete contacts
- [ ] Validate phone numbers and emails

**Data Requirements:**
- [ ] Contact records with multiple fields
- [ ] Search and sort capabilities
- [ ] Data validation
- [ ] Contact management operations

**Example Usage:**
```
Contact Manager:
1. Add Contact
2. Search Contact
3. Display All Contacts
4. Delete Contact
5. Exit

Choice: 1
Enter name: John Doe
Enter phone: (555) 123-4567
Enter email: john@example.com
Contact added!

Choice: 2
Enter search name: John
Found: John Doe - (555) 123-4567 - john@example.com
```

**Your Task:**
1. Design contact data structure
2. Plan contact operations and validation
3. Write detailed pseudocode
4. Implement contact management system

---

## Problem 4: Library Book Database

**Problem Description:**
Create a library system that tracks:
- [ ] Up to 200 books
- [ ] Each book has title, author, ISBN, and availability status
- [ ] Check out and return books
- [ ] Search by title, author, or ISBN
- [ ] Show overdue books (simplified)
- [ ] Generate library statistics

**Data Requirements:**
- [ ] Book records with multiple attributes
- [ ] Availability tracking
- [ ] Search across multiple fields
- [ ] Statistical reporting

**Example Usage:**
```
Library System:
1. Add Book
2. Search Books
3. Check Out Book
4. Return Book
5. Show Statistics
6. Exit

Choice: 5
Library Statistics:
Total Books: 150
Available: 120
Checked Out: 30
Most Popular Author: J.K. Rowling (8 books)
```

**Your Task:**
1. Design book database structure
2. Plan library operations
3. Write comprehensive pseudocode
4. Implement library management system

---

## Problem 5: Expense Tracker

**Problem Description:**
Build a personal finance tracker that:
- [ ] Records up to 100 expenses
- [ ] Each expense has date, description, amount, and category
- [ ] Categories: Food, Transportation, Entertainment, Utilities, Other
- [ ] Calculate spending by category
- [ ] Show monthly totals
- [ ] Find highest and lowest expenses
- [ ] Budget alerts

**Data Requirements:**
- [ ] Expense records with multiple attributes
- [ ] Category-based organization
- [ ] Date handling (simplified)
- [ ] Financial calculations and summaries

**Example Usage:**
```
Expense Tracker:
1. Add Expense
2. View by Category
3. Show Monthly Summary
4. Find Expensive Items
5. Exit

Choice: 2
Spending by Category:
Food: $450.50
Transportation: $120.00
Entertainment: $89.99
Utilities: $200.00
Other: $50.25
Total: $910.74
```

**Your Task:**
1. Design expense data structure
2. Plan financial tracking operations
3. Write detailed pseudocode
4. Implement expense management system

---

## Problem 6: Task Management System

**Problem Description:**
Create a to-do list manager that can:
- [ ] Store up to 50 tasks
- [ ] Each task has title, description, priority (High/Medium/Low), and completion status
- [ ] Add new tasks
- [ ] Mark tasks as complete
- [ ] Display tasks by priority
- [ ] Search tasks by title
- [ ] Show completion statistics

**Data Requirements:**
- [ ] Task records with multiple attributes
- [ ] Priority-based organization
- [ ] Status tracking
- [ ] Search and filter capabilities

**Example Usage:**
```
Task Manager:
1. Add Task
2. Complete Task
3. View by Priority
4. Search Tasks
5. Show Statistics
6. Exit

Choice: 3
High Priority Tasks:
1. Finish project report (Not completed)
2. Call dentist (Not completed)

Medium Priority Tasks:
1. Buy groceries (Completed)
2. Clean room (Not completed)
```

**Your Task:**
1. Design task data structure
2. Plan task management operations
3. Write comprehensive pseudocode
4. Implement task management system

---

### Data Structure Design Guidelines

**Choosing Data Structures:**
- [ ] **Arrays**: When you know the maximum size
- [ ] **Strings**: For text data (names, descriptions)
- [ ] **Numbers**: For quantities, prices, scores
- [ ] **Flags**: For boolean status (true/false, yes/no)

**Data Organization:**
- [ ] **Group related data** together
- [ ] **Use consistent naming** conventions
- [ ] **Plan for growth** (leave room for expansion)
- [ ] **Consider access patterns** (how data will be used)

**Example Design:**
```
Student Grade Book:
- [ ] student_names[100][50] - array of strings
- [ ] student_grades[100] - array of floats
- [ ] student_count - current number of students

Each student[i] corresponds to:
- [ ] student_names[i] and student_grades[i]
```

---

### Success Checklist

**Data Design:**
- [ ] Identified all data elements needed
- [ ] Chose appropriate data types
- [ ] Designed logical data relationships
- [ ] Planned for data capacity limits

**Operations:**
- [ ] Implemented all required CRUD operations
- [ ] Added search and filter capabilities
- [ ] Included data validation
- [ ] Provided meaningful error messages

**User Experience:**
- [ ] Clear menu-driven interface
- [ ] Helpful prompts and instructions
- [ ] Formatted data display
- [ ] Confirmation of successful operations

---

### Try This (Optional Challenges)

1. **Data Persistence**: Save/load data to files
2. **Advanced Search**: Multiple search criteria
3. **Sorting**: Sort data by different fields
4. **Reports**: Generate summary reports

---

## Data Management Patterns

### Array Management
```
Initialize array and counter
While adding items:
    If not at capacity:
        Store item in array[index]
        Increment counter
    Else:
        Show capacity error
```

### Search Operations
```
Initialize found flag to false
For each item in collection:
    If item matches search criteria:
        Display item information
        Set found flag to true
If not found:
    Display "not found" message
```

### Data Validation
```
When receiving input:
    Check if input is valid format
    Check if input is within acceptable range
    Check for required fields
    Show appropriate error messages
```

### Statistical Calculations
```
Initialize accumulator variables
For each data item:
    Add to running totals
    Update min/max trackers
    Count valid items
Calculate averages and percentages
Display formatted results
```

---

<div style="page-break-after: always;"></div>

---

## SOLUTION APPROACH (Read after attempting!)

### Problem 1: Student Grade Book

**Data Structure Design:**
```
student_names[25][50] - array of student names
student_grades[25] - array of corresponding grades
student_count - number of students currently stored
```

**Key Operations:**
- [ ] Add student: Validate grade range, store in next available slot
- [ ] Display all: Loop through arrays, format output
- [ ] Statistics: Calculate average, find min/max with names
- [ ] Search: Loop through arrays, compare against threshold

**Edge Cases:**
- [ ] Empty grade book
- [ ] Full grade book (25 students)
- [ ] Invalid grades (outside 0-100)
- [ ] Single student statistics

---

### Problem 2: Inventory Tracker

**Data Structure Design:**
```
product_names[50][50] - product names
product_prices[50] - product prices
product_stock[50] - current stock levels
product_count - number of products
```

**Key Operations:**
- [ ] Add product: Store name, price, initial stock
- [ ] Update stock: Find product, modify stock level
- [ ] Search: Find products by name substring
- [ ] Low stock: Check all products, alert if < 5 units
- [ ] Total value: Sum (price × stock) for all products

**Business Logic:**
- [ ] Stock cannot go negative
- [ ] Price must be positive
- [ ] Product names must be unique

---

### Problem 3: Contact List Manager

**Data Structure Design:**
```
contact_names[100][50] - contact names
contact_phones[100][20] - phone numbers
contact_emails[100][50] - email addresses
contact_count - number of contacts
```

**Key Operations:**
- [ ] Add contact: Validate phone/email format, store all fields
- [ ] Search: Find contacts by name (partial match)
- [ ] Display: Sort alphabetically or by addition order
- [ ] Delete: Find and remove contact, shift remaining contacts

**Validation Rules:**
- [ ] Phone: Basic format check (digits, parentheses, dashes)
- [ ] Email: Contains @ and . in reasonable positions
- [ ] Name: Not empty, reasonable length

---

### Problem 4: Library Book Database

**Data Structure Design:**
```
book_titles[200][100] - book titles
book_authors[200][50] - author names
book_isbns[200][20] - ISBN numbers
book_available[200] - availability status (1=available, 0=checked out)
book_count - number of books
```

**Key Operations:**
- [ ] Add book: Store all book information
- [ ] Search: Find by title, author, or ISBN
- [ ] Check out/return: Update availability status
- [ ] Statistics: Count total, available, checked out books

**Advanced Features:**
- [ ] Due date tracking (simplified)
- [ ] Popular author identification
- [ ] Book reservation system

---

### Problem 5: Expense Tracker

**Data Structure Design:**
```
expense_dates[100][20] - expense dates (MM/DD/YYYY format)
expense_descriptions[100][100] - expense descriptions
expense_amounts[100] - expense amounts
expense_categories[100] - category indices (0=Food, 1=Transportation, etc.)
expense_count - number of expenses
```

**Key Operations:**
- [ ] Add expense: Store all expense details
- [ ] Category summary: Sum expenses by category
- [ ] Monthly totals: Group by month (simplified)
- [ ] Budget alerts: Compare against monthly budgets

**Categories Array:**
```
categories[5] = {"Food", "Transportation", "Entertainment", "Utilities", "Other"}
```

---

### Problem 6: Task Management System

**Data Structure Design:**
```
task_titles[50][100] - task titles
task_descriptions[50][200] - task descriptions
task_priorities[50] - priority levels (0=Low, 1=Medium, 2=High)
task_completed[50] - completion status (0=pending, 1=completed)
task_count - number of tasks
```

**Key Operations:**
- [ ] Add task: Store all task information
- [ ] Complete task: Find and mark as completed
- [ ] Display by priority: Group and show tasks by priority level
- [ ] Search: Find tasks by title substring
- [ ] Statistics: Completion rates, priority distribution

**Priority Display:**
```
High Priority: Show first (most important)
Medium Priority: Show second
Low Priority: Show last
Completed tasks: Show with checkmark
```

---

### Implementation Strategy

**Start with Core Data Structure:**
```c
# define MAX_ITEMS 100
char names[MAX_ITEMS][50];
float values[MAX_ITEMS];
int count = 0;
```

**Add One Operation at a Time:**
1. Implement data storage
2. Add display functionality
3. Implement search
4. Add statistics
5. Add validation

**Test Incrementally:**
- [ ] Test with 1 item first
- [ ] Test with maximum capacity
- [ ] Test edge cases (empty, full, invalid data)
- [ ] Test all operations in combination

---

 **Excellent! You're mastering data management and organization!** 

*Data structures are the foundation of all software. Next: Mathematical problem solving! *

### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim


### Additional Content

Understand the key concepts:

- [ ] Review each function
- [ ] Understand the flow
- [ ] Learn the patterns used


### Code Review

Key functions and their purpose:

- [ ] Main function: Entry point
- [ ] Helper functions: Support logic


### <div style="page-break-after: always;"></div>

Answer Key

Expected implementation provided.

<div style="page-break-after: always;"></div>

---

## Answer Key

### Complete Solution

```
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard C++ conventions with proper imports and main function
2. **Output**: Uses printf to print messages to the console
3. **Standard Library**: Includes stdio.h for input/output operations
4. **Return Value**: Returns 0 to indicate successful execution
5. **Best Practices**: Code is readable and uses C++ idioms

### Testing Your Solution

1. **Compile**: `gcc main.c -o main`
2. **Run**: `./hello`
3. **Expected Output**: `Hello, World!`

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `command not found: gcc` | Compiler not installed | `sudo apt install gcc` (Ubuntu) |
| `undefined reference to main` | Missing main function | Ensure `int main()` exists |
| `error: implicit declaration of function 'printf'` | Missing stdio.h | Add `#include <stdio.h>` |

### Tips for Learning

- C uses stdio.h for input/output with additional features
- `printf` is the C standard for formatted output
- `\n` adds a newline character in format strings
- Format specifiers control how data is displayed (%d, %f, %s, etc.)
