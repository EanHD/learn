# Level 4: Interactive Application - Task Manager

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
```python
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

- **Object-Oriented Programming**: Using classes to encapsulate data and behavior
- **Data Structures**: Lists and dictionaries for storing task information
- **Control Flow**: While loops for continuous operation, if-elif for menu handling
- **User Input**: Getting and validating user input from command line
- **Error Handling**: Try-except blocks for input validation
- **Modular Design**: Separating concerns into different functions

## Potential Enhancements

- Add task priorities or due dates
- Save tasks to a file for persistence
- Add search functionality
- Implement undo operations
- Add task categories or tags