# Advanced Calculator

A comprehensive Python calculator with basic and advanced mathematical operations, memory functions, and calculation history.

## How to Run

1. **Run the program**:
    ```bash
    python3 main.py
    ```

2. **Use the menu system** to perform calculations.

## Features

- Basic arithmetic operations (+, -, *, /)
- Advanced operations (power, square root, factorial)
- Trigonometric functions (sin, cos, tan)
- Memory functions (store, recall, clear)
- Calculation history
- Input validation and error handling
- Constants (π, e)

## Example Usage

```
Advanced Calculator
===================

Operations Menu:
1. Basic Calculator (+, -, *, /)
2. Advanced Operations (^, √, !)
3. Trigonometric Functions
4. Memory Functions
5. View History
6. Clear History
7. Exit

Enter choice (1-7): 1

Basic Calculator:
Enter first number: 15
Enter operation (+, -, *, /): *
Enter second number: 7
Result: 15 * 7 = 105

Add to memory? (y/n): y
 Result stored in memory!
```

## Learning Outcomes

This application demonstrates:
- **Mathematical Operations**: Implementing various math functions
- **Input Validation**: Ensuring valid numbers and operations
- **State Management**: Memory and history functionality
- **Error Handling**: Managing mathematical errors (division by zero, etc.)
- **Data Persistence**: Saving calculation history
- **User Experience**: Intuitive menu-driven interface

## Code Structure

- `main()`: Program entry point and main menu
- `basic_calculator()`: Handles basic arithmetic
- `advanced_operations()`: Power, square root, factorial
- `trigonometric_functions()`: Sin, cos, tan operations
- `memory_functions()`: Store, recall, clear memory
- `view_history()`: Display calculation history
- `validate_number()`: Input validation for numbers

---

*Built as Level 3 of Stage 4: Full Problem Solving in the Python Programming Curriculum*