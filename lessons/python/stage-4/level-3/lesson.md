# Level 3: Mathematical Application - Advanced Calculator

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 4: Full Problem Solving

### Today's Mission

Mathematics is at the heart of programming! This advanced calculator demonstrates how to implement complex mathematical operations, handle user input validation, manage application state (memory and history), and create a professional user interface.

---

### Learning Goals

- Implement various mathematical functions using Python's math module
- Create robust input validation and error handling
- Manage application state with global variables
- Build a multi-feature menu-driven application
- Understand the importance of calculation history and memory functions

---

### Your Task

**Study the calculator implementation and understand how it handles different types of mathematical operations. Then enhance it with additional features or create your own mathematical tools.**

The calculator should provide:
1. Basic arithmetic operations
2. Advanced mathematical functions
3. Trigonometric calculations
4. Memory storage and recall
5. Calculation history
6. Input validation and error handling

---

### How to Run

1. **Navigate to this level's directory**:
    ```
    cd python/stage-4-full-problem-solving/level-3-mathematical-application
    ```

2. **Run the program**:
    ```
    python3 main.py
    ```

3. **Test all calculator functions** and explore the features

---

### Success Checklist

- [ ] Basic arithmetic operations work correctly
- [ ] Advanced functions (power, square root, factorial) work
- [ ] Trigonometric functions handle degree/radian conversion
- [ ] Memory functions store and recall values
- [ ] History feature tracks calculations
- [ ] Error handling prevents crashes on invalid input

---

### Mathematical Programming Concepts

This calculator demonstrates several important mathematical programming concepts:

- **Library Usage**: Importing and using the `math` module
- **Function Composition**: Building complex operations from simpler ones
- **State Management**: Maintaining memory and history across operations
- **Input Sanitization**: Converting and validating user input
- **Error Prevention**: Checking for mathematical constraints (division by zero, domain restrictions)

---

### Enhancement Ideas

Try these advanced mathematical features:

1. **Unit Conversions** - Length, weight, temperature conversions
2. **Equation Solver** - Solve linear equations or systems
3. **Graphing Calculator** - Simple function plotting with text characters
4. **Statistics Calculator** - Mean, median, standard deviation
5. **Matrix Operations** - Basic matrix arithmetic
6. **Complex Numbers** - Operations with complex numbers

---

## Code Analysis

### Mathematical Operations Implementation

```
import math

# Basic operations
result = num1 + num2  # Addition
result = num1 ** exponent  # Power

# Advanced operations
result = math.sqrt(num)  # Square root
result = math.factorial(int(num))  # Factorial
result = math.log(num)  # Natural logarithm
result = math.exp(num)  # Exponential
```

- **Built-in Operators**: Python provides `+`, `-`, `*`, `/`, `**` directly
- **Math Module**: `import math` gives access to advanced functions
- **Type Conversion**: `int()` for factorial, careful handling needed

### Trigonometric Functions

```
# Convert degrees to radians for math functions
angle_rad = math.radians(angle)
result = math.sin(angle_rad)

# Convert back to degrees for inverse functions
result = math.degrees(math.asin(value))
```

- **Radian Conversion**: Math functions expect radians, not degrees
- **Inverse Functions**: asin, acos, atan return radians, convert back to degrees
- **Domain Restrictions**: Check valid input ranges for inverse functions

### State Management

```
# Global variables for persistent state
memory = 0.0
history = []

def add_to_history(operation, result):
    """Add calculation to history."""
    history.append(f"{operation} = {result}")
```

- **Global State**: Variables accessible across function calls
- **Data Persistence**: History maintained throughout program execution
- **Memory Functions**: Store and recall values between calculations

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (Study the implementation!)

### Mathematical Function Categories

| Category | Functions | Use Cases |
|----------|-----------|-----------|
| **Basic Arithmetic** | `+`, `-`, `*`, `/` | Everyday calculations |
| **Advanced Operations** | `**`, `sqrt()`, `factorial()` | Scientific calculations |
| **Trigonometric** | `sin()`, `cos()`, `tan()` | Angles and triangles |
| **Logarithmic** | `log()`, `exp()` | Growth, decay, scales |
| **Inverse Trig** | `asin()`, `acos()`, `atan()` | Angle from ratio |

### Error Handling Strategy

| Error Type | Detection | Response |
|------------|-----------|----------|
| **Invalid Operation** | Not in allowed list | Clear error message |
| **Division by Zero** | `num2 == 0` | Prevent operation |
| **Domain Error** | `sqrt(num < 0)` | Check before calculation |
| **Type Error** | Non-numeric input | Validate with try/except |
| **Range Error** | Invalid trig input | Check bounds |

### Input Validation Patterns

```
def validate_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print(" Invalid input. Please enter a valid number.")
```

- **Loop Until Valid**: Keeps prompting until good input received
- **Type Conversion**: `float()` handles both integers and decimals
- **User-Friendly**: Clear error messages guide user correction

### Memory and History Implementation

```
# Memory operations
memory = 0.0

def memory_functions():
    if choice == '1':  # Store
        memory = value
    elif choice == '2':  # Recall
        print(f"Memory: {memory}")
```

- **Persistent Storage**: Memory retains value between operations
- **Multiple Operations**: Store, recall, add, subtract, clear
- **History Tracking**: List maintains chronological record

### Menu System Design

```
while True:
    print_menu()
    choice = get_choice()

    if choice == '1':
        basic_calculator()
    elif choice == '7':
        break
```

- **Main Loop**: Continues until user chooses to exit
- **Modular Functions**: Each menu option calls separate function
- **Input Validation**: Ensures valid menu choices
- **Clean Interface**: Clear prompts and organized display

---

 **Outstanding! You now have a professional calculator application!** 

*Next up: Interactive Application - building user-focused programs!*


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
Advanced Calculator
A comprehensive calculator with basic and advanced mathematical operations.
"""

import math

# Global variables for memory and history
memory = 0.0
history = []

def validate_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def add_to_history(operation, result):
    """Add calculation to history."""
    history.append(f"{operation} = {result}")

def basic_calculator():
    """Handle basic arithmetic operations."""
    print("\nBasic Calculator (+, -, *, /)")

    num1 = validate_number("Enter first number: ")

    operation = input("Enter operation (+, -, *, /): ").strip()

    if operation not in ['+', '-', '*', '/']:
        print("❌ Invalid operation. Please use +, -, *, or /.")
        return

    num2 = validate_number("Enter second number: ")

    if operation == '/' and num2 == 0:
        print("❌ Division by zero is not allowed!")
        return

    # Perform calculation
    result = 0.0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2

    operation_str = f"{num1} {operation} {num2}"
    print(f"Result: {operation_str} = {result}")

    add_to_history(operation_str, result)

    # Memory option
    store_memory = input("Add to memory? (y/n): ").lower().strip()
    if store_memory == 'y':
        global memory
        memory = result
        print("✅ Result stored in memory!")

def advanced_operations():
    """Handle advanced mathematical operations."""
    print("\nAdvanced Operations")
    print("1. Power (x^y)")
    print("2. Square Root (√x)")
    print("3. Factorial (x!)")
    print("4. Natural Logarithm (ln x)")
    print("5. Exponential (e^x)")

    choice = input("Enter choice (1-5): ").strip()

    if choice == '1':
        # Power
        base = validate_number("Enter base: ")
        exponent = validate_number("Enter exponent: ")
        result = base ** exponent
        operation_str = f"{base}^{exponent}"
        print(f"Result: {operation_str} = {result}")
        add_to_history(operation_str, result)

    elif choice == '2':
        # Square root
        num = validate_number("Enter number: ")
        if num < 0:
            print("❌ Cannot calculate square root of negative number!")
            return
        result = math.sqrt(num)
        operation_str = f"√{num}"
        print(f"Result: {operation_str} = {result}")
        add_to_history(operation_str, result)

    elif choice == '3':
        # Factorial
        num = validate_number("Enter integer: ")
        if num < 0 or not num.is_integer():
            print("❌ Factorial requires non-negative integer!")
            return
        result = math.factorial(int(num))
        operation_str = f"{int(num)}!"
        print(f"Result: {operation_str} = {result}")
        add_to_history(operation_str, result)

    elif choice == '4':
        # Natural logarithm
        num = validate_number("Enter positive number: ")
        if num <= 0:
            print("❌ Natural logarithm requires positive number!")
            return
        result = math.log(num)
        operation_str = f"ln({num})"
        print(f"Result: {operation_str} = {result:.6f}")
        add_to_history(operation_str, result)

    elif choice == '5':
        # Exponential
        num = validate_number("Enter exponent: ")
        result = math.exp(num)
        operation_str = f"e^{num}"
        print(f"Result: {operation_str} = {result:.6f}")
        add_to_history(operation_str, result)

    else:
        print("❌ Invalid choice!")
        return

def trigonometric_functions():
    """Handle trigonometric functions."""
    print("\nTrigonometric Functions")
    print("1. Sine (sin x)")
    print("2. Cosine (cos x)")
    print("3. Tangent (tan x)")
    print("4. Arcsine (asin x)")
    print("5. Arccosine (acos x)")
    print("6. Arctangent (atan x)")

    choice = input("Enter choice (1-6): ").strip()
    angle = validate_number("Enter angle in degrees: ")

    # Convert to radians for calculation
    angle_rad = math.radians(angle)
    result = 0.0
    operation_str = ""

    if choice == '1':
        result = math.sin(angle_rad)
        operation_str = f"sin({angle}°)"
    elif choice == '2':
        result = math.cos(angle_rad)
        operation_str = f"cos({angle}°)"
    elif choice == '3':
        result = math.tan(angle_rad)
        operation_str = f"tan({angle}°)"
    elif choice == '4':
        if not -1 <= angle <= 1:
            print("❌ Arcsine requires value between -1 and 1!")
            return
        result = math.degrees(math.asin(angle))
        operation_str = f"asin({angle})"
    elif choice == '5':
        if not -1 <= angle <= 1:
            print("❌ Arccosine requires value between -1 and 1!")
            return
        result = math.degrees(math.acos(angle))
        operation_str = f"acos({angle})"
    elif choice == '6':
        result = math.degrees(math.atan(angle))
        operation_str = f"atan({angle})"
    else:
        print("❌ Invalid choice!")
        return

    print(f"Result: {operation_str} = {result:.6f}")
    add_to_history(operation_str, result)

def memory_functions():
    """Handle memory operations."""
    print("\nMemory Functions")
    print("1. Store Value")
    print("2. Recall Value")
    print("3. Clear Memory")
    print("4. Add to Memory")
    print("5. Subtract from Memory")

    choice = input("Enter choice (1-5): ").strip()

    if choice == '1':
        value = validate_number("Enter value to store: ")
        global memory
        memory = value
        print(f"✅ Stored {value} in memory")
    elif choice == '2':
        print(f"Memory value: {memory}")
    elif choice == '3':
        memory = 0.0
        print("✅ Memory cleared")
    elif choice == '4':
        value = validate_number("Enter value to add: ")
        memory += value
        print(f"✅ Added {value}. New memory value: {memory}")
    elif choice == '5':
        value = validate_number("Enter value to subtract: ")
        memory -= value
        print(f"✅ Subtracted {value}. New memory value: {memory}")
    else:
        print("❌ Invalid choice!")

def view_history():
    """Display calculation history."""
    print("\nCalculation History")
    print("=" * 20)

    if not history:
        print("No calculations in history.")
        return

    for i, calc in enumerate(history, 1):
        print(f"{i}. {calc}")

def clear_history():
    """Clear calculation history."""
    global history
    history.clear()
    print("✅ Calculation history cleared!")

def main():
    """Main program function."""
    print("🧮 Advanced Calculator 🧮")
    print("=" * 25)

    while True:
        print("\nOperations Menu:")
        print("1. Basic Calculator (+, -, *, /)")
        print("2. Advanced Operations (^, √, !)")
        print("3. Trigonometric Functions")
        print("4. Memory Functions")
        print("5. View History")
        print("6. Clear History")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()

        if choice == '1':
            basic_calculator()
        elif choice == '2':
            advanced_operations()
        elif choice == '3':
            trigonometric_functions()
        elif choice == '4':
            memory_functions()
        elif choice == '5':
            view_history()
        elif choice == '6':
            clear_history()
        elif choice == '7':
            print("\nThank you for using the Advanced Calculator! 🧮")
            break
        else:
            print("❌ Invalid choice. Please enter 1-7.")

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
