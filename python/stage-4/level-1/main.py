#!/usr/bin/env python3
"""
Temperature Converter
A simple Python program for converting between Celsius and Fahrenheit.
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def get_temperature_input(prompt):
    """Get temperature input from user with validation."""
    while True:
        try:
            temp = float(input(prompt))
            return temp
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def get_menu_choice():
    """Get menu choice from user with validation."""
    while True:
        try:
            choice = int(input("Enter choice (1 or 2): "))
            if choice in [1, 2]:
                return choice
            else:
                print("❌ Please enter 1 or 2.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

def main():
    """Main program function."""
    print("🌡️  Temperature Converter 🌡️")
    print("=" * 30)
    print("What conversion do you want?")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = get_menu_choice()

    if choice == 1:
        # Celsius to Fahrenheit
        celsius = get_temperature_input("Enter temperature in Celsius: ")
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(".1f")
    elif choice == 2:
        # Fahrenheit to Celsius
        fahrenheit = get_temperature_input("Enter temperature in Fahrenheit: ")
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(".1f")
if __name__ == "__main__":
    main()