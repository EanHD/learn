# Level 4: Interactive Problems

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 3: Problem to Pseudocode

### Today's Mission

Interactive problems require handling multiple user inputs and decisions. You'll design a solution for a problem that involves ongoing user interaction.

---

### Learning Goals

- Design multi-step user interaction flows
- Handle conditional logic based on user choices
- Manage program state through multiple interactions
- Create intuitive user experience patterns

---

### Your Task

**Read the problem below, then write pseudocode to solve it. Create a file called `interactive_problems.md` with your pseudocode solution.**


### How to Run

1. **Compile the code**:
   ```
   rustc hello.rs -o hello hello.rs
   ```

2. **Run your program**:
   ```
   ./hello hello
   ```

**Expected output:**
```
Hello, World!
```

### Problem: Simple Banking System

**Description:**
Create a simple banking system that allows users to perform basic banking operations. The program should:

1. Start with an initial balance of $1000
2. Display a menu of operations:
   - Check balance
   - Deposit money
   - Withdraw money
   - Exit
3. Process user selections until they choose to exit
4. Validate withdrawals (cannot withdraw more than balance)
5. Display transaction confirmations
6. Show updated balance after each transaction

**Menu Options:**
```
Simple Bank System
==================
Current Balance: $1000.00

Choose an option:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice (1-4):
```

**Example Interaction:**
```
Simple Bank System
==================
Current Balance: $1000.00

Choose an option:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice (1-4): 2
Enter deposit amount: $500

Deposit successful! New balance: $1500.00

Choose an option:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice (1-4): 3
Enter withdrawal amount: $200

Withdrawal successful! New balance: $1300.00

Choose an option:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit

Enter your choice (1-4): 4

Thank you for using Simple Bank System!
```

---

### How to Create Your Solution

1. **Navigate to your working directory**:
   ```
   cd /path/to/your/folder
   ```
2. **Create your pseudocode file**:
   ```
   touch interactive_problems.md
   ```
3. **Plan the main loop** - Program runs until user exits
4. **Design menu system** - Clear options for user
5. **Handle each operation** - Different logic for each choice

---

### Success Checklist

- [ ] Created `interactive_problems.md` file
- [ ] Designed main program loop with exit condition
- [ ] Planned menu display and user choice handling
- [ ] Created deposit logic with balance updates
- [ ] Created withdrawal logic with validation
- [ ] Planned clear transaction feedback

---

### What Did You Learn?

Interactive problem analysis involves:
- **Loop control** - When to continue vs exit
- **State management** - Tracking balance changes
- **Input validation** - Ensuring valid operations
- **User feedback** - Clear communication of results

---

### Try This (Optional Challenges)

1. Add transaction history display
2. Implement transfer between accounts
3. Add minimum balance requirements

---

## Need Help with Vim?

Check the `VIM_CHEATSHEET.md` for editing commands!

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Problem Analysis

**Interactive Components:**
- **Menu System**: Repeated display of options
- **User Choice**: Input validation for menu selection
- **Transaction Processing**: Different logic per operation
- **State Persistence**: Balance maintained across operations
- **Exit Condition**: Clean program termination

**Program Flow:**
```
Initialize balance
WHILE user hasn't chosen exit:
    Display menu with current balance
    Get user choice
    Process choice (check/deposit/withdraw)
    Update balance if needed
    Show confirmation
END WHILE
Display exit message
```

### Sample Pseudocode Solution

```
START PROGRAM
    SET balance TO 1000.00

    SET running TO true
    WHILE running == true DO
        // Display menu
        DISPLAY "Simple Bank System"
        DISPLAY "=================="
        DISPLAY "Current Balance: $" + balance
        DISPLAY ""
        DISPLAY "Choose an option:"
        DISPLAY "1. Check Balance"
        DISPLAY "2. Deposit Money"
        DISPLAY "3. Withdraw Money"
        DISPLAY "4. Exit"
        DISPLAY ""
        DISPLAY "Enter your choice (1-4):"
        READ choice AS NUMBER

        // Process choice
        IF choice == 1 THEN
            // Check balance
            DISPLAY "Your current balance is: $" + balance
            DISPLAY ""

        ELSE IF choice == 2 THEN
            // Deposit
            DISPLAY "Enter deposit amount:"
            READ deposit_amount AS NUMBER

            IF deposit_amount > 0 THEN
                SET balance TO balance + deposit_amount
                DISPLAY "Deposit successful! New balance: $" + balance
            ELSE
                DISPLAY "Invalid deposit amount. Please enter a positive number."
            END IF
            DISPLAY ""

        ELSE IF choice == 3 THEN
            // Withdraw
            DISPLAY "Enter withdrawal amount:"
            READ withdrawal_amount AS NUMBER

            IF withdrawal_amount > 0 AND withdrawal_amount <= balance THEN
                SET balance TO balance - withdrawal_amount
                DISPLAY "Withdrawal successful! New balance: $" + balance
            ELSE IF withdrawal_amount <= 0 THEN
                DISPLAY "Invalid withdrawal amount. Please enter a positive number."
            ELSE
                DISPLAY "Insufficient funds. Your balance is $" + balance
            END IF
            DISPLAY ""

        ELSE IF choice == 4 THEN
            // Exit
            SET running TO false
            DISPLAY "Thank you for using Simple Bank System!"

        ELSE
            // Invalid choice
            DISPLAY "Invalid choice. Please select 1-4."
            DISPLAY ""
        END IF
    END WHILE
END PROGRAM
```

### Analysis Breakdown

**Interactive Logic:**
- **Loop Structure**: While loop continues until exit chosen
- **Menu Display**: Clear options with current balance
- **Choice Processing**: IF-ELSE chain for different operations
- **Validation**: Positive amounts and sufficient funds
- **Feedback**: Clear success/error messages

**Why this approach?**
- **State Management**: Balance persists across transactions
- **Input Validation**: Prevents invalid operations
- **User Experience**: Clear menu and feedback
- **Error Handling**: Graceful handling of invalid inputs

**Potential improvements:**
- Input validation for non-numeric entries
- Transaction limits and fees
- Account number system
- Transaction history storage

### Common Analysis Mistakes

| Common Issue | Why It Happens | Solution |
|--------------|----------------|----------|
| No loop exit | Program runs forever | Include exit condition in loop |
| Balance not updated | Forgetting to modify variable | Use assignment operators (+=, -=) |
| No validation | Invalid transactions allowed | Check conditions before processing |
| Poor feedback | User confused about results | Display clear success/error messages |

### Bonus Knowledge

- **Event-Driven Programming**: Responding to user actions
- **State Machines**: Managing program states
- **Input Sanitization**: Validating user data
- **UX Design**: Creating intuitive interfaces

---

 **Great! You designed an interactive banking system!**

*Next: Decision-Based Problems!*


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic
