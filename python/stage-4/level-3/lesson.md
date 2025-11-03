# Level 3: Mathematical Application - Advanced Calculator
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
    ```bash
    cd python/stage-4-full-problem-solving/level-3-mathematical-application
    ```

2. **Run the program**:
    ```bash
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

```python
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

```python
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

```python
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

```python
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

```python
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

```python
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