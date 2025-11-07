# Level 6: Loop Pseudocode

> **LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.c\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Loops are the workhorses of programming! Today you'll master algorithms that use repetition, accumulation, and iteration to solve complex problems. You'll learn to think in terms of patterns, sequences, and repeated operations.

---

### Learning Goals

- [ ] Implement algorithms with counting and accumulation loops
- [ ] Create nested loop structures for complex patterns
- [ ] Use loops for data processing and validation
- [ ] Master loop control and termination conditions
- [ ] Develop iterative problem-solving approaches

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
- [ ] **Initialization**: Set starting values
- [ ] **Condition**: When to continue looping
- [ ] **Update**: Change values each iteration
- [ ] **Termination**: When to stop

---

### Your Task

**Translate each loop-based pseudocode algorithm into working C code.**

---

## Algorithm 1: Sales Data Analyzer

**Pseudocode:**
```
Algorithm: Analyze Monthly Sales Data
1. Display "=== Sales Data Analyzer ==="
2. Initialize sales array (can hold 30 values)
3. Initialize sales_count to 0
4. Initialize total_sales to 0
5. Initialize highest_sale to 0
6. Initialize lowest_sale to 999999
7. Display "Enter daily sales (enter -1 to finish):"
8. While sales_count < 30:
   a. Display "Day " + (sales_count + 1) + ": $"
   b. Get daily_sale from user
   c. If daily_sale equals -1:
      i. Break out of loop
   d. Else if daily_sale >= 0:
      i. Store daily_sale in sales array
      ii. Add daily_sale to total_sales
      iii. Add 1 to sales_count
      iv. If daily_sale > highest_sale:
         i. Set highest_sale to daily_sale
      v. If daily_sale < lowest_sale:
         i. Set lowest_sale to daily_sale
   e. Else:
      i. Display " Invalid sale amount! Please enter positive number."
9. If sales_count > 0:
   a. Calculate average_sale = total_sales ÷ sales_count
   b. Display "=== Sales Summary ==="
   c. Display "Total days: " + sales_count
   d. Display "Total sales: $" + total_sales
   e. Display "Average daily sales: $" + average_sale
   f. Display "Highest sale: $" + highest_sale
   g. Display "Lowest sale: $" + lowest_sale
   h. Display "=== Daily Breakdown ==="
   i. For i from 0 to sales_count - 1:
      i. Display "Day " + (i + 1) + ": $" + sales[i]
10. Else:
   a. Display "No sales data entered."
```

**Loop Logic:**
- [ ] Input loop with validation
- [ ] Accumulation of sales data
- [ ] Statistical calculations
- [ ] Array iteration for display

**Your Task:** Create a sales data analysis system.

---

## Algorithm 2: Student Attendance Tracker

**Pseudocode:**
```
Algorithm: Track Class Attendance
1. Display "=== Class Attendance Tracker ==="
2. Display "Enter number of students: "
3. Get num_students from user
4. Initialize attendance array (size num_students)
5. Initialize present_count to 0
6. For student from 1 to num_students:
   a. Display "Student " + student + " present? (y/n): "
   b. Get attendance_status from user
   c. If attendance_status is "y" or "Y":
      i. Set attendance[student-1] to true
      ii. Add 1 to present_count
   d. Else:
      i. Set attendance[student-1] to false
7. Calculate attendance_percentage = (present_count ÷ num_students) × 100
8. Display "=== Attendance Report ==="
9. Display "Total students: " + num_students
10. Display "Present: " + present_count
11. Display "Absent: " + (num_students - present_count)
12. Display "Attendance rate: " + attendance_percentage + "%"
13. If attendance_percentage >= 90:
   a. Display " Excellent attendance!"
14. Else if attendance_percentage >= 75:
   a. Display " Satisfactory attendance"
15. Else:
   a. Display " Poor attendance - follow up required"
16. Display "=== Individual Status ==="
17. For student from 1 to num_students:
   a. If attendance[student-1] is true:
      i. Display "Student " + student + ":  Present"
   b. Else:
      i. Display "Student " + student + ":  Absent"
```

**Loop Logic:**
- [ ] Fixed iteration for known number of students
- [ ] Array storage of attendance data
- [ ] Percentage calculations
- [ ] Conditional reporting based on attendance rate

**Your Task:** Build a class attendance tracking system.

---

## Algorithm 3: Inventory Management System

**Pseudocode:**
```
Algorithm: Manage Store Inventory
1. Display "=== Inventory Management System ==="
2. Initialize item_names array (can hold 50 items)
3. Initialize item_quantities array (size 50)
4. Initialize item_count to 0
5. Initialize is_running to true
6. While is_running is true:
   a. Display menu:
      i. "1. Add Item"
      ii. "2. Update Quantity"
      iii. "3. Display Inventory"
      iv. "4. Find Low Stock Items"
      v. "5. Exit"
   b. Display "Choose option (1-5): "
   c. Get choice from user
   d. If choice is 1:
      i. If item_count < 50:
         i. Display "Enter item name: "
         ii. Get new_item_name from user
         iii. Display "Enter initial quantity: "
         iv. Get new_quantity from user
         v. If new_quantity >= 0:
            i. Store new_item_name in item_names array
            ii. Store new_quantity in item_quantities array
            iii. Add 1 to item_count
            iv. Display " Item added successfully!"
         vi. Else:
            i. Display " Invalid quantity!"
      ii. Else:
         i. Display " Inventory is full!"
   e. Else if choice is 2:
      i. If item_count > 0:
         i. Display "Enter item name to update: "
         ii. Get search_name from user
         iii. Initialize found to false
         iv. For i from 0 to item_count - 1:
            i. If item_names[i] equals search_name:
               i. Display "Current quantity: " + item_quantities[i]
               ii. Display "Enter new quantity: "
               iii. Get new_quantity from user
               iv. If new_quantity >= 0:
                  i. Set item_quantities[i] to new_quantity
                  ii. Display " Quantity updated!"
                  iii. Set found to true
                  iv. Break out of loop
         v. If found is false:
            i. Display " Item not found!"
      ii. Else:
         i. Display " No items in inventory."
   f. Else if choice is 3:
      i. If item_count > 0:
         i. Display "=== Current Inventory ==="
         ii. For i from 0 to item_count - 1:
            i. Display item_names[i] + ": " + item_quantities[i] + " units"
      ii. Else:
         i. Display " Inventory is empty."
   g. Else if choice is 4:
      i. If item_count > 0:
         i. Display "=== Low Stock Alert (≤5 units) ==="
         ii. Initialize low_stock_count to 0
         iii. For i from 0 to item_count - 1:
            i. If item_quantities[i] <= 5:
               i. Display item_names[i] + ": " + item_quantities[i] + " units "
               ii. Add 1 to low_stock_count
         iv. If low_stock_count is 0:
            i. Display " All items have sufficient stock."
      ii. Else:
         i. Display " No items to check."
   h. Else if choice is 5:
      i. Set is_running to false
   i. Else:
      i. Display " Invalid choice!"
7. Display "Thank you for using Inventory Management System! "
```

**Loop Logic:**
- [ ] Menu-driven interface with multiple operations
- [ ] Array search and update operations
- [ ] Inventory monitoring and alerts
- [ ] Data validation and error handling

**Your Task:** Create a comprehensive inventory management system.

---

## Algorithm 4: Grade Book Calculator

**Pseudocode:**
```
Algorithm: Calculate Final Grades
1. Display "=== Grade Book Calculator ==="
2. Display "Enter number of students: "
3. Get num_students from user
4. Display "Enter number of assignments: "
5. Get num_assignments from user
6. Initialize grades 2D array (num_students × num_assignments)
7. Initialize student_names array (size num_students)
8. For student from 0 to num_students - 1:
   a. Display "Enter name for student " + (student + 1) + ": "
   b. Get student_names[student] from user
   c. Initialize student_total to 0
   d. For assignment from 0 to num_assignments - 1:
      i. Display "Enter grade for " + student_names[student] + " assignment " + (assignment + 1) + ": "
      ii. Get grade from user
      iii. Store grade in grades[student][assignment]
      iv. Add grade to student_total
   e. Calculate student_average = student_total ÷ num_assignments
   f. Display student_names[student] + "'s average: " + student_average
9. Display "=== Class Statistics ==="
10. Initialize class_total to 0
11. Initialize highest_average to 0
12. Initialize lowest_average to 100
13. For student from 0 to num_students - 1:
   a. Initialize student_total to 0
   b. For assignment from 0 to num_assignments - 1:
      i. Add grades[student][assignment] to student_total
   c. Calculate student_average = student_total ÷ num_assignments
   d. Add student_average to class_total
   e. If student_average > highest_average:
      i. Set highest_average to student_average
   f. If student_average < lowest_average:
      i. Set lowest_average to student_average
14. Calculate class_average = class_total ÷ num_students
15. Display "Class average: " + class_average
16. Display "Highest student average: " + highest_average
17. Display "Lowest student average: " + lowest_average
18. Display "=== Grade Distribution ==="
19. Initialize grade_ranges array [0,0,0,0,0] (A, B, C, D, F)
20. For student from 0 to num_students - 1:
   a. Calculate student_average as above
   b. If student_average >= 90:
      i. Add 1 to grade_ranges[0] (A)
   c. Else if student_average >= 80:
      i. Add 1 to grade_ranges[1] (B)
   d. Else if student_average >= 70:
      i. Add 1 to grade_ranges[2] (C)
   e. Else if student_average >= 60:
      i. Add 1 to grade_ranges[3] (D)
   f. Else:
      i. Add 1 to grade_ranges[4] (F)
21. Display "A grades: " + grade_ranges[0]
22. Display "B grades: " + grade_ranges[1]
23. Display "C grades: " + grade_ranges[2]
24. Display "D grades: " + grade_ranges[3]
25. Display "F grades: " + grade_ranges[4]
```

**Loop Logic:**
- [ ] 2D array processing (nested loops)
- [ ] Multiple statistical calculations
- [ ] Grade distribution analysis
- [ ] Complex data aggregation

**Your Task:** Build a comprehensive grade book system.

---

## Algorithm 5: Password Generator

**Pseudocode:**
```
Algorithm: Generate Secure Passwords
1. Display "=== Password Generator ==="
2. Display "Enter desired password length (8-20): "
3. Get password_length from user
4. While password_length < 8 or password_length > 20:
   a. Display " Length must be between 8-20 characters!"
   b. Display "Enter desired password length (8-20): "
   c. Get password_length from user
5. Display "Include uppercase letters? (y/n): "
6. Get include_upper from user
7. Display "Include numbers? (y/n): "
8. Get include_numbers from user
9. Display "Include special characters? (y/n): "
10. Get include_special from user
11. Initialize character_sets array
12. Add "abcdefghijklmnopqrstuvwxyz" to character_sets (lowercase always included)
13. If include_upper is "y":
   a. Add "ABCDEFGHIJKLMNOPQRSTUVWXYZ" to character_sets
14. If include_numbers is "y":
   a. Add "0123456789" to character_sets
15. If include_special is "y":
   a. Add "!@#$%^&*()_+-=[]{}|;:,.<>?" to character_sets
16. Initialize password as empty string
17. For position from 1 to password_length:
   a. Randomly select one character set from character_sets
   b. Randomly select one character from selected set
   c. Append character to password
18. Display "Generated Password: " + password
19. Display "Password length: " + password_length
20. Display "Character sets used:"
21. If include_upper is "y":
   a. Display " Uppercase letters"
22. If include_numbers is "y":
   a. Display " Numbers"
23. If include_special is "y":
   a. Display " Special characters"
24. Display " Lowercase letters (always included)"
```

**Loop Logic:**
- [ ] Input validation loop
- [ ] Character set configuration
- [ ] Password generation loop
- [ ] Random character selection

**Your Task:** Create a customizable password generator.

---

## Algorithm 6: Voting System

**Pseudocode:**
```
Algorithm: Conduct Election Voting
1. Display "=== Election Voting System ==="
2. Initialize candidate_names array ["Alice", "Bob", "Charlie"]
3. Initialize votes array [0, 0, 0] (one for each candidate)
4. Initialize total_votes to 0
5. Initialize voting_active to true
6. While voting_active is true:
   a. Display "=== Vote Menu ==="
   b. Display "Candidates:"
   c. For i from 0 to 2:
      i. Display (i + 1) + ". " + candidate_names[i]
   d. Display "4. Show Results"
   e. Display "5. End Voting"
   f. Display "Enter your choice (1-5): "
   g. Get choice from user
   h. If choice >= 1 and choice <= 3:
      i. Add 1 to votes[choice - 1]
      ii. Add 1 to total_votes
      iii. Display " Vote recorded for " + candidate_names[choice - 1]
   i. Else if choice is 4:
      i. Display "=== Current Results ==="
      ii. Display "Total votes: " + total_votes
      iii. For i from 0 to 2:
         i. Calculate percentage = (votes[i] ÷ total_votes) × 100
         ii. Display candidate_names[i] + ": " + votes[i] + " votes (" + percentage + "%)"
   j. Else if choice is 5:
      i. Set voting_active to false
   k. Else:
      i. Display " Invalid choice!"
7. If total_votes > 0:
   a. Display "=== Final Election Results ==="
   b. Initialize winner_index to 0
   c. Initialize max_votes to votes[0]
   d. For i from 1 to 2:
      i. If votes[i] > max_votes:
         i. Set max_votes to votes[i]
         ii. Set winner_index to i
   e. Display " Winner: " + candidate_names[winner_index] + " with " + max_votes + " votes!"
   f. Display "Total votes cast: " + total_votes
   g. For i from 0 to 2:
      i. Calculate percentage = (votes[i] ÷ total_votes) × 100
      ii. Display candidate_names[i] + ": " + votes[i] + " votes (" + percentage + "%)"
8. Else:
   a. Display "No votes were cast."
```

**Loop Logic:**
- [ ] Menu-driven voting interface
- [ ] Vote counting and storage
- [ ] Real-time results display
- [ ] Winner determination algorithm

**Your Task:** Build an election voting system.

---

### Loop Control Techniques

**Loop Termination Conditions:**
- [ ] **Counter-controlled**: Fixed number of iterations
- [ ] **Sentinel-controlled**: Special value ends input
- [ ] **Flag-controlled**: Boolean condition controls loop
- [ ] **User-controlled**: User chooses to continue/stop

**Loop Best Practices:**
- [ ] Initialize loop variables properly
- [ ] Update loop variables in each iteration
- [ ] Use meaningful variable names
- [ ] Avoid infinite loops
- [ ] Consider loop efficiency

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

1. **Add Data Persistence**: Save/load data to files
2. **Enhanced Features**: Add sorting, filtering, search
3. **Error Recovery**: Handle system errors gracefully
4. **Performance Optimization**: Improve algorithm efficiency

---

## Loop Algorithm Patterns

### Accumulation Pattern
```
Initialize total to 0
While getting values:
    Get next_value
    Add next_value to total
Display "Total: " + total
```

### Counting Pattern
```
Initialize count to 0
For each item:
    If item meets criteria:
        Add 1 to count
Display "Count: " + count
```

### Search Pattern
```
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
```

### Validation Pattern
```
Initialize is_valid to false
While not is_valid:
    Get user_input
    If input meets criteria:
        Set is_valid to true
    Else:
        Display error message
Process valid input
```

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Sales Data Analyzer

```c
#include <stdio.h>

int main() {
    float sales[30];
    int sales_count = 0;
    float total_sales = 0.0, highest_sale = 0.0, lowest_sale = 999999.0;

    printf("=== Sales Data Analyzer ===\n");
    printf("Enter daily sales (enter -1 to finish):\n");

    while (sales_count < 30) {
        printf("Day %d: $", sales_count + 1);
        float daily_sale;
        scanf("%f", &daily_sale);

        if (daily_sale == -1) {
            break;
        } else if (daily_sale >= 0) {
            sales[sales_count] = daily_sale;
            total_sales += daily_sale;
            sales_count++;

            if (daily_sale > highest_sale) {
                highest_sale = daily_sale;
            }
            if (daily_sale < lowest_sale) {
                lowest_sale = daily_sale;
            }
        } else {
            printf(" Invalid sale amount! Please enter positive number.\n");
        }
    }

    if (sales_count > 0) {
        float average_sale = total_sales / sales_count;

        printf("\n=== Sales Summary ===\n");
        printf("Total days: %d\n", sales_count);
        printf("Total sales: $%.2f\n", total_sales);
        printf("Average daily sales: $%.2f\n", average_sale);
        printf("Highest sale: $%.2f\n", highest_sale);
        printf("Lowest sale: $%.2f\n", lowest_sale);

        printf("\n=== Daily Breakdown ===\n");
        for (int i = 0; i < sales_count; i++) {
            printf("Day %d: $%.2f\n", i + 1, sales[i]);
        }
    } else {
        printf("No sales data entered.\n");
    }

    return 0;
}
```

**Key Concepts:**
- [ ] Array storage for sales data
- [ ] Loop with sentinel value (-1) for termination
- [ ] Statistical calculations with accumulation
- [ ] Input validation and error handling

---

### Algorithm 2: Student Attendance Tracker

```c
#include <stdio.h>
# include <string.h>

int main() {
    int num_students, present_count = 0;
    char attendance_status[10];

    printf("=== Class Attendance Tracker ===\n");
    printf("Enter number of students: ");
    scanf("%d", &num_students);

    // Using array for attendance (1 = present, 0 = absent)
    int attendance[100]; // Assuming max 100 students

    for (int student = 1; student <= num_students; student++) {
        printf("Student %d present? (y/n): ", student);
        scanf("%s", attendance_status);

        if (strcmp(attendance_status, "y") == 0 || strcmp(attendance_status, "Y") == 0) {
            attendance[student - 1] = 1;
            present_count++;
        } else {
            attendance[student - 1] = 0;
        }
    }

    float attendance_percentage = (float)present_count / num_students * 100;

    printf("\n=== Attendance Report ===\n");
    printf("Total students: %d\n", num_students);
    printf("Present: %d\n", present_count);
    printf("Absent: %d\n", num_students - present_count);
    printf("Attendance rate: %.1f%%\n", attendance_percentage);

    if (attendance_percentage >= 90) {
        printf(" Excellent attendance!\n");
    } else if (attendance_percentage >= 75) {
        printf(" Satisfactory attendance\n");
    } else {
        printf(" Poor attendance - follow up required\n");
    }

    printf("\n=== Individual Status ===\n");
    for (int student = 1; student <= num_students; student++) {
        if (attendance[student - 1] == 1) {
            printf("Student %d:  Present\n", student);
        } else {
            printf("Student %d:  Absent\n", student);
        }
    }

    return 0;
}
```

**Key Concepts:**
- [ ] Fixed iteration for known number of students
- [ ] Array storage of boolean attendance data
- [ ] Percentage calculations
- [ ] Individual status reporting

---

### Algorithm 3: Inventory Management System

```c
#include <stdio.h>
# include <string.h>

int main() {
    char item_names[50][50]; // 50 items, each name up to 50 chars
    int item_quantities[50];
    int item_count = 0;
    int is_running = 1;
    int choice;

    printf("=== Inventory Management System ===\n");

    while (is_running) {
        printf("\n1. Add Item\n");
        printf("2. Update Quantity\n");
        printf("3. Display Inventory\n");
        printf("4. Find Low Stock Items\n");
        printf("5. Exit\n");
        printf("Choose option (1-5): ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: {
                if (item_count < 50) {
                    char new_item_name[50];
                    int new_quantity;

                    printf("Enter item name: ");
                    scanf("%s", new_item_name);
                    printf("Enter initial quantity: ");
                    scanf("%d", &new_quantity);

                    if (new_quantity >= 0) {
                        strcpy(item_names[item_count], new_item_name);
                        item_quantities[item_count] = new_quantity;
                        item_count++;
                        printf(" Item added successfully!\n");
                    } else {
                        printf(" Invalid quantity!\n");
                    }
                } else {
                    printf(" Inventory is full!\n");
                }
                break;
            }
            case 2: {
                if (item_count > 0) {
                    char search_name[50];
                    printf("Enter item name to update: ");
                    scanf("%s", search_name);

                    int found = 0;
                    for (int i = 0; i < item_count; i++) {
                        if (strcmp(item_names[i], search_name) == 0) {
                            printf("Current quantity: %d\n", item_quantities[i]);
                            printf("Enter new quantity: ");
                            int new_quantity;
                            scanf("%d", &new_quantity);

                            if (new_quantity >= 0) {
                                item_quantities[i] = new_quantity;
                                printf(" Quantity updated!\n");
                                found = 1;
                            } else {
                                printf(" Invalid quantity!\n");
                            }
                            break;
                        }
                    }

                    if (!found) {
                        printf(" Item not found!\n");
                    }
                } else {
                    printf(" No items in inventory.\n");
                }
                break;
            }
            case 3:
                if (item_count > 0) {
                    printf("=== Current Inventory ===\n");
                    for (int i = 0; i < item_count; i++) {
                        printf("%s: %d units\n", item_names[i], item_quantities[i]);
                    }
                } else {
                    printf(" Inventory is empty.\n");
                }
                break;
            case 4:
                if (item_count > 0) {
                    printf("=== Low Stock Alert (≤5 units) ===\n");
                    int low_stock_count = 0;

                    for (int i = 0; i < item_count; i++) {
                        if (item_quantities[i] <= 5) {
                            printf("%s: %d units \n", item_names[i], item_quantities[i]);
                            low_stock_count++;
                        }
                    }

                    if (low_stock_count == 0) {
                        printf(" All items have sufficient stock.\n");
                    }
                } else {
                    printf(" No items to check.\n");
                }
                break;
            case 5:
                is_running = 0;
                break;
            default:
                printf(" Invalid choice!\n");
                break;
        }
    }

    printf("Thank you for using Inventory Management System! \n");

    return 0;
}
```

**Key Concepts:**
- [ ] 2D array for string storage
- [ ] Array search and update operations
- [ ] Menu-driven interface
- [ ] Inventory monitoring and alerts

---

### Algorithm 4: Grade Book Calculator

```c
#include <stdio.h>
# include <string.h>

int main() {
    int num_students, num_assignments;

    printf("=== Grade Book Calculator ===\n");
    printf("Enter number of students: ");
    scanf("%d", &num_students);
    printf("Enter number of assignments: ");
    scanf("%d", &num_assignments);

    char student_names[50][50]; // Max 50 students, names up to 50 chars
    float grades[50][20]; // Max 50 students, 20 assignments

    // Input student data
    for (int student = 0; student < num_students; student++) {
        printf("Enter name for student %d: ", student + 1);
        scanf("%s", student_names[student]);

        float student_total = 0.0;
        for (int assignment = 0; assignment < num_assignments; assignment++) {
            printf("Enter grade for %s assignment %d: ",
                   student_names[student], assignment + 1);
            scanf("%f", &grades[student][assignment]);
            student_total += grades[student][assignment];
        }

        float student_average = student_total / num_assignments;
        printf("%s's average: %.1f\n", student_names[student], student_average);
    }

    // Calculate class statistics
    printf("\n=== Class Statistics ===\n");
    float class_total = 0.0;
    float highest_average = 0.0;
    float lowest_average = 100.0;

    for (int student = 0; student < num_students; student++) {
        float student_total = 0.0;
        for (int assignment = 0; assignment < num_assignments; assignment++) {
            student_total += grades[student][assignment];
        }

        float student_average = student_total / num_assignments;
        class_total += student_average;

        if (student_average > highest_average) {
            highest_average = student_average;
        }
        if (student_average < lowest_average) {
            lowest_average = student_average;
        }
    }

    float class_average = class_total / num_students;
    printf("Class average: %.1f\n", class_average);
    printf("Highest student average: %.1f\n", highest_average);
    printf("Lowest student average: %.1f\n", lowest_average);

    // Grade distribution
    printf("\n=== Grade Distribution ===\n");
    int grade_ranges[5] = {0, 0, 0, 0, 0}; // A, B, C, D, F

    for (int student = 0; student < num_students; student++) {
        float student_total = 0.0;
        for (int assignment = 0; assignment < num_assignments; assignment++) {
            student_total += grades[student][assignment];
        }

        float student_average = student_total / num_assignments;

        if (student_average >= 90) grade_ranges[0]++;
        else if (student_average >= 80) grade_ranges[1]++;
        else if (student_average >= 70) grade_ranges[2]++;
        else if (student_average >= 60) grade_ranges[3]++;
        else grade_ranges[4]++;
    }

    printf("A grades: %d\n", grade_ranges[0]);
    printf("B grades: %d\n", grade_ranges[1]);
    printf("C grades: %d\n", grade_ranges[2]);
    printf("D grades: %d\n", grade_ranges[3]);
    printf("F grades: %d\n", grade_ranges[4]);

    return 0;
}
```

**Key Concepts:**
- [ ] 2D array processing with nested loops
- [ ] Multiple statistical calculations
- [ ] Grade distribution analysis
- [ ] Complex data aggregation

---

### Algorithm 5: Password Generator

```c
#include <stdio.h>
# include <stdlib.h>
# include <time.h>
# include <string.h>

int main() {
    int password_length;
    char include_upper[10], include_numbers[10], include_special[10];

    printf("=== Password Generator ===\n");
    printf("Enter desired password length (8-20): ");
    scanf("%d", &password_length);

    while (password_length < 8 || password_length > 20) {
        printf(" Length must be between 8-20 characters!\n");
        printf("Enter desired password length (8-20): ");
        scanf("%d", &password_length);
    }

    printf("Include uppercase letters? (y/n): ");
    scanf("%s", include_upper);
    printf("Include numbers? (y/n): ");
    scanf("%s", include_numbers);
    printf("Include special characters? (y/n): ");
    scanf("%s", include_special);

    // Character sets
    char lowercase[] = "abcdefghijklmnopqrstuvwxyz";
    char uppercase[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char numbers[] = "0123456789";
    char special[] = "!@#$%^&*()_+-=[]{}|;:,.<>?";

    // Build available character sets
    char* char_sets[10];
    int set_count = 1;
    char_sets[0] = lowercase; // Always include lowercase

    if (strcmp(include_upper, "y") == 0 || strcmp(include_upper, "Y") == 0) {
        char_sets[set_count++] = uppercase;
    }
    if (strcmp(include_numbers, "y") == 0 || strcmp(include_numbers, "Y") == 0) {
        char_sets[set_count++] = numbers;
    }
    if (strcmp(include_special, "y") == 0 || strcmp(include_special, "Y") == 0) {
        char_sets[set_count++] = special;
    }

    // Seed random number generator
    srand(time(NULL));

    // Generate password
    char password[21]; // Max length 20 + null terminator
    for (int i = 0; i < password_length; i++) {
        // Pick random character set
        int set_index = rand() % set_count;
        char* selected_set = char_sets[set_index];

        // Pick random character from set
        int char_index = rand() % strlen(selected_set);
        password[i] = selected_set[char_index];
    }
    password[password_length] = '\0'; // Null terminate

    printf("Generated Password: %s\n", password);
    printf("Password length: %d\n", password_length);
    printf("Character sets used:\n");
    if (strcmp(include_upper, "y") == 0 || strcmp(include_upper, "Y") == 0) {
        printf(" Uppercase letters\n");
    }
    if (strcmp(include_numbers, "y") == 0 || strcmp(include_numbers, "Y") == 0) {
        printf(" Numbers\n");
    }
    if (strcmp(include_special, "y") == 0 || strcmp(include_special, "Y") == 0) {
        printf(" Special characters\n");
    }
    printf(" Lowercase letters (always included)\n");

    return 0;
}
```

**Key Concepts:**
- [ ] Input validation loop
- [ ] Character set configuration
- [ ] Random number generation
- [ ] Array of string pointers

---

### Algorithm 6: Voting System

```c
#include <stdio.h>
# include <string.h>

int main() {
    char candidate_names[3][20] = {"Alice", "Bob", "Charlie"};
    int votes[3] = {0, 0, 0};
    int total_votes = 0;
    int voting_active = 1;
    int choice;

    printf("=== Election Voting System ===\n");

    while (voting_active) {
        printf("\n=== Vote Menu ===\n");
        printf("Candidates:\n");
        for (int i = 0; i < 3; i++) {
            printf("%d. %s\n", i + 1, candidate_names[i]);
        }
        printf("4. Show Results\n");
        printf("5. End Voting\n");
        printf("Enter your choice (1-5): ");
        scanf("%d", &choice);

        if (choice >= 1 && choice <= 3) {
            votes[choice - 1]++;
            total_votes++;
            printf(" Vote recorded for %s\n", candidate_names[choice - 1]);
        } else if (choice == 4) {
            printf("=== Current Results ===\n");
            printf("Total votes: %d\n", total_votes);

            if (total_votes > 0) {
                for (int i = 0; i < 3; i++) {
                    float percentage = (float)votes[i] / total_votes * 100;
                    printf("%s: %d votes (%.1f%%)\n",
                           candidate_names[i], votes[i], percentage);
                }
            } else {
                printf("No votes cast yet.\n");
            }
        } else if (choice == 5) {
            voting_active = 0;
        } else {
            printf(" Invalid choice!\n");
        }
    }

    if (total_votes > 0) {
        printf("\n=== Final Election Results ===\n");

        // Find winner
        int winner_index = 0;
        int max_votes = votes[0];

        for (int i = 1; i < 3; i++) {
            if (votes[i] > max_votes) {
                max_votes = votes[i];
                winner_index = i;
            }
        }

        printf(" Winner: %s with %d votes!\n",
               candidate_names[winner_index], max_votes);
        printf("Total votes cast: %d\n", total_votes);

        for (int i = 0; i < 3; i++) {
            float percentage = (float)votes[i] / total_votes * 100;
            printf("%s: %d votes (%.1f%%)\n",
                   candidate_names[i], votes[i], percentage);
        }
    } else {
        printf("No votes were cast.\n");
    }

    return 0;
}
```

**Key Concepts:**
- [ ] Menu-driven voting interface
- [ ] Vote counting and storage
- [ ] Real-time results display
- [ ] Winner determination algorithm

---

### Loop Efficiency Considerations

**Array Processing:**
```c
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
```

**Early Termination:**
```c
// Good - stop when found
for (int i = 0; i < size; i++) {
    if (array[i] == target) {
        found = 1;
        break; // Don't continue searching
    }
}
```

---

 **Fantastic! You've mastered loop-based algorithms!**

*Loops are the engines of computation. Next: Function pseudocode for modular programming! *

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
