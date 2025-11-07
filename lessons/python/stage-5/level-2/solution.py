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
