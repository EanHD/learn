# Level 1: Simple Application

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 4: Full Problem Solving

### Today's Mission

**FULL APPLICATION DEVELOPMENT!**  Welcome to Stage 4! You're now building complete, working applications from start to finish. No more partial implementations - you'll create fully functional programs that users can actually run and use.

**The Process:**
1. **Define Requirements**: What should the application do?
2. **Design Architecture**: Plan the program structure
3. **Implement Features**: Write complete, working code
4. **Add Error Handling**: Make it robust and user-friendly
5. **Test Thoroughly**: Verify all functionality works
6. **Document**: Explain how to use and modify the code

---

### Learning Goals

- [ ] Build complete, working applications
- [ ] Implement full program lifecycles
- [ ] Handle file I/O operations
- [ ] Create user-friendly interfaces
- [ ] Manage application state
- [ ] Write production-ready code

---

### Your Task

**Build a complete Grade Management Application with:**
1. **Student Management**: Add, view, and remove students
2. **Grade Management**: Record grades for different assignments
3. **Calculations**: GPA, averages, and statistics
4. **File Storage**: Save and load data from files
5. **Menu System**: Easy-to-use interface
6. **Error Handling**: Robust input validation

---

## Application Requirements

### Core Features
- [ ] **Student Registration**: Add students with ID and name
- [ ] **Grade Recording**: Add grades for assignments/quizzes/exams
- [ ] **Grade Calculations**: Calculate averages and GPA
- [ ] **Data Persistence**: Save/load data from files
- [ ] **Reports**: Display student information and statistics

### Technical Requirements
- [ ] Use structs for data organization
- [ ] Implement file I/O for data persistence
- [ ] Create modular functions
- [ ] Include proper error handling
- [ ] Provide clear user interface

---

## Application Architecture

### Data Structures
```c
# define MAX_STUDENTS 100
# define MAX_GRADES 50
# define MAX_NAME_LENGTH 50

typedef struct {
    int id;
    char name[MAX_NAME_LENGTH];
    float grades[MAX_GRADES];
    int grade_count;
    float gpa;
} Student;

typedef struct {
    Student students[MAX_STUDENTS];
    int student_count;
    char filename[100];
} GradeBook;
```

### Function Modules
- [ ] **File Operations**: `save_data()`, `load_data()`
- [ ] **Student Management**: `add_student()`, `find_student()`, `remove_student()`
- [ ] **Grade Management**: `add_grade()`, `calculate_average()`
- [ ] **User Interface**: `display_menu()`, `get_user_choice()`
- [ ] **Reports**: `display_student()`, `display_all_students()`

---

## Complete Implementation

### Header File (gradebook.h)
```c
# ifndef GRADEBOOK_H
# define GRADEBOOK_H

# include <stdio.h>
# include <stdlib.h>
# include <string.h>

# define MAX_STUDENTS 100
# define MAX_GRADES 50
# define MAX_NAME_LENGTH 50

typedef struct {
    int id;
    char name[MAX_NAME_LENGTH];
    float grades[MAX_GRADES];
    int grade_count;
    float gpa;
} Student;

typedef struct {
    Student students[MAX_STUDENTS];
    int student_count;
    char filename[100];
} GradeBook;

// Function prototypes
void initialize_gradebook(GradeBook *book, const char *filename);
int add_student(GradeBook *book, int id, const char *name);
int find_student(const GradeBook *book, int id);
int add_grade(GradeBook *book, int student_id, float grade);
void calculate_gpa(Student *student);
void display_student(const Student *student);
void display_all_students(const GradeBook *book);
int save_data(const GradeBook *book);
int load_data(GradeBook *book);
void display_menu(void);
int get_user_choice(void);

# endif
```

### Implementation File (gradebook.c)
```c
# include "gradebook.h"

// Initialize gradebook with filename
void initialize_gradebook(GradeBook *book, const char *filename) {
    book->student_count = 0;
    strcpy(book->filename, filename);
    load_data(book); // Try to load existing data
}

// Add a new student
int add_student(GradeBook *book, int id, const char *name) {
    if (book->student_count >= MAX_STUDENTS) {
        std::cout << "Error: Maximum number of students reached.\n");
        return 0;
    }

    // Check if student ID already exists
    if (find_student(book, id) != -1) {
        std::cout << "Error: Student ID %d already exists.\n", id);
        return 0;
    }

    Student *student = &book->students[book->student_count];
    student->id = id;
    strcpy(student->name, name);
    student->grade_count = 0;
    student->gpa = 0.0;

    book->student_count++;
    std::cout << "Student %s (ID: %d) added successfully.\n", name, id);
    return 1;
}

// Find student by ID, return index or -1 if not found
int find_student(const GradeBook *book, int id) {
    for (int i = 0; i < book->student_count; i++) {
        if (book->students[i].id == id) {
            return i;
        }
    }
    return -1;
}

// Add grade to student
int add_grade(GradeBook *book, int student_id, float grade) {
    int index = find_student(book, student_id);
    if (index == -1) {
        std::cout << "Error: Student ID %d not found.\n", student_id);
        return 0;
    }

    Student *student = &book->students[index];
    if (student->grade_count >= MAX_GRADES) {
        std::cout << "Error: Maximum grades reached for student.\n");
        return 0;
    }

    if (grade < 0.0 || grade > 100.0) {
        std::cout << "Error: Grade must be between 0.0 and 100.0.\n");
        return 0;
    }

    student->grades[student->grade_count] = grade;
    student->grade_count++;
    calculate_gpa(student);

    std::cout << "Grade %.2f added to %s.\n", grade, student->name);
    return 1;
}

// Calculate GPA for student
void calculate_gpa(Student *student) {
    if (student->grade_count == 0) {
        student->gpa = 0.0;
        return;
    }

    float sum = 0.0;
    for (int i = 0; i < student->grade_count; i++) {
        sum += student->grades[i];
    }
    student->gpa = sum / student->grade_count;
}

// Display single student information
void display_student(const Student *student) {
    std::cout << "\n=== Student Information ===\n");
    std::cout << "ID: %d\n", student->id);
    std::cout << "Name: %s\n", student->name);
    std::cout << "Number of grades: %d\n", student->grade_count);
    std::cout << "GPA: %.2f\n", student->gpa);

    if (student->grade_count > 0) {
        std::cout << "Grades: ");
        for (int i = 0; i < student->grade_count; i++) {
            std::cout << "%.2f", student->grades[i]);
            if (i < student->grade_count - 1) std::cout << ", ");
        }
        std::cout << "\n");
    }
}

// Display all students
void display_all_students(const GradeBook *book) {
    if (book->student_count == 0) {
        std::cout << "No students in the gradebook.\n");
        return;
    }

    std::cout << "\n=== All Students ===\n");
    for (int i = 0; i < book->student_count; i++) {
        const Student *student = &book->students[i];
        std::cout << "%d. %s (ID: %d) - GPA: %.2f\n",
               i + 1, student->name, student->id, student->gpa);
    }
}

// Save data to file
int save_data(const GradeBook *book) {
    FILE *file = fopen(book->filename, "w");
    if (file == NULL) {
        std::cout << "Error: Could not open file for writing.\n");
        return 0;
    }

    fprintf(file, "%d\n", book->student_count);
    for (int i = 0; i < book->student_count; i++) {
        const Student *student = &book->students[i];
        fprintf(file, "%d\n%s\n%d\n",
                student->id, student->name, student->grade_count);

        for (int j = 0; j < student->grade_count; j++) {
            fprintf(file, "%.2f\n", student->grades[j]);
        }
    }

    fclose(file);
    std::cout << "Data saved to %s\n", book->filename);
    return 1;
}

// Load data from file
int load_data(GradeBook *book) {
    FILE *file = fopen(book->filename, "r");
    if (file == NULL) {
        std::cout << "No existing data file found. Starting fresh.\n");
        return 0;
    }

    fscanf(file, "%d", &book->student_count);
    for (int i = 0; i < book->student_count; i++) {
        Student *student = &book->students[i];
        fscanf(file, "%d", &student->id);

        // Read name (handle spaces)
        fgetc(file); // consume newline
        fgets(student->name, MAX_NAME_LENGTH, file);
        // Remove trailing newline
        student->name[strcspn(student->name, "\n")] = 0;

        fscanf(file, "%d", &student->grade_count);

        for (int j = 0; j < student->grade_count; j++) {
            fscanf(file, "%f", &student->grades[j]);
        }

        calculate_gpa(student);
    }

    fclose(file);
    std::cout << "Data loaded from %s\n", book->filename);
    return 1;
}

// Display menu
void display_menu(void) {
    std::cout << "\n=== Grade Management System ===\n");
    std::cout << "1. Add Student\n");
    std::cout << "2. Add Grade\n");
    std::cout << "3. View Student\n");
    std::cout << "4. View All Students\n");
    std::cout << "5. Save Data\n");
    std::cout << "6. Exit\n");
    std::cout << "Enter your choice (1-6): ");
}

// Get user choice
int get_user_choice(void) {
    int choice;
    scanf("%d", &choice);
    return choice;
}
```

### Main Program (main.c)
```c
# include "gradebook.h"

int main() {
    GradeBook book;
    initialize_gradebook(&book, "grades.txt");

    int running = 1;
    while (running) {
        display_menu();
        int choice = get_user_choice();

        switch (choice) {
            case 1: { // Add Student
                int id;
                char name[MAX_NAME_LENGTH];

                std::cout << "Enter student ID: ");
                scanf("%d", &id);
                std::cout << "Enter student name: ");
                scanf(" %[^\n]", name); // Read entire line including spaces

                add_student(&book, id, name);
                break;
            }

            case 2: { // Add Grade
                int student_id;
                float grade;

                std::cout << "Enter student ID: ");
                scanf("%d", &student_id);
                std::cout << "Enter grade (0-100): ");
                scanf("%f", &grade);

                add_grade(&book, student_id, grade);
                break;
            }

            case 3: { // View Student
                int student_id;
                std::cout << "Enter student ID: ");
                scanf("%d", &student_id);

                int index = find_student(&book, student_id);
                if (index != -1) {
                    display_student(&book.students[index]);
                } else {
                    std::cout << "Student not found.\n");
                }
                break;
            }

            case 4: { // View All Students
                display_all_students(&book);
                break;
            }

            case 5: { // Save Data
                save_data(&book);
                break;
            }

            case 6: { // Exit
                save_data(&book); // Auto-save on exit
                std::cout << "Goodbye!\n");
                running = 0;
                break;
            }

            default:
                std::cout << "Invalid choice. Please try again.\n");
        }
    }

    return 0;
}
```

---

## Testing the Application

### Compilation Instructions
```
# Compile the program
g++ -o gradebook main.c gradebook.c

# Run the program
./gradebook
```

### Test Scenarios
1. **Add Students**: Try adding 2-3 students with different IDs
2. **Add Grades**: Add multiple grades to each student
3. **View Data**: Check individual and all student displays
4. **Save/Load**: Exit and restart to verify data persistence
5. **Error Handling**: Test invalid IDs, out-of-range grades

### Sample Usage
```
=== Grade Management System ===
1. Add Student
2. Add Grade
3. View Student
4. View All Students
5. Save Data
6. Exit
Enter your choice (1-6): 1
Enter student ID: 1001
Enter student name: Alice Johnson
Student Alice Johnson (ID: 1001) added successfully.

Enter your choice (1-6): 2
Enter student ID: 1001
Enter grade (0-100): 95.5
Grade 95.50 added to Alice Johnson.

Enter your choice (1-6): 3
Enter student ID: 1001

=== Student Information ===
ID: 1001
Name: Alice Johnson
Number of grades: 1
GPA: 95.50
Grades: 95.50
```

---

## Code Explanation

### Key Features Implemented

**Data Management:**
- [ ] Struct-based data organization
- [ ] Dynamic GPA calculation
- [ ] Array-based storage with size limits

**File I/O:**
- [ ] Text file storage for persistence
- [ ] Load on startup, save on demand
- [ ] Structured data format

**Error Handling:**
- [ ] Input validation for grades and IDs
- [ ] Duplicate ID prevention
- [ ] File operation error checking

**User Interface:**
- [ ] Clear menu system
- [ ] Informative prompts
- [ ] Formatted output display

---

## Enhancements to Try

### Beginner Enhancements
1. **Remove Student**: Add functionality to remove students
2. **Grade Statistics**: Show class average, highest/lowest grades
3. **Search by Name**: Find students by partial name match

### Intermediate Enhancements
1. **Grade Categories**: Separate homework, quizzes, exams
2. **Weighted GPA**: Different assignment types have different weights
3. **Grade Letter Conversion**: Convert numeric grades to A/B/C/D/F

### Advanced Enhancements
1. **Multiple Classes**: Support multiple gradebooks
2. **Grade History**: Track when grades were added
3. **Export Reports**: Generate formatted reports to files

---

## Success Checklist

**Application Features:**
- [x] **Student Management**: Add/view students with proper validation
- [x] **Grade Recording**: Add grades with range checking
- [x] **Calculations**: GPA calculation and display
- [x] **File I/O**: Save and load data persistence
- [x] **Menu System**: Complete user interface
- [x] **Error Handling**: Robust input validation and error messages

**Code Quality:**
- [x] **Modular Design**: Separate functions for different operations
- [x] **Data Structures**: Proper use of structs and arrays
- [x] **Documentation**: Clear comments and function documentation
- [x] **Testing**: Comprehensive test scenarios covered

---

## Learning Outcomes

**Technical Skills:**
- [ ] Complete application development lifecycle
- [ ] File I/O operations in C
- [ ] Struct-based data management
- [ ] Modular program design
- [ ] User input validation and error handling

**Problem-Solving Skills:**
- [ ] Application architecture design
- [ ] Feature prioritization and implementation
- [ ] Data persistence strategies
- [ ] User experience considerations

---

## Code Walkthrough

### Program Flow
1. **Initialization**: Load existing data or start fresh
2. **Main Loop**: Display menu and process user choices
3. **Operations**: Perform requested actions with validation
4. **Persistence**: Auto-save on exit, manual save available
5. **Cleanup**: Proper resource management

### Data Flow
```
User Input → Validation → Processing → Storage → Display
              ↓           ↓         ↓        ↓
         Error Messages  Business  File I/O  UI Updates
         and Recovery   Logic     Operations  Feedback
```

---

<div style="page-break-after: always;"></div>

---

## Implementation Notes

### Design Decisions
- [ ] **Fixed Arrays**: Used for simplicity, could be dynamic in advanced version
- [ ] **Text File Storage**: Human-readable format for debugging
- [ ] **Simple GPA**: Basic average, could be weighted in enhancements
- [ ] **ID-based Lookup**: Fast searching with integer keys

### Potential Improvements
- [ ] **Memory Management**: Use dynamic allocation for unlimited students
- [ ] **Database Integration**: Replace file I/O with SQLite
- [ ] **GUI Interface**: Add graphical user interface
- [ ] **Network Features**: Multi-user support with server

### Best Practices Demonstrated
- [ ] **Separation of Concerns**: UI, business logic, and data access separated
- [ ] **Error Handling**: Comprehensive validation and user feedback
- [ ] **Code Organization**: Modular functions with clear responsibilities
- [ ] **Documentation**: Inline comments and function documentation

---

 **Congratulations! You've built your first complete application!** 

*This is a major milestone - you can now create fully functional programs from scratch! Next: Data processing applications with advanced file operations! *

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


### <div style="page-break-after: always;"></div>

Answer Key

Expected implementation provided.

<div style="page-break-after: always;"></div>

---

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
