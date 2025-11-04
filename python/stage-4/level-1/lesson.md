# Level 1: Simple Application - Temperature Converter

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 4: Full Problem Solving

### Today's Mission

Welcome to Stage 4! Now that you understand Python fundamentals, it's time to build complete applications. We'll start with a simple but complete temperature converter that demonstrates the full development cycle: planning, coding, testing, and documentation.

---

### Learning Goals

- Apply all Python concepts learned so far in a complete program
- Practice the full software development process
- Learn about user input validation and error handling
- Understand program structure and organization
- Create documentation for your code

---

### Your Task

**Study the provided `main.py` file and understand how it works. Then create your own version or modify the existing one.**

The temperature converter should:
1. Display a menu with conversion options
2. Get user input for temperature and conversion type
3. Perform the appropriate conversion
4. Display the result clearly
5. Handle invalid inputs gracefully

---

### How to Run

1. **Navigate to this level's directory**:
    ```bash
    cd python/stage-4-full-problem-solving/level-1-simple-application
    ```

2. **Run the program**:
    ```bash
    python3 main.py
    ```

3. **Test different conversions** and edge cases

---

### Success Checklist

- [ ] Program runs without errors
- [ ] Menu displays correctly
- [ ] Both conversion directions work
- [ ] Input validation prevents crashes
- [ ] Output is clear and formatted
- [ ] Program handles edge cases (negative temperatures, etc.)

---

### What Makes This a Complete Application?

This temperature converter demonstrates several key aspects of real software:

- **User Interface**: Clear menu and prompts
- **Input Validation**: Prevents invalid data from crashing the program
- **Error Handling**: Graceful recovery from mistakes
- **Modular Design**: Functions for different responsibilities
- **Documentation**: Comments explaining what each part does
- **Testing**: Multiple test cases to verify correctness

---

### Enhancement Ideas

Try these improvements to make the program even better:

1. **Add Kelvin conversion** - Support absolute temperature scale
2. **Temperature ranges** - Add warnings for extreme temperatures
3. **Conversion history** - Keep track of previous conversions
4. **Batch conversion** - Convert multiple temperatures at once
5. **Unit preferences** - Remember user's preferred units

---

## Code Review

### Key Functions

```python
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
```

- **Clear naming**: Function name describes exactly what it does
- **Documentation**: Docstring explains the purpose
- **Simple logic**: One clear mathematical formula
- **Return value**: Result is returned for use by caller

```python
def get_temperature_input(prompt):
    """Get temperature input from user with validation."""
    while True:
        try:
            temp = float(input(prompt))
            return temp
        except ValueError:
            print(" Invalid input. Please enter a valid number.")
```

- **Input validation**: Uses try/except to handle invalid input
- **User-friendly**: Clear error messages
- **Robust**: Won't crash on bad input
- **Loop until valid**: Keeps asking until good input received

### Program Structure

```
main.py
├── Import statements (if needed)
├── Helper functions
│   ├── celsius_to_fahrenheit()
│   ├── fahrenheit_to_celsius()
│   ├── get_temperature_input()
│   └── get_menu_choice()
└── main() function
    └── Program logic and menu
```

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (Study the provided code!)

### Temperature Conversion Formulas

**Celsius to Fahrenheit:**
```
°F = (°C × 9/5) + 32
```

**Fahrenheit to Celsius:**
```
°C = (°F - 32) × 5/9
```

### Key Programming Concepts Demonstrated

| Concept | Example | Why Important |
|---------|---------|---------------|
| **Functions** | `celsius_to_fahrenheit()` | Reusable code, clear organization |
| **Error Handling** | `try/except` blocks | Robust programs don't crash |
| **Input Validation** | Checking menu choices | Data integrity and security |
| **Loop Control** | `while True` loops | Keep trying until success |
| **String Formatting** | f-strings | Readable output formatting |
| **Documentation** | Docstrings and comments | Code maintainability |

### Common Issues & Solutions

| Issue | Symptom | Solution |
|-------|---------|----------|
| **ValueError** | Program crashes on invalid input | Use try/except blocks |
| **TypeError** | Wrong data types in operations | Validate input types |
| **Logic Error** | Wrong conversion results | Double-check formulas |
| **Infinite Loop** | Program never exits input loop | Ensure loop exit conditions |

### Testing Strategy

**Test Cases to Try:**
- Normal temperatures: 25°C, 77°F
- Extreme temperatures: -40°C, 1000°F
- Edge cases: 0°C, 32°F, -273.15°C
- Invalid inputs: "abc", "", "25.5.5"

**Expected Behavior:**
- Valid inputs → Correct conversions
- Invalid inputs → Clear error messages, retry prompts
- Edge cases → Reasonable results or appropriate warnings

### Code Quality Checklist

- [ ] **Readability**: Clear variable names and comments
- [ ] **Modularity**: Functions have single responsibilities
- [ ] **Error Handling**: Graceful failure recovery
- [ ] **Documentation**: Purpose of each function clear
- [ ] **Testing**: Multiple test cases covered
- [ ] **User Experience**: Clear prompts and feedback

---

 **Congratulations! You've built your first complete Python application!** 

*This temperature converter demonstrates the full software development process. Next up: Data Processing Application!*