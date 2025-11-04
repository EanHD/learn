# Level 4: Interactive Problems

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 3: Problem to Pseudocode

### Today's Mission

**USER INTERACTION MASTER!**  You're now creating interactive programs with menus, user choices, and multi-step workflows. This level focuses on designing user-friendly interfaces and handling complex user interactions.

**The Process:**
1. **Design** the user interface and menu structure
2. **Plan** user workflows and navigation
3. **Handle** user input validation and choices
4. **Create** menu-driven program logic
5. **Write pseudocode** for interactive flow
6. **Test user scenarios** thoroughly
7. **Implement** in C code

---

### Learning Goals

- Design intuitive menu systems
- Handle user input validation
- Create multi-step user workflows
- Implement program loops and navigation
- Provide clear user feedback
- Handle exit conditions gracefully

---

### Interactive Design Framework

**STEP 1: User Experience Design**
- What tasks should the user be able to perform?
- How should the menu be organized?
- What is the user workflow for each feature?
- How to provide clear instructions and feedback?

**STEP 2: Program Structure**
- What is the main menu structure?
- How to handle user choices and navigation?
- What data needs to be maintained between operations?
- How to handle program exit?

**STEP 3: Input Validation**
- What inputs need validation?
- How to handle invalid inputs gracefully?
- What error messages to display?
- How to allow users to retry?

**STEP 4: Interactive Pseudocode**
- Design menu display logic
- Plan input processing loops
- Handle navigation between menus
- Consider user experience flow

---

### Your Task

**For each interactive problem:**
1. **Design** the menu system and user workflow
2. **Plan** input validation and error handling
3. **Write pseudocode** for the interactive program
4. **Test user scenarios** mentally
5. **Implement** in C code
6. **Test thoroughly** with different user paths

---

## Problem 1: Menu-Driven Calculator

**Problem Description:**
Create an interactive calculator program with a menu that allows users to:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

The program should display a menu, get user choice, perform the selected operation, and return to the menu until the user chooses to exit.

**Example:**
```
=== Calculator Menu ===
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter your choice (1-5): 1

Enter first number: 10
Enter second number: 5
Result: 10 + 5 = 15

Press Enter to continue...
```

**Your Task:**
1. Write pseudocode for menu-driven calculator
2. Test all operations and menu navigation
3. Implement in C code

---

## Problem 2: Simple Banking System

**Problem Description:**
Create a banking system menu that allows users to:
1. Check balance
2. Deposit money
3. Withdraw money
4. View transaction history
5. Exit

Maintain a balance and track transactions. Handle insufficient funds for withdrawals.

**Example:**
```
=== Banking Menu ===
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
Enter choice: 2

Enter deposit amount: 100
Deposit successful! New balance: $100.00

Press Enter to continue...
```

**Your Task:**
1. Write pseudocode for banking system
2. Test deposits, withdrawals, and balance checks
3. Implement in C code

---

## Problem 3: Student Grade Manager

**Problem Description:**
Create a student grade management system with menu options:
1. Add student grades
2. View all grades
3. Calculate average
4. Find highest/lowest grade
5. Exit

Store up to 10 student names and grades. Handle cases where no grades are entered.

**Example:**
```
=== Grade Manager ===
1. Add Student Grade
2. View All Grades
3. Calculate Average
4. Find Highest/Lowest
5. Exit
Enter choice: 1

Enter student name: Alice
Enter grade (0-100): 95
Grade added successfully!

Press Enter to continue...
```

**Your Task:**
1. Write pseudocode for grade management
2. Test adding grades and viewing statistics
3. Implement in C code

---

## Problem 4: Restaurant Ordering System

**Problem Description:**
Create a restaurant menu system with:
1. View menu
2. Place order
3. View current order
4. Calculate total
5. Checkout
6. Exit

Include at least 5 menu items with prices. Allow multiple items in one order.

**Example:**
```
=== Restaurant Menu ===
1. View Menu
2. Place Order
3. View Current Order
4. Calculate Total
5. Checkout
6. Exit
Enter choice: 1

=== Our Menu ===
1. Burger - $8.99
2. Pizza - $12.99
3. Salad - $6.99
4. Drink - $2.99
5. Dessert - $4.99

Press Enter to continue...
```

**Your Task:**
1. Write pseudocode for restaurant ordering
2. Test ordering multiple items and checkout
3. Implement in C code

---

## Problem 5: Library Book System

**Problem Description:**
Create a library book management system with:
1. Add book
2. Search books
3. Borrow book
4. Return book
5. View all books
6. Exit

Track book availability and borrower names. Handle cases where books are not available.

**Example:**
```
=== Library System ===
1. Add Book
2. Search Books
3. Borrow Book
4. Return Book
5. View All Books
6. Exit
Enter choice: 1

Enter book title: The C Programming Language
Enter author: Kernighan & Ritchie
Book added successfully!

Press Enter to continue...
```

**Your Task:**
1. Write pseudocode for library system
2. Test adding, borrowing, and returning books
3. Implement in C code

---

## Problem 6: Simple Game Menu

**Problem Description:**
Create a simple game menu system with:
1. Start New Game
2. Load Game
3. View High Scores
4. Settings
5. Exit

Include a number guessing game for "Start New Game". Track high scores and allow basic settings.

**Example:**
```
=== Game Menu ===
1. Start New Game
2. Load Game
3. View High Scores
4. Settings
5. Exit
Enter choice: 1

=== Number Guessing Game ===
I'm thinking of a number between 1-100.
Enter your guess: 50
Too high! Try again: 25
Too low! Try again: 37
Correct! You won in 3 guesses!

Press Enter to continue...
```

**Your Task:**
1. Write pseudocode for game menu system
2. Test game play and menu navigation
3. Implement in C code

---

### Interactive Pseudocode Guidelines

**Menu System Structure:**
```
Algorithm: Menu System
1. Display menu options clearly
2. Get user choice
3. Validate choice is valid
4. Process choice with appropriate action
5. Return to menu or exit based on choice
6. Handle invalid inputs gracefully
```

**Input Validation Loop:**
```
While input is invalid:
    Display prompt
    Get user input
    If input is valid:
        Process input
        Break loop
    Else:
        Display error message
        Continue loop
```

---

### Success Checklist

**For Each Problem:**
- [ ] **Menu Design**: Clear, numbered menu options
- [ ] **Input Validation**: Handle invalid choices gracefully
- [ ] **User Feedback**: Clear messages and confirmations
- [ ] **Navigation**: Easy movement between menu options
- [ ] **Data Persistence**: Maintain state between operations
- [ ] **Exit Handling**: Clean program termination
- [ ] **Error Recovery**: Allow users to retry after errors

**Interactive Skills:**
- [ ] Design intuitive user interfaces
- [ ] Handle complex user workflows
- [ ] Provide helpful error messages
- [ ] Maintain program state
- [ ] Test all user paths thoroughly

---

### Try This (Optional Challenges)

1. **Advanced Menus**: Add sub-menus and navigation breadcrumbs
2. **Input Enhancement**: Add keyboard shortcuts and arrow key navigation
3. **Data Persistence**: Save data to files between program runs
4. **User Experience**: Add loading messages and progress indicators

---

## Interactive Design Framework

### Step 1: User Workflow Analysis
- **Tasks**: What can the user accomplish?
- **Flow**: How does the user navigate the system?
- **Data**: What information needs to be maintained?
- **Feedback**: How to keep the user informed?

### Step 2: Menu Structure Design
- **Main Menu**: Primary options and organization
- **Sub-menus**: Detailed options for complex features
- **Navigation**: How users move between menus
- **Exit Points**: Where users can leave the system

### Step 3: Input Handling
- **Validation**: What constitutes valid input?
- **Error Messages**: Clear, helpful error feedback
- **Retry Logic**: Allow users to correct mistakes
- **Default Values**: Sensible defaults where appropriate

---

<div style="page-break-after: always;"></div>

---

## SOLUTION APPROACH (Read after attempting!)

### Problem 1: Menu-Driven Calculator

**Analysis:**
- Menu with 5 options (4 operations + exit)
- Input validation for menu choice
- Operation-specific input for numbers
- Loop until user chooses exit

**Menu Structure:**
```
While user hasn't chosen exit:
    Display menu
    Get choice
    If choice == 1-4:
        Get two numbers
        Perform operation
        Display result
    Else if choice == 5:
        Exit program
    Else:
        Display invalid choice message
```

---

### Problem 2: Simple Banking System

**Analysis:**
- Maintain balance variable
- Track transactions (could use array or just last operation)
- Validate withdrawal amounts
- Menu-driven with 5 options

**Key Features:**
- Balance starts at $0.00
- Deposit: add to balance
- Withdraw: check sufficient funds, subtract
- History: display last few transactions
- Input validation for amounts

---

### Problem 3: Student Grade Manager

**Analysis:**
- Arrays for names and grades (up to 10)
- Counter for number of students
- Menu with 5 options
- Handle empty list for statistics

**Data Structure:**
- char names[10][50]
- float grades[10]
- int student_count = 0

---

### Problem 4: Restaurant Ordering System

**Analysis:**
- Menu items with prices (use arrays)
- Current order tracking
- Multiple items per order
- Total calculation

**Order Structure:**
- Item IDs array
- Quantities array
- Running total
- Clear order option

---

### Problem 5: Library Book System

**Analysis:**
- Book database (title, author, available, borrower)
- Search functionality
- Borrow/return logic
- Availability checking

**Book Structure:**
- Title and author strings
- Available flag
- Borrower name (when borrowed)

---

### Problem 6: Simple Game Menu

**Analysis:**
- Game menu with 5 options
- Number guessing game implementation
- High score tracking
- Basic settings (difficulty?)

**Game Logic:**
- Random number generation
- Guess counter
- Win/lose conditions
- Score calculation

---

### Interactive Programming Best Practices

**User Experience:**
- Clear, numbered menus
- Consistent formatting
- Helpful prompts and messages
- Graceful error handling

**Program Structure:**
- Main menu loop
- Modular functions for each feature
- Clear variable naming
- Comments explaining complex logic

**Input Handling:**
- Validate all user inputs
- Provide clear error messages
- Allow users to retry
- Handle unexpected inputs

---

 **Congratulations! You've created interactive user interfaces!** 

*Next: Decision-based problems with rule engines and eligibility systems! *