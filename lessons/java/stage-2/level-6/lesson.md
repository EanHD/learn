# Level 6: Loop Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`Main.java` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Loops are the workhorses of programming! Today you'll master algorithms that use repetition, accumulation, and iteration to solve complex problems. You'll learn to think in terms of patterns, sequences, and repeated operations.

---

### Learning Goals

- Implement algorithms with counting and accumulation loops
- Create nested loop structures for complex patterns
- Use loops for data processing and validation
- Master loop control and termination conditions
- Develop iterative problem-solving approaches

---

### Loop Patterns in Programming

**Common Loop Applications:**
1. **Counting**: Track how many times something occurs
2. **Accumulation**: Sum values, calculate totals
3. **Iteration**: Process each item in a collection
4. **Validation**: Repeat until valid input received
5. **Generation**: Create sequences and patterns
6. **Searching**: Look through data for specific items

**Loop Control:**
- **Initialization**: Set starting values
- **Condition**: When to continue looping
- **Update**: Change values each iteration
- **Termination**: When to stop

---

### Your Task

**Translate each loop-based pseudocode algorithm into working Java code.**

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
```java
Hello, World!
```java

## Algorithm 1: Sales Data Analyzer

**Pseudocode:**
```java
Algorithm: Analyze Monthly Sales Data
1. Display "=== Sales Data Analyzer ==="
2. Initialize sales array (can hold 30 values)
3. Initialize salesCount to 0
4. Initialize totalSales to 0
5. Initialize highestSale to 0
6. Initialize lowestSale to 999999
7. Display "Enter daily sales (enter -1 to finish):"
8. While salesCount < 30:
   a. Display "Day " + (salesCount + 1) + ": $"
   b. Get dailySale from user
   c. If dailySale equals -1:
      i. Break out of loop
   d. Else if dailySale >= 0:
      i. Store dailySale in sales array
      ii. Add dailySale to totalSales
      iii. Add 1 to salesCount
      iv. If dailySale > highestSale:
         i. Set highestSale to dailySale
      v. If dailySale < lowestSale:
         i. Set lowestSale to dailySale
   e. Else:
      i. Display " Invalid sale amount! Please enter positive number."
9. If salesCount > 0:
   a. Calculate averageSale = totalSales ÷ salesCount
   b. Display "=== Sales Summary ==="
   c. Display "Total days: " + salesCount
   d. Display "Total sales: $" + totalSales
   e. Display "Average daily sales: $" + averageSale
   f. Display "Highest sale: $" + highestSale
   g. Display "Lowest sale: $" + lowestSale
   h. Display "=== Daily Breakdown ==="
   i. For i from 0 to salesCount - 1:
      i. Display "Day " + (i + 1) + ": $" + sales[i]
10. Else:
   a. Display "No sales data entered."
```java

**Loop Logic:**
- Input loop with validation
- Accumulation of sales data
- Statistical calculations
- Array iteration for display

**Your Task:** Create a sales data analysis system.

---

## Algorithm 2: Student Attendance Tracker

**Pseudocode:**
```java
Algorithm: Track Class Attendance
1. Display "=== Class Attendance Tracker ==="
2. Display "Enter number of students: "
3. Get numStudents from user
4. Initialize attendance array (size numStudents)
5. Initialize presentCount to 0
6. For student from 1 to numStudents:
   a. Display "Student " + student + " present? (y/n): "
   b. Get attendanceStatus from user
   c. If attendanceStatus is "y" or "Y":
      i. Set attendance[student-1] to true
      ii. Add 1 to presentCount
   d. Else:
      i. Set attendance[student-1] to false
7. Calculate attendancePercentage = (presentCount ÷ numStudents) × 100
8. Display "=== Attendance Report ==="
9. Display "Total students: " + numStudents
10. Display "Present: " + presentCount
11. Display "Absent: " + (numStudents - presentCount)
12. Display "Attendance rate: " + attendancePercentage + "%"
13. If attendancePercentage >= 90:
   a. Display " Excellent attendance!"
14. Else if attendancePercentage >= 75:
   a. Display " Satisfactory attendance"
15. Else:
   a. Display " Poor attendance - follow up required"
16. Display "=== Individual Status ==="
17. For student from 1 to numStudents:
   a. If attendance[student-1] is true:
      i. Display "Student " + student + ":  Present"
   b. Else:
      i. Display "Student " + student + ":  Absent"
```java

**Loop Logic:**
- Fixed iteration for known number of students
- Array storage of attendance data
- Percentage calculations
- Conditional reporting based on attendance rate

**Your Task:** Build a class attendance tracking system.

---

## Algorithm 3: Inventory Management System

**Pseudocode:**
```java
Algorithm: Manage Store Inventory
1. Display "=== Inventory Management System ==="
2. Initialize itemNames array (can hold 50 items)
3. Initialize itemQuantities array (size 50)
4. Initialize itemCount to 0
5. Initialize isRunning to true
6. While isRunning is true:
   a. Display menu:
      i. "1. Add Item"
      ii. "2. Update Quantity"
      iii. "3. Display Inventory"
      iv. "4. Find Low Stock Items"
      v. "5. Exit"
   b. Display "Choose option (1-5): "
   c. Get choice from user
   d. If choice is 1:
      i. If itemCount < 50:
         i. Display "Enter item name: "
         ii. Get newItemName from user
         iii. Display "Enter initial quantity: "
         iv. Get newQuantity from user
         v. If newQuantity >= 0:
            i. Store newItemName in itemNames array
            ii. Store newQuantity in itemQuantities array
            iii. Add 1 to itemCount
            iv. Display " Item added successfully!"
         vi. Else:
            i. Display " Invalid quantity!"
      ii. Else:
         i. Display " Inventory is full!"
   e. Else if choice is 2:
      i. If itemCount > 0:
         i. Display "Enter item name to update: "
         ii. Get searchName from user
         iii. Initialize found to false
         iv. For i from 0 to itemCount - 1:
            i. If itemNames[i] equals searchName:
               i. Display "Current quantity: " + itemQuantities[i]
               ii. Display "Enter new quantity: "
               iii. Get newQuantity from user
               iv. If newQuantity >= 0:
                  i. Set itemQuantities[i] to newQuantity
                  ii. Display " Quantity updated!"
                  iii. Set found to true
                  iv. Break out of loop
         v. If found is false:
            i. Display " Item not found!"
      ii. Else:
         i. Display "ℹ No items in inventory."
   f. Else if choice is 3:
      i. If itemCount > 0:
         i. Display "=== Current Inventory ==="
         ii. For i from 0 to itemCount - 1:
            i. Display itemNames[i] + ": " + itemQuantities[i] + " units"
      ii. Else:
         i. Display "ℹ Inventory is empty."
   g. Else if choice is 4:
      i. If itemCount > 0:
         i. Display "=== Low Stock Alert (≤5 units) ==="
         ii. Initialize lowStockCount to 0
         iii. For i from 0 to itemCount - 1:
            i. If itemQuantities[i] <= 5:
               i. Display itemNames[i] + ": " + itemQuantities[i] + " units "
               ii. Add 1 to lowStockCount
         iv. If lowStockCount is 0:
            i. Display " All items have sufficient stock."
      ii. Else:
         i. Display "ℹ No items to check."
   h. Else if choice is 5:
      i. Set isRunning to false
   i. Else:
      i. Display " Invalid choice!"
7. Display "Thank you for using Inventory Management System! "
```java

**Loop Logic:**
- Menu-driven interface with multiple operations
- Array search and update operations
- Inventory monitoring and alerts
- Data validation and error handling

**Your Task:** Create a comprehensive inventory management system.

---

## Algorithm 4: Grade Book Calculator

**Pseudocode:**
```java
Algorithm: Calculate Final Grades
1. Display "=== Grade Book Calculator ==="
2. Display "Enter number of students: "
3. Get numStudents from user
4. Display "Enter number of assignments: "
5. Get numAssignments from user
6. Initialize grades 2D array (numStudents × numAssignments)
7. Initialize studentNames array (size numStudents)
8. For student from 0 to numStudents - 1:
   a. Display "Enter name for student " + (student + 1) + ": "
   b. Get studentNames[student] from user
   c. Initialize studentTotal to 0
   d. For assignment from 0 to numAssignments - 1:
      i. Display "Enter grade for " + studentNames[student] + " assignment " + (assignment + 1) + ": "
      ii. Get grade from user
      iii. Store grade in grades[student][assignment]
      iv. Add grade to studentTotal
   e. Calculate studentAverage = studentTotal ÷ numAssignments
   f. Display studentNames[student] + "'s average: " + studentAverage
9. Display "=== Class Statistics ==="
10. Initialize classTotal to 0
11. Initialize highestAverage to 0
12. Initialize lowestAverage to 100
13. For student from 0 to numStudents - 1:
   a. Initialize studentTotal to 0
   b. For assignment from 0 to numAssignments - 1:
      i. Add grades[student][assignment] to studentTotal
   c. Calculate studentAverage = studentTotal ÷ numAssignments
   d. Add studentAverage to classTotal
   e. If studentAverage > highestAverage:
      i. Set highestAverage to studentAverage
   f. If studentAverage < lowestAverage:
      i. Set lowestAverage to studentAverage
14. Calculate classAverage = classTotal ÷ numStudents
15. Display "Class average: " + classAverage
16. Display "Highest student average: " + highestAverage
17. Display "Lowest student average: " + lowestAverage
18. Display "=== Grade Distribution ==="
19. Initialize gradeRanges array [0,0,0,0,0] (A, B, C, D, F)
20. For student from 0 to numStudents - 1:
   a. Calculate studentAverage as above
   b. If studentAverage >= 90:
      i. Add 1 to gradeRanges[0] (A)
   c. Else if studentAverage >= 80:
      i. Add 1 to gradeRanges[1] (B)
   d. Else if studentAverage >= 70:
      i. Add 1 to gradeRanges[2] (C)
   e. Else if studentAverage >= 60:
      i. Add 1 to gradeRanges[3] (D)
   f. Else:
      i. Add 1 to gradeRanges[4] (F)
21. Display "A grades: " + gradeRanges[0]
22. Display "B grades: " + gradeRanges[1]
23. Display "C grades: " + gradeRanges[2]
24. Display "D grades: " + gradeRanges[3]
25. Display "F grades: " + gradeRanges[4]
```java

**Loop Logic:**
- 2D array processing (nested loops)
- Multiple statistical calculations
- Grade distribution analysis
- Complex data aggregation

**Your Task:** Build a comprehensive grade book system.

---

## Algorithm 5: Password Generator

**Pseudocode:**
```java
Algorithm: Generate Secure Passwords
1. Display "=== Password Generator ==="
2. Display "Enter desired password length (8-20): "
3. Get passwordLength from user
4. While passwordLength < 8 or passwordLength > 20:
   a. Display " Length must be between 8-20 characters!"
   b. Display "Enter desired password length (8-20): "
   c. Get passwordLength from user
5. Display "Include uppercase letters? (y/n): "
6. Get includeUpper from user
7. Display "Include numbers? (y/n): "
8. Get includeNumbers from user
9. Display "Include special characters? (y/n): "
10. Get includeSpecial from user
11. Initialize characterSets as empty list
12. Add "abcdefghijklmnopqrstuvwxyz" to characterSets (lowercase always included)
13. If includeUpper is "y":
   a. Add "ABCDEFGHIJKLMNOPQRSTUVWXYZ" to characterSets
14. If includeNumbers is "y":
   a. Add "0123456789" to characterSets
15. If includeSpecial is "y":
   a. Add "!@#$%^&*()_+-=[]{}|;:,.<>?" to characterSets
16. Initialize password as empty string
17. For position from 1 to passwordLength:
   a. Randomly select one character set from characterSets
   b. Randomly select one character from selected set
   c. Append character to password
18. Display "Generated Password: " + password
19. Display "Password length: " + passwordLength
20. Display "Character sets used:"
21. If includeUpper is "y":
   a. Display " Uppercase letters"
22. If includeNumbers is "y":
   a. Display " Numbers"
23. If includeSpecial is "y":
   a. Display " Special characters"
24. Display " Lowercase letters (always included)"
```java

**Loop Logic:**
- Input validation loop
- Character set configuration
- Password generation loop
- Random character selection

**Your Task:** Create a customizable password generator.

---

## Algorithm 6: Voting System

**Pseudocode:**
```java
Algorithm: Conduct Election Voting
1. Display "=== Election Voting System ==="
2. Initialize candidateNames array ["Alice", "Bob", "Charlie"]
3. Initialize votes array [0, 0, 0] (one for each candidate)
4. Initialize totalVotes to 0
5. Initialize votingActive to true
6. While votingActive is true:
   a. Display "=== Vote Menu ==="
   b. Display "Candidates:"
   c. For i from 0 to 2:
      i. Display (i + 1) + ". " + candidateNames[i]
   d. Display "4. Show Results"
   e. Display "5. End Voting"
   f. Display "Enter your choice (1-5): "
   g. Get choice from user
   h. If choice >= 1 and choice <= 3:
      i. Add 1 to votes[choice - 1]
      ii. Add 1 to totalVotes
      iii. Display " Vote recorded for " + candidateNames[choice - 1]
   i. Else if choice is 4:
      i. Display "=== Current Results ==="
      ii. Display "Total votes: " + totalVotes
      iii. For i from 0 to 2:
         i. Calculate percentage = (votes[i] ÷ totalVotes) × 100
         ii. Display candidateNames[i] + ": " + votes[i] + " votes (" + percentage + "%)"
   j. Else if choice is 5:
      i. Set votingActive to false
   k. Else:
      i. Display " Invalid choice!"
7. If totalVotes > 0:
   a. Display "=== Final Election Results ==="
   b. Initialize winnerIndex to 0
   c. Initialize maxVotes to votes[0]
   d. For i from 1 to 2:
      i. If votes[i] > maxVotes:
         i. Set maxVotes to votes[i]
         ii. Set winnerIndex to i
   e. Display " Winner: " + candidateNames[winnerIndex] + " with " + maxVotes + " votes!"
   f. Display "Total votes cast: " + totalVotes
   g. For i from 0 to 2:
      i. Calculate percentage = (votes[i] ÷ totalVotes) × 100
      ii. Display candidateNames[i] + ": " + votes[i] + " votes (" + percentage + "%)"
8. Else:
   a. Display "No votes were cast."
```java

**Loop Logic:**
- Menu-driven voting interface
- Vote counting and storage
- Real-time results display
- Winner determination algorithm

**Your Task:** Build an election voting system.

---

### Loop Control Techniques

**Loop Termination Conditions:**
- **Counter-controlled**: Fixed number of iterations
- **Sentinel-controlled**: Special value ends input
- **Flag-controlled**: Boolean condition controls loop
- **User-controlled**: User chooses to continue/stop

**Loop Best Practices:**
- Initialize loop variables properly
- Update loop variables in each iteration
- Use meaningful variable names
- Avoid infinite loops
- Consider loop efficiency

---

### Success Checklist

**For Each Algorithm:**
- [ ] Implemented appropriate loop structures
- [ ] Used correct loop control variables
- [ ] Handled array indexing properly
- [ ] Included proper input validation
- [ ] Provided clear output formatting

**Loop Implementation:**
- [ ] Used for loops for counted iterations
- [ ] Used while loops for conditional repetition
- [ ] Implemented nested loops where needed
- [ ] Handled loop termination correctly

---

### Try This (Optional Challenges)

1. **Add Data Persistence**: Save/load data to files using PrintWriter/Scanner
2. **Enhanced Features**: Add sorting (Arrays.sort()), filtering, search
3. **Error Recovery**: Handle system errors gracefully with try-catch
4. **Performance Optimization**: Improve algorithm efficiency with early termination

---

## Loop Algorithm Patterns

### Accumulation Pattern
```java
Initialize total to 0
While getting values:
    Get nextValue
    Add nextValue to total
Display "Total: " + total
```java

### Counting Pattern
```java
Initialize count to 0
For each item:
    If item meets criteria:
        Add 1 to count
Display "Count: " + count
```java

### Search Pattern
```java
Initialize found to false
For each item in collection:
    If item matches target:
        Set found to true
        Store item location
        Break from loop
If found:
    Display "Found at location"
Else:
    Display "Not found"
```java

### Validation Pattern
```java
Initialize isValid to false
While not isValid:
    Get userInput
    If input meets criteria:
        Set isValid to true
    Else:
        Display error message
Process valid input
```java

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Sales Data Analyzer

```java
import java.util.Scanner;

public class SalesAnalyzer {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] sales = new double[30];
        int salesCount = 0;
        double totalSales = 0.0, highestSale = 0.0, lowestSale = 999999.0;
        
        System.out.println("=== Sales Data Analyzer ===");
        System.out.println("Enter daily sales (enter -1 to finish):");
        
        while (salesCount < 30) {
            System.out.print("Day " + (salesCount + 1) + ": $");
            double dailySale = scanner.nextDouble();
            
            if (dailySale == -1) {
                break;
            } else if (dailySale >= 0) {
                sales[salesCount] = dailySale;
                totalSales += dailySale;
                salesCount++;
                
                if (dailySale > highestSale) {
                    highestSale = dailySale;
                }
                if (dailySale < lowestSale) {
                    lowestSale = dailySale;
                }
            } else {
                System.out.println(" Invalid sale amount! Please enter positive number.");
            }
        }
        
        if (salesCount > 0) {
            double averageSale = totalSales / salesCount;
            
            System.out.println("\n=== Sales Summary ===");
            System.out.println("Total days: " + salesCount);
            System.out.printf("Total sales: $%.2f\n", totalSales);
            System.out.printf("Average daily sales: $%.2f\n", averageSale);
            System.out.printf("Highest sale: $%.2f\n", highestSale);
            System.out.printf("Lowest sale: $%.2f\n", lowestSale);
            
            System.out.println("\n=== Daily Breakdown ===");
            for (int i = 0; i < salesCount; i++) {
                System.out.printf("Day %d: $%.2f\n", i + 1, sales[i]);
            }
        } else {
            System.out.println("No sales data entered.");
        }
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Array storage for sales data
- Loop with sentinel value (-1) for termination using break
- Statistical calculations with accumulation
- Input validation and error handling

**Variable Analysis:**
- `sales` (double[]): Array storing up to 30 daily sales
- `salesCount` (int): Tracks number of entries (logical size)
- `totalSales` (double): Accumulator for sum
- `highestSale`, `lowestSale` (double): Track extremes

**Java-Specific Notes:**
- break statement exits loop immediately
- Initialize lowestSale to large value (999999) to ensure first entry replaces it
- Use salesCount (not array.length) for iteration

---

### Algorithm 2: Student Attendance Tracker

```java
import java.util.Scanner;

public class AttendanceTracker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numStudents, presentCount = 0;
        
        System.out.println("=== Class Attendance Tracker ===");
        System.out.print("Enter number of students: ");
        numStudents = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        
        boolean[] attendance = new boolean[numStudents];
        
        for (int student = 1; student <= numStudents; student++) {
            System.out.print("Student " + student + " present? (y/n): ");
            String attendanceStatus = scanner.nextLine();
            
            if (attendanceStatus.equalsIgnoreCase("y")) {
                attendance[student - 1] = true;
                presentCount++;
            } else {
                attendance[student - 1] = false;
            }
        }
        
        double attendancePercentage = (double) presentCount / numStudents * 100;
        
        System.out.println("\n=== Attendance Report ===");
        System.out.println("Total students: " + numStudents);
        System.out.println("Present: " + presentCount);
        System.out.println("Absent: " + (numStudents - presentCount));
        System.out.printf("Attendance rate: %.1f%%\n", attendancePercentage);
        
        if (attendancePercentage >= 90) {
            System.out.println(" Excellent attendance!");
        } else if (attendancePercentage >= 75) {
            System.out.println(" Satisfactory attendance");
        } else {
            System.out.println(" Poor attendance - follow up required");
        }
        
        System.out.println("\n=== Individual Status ===");
        for (int student = 1; student <= numStudents; student++) {
            if (attendance[student - 1]) {
                System.out.println("Student " + student + ":  Present");
            } else {
                System.out.println("Student " + student + ":  Absent");
            }
        }
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Fixed iteration for known number of students (for loop)
- boolean array for attendance data (true/false)
- Percentage calculations with cast
- Individual status reporting

**Variable Analysis:**
- `attendance` (boolean[]): Array storing presence (true) or absence (false)
- `presentCount` (int): Counter for students present
- `attendancePercentage` (double): Calculated percentage

**Java-Specific Notes:**
- boolean array more natural than int (0/1) for true/false data
- Cast to double for percentage: `(double) presentCount / numStudents * 100`
- Loop from 1 to numStudents (inclusive) but array indices 0 to numStudents-1

---

### Algorithm 3: Inventory Management System

```java
import java.util.Scanner;

public class InventoryManager {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] itemNames = new String[50];
        int[] itemQuantities = new int[50];
        int itemCount = 0;
        boolean isRunning = true;
        int choice;
        
        System.out.println("=== Inventory Management System ===");
        
        while (isRunning) {
            System.out.println("\n1. Add Item");
            System.out.println("2. Update Quantity");
            System.out.println("3. Display Inventory");
            System.out.println("4. Find Low Stock Items");
            System.out.println("5. Exit");
            System.out.print("Choose option (1-5): ");
            choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline
            
            switch (choice) {
                case 1: {
                    if (itemCount < 50) {
                        System.out.print("Enter item name: ");
                        String newItemName = scanner.nextLine();
                        System.out.print("Enter initial quantity: ");
                        int newQuantity = scanner.nextInt();
                        scanner.nextLine(); // Consume newline
                        
                        if (newQuantity >= 0) {
                            itemNames[itemCount] = newItemName;
                            itemQuantities[itemCount] = newQuantity;
                            itemCount++;
                            System.out.println(" Item added successfully!");
                        } else {
                            System.out.println(" Invalid quantity!");
                        }
                    } else {
                        System.out.println(" Inventory is full!");
                    }
                    break;
                }
                case 2: {
                    if (itemCount > 0) {
                        System.out.print("Enter item name to update: ");
                        String searchName = scanner.nextLine();
                        
                        boolean found = false;
                        for (int i = 0; i < itemCount; i++) {
                            if (itemNames[i].equalsIgnoreCase(searchName)) {
                                System.out.println("Current quantity: " + itemQuantities[i]);
                                System.out.print("Enter new quantity: ");
                                int newQuantity = scanner.nextInt();
                                scanner.nextLine(); // Consume newline
                                
                                if (newQuantity >= 0) {
                                    itemQuantities[i] = newQuantity;
                                    System.out.println(" Quantity updated!");
                                    found = true;
                                } else {
                                    System.out.println(" Invalid quantity!");
                                }
                                break;
                            }
                        }
                        
                        if (!found) {
                            System.out.println(" Item not found!");
                        }
                    } else {
                        System.out.println("ℹ No items in inventory.");
                    }
                    break;
                }
                case 3:
                    if (itemCount > 0) {
                        System.out.println("=== Current Inventory ===");
                        for (int i = 0; i < itemCount; i++) {
                            System.out.println(itemNames[i] + ": " + itemQuantities[i] + " units");
                        }
                    } else {
                        System.out.println("ℹ Inventory is empty.");
                    }
                    break;
                case 4:
                    if (itemCount > 0) {
                        System.out.println("=== Low Stock Alert (≤5 units) ===");
                        int lowStockCount = 0;
                        
                        for (int i = 0; i < itemCount; i++) {
                            if (itemQuantities[i] <= 5) {
                                System.out.println(itemNames[i] + ": " + itemQuantities[i] + " units ");
                                lowStockCount++;
                            }
                        }
                        
                        if (lowStockCount == 0) {
                            System.out.println(" All items have sufficient stock.");
                        }
                    } else {
                        System.out.println("ℹ No items to check.");
                    }
                    break;
                case 5:
                    isRunning = false;
                    break;
                default:
                    System.out.println(" Invalid choice!");
                    break;
            }
        }
        
        System.out.println("Thank you for using Inventory Management System! ");
        scanner.close();
    }
}
```java

**Key Concepts:**
- Parallel arrays (itemNames and itemQuantities at same indices)
- Array search with linear scan
- Menu-driven interface with switch
- Inventory monitoring and alerts

**Variable Analysis:**
- `itemNames` (String[]): Stores item names
- `itemQuantities` (int[]): Stores corresponding quantities
- `itemCount` (int): Logical size (items actually stored)
- `found` (boolean): Flag for search result

**Java-Specific Notes:**
- Two separate arrays instead of 2D array (simpler for this case)
- equalsIgnoreCase() for case-insensitive search
- break statement in search loop for early termination
- Scanner buffer management after nextInt()

---

### Algorithm 4: Grade Book Calculator

```java
import java.util.Scanner;

public class GradeBook {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numStudents, numAssignments;
        
        System.out.println("=== Grade Book Calculator ===");
        System.out.print("Enter number of students: ");
        numStudents = scanner.nextInt();
        System.out.print("Enter number of assignments: ");
        numAssignments = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        
        String[] studentNames = new String[numStudents];
        double[][] grades = new double[numStudents][numAssignments];
        
        // Input student data
        for (int student = 0; student < numStudents; student++) {
            System.out.print("Enter name for student " + (student + 1) + ": ");
            studentNames[student] = scanner.nextLine();
            
            double studentTotal = 0.0;
            for (int assignment = 0; assignment < numAssignments; assignment++) {
                System.out.print("Enter grade for " + studentNames[student] + 
                               " assignment " + (assignment + 1) + ": ");
                grades[student][assignment] = scanner.nextDouble();
                studentTotal += grades[student][assignment];
            }
            scanner.nextLine(); // Consume newline after grades
            
            double studentAverage = studentTotal / numAssignments;
            System.out.printf("%s's average: %.1f\n", studentNames[student], studentAverage);
        }
        
        // Calculate class statistics
        System.out.println("\n=== Class Statistics ===");
        double classTotal = 0.0;
        double highestAverage = 0.0;
        double lowestAverage = 100.0;
        
        for (int student = 0; student < numStudents; student++) {
            double studentTotal = 0.0;
            for (int assignment = 0; assignment < numAssignments; assignment++) {
                studentTotal += grades[student][assignment];
            }
            
            double studentAverage = studentTotal / numAssignments;
            classTotal += studentAverage;
            
            if (studentAverage > highestAverage) {
                highestAverage = studentAverage;
            }
            if (studentAverage < lowestAverage) {
                lowestAverage = studentAverage;
            }
        }
        
        double classAverage = classTotal / numStudents;
        System.out.printf("Class average: %.1f\n", classAverage);
        System.out.printf("Highest student average: %.1f\n", highestAverage);
        System.out.printf("Lowest student average: %.1f\n", lowestAverage);
        
        // Grade distribution
        System.out.println("\n=== Grade Distribution ===");
        int[] gradeRanges = new int[5]; // A, B, C, D, F
        
        for (int student = 0; student < numStudents; student++) {
            double studentTotal = 0.0;
            for (int assignment = 0; assignment < numAssignments; assignment++) {
                studentTotal += grades[student][assignment];
            }
            
            double studentAverage = studentTotal / numAssignments;
            
            if (studentAverage >= 90) gradeRanges[0]++;
            else if (studentAverage >= 80) gradeRanges[1]++;
            else if (studentAverage >= 70) gradeRanges[2]++;
            else if (studentAverage >= 60) gradeRanges[3]++;
            else gradeRanges[4]++;
        }
        
        System.out.println("A grades: " + gradeRanges[0]);
        System.out.println("B grades: " + gradeRanges[1]);
        System.out.println("C grades: " + gradeRanges[2]);
        System.out.println("D grades: " + gradeRanges[3]);
        System.out.println("F grades: " + gradeRanges[4]);
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- 2D array processing with nested loops (rows=students, cols=assignments)
- Multiple statistical calculations
- Grade distribution analysis with frequency counting
- Complex data aggregation

**Variable Analysis:**
- `grades` (double[][]): 2D array storing all grades
- `studentNames` (String[]): Parallel array for names
- `gradeRanges` (int[]): Frequency array for A/B/C/D/F counts
- `studentTotal`, `classTotal` (double): Accumulators at different levels

**Java-Specific Notes:**
- 2D array declaration: `double[][] grades = new double[numStudents][numAssignments]`
- Access with grades[student][assignment]
- Nested loops: outer for students, inner for assignments
- Calculate average multiple times (not optimal but clearer)

**Common Mistakes:**
- Forgetting to consume newline after nextInt() before nextLine()
- Mixing up row/column indices
- Off-by-one errors with array bounds

---

### Algorithm 5: Password Generator

```java
import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;

public class PasswordGenerator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        int passwordLength;
        
        System.out.println("=== Password Generator ===");
        System.out.print("Enter desired password length (8-20): ");
        passwordLength = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        
        while (passwordLength < 8 || passwordLength > 20) {
            System.out.println(" Length must be between 8-20 characters!");
            System.out.print("Enter desired password length (8-20): ");
            passwordLength = scanner.nextInt();
            scanner.nextLine();
        }
        
        System.out.print("Include uppercase letters? (y/n): ");
        String includeUpper = scanner.nextLine();
        System.out.print("Include numbers? (y/n): ");
        String includeNumbers = scanner.nextLine();
        System.out.print("Include special characters? (y/n): ");
        String includeSpecial = scanner.nextLine();
        
        // Character sets
        String lowercase = "abcdefghijklmnopqrstuvwxyz";
        String uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String numbers = "0123456789";
        String special = "!@#$%^&*()_+-=[]{}|;:,.<>?";
        
        // Build available character sets
        ArrayList<String> charSets = new ArrayList<>();
        charSets.add(lowercase); // Always include lowercase
        
        if (includeUpper.equalsIgnoreCase("y")) {
            charSets.add(uppercase);
        }
        if (includeNumbers.equalsIgnoreCase("y")) {
            charSets.add(numbers);
        }
        if (includeSpecial.equalsIgnoreCase("y")) {
            charSets.add(special);
        }
        
        // Generate password
        StringBuilder password = new StringBuilder();
        for (int i = 0; i < passwordLength; i++) {
            // Pick random character set
            int setIndex = random.nextInt(charSets.size());
            String selectedSet = charSets.get(setIndex);
            
            // Pick random character from set
            int charIndex = random.nextInt(selectedSet.length());
            password.append(selectedSet.charAt(charIndex));
        }
        
        System.out.println("Generated Password: " + password.toString());
        System.out.println("Password length: " + passwordLength);
        System.out.println("Character sets used:");
        if (includeUpper.equalsIgnoreCase("y")) {
            System.out.println(" Uppercase letters");
        }
        if (includeNumbers.equalsIgnoreCase("y")) {
            System.out.println(" Numbers");
        }
        if (includeSpecial.equalsIgnoreCase("y")) {
            System.out.println(" Special characters");
        }
        System.out.println(" Lowercase letters (always included)");
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Input validation loop (while with compound condition)
- Character set configuration with ArrayList
- Random number generation with Random class
- String building with StringBuilder

**Variable Analysis:**
- `charSets` (ArrayList<String>): Dynamic list of character sets to use
- `password` (StringBuilder): Efficient string building
- `random` (Random): Random number generator
- Character set strings: immutable String constants

**Java-Specific Notes:**
- ArrayList for dynamic collection (don't know size in advance)
- Random class: `random.nextInt(n)` returns 0 to n-1
- StringBuilder for efficient string concatenation in loop
- String.charAt(index) to get character at position

**Common Mistakes:**
- Using String concatenation in loop (inefficient, use StringBuilder)
- Not seeding random properly (Random() uses current time automatically)
- Off-by-one with random.nextInt() - it returns 0 to n-1, not 1 to n

---

### Algorithm 6: Voting System

```java
import java.util.Scanner;

public class VotingSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] candidateNames = {"Alice", "Bob", "Charlie"};
        int[] votes = {0, 0, 0};
        int totalVotes = 0;
        boolean votingActive = true;
        int choice;
        
        System.out.println("=== Election Voting System ===");
        
        while (votingActive) {
            System.out.println("\n=== Vote Menu ===");
            System.out.println("Candidates:");
            for (int i = 0; i < 3; i++) {
                System.out.println((i + 1) + ". " + candidateNames[i]);
            }
            System.out.println("4. Show Results");
            System.out.println("5. End Voting");
            System.out.print("Enter your choice (1-5): ");
            choice = scanner.nextInt();
            
            if (choice >= 1 && choice <= 3) {
                votes[choice - 1]++;
                totalVotes++;
                System.out.println(" Vote recorded for " + candidateNames[choice - 1]);
            } else if (choice == 4) {
                System.out.println("=== Current Results ===");
                System.out.println("Total votes: " + totalVotes);
                
                if (totalVotes > 0) {
                    for (int i = 0; i < 3; i++) {
                        double percentage = (double) votes[i] / totalVotes * 100;
                        System.out.printf("%s: %d votes (%.1f%%)\n", 
                                        candidateNames[i], votes[i], percentage);
                    }
                } else {
                    System.out.println("No votes cast yet.");
                }
            } else if (choice == 5) {
                votingActive = false;
            } else {
                System.out.println(" Invalid choice!");
            }
        }
        
        if (totalVotes > 0) {
            System.out.println("\n=== Final Election Results ===");
            
            // Find winner
            int winnerIndex = 0;
            int maxVotes = votes[0];
            
            for (int i = 1; i < 3; i++) {
                if (votes[i] > maxVotes) {
                    maxVotes = votes[i];
                    winnerIndex = i;
                }
            }
            
            System.out.println(" Winner: " + candidateNames[winnerIndex] + 
                             " with " + maxVotes + " votes!");
            System.out.println("Total votes cast: " + totalVotes);
            
            for (int i = 0; i < 3; i++) {
                double percentage = (double) votes[i] / totalVotes * 100;
                System.out.printf("%s: %d votes (%.1f%%)\n", 
                                candidateNames[i], votes[i], percentage);
            }
        } else {
            System.out.println("No votes were cast.");
        }
        
        scanner.close();
    }
}
```java

**Key Concepts:**
- Menu-driven voting interface with while loop
- Vote counting and storage in parallel arrays
- Real-time results display
- Winner determination algorithm (max-finding)

**Variable Analysis:**
- `candidateNames` (String[]): Fixed array of candidates
- `votes` (int[]): Parallel array tracking votes per candidate
- `totalVotes` (int): Total votes cast (sum of votes array)
- `winnerIndex` (int): Index of winning candidate

**Java-Specific Notes:**
- Array initialization with values: `{"Alice", "Bob", "Charlie"}`
- Cast for percentage: `(double) votes[i] / totalVotes * 100`
- Max-finding pattern: assume first is max, then scan rest
- Check totalVotes > 0 before calculating percentages (avoid division by zero)

**Common Mistakes:**
- Integer division for percentage (cast to double)
- Off-by-one: menu shows 1-3, array uses 0-2
- Not checking for zero votes before division

---

### Loop Efficiency Considerations in Java

**Array Processing:**
```java
// Efficient - single pass
for (int i = 0; i < size; i++) {
    total += array[i];
    if (array[i] > max) max = array[i];
}

// Less efficient - multiple passes
for (int i = 0; i < size; i++) {
    total += array[i];
}
for (int i = 0; i < size; i++) {
    if (array[i] > max) max = array[i];
}
```java

**Early Termination:**
```java
// Good - stop when found
for (int i = 0; i < size; i++) {
    if (array[i] == target) {
        found = true;
        break; // Don't continue searching
    }
}
```java

**Enhanced For Loop:**
```java
// For iteration (no index needed)
for (String name : studentNames) {
    System.out.println(name);
}

// Traditional for loop (when index needed)
for (int i = 0; i < studentNames.length; i++) {
    System.out.println((i + 1) + ". " + studentNames[i]);
}
```java

---

 **Fantastic! You've mastered loop-based algorithms!** 

*Loops are the engines of computation. Next: Function pseudocode for modular programming! *
