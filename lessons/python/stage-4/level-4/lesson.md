# Level 4: Interactive Application - Task Manager

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Learning Objectives

By completing this level, you will:

- Understand how to create interactive, menu-driven applications
- Learn to implement basic CRUD (Create, Read, Update, Delete) operations
- Practice object-oriented programming with classes and methods
- Handle user input validation and error handling
- Design user-friendly command-line interfaces

## Code Analysis

### Application Structure

The Task Manager application consists of:

1. **TaskManager Class**: Manages the collection of tasks and provides methods for task operations
2. **Main Function**: Contains the application loop and menu handling
3. **Helper Functions**: Display menu and get user input

### Key Components

**Task Data Structure:**
```
task = {
    'id': self.next_id,
    'description': description,
    'completed': False
}
```
Each task is stored as a dictionary with an ID, description, and completion status.

**Menu System:**
The application uses a while loop to continuously display a menu and process user choices until the user chooses to exit.

**Input Validation:**
- Menu choices are validated to ensure they are integers between 1-5
- Task descriptions are checked to prevent empty entries
- Task IDs are validated before operations

### Problem-Solving Approach

1. **Requirements Analysis**: Identify needed features (add, view, complete, delete tasks)
2. **Data Design**: Choose appropriate data structures (list of dictionaries)
3. **Interface Design**: Create an intuitive menu system
4. **Implementation**: Build each feature incrementally
5. **Testing**: Verify each operation works correctly

## Success Checklist

- [ ] Application starts and displays welcome message
- [ ] Menu displays all 5 options clearly
- [ ] Can add tasks with descriptions
- [ ] Can view all tasks with completion status
- [ ] Can mark tasks as completed
- [ ] Can delete tasks from the list
- [ ] Input validation prevents invalid menu choices
- [ ] Application exits cleanly when requested
- [ ] Code is well-organized with classes and functions
- [ ] Error messages are helpful and informative

## Key Concepts Demonstrated

- [ ] **Object-Oriented Programming**: Using classes to encapsulate data and behavior
- [ ] **Data Structures**: Lists and dictionaries for storing task information
- [ ] **Control Flow**: While loops for continuous operation, if-elif for menu handling
- [ ] **User Input**: Getting and validating user input from command line
- [ ] **Error Handling**: Try-except blocks for input validation
- [ ] **Modular Design**: Separating concerns into different functions

## Potential Enhancements

- [ ] Add task priorities or due dates
- [ ] Save tasks to a file for persistence
- [ ] Add search functionality
- [ ] Implement undo operations
- [ ] Add task categories or tags

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No cheating until you've tried!)

### Code Breakdown

> **NEEDS_AUTHOR:** This lesson needs a complete answer key with code breakdown, execution process explanation, common errors table, and bonus knowledge section. Reference c-c++/stage-1/level-1/lesson.md for the gold standard format.

### Key Concepts

- Review the code structure specific to Python
- Understand the execution flow
- Learn common pitfalls and solutions

### Next Steps

Practice the code and experiment with variations!

---

**Congratulations! Keep coding!**


### Learning Goals

- Understand core concepts
- Practice implementation


### Your Task

1. Review the code structure
2. Implement the required functionality
3. Test your solution


### How to Run

1. Open the code file
2. Review and understand the implementation
3. Execute using: `<Space>r` in Vim


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic
