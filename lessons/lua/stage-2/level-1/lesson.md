# Level 1: Basic Pseudocode Translation

> ** LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.


## Stage 2: Pseudocode to Code

### Today's Mission

Welcome to Stage 2! You've mastered copying code - now it's time to think like a programmer! Today you'll learn to translate written instructions (pseudocode) into working Lua programs. This is where programming becomes creative problem-solving!

---

### Learning Goals

- Understand what pseudocode is and why it's useful
- Learn to read and interpret algorithmic descriptions
- Practice translating simple algorithms into Lua code
- Develop logical thinking for programming
- Create working programs from written instructions

---

### What is Pseudocode?

**Pseudocode** is a way to write programming logic in plain English (or your native language) before writing actual code. It's like writing a recipe or instructions for a task.

**Example:**
```
Algorithm: Make a sandwich
1. Get bread from pantry
2. Get peanut butter from fridge
3. Get jelly from pantry
4. Spread peanut butter on one bread slice
5. Spread jelly on the other bread slice
6. Put slices together
7. Enjoy your sandwich!
```

This is much easier to understand than trying to write code first!

---

### Your Task

**For each pseudocode algorithm below, translate it into working Lua code.**

---


### How to Run

1. **Run the code**:
   ```
   lua hello.lua
   ```

**Expected output:**
```
Hello, World!
```

## Algorithm 1: Greeting Program

**Pseudocode:**
```
Algorithm: Display Personal Greeting
1. Display "Hello! What's your name?" to the user
2. Get the user's name from input
3. Display "Nice to meet you, " followed by the user's name
4. Display "Welcome to programming!"
```

**Your Task:** Create a Lua program that follows these exact steps.

---

## Algorithm 2: Simple Calculator

**Pseudocode:**
```
Algorithm: Add Two Numbers
1. Ask user for first number
2. Get first number from user
3. Ask user for second number
4. Get second number from user
5. Calculate sum of the two numbers
6. Display "The sum is: " followed by the sum
```

**Your Task:** Create a Lua program that implements this calculator.

---

## Algorithm 3: Age Calculator

**Pseudocode:**
```
Algorithm: Calculate Age in Days
1. Display "Enter your age in years: "
2. Get age in years from user
3. Calculate days = age × 365
4. Display "You are approximately " + days + " days old"
5. Display "That's a lot of days!"
```

**Your Task:** Create a program that calculates approximate age in days.

---

## Algorithm 4: Temperature Converter

**Pseudocode:**
```
Algorithm: Celsius to Fahrenheit Converter
1. Display "Enter temperature in Celsius: "
2. Get temperature in Celsius from user
3. Calculate Fahrenheit = (Celsius × 9/5) + 32
4. Display the Celsius temperature
5. Display "°C = "
6. Display the Fahrenheit temperature
7. Display "°F"
```

**Your Task:** Create a temperature conversion program.

---

## Algorithm 5: Rectangle Area Calculator

**Pseudocode:**
```
Algorithm: Calculate Rectangle Area
1. Display "Rectangle Area Calculator"
2. Display "Enter length: "
3. Get length from user
4. Display "Enter width: "
5. Get width from user
6. Calculate area = length × width
7. Calculate perimeter = 2 × (length + width)
8. Display "Area: " + area
9. Display "Perimeter: " + perimeter
```

**Your Task:** Create a program that calculates both area and perimeter.

---

## Algorithm 6: Simple Interest Calculator

**Pseudocode:**
```
Algorithm: Calculate Simple Interest
1. Display "Simple Interest Calculator"
2. Display "Enter principal amount: $"
3. Get principal from user
4. Display "Enter interest rate (%): "
5. Get rate from user
6. Display "Enter time in years: "
7. Get time from user
8. Calculate interest = (principal × rate × time) ÷ 100
9. Calculate total = principal + interest
10. Display "Principal: $" + principal
11. Display "Interest: $" + interest
12. Display "Total: $" + total
```

**Your Task:** Implement the complete interest calculation.

---

## Algorithm 7: BMI Calculator

**Pseudocode:**
```
Algorithm: Calculate Body Mass Index
1. Display "BMI Calculator"
2. Display "Enter weight in kg: "
3. Get weight from user
4. Display "Enter height in meters: "
5. Get height from user
6. Calculate bmi = weight ÷ (height × height)
7. Display "Your BMI is: " + bmi
8. If bmi < 18.5 then
   Display "Category: Underweight"
9. Else if bmi < 25 then
   Display "Category: Normal weight"
10. Else if bmi < 30 then
   Display "Category: Overweight"
11. Else
   Display "Category: Obesity"
```

**Your Task:** Create a program that calculates BMI with categorization.

---

### How to Approach Each Algorithm

**Step-by-Step Process:**

1. **Read Carefully**: Understand what the algorithm does
2. **Identify Inputs**: What information does the user provide?
3. **Identify Outputs**: What should the program display?
4. **Identify Calculations**: What math is needed?
5. **Plan the Code Structure**:
   - Define variables for user input
   - Use appropriate functions for input/output
   - Perform calculations
   - Display results

**Example Planning for Algorithm 1:**
- **Inputs**: User's name (string)
- **Outputs**: Greeting messages
- **No calculations needed**
- **Structure**: Input statement → Output statements

---

### Success Checklist

**For Each Algorithm:**
- [ ] Program executes without errors
- [ ] Program runs and produces expected output
- [ ] Followed the pseudocode steps exactly
- [ ] Used appropriate variable names
- [ ] Included clear output messages

**Overall Progress:**
- [ ] Completed all 7 algorithms
- [ ] All programs work correctly
- [ ] Code is well-organized and readable

---

### Try This (Optional Challenges)

1. **Modify Algorithm 1**: Add a question about favorite color and respond to it
2. **Modify Algorithm 3**: Make the calculation more accurate (account for leap years)
3. **Combine Algorithms**: Create a program that does temperature conversion AND age calculation
4. **Add Validation**: Check if user enters valid numbers (no negative ages, etc.)

---

## Pseudocode Best Practices

### Good Pseudocode
```
Algorithm: Process User Data
1. Get user's name
2. Get user's age
3. If age >= 18 then
   Display "Adult user"
Else
   Display "Minor user"
4. Display "Data processed"
```

### Bad Pseudocode (Too Vague)
```
Algorithm: Do stuff
1. Get things
2. Calculate something
3. Show results
```

### Good Pseudocode (Clear and Specific)
```
Algorithm: Calculate BMI
1. Display "BMI Calculator"
2. Display "Enter weight in kg: "
3. Get weight from user
4. Display "Enter height in meters: "
5. Get height from user
6. Calculate BMI = weight ÷ (height × height)
7. Display "Your BMI is: " + BMI
```

---

<div style="page-break-after: always;"></div>

---

## ANSWER KEY (No peeking until you've tried!)

### Algorithm 1: Greeting Program

```
print("Algorithm 1: Greeting Program")

-- Display "Hello! What's your name?" to the user
io.write("Hello! What's your name? ")
local name = io.read()

-- Display "Nice to meet you, " followed by the user's name
print("Nice to meet you, " .. name)

-- Display "Welcome to programming!"
print("Welcome to programming!")
```

### Algorithm 2: Simple Calculator

```
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
```

### Algorithm 3: Age Calculator

```
print("Algorithm 3: Age Calculator")

-- Display "Enter your age in years: "
io.write("Enter your age in years: ")
local age = tonumber(io.read())

-- Calculate days = age × 365
local days = age * 365

-- Display messages
print("You are approximately " .. days .. " days old")
print("That's a lot of days!")
```

### Algorithm 4: Temperature Converter

```
print("Algorithm 4: Temperature Converter")

-- Display "Enter temperature in Celsius: "
io.write("Enter temperature in Celsius: ")
local celsius = tonumber(io.read())

-- Calculate Fahrenheit = (Celsius × 9/5) + 32
local fahrenheit = (celsius * 9/5) + 32

-- Display the results
print(celsius .. "°C = " .. fahrenheit .. "°F")
```

### Algorithm 5: Rectangle Area Calculator

```
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
```

### Algorithm 6: Simple Interest Calculator

```
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
```

### Algorithm 7: BMI Calculator

```
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
```

### Common Translation Patterns

| Pseudocode Pattern | Lua Equivalent |
|-------------------|----------------|
| `Display message` | `print(message)` or `io.write(message)` |
| `Get variable from user` | `io.read()` |
| `Calculate result = a + b` | `result = a + b` |
| `If condition then` | `if condition then` |
| `Else if` | `elseif condition then` |
| `Else` | `else` |

### Debugging Tips

**"Program doesn't run":**
- Check syntax errors like missing `end` statements
- Verify variable declarations
- Ensure proper use of `then` and `end`

**"Wrong output":**
- Check variable names match (case-sensitive)
- Verify data types match usage
- Check mathematical formulas

**"Input not working":**
- Use `tonumber(io.read())` for numeric input
- Use `io.read()` for string input
- Use `io.write()` without newline for prompts

### Variable Naming Best Practices

**Good Names:**
- `user_age` (clear what it stores)
- `temperature_celsius` (descriptive)
- `rectangle_area` (specific purpose)

**Bad Names:**
- `x` (too vague)
- `temp` (unclear what kind of temperature)
- `var1` (meaningless)

### Input/Output Patterns

**Getting Numbers:**
```
io.write("Enter age: ")
local age = tonumber(io.read())
```

**Getting Text:**
```
io.write("Enter name: ")
local name = io.read()
```

**Displaying Results:**
```
print("Result: " .. result)
print("Price: $" .. string.format("%.2f", price))
print("Hello, " .. name .. "!")
```

---

 **Congratulations! You've translated your first pseudocode algorithms into working Lua programs!**

*This is a major milestone - you're now thinking like a programmer! Next up: Variables in pseudocode!*


### Additional Content

Understand the key concepts:

- Review each function
- Understand the flow
- Learn the patterns used


### Code Review

Key functions and their purpose:

- Main function: Entry point
- Helper functions: Support logic
