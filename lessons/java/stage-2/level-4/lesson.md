# Level 4: Input/Output Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (`Main.java` or similar). The lesson stays on the **left** for reference. Press `Ctrl+l` to switch to your code window, or `<Space>h` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

User interaction is the heart of useful programs! Today you'll master the art of getting information from users and presenting results beautifully. You'll learn input validation, menu systems, formatted output, and creating user-friendly programs with Java's Scanner class.

---

### Learning Goals

- Implement robust input validation
- Create user-friendly menu systems
- Format output for better readability
- Handle input errors gracefully
- Design intuitive user interfaces
- Create interactive program flows

---

### Your Task

**Translate each interactive pseudocode algorithm into working Java code with excellent user experience.**

---


### How to Compile and Run

1. **Compile the code**:
   ```
   javac hello.java
   ```

2. **Run your program**:
   ```
   java hello
   ```

**Expected output:**
```
Hello, World!
```

## Algorithm 1: Age Verification System

**Pseudocode:**
```
Algorithm: Verify User Age
1. Display "=== Age Verification System ==="
2. Initialize isValidAge to false
3. While isValidAge is false:
   a. Display "Please enter your age (0-120): "
   b. Get ageInput from user
   c. If ageInput is not a valid number:
      i. Display " Invalid input! Please enter a number."
   d. Else if ageInput < 0:
      i. Display " Age cannot be negative!"
   e. Else if ageInput > 120:
      i. Display " Age cannot be over 120!"
   f. Else:
      i. Set isValidAge to true
4. Display " Age verified: " + ageInput + " years old"
5. If ageInput >= 18:
   a. Display " You are an adult!"
6. Else:
   a. Display " You are a minor."
```

**Input/Output Focus:**
- Input validation (numeric, range checking)
- Error messages with emojis
- Success confirmation
- Conditional output based on age

**Your Task:** Create a robust age verification system.

---

## Algorithm 2: Restaurant Menu System

**Pseudocode:**
```
Algorithm: Restaurant Ordering System
1. Display "=== Welcome to Code Café ==="
2. Initialize totalCost to 0
3. Initialize orderComplete to false
4. While orderComplete is false:
   a. Display menu options:
      i. "1. Coffee - $3.50"
      ii. "2. Sandwich - $8.75"
      iii. "3. Salad - $6.25"
      iv. "4. Dessert - $4.00"
      v. "5. Complete Order"
   b. Display "Enter your choice (1-5): "
   c. Get choice from user
   d. If choice is 1:
      i. Add 3.50 to totalCost
      ii. Display " Coffee added to your order!"
   e. Else if choice is 2:
      i. Add 8.75 to totalCost
      ii. Display " Sandwich added to your order!"
   f. Else if choice is 3:
      i. Add 6.25 to totalCost
      ii. Display " Salad added to your order!"
   g. Else if choice is 4:
      i. Add 4.00 to totalCost
      ii. Display " Dessert added to your order!"
   h. Else if choice is 5:
      i. Set orderComplete to true
   i. Else:
      i. Display " Invalid choice! Please select 1-5."
5. Display "=== Order Summary ==="
6. Display "Total cost: $" + totalCost
7. Calculate tax = totalCost × 0.08
8. Calculate finalTotal = totalCost + tax
9. Display "Tax (8%): $" + tax
10. Display "Final total: $" + finalTotal
11. Display "Thank you for your order! "
```

**Input/Output Focus:**
- Clear menu formatting
- Itemized feedback for each choice
- Professional order summary
- Currency formatting

**Your Task:** Build an interactive restaurant ordering system.

---

## Algorithm 3: Student Grade Manager

**Pseudocode:**
```
Algorithm: Student Grade Management
1. Display "=== Student Grade Manager ==="
2. Initialize grades array (can hold 100 grades)
3. Initialize gradeCount to 0
4. Initialize isRunning to true
5. While isRunning is true:
   a. Display menu:
      i. "1. Add Grade"
      ii. "2. View All Grades"
      iii. "3. Calculate Average"
      iv. "4. Find Highest/Lowest"
      v. "5. Exit"
   b. Display "Choose an option (1-5): "
   c. Get choice from user
   d. If choice is 1:
      i. If gradeCount < 100:
         i. Display "Enter grade (0-100): "
         ii. Get newGrade from user
         iii. If newGrade is valid (0-100):
            i. Store newGrade in grades array
            ii. Add 1 to gradeCount
            iii. Display " Grade added: " + newGrade
         iv. Else:
            i. Display " Invalid grade! Must be 0-100."
      ii. Else:
         i. Display " Grade book is full!"
   e. Else if choice is 2:
      i. If gradeCount > 0:
         i. Display "=== All Grades ==="
         ii. For each grade in grades array:
            i. Display grade
      ii. Else:
         i. Display "ℹ No grades entered yet."
   f. Else if choice is 3:
      i. If gradeCount > 0:
         i. Initialize sum to 0
         ii. For each grade in grades array:
            i. Add grade to sum
         iii. Calculate average = sum ÷ gradeCount
         iv. Display " Average: " + average + "%"
      ii. Else:
         i. Display "ℹ No grades to average."
   g. Else if choice is 4:
      i. If gradeCount > 0:
         i. Initialize highest to first grade
         ii. Initialize lowest to first grade
         iii. For each remaining grade:
            i. If grade > highest: set highest to grade
            ii. If grade < lowest: set lowest to grade
         iv. Display "⬆ Highest: " + highest + "%"
         v. Display "⬇ Lowest: " + lowest + "%"
      ii. Else:
         i. Display "ℹ No grades to analyze."
   h. Else if choice is 5:
      i. Set isRunning to false
   i. Else:
      i. Display " Invalid choice! Please select 1-5."
6. Display "Thank you for using Grade Manager! "
```

**Input/Output Focus:**
- Array data storage
- Multiple menu operations
- Formatted data display
- Empty state handling

**Your Task:** Create a comprehensive grade management system.

---

## Algorithm 4: Unit Converter

**Pseudocode:**
```
Algorithm: Unit Conversion Calculator
1. Display "=== Unit Converter ==="
2. Initialize isRunning to true
3. While isRunning is true:
   a. Display conversion options:
      i. "1. Temperature (°F ↔ °C)"
      ii. "2. Length (Feet ↔ Meters)"
      iii. "3. Weight (Pounds ↔ Kilograms)"
      iv. "4. Exit"
   b. Display "Select conversion type (1-4): "
   c. Get conversionType from user
   d. If conversionType is 1:
      i. Display "1. °F to °C"
      ii. Display "2. °C to °F"
      iii. Display "Choose direction: "
      iv. Get direction from user
      v. Display "Enter temperature: "
      vi. Get value from user
      vii. If direction is 1:
         i. Calculate result = (value - 32) × 5 ÷ 9
         ii. Display value + "°F = " + result + "°C"
      viii. Else if direction is 2:
         i. Calculate result = (value × 9 ÷ 5) + 32
         ii. Display value + "°C = " + result + "°F"
   e. Else if conversionType is 2:
      i. Display "1. Feet to Meters"
      ii. Display "2. Meters to Feet"
      iii. Display "Choose direction: "
      iv. Get direction from user
      v. Display "Enter length: "
      vi. Get value from user
      vii. If direction is 1:
         i. Calculate result = value × 0.3048
         ii. Display value + " ft = " + result + " m"
      viii. Else if direction is 2:
         i. Calculate result = value ÷ 0.3048
         ii. Display value + " m = " + result + " ft"
   f. Else if conversionType is 3:
      i. Display "1. Pounds to Kilograms"
      ii. Display "2. Kilograms to Pounds"
      iii. Display "Choose direction: "
      iv. Get direction from user
      v. Display "Enter weight: "
      vi. Get value from user
      vii. If direction is 1:
         i. Calculate result = value × 0.4536
         ii. Display value + " lbs = " + result + " kg"
      viii. Else if direction is 2:
         i. Calculate result = value ÷ 0.4536
         ii. Display value + " kg = " + result + " lbs"
   g. Else if conversionType is 4:
      i. Set isRunning to false
   h. Else:
      i. Display " Invalid conversion type!"
4. Display "Thank you for using Unit Converter! "
```

**Input/Output Focus:**
- Nested menu systems
- Multiple conversion categories
- Bidirectional conversions
- Clear unit labeling

**Your Task:** Build a comprehensive unit conversion tool.

---

## Algorithm 5: Survey Data Collector

**Pseudocode:**
```
Algorithm: Customer Satisfaction Survey
1. Display "=== Customer Satisfaction Survey ==="
2. Initialize responses array (can hold 50 responses)
3. Initialize responseCount to 0
4. Initialize surveyComplete to false
5. While surveyComplete is false:
   a. Display "Participant #" + (responseCount + 1)
   b. Display "Rate your satisfaction (1-5): "
   c. Display "1 = Very Dissatisfied"
   d. Display "2 = Dissatisfied"
   e. Display "3 = Neutral"
   f. Display "4 = Satisfied"
   g. Display "5 = Very Satisfied"
   h. Display "Enter rating (1-5, or 0 to finish survey): "
   i. Get rating from user
   j. If rating is 0:
      i. Set surveyComplete to true
   k. Else if rating is valid (1-5):
      i. Store rating in responses array
      ii. Add 1 to responseCount
      iii. Display " Thank you for your feedback!"
   l. Else:
      i. Display " Invalid rating! Please enter 1-5 or 0 to finish."
6. If responseCount > 0:
   a. Display "=== Survey Results ==="
   b. Display "Total responses: " + responseCount
   c. Initialize count array for ratings 1-5 (all start at 0)
   d. For each response in responses array:
      i. Add 1 to count[response]
   e. For rating from 1 to 5:
      i. Calculate percentage = (count[rating] ÷ responseCount) × 100
      ii. Display rating + ": " + count[rating] + " responses (" + percentage + "%)"
   f. Calculate average = sum of all responses ÷ responseCount
   g. Display "Average satisfaction: " + average + "/5.0"
7. Else:
   a. Display "No survey responses collected."
8. Display "Thank you for participating! "
```

**Input/Output Focus:**
- Clear survey instructions
- Rating scale explanation
- Statistical analysis output
- Percentage calculations

**Your Task:** Create an interactive survey system with analysis.

---

## Algorithm 6: Library Book Tracker

**Pseudocode:**
```
Algorithm: Library Book Management
1. Display "=== Library Book Tracker ==="
2. Initialize books array (can hold 20 book titles)
3. Initialize bookCount to 0
4. Initialize isRunning to true
5. While isRunning is true:
   a. Display menu:
      i. "1. Add Book"
      ii. "2. List All Books"
      iii. "3. Search Books"
      iv. "4. Remove Book"
      v. "5. Exit"
   b. Display "Choose option (1-5): "
   c. Get choice from user
   d. If choice is 1:
      i. If bookCount < 20:
         i. Display "Enter book title: "
         ii. Get bookTitle from user
         iii. If bookTitle is not empty:
            i. Store bookTitle in books array
            ii. Add 1 to bookCount
            iii. Display " Book added: '" + bookTitle + "'"
         iv. Else:
            i. Display " Book title cannot be empty!"
      ii. Else:
         i. Display " Library is full!"
   e. Else if choice is 2:
      i. If bookCount > 0:
         i. Display "=== Library Collection ==="
         ii. For i from 1 to bookCount:
            i. Display i + ". " + books[i-1]
      ii. Else:
         i. Display "ℹ No books in library yet."
   f. Else if choice is 3:
      i. If bookCount > 0:
         i. Display "Enter search term: "
         ii. Get searchTerm from user
         iii. Initialize foundCount to 0
         iv. For each book in books array:
            i. If book contains searchTerm:
               i. Display " " + book
               ii. Add 1 to foundCount
         v. If foundCount is 0:
            i. Display "ℹ No books found matching '" + searchTerm + "'"
      ii. Else:
         i. Display "ℹ No books to search."
   g. Else if choice is 4:
      i. If bookCount > 0:
         i. Display "Enter book number to remove (1-" + bookCount + "): "
         ii. Get bookNumber from user
         iii. If bookNumber is valid (1 to bookCount):
            i. Display "Removing: '" + books[bookNumber-1] + "'"
            ii. Shift remaining books left in array
            iii. Subtract 1 from bookCount
            iv. Display " Book removed successfully!"
         iv. Else:
            i. Display " Invalid book number!"
      ii. Else:
         i. Display "ℹ No books to remove."
   h. Else if choice is 5:
      i. Set isRunning to false
   i. Else:
      i. Display " Invalid choice!"
6. Display "Thank you for using Library Book Tracker! "
```

**Input/Output Focus:**
- String array management
- Search functionality
- Numbered list display
- Array manipulation (removal)

**Your Task:** Build a library book management system.

---

### Input Validation Techniques

**Numeric Input Validation:**
```
// Check if input is within range
if (input >= minValue && input <= maxValue) {
    // Valid input
} else {
    // Invalid input - show error
}
```

**String Input Validation:**
```
// Check if string is not empty
if (!inputString.isEmpty()) {
    // Valid input
} else {
    // Empty input - show error
}
```

**Scanner Exception Handling:**
```
Scanner scanner = new Scanner(System.in);

try {
    int value = scanner.nextInt();
    // Process valid integer
} catch (InputMismatchException e) {
    scanner.nextLine(); // Clear invalid input
    System.out.println("Invalid input! Please enter a number.");
}
```

---

### Success Checklist

**For Each Algorithm:**
- [ ] Implemented robust input validation
- [ ] Created user-friendly menus
- [ ] Provided clear error messages
- [ ] Formatted output professionally
- [ ] Handled edge cases (empty data, invalid inputs)
- [ ] Used appropriate data structures (arrays, variables)

**User Experience:**
- [ ] Clear instructions for users
- [ ] Consistent formatting
- [ ] Helpful error messages
- [ ] Confirmation of successful operations
- [ ] Graceful program termination

---

### Try This (Optional Challenges)

1. **Enhanced Validation**: Add more sophisticated input checking with try-catch
2. **Data Persistence**: Save/load data to files using PrintWriter/BufferedReader
3. **Advanced Features**: Add sorting (Arrays.sort()), filtering, statistics
4. **Multi-user Support**: Handle multiple users/sessions with collections

---

## User Interface Design Principles

### Clear Menu Design
```
=== Main Menu ===
1. Add Item      - Add new item to collection
2. View Items    - Display all items
3. Search Items  - Find specific items
4. Remove Item   - Delete an item
5. Exit          - Quit the program

Enter choice (1-5):
```

### Error Message Best Practices
- **Be specific**: "Grade must be between 0-100" not "Invalid input"
- **Be helpful**: Suggest correct input format
- **Be consistent**: Use same error style throughout
- **Use emojis**:  for success,  for errors,  for warnings

### Input Prompt Guidelines
- **Be descriptive**: "Enter your age in years:"
- **Show format**: "Enter date (MM/DD/YYYY):"
- **Indicate ranges**: "Enter rating (1-5):"
- **Show defaults**: "Enter timeout [30 seconds]:"

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Age Verification System

```
import java.util.Scanner;
import java.util.InputMismatchException;

public class AgeVerification {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int ageInput = 0;
        boolean isValidAge = false;
        
        System.out.println("=== Age Verification System ===");
        
        while (!isValidAge) {
            System.out.print("Please enter your age (0-120): ");
            
            try {
                ageInput = scanner.nextInt();
                
                if (ageInput < 0) {
                    System.out.println(" Age cannot be negative!");
                } else if (ageInput > 120) {
                    System.out.println(" Age cannot be over 120!");
                } else {
                    isValidAge = true;
                }
            } catch (InputMismatchException e) {
                scanner.nextLine(); // Clear invalid input
                System.out.println(" Invalid input! Please enter a number.");
            }
        }
        
        System.out.println(" Age verified: " + ageInput + " years old");
        
        if (ageInput >= 18) {
            System.out.println(" You are an adult!");
        } else {
            System.out.println(" You are a minor.");
        }
        
        scanner.close();
    }
}
```

**Key Concepts:**
- Input validation with try-catch for InputMismatchException
- Clearing invalid input from Scanner buffer
- Boolean flag for validation state
- camelCase naming (isValidAge, ageInput)

**Variable Analysis:**
- `ageInput` (int): Stores user's age after validation
- `isValidAge` (boolean): Tracks whether input passed all checks
- `scanner` (Scanner): Input reader object

---

### Algorithm 2: Restaurant Menu System

```
import java.util.Scanner;

public class RestaurantMenu {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double totalCost = 0.0;
        boolean orderComplete = false;
        int choice;
        
        System.out.println("=== Welcome to Code Café ===");
        
        while (!orderComplete) {
            System.out.println("\n1. Coffee - $3.50");
            System.out.println("2. Sandwich - $8.75");
            System.out.println("3. Salad - $6.25");
            System.out.println("4. Dessert - $4.00");
            System.out.println("5. Complete Order");
            System.out.print("Enter your choice (1-5): ");
            choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    totalCost += 3.50;
                    System.out.println(" Coffee added to your order!");
                    break;
                case 2:
                    totalCost += 8.75;
                    System.out.println(" Sandwich added to your order!");
                    break;
                case 3:
                    totalCost += 6.25;
                    System.out.println(" Salad added to your order!");
                    break;
                case 4:
                    totalCost += 4.00;
                    System.out.println(" Dessert added to your order!");
                    break;
                case 5:
                    orderComplete = true;
                    break;
                default:
                    System.out.println(" Invalid choice! Please select 1-5.");
                    break;
            }
        }
        
        System.out.println("\n=== Order Summary ===");
        System.out.printf("Total cost: $%.2f\n", totalCost);
        
        double tax = totalCost * 0.08;
        double finalTotal = totalCost + tax;
        
        System.out.printf("Tax (8%%): $%.2f\n", tax);
        System.out.printf("Final total: $%.2f\n", finalTotal);
        System.out.println("Thank you for your order! ");
        
        scanner.close();
    }
}
```

**Key Concepts:**
- Switch statement for menu handling
- Accumulator pattern for total cost (+=)
- Professional receipt formatting with printf
- double for currency (not float, for precision)

**Variable Analysis:**
- `totalCost` (double): Running sum of all order items
- `orderComplete` (boolean): Loop control flag
- `choice` (int): User's menu selection
- `tax`, `finalTotal` (double): Calculated values

**Java-Specific Notes:**
- Use `printf("%.2f", value)` for 2 decimal places
- `%%` in printf escapes the % sign for "8%"
- Scanner.close() releases system resources

---

### Algorithm 3: Student Grade Manager

```
import java.util.Scanner;

public class GradeManager {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] grades = new double[100];
        int gradeCount = 0;
        boolean isRunning = true;
        int choice;
        
        System.out.println("=== Student Grade Manager ===");
        
        while (isRunning) {
            System.out.println("\n1. Add Grade");
            System.out.println("2. View All Grades");
            System.out.println("3. Calculate Average");
            System.out.println("4. Find Highest/Lowest");
            System.out.println("5. Exit");
            System.out.print("Choose an option (1-5): ");
            choice = scanner.nextInt();
            
            switch (choice) {
                case 1: {
                    if (gradeCount < 100) {
                        System.out.print("Enter grade (0-100): ");
                        double newGrade = scanner.nextDouble();
                        
                        if (newGrade >= 0 && newGrade <= 100) {
                            grades[gradeCount] = newGrade;
                            gradeCount++;
                            System.out.printf(" Grade added: %.1f\n", newGrade);
                        } else {
                            System.out.println(" Invalid grade! Must be 0-100.");
                        }
                    } else {
                        System.out.println(" Grade book is full!");
                    }
                    break;
                }
                case 2:
                    if (gradeCount > 0) {
                        System.out.println("=== All Grades ===");
                        for (int i = 0; i < gradeCount; i++) {
                            System.out.printf("%.1f\n", grades[i]);
                        }
                    } else {
                        System.out.println("ℹ No grades entered yet.");
                    }
                    break;
                case 3:
                    if (gradeCount > 0) {
                        double sum = 0;
                        for (int i = 0; i < gradeCount; i++) {
                            sum += grades[i];
                        }
                        double average = sum / gradeCount;
                        System.out.printf(" Average: %.1f%%\n", average);
                    } else {
                        System.out.println("ℹ No grades to average.");
                    }
                    break;
                case 4:
                    if (gradeCount > 0) {
                        double highest = grades[0];
                        double lowest = grades[0];
                        
                        for (int i = 1; i < gradeCount; i++) {
                            if (grades[i] > highest) highest = grades[i];
                            if (grades[i] < lowest) lowest = grades[i];
                        }
                        
                        System.out.printf("⬆ Highest: %.1f%%\n", highest);
                        System.out.printf("⬇ Lowest: %.1f%%\n", lowest);
                    } else {
                        System.out.println("ℹ No grades to analyze.");
                    }
                    break;
                case 5:
                    isRunning = false;
                    break;
                default:
                    System.out.println(" Invalid choice! Please select 1-5.");
                    break;
            }
        }
        
        System.out.println("Thank you for using Grade Manager! ");
        scanner.close();
    }
}
```

**Key Concepts:**
- Array storage for multiple grades
- Multiple menu operations with switch
- Statistical calculations on array data
- Empty state handling (gradeCount > 0 checks)
- Finding min/max with single loop

**Variable Analysis:**
- `grades` (double[]): Array storing up to 100 grade values
- `gradeCount` (int): Number of grades currently stored
- `isRunning` (boolean): Main loop control
- `sum`, `average`, `highest`, `lowest` (double): Calculation variables

**Java-Specific Notes:**
- Arrays have fixed size (100) declared at creation
- Use gradeCount to track logical size vs physical array size
- printf("%.1f", value) for 1 decimal place
- Empty blocks in switch need braces if declaring variables

---

### Algorithm 4: Unit Converter

```
import java.util.Scanner;

public class UnitConverter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean isRunning = true;
        int conversionType, direction;
        double value, result;
        
        System.out.println("=== Unit Converter ===");
        
        while (isRunning) {
            System.out.println("\n1. Temperature (°F ↔ °C)");
            System.out.println("2. Length (Feet ↔ Meters)");
            System.out.println("3. Weight (Pounds ↔ Kilograms)");
            System.out.println("4. Exit");
            System.out.print("Select conversion type (1-4): ");
            conversionType = scanner.nextInt();
            
            if (conversionType == 1) {
                System.out.println("1. °F to °C");
                System.out.println("2. °C to °F");
                System.out.print("Choose direction: ");
                direction = scanner.nextInt();
                System.out.print("Enter temperature: ");
                value = scanner.nextDouble();
                
                if (direction == 1) {
                    result = (value - 32) * 5 / 9;
                    System.out.printf("%.1f°F = %.1f°C\n", value, result);
                } else if (direction == 2) {
                    result = (value * 9 / 5) + 32;
                    System.out.printf("%.1f°C = %.1f°F\n", value, result);
                }
            } else if (conversionType == 2) {
                System.out.println("1. Feet to Meters");
                System.out.println("2. Meters to Feet");
                System.out.print("Choose direction: ");
                direction = scanner.nextInt();
                System.out.print("Enter length: ");
                value = scanner.nextDouble();
                
                if (direction == 1) {
                    result = value * 0.3048;
                    System.out.printf("%.2f ft = %.2f m\n", value, result);
                } else if (direction == 2) {
                    result = value / 0.3048;
                    System.out.printf("%.2f m = %.2f ft\n", value, result);
                }
            } else if (conversionType == 3) {
                System.out.println("1. Pounds to Kilograms");
                System.out.println("2. Kilograms to Pounds");
                System.out.print("Choose direction: ");
                direction = scanner.nextInt();
                System.out.print("Enter weight: ");
                value = scanner.nextDouble();
                
                if (direction == 1) {
                    result = value * 0.4536;
                    System.out.printf("%.2f lbs = %.2f kg\n", value, result);
                } else if (direction == 2) {
                    result = value / 0.4536;
                    System.out.printf("%.2f kg = %.2f lbs\n", value, result);
                }
            } else if (conversionType == 4) {
                isRunning = false;
            } else {
                System.out.println(" Invalid conversion type!");
            }
        }
        
        System.out.println("Thank you for using Unit Converter! ");
        scanner.close();
    }
}
```

**Key Concepts:**
- Nested menu system (two levels of choices)
- Multiple conversion formulas
- Bidirectional conversions (forward and reverse)
- Clear unit labeling in output

**Variable Analysis:**
- `conversionType` (int): Which category (temp/length/weight)
- `direction` (int): Which direction of conversion
- `value` (double): User input value to convert
- `result` (double): Converted result

**Java-Specific Notes:**
- Integer division avoided by using doubles: 5/9 would be 0, but 5.0/9.0 is correct
- printf for consistent decimal formatting
- if-else chains (could be switch, but direction is contextual)

---

### Algorithm 5: Survey Data Collector

```
import java.util.Scanner;

public class SurveyCollector {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] responses = new int[50];
        int responseCount = 0;
        boolean surveyComplete = false;
        int rating;
        
        System.out.println("=== Customer Satisfaction Survey ===");
        
        while (!surveyComplete) {
            System.out.println("\nParticipant #" + (responseCount + 1));
            System.out.println("Rate your satisfaction (1-5):");
            System.out.println("1 = Very Dissatisfied");
            System.out.println("2 = Dissatisfied");
            System.out.println("3 = Neutral");
            System.out.println("4 = Satisfied");
            System.out.println("5 = Very Satisfied");
            System.out.print("Enter rating (1-5, or 0 to finish survey): ");
            rating = scanner.nextInt();
            
            if (rating == 0) {
                surveyComplete = true;
            } else if (rating >= 1 && rating <= 5) {
                responses[responseCount] = rating;
                responseCount++;
                System.out.println(" Thank you for your feedback!");
            } else {
                System.out.println(" Invalid rating! Please enter 1-5 or 0 to finish.");
            }
        }
        
        if (responseCount > 0) {
            System.out.println("\n=== Survey Results ===");
            System.out.println("Total responses: " + responseCount);
            
            int[] counts = new int[6]; // Index 0-5, use 1-5 for ratings
            
            for (int i = 0; i < responseCount; i++) {
                counts[responses[i]]++;
            }
            
            for (int ratingLevel = 1; ratingLevel <= 5; ratingLevel++) {
                double percentage = (double) counts[ratingLevel] / responseCount * 100;
                System.out.printf("%d: %d responses (%.1f%%)\n", 
                    ratingLevel, counts[ratingLevel], percentage);
            }
            
            int sum = 0;
            for (int i = 0; i < responseCount; i++) {
                sum += responses[i];
            }
            double average = (double) sum / responseCount;
            
            System.out.printf("Average satisfaction: %.1f/5.0\n", average);
        } else {
            System.out.println("No survey responses collected.");
        }
        
        System.out.println("Thank you for participating! ");
        scanner.close();
    }
}
```

**Key Concepts:**
- Array storage for survey responses
- Statistical analysis (counts, percentages, averages)
- Clear survey interface with rating scale
- Comprehensive results display
- Frequency counting with array indexing

**Variable Analysis:**
- `responses` (int[]): Stores each participant's rating
- `responseCount` (int): Number of responses collected
- `counts` (int[]): Frequency array for each rating (1-5)
- `sum` (int): Total of all ratings for average calculation

**Java-Specific Notes:**
- Cast to double for percentage: `(double) counts[rating] / responseCount * 100`
- Size 6 array but use indices 1-5 (index 0 unused, simpler logic)
- printf for formatted percentage output

---

### Algorithm 6: Library Book Tracker

```
import java.util.Scanner;

public class LibraryTracker {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] books = new String[20];
        int bookCount = 0;
        boolean isRunning = true;
        int choice;
        
        System.out.println("=== Library Book Tracker ===");
        
        while (isRunning) {
            System.out.println("\n1. Add Book");
            System.out.println("2. List All Books");
            System.out.println("3. Search Books");
            System.out.println("4. Remove Book");
            System.out.println("5. Exit");
            System.out.print("Choose option (1-5): ");
            choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline after nextInt()
            
            switch (choice) {
                case 1: {
                    if (bookCount < 20) {
                        System.out.print("Enter book title: ");
                        String bookTitle = scanner.nextLine();
                        
                        if (!bookTitle.isEmpty()) {
                            books[bookCount] = bookTitle;
                            bookCount++;
                            System.out.println(" Book added: '" + bookTitle + "'");
                        } else {
                            System.out.println(" Book title cannot be empty!");
                        }
                    } else {
                        System.out.println(" Library is full!");
                    }
                    break;
                }
                case 2:
                    if (bookCount > 0) {
                        System.out.println("=== Library Collection ===");
                        for (int i = 0; i < bookCount; i++) {
                            System.out.println((i + 1) + ". " + books[i]);
                        }
                    } else {
                        System.out.println("ℹ No books in library yet.");
                    }
                    break;
                case 3: {
                    if (bookCount > 0) {
                        System.out.print("Enter search term: ");
                        String searchTerm = scanner.nextLine();
                        
                        int foundCount = 0;
                        for (int i = 0; i < bookCount; i++) {
                            if (books[i].toLowerCase().contains(searchTerm.toLowerCase())) {
                                System.out.println(" " + books[i]);
                                foundCount++;
                            }
                        }
                        
                        if (foundCount == 0) {
                            System.out.println("ℹ No books found matching '" + searchTerm + "'");
                        }
                    } else {
                        System.out.println("ℹ No books to search.");
                    }
                    break;
                }
                case 4: {
                    if (bookCount > 0) {
                        System.out.print("Enter book number to remove (1-" + bookCount + "): ");
                        int bookNumber = scanner.nextInt();
                        scanner.nextLine(); // Consume newline
                        
                        if (bookNumber >= 1 && bookNumber <= bookCount) {
                            System.out.println("Removing: '" + books[bookNumber - 1] + "'");
                            
                            // Shift remaining books left
                            for (int i = bookNumber - 1; i < bookCount - 1; i++) {
                                books[i] = books[i + 1];
                            }
                            
                            bookCount--;
                            System.out.println(" Book removed successfully!");
                        } else {
                            System.out.println(" Invalid book number!");
                        }
                    } else {
                        System.out.println("ℹ No books to remove.");
                    }
                    break;
                }
                case 5:
                    isRunning = false;
                    break;
                default:
                    System.out.println(" Invalid choice!");
                    break;
            }
        }
        
        System.out.println("Thank you for using Library Book Tracker! ");
        scanner.close();
    }
}
```

**Key Concepts:**
- String array management
- String search with contains()
- Numbered list display
- Array manipulation (removal with shifting)
- Scanner buffer management (nextInt then nextLine)

**Variable Analysis:**
- `books` (String[]): Array storing up to 20 book titles
- `bookCount` (int): Number of books currently stored
- `bookTitle`, `searchTerm` (String): User input strings

**Java-Specific Notes:**
- **CRITICAL**: `scanner.nextLine()` after `nextInt()` to consume leftover newline
- String.isEmpty() checks for empty strings
- String.contains() for substring search (case-sensitive)
- toLowerCase() on both strings for case-insensitive search
- Array shifting: copy each element left when removing

**Common Mistakes:**
- Forgetting to consume newline after nextInt() causes nextLine() to read empty string
- Not checking isEmpty() before adding to array
- Off-by-one errors with array indices (user sees 1-20, array uses 0-19)

---

### Advanced Input Techniques in Java

**Clearing Scanner Buffer:**
```
// After nextInt(), consume leftover newline
scanner.nextInt();
scanner.nextLine(); // Clears the '\n'
```

**Reading Full Lines Safely:**
```
String line = scanner.nextLine().trim(); // Remove leading/trailing whitespace
```

**Input Validation Patterns:**
```
// Numeric range validation with exception handling
public static int getValidNumber(Scanner scanner, int min, int max) {
    while (true) {
        try {
            System.out.printf("Enter number (%d-%d): ", min, max);
            int value = scanner.nextInt();
            scanner.nextLine(); // Clear buffer
            
            if (value >= min && value <= max) {
                return value;
            }
            System.out.println("Number must be between " + min + " and " + max);
        } catch (InputMismatchException e) {
            scanner.nextLine(); // Clear bad input
            System.out.println("Invalid input! Please enter a number.");
        }
    }
}
```

**Scanner vs BufferedReader:**
- Scanner: Easier for mixed types (nextInt, nextDouble, nextLine)
- BufferedReader: Faster for large input, returns only Strings

---

 **Excellent! You've mastered user interaction and I/O operations!** 

*Programs that talk to users are much more useful. Next: Decision-making in pseudocode! ��*
