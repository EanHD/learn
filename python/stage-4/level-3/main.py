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