# Level 7: Function Pseudocode

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`Main.java` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Functions (methods in Java) are the building blocks of organized code! Today you'll master algorithms that use methods for modularity, reusability, and clean program design. You'll learn to break complex problems into smaller, manageable methods.

---

### Learning Goals

- Design algorithms using method decomposition
- Implement method-based program architecture
- Master parameter passing and return values
- Create reusable method libraries
- Develop modular programming practices

---

### Function-Based Design Principles

**Method Decomposition:**
1. **Single Responsibility**: Each method does one thing well
2. **Clear Interface**: Well-defined inputs and outputs
3. **Reusability**: Methods can be used in multiple contexts
4. **Testability**: Individual methods can be tested separately
5. **Maintainability**: Changes are localized to specific methods

**Method Types:**
- **Input Methods**: Get data from users
- **Processing Methods**: Perform calculations
- **Output Methods**: Display results
- **Utility Methods**: Provide common operations
- **Main Method**: Orchestrates the program flow

---

### Your Task

**Translate each method-based pseudocode algorithm into working Java code with proper method decomposition.**

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

## Algorithm 1: Calculator Program with Methods

**Pseudocode:**
```java
Algorithm: Modular Calculator Program

Method: displayMenu()
    Display "=== Calculator Menu ==="
    Display "1. Addition"
    Display "2. Subtraction"
    Display "3. Multiplication"
    Display "4. Division"
    Display "5. Exit"
    Display "Choose operation (1-5): "

Method: getNumber(scanner, prompt)
    Display prompt
    Get number from user
    Return number

Method: performAddition(a, b)
    Return a + b

Method: performSubtraction(a, b)
    Return a - b

Method: performMultiplication(a, b)
    Return a * b

Method: performDivision(a, b)
    If b equals 0:
        Display "❌ Error: Division by zero!"
        Return 0
    Else:
        Return a ÷ b

Method: displayResult(operation, a, b, result)
    Display "Result: " + a + " " + operation + " " + b + " = " + result

Main Algorithm:
1. Initialize scanner
2. Initialize running to true
3. While running is true:
   a. Call displayMenu()
   b. Get choice from user
   c. If choice >= 1 and choice <= 4:
      i. Set num1 = getNumber(scanner, "Enter first number: ")
      ii. Set num2 = getNumber(scanner, "Enter second number: ")
      iii. If choice is 1:
         i. Set result = performAddition(num1, num2)
         ii. Call displayResult("+", num1, num2, result)
      iv. Else if choice is 2:
         i. Set result = performSubtraction(num1, num2)
         ii. Call displayResult("-", num1, num2, result)
      v. Else if choice is 3:
         i. Set result = performMultiplication(num1, num2)
         ii. Call displayResult("*", num1, num2, result)
      vi. Else if choice is 4:
         i. Set result = performDivision(num1, num2)
         ii. If result is not 0 or num2 is not 0:
            i. Call displayResult("/", num1, num2, result)
   d. Else if choice is 5:
      i. Set running to false
   e. Else:
      i. Display "❌ Invalid choice!"
4. Display "Thank you for using the calculator! 👋"
```

**Method Design:**
- `displayMenu()`: Handles UI display
- `getNumber()`: Handles input with prompt
- `perform*()`: Pure calculation methods
- `displayResult()`: Handles output formatting

**Your Task:** Build a modular calculator program.

---

## Algorithm 2: Student Grade Management System

**Pseudocode:**
```java
Algorithm: Student Grade Management with Methods

Method: displayMainMenu()
    Display "=== Grade Management System ==="
    Display "1. Add Student"
    Display "2. View All Students"
    Display "3. Calculate Class Average"
    Display "4. Find Top Performer"
    Display "5. Exit"
    Display "Choose option (1-5): "

Method: addStudent(students, grades, count, scanner)
    If count < 50:
        Display "Enter student name: "
        Get name from user
        Display "Enter grade (0-100): "
        Get grade from user
        If grade is valid (0-100):
            Store name in students[count]
            Store grade in grades[count]
            Add 1 to count
            Display "✓ Student added successfully!"
            Return count
        Else:
            Display "❌ Invalid grade!"
            Return count
    Else:
        Display "⚠ Student list is full!"
        Return count

Method: displayAllStudents(students, grades, count)
    If count > 0:
        Display "=== Student List ==="
        For i from 0 to count - 1:
            Display (i + 1) + ". " + students[i] + " - " + grades[i] + "%"
    Else:
        Display "ℹ No students in the system."

Method: calculateClassAverage(grades, count)
    If count > 0:
        Initialize sum to 0
        For i from 0 to count - 1:
            Add grades[i] to sum
        Return sum ÷ count
    Else:
        Return 0

Method: findTopPerformer(students, grades, count)
    If count > 0:
        Initialize maxGrade to grades[0]
        Initialize topStudent to students[0]
        For i from 1 to count - 1:
            If grades[i] > maxGrade:
                Set maxGrade to grades[i]
                Set topStudent to students[i]
        Display "🏆 Top Performer: " + topStudent + " (" + maxGrade + "%)"
    Else:
        Display "ℹ No students in the system."

Main Algorithm:
1. Initialize students array (50 names)
2. Initialize grades array (50 grades)
3. Initialize studentCount to 0
4. Initialize running to true
5. Initialize scanner
6. While running is true:
   a. Call displayMainMenu()
   b. Get choice from user
   c. If choice is 1:
      i. Set studentCount = addStudent(students, grades, studentCount, scanner)
   d. Else if choice is 2:
      i. Call displayAllStudents(students, grades, studentCount)
   e. Else if choice is 3:
      i. Set average = calculateClassAverage(grades, studentCount)
      ii. If studentCount > 0:
         i. Display "📊 Class Average: " + average + "%"
      iii. Else:
         i. Display "ℹ No students to average."
   f. Else if choice is 4:
      i. Call findTopPerformer(students, grades, studentCount)
   g. Else if choice is 5:
      i. Set running to false
   h. Else:
      i. Display "❌ Invalid choice!"
7. Display "Thank you for using Grade Management System! 👋"
```

**Method Design:**
- `displayMainMenu()`: UI method
- `addStudent()`: Input/modification method
- `displayAllStudents()`: Output method
- `calculateClassAverage()`: Processing method
- `findTopPerformer()`: Analysis method

**Your Task:** Create a modular student grade management system.

---

## Algorithm 3: Banking System with Methods

**Pseudocode:**
```java
Algorithm: Simple Banking System with Methods

Method: displayBankMenu()
    Display "=== Banking System ==="
    Display "1. Deposit"
    Display "2. Withdraw"
    Display "3. Check Balance"
    Display "4. Transaction History"
    Display "5. Exit"
    Display "Choose option (1-5): "

Method: deposit(balance, amount)
    If amount > 0:
        Set newBalance = balance + amount
        Display "✓ Deposited: $" + amount
        Display "New balance: $" + newBalance
        Return newBalance
    Else:
        Display "❌ Invalid deposit amount!"
        Return balance

Method: withdraw(balance, amount)
    If amount > 0 and amount <= balance:
        Set newBalance = balance - amount
        Display "✓ Withdrawn: $" + amount
        Display "New balance: $" + newBalance
        Return newBalance
    Else if amount > balance:
        Display "❌ Insufficient funds!"
        Return balance
    Else:
        Display "❌ Invalid withdrawal amount!"
        Return balance

Method: displayBalance(balance)
    Display "💰 Current Balance: $" + balance

Method: addTransaction(transactions, count, type, amount)
    If count < 100:
        Store type + " $" + amount in transactions[count]
        Return count + 1
    Else:
        Return count

Method: displayTransactions(transactions, count)
    If count > 0:
        Display "=== Transaction History ==="
        For i from 0 to count - 1:
            Display (i + 1) + ". " + transactions[i]
    Else:
        Display "ℹ No transactions yet."

Main Algorithm:
1. Initialize balance to 1000.00
2. Initialize transactions array (100 entries)
3. Initialize transactionCount to 0
4. Initialize running to true
5. Initialize scanner
6. While running is true:
   a. Call displayBankMenu()
   b. Get choice from user
   c. If choice is 1:
      i. Display "Enter deposit amount: $"
      ii. Get amount from user
      iii. Set oldBalance = balance
      iv. Set balance = deposit(balance, amount)
      v. If balance != oldBalance:
         i. Set transactionCount = addTransaction(transactions, transactionCount, "Deposit", amount)
   d. Else if choice is 2:
      i. Display "Enter withdrawal amount: $"
      ii. Get amount from user
      iii. Set oldBalance = balance
      iv. Set balance = withdraw(balance, amount)
      v. If balance != oldBalance:
         i. Set transactionCount = addTransaction(transactions, transactionCount, "Withdrawal", amount)
   e. Else if choice is 3:
      i. Call displayBalance(balance)
   f. Else if choice is 4:
      i. Call displayTransactions(transactions, transactionCount)
   g. Else if choice is 5:
      i. Set running to false
   h. Else:
      i. Display "❌ Invalid choice!"
7. Display "Thank you for banking with us! 👋"
```

**Method Design:**
- `displayBankMenu()`: UI method
- `deposit()`, `withdraw()`: Transaction methods
- `displayBalance()`: Status method
- `addTransaction()`, `displayTransactions()`: History methods

**Your Task:** Build a modular banking system.

---

## Algorithm 4: Statistics Calculator with Methods

**Pseudocode:**
```java
Algorithm: Statistical Analysis with Methods

Method: displayStatsMenu()
    Display "=== Statistics Calculator ==="
    Display "1. Enter Data"
    Display "2. Calculate Mean"
    Display "3. Calculate Median"
    Display "4. Calculate Mode"
    Display "5. Display All Stats"
    Display "6. Exit"
    Display "Choose option (1-6): "

Method: enterData(data, scanner)
    Display "How many numbers to enter? "
    Get count from user
    If count > 0 and count <= 100:
        For i from 0 to count - 1:
            Display "Enter number " + (i + 1) + ": "
            Get data[i] from user
        Display "✓ " + count + " numbers entered."
        Return count
    Else:
        Display "❌ Invalid count!"
        Return 0

Method: calculateMean(data, count)
    If count > 0:
        Initialize sum to 0
        For i from 0 to count - 1:
            Add data[i] to sum
        Return sum ÷ count
    Else:
        Return 0

Method: calculateMedian(data, count)
    If count > 0:
        Sort data array
        If count is odd:
            Return data[count ÷ 2]
        Else:
            Set mid1 = data[count ÷ 2 - 1]
            Set mid2 = data[count ÷ 2]
            Return (mid1 + mid2) ÷ 2
    Else:
        Return 0

Method: calculateMode(data, count)
    If count > 0:
        Initialize maxFrequency to 0
        Initialize mode to data[0]
        For i from 0 to count - 1:
            Initialize frequency to 0
            For j from 0 to count - 1:
                If data[j] equals data[i]:
                    Add 1 to frequency
            If frequency > maxFrequency:
                Set maxFrequency to frequency
                Set mode to data[i]
        Return mode
    Else:
        Return 0

Method: displayAllStats(data, count)
    If count > 0:
        Display "=== Statistical Summary ==="
        Display "Count: " + count
        Display "Mean: " + calculateMean(data, count)
        Display "Median: " + calculateMedian(data, count)
        Display "Mode: " + calculateMode(data, count)
    Else:
        Display "ℹ No data entered yet."

Main Algorithm:
1. Initialize data array (100 numbers)
2. Initialize dataCount to 0
3. Initialize running to true
4. Initialize scanner
5. While running is true:
   a. Call displayStatsMenu()
   b. Get choice from user
   c. If choice is 1:
      i. Set dataCount = enterData(data, scanner)
   d. Else if choice is 2:
      i. If dataCount > 0:
         i. Display "📊 Mean: " + calculateMean(data, dataCount)
      ii. Else:
         i. Display "ℹ No data to calculate."
   e. Else if choice is 3:
      i. If dataCount > 0:
         i. Display "📊 Median: " + calculateMedian(data, dataCount)
      ii. Else:
         i. Display "ℹ No data to calculate."
   f. Else if choice is 4:
      i. If dataCount > 0:
         i. Display "📊 Mode: " + calculateMode(data, dataCount)
      ii. Else:
         i. Display "ℹ No data to calculate."
   g. Else if choice is 5:
      i. Call displayAllStats(data, dataCount)
   h. Else if choice is 6:
      i. Set running to false
   i. Else:
      i. Display "❌ Invalid choice!"
6. Display "Thank you for using Statistics Calculator! 👋"
```

**Method Design:**
- `displayStatsMenu()`: UI method
- `enterData()`: Input method
- `calculateMean()`, `calculateMedian()`, `calculateMode()`: Statistical methods
- `displayAllStats()`: Summary method

**Your Task:** Create a statistical analysis system.

---

## Algorithm 5: Text Analyzer with Methods

**Pseudocode:**
```java
Algorithm: Text Analysis with Methods

Method: displayTextMenu()
    Display "=== Text Analyzer ==="
    Display "1. Enter Text"
    Display "2. Count Words"
    Display "3. Count Characters"
    Display "4. Count Vowels"
    Display "5. Reverse Text"
    Display "6. Display All Analysis"
    Display "7. Exit"
    Display "Choose option (1-7): "

Method: enterText(scanner)
    Display "Enter text: "
    Get text from user
    Display "✓ Text entered successfully!"
    Return text

Method: countWords(text)
    If text is empty:
        Return 0
    Initialize count to 1
    For each character in text:
        If character is space:
            Add 1 to count
    Return count

Method: countCharacters(text)
    Return length of text

Method: countVowels(text)
    Initialize count to 0
    For each character in text:
        If character is 'a', 'e', 'i', 'o', 'u' (case-insensitive):
            Add 1 to count
    Return count

Method: reverseText(text)
    Initialize reversed to empty string
    For i from (length of text - 1) down to 0:
        Append text[i] to reversed
    Return reversed

Method: displayAllAnalysis(text)
    If text is not empty:
        Display "=== Text Analysis Results ==="
        Display "Original Text: " + text
        Display "Word Count: " + countWords(text)
        Display "Character Count: " + countCharacters(text)
        Display "Vowel Count: " + countVowels(text)
        Display "Reversed: " + reverseText(text)
    Else:
        Display "ℹ No text entered yet."

Main Algorithm:
1. Initialize text to empty string
2. Initialize running to true
3. Initialize scanner
4. While running is true:
   a. Call displayTextMenu()
   b. Get choice from user
   c. If choice is 1:
      i. Set text = enterText(scanner)
   d. Else if choice is 2:
      i. If text is not empty:
         i. Display "📝 Word Count: " + countWords(text)
      ii. Else:
         i. Display "ℹ No text entered yet."
   e. Else if choice is 3:
      i. If text is not empty:
         i. Display "📝 Character Count: " + countCharacters(text)
      ii. Else:
         i. Display "ℹ No text entered yet."
   f. Else if choice is 4:
      i. If text is not empty:
         i. Display "📝 Vowel Count: " + countVowels(text)
      ii. Else:
         i. Display "ℹ No text entered yet."
   g. Else if choice is 5:
      i. If text is not empty:
         i. Display "📝 Reversed: " + reverseText(text)
      ii. Else:
         i. Display "ℹ No text entered yet."
   h. Else if choice is 6:
      i. Call displayAllAnalysis(text)
   i. Else if choice is 7:
      i. Set running to false
   j. Else:
      i. Display "❌ Invalid choice!"
5. Display "Thank you for using Text Analyzer! 👋"
```

**Method Design:**
- `displayTextMenu()`: UI method
- `enterText()`: Input method
- `countWords()`, `countCharacters()`, `countVowels()`: Analysis methods
- `reverseText()`: Transformation method
- `displayAllAnalysis()`: Summary method

**Your Task:** Build a text analysis system.

---

### Method Design Best Practices

**Method Signature Guidelines:**
- **Descriptive Names**: Use verbs for actions (calculateTotal, displayMenu)
- **Clear Parameters**: Only pass what's needed
- **Return Values**: Return results rather than printing when possible
- **Consistent Patterns**: Use similar naming for similar operations

**Parameter Passing:**
- **Primitive Types**: Passed by value (int, double, boolean)
- **Objects/Arrays**: Passed by reference (modifications affect original)
- **Scanner Objects**: Pass as parameter to avoid multiple Scanner instances

**Method Length:**
- Keep methods focused (single responsibility)
- Aim for 10-30 lines per method
- Extract complex logic into helper methods

---

### Success Checklist

**For Each Algorithm:**
- [ ] Decomposed program into logical methods
- [ ] Each method has single, clear purpose
- [ ] Used appropriate parameter passing
- [ ] Returned values from calculation methods
- [ ] Avoided code duplication

**Method Implementation:**
- [ ] Used static methods for utility functions
- [ ] Passed Scanner as parameter where needed
- [ ] Named methods descriptively
- [ ] Handled edge cases in methods

---

### Try This (Optional Challenges)

1. **Add Method Overloading**: Create multiple versions of methods with different parameters
2. **Extract Validation**: Create separate validation methods
3. **Add Helper Methods**: Break complex methods into smaller helpers
4. **Create Utility Classes**: Group related methods into separate classes

---

## Method Design Patterns

### Input-Process-Output Pattern
```
Method: getUserInput(scanner, prompt)
    Display prompt
    Get and return input

Method: processData(data)
    Perform calculations
    Return result

Method: displayOutput(result)
    Format and display result
```

### Validation Pattern
```java
Method: isValid(value, min, max)
    Return value >= min && value <= max

Method: getValidInput(scanner, prompt, min, max)
    While true:
        Display prompt
        Get input
        If isValid(input, min, max):
            Return input
        Display error message
```

### Calculation with Helper Pattern
```java
Method: calculateTotal(items, count)
    Sum = 0
    For i from 0 to count:
        Sum += calculateItemValue(items[i])
    Return sum

Method: calculateItemValue(item)
    Return item.price * item.quantity
```

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Calculator Program with Methods

```java
import java.util.Scanner;

public class ModularCalculator {
    
    public static void displayMenu() {
        System.out.println("\n=== Calculator Menu ===");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");
        System.out.println("5. Exit");
        System.out.print("Choose operation (1-5): ");
    }
    
    public static double getNumber(Scanner scanner, String prompt) {
        System.out.print(prompt);
        return scanner.nextDouble();
    }
    
    public static double performAddition(double a, double b) {
        return a + b;
    }
    
    public static double performSubtraction(double a, double b) {
        return a - b;
    }
    
    public static double performMultiplication(double a, double b) {
        return a * b;
    }
    
    public static double performDivision(double a, double b) {
        if (b == 0) {
            System.out.println("❌ Error: Division by zero!");
            return 0;
        } else {
            return a / b;
        }
    }
    
    public static void displayResult(String operation, double a, double b, double result) {
        System.out.printf("Result: %.2f %s %.2f = %.2f\n", a, operation, b, result);
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;
        
        while (running) {
            displayMenu();
            int choice = scanner.nextInt();
            
            if (choice >= 1 && choice <= 4) {
                double num1 = getNumber(scanner, "Enter first number: ");
                double num2 = getNumber(scanner, "Enter second number: ");
                double result;
                
                switch (choice) {
                    case 1:
                        result = performAddition(num1, num2);
                        displayResult("+", num1, num2, result);
                        break;
                    case 2:
                        result = performSubtraction(num1, num2);
                        displayResult("-", num1, num2, result);
                        break;
                    case 3:
                        result = performMultiplication(num1, num2);
                        displayResult("*", num1, num2, result);
                        break;
                    case 4:
                        result = performDivision(num1, num2);
                        if (result != 0 || num2 != 0) {
                            displayResult("/", num1, num2, result);
                        }
                        break;
                }
            } else if (choice == 5) {
                running = false;
            } else {
                System.out.println("❌ Invalid choice!");
            }
        }
        
        System.out.println("Thank you for using the calculator! 👋");
        scanner.close();
    }
}
```

**Key Concepts:**
- Static methods for utility functions (no instance needed)
- Method decomposition: separate concerns
- Parameter passing for Scanner and values
- Return values from calculation methods

**Variable Analysis:**
- Methods are static (called without object instance)
- Scanner passed as parameter to avoid multiple instances
- Each calculation method is pure (no side effects)

**Java-Specific Notes:**
- `public static` for methods called from main
- Method naming: camelCase (performAddition not perform_addition)
- void return type for display methods
- double return type for calculations

---

### Algorithm 2: Student Grade Management System

```java
import java.util.Scanner;

public class GradeManagement {
    
    public static void displayMainMenu() {
        System.out.println("\n=== Grade Management System ===");
        System.out.println("1. Add Student");
        System.out.println("2. View All Students");
        System.out.println("3. Calculate Class Average");
        System.out.println("4. Find Top Performer");
        System.out.println("5. Exit");
        System.out.print("Choose option (1-5): ");
    }
    
    public static int addStudent(String[] students, double[] grades, int count, Scanner scanner) {
        if (count < 50) {
            scanner.nextLine(); // Consume newline
            System.out.print("Enter student name: ");
            String name = scanner.nextLine();
            System.out.print("Enter grade (0-100): ");
            double grade = scanner.nextDouble();
            
            if (grade >= 0 && grade <= 100) {
                students[count] = name;
                grades[count] = grade;
                System.out.println("✓ Student added successfully!");
                return count + 1;
            } else {
                System.out.println("❌ Invalid grade!");
                return count;
            }
        } else {
            System.out.println("⚠ Student list is full!");
            return count;
        }
    }
    
    public static void displayAllStudents(String[] students, double[] grades, int count) {
        if (count > 0) {
            System.out.println("\n=== Student List ===");
            for (int i = 0; i < count; i++) {
                System.out.printf("%d. %s - %.1f%%\n", i + 1, students[i], grades[i]);
            }
        } else {
            System.out.println("ℹ No students in the system.");
        }
    }
    
    public static double calculateClassAverage(double[] grades, int count) {
        if (count > 0) {
            double sum = 0;
            for (int i = 0; i < count; i++) {
                sum += grades[i];
            }
            return sum / count;
        } else {
            return 0;
        }
    }
    
    public static void findTopPerformer(String[] students, double[] grades, int count) {
        if (count > 0) {
            double maxGrade = grades[0];
            String topStudent = students[0];
            
            for (int i = 1; i < count; i++) {
                if (grades[i] > maxGrade) {
                    maxGrade = grades[i];
                    topStudent = students[i];
                }
            }
            
            System.out.printf("🏆 Top Performer: %s (%.1f%%)\n", topStudent, maxGrade);
        } else {
            System.out.println("ℹ No students in the system.");
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] students = new String[50];
        double[] grades = new double[50];
        int studentCount = 0;
        boolean running = true;
        
        while (running) {
            displayMainMenu();
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    studentCount = addStudent(students, grades, studentCount, scanner);
                    break;
                case 2:
                    displayAllStudents(students, grades, studentCount);
                    break;
                case 3:
                    if (studentCount > 0) {
                        double average = calculateClassAverage(grades, studentCount);
                        System.out.printf("📊 Class Average: %.1f%%\n", average);
                    } else {
                        System.out.println("ℹ No students to average.");
                    }
                    break;
                case 4:
                    findTopPerformer(students, grades, studentCount);
                    break;
                case 5:
                    running = false;
                    break;
                default:
                    System.out.println("❌ Invalid choice!");
                    break;
            }
        }
        
        System.out.println("Thank you for using Grade Management System! 👋");
        scanner.close();
    }
}
```

**Key Concepts:**
- Methods modifying arrays (arrays passed by reference)
- Return updated count from addStudent
- void methods for display operations
- double return for calculations

**Variable Analysis:**
- Arrays passed to methods (modifications affect original)
- count returned from addStudent (can't modify primitive parameter)
- maxGrade and topStudent tracked together

**Java-Specific Notes:**
- Arrays are objects, passed by reference
- Must return new count (int is pass-by-value)
- scanner.nextLine() after nextInt() to consume newline

---

### Algorithm 3: Banking System with Methods

```java
import java.util.Scanner;

public class BankingSystem {
    
    public static void displayBankMenu() {
        System.out.println("\n=== Banking System ===");
        System.out.println("1. Deposit");
        System.out.println("2. Withdraw");
        System.out.println("3. Check Balance");
        System.out.println("4. Transaction History");
        System.out.println("5. Exit");
        System.out.print("Choose option (1-5): ");
    }
    
    public static double deposit(double balance, double amount) {
        if (amount > 0) {
            double newBalance = balance + amount;
            System.out.printf("✓ Deposited: $%.2f\n", amount);
            System.out.printf("New balance: $%.2f\n", newBalance);
            return newBalance;
        } else {
            System.out.println("❌ Invalid deposit amount!");
            return balance;
        }
    }
    
    public static double withdraw(double balance, double amount) {
        if (amount > 0 && amount <= balance) {
            double newBalance = balance - amount;
            System.out.printf("✓ Withdrawn: $%.2f\n", amount);
            System.out.printf("New balance: $%.2f\n", newBalance);
            return newBalance;
        } else if (amount > balance) {
            System.out.println("❌ Insufficient funds!");
            return balance;
        } else {
            System.out.println("❌ Invalid withdrawal amount!");
            return balance;
        }
    }
    
    public static void displayBalance(double balance) {
        System.out.printf("💰 Current Balance: $%.2f\n", balance);
    }
    
    public static int addTransaction(String[] transactions, int count, String type, double amount) {
        if (count < 100) {
            transactions[count] = String.format("%s $%.2f", type, amount);
            return count + 1;
        } else {
            return count;
        }
    }
    
    public static void displayTransactions(String[] transactions, int count) {
        if (count > 0) {
            System.out.println("\n=== Transaction History ===");
            for (int i = 0; i < count; i++) {
                System.out.println((i + 1) + ". " + transactions[i]);
            }
        } else {
            System.out.println("ℹ No transactions yet.");
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double balance = 1000.00;
        String[] transactions = new String[100];
        int transactionCount = 0;
        boolean running = true;
        
        while (running) {
            displayBankMenu();
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    System.out.print("Enter deposit amount: $");
                    double depositAmount = scanner.nextDouble();
                    double oldBalance = balance;
                    balance = deposit(balance, depositAmount);
                    if (balance != oldBalance) {
                        transactionCount = addTransaction(transactions, transactionCount, 
                                                        "Deposit", depositAmount);
                    }
                    break;
                case 2:
                    System.out.print("Enter withdrawal amount: $");
                    double withdrawAmount = scanner.nextDouble();
                    oldBalance = balance;
                    balance = withdraw(balance, withdrawAmount);
                    if (balance != oldBalance) {
                        transactionCount = addTransaction(transactions, transactionCount, 
                                                        "Withdrawal", withdrawAmount);
                    }
                    break;
                case 3:
                    displayBalance(balance);
                    break;
                case 4:
                    displayTransactions(transactions, transactionCount);
                    break;
                case 5:
                    running = false;
                    break;
                default:
                    System.out.println("❌ Invalid choice!");
                    break;
            }
        }
        
        System.out.println("Thank you for banking with us! 👋");
        scanner.close();
    }
}
```

**Key Concepts:**
- Methods returning new balance (double)
- Transaction logging with String array
- Conditional transaction recording (only if successful)
- Balance validation in withdraw method

**Variable Analysis:**
- balance updated by returning new value
- oldBalance stored to detect changes
- transactions array for history

**Java-Specific Notes:**
- Return new balance from deposit/withdraw
- String.format() for transaction formatting
- Check balance change to log transaction

---

### Algorithm 4: Statistics Calculator with Methods

```java
import java.util.Scanner;
import java.util.Arrays;

public class StatisticsCalculator {
    
    public static void displayStatsMenu() {
        System.out.println("\n=== Statistics Calculator ===");
        System.out.println("1. Enter Data");
        System.out.println("2. Calculate Mean");
        System.out.println("3. Calculate Median");
        System.out.println("4. Calculate Mode");
        System.out.println("5. Display All Stats");
        System.out.println("6. Exit");
        System.out.print("Choose option (1-6): ");
    }
    
    public static int enterData(double[] data, Scanner scanner) {
        System.out.print("How many numbers to enter? ");
        int count = scanner.nextInt();
        
        if (count > 0 && count <= 100) {
            for (int i = 0; i < count; i++) {
                System.out.print("Enter number " + (i + 1) + ": ");
                data[i] = scanner.nextDouble();
            }
            System.out.println("✓ " + count + " numbers entered.");
            return count;
        } else {
            System.out.println("❌ Invalid count!");
            return 0;
        }
    }
    
    public static double calculateMean(double[] data, int count) {
        if (count > 0) {
            double sum = 0;
            for (int i = 0; i < count; i++) {
                sum += data[i];
            }
            return sum / count;
        } else {
            return 0;
        }
    }
    
    public static double calculateMedian(double[] data, int count) {
        if (count > 0) {
            // Create copy to avoid modifying original
            double[] sorted = Arrays.copyOf(data, count);
            Arrays.sort(sorted);
            
            if (count % 2 == 1) {
                return sorted[count / 2];
            } else {
                double mid1 = sorted[count / 2 - 1];
                double mid2 = sorted[count / 2];
                return (mid1 + mid2) / 2.0;
            }
        } else {
            return 0;
        }
    }
    
    public static double calculateMode(double[] data, int count) {
        if (count > 0) {
            int maxFrequency = 0;
            double mode = data[0];
            
            for (int i = 0; i < count; i++) {
                int frequency = 0;
                for (int j = 0; j < count; j++) {
                    if (data[j] == data[i]) {
                        frequency++;
                    }
                }
                
                if (frequency > maxFrequency) {
                    maxFrequency = frequency;
                    mode = data[i];
                }
            }
            
            return mode;
        } else {
            return 0;
        }
    }
    
    public static void displayAllStats(double[] data, int count) {
        if (count > 0) {
            System.out.println("\n=== Statistical Summary ===");
            System.out.println("Count: " + count);
            System.out.printf("Mean: %.2f\n", calculateMean(data, count));
            System.out.printf("Median: %.2f\n", calculateMedian(data, count));
            System.out.printf("Mode: %.2f\n", calculateMode(data, count));
        } else {
            System.out.println("ℹ No data entered yet.");
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] data = new double[100];
        int dataCount = 0;
        boolean running = true;
        
        while (running) {
            displayStatsMenu();
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    dataCount = enterData(data, scanner);
                    break;
                case 2:
                    if (dataCount > 0) {
                        System.out.printf("📊 Mean: %.2f\n", calculateMean(data, dataCount));
                    } else {
                        System.out.println("ℹ No data to calculate.");
                    }
                    break;
                case 3:
                    if (dataCount > 0) {
                        System.out.printf("📊 Median: %.2f\n", calculateMedian(data, dataCount));
                    } else {
                        System.out.println("ℹ No data to calculate.");
                    }
                    break;
                case 4:
                    if (dataCount > 0) {
                        System.out.printf("📊 Mode: %.2f\n", calculateMode(data, dataCount));
                    } else {
                        System.out.println("ℹ No data to calculate.");
                    }
                    break;
                case 5:
                    displayAllStats(data, dataCount);
                    break;
                case 6:
                    running = false;
                    break;
                default:
                    System.out.println("❌ Invalid choice!");
                    break;
            }
        }
        
        System.out.println("Thank you for using Statistics Calculator! 👋");
        scanner.close();
    }
}
```

**Key Concepts:**
- Statistical calculation methods
- Array sorting for median (using Arrays.sort())
- Frequency counting for mode
- Reusing calculation methods in displayAllStats

**Variable Analysis:**
- data array modified by enterData
- sorted copy created in calculateMedian (preserve original)
- Nested loops for mode frequency counting

**Java-Specific Notes:**
- Arrays.copyOf() to create copy before sorting
- Arrays.sort() for sorting (import java.util.Arrays)
- Modulo (%) for odd/even detection

---

### Algorithm 5: Text Analyzer with Methods

```java
import java.util.Scanner;

public class TextAnalyzer {
    
    public static void displayTextMenu() {
        System.out.println("\n=== Text Analyzer ===");
        System.out.println("1. Enter Text");
        System.out.println("2. Count Words");
        System.out.println("3. Count Characters");
        System.out.println("4. Count Vowels");
        System.out.println("5. Reverse Text");
        System.out.println("6. Display All Analysis");
        System.out.println("7. Exit");
        System.out.print("Choose option (1-7): ");
    }
    
    public static String enterText(Scanner scanner) {
        scanner.nextLine(); // Consume newline
        System.out.print("Enter text: ");
        String text = scanner.nextLine();
        System.out.println("✓ Text entered successfully!");
        return text;
    }
    
    public static int countWords(String text) {
        if (text.isEmpty()) {
            return 0;
        }
        
        int count = 1;
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == ' ') {
                count++;
            }
        }
        return count;
    }
    
    public static int countCharacters(String text) {
        return text.length();
    }
    
    public static int countVowels(String text) {
        int count = 0;
        String vowels = "aeiouAEIOU";
        
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (vowels.indexOf(c) != -1) {
                count++;
            }
        }
        return count;
    }
    
    public static String reverseText(String text) {
        StringBuilder reversed = new StringBuilder();
        for (int i = text.length() - 1; i >= 0; i--) {
            reversed.append(text.charAt(i));
        }
        return reversed.toString();
    }
    
    public static void displayAllAnalysis(String text) {
        if (!text.isEmpty()) {
            System.out.println("\n=== Text Analysis Results ===");
            System.out.println("Original Text: " + text);
            System.out.println("Word Count: " + countWords(text));
            System.out.println("Character Count: " + countCharacters(text));
            System.out.println("Vowel Count: " + countVowels(text));
            System.out.println("Reversed: " + reverseText(text));
        } else {
            System.out.println("ℹ No text entered yet.");
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String text = "";
        boolean running = true;
        
        while (running) {
            displayTextMenu();
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    text = enterText(scanner);
                    break;
                case 2:
                    if (!text.isEmpty()) {
                        System.out.println("📝 Word Count: " + countWords(text));
                    } else {
                        System.out.println("ℹ No text entered yet.");
                    }
                    break;
                case 3:
                    if (!text.isEmpty()) {
                        System.out.println("📝 Character Count: " + countCharacters(text));
                    } else {
                        System.out.println("ℹ No text entered yet.");
                    }
                    break;
                case 4:
                    if (!text.isEmpty()) {
                        System.out.println("📝 Vowel Count: " + countVowels(text));
                    } else {
                        System.out.println("ℹ No text entered yet.");
                    }
                    break;
                case 5:
                    if (!text.isEmpty()) {
                        System.out.println("📝 Reversed: " + reverseText(text));
                    } else {
                        System.out.println("ℹ No text entered yet.");
                    }
                    break;
                case 6:
                    displayAllAnalysis(text);
                    break;
                case 7:
                    running = false;
                    break;
                default:
                    System.out.println("❌ Invalid choice!");
                    break;
            }
        }
        
        System.out.println("Thank you for using Text Analyzer! 👋");
        scanner.close();
    }
}
```

**Key Concepts:**
- String manipulation methods
- Character iteration with charAt()
- StringBuilder for efficient string building
- String methods (isEmpty(), length(), indexOf())

**Variable Analysis:**
- text stored as String (immutable)
- reversed built with StringBuilder (mutable, efficient)
- count variables for statistics

**Java-Specific Notes:**
- String is immutable (can't modify characters)
- charAt(i) to access character at index
- indexOf() to search for character in string
- StringBuilder for building strings in loops

**Common Mistakes:**
- Using String concatenation in loops (inefficient)
- Not consuming newline after nextInt()
- Treating String as char array (use charAt())

---

### Method Design Patterns in Java

**Input Validation Method:**
```java
public static int getValidInt(Scanner scanner, String prompt, int min, int max) {
    while (true) {
        System.out.print(prompt);
        if (scanner.hasNextInt()) {
            int value = scanner.nextInt();
            if (value >= min && value <= max) {
                return value;
            }
        } else {
            scanner.next(); // Clear invalid input
        }
        System.out.printf("Please enter a number between %d and %d\n", min, max);
    }
}
```

**Array Processing Pattern:**
```java
public static double processArray(double[] array, int count) {
    double result = 0;
    for (int i = 0; i < count; i++) {
        result += someOperation(array[i]);
    }
    return result;
}

private static double someOperation(double value) {
    // Helper method for complex operation
    return value * 2;
}
```

**Menu-Driven Pattern:**
```java
public static void displayMenu() {
    System.out.println("\n=== Menu ===");
    // Display options
}

public static void handleChoice(int choice, /* parameters */) {
    switch (choice) {
        case 1:
            method1();
            break;
        case 2:
            method2();
            break;
        // etc.
    }
}
```

---

✅ **Congratulations! You've mastered method-based programming in Java!** 

*You've completed Stage 2! You can now translate pseudocode into well-organized, modular Java programs. Next stages will challenge you with problem-solving and algorithm design! 🎓*
