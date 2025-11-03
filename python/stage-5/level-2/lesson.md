# Level 2: Temperature Converter

## Stage 5: Capstone Project

### Your Project

Build a program that:

1. Displays a menu of conversions
2. Celsius to Fahrenheit: F = (C × 9/5) + 32
3. Fahrenheit to Celsius: C = (F - 32) × 5/9
4. Kelvin conversions
5. Repeats until user quits

---

## ANSWER KEY

```python
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kelvin to Celsius")
    print("4. Quit")

    choice = input("Choose (1-4): ")

    if choice == "4":
        print("Goodbye!")
        break
    elif choice == "1":
        c = float(input("Enter Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(str(c) + "C = " + str(round(f, 2)) + "F")
    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(str(f) + "F = " + str(round(c, 2)) + "C")
    elif choice == "3":
        k = float(input("Enter Kelvin: "))
        c = kelvin_to_celsius(k)
        print(str(k) + "K = " + str(round(c, 2)) + "C")
```

---

**Menu-driven programs with functions!**
