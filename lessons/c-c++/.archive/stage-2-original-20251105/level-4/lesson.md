# Level 4: Input/Output Pseudocode

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

User interaction is the heart of useful programs! Today you'll master the art of getting information from users and presenting results beautifully. You'll learn input validation, menu systems, formatted output, and creating user-friendly programs.

---

### Learning Goals

- [ ] Implement robust input validation
- [ ] Create user-friendly menu systems
- [ ] Format output for better readability
- [ ] Handle input errors gracefully
- [ ] Design intuitive user interfaces
- [ ] Create interactive program flows

---

### Your Task

**Translate each interactive pseudocode algorithm into working C code with excellent user experience.**

---

## Algorithm 1: Age Verification System

**Pseudocode:**
```
Algorithm: Verify User Age
1. Display "=== Age Verification System ==="
2. Initialize is_valid_age to false
3. While is_valid_age is false:
   a. Display "Please enter your age (0-120): "
   b. Get age_input from user
   c. If age_input is not a valid number:
      i. Display " Invalid input! Please enter a number."
   d. Else if age_input < 0:
      i. Display " Age cannot be negative!"
   e. Else if age_input > 120:
      i. Display " Age cannot be over 120!"
   f. Else:
      i. Set is_valid_age to true
4. Display " Age verified: " + age_input + " years old"
5. If age_input >= 18:
   a. Display " You are an adult!"
6. Else:
   a. Display " You are a minor."
```

**Input/Output Focus:**
- [ ] Input validation (numeric, range checking)
- [ ] Error messages with emojis
- [ ] Success confirmation
- [ ] Conditional output based on age

**Your Task:** Create a robust age verification system.

---

## Algorithm 2: Restaurant Menu System

**Pseudocode:**
```
Algorithm: Restaurant Ordering System
1. Display "=== Welcome to Code Café ==="
2. Initialize total_cost to 0
3. Initialize order_complete to false
4. While order_complete is false:
   a. Display menu options:
      i. "1. Coffee - $3.50"
      ii. "2. Sandwich - $8.75"
      iii. "3. Salad - $6.25"
      iv. "4. Dessert - $4.00"
      v. "5. Complete Order"
   b. Display "Enter your choice (1-5): "
   c. Get choice from user
   d. If choice is 1:
      i. Add 3.50 to total_cost
      ii. Display " Coffee added to your order!"
   e. Else if choice is 2:
      i. Add 8.75 to total_cost
      ii. Display " Sandwich added to your order!"
   f. Else if choice is 3:
      i. Add 6.25 to total_cost
      ii. Display " Salad added to your order!"
   g. Else if choice is 4:
      i. Add 4.00 to total_cost
      ii. Display " Dessert added to your order!"
   h. Else if choice is 5:
      i. Set order_complete to true
   i. Else:
      i. Display " Invalid choice! Please select 1-5."
5. Display "=== Order Summary ==="
6. Display "Total cost: $" + total_cost
7. Calculate tax = total_cost × 0.08
8. Calculate final_total = total_cost + tax
9. Display "Tax (8%): $" + tax
10. Display "Final total: $" + final_total
11. Display "Thank you for your order! "
```

**Input/Output Focus:**
- [ ] Clear menu formatting
- [ ] Itemized feedback for each choice
- [ ] Professional order summary
- [ ] Currency formatting

**Your Task:** Build an interactive restaurant ordering system.

---

## Algorithm 3: Student Grade Manager

**Pseudocode:**
```
Algorithm: Student Grade Management
1. Display "=== Student Grade Manager ==="
2. Initialize grades array (can hold 100 grades)
3. Initialize grade_count to 0
4. Initialize is_running to true
5. While is_running is true:
   a. Display menu:
      i. "1. Add Grade"
      ii. "2. View All Grades"
      iii. "3. Calculate Average"
      iv. "4. Find Highest/Lowest"
      v. "5. Exit"
   b. Display "Choose an option (1-5): "
   c. Get choice from user
   d. If choice is 1:
      i. If grade_count < 100:
         i. Display "Enter grade (0-100): "
         ii. Get new_grade from user
         iii. If new_grade is valid (0-100):
            i. Store new_grade in grades array
            ii. Add 1 to grade_count
            iii. Display " Grade added: " + new_grade
         iv. Else:
            i. Display " Invalid grade! Must be 0-100."
      ii. Else:
         i. Display " Grade book is full!"
   e. Else if choice is 2:
      i. If grade_count > 0:
         i. Display "=== All Grades ==="
         ii. For each grade in grades array:
            i. Display grade
      ii. Else:
         i. Display " No grades entered yet."
   f. Else if choice is 3:
      i. If grade_count > 0:
         i. Initialize sum to 0
         ii. For each grade in grades array:
            i. Add grade to sum
         iii. Calculate average = sum ÷ grade_count
         iv. Display " Average: " + average + "%"
      ii. Else:
         i. Display " No grades to average."
   g. Else if choice is 4:
      i. If grade_count > 0:
         i. Initialize highest to first grade
         ii. Initialize lowest to first grade
         iii. For each remaining grade:
            i. If grade > highest: set highest to grade
            ii. If grade < lowest: set lowest to grade
         iv. Display " Highest: " + highest + "%"
         v. Display " Lowest: " + lowest + "%"
      ii. Else:
         i. Display " No grades to analyze."
   h. Else if choice is 5:
      i. Set is_running to false
   i. Else:
      i. Display " Invalid choice! Please select 1-5."
6. Display "Thank you for using Grade Manager! "
```

**Input/Output Focus:**
- [ ] Array data storage
- [ ] Multiple menu operations
- [ ] Formatted data display
- [ ] Empty state handling

**Your Task:** Create a comprehensive grade management system.

---

## Algorithm 4: Unit Converter

**Pseudocode:**
```
Algorithm: Unit Conversion Calculator
1. Display "=== Unit Converter ==="
2. Initialize is_running to true
3. While is_running is true:
   a. Display conversion options:
      i. "1. Temperature (°F ↔ °C)"
      ii. "2. Length (Feet ↔ Meters)"
      iii. "3. Weight (Pounds ↔ Kilograms)"
      iv. "4. Exit"
   b. Display "Select conversion type (1-4): "
   c. Get conversion_type from user
   d. If conversion_type is 1:
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
   e. Else if conversion_type is 2:
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
   f. Else if conversion_type is 3:
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
   g. Else if conversion_type is 4:
      i. Set is_running to false
   h. Else:
      i. Display " Invalid conversion type!"
4. Display "Thank you for using Unit Converter! "
```

**Input/Output Focus:**
- [ ] Nested menu systems
- [ ] Multiple conversion categories
- [ ] Bidirectional conversions
- [ ] Clear unit labeling

**Your Task:** Build a comprehensive unit conversion tool.

---

## Algorithm 5: Survey Data Collector

**Pseudocode:**
```
Algorithm: Customer Satisfaction Survey
1. Display "=== Customer Satisfaction Survey ==="
2. Initialize responses array (can hold 50 responses)
3. Initialize response_count to 0
4. Initialize survey_complete to false
5. While survey_complete is false:
   a. Display "Participant #" + (response_count + 1)
   b. Display "Rate your satisfaction (1-5): "
   c. Display "1 = Very Dissatisfied"
   d. Display "2 = Dissatisfied"
   e. Display "3 = Neutral"
   f. Display "4 = Satisfied"
   g. Display "5 = Very Satisfied"
   h. Display "Enter rating (1-5, or 0 to finish survey): "
   i. Get rating from user
   j. If rating is 0:
      i. Set survey_complete to true
   k. Else if rating is valid (1-5):
      i. Store rating in responses array
      ii. Add 1 to response_count
      iii. Display " Thank you for your feedback!"
   l. Else:
      i. Display " Invalid rating! Please enter 1-5 or 0 to finish."
6. If response_count > 0:
   a. Display "=== Survey Results ==="
   b. Display "Total responses: " + response_count
   c. Initialize count array for ratings 1-5 (all start at 0)
   d. For each response in responses array:
      i. Add 1 to count[response]
   e. For rating from 1 to 5:
      i. Calculate percentage = (count[rating] ÷ response_count) × 100
      ii. Display rating + ": " + count[rating] + " responses (" + percentage + "%)"
   f. Calculate average = sum of all responses ÷ response_count
   g. Display "Average satisfaction: " + average + "/5.0"
7. Else:
   a. Display "No survey responses collected."
8. Display "Thank you for participating! "
```

**Input/Output Focus:**
- [ ] Clear survey instructions
- [ ] Rating scale explanation
- [ ] Statistical analysis output
- [ ] Percentage calculations

**Your Task:** Create an interactive survey system with analysis.

---

## Algorithm 6: Library Book Tracker

**Pseudocode:**
```
Algorithm: Library Book Management
1. Display "=== Library Book Tracker ==="
2. Initialize books array (can hold 20 book titles)
3. Initialize book_count to 0
4. Initialize is_running to true
5. While is_running is true:
   a. Display menu:
      i. "1. Add Book"
      ii. "2. List All Books"
      iii. "3. Search Books"
      iv. "4. Remove Book"
      v. "5. Exit"
   b. Display "Choose option (1-5): "
   c. Get choice from user
   d. If choice is 1:
      i. If book_count < 20:
         i. Display "Enter book title: "
         ii. Get book_title from user
         iii. If book_title is not empty:
            i. Store book_title in books array
            ii. Add 1 to book_count
            iii. Display " Book added: '" + book_title + "'"
         iv. Else:
            i. Display " Book title cannot be empty!"
      ii. Else:
         i. Display " Library is full!"
   e. Else if choice is 2:
      i. If book_count > 0:
         i. Display "=== Library Collection ==="
         ii. For i from 1 to book_count:
            i. Display i + ". " + books[i-1]
      ii. Else:
         i. Display " No books in library yet."
   f. Else if choice is 3:
      i. If book_count > 0:
         i. Display "Enter search term: "
         ii. Get search_term from user
         iii. Initialize found_count to 0
         iv. For each book in books array:
            i. If book contains search_term:
               i. Display " " + book
               ii. Add 1 to found_count
         v. If found_count is 0:
            i. Display " No books found matching '" + search_term + "'"
      ii. Else:
         i. Display " No books to search."
   g. Else if choice is 4:
      i. If book_count > 0:
         i. Display "Enter book number to remove (1-" + book_count + "): "
         ii. Get book_number from user
         iii. If book_number is valid (1 to book_count):
            i. Display "Removing: '" + books[book_number-1] + "'"
            ii. Shift remaining books left in array
            iii. Subtract 1 from book_count
            iv. Display " Book removed successfully!"
         iv. Else:
            i. Display " Invalid book number!"
      ii. Else:
         i. Display " No books to remove."
   h. Else if choice is 5:
      i. Set is_running to false
   i. Else:
      i. Display " Invalid choice!"
6. Display "Thank you for using Library Book Tracker! "
```

**Input/Output Focus:**
- [ ] String array management
- [ ] Search functionality
- [ ] Numbered list display
- [ ] Array manipulation (removal)

**Your Task:** Build a library book management system.

---

### Input Validation Techniques

**Numeric Input Validation:**
```c
// Check if input is within range
if (input >= min_value && input <= max_value) {
    // Valid input
} else {
    // Invalid input - show error
}
```

**String Input Validation:**
```c
// Check if string is not empty
if (strlen(input_string) > 0) {
    // Valid input
} else {
    // Empty input - show error
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

1. **Enhanced Validation**: Add more sophisticated input checking
2. **Data Persistence**: Save/load data to files
3. **Advanced Features**: Add sorting, filtering, statistics
4. **Multi-user Support**: Handle multiple users/sessions

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
- [ ] **Be specific**: "Grade must be between 0-100" not "Invalid input"
- [ ] **Be helpful**: Suggest correct input format
- [ ] **Be consistent**: Use same error style throughout
- [ ] **Use emojis**:  for success,  for errors,  for warnings

### Input Prompt Guidelines
- [ ] **Be descriptive**: "Enter your age in years:"
- [ ] **Show format**: "Enter date (MM/DD/YYYY):"
- [ ] **Indicate ranges**: "Enter rating (1-5):"
- [ ] **Show defaults**: "Enter timeout [30 seconds]:"

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Age Verification System

```c
# include <stdio.h>

int main() {
    int age_input;
    int is_valid_age = 0;
    
    std::cout << "=== Age Verification System ===\n");
    
    while (!is_valid_age) {
        std::cout << "Please enter your age (0-120): ");
        
        if (scanf("%d", &age_input) != 1) {
            // Clear invalid input
            while (getchar() != '\n');
            std::cout << " Invalid input! Please enter a number.\n");
        } else if (age_input < 0) {
            std::cout << " Age cannot be negative!\n");
        } else if (age_input > 120) {
            std::cout << " Age cannot be over 120!\n");
        } else {
            is_valid_age = 1;
        }
    }
    
    std::cout << " Age verified: %d years old\n", age_input);
    
    if (age_input >= 18) {
        std::cout << " You are an adult!\n");
    } else {
        std::cout << " You are a minor.\n");
    }
    
    return 0;
}
```

**Key Concepts:**
- [ ] Input validation with `scanf()` return value checking
- [ ] Clearing invalid input from buffer
- [ ] Boolean flag for validation state

---

### Algorithm 2: Restaurant Menu System

```c
# include <stdio.h>

int main() {
    float total_cost = 0.0;
    int order_complete = 0;
    int choice;
    
    std::cout << "=== Welcome to Code Café ===\n");
    
    while (!order_complete) {
        std::cout << "\n1. Coffee - $3.50\n");
        std::cout << "2. Sandwich - $8.75\n");
        std::cout << "3. Salad - $6.25\n");
        std::cout << "4. Dessert - $4.00\n");
        std::cout << "5. Complete Order\n");
        std::cout << "Enter your choice (1-5): ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                total_cost += 3.50;
                std::cout << " Coffee added to your order!\n");
                break;
            case 2:
                total_cost += 8.75;
                std::cout << " Sandwich added to your order!\n");
                break;
            case 3:
                total_cost += 6.25;
                std::cout << " Salad added to your order!\n");
                break;
            case 4:
                total_cost += 4.00;
                std::cout << " Dessert added to your order!\n");
                break;
            case 5:
                order_complete = 1;
                break;
            default:
                std::cout << " Invalid choice! Please select 1-5.\n");
                break;
        }
    }
    
    std::cout << "\n=== Order Summary ===\n");
    std::cout << "Total cost: $%.2f\n", total_cost);
    
    float tax = total_cost * 0.08;
    float final_total = total_cost + tax;
    
    std::cout << "Tax (8%%): $%.2f\n", tax);
    std::cout << "Final total: $%.2f\n", final_total);
    std::cout << "Thank you for your order! \n");
    
    return 0;
}
```

**Key Concepts:**
- [ ] Switch statement for menu handling
- [ ] Accumulator pattern for total cost
- [ ] Professional receipt formatting

---

### Algorithm 3: Student Grade Manager

```c
# include <stdio.h>

int main() {
    float grades[100];
    int grade_count = 0;
    int is_running = 1;
    int choice;
    
    std::cout << "=== Student Grade Manager ===\n");
    
    while (is_running) {
        std::cout << "\n1. Add Grade\n");
        std::cout << "2. View All Grades\n");
        std::cout << "3. Calculate Average\n");
        std::cout << "4. Find Highest/Lowest\n");
        std::cout << "5. Exit\n");
        std::cout << "Choose an option (1-5): ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1: {
                if (grade_count < 100) {
                    float new_grade;
                    std::cout << "Enter grade (0-100): ");
                    scanf("%f", &new_grade);
                    
                    if (new_grade >= 0 && new_grade <= 100) {
                        grades[grade_count] = new_grade;
                        grade_count++;
                        std::cout << " Grade added: %.1f\n", new_grade);
                    } else {
                        std::cout << " Invalid grade! Must be 0-100.\n");
                    }
                } else {
                    std::cout << " Grade book is full!\n");
                }
                break;
            }
            case 2:
                if (grade_count > 0) {
                    std::cout << "=== All Grades ===\n");
                    for (int i = 0; i < grade_count; i++) {
                        std::cout << "%.1f\n", grades[i]);
                    }
                } else {
                    std::cout << " No grades entered yet.\n");
                }
                break;
            case 3:
                if (grade_count > 0) {
                    float sum = 0;
                    for (int i = 0; i < grade_count; i++) {
                        sum += grades[i];
                    }
                    float average = sum / grade_count;
                    std::cout << " Average: %.1f%%\n", average);
                } else {
                    std::cout << " No grades to average.\n");
                }
                break;
            case 4:
                if (grade_count > 0) {
                    float highest = grades[0];
                    float lowest = grades[0];
                    
                    for (int i = 1; i < grade_count; i++) {
                        if (grades[i] > highest) highest = grades[i];
                        if (grades[i] < lowest) lowest = grades[i];
                    }
                    
                    std::cout << " Highest: %.1f%%\n", highest);
                    std::cout << " Lowest: %.1f%%\n", lowest);
                } else {
                    std::cout << " No grades to analyze.\n");
                }
                break;
            case 5:
                is_running = 0;
                break;
            default:
                std::cout << " Invalid choice! Please select 1-5.\n");
                break;
        }
    }
    
    std::cout << "Thank you for using Grade Manager! \n");
    
    return 0;
}
```

**Key Concepts:**
- [ ] Array storage for multiple grades
- [ ] Multiple menu operations
- [ ] Statistical calculations on array data
- [ ] Input validation for grade ranges

---

### Algorithm 4: Unit Converter

```c
# include <stdio.h>

int main() {
    int is_running = 1;
    int conversion_type, direction;
    float value, result;
    
    std::cout << "=== Unit Converter ===\n");
    
    while (is_running) {
        std::cout << "\n1. Temperature (°F ↔ °C)\n");
        std::cout << "2. Length (Feet ↔ Meters)\n");
        std::cout << "3. Weight (Pounds ↔ Kilograms)\n");
        std::cout << "4. Exit\n");
        std::cout << "Select conversion type (1-4): ");
        scanf("%d", &conversion_type);
        
        if (conversion_type == 1) {
            std::cout << "1. °F to °C\n2. °C to °F\n");
            std::cout << "Choose direction: ");
            scanf("%d", &direction);
            std::cout << "Enter temperature: ");
            scanf("%f", &value);
            
            if (direction == 1) {
                result = (value - 32) * 5 / 9;
                std::cout << "%.1f°F = %.1f°C\n", value, result);
            } else if (direction == 2) {
                result = (value * 9 / 5) + 32;
                std::cout << "%.1f°C = %.1f°F\n", value, result);
            }
        } else if (conversion_type == 2) {
            std::cout << "1. Feet to Meters\n2. Meters to Feet\n");
            std::cout << "Choose direction: ");
            scanf("%d", &direction);
            std::cout << "Enter length: ");
            scanf("%f", &value);
            
            if (direction == 1) {
                result = value * 0.3048;
                std::cout << "%.2f ft = %.2f m\n", value, result);
            } else if (direction == 2) {
                result = value / 0.3048;
                std::cout << "%.2f m = %.2f ft\n", value, result);
            }
        } else if (conversion_type == 3) {
            std::cout << "1. Pounds to Kilograms\n2. Kilograms to Pounds\n");
            std::cout << "Choose direction: ");
            scanf("%d", &direction);
            std::cout << "Enter weight: ");
            scanf("%f", &value);
            
            if (direction == 1) {
                result = value * 0.4536;
                std::cout << "%.2f lbs = %.2f kg\n", value, result);
            } else if (direction == 2) {
                result = value / 0.4536;
                std::cout << "%.2f kg = %.2f lbs\n", value, result);
            }
        } else if (conversion_type == 4) {
            is_running = 0;
        } else {
            std::cout << " Invalid conversion type!\n");
        }
    }
    
    std::cout << "Thank you for using Unit Converter! \n");
    
    return 0;
}
```

**Key Concepts:**
- [ ] Nested menu system
- [ ] Multiple conversion formulas
- [ ] Bidirectional conversions
- [ ] Clear unit labeling in output

---

### Algorithm 5: Survey Data Collector

```c
# include <stdio.h>

int main() {
    int responses[50];
    int response_count = 0;
    int survey_complete = 0;
    int rating;
    
    std::cout << "=== Customer Satisfaction Survey ===\n");
    
    while (!survey_complete) {
        std::cout << "\nParticipant #%d\n", response_count + 1);
        std::cout << "Rate your satisfaction (1-5):\n");
        std::cout << "1 = Very Dissatisfied\n");
        std::cout << "2 = Dissatisfied\n");
        std::cout << "3 = Neutral\n");
        std::cout << "4 = Satisfied\n");
        std::cout << "5 = Very Satisfied\n");
        std::cout << "Enter rating (1-5, or 0 to finish survey): ");
        scanf("%d", &rating);
        
        if (rating == 0) {
            survey_complete = 1;
        } else if (rating >= 1 && rating <= 5) {
            responses[response_count] = rating;
            response_count++;
            std::cout << " Thank you for your feedback!\n");
        } else {
            std::cout << " Invalid rating! Please enter 1-5 or 0 to finish.\n");
        }
    }
    
    if (response_count > 0) {
        std::cout << "\n=== Survey Results ===\n");
        std::cout << "Total responses: %d\n", response_count);
        
        int counts[6] = {0}; // Index 1-5 for ratings
        
        for (int i = 0; i < response_count; i++) {
            counts[responses[i]]++;
        }
        
        for (int rating = 1; rating <= 5; rating++) {
            float percentage = (float)counts[rating] / response_count * 100;
            std::cout << "%d: %d responses (%.1f%%)\n", rating, counts[rating], percentage);
        }
        
        float sum = 0;
        for (int i = 0; i < response_count; i++) {
            sum += responses[i];
        }
        float average = sum / response_count;
        
        std::cout << "Average satisfaction: %.1f/5.0\n", average);
    } else {
        std::cout << "No survey responses collected.\n");
    }
    
    std::cout << "Thank you for participating! \n");
    
    return 0;
}
```

**Key Concepts:**
- [ ] Array storage for survey responses
- [ ] Statistical analysis (counts, percentages, averages)
- [ ] Clear survey interface with rating scale
- [ ] Comprehensive results display

---

### Algorithm 6: Library Book Tracker

```c
# include <stdio.h>
# include <string.h>

int main() {
    char books[20][100]; // 20 books, each up to 100 characters
    int book_count = 0;
    int is_running = 1;
    int choice;
    
    std::cout << "=== Library Book Tracker ===\n");
    
    while (is_running) {
        std::cout << "\n1. Add Book\n");
        std::cout << "2. List All Books\n");
        std::cout << "3. Search Books\n");
        std::cout << "4. Remove Book\n");
        std::cout << "5. Exit\n");
        std::cout << "Choose option (1-5): ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1: {
                if (book_count < 20) {
                    char book_title[100];
                    std::cout << "Enter book title: ");
                    getchar(); // Clear newline
                    fgets(book_title, sizeof(book_title), stdin);
                    
                    // Remove trailing newline
                    book_title[strcspn(book_title, "\n")] = '\0';
                    
                    if (strlen(book_title) > 0) {
                        strcpy(books[book_count], book_title);
                        book_count++;
                        std::cout << " Book added: '%s'\n", book_title);
                    } else {
                        std::cout << " Book title cannot be empty!\n");
                    }
                } else {
                    std::cout << " Library is full!\n");
                }
                break;
            }
            case 2:
                if (book_count > 0) {
                    std::cout << "=== Library Collection ===\n");
                    for (int i = 0; i < book_count; i++) {
                        std::cout << "%d. %s\n", i + 1, books[i]);
                    }
                } else {
                    std::cout << " No books in library yet.\n");
                }
                break;
            case 3: {
                if (book_count > 0) {
                    char search_term[100];
                    std::cout << "Enter search term: ");
                    getchar(); // Clear newline
                    fgets(search_term, sizeof(search_term), stdin);
                    search_term[strcspn(search_term, "\n")] = '\0';
                    
                    int found_count = 0;
                    for (int i = 0; i < book_count; i++) {
                        if (strstr(books[i], search_term) != NULL) {
                            std::cout << " %s\n", books[i]);
                            found_count++;
                        }
                    }
                    
                    if (found_count == 0) {
                        std::cout << " No books found matching '%s'\n", search_term);
                    }
                } else {
                    std::cout << " No books to search.\n");
                }
                break;
            }
            case 4: {
                if (book_count > 0) {
                    int book_number;
                    std::cout << "Enter book number to remove (1-%d): ", book_count);
                    scanf("%d", &book_number);
                    
                    if (book_number >= 1 && book_number <= book_count) {
                        std::cout << "Removing: '%s'\n", books[book_number - 1]);
                        
                        // Shift remaining books left
                        for (int i = book_number - 1; i < book_count - 1; i++) {
                            strcpy(books[i], books[i + 1]);
                        }
                        
                        book_count--;
                        std::cout << " Book removed successfully!\n");
                    } else {
                        std::cout << " Invalid book number!\n");
                    }
                } else {
                    std::cout << " No books to remove.\n");
                }
                break;
            }
            case 5:
                is_running = 0;
                break;
            default:
                std::cout << " Invalid choice!\n");
                break;
        }
    }
    
    std::cout << "Thank you for using Library Book Tracker! \n");
    
    return 0;
}
```

**Key Concepts:**
- [ ] 2D array for string storage
- [ ] String input with `fgets()` and newline handling
- [ ] String search with `strstr()`
- [ ] Array manipulation for removal
- [ ] Numbered list display

---

### Advanced Input Techniques

**Clearing Input Buffer:**
```c
// After scanf, clear remaining input
int c;
while ((c = getchar()) != '\n' && c != EOF);
```

**Reading Full Lines:**
```c
char buffer[100];
fgets(buffer, sizeof(buffer), stdin);
// Remove trailing newline
buffer[strcspn(buffer, "\n")] = '\0';
```

**Input Validation Patterns:**
```c
// Numeric range validation
int get_valid_number(int min, int max) {
    int value;
    do {
        std::cout << "Enter number (%d-%d): ", min, max);
        if (scanf("%d", &value) != 1) {
            while (getchar() != '\n'); // Clear bad input
            continue;
        }
    } while (value < min || value > max);
    return value;
}
```

---

 **Excellent! You've mastered user interaction and I/O operations!** 

*Programs that talk to users are much more useful. Next: Decision-making in pseudocode! *

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
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard C++ conventions with proper imports and main function
2. **Output**: Uses std::cout to print messages to the console
3. **Standard Library**: Includes iostream for input/output operations
4. **Return Value**: Returns 0 to indicate successful execution
5. **Best Practices**: Code is readable and uses C++ idioms

### Testing Your Solution

1. **Compile**: `g++ hello.cpp -o hello`
2. **Run**: `./hello`
3. **Expected Output**: `Hello, World!`

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| `command not found: g++` | Compiler not installed | `sudo apt install g++` (Ubuntu) |
| `undefined reference to main` | Missing main function | Ensure `int main()` exists |
| `error: unknown type name 'cout'` | Missing iostream | Add `#include <iostream>` |

### Tips for Learning

- C++ is a superset of C with additional features
- `std::cout` is the C++ way to print (replaces `printf`)
- `std::endl` adds a newline and flushes the buffer
- The `std::` prefix means these are from the "standard" namespace
