# Level 7: Function Pseudocode

> **LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.c\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Functions are the building blocks of organized code! Today you'll master algorithms that use functions for modularity, reusability, and clean program design. You'll learn to break complex problems into smaller, manageable functions.

---

### Learning Goals

- [ ] Design algorithms using function decomposition
- [ ] Implement function-based program architecture
- [ ] Master parameter passing and return values
- [ ] Create reusable function libraries
- [ ] Develop modular programming practices

---

### Function-Based Design Principles

**Function Decomposition:**
1. **Single Responsibility**: Each function does one thing well
2. **Clear Interface**: Well-defined inputs and outputs
3. **Reusability**: Functions can be used in multiple contexts
4. **Testability**: Individual functions can be tested separately
5. **Maintainability**: Changes are localized to specific functions

**Function Types:**
- [ ] **Input Functions**: Get data from users
- [ ] **Processing Functions**: Perform calculations
- [ ] **Output Functions**: Display results
- [ ] **Utility Functions**: Provide common operations
- [ ] **Main Function**: Orchestrates the program flow

---

### Your Task

**Translate each function-based pseudocode algorithm into working C code with proper function decomposition.**

---

## Algorithm 1: Calculator Program with Functions

**Pseudocode:**
```
Algorithm: Modular Calculator Program

Function: display_menu()
    Display "=== Calculator Menu ==="
    Display "1. Addition"
    Display "2. Subtraction"
    Display "3. Multiplication"
    Display "4. Division"
    Display "5. Exit"
    Display "Choose operation (1-5): "

Function: get_number(prompt)
    Display prompt
    Get number from user
    Return number

Function: perform_addition(a, b)
    Return a + b

Function: perform_subtraction(a, b)
    Return a - b

Function: perform_multiplication(a, b)
    Return a * b

Function: perform_division(a, b)
    If b equals 0:
        Display " Error: Division by zero!"
        Return 0
    Else:
        Return a ÷ b

Function: display_result(operation, a, b, result)
    Display "Result: " + a + " " + operation + " " + b + " = " + result

Main Algorithm:
1. Initialize running to true
2. While running is true:
   a. Call display_menu()
   b. Get choice from user
   c. If choice >= 1 and choice <= 4:
      i. Set num1 = get_number("Enter first number: ")
      ii. Set num2 = get_number("Enter second number: ")
      iii. If choice is 1:
         i. Set result = perform_addition(num1, num2)
         ii. Call display_result("+", num1, num2, result)
      iv. Else if choice is 2:
         i. Set result = perform_subtraction(num1, num2)
         ii. Call display_result("-", num1, num2, result)
      v. Else if choice is 3:
         i. Set result = perform_multiplication(num1, num2)
         ii. Call display_result("*", num1, num2, result)
      vi. Else if choice is 4:
         i. Set result = perform_division(num1, num2)
         ii. If result is not 0 or num2 is not 0:
            i. Call display_result("/", num1, num2, result)
   d. Else if choice is 5:
      i. Set running to false
   e. Else:
      i. Display " Invalid choice!"
3. Display "Thank you for using the calculator! "
```

**Function Design:**
- [ ] `display_menu()`: Handles UI display
- [ ] `get_number()`: Handles input with prompt
- [ ] `perform_*()`: Pure calculation functions
- [ ] `display_result()`: Handles output formatting

**Your Task:** Build a modular calculator program.

---

## Algorithm 2: Student Grade Management System

**Pseudocode:**
```
Algorithm: Student Grade Management with Functions

Function: display_main_menu()
    Display "=== Grade Management System ==="
    Display "1. Add Student"
    Display "2. View All Students"
    Display "3. Calculate Class Average"
    Display "4. Find Top Performer"
    Display "5. Exit"
    Display "Choose option (1-5): "

Function: add_student(students, grades, count)
    If count < 50:
        Display "Enter student name: "
        Get name from user
        Display "Enter grade (0-100): "
        Get grade from user
        If grade is valid (0-100):
            Store name in students[count]
            Store grade in grades[count]
            Add 1 to count
            Display " Student added successfully!"
            Return true
        Else:
            Display " Invalid grade!"
            Return false
    Else:
        Display " Student list is full!"
        Return false

Function: display_all_students(students, grades, count)
    If count > 0:
        Display "=== Student List ==="
        For i from 0 to count - 1:
            Display (i + 1) + ". " + students[i] + " - " + grades[i] + "%"
    Else:
        Display " No students in the system."

Function: calculate_class_average(grades, count)
    If count > 0:
        Initialize sum to 0
        For i from 0 to count - 1:
            Add grades[i] to sum
        Return sum ÷ count
    Else:
        Return 0

Function: find_top_performer(students, grades, count)
    If count > 0:
        Initialize max_grade to grades[0]
        Initialize top_student to students[0]
        For i from 1 to count - 1:
            If grades[i] > max_grade:
                Set max_grade to grades[i]
                Set top_student to students[i]
        Return top_student and max_grade
    Else:
        Return "No students" and 0

Main Algorithm:
1. Initialize students array (50 names)
2. Initialize grades array (50 grades)
3. Initialize student_count to 0
4. Initialize running to true
5. While running is true:
   a. Call display_main_menu()
   b. Get choice from user
   c. If choice is 1:
      i. Call add_student(students, grades, student_count)
   d. Else if choice is 2:
      i. Call display_all_students(students, grades, student_count)
   e. Else if choice is 3:
      i. Set average = calculate_class_average(grades, student_count)
      ii. If student_count > 0:
         i. Display " Class Average: " + average + "%"
      iii. Else:
         i. Display " No students to average."
   f. Else if choice is 4:
      i. Call find_top_performer(students, grades, student_count)
      ii. Get top_student and max_grade from result
      iii. If top_student is not "No students":
         i. Display " Top Performer: " + top_student + " (" + max_grade + "%)"
      iv. Else:
         i. Display " No students in the system."
   g. Else if choice is 5:
      i. Set running to false
   h. Else:
      i. Display " Invalid choice!"
6. Display "Thank you for using Grade Management System! "
```

**Function Design:**
- [ ] `display_main_menu()`: UI function
- [ ] `add_student()`: Input/modification function
- [ ] `display_all_students()`: Output function
- [ ] `calculate_class_average()`: Processing function
- [ ] `find_top_performer()`: Analysis function

**Your Task:** Create a modular student grade management system.

---

## Algorithm 3: Library Book System

**Pseudocode:**
```
Algorithm: Library Management System with Functions

Function: display_library_menu()
    Display "=== Library Management ==="
    Display "1. Add Book"
    Display "2. Search Books"
    Display "3. Display All Books"
    Display "4. Check Out Book"
    Display "5. Return Book"
    Display "6. Exit"
    Display "Choose option (1-6): "

Function: add_book(titles, authors, available, count)
    If count < 100:
        Display "Enter book title: "
        Get title from user
        Display "Enter author name: "
        Get author from user
        Store title in titles[count]
        Store author in authors[count]
        Set available[count] to true
        Add 1 to count
        Display " Book added successfully!"
        Return true
    Else:
        Display " Library is full!"
        Return false

Function: search_books(titles, authors, available, count, search_term)
    Initialize found_count to 0
    Display "=== Search Results for '" + search_term + "' ==="
    For i from 0 to count - 1:
        If titles[i] contains search_term OR authors[i] contains search_term:
            Display " " + titles[i] + " by " + authors[i]
            If available[i] is true:
                Display "   Status: Available "
            Else:
                Display "   Status: Checked Out "
            Add 1 to found_count
    If found_count is 0:
        Display " No books found matching '" + search_term + "'"
    Return found_count

Function: display_all_books(titles, authors, available, count)
    If count > 0:
        Display "=== Library Collection ==="
        For i from 0 to count - 1:
            Display (i + 1) + ". " + titles[i] + " by " + authors[i]
            If available[i] is true:
                Display "   Status: Available "
            Else:
                Display "   Status: Checked Out "
    Else:
        Display " Library is empty."

Function: checkout_book(titles, available, count, book_title)
    For i from 0 to count - 1:
        If titles[i] equals book_title AND available[i] is true:
            Set available[i] to false
            Display " '" + book_title + "' checked out successfully!"
            Return true
    Display " Book not found or already checked out."
    Return false

Function: return_book(titles, available, count, book_title)
    For i from 0 to count - 1:
        If titles[i] equals book_title AND available[i] is false:
            Set available[i] to true
            Display " '" + book_title + "' returned successfully!"
            Return true
    Display " Book not found or not checked out."
    Return false

Main Algorithm:
1. Initialize titles array (100 books)
2. Initialize authors array (100 authors)
3. Initialize available array (100 booleans)
4. Initialize book_count to 0
5. Initialize running to true
6. While running is true:
   a. Call display_library_menu()
   b. Get choice from user
   c. If choice is 1:
      i. Call add_book(titles, authors, available, book_count)
   d. Else if choice is 2:
      i. Display "Enter search term: "
      ii. Get search_term from user
      iii. Call search_books(titles, authors, available, book_count, search_term)
   e. Else if choice is 3:
      i. Call display_all_books(titles, authors, available, book_count)
   f. Else if choice is 4:
      i. Display "Enter book title to check out: "
      ii. Get book_title from user
      iii. Call checkout_book(titles, available, book_count, book_title)
   g. Else if choice is 5:
      i. Display "Enter book title to return: "
      ii. Get book_title from user
      iii. Call return_book(titles, available, book_count, book_title)
   h. Else if choice is 6:
      i. Set running to false
   i. Else:
      i. Display " Invalid choice!"
7. Display "Thank you for using Library Management System! "
```

**Function Design:**
- [ ] `display_library_menu()`: UI function
- [ ] `add_book()`: Creation function
- [ ] `search_books()`: Query function
- [ ] `display_all_books()`: Display function
- [ ] `checkout_book()` & `return_book()`: Modification functions

**Your Task:** Build a comprehensive library management system.

---

## Algorithm 4: Math Quiz Game

**Pseudocode:**
```
Algorithm: Interactive Math Quiz with Functions

Function: generate_question()
    Randomly select operation from ["+", "-", "*", "/"]
    Generate num1 as random number 1-20
    Generate num2 as random number 1-20
    If operation is "/":
        Set num1 to num1 × num2 (ensure clean division)
    Return num1, operation, num2

Function: calculate_answer(num1, operation, num2)
    If operation is "+":
        Return num1 + num2
    Else if operation is "-":
        Return num1 - num2
    Else if operation is "*":
        Return num1 × num2
    Else if operation is "/":
        Return num1 ÷ num2

Function: display_question(num1, operation, num2, question_number)
    Display "Question " + question_number + ":"
    Display "What is " + num1 + " " + operation + " " + num2 + "?"

Function: get_user_answer()
    Display "Your answer: "
    Get answer from user
    Return answer

Function: check_answer(user_answer, correct_answer)
    If user_answer equals correct_answer:
        Display " Correct!"
        Return true
    Else:
        Display " Incorrect. The answer is " + correct_answer
        Return false

Function: display_score(correct_answers, total_questions)
    Calculate percentage = (correct_answers ÷ total_questions) × 100
    Display "=== Quiz Complete ==="
    Display "Score: " + correct_answers + "/" + total_questions + " (" + percentage + "%)"
    If percentage >= 90:
        Display " Excellent! Math Master!"
    Else if percentage >= 70:
        Display " Good job!"
    Else if percentage >= 50:
        Display " Keep practicing!"
    Else:
        Display " Don't give up! Try again!"

Main Algorithm:
1. Display "=== Math Quiz Game ==="
2. Display "How many questions? (1-20): "
3. Get num_questions from user
4. While num_questions < 1 or num_questions > 20:
   a. Display " Please enter 1-20 questions."
   b. Get num_questions from user
5. Initialize correct_count to 0
6. For question_num from 1 to num_questions:
   a. Call generate_question()
   b. Get num1, operation, num2 from result
   c. Call display_question(num1, operation, num2, question_num)
   d. Set correct_answer = calculate_answer(num1, operation, num2)
   e. Set user_answer = get_user_answer()
   f. If check_answer(user_answer, correct_answer) is true:
      i. Add 1 to correct_count
   g. Display blank line
7. Call display_score(correct_count, num_questions)
8. Display "Thanks for playing! "
```

**Function Design:**
- [ ] `generate_question()`: Random question creation
- [ ] `calculate_answer()`: Answer computation
- [ ] `display_question()`: Question presentation
- [ ] `get_user_answer()`: Input handling
- [ ] `check_answer()`: Validation and feedback
- [ ] `display_score()`: Results presentation

**Your Task:** Create an interactive math quiz game.

---

## Algorithm 5: Bank Account Manager

**Pseudocode:**
```
Algorithm: Bank Account Management with Functions

Function: display_account_menu()
    Display "=== Bank Account Menu ==="
    Display "1. Check Balance"
    Display "2. Deposit Money"
    Display "3. Withdraw Money"
    Display "4. View Transaction History"
    Display "5. Exit"
    Display "Choose option (1-5): "

Function: display_balance(balance)
    Display " Current Balance: $" + balance

Function: deposit_money(balance, amount)
    If amount > 0:
        Add amount to balance
        Display " Deposit successful! New balance: $" + balance
        Return balance
    Else:
        Display " Deposit amount must be positive!"
        Return original balance

Function: withdraw_money(balance, amount)
    If amount > 0:
        If amount <= balance:
            Subtract amount from balance
            Display " Withdrawal successful! New balance: $" + balance
            Return balance
        Else:
            Display " Insufficient funds!"
            Return original balance
    Else:
        Display " Withdrawal amount must be positive!"
        Return original balance

Function: add_transaction(transactions, amounts, descriptions, count, amount, description)
    If count < 100:
        Set transactions[count] to current date/time (simplified)
        Set amounts[count] to amount
        Set descriptions[count] to description
        Add 1 to count
        Return true
    Else:
        Display " Transaction history is full!"
        Return false

Function: display_transaction_history(transactions, amounts, descriptions, count)
    If count > 0:
        Display "=== Transaction History ==="
        For i from count - 1 down to 0:  // Most recent first
            Display transactions[i] + " - " + descriptions[i] + " $" + amounts[i]
    Else:
        Display " No transactions yet."

Main Algorithm:
1. Initialize balance to 1000.00
2. Initialize transactions array (100 entries)
3. Initialize amounts array (100 entries)
4. Initialize descriptions array (100 entries)
5. Initialize transaction_count to 0
6. Initialize running to true
7. While running is true:
   a. Call display_account_menu()
   b. Get choice from user
   c. If choice is 1:
      i. Call display_balance(balance)
   d. Else if choice is 2:
      i. Display "Enter deposit amount: $"
      ii. Get amount from user
      iii. Set balance = deposit_money(balance, amount)
      iv. If amount > 0:
         i. Call add_transaction(transactions, amounts, descriptions, transaction_count, amount, "Deposit")
   e. Else if choice is 3:
      i. Display "Enter withdrawal amount: $"
      ii. Get amount from user
      iii. Set balance = withdraw_money(balance, amount)
      iv. If amount > 0 and amount <= original balance:
         i. Call add_transaction(transactions, amounts, descriptions, transaction_count, -amount, "Withdrawal")
   f. Else if choice is 4:
      i. Call display_transaction_history(transactions, amounts, descriptions, transaction_count)
   g. Else if choice is 5:
      i. Set running to false
   h. Else:
      i. Display " Invalid choice!"
8. Display "Thank you for banking with us! "
```

**Function Design:**
- [ ] `display_account_menu()`: UI function
- [ ] `display_balance()`: Information display
- [ ] `deposit_money()` & `withdraw_money()`: Transaction functions
- [ ] `add_transaction()`: Record keeping
- [ ] `display_transaction_history()`: History display

**Your Task:** Build a bank account management system.

---

## Algorithm 6: Text Analyzer

**Pseudocode:**
```
Algorithm: Text Analysis Tool with Functions

Function: count_words(text)
    Initialize word_count to 0
    Initialize in_word to false
    For each character in text:
        If character is letter and in_word is false:
            Set in_word to true
            Add 1 to word_count
        Else if character is not letter:
            Set in_word to false
    Return word_count

Function: count_sentences(text)
    Initialize sentence_count to 0
    For each character in text:
        If character is "." or "!" or "?":
            Add 1 to sentence_count
    Return sentence_count

Function: count_characters(text)
    Return length of text

Function: calculate_average_word_length(text, word_count)
    If word_count > 0:
        Initialize total_length to 0
        Initialize current_word_length to 0
        Initialize in_word to false
        For each character in text:
            If character is letter:
                Set in_word to true
                Add 1 to current_word_length
            Else if in_word is true:
                Add current_word_length to total_length
                Set current_word_length to 0
                Set in_word to false
        If in_word is true:  // Handle last word
            Add current_word_length to total_length
        Return total_length ÷ word_count
    Else:
        Return 0

Function: find_most_frequent_character(text)
    Initialize char_counts array (256 elements, all 0)
    For each character in text:
        If character is not space:
            Add 1 to char_counts[character]
    Initialize max_count to 0
    Initialize most_frequent to space
    For i from 0 to 255:
        If char_counts[i] > max_count:
            Set max_count to char_counts[i]
            Set most_frequent to character i
    Return most_frequent and max_count

Function: display_analysis(text)
    Set word_count = count_words(text)
    Set sentence_count = count_sentences(text)
    Set char_count = count_characters(text)
    Set avg_word_length = calculate_average_word_length(text, word_count)
    Call find_most_frequent_character(text)
    Get most_frequent and freq_count from result
    
    Display "=== Text Analysis Results ==="
    Display "Characters: " + char_count
    Display "Words: " + word_count
    Display "Sentences: " + sentence_count
    Display "Average word length: " + avg_word_length + " characters"
    Display "Most frequent character: '" + most_frequent + "' (" + freq_count + " times)"

Main Algorithm:
1. Display "=== Text Analyzer ==="
2. Display "Enter text to analyze (max 1000 characters):"
3. Get text from user (allow multiple lines until empty line)
4. If text is not empty:
   a. Call display_analysis(text)
5. Else:
   a. Display " No text entered."
6. Display "Analysis complete! "
```

**Function Design:**
- [ ] `count_words()`: Word counting logic
- [ ] `count_sentences()`: Sentence counting logic
- [ ] `count_characters()`: Character counting
- [ ] `calculate_average_word_length()`: Statistical calculation
- [ ] `find_most_frequent_character()`: Character frequency analysis
- [ ] `display_analysis()`: Results presentation

**Your Task:** Create a comprehensive text analysis tool.

---

### Function Design Best Practices

**Function Naming:**
```c
// Good - clear and descriptive
int calculate_circle_area(float radius);
void display_student_report(Student s);
int validate_user_input(char* input);

// Bad - unclear purpose
int calc(float x);
void process();
int check(char* str);
```

**Parameter Design:**
```c
// Good - clear parameter purposes
void transfer_money(Account* from, Account* to, float amount);

// Bad - unclear what parameters do
void process(float a, float b, int c);
```

**Return Value Design:**
```c
// Good - clear success/failure indication
int save_file(const char* filename);  // Returns 0 on success, -1 on error

// Bad - unclear return meaning
int do_something();
```

---

### Success Checklist

**For Each Algorithm:**
- [ ] Implemented proper function decomposition
- [ ] Used appropriate function signatures
- [ ] Handled parameters and return values correctly
- [ ] Created modular, reusable functions
- [ ] Maintained clean separation of concerns

**Function Quality:**
- [ ] Functions have single responsibilities
- [ ] Clear and descriptive function names
- [ ] Proper parameter validation
- [ ] Consistent error handling
- [ ] Good documentation through naming

---

### Try This (Optional Challenges)

1. **Add Input Validation**: Ensure all functions handle invalid inputs
2. **Create Function Libraries**: Group related functions into modules
3. **Add Error Handling**: Implement proper error codes and messages
4. **Performance Optimization**: Optimize functions for speed and memory

---

## Function Architecture Patterns

### Layered Architecture
```
Presentation Layer (UI functions)
    ↓
Business Logic Layer (processing functions)
    ↓
Data Access Layer (storage/retrieval functions)
```

### Pipeline Pattern
```c
// Data flows through a series of transformations
Result process_data(Input data) {
    data = validate_input(data);
    data = normalize_data(data);
    data = process_data(data);
    data = format_output(data);
    return data;
}
```

### Factory Pattern
```c
// Functions that create other functions/objects
Calculator* create_calculator(CalculationType type) {
    switch (type) {
        case BASIC: return new BasicCalculator();
        case SCIENTIFIC: return new ScientificCalculator();
        default: return NULL;
    }
}
```

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Calculator Program with Functions

```c
#include <stdio.h>

void display_menu() {
    printf("=== Calculator Menu ===\n");
    printf("1. Addition\n");
    printf("2. Subtraction\n");
    printf("3. Multiplication\n");
    printf("4. Division\n");
    printf("5. Exit\n");
    printf("Choose operation (1-5): ");
}

float get_number(const char* prompt) {
    float number;
    printf("%s", prompt);
    scanf("%f", &number);
    return number;
}

float perform_addition(float a, float b) {
    return a + b;
}

float perform_subtraction(float a, float b) {
    return a - b;
}

float perform_multiplication(float a, float b) {
    return a * b;
}

float perform_division(float a, float b) {
    if (b == 0) {
        printf(" Error: Division by zero!\n");
        return 0;
    }
    return a / b;
}

void display_result(const char* operation, float a, float b, float result) {
    printf("Result: %.2f %s %.2f = %.2f\n", a, operation, b, result);
}

int main() {
    int running = 1;
    
    while (running) {
        display_menu();
        int choice;
        scanf("%d", &choice);
        
        if (choice >= 1 && choice <= 4) {
            float num1 = get_number("Enter first number: ");
            float num2 = get_number("Enter second number: ");
            float result;
            
            switch (choice) {
                case 1:
                    result = perform_addition(num1, num2);
                    display_result("+", num1, num2, result);
                    break;
                case 2:
                    result = perform_subtraction(num1, num2);
                    display_result("-", num1, num2, result);
                    break;
                case 3:
                    result = perform_multiplication(num1, num2);
                    display_result("*", num1, num2, result);
                    break;
                case 4:
                    result = perform_division(num1, num2);
                    if (num2 != 0) {
                        display_result("/", num1, num2, result);
                    }
                    break;
            }
        } else if (choice == 5) {
            running = 0;
        } else {
            printf(" Invalid choice!\n");
        }
    }
    
    printf("Thank you for using the calculator! \n");
    return 0;
}
```

**Key Concepts:**
- [ ] Modular function design with single responsibilities
- [ ] Clean separation between UI, input, processing, and output
- [ ] Proper parameter passing and return values
- [ ] Error handling in division function

---

### Algorithm 2: Student Grade Management System

```c
#include <stdio.h>
# include <string.h>

void display_main_menu() {
    printf("=== Grade Management System ===\n");
    printf("1. Add Student\n");
    printf("2. View All Students\n");
    printf("3. Calculate Class Average\n");
    printf("4. Find Top Performer\n");
    printf("5. Exit\n");
    printf("Choose option (1-5): ");
}

int add_student(char students[50][50], float grades[50], int* count) {
    if (*count < 50) {
        char name[50];
        float grade;
        
        printf("Enter student name: ");
        scanf("%s", name);
        printf("Enter grade (0-100): ");
        scanf("%f", &grade);
        
        if (grade >= 0 && grade <= 100) {
            strcpy(students[*count], name);
            grades[*count] = grade;
            (*count)++;
            printf(" Student added successfully!\n");
            return 1;
        } else {
            printf(" Invalid grade!\n");
            return 0;
        }
    } else {
        printf(" Student list is full!\n");
        return 0;
    }
}

void display_all_students(char students[50][50], float grades[50], int count) {
    if (count > 0) {
        printf("=== Student List ===\n");
        for (int i = 0; i < count; i++) {
            printf("%d. %s - %.1f%%\n", i + 1, students[i], grades[i]);
        }
    } else {
        printf(" No students in the system.\n");
    }
}

float calculate_class_average(float grades[50], int count) {
    if (count > 0) {
        float sum = 0;
        for (int i = 0; i < count; i++) {
            sum += grades[i];
        }
        return sum / count;
    }
    return 0;
}

void find_top_performer(char students[50][50], float grades[50], int count, 
                       char* top_student, float* max_grade) {
    if (count > 0) {
        *max_grade = grades[0];
        strcpy(top_student, students[0]);
        
        for (int i = 1; i < count; i++) {
            if (grades[i] > *max_grade) {
                *max_grade = grades[i];
                strcpy(top_student, students[i]);
            }
        }
    } else {
        strcpy(top_student, "No students");
        *max_grade = 0;
    }
}

int main() {
    char students[50][50];
    float grades[50];
    int student_count = 0;
    int running = 1;
    
    while (running) {
        display_main_menu();
        int choice;
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                add_student(students, grades, &student_count);
                break;
            case 2:
                display_all_students(students, grades, student_count);
                break;
            case 3: {
                float average = calculate_class_average(grades, student_count);
                if (student_count > 0) {
                    printf(" Class Average: %.1f%%\n", average);
                } else {
                    printf(" No students to average.\n");
                }
                break;
            }
            case 4: {
                char top_student[50];
                float max_grade;
                find_top_performer(students, grades, student_count, top_student, &max_grade);
                
                if (strcmp(top_student, "No students") != 0) {
                    printf(" Top Performer: %s (%.1f%%)\n", top_student, max_grade);
                } else {
                    printf(" No students in the system.\n");
                }
                break;
            }
            case 5:
                running = 0;
                break;
            default:
                printf(" Invalid choice!\n");
                break;
        }
    }
    
    printf("Thank you for using Grade Management System! \n");
    return 0;
}
```

**Key Concepts:**
- [ ] Array parameters with pointers for modification
- [ ] String handling with character arrays
- [ ] Statistical calculations in separate functions
- [ ] Pointer parameters for returning multiple values

---

### Algorithm 3: Library Book System

```c
#include <stdio.h>
# include <string.h>

void display_library_menu() {
    printf("=== Library Management ===\n");
    printf("1. Add Book\n");
    printf("2. Search Books\n");
    printf("3. Display All Books\n");
    printf("4. Check Out Book\n");
    printf("5. Return Book\n");
    printf("6. Exit\n");
    printf("Choose option (1-6): ");
}

int add_book(char titles[100][100], char authors[100][50], int available[100], int* count) {
    if (*count < 100) {
        char title[100], author[50];
        
        printf("Enter book title: ");
        getchar(); // Clear newline
        fgets(title, sizeof(title), stdin);
        title[strcspn(title, "\n")] = '\0'; // Remove newline
        
        printf("Enter author name: ");
        fgets(author, sizeof(author), stdin);
        author[strcspn(author, "\n")] = '\0';
        
        strcpy(titles[*count], title);
        strcpy(authors[*count], author);
        available[*count] = 1; // true
        (*count)++;
        
        printf(" Book added successfully!\n");
        return 1;
    } else {
        printf(" Library is full!\n");
        return 0;
    }
}

int search_books(char titles[100][100], char authors[100][50], int available[100], 
                int count, const char* search_term) {
    int found_count = 0;
    printf("=== Search Results for '%s' ===\n", search_term);
    
    for (int i = 0; i < count; i++) {
        if (strstr(titles[i], search_term) != NULL || strstr(authors[i], search_term) != NULL) {
            printf(" %s by %s\n", titles[i], authors[i]);
            printf("   Status: %s\n", available[i] ? "Available " : "Checked Out ");
            found_count++;
        }
    }
    
    if (found_count == 0) {
        printf(" No books found matching '%s'\n", search_term);
    }
    
    return found_count;
}

void display_all_books(char titles[100][100], char authors[100][50], int available[100], int count) {
    if (count > 0) {
        printf("=== Library Collection ===\n");
        for (int i = 0; i < count; i++) {
            printf("%d. %s by %s\n", i + 1, titles[i], authors[i]);
            printf("   Status: %s\n", available[i] ? "Available " : "Checked Out ");
        }
    } else {
        printf(" Library is empty.\n");
    }
}

int checkout_book(char titles[100][100], int available[100], int count, const char* book_title) {
    for (int i = 0; i < count; i++) {
        if (strcmp(titles[i], book_title) == 0 && available[i]) {
            available[i] = 0; // false
            printf(" '%s' checked out successfully!\n", book_title);
            return 1;
        }
    }
    printf(" Book not found or already checked out.\n");
    return 0;
}

int return_book(char titles[100][100], int available[100], int count, const char* book_title) {
    for (int i = 0; i < count; i++) {
        if (strcmp(titles[i], book_title) == 0 && !available[i]) {
            available[i] = 1; // true
            printf(" '%s' returned successfully!\n", book_title);
            return 1;
        }
    }
    printf(" Book not found or not checked out.\n");
    return 0;
}

int main() {
    char titles[100][100];
    char authors[100][50];
    int available[100];
    int book_count = 0;
    int running = 1;
    
    while (running) {
        display_library_menu();
        int choice;
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                add_book(titles, authors, available, &book_count);
                break;
            case 2: {
                char search_term[100];
                printf("Enter search term: ");
                getchar(); // Clear newline
                fgets(search_term, sizeof(search_term), stdin);
                search_term[strcspn(search_term, "\n")] = '\0';
                search_books(titles, authors, available, book_count, search_term);
                break;
            }
            case 3:
                display_all_books(titles, authors, available, book_count);
                break;
            case 4: {
                char book_title[100];
                printf("Enter book title to check out: ");
                getchar(); // Clear newline
                fgets(book_title, sizeof(book_title), stdin);
                book_title[strcspn(book_title, "\n")] = '\0';
                checkout_book(titles, available, book_count, book_title);
                break;
            }
            case 5: {
                char book_title[100];
                printf("Enter book title to return: ");
                getchar(); // Clear newline
                fgets(book_title, sizeof(book_title), stdin);
                book_title[strcspn(book_title, "\n")] = '\0';
                return_book(titles, available, book_count, book_title);
                break;
            }
            case 6:
                running = 0;
                break;
            default:
                printf(" Invalid choice!\n");
                break;
        }
    }
    
    printf("Thank you for using Library Management System! \n");
    return 0;
}
```

**Key Concepts:**
- [ ] Complex string handling with fgets and newline removal
- [ ] Multiple 2D arrays for related data
- [ ] Search functionality with string matching
- [ ] State management with boolean arrays

---

### Algorithm 4: Math Quiz Game

```c
#include <stdio.h>
# include <stdlib.h>
# include <time.h>

void generate_question(int* num1, char* operation, int* num2) {
    *operation = "+-*/"[rand() % 4]; // Random operation
    
    *num1 = rand() % 20 + 1;
    *num2 = rand() % 20 + 1;
    
    // Ensure clean division
    if (*operation == '/') {
        *num1 = *num2 * (rand() % 10 + 1);
    }
}

int calculate_answer(int num1, char operation, int num2) {
    switch (operation) {
        case '+': return num1 + num2;
        case '-': return num1 - num2;
        case '*': return num1 * num2;
        case '/': return num1 / num2;
        default: return 0;
    }
}

void display_question(int num1, char operation, int num2, int question_number) {
    printf("Question %d:\n", question_number);
    printf("What is %d %c %d?\n", num1, operation, num2);
}

int get_user_answer() {
    int answer;
    printf("Your answer: ");
    scanf("%d", &answer);
    return answer;
}

int check_answer(int user_answer, int correct_answer) {
    if (user_answer == correct_answer) {
        printf(" Correct!\n");
        return 1;
    } else {
        printf(" Incorrect. The answer is %d\n", correct_answer);
        return 0;
    }
}

void display_score(int correct_answers, int total_questions) {
    float percentage = (float)correct_answers / total_questions * 100;
    
    printf("=== Quiz Complete ===\n");
    printf("Score: %d/%d (%.1f%%)\n", correct_answers, total_questions, percentage);
    
    if (percentage >= 90) {
        printf(" Excellent! Math Master!\n");
    } else if (percentage >= 70) {
        printf(" Good job!\n");
    } else if (percentage >= 50) {
        printf(" Keep practicing!\n");
    } else {
        printf(" Don't give up! Try again!\n");
    }
}

int main() {
    srand(time(NULL)); // Seed random number generator
    
    printf("=== Math Quiz Game ===\n");
    printf("How many questions? (1-20): ");
    int num_questions;
    scanf("%d", &num_questions);
    
    while (num_questions < 1 || num_questions > 20) {
        printf(" Please enter 1-20 questions.\n");
        scanf("%d", &num_questions);
    }
    
    int correct_count = 0;
    
    for (int question_num = 1; question_num <= num_questions; question_num++) {
        int num1, num2;
        char operation;
        
        generate_question(&num1, &operation, &num2);
        display_question(num1, operation, num2, question_num);
        
        int correct_answer = calculate_answer(num1, operation, num2);
        int user_answer = get_user_answer();
        
        if (check_answer(user_answer, correct_answer)) {
            correct_count++;
        }
        
        printf("\n");
    }
    
    display_score(correct_count, num_questions);
    printf("Thanks for playing! \n");
    
    return 0;
}
```

**Key Concepts:**
- [ ] Random number generation for question creation
- [ ] Pointer parameters for returning multiple values
- [ ] Modular design with single-responsibility functions
- [ ] Game-like interactive flow

---

### Algorithm 5: Bank Account Manager

```c
#include <stdio.h>
# include <string.h>

void display_account_menu() {
    printf("=== Bank Account Menu ===\n");
    printf("1. Check Balance\n");
    printf("2. Deposit Money\n");
    printf("3. Withdraw Money\n");
    printf("4. View Transaction History\n");
    printf("5. Exit\n");
    printf("Choose option (1-5): ");
}

void display_balance(float balance) {
    printf(" Current Balance: $%.2f\n", balance);
}

float deposit_money(float balance, float amount) {
    if (amount > 0) {
        balance += amount;
        printf(" Deposit successful! New balance: $%.2f\n", balance);
        return balance;
    } else {
        printf(" Deposit amount must be positive!\n");
        return balance;
    }
}

float withdraw_money(float balance, float amount) {
    if (amount > 0) {
        if (amount <= balance) {
            balance -= amount;
            printf(" Withdrawal successful! New balance: $%.2f\n", balance);
            return balance;
        } else {
            printf(" Insufficient funds!\n");
            return balance;
        }
    } else {
        printf(" Withdrawal amount must be positive!\n");
        return balance;
    }
}

int add_transaction(char transactions[100][20], float amounts[100], 
                   char descriptions[100][30], int* count, float amount, 
                   const char* description) {
    if (*count < 100) {
        // Simplified transaction recording
        sprintf(transactions[*count], "Transaction %d", *count + 1);
        amounts[*count] = amount;
        strcpy(descriptions[*count], description);
        (*count)++;
        return 1;
    } else {
        printf(" Transaction history is full!\n");
        return 0;
    }
}

void display_transaction_history(char transactions[100][20], float amounts[100], 
                               char descriptions[100][30], int count) {
    if (count > 0) {
        printf("=== Transaction History ===\n");
        for (int i = count - 1; i >= 0; i--) { // Most recent first
            printf("%s - %s $%.2f\n", transactions[i], descriptions[i], amounts[i]);
        }
    } else {
        printf(" No transactions yet.\n");
    }
}

int main() {
    float balance = 1000.00;
    char transactions[100][20];
    float amounts[100];
    char descriptions[100][30];
    int transaction_count = 0;
    int running = 1;
    
    while (running) {
        display_account_menu();
        int choice;
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                display_balance(balance);
                break;
            case 2: {
                printf("Enter deposit amount: $");
                float amount;
                scanf("%f", &amount);
                float old_balance = balance;
                balance = deposit_money(balance, amount);
                if (amount > 0) {
                    add_transaction(transactions, amounts, descriptions, 
                                   &transaction_count, amount, "Deposit");
                }
                break;
            }
            case 3: {
                printf("Enter withdrawal amount: $");
                float amount;
                scanf("%f", &amount);
                float old_balance = balance;
                balance = withdraw_money(balance, amount);
                if (amount > 0 && amount <= old_balance) {
                    add_transaction(transactions, amounts, descriptions, 
                                   &transaction_count, -amount, "Withdrawal");
                }
                break;
            }
            case 4:
                display_transaction_history(transactions, amounts, descriptions, transaction_count);
                break;
            case 5:
                running = 0;
                break;
            default:
                printf(" Invalid choice!\n");
                break;
        }
    }
    
    printf("Thank you for banking with us! \n");
    return 0;
}
```

**Key Concepts:**
- [ ] Financial transaction processing
- [ ] Balance validation and updates
- [ ] Transaction history management
- [ ] Pointer parameters for array modification

---

### Algorithm 6: Text Analyzer

```c
#include <stdio.h>
# include <string.h>
# include <ctype.h>

int count_words(const char* text) {
    int word_count = 0;
    int in_word = 0;
    
    for (int i = 0; text[i] != '\0'; i++) {
        if (isalpha(text[i]) && !in_word) {
            in_word = 1;
            word_count++;
        } else if (!isalpha(text[i])) {
            in_word = 0;
        }
    }
    
    return word_count;
}

int count_sentences(const char* text) {
    int sentence_count = 0;
    
    for (int i = 0; text[i] != '\0'; i++) {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?') {
            sentence_count++;
        }
    }
    
    return sentence_count;
}

int count_characters(const char* text) {
    return strlen(text);
}

float calculate_average_word_length(const char* text, int word_count) {
    if (word_count == 0) return 0.0;
    
    int total_length = 0;
    int current_word_length = 0;
    int in_word = 0;
    
    for (int i = 0; text[i] != '\0'; i++) {
        if (isalpha(text[i])) {
            in_word = 1;
            current_word_length++;
        } else if (in_word) {
            total_length += current_word_length;
            current_word_length = 0;
            in_word = 0;
        }
    }
    
    // Handle last word
    if (in_word) {
        total_length += current_word_length;
    }
    
    return (float)total_length / word_count;
}

void find_most_frequent_character(const char* text, char* most_frequent, int* freq_count) {
    int char_counts[256] = {0};
    
    for (int i = 0; text[i] != '\0'; i++) {
        if (text[i] != ' ') {
            char_counts[(unsigned char)text[i]]++;
        }
    }
    
    int max_count = 0;
    char most_freq = ' ';
    
    for (int i = 0; i < 256; i++) {
        if (char_counts[i] > max_count) {
            max_count = char_counts[i];
            most_freq = (char)i;
        }
    }
    
    *most_frequent = most_freq;
    *freq_count = max_count;
}

void display_analysis(const char* text) {
    int word_count = count_words(text);
    int sentence_count = count_sentences(text);
    int char_count = count_characters(text);
    float avg_word_length = calculate_average_word_length(text, word_count);
    
    char most_frequent;
    int freq_count;
    find_most_frequent_character(text, &most_frequent, &freq_count);
    
    printf("=== Text Analysis Results ===\n");
    printf("Characters: %d\n", char_count);
    printf("Words: %d\n", word_count);
    printf("Sentences: %d\n", sentence_count);
    printf("Average word length: %.1f characters\n", avg_word_length);
    printf("Most frequent character: '%c' (%d times)\n", most_frequent, freq_count);
}

int main() {
    printf("=== Text Analyzer ===\n");
    printf("Enter text to analyze (max 1000 characters):\n");
    
    char text[1001];
    fgets(text, sizeof(text), stdin);
    
    // Remove trailing newline
    text[strcspn(text, "\n")] = '\0';
    
    if (strlen(text) > 0) {
        display_analysis(text);
    } else {
        printf(" No text entered.\n");
    }
    
    printf("Analysis complete! \n");
    return 0;
}
```

**Key Concepts:**
- [ ] Text processing algorithms
- [ ] Character-by-character analysis
- [ ] Statistical calculations on text
- [ ] Complex string manipulation
- [ ] Array-based frequency counting

---

### Function Design Principles Demonstrated

**Single Responsibility:**
- [ ] Each function does exactly one thing
- [ ] Clear, focused purpose
- [ ] Easy to test and modify

**Clear Interfaces:**
- [ ] Descriptive parameter names
- [ ] Consistent return value patterns
- [ ] Well-documented behavior

**Error Handling:**
- [ ] Input validation in functions
- [ ] Graceful error reporting
- [ ] Safe default behaviors

---

 **Congratulations! You've mastered function-based programming!** 

*Functions are the cornerstone of good software design. Next: Stage 3 - Problem to Pseudocode! *

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

- C++ is a superset of C with additional features
- `printf` is the C standard for formatted output
- `\n` adds a newline character in format strings
- Format specifiers control how data is displayed (%d, %f, %s, etc.)
