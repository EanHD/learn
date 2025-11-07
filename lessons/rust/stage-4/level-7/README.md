# Library Management System

A comprehensive Rust application for managing library operations including book inventory, user management, and transaction tracking with data persistence.

## Features

- **Complete Book Management**: Add, remove, search, and display books with status tracking
- **User Registration System**: Register users with borrowing limits and history tracking
- **Transaction Management**: Checkout, return, and track book loans with due dates
- **Data Persistence**: Save and load library state across sessions using custom file format
- **Advanced Search**: Search books by title, author, ISBN, or all fields
- **Reporting & Analytics**: Generate statistics, view overdue books, and track popular items
- **Robust Error Handling**: Comprehensive validation and user-friendly error messages
- **Multi-level Menu System**: Intuitive navigation through all library functions

## Quick Start

1. **Compile the program**:
   ```bash
   rustc main.rs
   ```

2. **Run the application**:
   ```bash
   ./main
   ```

3. **Use the menu system** to navigate and manage your library

4. **Data is automatically saved** when you exit the program

## Menu Structure

### Main Menu
- **1. Book Management** - Add, remove, search, and display books
- **2. User Management** - Register and view user information
- **3. Transaction Management** - Checkout, return, and track loans
- **4. Reports & Analytics** - View statistics and reports
- **5. Save & Exit** - Save data and exit the program

### Book Management Submenu
- Add new books to the library
- Remove books from circulation
- Search books by various criteria
- Display all books or just available ones

### User Management Submenu
- Register new library users
- View detailed user information
- Display all registered users

### Transaction Management Submenu
- Checkout books to users
- Return books from users
- View all active transactions

### Reports & Analytics Submenu
- Generate comprehensive library statistics
- View overdue books and notices
- Track most popular books

## Data Files

### library_data.txt
- **Purpose**: Stores all library data between sessions
- **Format**: Custom binary format (LIBRARY_DATA_V1)
- **Auto-created**: Generated automatically when you first save
- **Backup**: Consider backing up this file regularly

### File Structure
```
LIBRARY_DATA_V1
NEXT_IDS 4 3 2
BOOKS 3
1|Title|Author|ISBN|AVAILABLE
USERS 2
1|Name|Email|borrowed_books
TRANSACTIONS 1
1|book_id|user_id|checkout|due|return|status
```

## Usage Examples

### Adding Books
```
 ADD NEW BOOK
===============
Enter book title: The Rust Programming Language
Enter author name: Steve Klabnik
Enter ISBN: 978-1593278281
 Book added successfully with ID: 1
```

### Registering Users
```
 ADD NEW USER
===============
Enter user name: Alice Johnson
Enter email address: alice@example.com
 User added successfully with ID: 1
```

### Checking Out Books
```
 CHECKOUT BOOK
=================
Enter book ID: 1
Enter user ID: 1
Enter loan period in days: 14
 Book checked out successfully!
   Due date: Timestamp: 1735689600
```

### Searching Books
```
 SEARCH BOOKS
===============
Search by:
1. Title
2. Author
3. ISBN
4. All fields
Enter choice (1-4): 1
Enter search term: rust

Search Results:
---------------
Title: The Rust Programming Language
Author: Steve Klabnik
ISBN: 978-1593278281
Status: Available

Found 1 book(s) matching "rust"
```

## Core Concepts Demonstrated

### Data Structures
- **Structs**: Book, User, Transaction, Library
- **Enums**: BookStatus, TransactionStatus
- **Collections**: HashMap for efficient lookups, Vec for lists

### File I/O
- **Reading**: Load library data from custom format files
- **Writing**: Save complete library state to disk
- **Error Handling**: Robust file operation error recovery

### Memory Management
- **Ownership**: Proper data ownership and borrowing
- **References**: Efficient data access without copying
- **Lifetimes**: Managing data relationships safely

### Error Handling
- **Result Types**: Comprehensive error propagation
- **Custom Errors**: Domain-specific error messages
- **Validation**: Input validation at all levels

### Algorithm Design
- **Search Algorithms**: Multi-criteria book searching
- **Sorting**: Popular book ranking by transaction count
- **Filtering**: Available books, overdue items, active transactions

## Technical Architecture

### Library Struct
Central data structure containing:
- `books`: HashMap<u32, Book> - All library books
- `users`: HashMap<u32, User> - Registered users
- `transactions`: HashMap<u32, Transaction> - Transaction history
- ID counters for automatic ID generation

### Book Status System
- **Available**: Book ready for checkout
- **Borrowed**: Book loaned with due date
- **Overdue**: Book past due date

### Transaction Tracking
- Complete audit trail of all book movements
- Due date calculation and overdue detection
- Status tracking (Active, Returned, Overdue)

## Business Rules

### Borrowing Limits
- Default: 3 books per user
- Configurable per user
- Enforced at checkout

### Loan Periods
- User-specified duration (days)
- Automatic due date calculation
- Overdue detection and reporting

### Book Removal
- Only available books can be removed
- Borrowed books must be returned first
- Data integrity preservation

## Troubleshooting

### Common Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| File not found | "No existing library data found" | Normal for first run, data will be created |
| Compilation errors | Rust compiler warnings/errors | Check syntax, ensure all dependencies available |
| Invalid input | "Please enter a valid number" | Enter numeric values for IDs and choices |
| Book not available | "Book is not available" | Check book status, may be borrowed or overdue |
| User limit exceeded | "User has reached maximum book limit" | Return books before borrowing more |

### Data Recovery
- **Backup regularly**: Copy `library_data.txt` to safe location
- **File corruption**: Delete corrupted file, restart with empty library
- **Manual editing**: Edit file carefully, maintain exact format

### Performance Considerations
- **Large datasets**: HashMap provides O(1) lookup performance
- **Memory usage**: Efficient storage of book and user data
- **File I/O**: Minimal disk access, data loaded once at startup

## Advanced Features

### Search Capabilities
- **Multi-field search**: Title, author, ISBN simultaneously
- **Case-insensitive**: Search works regardless of case
- **Partial matching**: Find books containing search terms

### Analytics Engine
- **Real-time statistics**: Always up-to-date counts and metrics
- **Popularity tracking**: Transaction-based book ranking
- **Overdue management**: Automated overdue detection

### Data Integrity
- **Referential integrity**: All relationships validated
- **Atomic operations**: State changes are consistent
- **Error recovery**: Graceful handling of invalid operations

## Future Enhancements

### Potential Additions
- **Due date notifications**: Email alerts for upcoming due dates
- **Fine calculation**: Automatic late fee assessment
- **Book reservations**: Hold system for popular books
- **User categories**: Different limits for different user types
- **Bulk operations**: Import/export book data
- **Web interface**: REST API for web/mobile access
- **Barcode support**: ISBN scanning integration
- **Reporting**: Advanced analytics and custom reports

### Technical Improvements
- **Database integration**: Replace file storage with SQL database
- **Concurrent access**: Multi-user support with locking
- **Audit logging**: Detailed operation logging
- **Backup automation**: Scheduled data backups
- **API development**: RESTful API for integrations

## Learning Outcomes

This capstone project demonstrates mastery of:
- **Complex system design** and architecture
- **Data modeling** with relationships and constraints
- **File I/O** and data persistence techniques
- **Error handling** and validation strategies
- **User interface design** for complex applications
- **Algorithm implementation** for search and analytics
- **Memory management** in large applications
- **Code organization** and maintainability

## Educational Value

### Skills Developed
- **Systems thinking**: Understanding interconnected components
- **Data architecture**: Designing efficient data storage and access
- **User experience**: Creating intuitive interfaces for complex tasks
- **Quality assurance**: Comprehensive testing and validation
- **Documentation**: Clear code documentation and user guides

### Professional Readiness
- **Real-world application**: Production-quality software development
- **Scalability considerations**: Designing for growth and change
- **Maintenance mindset**: Writing maintainable, extensible code
- **Problem-solving**: Complex multi-constraint problem resolution

---

*Built as the capstone project for the complete Rust Programming Curriculum*

*This represents the culmination of 28 lessons across 4 stages of learning, from basic syntax to advanced system design.*