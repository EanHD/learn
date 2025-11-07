# Level 2: Variables in Pseudocode

> **LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.c\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Variables are the memory of your programs! Today you'll learn how to use variables effectively in pseudocode and translate that understanding into C code. You'll see how variables change, store information, and control program flow.

---

### Learning Goals

- [ ] Understand how variables work in algorithmic thinking
- [ ] Learn different types of variables (counters, accumulators, flags)
- [ ] Practice tracking variable changes through algorithms
- [ ] Master variable initialization and assignment
- [ ] Create programs that use variables effectively

---

### Variable Types in Programming

**Variables** are like containers that hold information. In pseudocode, we think about:

1. **Data Variables**: Store user input or calculated results
2. **Counter Variables**: Keep track of how many times something happens
3. **Accumulator Variables**: Add up values (like running totals)
4. **Flag Variables**: Store true/false conditions
5. **Temporary Variables**: Hold intermediate calculations

---

### Your Task

**Translate each pseudocode algorithm into C code, paying special attention to how variables are used, initialized, and changed.**

---

## Algorithm 1: Shopping Cart Total

**Pseudocode:**
```
Algorithm: Calculate Shopping Total
1. Initialize total to 0
2. Initialize item_count to 0
3. Display "Enter price of item 1 (or 0 to finish): "
4. Get price from user
5. While price is not 0:
   a. Add price to total
   b. Add 1 to item_count
   c. Display "Enter price of item " + (item_count + 1) + " (or 0 to finish): "
   d. Get next price from user
6. Display "Items purchased: " + item_count
7. Display "Total cost: $" + total
```

**Variable Analysis:**
- [ ] `total`: Accumulator (starts at 0, adds prices)
- [ ] `item_count`: Counter (starts at 0, counts items)
- [ ] `price`: Temporary (holds each item's price)

**Your Task:** Implement this shopping cart calculator.

---

## Algorithm 2: Password Validation

**Pseudocode:**
```
Algorithm: Validate Password
1. Initialize attempts to 0
2. Initialize is_valid to false
3. Set correct_password to "secret123"
4. While attempts < 3 AND is_valid is false:
   a. Add 1 to attempts
   b. Display "Enter password (attempt " + attempts + "/3): "
   c. Get user_input from user
   d. If user_input equals correct_password:
      i. Set is_valid to true
5. If is_valid is true:
   a. Display "Access granted! "
6. Else:
   a. Display "Access denied! "
```

**Variable Analysis:**
- [ ] `attempts`: Counter (tracks login attempts)
- [ ] `is_valid`: Flag (true/false status)
- [ ] `correct_password`: Constant (fixed value)
- [ ] `user_input`: Temporary (holds user entry)

**Your Task:** Create a password validation system.

---

## Algorithm 3: Grade Average Calculator

**Pseudocode:**
```
Algorithm: Calculate Class Average
1. Initialize total_score to 0
2. Initialize student_count to 0
3. Initialize has_more_students to true
4. While has_more_students is true:
   a. Display "Enter score for student " + (student_count + 1) + " (or -1 to finish): "
   b. Get score from user
   c. If score equals -1:
      i. Set has_more_students to false
   d. Else:
      i. Add score to total_score
      ii. Add 1 to student_count
5. If student_count > 0:
   a. Calculate average = total_score ÷ student_count
   b. Display "Class average: " + average + "%"
   c. Display "Total students: " + student_count
6. Else:
   a. Display "No students entered"
```

**Variable Analysis:**
- [ ] `total_score`: Accumulator (sums all grades)
- [ ] `student_count`: Counter (counts students)
- [ ] `has_more_students`: Flag (controls loop continuation)
- [ ] `score`: Temporary (each student's grade)
- [ ] `average`: Calculated result

**Your Task:** Build a class grade averaging system.

---

## Algorithm 4: Number Guessing Game

**Pseudocode:**
```
Algorithm: Number Guessing Game
1. Initialize secret_number to 42
2. Initialize guess_count to 0
3. Initialize game_won to false
4. Display "I'm thinking of a number between 1-100!"
5. While game_won is false:
   a. Add 1 to guess_count
   b. Display "Guess #" + guess_count + ": "
   c. Get user_guess from user
   d. If user_guess equals secret_number:
      i. Set game_won to true
      ii. Display "Correct! You won in " + guess_count + " guesses! "
   e. Else:
      i. If user_guess > secret_number:
         i. Display "Too high! Try lower."
      ii. Else:
         i. Display "Too low! Try higher."
6. Display "Thanks for playing!"
```

**Variable Analysis:**
- [ ] `secret_number`: Constant (game target)
- [ ] `guess_count`: Counter (attempts made)
- [ ] `game_won`: Flag (win condition)
- [ ] `user_guess`: Temporary (each guess)

**Your Task:** Create an interactive guessing game.

---

## Algorithm 5: Bank Account Simulator

**Pseudocode:**
```
Algorithm: Bank Account Manager
1. Initialize balance to 1000.00
2. Initialize transaction_count to 0
3. Initialize is_running to true
4. Display "Welcome to Bank Account Manager"
5. Display "Initial balance: $" + balance
6. While is_running is true:
   a. Display menu options
   b. Get user_choice from user
   c. If user_choice is 1 (deposit):
      i. Display "Enter deposit amount: $"
      ii. Get amount from user
      iii. Add amount to balance
      iv. Add 1 to transaction_count
      v. Display "Deposit successful. New balance: $" + balance
   d. Else if user_choice is 2 (withdraw):
      i. Display "Enter withdrawal amount: $"
      ii. Get amount from user
      iii. If amount <= balance:
         i. Subtract amount from balance
         ii. Add 1 to transaction_count
         iii. Display "Withdrawal successful. New balance: $" + balance
      iv. Else:
         i. Display "Insufficient funds!"
   e. Else if user_choice is 3 (check balance):
      i. Display "Current balance: $" + balance
      ii. Display "Transactions today: " + transaction_count
   f. Else if user_choice is 4 (exit):
      i. Set is_running to false
   g. Else:
      i. Display "Invalid choice!"
7. Display "Thank you for banking with us!"
```

**Variable Analysis:**
- [ ] `balance`: Accumulator (changes with deposits/withdrawals)
- [ ] `transaction_count`: Counter (number of operations)
- [ ] `is_running`: Flag (program continuation)
- [ ] `user_choice`: Temporary (menu selection)
- [ ] `amount`: Temporary (transaction amount)

**Your Task:** Build a bank account management system.

---

## Algorithm 6: Temperature Tracker

**Pseudocode:**
```
Algorithm: Daily Temperature Tracker
1. Initialize day_count to 0
2. Initialize total_temperature to 0
3. Initialize highest_temp to -1000
4. Initialize lowest_temp to 1000
5. Initialize reading_count to 0
6. Display "Daily Temperature Tracker"
7. While reading_count < 24:
   a. Add 1 to reading_count
   b. Display "Enter temperature reading #" + reading_count + " (°F): "
   c. Get temperature from user
   d. Add temperature to total_temperature
   e. If temperature > highest_temp:
      i. Set highest_temp to temperature
   f. If temperature < lowest_temp:
      i. Set lowest_temp to temperature
8. Calculate average_temp = total_temperature ÷ 24
9. Display "Temperature Summary:"
10. Display "Average: " + average_temp + "°F"
11. Display "Highest: " + highest_temp + "°F"
12. Display "Lowest: " + lowest_temp + "°F"
13. Display "Readings taken: " + reading_count
```

**Variable Analysis:**
- [ ] `total_temperature`: Accumulator (sum of all readings)
- [ ] `highest_temp`: Tracker (maximum value seen)
- [ ] `lowest_temp`: Tracker (minimum value seen)
- [ ] `reading_count`: Counter (number of readings)
- [ ] `average_temp`: Calculated result

**Your Task:** Create a temperature tracking system.

---

### Variable Tracking Techniques

**For each algorithm, track how variables change:**

**Example for Algorithm 1:**
```
Initial state:
total = 0, item_count = 0

User enters: 10.50
After processing:
total = 10.50, item_count = 1

User enters: 5.25
After processing:
total = 15.75, item_count = 2

User enters: 0 (finish)
Final state:
total = 15.75, item_count = 2
```

---

### Success Checklist

**For Each Algorithm:**
- [ ] Identified all variables and their purposes
- [ ] Initialized variables with correct starting values
- [ ] Used appropriate data types (int, float, char[])
- [ ] Updated variables correctly throughout the program
- [ ] Handled edge cases (division by zero, invalid inputs)

**Variable Usage:**
- [ ] Used counters for counting operations
- [ ] Used accumulators for running totals
- [ ] Used flags for true/false conditions
- [ ] Used temporary variables for intermediate values

---

### Try This (Optional Challenges)

1. **Add Input Validation**: Check for negative prices, invalid menu choices
2. **Enhanced Features**: Add transaction history, daily limits
3. **Multiple Users**: Support multiple bank accounts
4. **Data Persistence**: Save/load account data (advanced)

---

## Variable Patterns in Pseudocode

### Counter Variables
```
Initialize counter to 0
While condition:
    Add 1 to counter
    // do something
Display "Count: " + counter
```

### Accumulator Variables
```
Initialize total to 0
While getting values:
    Get value from user
    Add value to total
Display "Total: " + total
```

### Flag Variables
```
Initialize is_valid to false
// check conditions
If condition met:
    Set is_valid to true
If is_valid:
    Display "Success"
Else:
    Display "Failed"
```

### Tracker Variables
```
Initialize maximum to smallest possible value
Initialize minimum to largest possible value
For each value:
    If value > maximum: set maximum to value
    If value < minimum: set minimum to value
```

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Shopping Cart Total

```c
#include <stdio.h>

int main() {
    float total = 0.0;
    int item_count = 0;
    float price;
    
    printf("Enter price of item 1 (or 0 to finish): ");
    scanf("%f", &price);
    
    while (price != 0) {
        total = total + price;
        item_count = item_count + 1;
        
        printf("Enter price of item %d (or 0 to finish): ", item_count + 1);
        scanf("%f", &price);
    }
    
    printf("Items purchased: %d\n", item_count);
    printf("Total cost: $%.2f\n", total);
    
    return 0;
}
```

**Variable Flow:**
- [ ] `total`: Starts at 0, accumulates prices
- [ ] `item_count`: Starts at 0, increments for each item
- [ ] `price`: Temporary variable for each input

---

### Algorithm 2: Password Validation

```c
#include <stdio.h>
# include <string.h>

int main() {
    int attempts = 0;
    int is_valid = 0;  // 0 = false, 1 = true
    char correct_password[] = "secret123";
    char user_input[50];
    
    while (attempts < 3 && is_valid == 0) {
        attempts = attempts + 1;
        
        printf("Enter password (attempt %d/3): ", attempts);
        scanf("%s", user_input);
        
        if (strcmp(user_input, correct_password) == 0) {
            is_valid = 1;
        }
    }
    
    if (is_valid == 1) {
        printf("Access granted! \n");
    } else {
        printf("Access denied! \n");
    }
    
    return 0;
}
```

**Key Concepts:**
- [ ] String comparison with `strcmp()`
- [ ] Boolean logic with integers (0/1)
- [ ] Loop control with multiple conditions

---

### Algorithm 3: Grade Average Calculator

```c
#include <stdio.h>

int main() {
    float total_score = 0.0;
    int student_count = 0;
    int has_more_students = 1;  // 1 = true, 0 = false
    float score;
    
    while (has_more_students == 1) {
        printf("Enter score for student %d (or -1 to finish): ", student_count + 1);
        scanf("%f", &score);
        
        if (score == -1) {
            has_more_students = 0;
        } else {
            total_score = total_score + score;
            student_count = student_count + 1;
        }
    }
    
    if (student_count > 0) {
        float average = total_score / student_count;
        printf("Class average: %.1f%%\n", average);
        printf("Total students: %d\n", student_count);
    } else {
        printf("No students entered\n");
    }
    
    return 0;
}
```

**Variable Management:**
- [ ] `total_score`: Accumulates all grades
- [ ] `student_count`: Counts valid entries
- [ ] `has_more_students`: Controls loop execution

---

### Algorithm 4: Number Guessing Game

```c
#include <stdio.h>

int main() {
    int secret_number = 42;
    int guess_count = 0;
    int game_won = 0;  // 0 = false, 1 = true
    int user_guess;
    
    printf("I'm thinking of a number between 1-100!\n");
    
    while (game_won == 0) {
        guess_count = guess_count + 1;
        
        printf("Guess #%d: ", guess_count);
        scanf("%d", &user_guess);
        
        if (user_guess == secret_number) {
            game_won = 1;
            printf("Correct! You won in %d guesses! \n", guess_count);
        } else {
            if (user_guess > secret_number) {
                printf("Too high! Try lower.\n");
            } else {
                printf("Too low! Try higher.\n");
            }
        }
    }
    
    printf("Thanks for playing!\n");
    
    return 0;
}
```

**Game Logic:**
- [ ] `game_won` flag controls the game loop
- [ ] `guess_count` tracks attempts
- [ ] Conditional feedback based on guess comparison

---

### Algorithm 5: Bank Account Simulator

```c
#include <stdio.h>

int main() {
    float balance = 1000.00;
    int transaction_count = 0;
    int is_running = 1;  // 1 = true, 0 = false
    int user_choice;
    float amount;
    
    printf("Welcome to Bank Account Manager\n");
    printf("Initial balance: $%.2f\n", balance);
    
    while (is_running == 1) {
        printf("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &user_choice);
        
        if (user_choice == 1) {
            printf("Enter deposit amount: $");
            scanf("%f", &amount);
            balance = balance + amount;
            transaction_count = transaction_count + 1;
            printf("Deposit successful. New balance: $%.2f\n", balance);
        } else if (user_choice == 2) {
            printf("Enter withdrawal amount: $");
            scanf("%f", &amount);
            if (amount <= balance) {
                balance = balance - amount;
                transaction_count = transaction_count + 1;
                printf("Withdrawal successful. New balance: $%.2f\n", balance);
            } else {
                printf("Insufficient funds!\n");
            }
        } else if (user_choice == 3) {
            printf("Current balance: $%.2f\n", balance);
            printf("Transactions today: %d\n", transaction_count);
        } else if (user_choice == 4) {
            is_running = 0;
        } else {
            printf("Invalid choice!\n");
        }
    }
    
    printf("Thank you for banking with us!\n");
    
    return 0;
}
```

**Complex Variable Management:**
- [ ] `balance`: Changes with deposits/withdrawals
- [ ] `transaction_count`: Increments on successful operations
- [ ] `is_running`: Controls main program loop

---

### Algorithm 6: Temperature Tracker

```c
#include <stdio.h>

int main() {
    int day_count = 0;  // Not used in this version, but could be for multiple days
    float total_temperature = 0.0;
    float highest_temp = -1000.0;
    float lowest_temp = 1000.0;
    int reading_count = 0;
    float temperature;
    
    printf("Daily Temperature Tracker\n");
    
    while (reading_count < 24) {
        reading_count = reading_count + 1;
        
        printf("Enter temperature reading #%d (°F): ", reading_count);
        scanf("%f", &temperature);
        
        total_temperature = total_temperature + temperature;
        
        if (temperature > highest_temp) {
            highest_temp = temperature;
        }
        
        if (temperature < lowest_temp) {
            lowest_temp = temperature;
        }
    }
    
    float average_temp = total_temperature / 24;
    
    printf("\nTemperature Summary:\n");
    printf("Average: %.1f°F\n", average_temp);
    printf("Highest: %.1f°F\n", highest_temp);
    printf("Lowest: %.1f°F\n", lowest_temp);
    printf("Readings taken: %d\n", reading_count);
    
    return 0;
}
```

**Statistical Tracking:**
- [ ] `highest_temp`: Tracks maximum value (initialized to very low)
- [ ] `lowest_temp`: Tracks minimum value (initialized to very high)
- [ ] `total_temperature`: Accumulates all readings for average

---

### Variable Initialization Best Practices

**Counters:** Always start at 0
```c
int count = 0;
```

**Accumulators:** Usually start at 0
```c
float total = 0.0;
```

**Flags:** Initialize to false/0
```c
int is_done = 0;
```

**Maximum Trackers:** Initialize to minimum possible value
```c
int max_value = INT_MIN;  // or a very small number
```

**Minimum Trackers:** Initialize to maximum possible value
```c
int min_value = INT_MAX;  // or a very large number
```

### Common Variable Mistakes

**Forgetting Initialization:**
```c
int sum;  // Uninitialized - contains garbage value
sum = sum + 5;  // Undefined behavior!
```

**Wrong Data Types:**
```c
int average;  // Wrong! Should be float for decimals
average = 85.5;  // Gets truncated to 85
```

**Scope Issues:**
```c
if (condition) {
    int temp = 5;  // Only exists in this block
}
// temp is undefined here!
```

---

 **Excellent! You now understand how variables work in algorithms and code!** 

*Variables are the foundation of programming logic. Next: Mathematical operations in pseudocode! *

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


<div style="page-break-after: always;"></div>

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
