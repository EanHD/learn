# Level 7: Complex System Problems

> **LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.c\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 3: Problem to Pseudocode

### Today's Mission

**SYSTEM ARCHITECT!**  You're now designing and implementing complete multi-component systems that integrate multiple features and data types. This level focuses on creating cohesive programs with interconnected components.

**The Process:**
1. **Analyze** the system requirements and components
2. **Design** the system architecture and data flow
3. **Plan** component interactions and data sharing
4. **Implement** modular functions for each component
5. **Integrate** components into a cohesive system
6. **Write pseudocode** for the complete system
7. **Test system integration** thoroughly
8. **Implement** in C code

---

### Learning Goals

- [ ] Design multi-component system architecture
- [ ] Implement data flow between components
- [ ] Create modular, reusable functions
- [ ] Handle complex state management
- [ ] Integrate diverse system features
- [ ] Manage system complexity effectively

---

### System Architecture Framework

**STEP 1: System Analysis**
- [ ] What are the main system components?
- [ ] How do components interact?
- [ ] What data flows between components?
- [ ] What is the user workflow through the system?

**STEP 2: Component Design**
- [ ] Break system into logical modules
- [ ] Define interfaces between components
- [ ] Plan data structures for each component
- [ ] Design error handling and validation

**STEP 3: Integration Planning**
- [ ] How components share data
- [ ] What global state needs to be maintained?
- [ ] How to handle component dependencies?
- [ ] What integration testing is needed?

**STEP 4: System Implementation**
- [ ] Implement components in logical order
- [ ] Test component interactions
- [ ] Handle system-wide error conditions
- [ ] Optimize for performance and usability

---

### Your Task

**For each complex system:**
1. **Design** the system architecture and components
2. **Plan** data flow and component interactions
3. **Write pseudocode** for the integrated system
4. **Design modular functions** for each component
5. **Test system workflows** mentally
6. **Implement** in C code
7. **Validate** complete system functionality

---

## Problem 1: Student Management System

**Problem Description:**
Create a comprehensive student management system with:
- [ ] Student registration (name, ID, courses)
- [ ] Grade management (add/view grades per course)
- [ ] Attendance tracking (mark present/absent)
- [ ] Report generation (GPA, attendance percentage)
- [ ] Student search and modification

**Example:**
```
=== Student Management System ===
1. Register Student
2. Add Grades
3. Mark Attendance
4. View Student Report
5. Search Student
6. Exit

Enter choice: 1
Enter student name: Alice Johnson
Enter student ID: 12345
Enter number of courses: 3
Enter courses: Math Physics Chemistry

Student registered successfully!
```

**Your Task:**
1. Write pseudocode for the complete student management system
2. Test all system features and data flow
3. Implement in C code

---

## Problem 2: Inventory Management System

**Problem Description:**
Create an inventory system for a store with:
- [ ] Product catalog (name, price, stock level)
- [ ] Stock management (add/remove inventory)
- [ ] Sales processing (checkout, update stock)
- [ ] Low stock alerts
- [ ] Sales reporting (total sales, popular items)
- [ ] Product search and modification

**Example:**
```
=== Inventory Management ===
1. Add Product
2. Update Stock
3. Process Sale
4. View Inventory
5. Generate Report
6. Exit

Enter choice: 3
Enter product ID: 101
Enter quantity to sell: 2

Sale processed! Total: $29.98
Stock updated: Widget (8 remaining)
```

**Your Task:**
1. Write pseudocode for inventory system integration
2. Test inventory updates and sales processing
3. Implement in C code

---

## Problem 3: Bank Account Management System

**Problem Description:**
Create a banking system with multiple account types:
- [ ] Account creation (checking/savings)
- [ ] Deposits and withdrawals
- [ ] Fund transfers between accounts
- [ ] Transaction history
- [ ] Interest calculation for savings
- [ ] Account statements
- [ ] Balance inquiries

**Example:**
```
=== Banking System ===
1. Create Account
2. Deposit
3. Withdraw
4. Transfer
5. View History
6. Generate Statement
7. Exit

Enter choice: 4
From account: 1001
To account: 1002
Amount to transfer: 500

Transfer successful!
Account 1001 balance: $1,500.00
Account 1002 balance: $2,500.00
```

**Your Task:**
1. Write pseudocode for banking system components
2. Test account interactions and transactions
3. Implement in C code

---

## Problem 4: Hospital Patient Management

**Problem Description:**
Create a hospital management system with:
- [ ] Patient registration (name, ID, condition)
- [ ] Doctor assignment
- [ ] Appointment scheduling
- [ ] Treatment tracking
- [ ] Medication management
- [ ] Discharge processing
- [ ] Patient search and reports

**Example:**
```
=== Hospital Management ===
1. Register Patient
2. Schedule Appointment
3. Assign Doctor
4. Record Treatment
5. View Patient History
6. Discharge Patient
7. Exit

Enter choice: 2
Enter patient ID: 5001
Enter appointment date: 2024-01-15
Enter time: 14:00
Enter doctor: Dr. Smith

Appointment scheduled successfully!
```

**Your Task:**
1. Write pseudocode for hospital system workflow
2. Test patient journey through the system
3. Implement in C code

---

## Problem 5: E-commerce Shopping System

**Problem Description:**
Create an online shopping system with:
- [ ] Product catalog browsing
- [ ] Shopping cart management
- [ ] User accounts and profiles
- [ ] Order processing and checkout
- [ ] Order history and tracking
- [ ] Inventory management integration
- [ ] Customer reviews and ratings

**Example:**
```
=== E-commerce System ===
1. Browse Products
2. Add to Cart
3. View Cart
4. Checkout
5. View Order History
6. Manage Account
7. Exit

Enter choice: 2
Enter product ID: 2001
Enter quantity: 2

Added to cart! Cart total: $49.98
```

**Your Task:**
1. Write pseudocode for e-commerce system integration
2. Test shopping workflow and order processing
3. Implement in C code

---

## Problem 6: Game Character System

**Problem Description:**
Create a game character management system with:
- [ ] Character creation (name, class, stats)
- [ ] Inventory management (weapons, armor, items)
- [ ] Experience and leveling system
- [ ] Quest tracking and completion
- [ ] Skill development
- [ ] Equipment management
- [ ] Character statistics display

**Example:**
```
=== Character System ===
1. Create Character
2. Manage Inventory
3. Complete Quest
4. Level Up
5. View Stats
6. Equip Items
7. Exit

Enter choice: 3
Enter quest name: Dragon Hunt
Enter experience gained: 500

Quest completed! Experience: +500
Level up! Now level 5
New stats: HP +20, Attack +5
```

**Your Task:**
1. Write pseudocode for game character system
2. Test character progression and inventory management
3. Implement in C code

---

### System Architecture Guidelines

**Modular Design:**
```
System: Complex Application
├── Component 1: Data Management
│   ├── Function: Add Data
│   ├── Function: Update Data
│   └── Function: Delete Data
├── Component 2: User Interface
│   ├── Function: Display Menu
│   ├── Function: Get Input
│   └── Function: Show Results
├── Component 3: Business Logic
│   ├── Function: Process Data
│   ├── Function: Validate Rules
│   └── Function: Calculate Results
└── Integration: Main System Loop
    ├── Initialize System
    ├── Process User Requests
    └── Maintain System State
```

**Data Flow Planning:**
```
User Input → Validation → Processing → Storage → Output
              ↓           ↓         ↓        ↓
         Error Handling  Business  Database  Display
         Messages       Logic     Updates   Results
```

---

### Success Checklist

**For Each System:**
- [ ] **Architecture Design**: Clear system component breakdown
- [ ] **Data Flow**: Well-defined data movement between components
- [ ] **Component Integration**: Seamless interaction between modules
- [ ] **State Management**: Proper handling of system-wide data
- [ ] **Error Handling**: Robust error management across components
- [ ] **User Experience**: Intuitive navigation and feedback
- [ ] **Pseudocode**: Complete system algorithm design
- [ ] **Implementation**: Working integrated C code
- [ ] **Testing**: Thorough validation of system workflows

**System Skills:**
- [ ] Design modular system architectures
- [ ] Implement component communication
- [ ] Manage complex application state
- [ ] Handle system-wide error conditions
- [ ] Create scalable program structures
- [ ] Integrate diverse functionality

---

### Try This (Optional Challenges)

1. **System Extensions**: Add new features to existing systems
2. **Data Persistence**: Implement file-based data storage
3. **Multi-user Support**: Add user authentication and permissions
4. **Performance Optimization**: Optimize for large datasets
5. **System Monitoring**: Add logging and performance metrics

---

## System Design Framework

### Step 1: Requirements Analysis
- [ ] **Features**: What functionality is needed?
- [ ] **Users**: Who will use the system?
- [ ] **Data**: What information needs to be stored?
- [ ] **Workflows**: How will users interact with the system?

### Step 2: Architecture Design
- [ ] **Components**: Break system into logical parts
- [ ] **Interfaces**: How components communicate
- [ ] **Data Structures**: What data formats are needed?
- [ ] **Dependencies**: What components rely on others?

### Step 3: Implementation Strategy
- [ ] **Order**: What to implement first?
- [ ] **Testing**: How to test component interactions?
- [ ] **Integration**: How to combine components?
- [ ] **Deployment**: How to make the system usable?

---

<div style="page-break-after: always;"></div>

---

## SOLUTION APPROACH (Read after attempting!)

### Problem 1: Student Management System

**System Components:**
- [ ] Student Database (names, IDs, courses)
- [ ] Grade Management (per student, per course)
- [ ] Attendance Tracking (dates, status)
- [ ] Report Generation (GPA calculations, attendance %)

**Data Structures:**
```c
struct Student {
    int id;
    char name[50];
    char courses[10][50];
    float grades[10];
    int attendance[365]; // 1 year
    int course_count;
};
```

**Main System Loop:**
```
While running:
    Display menu
    Get choice
    Switch choice:
        Case 1: Register student
        Case 2: Add grades to student
        Case 3: Mark attendance
        Case 4: Generate student report
        Case 5: Search and display student
```

---

### Problem 2: Inventory Management System

**System Components:**
- [ ] Product Catalog (items, prices, stock)
- [ ] Sales Processing (transactions, stock updates)
- [ ] Reporting (sales totals, low stock alerts)
- [ ] Search and Modification (find/update products)

**Key Integration Points:**
- [ ] Sales reduce inventory automatically
- [ ] Low stock triggers alerts
- [ ] Reports pull from transaction history
- [ ] Search works across all product data

---

### Problem 3: Bank Account Management System

**System Components:**
- [ ] Account Management (creation, types)
- [ ] Transaction Processing (deposits, withdrawals, transfers)
- [ ] History Tracking (all transactions)
- [ ] Interest Calculation (savings accounts)
- [ ] Statement Generation (period reports)

**Transaction Flow:**
```
Validate accounts exist
Check sufficient funds
Update balances
Record transaction in history
Update interest calculations
Generate confirmation
```

---

### Problem 4: Hospital Patient Management

**System Components:**
- [ ] Patient Records (personal info, medical history)
- [ ] Appointment System (scheduling, doctors)
- [ ] Treatment Tracking (procedures, medications)
- [ ] Doctor Assignment (availability, specialization)
- [ ] Discharge Processing (final reports)

**Patient Journey:**
```
Registration → Appointment → Doctor Assignment → Treatment → Discharge
     ↓            ↓              ↓                ↓          ↓
   Data Entry   Scheduling    Assignment      Recording   Processing
```

---

### Problem 5: E-commerce Shopping System

**System Components:**
- [ ] Product Catalog (inventory, descriptions)
- [ ] Shopping Cart (user selections, quantities)
- [ ] User Accounts (profiles, order history)
- [ ] Order Processing (checkout, payment simulation)
- [ ] Inventory Integration (stock updates)

**Shopping Workflow:**
```
Browse → Add to Cart → Checkout → Process Order → Update Inventory
   ↓          ↓            ↓           ↓              ↓
Catalog   Cart Mgmt   Payment   Order Creation   Stock Reduction
```

---

### Problem 6: Game Character System

**System Components:**
- [ ] Character Creation (stats, class selection)
- [ ] Inventory System (items, equipment)
- [ ] Progression System (experience, leveling)
- [ ] Quest Management (tracking, rewards)
- [ ] Statistics Display (current status)

**Character Development:**
```
Creation → Questing → Leveling → Equipment → Stats Growth
    ↓         ↓          ↓          ↓          ↓
  Setup    Progress   Rewards   Upgrades   Improvements
```

---

### System Integration Best Practices

**Modular Functions:**
- [ ] Each component in separate functions
- [ ] Clear function interfaces
- [ ] Consistent error handling
- [ ] Reusable utility functions

**Data Management:**
- [ ] Centralized data structures
- [ ] Consistent data validation
- [ ] Backup and recovery considerations
- [ ] Memory management

**User Experience:**
- [ ] Consistent menu systems
- [ ] Clear navigation paths
- [ ] Helpful error messages
- [ ] Progress feedback

**Scalability:**
- [ ] Design for growth
- [ ] Efficient data structures
- [ ] Performance considerations
- [ ] Extensibility hooks

---

 **Congratulations! You've built complete integrated systems!** 

*This completes Stage 3! You're now ready for Stage 4: Full Problem Solving with complete applications! *

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
