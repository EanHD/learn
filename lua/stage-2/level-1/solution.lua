print("Algorithm 1: Greeting Program")

-- Display "Hello! What's your name?" to the user
io.write("Hello! What's your name? ")
local name = io.read()

-- Display "Nice to meet you, " followed by the user's name
print("Nice to meet you, " .. name)

-- Display "Welcome to programming!"
print("Welcome to programming!")

print() -- Add some spacing

-- Algorithm 2: Simple Calculator
print("Algorithm 2: Simple Calculator")

-- Ask user for first number
io.write("Enter first number: ")
local first_num = tonumber(io.read())

-- Ask user for second number
io.write("Enter second number: ")
local second_num = tonumber(io.read())

-- Calculate sum of the two numbers
local sum = first_num + second_num

-- Display "The sum is: " followed by the sum
print("The sum is: " .. sum)

print() -- Add some spacing

-- Algorithm 3: Age Calculator
print("Algorithm 3: Age Calculator")

-- Display "Enter your age in years: "
io.write("Enter your age in years: ")
local age = tonumber(io.read())

-- Calculate days = age × 365
local days = age * 365

-- Display messages
print("You are approximately " .. days .. " days old")
print("That's a lot of days!")

print() -- Add some spacing

-- Algorithm 4: Temperature Converter
print("Algorithm 4: Temperature Converter")

-- Display "Enter temperature in Celsius: "
io.write("Enter temperature in Celsius: ")
local celsius = tonumber(io.read())

-- Calculate Fahrenheit = (Celsius × 9/5) + 32
local fahrenheit = (celsius * 9/5) + 32

-- Display the results
print(celsius .. "°C = " .. fahrenheit .. "°F")

print() -- Add some spacing

-- Algorithm 5: Rectangle Area Calculator
print("Rectangle Area Calculator")

-- Get length from user
io.write("Enter length: ")
local length = tonumber(io.read())

-- Get width from user
io.write("Enter width: ")
local width = tonumber(io.read())

-- Calculate area = length × width
local area = length * width

-- Calculate perimeter = 2 × (length + width)
local perimeter = 2 * (length + width)

-- Display results
print("Area: " .. area)
print("Perimeter: " .. perimeter)

print() -- Add some spacing

-- Algorithm 6: Simple Interest Calculator
print("Simple Interest Calculator")

-- Get principal from user
io.write("Enter principal amount: $")
local principal = tonumber(io.read())

-- Get rate from user
io.write("Enter interest rate (%): ")
local rate = tonumber(io.read())

-- Get time from user
io.write("Enter time in years: ")
local time = tonumber(io.read())

-- Calculate interest = (principal × rate × time) ÷ 100
local interest = (principal * rate * time) / 100

-- Calculate total = principal + interest
local total = principal + interest

-- Display results
print("Principal: $" .. string.format("%.2f", principal))
print("Interest: $" .. string.format("%.2f", interest))
print("Total: $" .. string.format("%.2f", total))

print() -- Add some spacing

-- Algorithm 7: BMI Calculator
print("BMI Calculator")

-- Get weight from user
io.write("Enter weight in kg: ")
local weight = tonumber(io.read())

-- Get height from user
io.write("Enter height in meters: ")
local height = tonumber(io.read())

-- Calculate bmi = weight ÷ (height × height)
local bmi = weight / (height * height)

-- Display the BMI
print("Your BMI is: " .. string.format("%.2f", bmi))

-- Category determination
if bmi < 18.5 then
    print("Category: Underweight")
elseif bmi < 25 then
    print("Category: Normal weight")
elseif bmi < 30 then
    print("Category: Overweight")
else
    print("Category: Obesity")
end