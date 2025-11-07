# Temperature Converter

A simple Python program that converts temperatures between Celsius and Fahrenheit.

## How to Run

1. **Run the program**:
    ```bash
    python3 main.py
    ```

2. **Follow the on-screen prompts** to convert temperatures.

## Features

- Convert Celsius to Fahrenheit
- Convert Fahrenheit to Celsius
- Input validation for menu choices and temperatures
- Clear, formatted output with units
- Error handling for invalid inputs

## Example Usage

```
Temperature Converter
=====================
What conversion do you want?
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
Enter choice (1 or 2): 1
Enter temperature in Celsius: 25
25.0°C is equal to 77.0°F
```

## Test Cases

Try these conversions to verify the program works:
- 0°C = 32°F (freezing point of water)
- 100°C = 212°F (boiling point of water)
- 25°C = 77°F (room temperature)
- -40°C = -40°F (equal at this temperature)

## Learning Outcomes

This application demonstrates:
- **User Input Handling**: Getting and validating user input
- **Conditional Logic**: Using if/elif/else for decision making
- **Mathematical Operations**: Performing temperature conversion calculations
- **Error Handling**: Managing invalid inputs gracefully
- **String Formatting**: Creating readable output with f-strings
- **Program Structure**: Organizing code into functions

## Code Structure

- `main()`: Program entry point and menu handling
- `celsius_to_fahrenheit()`: Converts Celsius to Fahrenheit
- `fahrenheit_to_celsius()`: Converts Fahrenheit to Celsius
- `get_temperature_input()`: Gets and validates temperature input
- `get_menu_choice()`: Gets and validates menu choice

---

*Built as Level 1 of Stage 4: Full Problem Solving in the Python Programming Curriculum*