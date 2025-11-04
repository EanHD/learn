# Level 2: Variables in Pseudocode

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`Main.java` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Variables are the memory of your programs! Today you'll learn how to use variables effectively in pseudocode and translate that understanding into Java code. You'll see how variables change, store information, and control program flow.

---

### Learning Goals

- Understand how variables work in algorithmic thinking
- Learn different types of variables (counters, accumulators, flags)
- Practice tracking variable changes through algorithms
- Master variable initialization and assignment
- Create programs that use variables effectively

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

**Translate each pseudocode algorithm into Java code, paying special attention to how variables are used, initialized, and changed.**

---


### How to Compile and Run

1. **Compile the code**:
   ```bash
   javac hello.java
   ```

2. **Run your program**:
   ```bash
   java hello
   ```

**Expected output:**
```
Hello, World!
```

## Algorithm 1: Shopping Cart Total

**Pseudocode:**
```java
Algorithm: Calculate Shopping Total
1. Initialize total to 0
2. Initialize itemCount to 0
3. Display "Enter price of item 1 (or 0 to finish): "
4. Get price from user
5. While price is not 0:
   a. Add price to total
   b. Add 1 to itemCount
   c. Display "Enter price of item " + (itemCount + 1) + " (or 0 to finish): "
   d. Get next price from user
6. Display "Items purchased: " + itemCount
7. Display "Total cost: $" + total
```

**Variable Analysis:**
- `total`: Accumulator (starts at 0, adds prices)
- `itemCount`: Counter (starts at 0, counts items)
- `price`: Temporary (holds each item's price)

**Your Task:** Implement this shopping cart calculator.

---

## Algorithm 2: Password Validation

**Pseudocode:**
```java
Algorithm: Validate Password
1. Initialize attempts to 0
2. Initialize isValid to false
3. Set correctPassword to "secret123"
4. While attempts < 3 AND isValid is false:
   a. Add 1 to attempts
   b. Display "Enter password (attempt " + attempts + "/3): "
   c. Get userInput from user
   d. If userInput equals correctPassword:
      i. Set isValid to true
5. If isValid is true:
   a. Display "Access granted! "
6. Else:
   a. Display "Access denied! "
```

**Variable Analysis:**
- `attempts`: Counter (tracks login attempts)
- `isValid`: Flag (true/false status)
- `correctPassword`: Constant (fixed value)
- `userInput`: Temporary (holds user entry)

**Your Task:** Create a password validation system.

---

## Algorithm 3: Grade Average Calculator

**Pseudocode:**
```java
Algorithm: Calculate Class Average
1. Initialize totalScore to 0
2. Initialize studentCount to 0
3. Initialize hasMoreStudents to true
4. While hasMoreStudents is true:
   a. Display "Enter score for student " + (studentCount + 1) + " (or -1 to finish): "
   b. Get score from user
   c. If score equals -1:
      i. Set hasMoreStudents to false
   d. Else:
      i. Add score to totalScore
      ii. Add 1 to studentCount
5. If studentCount > 0:
   a. Calculate average = totalScore ÷ studentCount
   b. Display "Class average: " + average + "%"
   c. Display "Total students: " + studentCount
6. Else:
   a. Display "No students entered"
```

**Variable Analysis:**
- `totalScore`: Accumulator (sums all grades)
- `studentCount`: Counter (counts students)
- `hasMoreStudents`: Flag (controls loop continuation)
- `score`: Temporary (each student's grade)
- `average`: Calculated result

**Your Task:** Build a class grade averaging system.

---

## Algorithm 4: Number Guessing Game

**Pseudocode:**
```java
Algorithm: Number Guessing Game
1. Initialize secretNumber to 42
2. Initialize guessCount to 0
3. Initialize gameWon to false
4. Display "I'm thinking of a number between 1-100!"
5. While gameWon is false:
   a. Add 1 to guessCount
   b. Display "Guess #" + guessCount + ": "
   c. Get userGuess from user
   d. If userGuess equals secretNumber:
      i. Set gameWon to true
      ii. Display "Correct! You won in " + guessCount + " guesses! "
   e. Else:
      i. If userGuess > secretNumber:
         i. Display "Too high! Try lower."
      ii. Else:
         i. Display "Too low! Try higher."
6. Display "Thanks for playing!"
```

**Variable Analysis:**
- `secretNumber`: Constant (game target)
- `guessCount`: Counter (attempts made)
- `gameWon`: Flag (win condition)
- `userGuess`: Temporary (each guess)

**Your Task:** Create an interactive guessing game.

---

## Algorithm 5: Bank Account Simulator

**Pseudocode:**
```java
Algorithm: Bank Account Manager
1. Initialize balance to 1000.00
2. Initialize transactionCount to 0
3. Initialize isRunning to true
4. Display "Welcome to Bank Account Manager"
5. Display "Initial balance: $" + balance
6. While isRunning is true:
   a. Display menu options
   b. Get userChoice from user
   c. If userChoice is 1 (deposit):
      i. Display "Enter deposit amount: $"
      ii. Get amount from user
      iii. Add amount to balance
      iv. Add 1 to transactionCount
      v. Display "Deposit successful. New balance: $" + balance
   d. Else if userChoice is 2 (withdraw):
      i. Display "Enter withdrawal amount: $"
      ii. Get amount from user
      iii. If amount <= balance:
         i. Subtract amount from balance
         ii. Add 1 to transactionCount
         iii. Display "Withdrawal successful. New balance: $" + balance
      iv. Else:
         i. Display "Insufficient funds!"
   e. Else if userChoice is 3 (check balance):
      i. Display "Current balance: $" + balance
      ii. Display "Transactions today: " + transactionCount
   f. Else if userChoice is 4 (exit):
      i. Set isRunning to false
   g. Else:
      i. Display "Invalid choice!"
7. Display "Thank you for banking with us!"
```

**Variable Analysis:**
- `balance`: Accumulator (changes with deposits/withdrawals)
- `transactionCount`: Counter (number of operations)
- `isRunning`: Flag (program continuation)
- `userChoice`: Temporary (menu selection)
- `amount`: Temporary (transaction amount)

**Your Task:** Build a bank account management system.

---

## Algorithm 6: Temperature Tracker

**Pseudocode:**
```java
Algorithm: Daily Temperature Tracker
1. Initialize dayCount to 0
2. Initialize totalTemperature to 0
3. Initialize highestTemp to -1000
4. Initialize lowestTemp to 1000
5. Initialize readingCount to 0
6. Display "Daily Temperature Tracker"
7. While readingCount < 24:
   a. Add 1 to readingCount
   b. Display "Enter temperature reading #" + readingCount + " (°F): "
   c. Get temperature from user
   d. Add temperature to totalTemperature
   e. If temperature > highestTemp:
      i. Set highestTemp to temperature
   f. If temperature < lowestTemp:
      i. Set lowestTemp to temperature
8. Calculate averageTemp = totalTemperature ÷ 24
9. Display "Temperature Summary:"
10. Display "Average: " + averageTemp + "°F"
11. Display "Highest: " + highestTemp + "°F"
12. Display "Lowest: " + lowestTemp + "°F"
13. Display "Readings taken: " + readingCount
```

**Variable Analysis:**
- `totalTemperature`: Accumulator (sum of all readings)
- `highestTemp`: Tracker (maximum value seen)
- `lowestTemp`: Tracker (minimum value seen)
- `readingCount`: Counter (number of readings)
- `averageTemp`: Calculated result

**Your Task:** Create a temperature tracking system.

---

### Variable Tracking Techniques

**For each algorithm, track how variables change:**

**Example for Algorithm 1:**
```java
Initial state:
total = 0, itemCount = 0

User enters: 10.50
After processing:
total = 10.50, itemCount = 1

User enters: 5.25
After processing:
total = 15.75, itemCount = 2

User enters: 0 (finish)
Final state:
total = 15.75, itemCount = 2
```

---

### Success Checklist

**For Each Algorithm:**
- [ ] Identified all variables and their purposes
- [ ] Initialized variables with correct starting values
- [ ] Used appropriate data types (int, double, boolean, String)
- [ ] Updated variables correctly throughout the program
- [ ] Handled edge cases (division by zero, invalid inputs)

**Variable Usage:**
- [ ] Used counters for counting operations
- [ ] Used accumulators for running totals
- [ ] Used flags (boolean) for true/false conditions
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
```java
Initialize counter to 0
While condition:
    Add 1 to counter
    // do something
Display "Count: " + counter
```

### Accumulator Variables
```java
Initialize total to 0
While getting values:
    Get value from user
    Add value to total
Display "Total: " + total
```

### Flag Variables
```java
Initialize isValid to false
// check conditions
If condition met:
    Set isValid to true
If isValid:
    Display "Success"
Else:
    Display "Failed"
```

### Tracker Variables
```java
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

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        double total = 0.0;
        int itemCount = 0;
        
        System.out.print("Enter price of item 1 (or 0 to finish): ");
        double price = scanner.nextDouble();
        
        while (price != 0) {
            total = total + price;
            itemCount = itemCount + 1;
            
            System.out.print("Enter price of item " + (itemCount + 1) + " (or 0 to finish): ");
            price = scanner.nextDouble();
        }
        
        System.out.println("Items purchased: " + itemCount);
        System.out.printf("Total cost: $%.2f\n", total);
        
        scanner.close();
    }
}
```

**Variable Flow:**
- `total`: Starts at 0, accumulates prices
- `itemCount`: Starts at 0, increments for each item
- `price`: Temporary variable for each input

**Java Notes:**
- Use `double` for currency (more precision than float)
- `printf` with `%.2f` formats to 2 decimal places
- Remember to close Scanner!

---

### Algorithm 2: Password Validation

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int attempts = 0;
        boolean isValid = false;
        String correctPassword = "secret123";
        
        while (attempts < 3 && !isValid) {
            attempts = attempts + 1;
            
            System.out.print("Enter password (attempt " + attempts + "/3): ");
            String userInput = scanner.nextLine();
            
            if (userInput.equals(correctPassword)) {
                isValid = true;
            }
        }
        
        if (isValid) {
            System.out.println("Access granted! ");
        } else {
            System.out.println("Access denied! ");
        }
        
        scanner.close();
    }
}
```

**Key Concepts:**
- String comparison with `.equals()` (NOT ==!)
- Boolean type in Java (true/false)
- Loop control with multiple conditions (`&&`)

**Common Java Mistakes:**
- Using `==` for strings (compares references, not content)
- Forgetting to use `!isValid` for "not valid"

---

### Algorithm 3: Grade Average Calculator

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        double totalScore = 0.0;
        int studentCount = 0;
        boolean hasMoreStudents = true;
        
        while (hasMoreStudents) {
            System.out.print("Enter score for student " + (studentCount + 1) + " (or -1 to finish): ");
            double score = scanner.nextDouble();
            
            if (score == -1) {
                hasMoreStudents = false;
            } else {
                totalScore = totalScore + score;
                studentCount = studentCount + 1;
            }
        }
        
        if (studentCount > 0) {
            double average = totalScore / studentCount;
            System.out.printf("Class average: %.1f%%\n", average);
            System.out.println("Total students: " + studentCount);
        } else {
            System.out.println("No students entered");
        }
        
        scanner.close();
    }
}
```

**Variable Management:**
- `totalScore`: Accumulates all grades
- `studentCount`: Counts valid entries
- `hasMoreStudents`: Controls loop execution

**Java Specifics:**
- Use `%%` in printf to display literal % symbol
- Division of doubles gives decimal result automatically

---

### Algorithm 4: Number Guessing Game

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int secretNumber = 42;
        int guessCount = 0;
        boolean gameWon = false;
        
        System.out.println("I'm thinking of a number between 1-100!");
        
        while (!gameWon) {
            guessCount = guessCount + 1;
            
            System.out.print("Guess #" + guessCount + ": ");
            int userGuess = scanner.nextInt();
            
            if (userGuess == secretNumber) {
                gameWon = true;
                System.out.println("Correct! You won in " + guessCount + " guesses! ");
            } else {
                if (userGuess > secretNumber) {
                    System.out.println("Too high! Try lower.");
                } else {
                    System.out.println("Too low! Try higher.");
                }
            }
        }
        
        System.out.println("Thanks for playing!");
        
        scanner.close();
    }
}
```

**Game Logic:**
- `gameWon` flag controls the game loop
- `guessCount` tracks attempts
- Conditional feedback based on guess comparison

**Enhancement Ideas:**
- Use `Math.random()` for random secret number
- Limit maximum number of guesses
- Add difficulty levels

---

### Algorithm 5: Bank Account Simulator

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        double balance = 1000.00;
        int transactionCount = 0;
        boolean isRunning = true;
        
        System.out.println("Welcome to Bank Account Manager");
        System.out.printf("Initial balance: $%.2f\n", balance);
        
        while (isRunning) {
            System.out.println("\n1. Deposit");
            System.out.println("2. Withdraw");
            System.out.println("3. Check Balance");
            System.out.println("4. Exit");
            System.out.print("Enter choice: ");
            int userChoice = scanner.nextInt();
            
            if (userChoice == 1) {
                System.out.print("Enter deposit amount: $");
                double amount = scanner.nextDouble();
                balance = balance + amount;
                transactionCount = transactionCount + 1;
                System.out.printf("Deposit successful. New balance: $%.2f\n", balance);
            } else if (userChoice == 2) {
                System.out.print("Enter withdrawal amount: $");
                double amount = scanner.nextDouble();
                if (amount <= balance) {
                    balance = balance - amount;
                    transactionCount = transactionCount + 1;
                    System.out.printf("Withdrawal successful. New balance: $%.2f\n", balance);
                } else {
                    System.out.println("Insufficient funds!");
                }
            } else if (userChoice == 3) {
                System.out.printf("Current balance: $%.2f\n", balance);
                System.out.println("Transactions today: " + transactionCount);
            } else if (userChoice == 4) {
                isRunning = false;
            } else {
                System.out.println("Invalid choice!");
            }
        }
        
        System.out.println("Thank you for banking with us!");
        
        scanner.close();
    }
}
```

**Complex Variable Management:**
- `balance`: Changes with deposits/withdrawals
- `transactionCount`: Increments on successful operations
- `isRunning`: Controls main program loop

**Java Best Practices:**
- Use meaningful variable names (camelCase)
- Format currency with `printf("$%.2f")`
- Validate inputs before processing

---

### Algorithm 6: Temperature Tracker

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int dayCount = 0;  // Not used in this version, but could be for multiple days
        double totalTemperature = 0.0;
        double highestTemp = -1000.0;
        double lowestTemp = 1000.0;
        int readingCount = 0;
        
        System.out.println("Daily Temperature Tracker");
        
        while (readingCount < 24) {
            readingCount = readingCount + 1;
            
            System.out.print("Enter temperature reading #" + readingCount + " (°F): ");
            double temperature = scanner.nextDouble();
            
            totalTemperature = totalTemperature + temperature;
            
            if (temperature > highestTemp) {
                highestTemp = temperature;
            }
            
            if (temperature < lowestTemp) {
                lowestTemp = temperature;
            }
        }
        
        double averageTemp = totalTemperature / 24;
        
        System.out.println("\nTemperature Summary:");
        System.out.printf("Average: %.1f°F\n", averageTemp);
        System.out.printf("Highest: %.1f°F\n", highestTemp);
        System.out.printf("Lowest: %.1f°F\n", lowestTemp);
        System.out.println("Readings taken: " + readingCount);
        
        scanner.close();
    }
}
```

**Statistical Tracking:**
- `highestTemp`: Tracks maximum value (initialized to very low)
- `lowestTemp`: Tracks minimum value (initialized to very high)
- `totalTemperature`: Accumulates all readings for average

**Java Temperature Handling:**
- Use `double` for decimal temperatures
- Initialize min/max with extreme values
- `%.1f` formats to 1 decimal place

---

### Variable Initialization Best Practices

**Counters:** Always start at 0
```java
int count = 0;
```

**Accumulators:** Usually start at 0
```java
double total = 0.0;
```

**Flags:** Initialize to false
```java
boolean isDone = false;
```

**Maximum Trackers:** Initialize to minimum possible value
```java
double maxValue = Double.MIN_VALUE;  // or a very small number like -1000
```

**Minimum Trackers:** Initialize to maximum possible value
```java
double minValue = Double.MAX_VALUE;  // or a very large number like 1000
```

### Common Variable Mistakes in Java

**Forgetting Initialization:**
```java
int sum;  // Uninitialized - compiler error in Java!
sum = sum + 5;  // Won't compile
```

**Wrong Data Types:**
```java
int average;  // Wrong! Should be double for decimals
average = 85.5;  // Compiler error - can't assign double to int
```

**Scope Issues:**
```java
if (condition) {
    int temp = 5;  // Only exists in this block
}
// temp is undefined here - compiler error!
```

**String Comparison:**
```java
String password = "secret";
if (password == "secret") { }  // WRONG! Compares references
if (password.equals("secret")) { }  // CORRECT! Compares content
```

---

### Java Variable Naming Conventions

**camelCase for variables:**
```java
int studentCount = 0;        // ✅ Good
int student_count = 0;       // ❌ Not Java style (that's C/Python)
int StudentCount = 0;        // ❌ That's for class names
```

**Descriptive names:**
```java
double total = 0.0;          // ✅ Clear purpose
double t = 0.0;              // ❌ Too short, unclear
double totalPriceInDollars;  // ✅ Very clear
```

**Constants (final):**
```java
final int MAX_ATTEMPTS = 3;  // ✅ UPPERCASE for constants
```

---

**Excellent! You now understand how variables work in algorithms and Java code!**

*Variables are the foundation of programming logic. Next: Mathematical operations in pseudocode!*
