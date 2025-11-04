# Level 7: Complex System Problems

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 3: Problem to Pseudocode

### Today's Mission

Complex system problems require integrating multiple components and managing system-wide interactions. You'll design a solution for a comprehensive system with multiple interacting parts.

---

### Learning Goals

- Analyze complex system requirements
- Design modular system components
- Manage data flow between components
- Create comprehensive system logic

---

### Your Task

**Read the problem below, then write pseudocode to solve it. Create a file called `complex_system_problems.md` with your pseudocode solution.**

### Problem: Library Management System

**Description:**
Create a comprehensive library management system that handles books, patrons, and transactions. The system should:

1. **Book Management:**
   - Add/remove books from catalog
   - Track book availability and location
   - Search books by title, author, genre

2. **Patron Management:**
   - Register new patrons
   - Track patron information and borrowing history
   - Manage patron status (active, suspended, etc.)

3. **Transaction Processing:**
   - Check out books to patrons
   - Process returns
   - Handle overdue books and fines
   - Reserve books when unavailable

4. **Reporting:**
   - Generate circulation statistics
   - List overdue books
   - Show popular books
   - Patron borrowing summaries

**System Requirements:**
- Maximum 3 books per patron at a time
- 14-day checkout period
- $0.25 per day overdue fine
- Books can be reserved when checked out

**Example Interaction:**
```
Library Management System
=========================

Main Menu:
1. Book Management
2. Patron Management
3. Circulation (Check out/Return)
4. Reports
5. Exit

Enter choice (1-5): 1

Book Management Menu:
1. Add New Book
2. Remove Book
3. Search Books
4. List All Books
5. Back to Main Menu

Enter choice (1-5): 1

Add New Book
------------
Enter ISBN: 978-0-123456-78-9
Enter title: The Rust Programming Language
Enter author: Steve Klabnik
Enter genre: Technology
Enter publication year: 2018
Book added successfully! ID: B001

Circulation Menu:
1. Check Out Book
2. Return Book
3. Renew Book
4. View Overdue Books
5. Back to Main Menu

Enter choice (1-5): 1

Check Out Book
--------------
Enter patron ID: P001
Enter book ID: B001

Checkout Summary:
Patron: John Doe
Book: The Rust Programming Language
Due Date: 2024-01-15
Status: SUCCESS

Reports Menu:
1. Circulation Statistics
2. Overdue Books Report
3. Popular Books Report
4. Patron Summary
5. Back to Main Menu

Enter choice (1-5): 1

Circulation Statistics (Last 30 Days)
=====================================
Total Checkouts: 45
Total Returns: 42
Currently Checked Out: 18
Overdue Books: 3
Total Fines Collected: $12.75
Most Popular Genre: Technology
Most Popular Book: The Rust Programming Language (8 checkouts)
```

---

### How to Create Your Solution

1. **Navigate to your working directory**:
   ```bash
   cd /path/to/your/folder
   ```
2. **Create your pseudocode file**:
   ```bash
   touch complex_system_problems.md
   ```
3. **Design system architecture** - Major components and their interactions
4. **Plan data structures** - How to store books, patrons, transactions
5. **Design menu system** - Navigation between different functions

---

### Success Checklist

- [ ] Created `complex_system_problems.md` file
- [ ] Designed modular system components (books, patrons, circulation)
- [ ] Planned data structures for complex relationships
- [ ] Created comprehensive menu navigation
- [ ] Designed transaction processing logic

---

### What Did You Learn?

Complex system analysis involves:
- **System architecture** - Breaking down large systems into components
- **Data relationships** - Managing connections between different entities
- **State management** - Tracking system status across operations
- **Error handling** - Managing complex failure scenarios

---

### Try This (Optional Challenges)

1. Add book reservation system
2. Implement fine payment processing
3. Add inter-library loan capabilities

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Problem Analysis

**System Components:**
- **Book Catalog**: Collection of all books with metadata
- **Patron Registry**: User accounts with borrowing privileges
- **Circulation Records**: Transaction history and current checkouts
- **Reservation System**: Queue for unavailable books

**Key Relationships:**
- Books ↔ Patrons (through checkouts)
- Books ↔ Reservations (waitlist system)
- Patrons ↔ Fines (overdue penalties)
- Transactions ↔ Time (due dates, overdue calculations)

**System Flow:**
```
Main Loop:
    Display main menu
    Process user choice
    Route to appropriate subsystem
    Handle transactions
    Update system state
    Return to main menu
```

### Sample Pseudocode Solution

```
START PROGRAM
    // Initialize system data structures
    INITIALIZE_BOOK_CATALOG()
    INITIALIZE_PATRON_REGISTRY()
    INITIALIZE_CIRCULATION_RECORDS()
    INITIALIZE_RESERVATION_SYSTEM()
    
    SET running TO true
    WHILE running == true DO
        DISPLAY "Library Management System"
        DISPLAY "========================="
        DISPLAY ""
        DISPLAY "Main Menu:"
        DISPLAY "1. Book Management"
        DISPLAY "2. Patron Management"
        DISPLAY "3. Circulation (Check out/Return)"
        DISPLAY "4. Reports"
        DISPLAY "5. Exit"
        DISPLAY ""
        DISPLAY "Enter choice (1-5):"
        READ main_choice AS NUMBER
        
        IF main_choice == 1 THEN
            HANDLE_BOOK_MANAGEMENT()
        ELSE IF main_choice == 2 THEN
            HANDLE_PATRON_MANAGEMENT()
        ELSE IF main_choice == 3 THEN
            HANDLE_CIRCULATION()
        ELSE IF main_choice == 4 THEN
            HANDLE_REPORTS()
        ELSE IF main_choice == 5 THEN
            SET running TO false
            DISPLAY "Thank you for using Library Management System!"
        ELSE
            DISPLAY "Invalid choice. Please select 1-5."
        END IF
        DISPLAY ""
    END WHILE
END PROGRAM

// ===== BOOK MANAGEMENT SYSTEM =====
PROCEDURE HANDLE_BOOK_MANAGEMENT()
    SET book_menu_running TO true
    WHILE book_menu_running == true DO
        DISPLAY "Book Management Menu:"
        DISPLAY "1. Add New Book"
        DISPLAY "2. Remove Book"
        DISPLAY "3. Search Books"
        DISPLAY "4. List All Books"
        DISPLAY "5. Back to Main Menu"
        DISPLAY ""
        DISPLAY "Enter choice (1-5):"
        READ book_choice AS NUMBER
        
        IF book_choice == 1 THEN
            ADD_NEW_BOOK()
        ELSE IF book_choice == 2 THEN
            REMOVE_BOOK()
        ELSE IF book_choice == 3 THEN
            SEARCH_BOOKS()
        ELSE IF book_choice == 4 THEN
            LIST_ALL_BOOKS()
        ELSE IF book_choice == 5 THEN
            SET book_menu_running TO false
        ELSE
            DISPLAY "Invalid choice."
        END IF
    END WHILE
END PROCEDURE

PROCEDURE ADD_NEW_BOOK()
    DISPLAY "Add New Book"
    DISPLAY "------------"
    
    DISPLAY "Enter ISBN:"
    READ isbn AS STRING
    
    // Check if book already exists
    IF BOOK_EXISTS(isbn) THEN
        DISPLAY "Book with this ISBN already exists!"
        RETURN
    END IF
    
    DISPLAY "Enter title:"
    READ title AS STRING
    
    DISPLAY "Enter author:"
    READ author AS STRING
    
    DISPLAY "Enter genre:"
    READ genre AS STRING
    
    DISPLAY "Enter publication year:"
    READ year AS NUMBER
    
    // Generate unique book ID
    SET book_id TO GENERATE_BOOK_ID()
    
    // Add to catalog
    ADD_BOOK_TO_CATALOG(book_id, isbn, title, author, genre, year, "available")
    
    DISPLAY "Book added successfully! ID: " + book_id
END PROCEDURE

PROCEDURE SEARCH_BOOKS()
    DISPLAY "Search Books"
    DISPLAY "-----------"
    DISPLAY "Search by:"
    DISPLAY "1. Title"
    DISPLAY "2. Author"
    DISPLAY "3. Genre"
    DISPLAY "4. ISBN"
    READ search_type AS NUMBER
    
    DISPLAY "Enter search term:"
    READ search_term AS STRING
    
    SET results TO SEARCH_BOOK_CATALOG(search_type, search_term)
    
    IF results IS EMPTY THEN
        DISPLAY "No books found matching your search."
    ELSE
        DISPLAY "Search Results:"
        FOR EACH book IN results DO
            DISPLAY_BOOK_INFO(book)
        END FOR
    END IF
END PROCEDURE

// ===== PATRON MANAGEMENT SYSTEM =====
PROCEDURE HANDLE_PATRON_MANAGEMENT()
    SET patron_menu_running TO true
    WHILE patron_menu_running == true DO
        DISPLAY "Patron Management Menu:"
        DISPLAY "1. Register New Patron"
        DISPLAY "2. Update Patron Info"
        DISPLAY "3. Search Patrons"
        DISPLAY "4. View Patron History"
        DISPLAY "5. Back to Main Menu"
        DISPLAY ""
        DISPLAY "Enter choice (1-5):"
        READ patron_choice AS NUMBER
        
        IF patron_choice == 1 THEN
            REGISTER_PATRON()
        ELSE IF patron_choice == 2 THEN
            UPDATE_PATRON()
        ELSE IF patron_choice == 3 THEN
            SEARCH_PATRONS()
        ELSE IF patron_choice == 4 THEN
            VIEW_PATRON_HISTORY()
        ELSE IF patron_choice == 5 THEN
            SET patron_menu_running TO false
        ELSE
            DISPLAY "Invalid choice."
        END IF
    END WHILE
END PROCEDURE

PROCEDURE REGISTER_PATRON()
    DISPLAY "Register New Patron"
    DISPLAY "-------------------"
    
    DISPLAY "Enter full name:"
    READ name AS STRING
    
    DISPLAY "Enter email:"
    READ email AS STRING
    
    DISPLAY "Enter phone:"
    READ phone AS STRING
    
    // Generate unique patron ID
    SET patron_id TO GENERATE_PATRON_ID()
    
    // Add to registry
    ADD_PATRON_TO_REGISTRY(patron_id, name, email, phone, "active", 0.00)
    
    DISPLAY "Patron registered successfully! ID: " + patron_id
END PROCEDURE

// ===== CIRCULATION SYSTEM =====
PROCEDURE HANDLE_CIRCULATION()
    SET circulation_menu_running TO true
    WHILE circulation_menu_running == true DO
        DISPLAY "Circulation Menu:"
        DISPLAY "1. Check Out Book"
        DISPLAY "2. Return Book"
        DISPLAY "3. Renew Book"
        DISPLAY "4. View Overdue Books"
        DISPLAY "5. Process Reservations"
        DISPLAY "6. Back to Main Menu"
        DISPLAY ""
        DISPLAY "Enter choice (1-6):"
        READ circulation_choice AS NUMBER
        
        IF circulation_choice == 1 THEN
            CHECK_OUT_BOOK()
        ELSE IF circulation_choice == 2 THEN
            RETURN_BOOK()
        ELSE IF circulation_choice == 3 THEN
            RENEW_BOOK()
        ELSE IF circulation_choice == 4 THEN
            VIEW_OVERDUE_BOOKS()
        ELSE IF circulation_choice == 5 THEN
            PROCESS_RESERVATIONS()
        ELSE IF circulation_choice == 6 THEN
            SET circulation_menu_running TO false
        ELSE
            DISPLAY "Invalid choice."
        END IF
    END WHILE
END PROCEDURE

PROCEDURE CHECK_OUT_BOOK()
    DISPLAY "Check Out Book"
    DISPLAY "--------------"
    
    DISPLAY "Enter patron ID:"
    READ patron_id AS STRING
    
    IF NOT PATRON_EXISTS(patron_id) THEN
        DISPLAY "Patron not found!"
        RETURN
    END IF
    
    // Check patron status and limits
    IF GET_PATRON_STATUS(patron_id) != "active" THEN
        DISPLAY "Patron account is not active."
        RETURN
    END IF
    
    IF GET_PATRON_CHECKOUT_COUNT(patron_id) >= 3 THEN
        DISPLAY "Patron has reached maximum checkout limit (3 books)."
        RETURN
    END IF
    
    DISPLAY "Enter book ID:"
    READ book_id AS STRING
    
    IF NOT BOOK_EXISTS_BY_ID(book_id) THEN
        DISPLAY "Book not found!"
        RETURN
    END IF
    
    IF GET_BOOK_STATUS(book_id) != "available" THEN
        DISPLAY "Book is not available for checkout."
        // Offer reservation
        DISPLAY "Would you like to reserve this book? (y/n):"
        READ reserve_choice AS STRING
        IF reserve_choice == "y" THEN
            ADD_RESERVATION(patron_id, book_id)
            DISPLAY "Book reserved successfully!"
        END IF
        RETURN
    END IF
    
    // Calculate due date (14 days from today)
    SET due_date TO CALCULATE_DUE_DATE(14)
    
    // Process checkout
    CHECKOUT_BOOK(patron_id, book_id, due_date)
    UPDATE_BOOK_STATUS(book_id, "checked_out")
    
    DISPLAY "Checkout Summary:"
    DISPLAY "Patron: " + GET_PATRON_NAME(patron_id)
    DISPLAY "Book: " + GET_BOOK_TITLE(book_id)
    DISPLAY "Due Date: " + due_date
    DISPLAY "Status: SUCCESS"
END PROCEDURE

PROCEDURE RETURN_BOOK()
    DISPLAY "Return Book"
    DISPLAY "-----------"
    
    DISPLAY "Enter book ID:"
    READ book_id AS STRING
    
    IF NOT BOOK_EXISTS_BY_ID(book_id) THEN
        DISPLAY "Book not found!"
        RETURN
    END IF
    
    IF GET_BOOK_STATUS(book_id) != "checked_out" THEN
        DISPLAY "This book is not checked out."
        RETURN
    END IF
    
    // Get checkout record
    SET checkout_record TO GET_CHECKOUT_RECORD(book_id)
    SET patron_id TO checkout_record.patron_id
    SET due_date TO checkout_record.due_date
    
    // Calculate any fines
    SET days_overdue TO CALCULATE_DAYS_OVERDUE(due_date)
    SET fine_amount TO 0.00
    
    IF days_overdue > 0 THEN
        SET fine_amount TO days_overdue * 0.25
        DISPLAY "Book is " + days_overdue + " days overdue."
        DISPLAY "Fine amount: $" + FORMAT_CURRENCY(fine_amount)
        
        // Add fine to patron account
        ADD_FINE_TO_PATRON(patron_id, fine_amount)
    END IF
    
    // Process return
    RETURN_BOOK_TRANSACTION(book_id)
    UPDATE_BOOK_STATUS(book_id, "available")
    
    // Check for reservations
    IF BOOK_HAS_RESERVATIONS(book_id) THEN
        SET next_reservation TO GET_NEXT_RESERVATION(book_id)
        NOTIFY_PATRON_OF_AVAILABLE_BOOK(next_reservation.patron_id, book_id)
        DISPLAY "Book is now reserved for another patron."
    END IF
    
    DISPLAY "Book returned successfully!"
    IF fine_amount > 0 THEN
        DISPLAY "Please pay fine amount at the circulation desk."
    END IF
END PROCEDURE

// ===== REPORTING SYSTEM =====
PROCEDURE HANDLE_REPORTS()
    SET reports_menu_running TO true
    WHILE reports_menu_running == true DO
        DISPLAY "Reports Menu:"
        DISPLAY "1. Circulation Statistics"
        DISPLAY "2. Overdue Books Report"
        DISPLAY "3. Popular Books Report"
        DISPLAY "4. Patron Summary"
        DISPLAY "5. Back to Main Menu"
        DISPLAY ""
        DISPLAY "Enter choice (1-5):"
        READ reports_choice AS NUMBER
        
        IF reports_choice == 1 THEN
            GENERATE_CIRCULATION_STATISTICS()
        ELSE IF reports_choice == 2 THEN
            GENERATE_OVERDUE_REPORT()
        ELSE IF reports_choice == 3 THEN
            GENERATE_POPULAR_BOOKS_REPORT()
        ELSE IF reports_choice == 4 THEN
            GENERATE_PATRON_SUMMARY()
        ELSE IF reports_choice == 5 THEN
            SET reports_menu_running TO false
        ELSE
            DISPLAY "Invalid choice."
        END IF
    END WHILE
END PROCEDURE

PROCEDURE GENERATE_CIRCULATION_STATISTICS()
    DISPLAY "Circulation Statistics (Last 30 Days)"
    DISPLAY "====================================="
    
    SET stats TO CALCULATE_CIRCULATION_STATS(30)
    
    DISPLAY "Total Checkouts: " + stats.total_checkouts
    DISPLAY "Total Returns: " + stats.total_returns
    DISPLAY "Currently Checked Out: " + stats.currently_checked_out
    DISPLAY "Overdue Books: " + stats.overdue_count
    DISPLAY "Total Fines Collected: $" + FORMAT_CURRENCY(stats.total_fines)
    DISPLAY "Most Popular Genre: " + stats.top_genre
    DISPLAY "Most Popular Book: " + stats.top_book + " (" + stats.top_book_checkouts + " checkouts)"
END PROCEDURE

// ===== UTILITY FUNCTIONS =====
// (These would contain the actual data management logic)

FUNCTION INITIALIZE_BOOK_CATALOG()
    // Initialize empty book catalog data structure
END FUNCTION

FUNCTION INITIALIZE_PATRON_REGISTRY()
    // Initialize empty patron registry data structure
END FUNCTION

FUNCTION INITIALIZE_CIRCULATION_RECORDS()
    // Initialize empty circulation records data structure
END FUNCTION

FUNCTION INITIALIZE_RESERVATION_SYSTEM()
    // Initialize empty reservation system data structure
END FUNCTION

FUNCTION GENERATE_BOOK_ID()
    // Generate unique book ID (e.g., B001, B002, etc.)
    RETURN "B" + NEXT_BOOK_NUMBER
END FUNCTION

FUNCTION GENERATE_PATRON_ID()
    // Generate unique patron ID (e.g., P001, P002, etc.)
    RETURN "P" + NEXT_PATRON_NUMBER
END FUNCTION

FUNCTION CALCULATE_DUE_DATE(days)
    // Calculate due date by adding days to current date
    RETURN CURRENT_DATE + days
END FUNCTION

FUNCTION CALCULATE_DAYS_OVERDUE(due_date)
    // Calculate how many days past due date
    RETURN MAX(0, CURRENT_DATE - due_date)
END FUNCTION

FUNCTION FORMAT_CURRENCY(amount)
    // Format number as currency (e.g., 12.50 -> $12.50)
    RETURN "$" + amount
END FUNCTION
```

### Analysis Breakdown

**System Architecture:**
- **Modular Design**: Separate procedures for each major function
- **Menu-Driven Interface**: Hierarchical menu system for navigation
- **Data Management**: Separate systems for books, patrons, circulation
- **Transaction Processing**: Comprehensive checkout/return logic

**Why this approach?**
- **Separation of Concerns**: Each subsystem handles specific functionality
- **Scalable Design**: Easy to add new features to existing modules
- **Data Integrity**: Centralized data management with validation
- **User-Friendly**: Clear menu navigation and feedback

**Potential improvements:**
- Database integration for persistent storage
- Advanced search and filtering capabilities
- Automated overdue notifications
- Integration with external systems (payment processing, etc.)

### Common Analysis Mistakes

| Common Issue | Why It Happens | Solution |
|--------------|----------------|----------|
| Monolithic code | Trying to handle everything in one place | Break into modular procedures |
| Poor data relationships | Not connecting related entities | Design clear data relationships upfront |
| No error handling | System crashes on invalid input | Add validation at all entry points |
| State inconsistency | Data gets out of sync | Use transactions for multi-step operations |

### Bonus Knowledge

- **System Design**: Breaking complex systems into manageable components
- **Data Modeling**: Designing relationships between different entities
- **Transaction Management**: Ensuring data consistency across operations
- **User Experience**: Creating intuitive interfaces for complex systems

---

 **Congratulations! You've designed a comprehensive library management system!** 

*This completes Stage 3: Problem to Pseudocode! Ready for Stage 4: Full Problem Solving?*