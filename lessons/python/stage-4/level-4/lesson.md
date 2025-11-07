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


<div style="page-break-after: always;"></div>

## Answer Key

### Complete Solution

```py
#!/usr/bin/env python3
"""
Interactive Task Manager Application
A simple command-line task management system with menu-driven interface.
"""

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        """Add a new task to the list."""
        task = {
            'id': self.next_id,
            'description': description,
            'completed': False
        }
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task '{description}' added successfully!")

    def view_tasks(self):
        """Display all tasks with their status."""
        if not self.tasks:
            print("No tasks found.")
            return

        print("\nCurrent Tasks:")
        print("-" * 40)
        for task in self.tasks:
            status = "[✓]" if task['completed'] else "[ ]"
            print(f"{task['id']}. {status} {task['description']}")
        print("-" * 40)

    def complete_task(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task['id'] == task_id:
                if task['completed']:
                    print(f"Task {task_id} is already completed.")
                else:
                    task['completed'] = True
                    print(f"Task '{task['description']}' marked as completed!")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        """Delete a task from the list."""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                removed_task = self.tasks.pop(i)
                print(f"Task '{removed_task['description']}' deleted successfully!")
                return
        print(f"Task with ID {task_id} not found.")

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("         INTERACTIVE TASK MANAGER")
    print("="*50)
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Exit")
    print("="*50)

def get_user_choice():
    """Get and validate user's menu choice."""
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main application loop."""
    manager = TaskManager()

    print("Welcome to the Interactive Task Manager!")
    print("Manage your tasks efficiently with this simple application.")

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            description = input("Enter task description: ").strip()
            if description:
                manager.add_task(description)
            else:
                print("Task description cannot be empty.")

        elif choice == 2:
            manager.view_tasks()

        elif choice == 3:
            if not manager.tasks:
                print("No tasks available to complete.")
                continue
            manager.view_tasks()
            try:
                task_id = int(input("Enter task ID to complete: "))
                manager.complete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID.")

        elif choice == 4:
            if not manager.tasks:
                print("No tasks available to delete.")
                continue
            manager.view_tasks()
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID.")

        elif choice == 5:
            print("Thank you for using the Task Manager. Goodbye!")
            break

        # Pause before showing menu again
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
```

### Code Breakdown

This solution demonstrates the key concepts from this lesson:

1. **Structure**: The program follows standard python conventions with proper imports and main function
2. **Variables**: Data types are correctly declared and initialized
3. **Logic**: The program implements the required functionality
4. **Output**: Results are displayed clearly to the user
5. **Best Practices**: Code is readable and follows naming conventions

### Testing Your Solution

Try these test cases to verify your code works correctly:

1. **Basic Test**: Run the program with standard inputs
2. **Edge Cases**: Test with boundary values (0, -1, very large numbers)
3. **Error Handling**: Verify the program handles invalid inputs gracefully

### Tips for Understanding

- Review each section carefully
- Try modifying values to see how output changes
- Add your own printf/print statements to trace execution
- Experiment with different inputs
