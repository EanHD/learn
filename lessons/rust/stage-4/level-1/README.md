# Temperature Converter

A simple Rust program that converts temperatures between Celsius and Fahrenheit.

## How to Run

1. Compile the program:
   ```bash
   rustc main.rs
   ```

2. Run the program:
   ```bash
   ./main
   ```

3. Follow the on-screen prompts to convert temperatures.

## Features

- Convert Celsius to Fahrenheit
- Convert Fahrenheit to Celsius
- Input validation for menu choices and temperatures
- Clear, formatted output with units

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